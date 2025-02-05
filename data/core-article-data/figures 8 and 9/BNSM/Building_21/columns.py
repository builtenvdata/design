import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1, 27822730.79933828, 11592804.49972428, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 61.62775704, 0.00135363, 74.5471247, 0.01547468, 7.45471247, 0.0481134, -61.62775704, -0.00135363, -74.5471247, -0.01547468, -7.45471247, -0.0481134, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 91.21955105, 0.00089211, 110.3424102, 0.01729167, 11.03424102, 0.06383276, -91.21955105, -0.00089211, -110.3424102, -0.01729167, -11.03424102, -0.06383276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 108.93161499, 0.02707269, 108.93161499, 0.08121808, 76.25213049, -1236.65077677, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 27.23290375, 9.162e-05, 81.69871124, 0.00027485, 272.32903747, 0.00091616, -27.23290375, -9.162e-05, -81.69871124, -0.00027485, -272.32903747, -0.00091616, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 134.81558129, 0.01784222, 134.81558129, 0.05352666, 94.37090691, -2077.88771809, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 33.70389532, 0.00011339, 101.11168597, 0.00034016, 337.03895324, 0.00113385, -33.70389532, -0.00011339, -101.11168597, -0.00034016, -337.03895324, -0.00113385, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.45, 0.0, 0.0)
    ops.node(121002, 4.45, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.2275, 29604556.89257659, 12335232.03857358, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 265.53169985, 0.00100549, 321.13467928, 0.03518031, 32.11346793, 0.08684335, -265.53169985, -0.00100549, -321.13467928, -0.03518031, -32.11346793, -0.08684335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 387.1216769, 0.00067453, 468.18589127, 0.04323492, 46.81858913, 0.13017873, -387.1216769, -0.00067453, -468.18589127, -0.04323492, -46.81858913, -0.13017873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 298.53369935, 0.02010972, 298.53369935, 0.06032917, 208.97358954, -4598.74795861, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 74.63342484, 0.00010372, 223.90027451, 0.00031116, 746.33424837, 0.00103722, -74.63342484, -0.00010372, -223.90027451, -0.00031116, -746.33424837, -0.00103722, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 466.13441053, 0.01349069, 466.13441053, 0.04047208, 326.29408737, -11178.76444619, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 116.53360263, 0.00016195, 349.6008079, 0.00048586, 1165.33602632, 0.00161952, -116.53360263, -0.00016195, -349.6008079, -0.00048586, -1165.33602632, -0.00161952, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.9, 0.0, 0.0)
    ops.node(121003, 8.9, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.2275, 29350185.11536952, 12229243.79807063, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 267.47699797, 0.00101143, 323.64791191, 0.03523624, 32.36479119, 0.08655681, -267.47699797, -0.00101143, -323.64791191, -0.03523624, -32.36479119, -0.08655681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 389.00570574, 0.00067834, 470.69798652, 0.04330099, 47.06979865, 0.12966845, -389.00570574, -0.00067834, -470.69798652, -0.04330099, -47.06979865, -0.12966845, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 301.08221052, 0.02022857, 301.08221052, 0.0606857, 210.75754737, -4777.31192849, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 75.27055263, 0.00010551, 225.81165789, 0.00031654, 752.70552631, 0.00105514, -75.27055263, -0.00010551, -225.81165789, -0.00031654, -752.70552631, -0.00105514, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 471.87313474, 0.01356682, 471.87313474, 0.04070045, 330.31119432, -11696.73624704, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 117.96828369, 0.00016537, 353.90485106, 0.0004961, 1179.68283686, 0.00165367, -117.96828369, -0.00016537, -353.90485106, -0.0004961, -1179.68283686, -0.00165367, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 20.8, 0.0, 0.0)
    ops.node(121006, 20.8, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.2275, 29316645.48374938, 12215268.95156224, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 267.21971182, 0.00102231, 323.35720209, 0.03517637, 32.33572021, 0.08645099, -267.21971182, -0.00102231, -323.35720209, -0.03517637, -32.33572021, -0.08645099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 390.08863648, 0.00068267, 472.03841813, 0.0432172, 47.20384181, 0.12950734, -390.08863648, -0.00068267, -472.03841813, -0.0432172, -47.20384181, -0.12950734, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 298.33009174, 0.02044622, 298.33009174, 0.06133867, 208.83106422, -4671.91379697, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 74.58252294, 0.00010467, 223.74756881, 0.00031401, 745.82522936, 0.00104669, -74.58252294, -0.00010467, -223.74756881, -0.00031401, -745.82522936, -0.00104669, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 466.89429546, 0.0136535, 466.89429546, 0.04096049, 326.82600682, -11390.77537106, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 116.72357386, 0.00016381, 350.17072159, 0.00049143, 1167.23573864, 0.00163809, -116.72357386, -0.00016381, -350.17072159, -0.00049143, -1167.23573864, -0.00163809, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 25.25, 0.0, 0.0)
    ops.node(121007, 25.25, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.2275, 29108038.54940441, 12128349.39558517, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 260.17688277, 0.00102334, 314.95680682, 0.03557532, 31.49568068, 0.08655994, -260.17688277, -0.00102334, -314.95680682, -0.03557532, -31.49568068, -0.08655994, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 383.5498014, 0.0006793, 464.30574239, 0.04370939, 46.43057424, 0.12951149, -383.5498014, -0.0006793, -464.30574239, -0.04370939, -46.43057424, -0.12951149, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 299.89290385, 0.02046673, 299.89290385, 0.06140018, 209.9250327, -4796.71873114, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 74.97322596, 0.00010597, 224.91967789, 0.00031791, 749.73225963, 0.00105971, -74.97322596, -0.00010597, -224.91967789, -0.00031791, -749.73225963, -0.00105971, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 470.61717949, 0.01358602, 470.61717949, 0.04075807, 329.43202564, -11753.14183081, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 117.65429487, 0.0001663, 352.96288462, 0.0004989, 1176.54294873, 0.00166299, -117.65429487, -0.0001663, -352.96288462, -0.0004989, -1176.54294873, -0.00166299, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 29.7, 0.0, 0.0)
    ops.node(121008, 29.7, 0.0, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1, 28772788.93017679, 11988662.05424033, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 62.2482385, 0.00137729, 75.21100705, 0.01500024, 7.52110071, 0.04891979, -62.2482385, -0.00137729, -75.21100705, -0.01500024, -7.52110071, -0.04891979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 92.43792071, 0.00090298, 111.68748344, 0.01672407, 11.16874834, 0.06509157, -92.43792071, -0.00090298, -111.68748344, -0.01672407, -11.16874834, -0.06509157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 109.85630708, 0.02754581, 109.85630708, 0.08263744, 76.89941496, -1182.92304524, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 27.46407677, 8.934e-05, 82.39223031, 0.00026803, 274.64076771, 0.00089343, -27.46407677, -8.934e-05, -82.39223031, -0.00026803, -274.64076771, -0.00089343, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 134.58881944, 0.01805967, 134.58881944, 0.05417902, 94.21217361, -1966.74667858, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 33.64720486, 0.00010946, 100.94161458, 0.00032837, 336.47204861, 0.00109457, -33.64720486, -0.00010946, -100.94161458, -0.00032837, -336.47204861, -0.00109457, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 5.15, 0.0)
    ops.node(121009, 0.0, 5.15, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.245, 29763744.8946366, 12401560.37276525, 0.00686927, 0.00275115, 0.01100458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 378.25440753, 0.00064159, 457.46885284, 0.03155522, 45.74688528, 0.09385367, -378.25440753, -0.00064159, -457.46885284, -0.03155522, -45.74688528, -0.09385367, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 228.217391, 0.00098462, 276.01092276, 0.02569831, 27.60109228, 0.06233198, -228.217391, -0.00098462, -276.01092276, -0.02569831, -27.60109228, -0.06233198, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 428.0518954, 0.01283182, 428.0518954, 0.03849547, 299.63632678, -7101.1472484, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 107.01297385, 0.00013736, 321.03892155, 0.00041208, 1070.12973849, 0.00137359, -107.01297385, -0.00013736, -321.03892155, -0.00041208, -1070.12973849, -0.00137359, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 265.11851554, 0.01969233, 265.11851554, 0.05907699, 185.58296088, -2925.79908371, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 66.27962889, 8.508e-05, 198.83888666, 0.00025523, 662.79628886, 0.00085075, -66.27962889, -8.508e-05, -198.83888666, -0.00025523, -662.79628886, -0.00085075, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 4.45, 5.15, 0.0)
    ops.node(121010, 4.45, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.4275, 29032683.72199382, 12096951.55083076, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 1122.53117714, 0.00060456, 1361.14781775, 0.04375835, 136.11478178, 0.11582628, -1122.53117714, -0.00060456, -1361.14781775, -0.04375835, -136.11478178, -0.11582628, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 740.04001385, 0.00086299, 897.35044373, 0.03918202, 89.73504437, 0.09354853, -740.04001385, -0.00086299, -897.35044373, -0.03918202, -89.73504437, -0.09354853, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 1118.96945121, 0.01209125, 1118.96945121, 0.03627375, 783.27861585, -32606.8337544, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 279.7423628, 0.00021097, 839.22708841, 0.0006329, 2797.42362803, 0.00210965, -279.7423628, -0.00021097, -839.22708841, -0.0006329, -2797.42362803, -0.00210965, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 463.45493381, 0.01725988, 463.45493381, 0.05177964, 324.41845367, -5921.94663473, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 115.86373345, 8.738e-05, 347.59120036, 0.00026213, 1158.63733453, 0.00087378, -115.86373345, -8.738e-05, -347.59120036, -0.00026213, -1158.63733453, -0.00087378, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.9, 5.15, 0.0)
    ops.node(121011, 8.9, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.4275, 28948284.03663175, 12061785.01526323, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 1133.26760006, 0.00061283, 1374.39320558, 0.04360672, 137.43932056, 0.11553596, -1133.26760006, -0.00061283, -1374.39320558, -0.04360672, -137.43932056, -0.11553596, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 739.73981569, 0.00088529, 897.13442486, 0.03906234, 89.71344249, 0.09332422, -739.73981569, -0.00088529, -897.13442486, -0.03906234, -89.71344249, -0.09332422, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 1106.75682064, 0.01225656, 1106.75682064, 0.03676967, 774.72977445, -31705.34168764, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 276.68920516, 0.00020927, 830.06761548, 0.00062781, 2766.8920516, 0.00209271, -276.68920516, -0.00020927, -830.06761548, -0.00062781, -2766.8920516, -0.00209271, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 459.16221212, 0.01770585, 459.16221212, 0.05311756, 321.41354849, -5800.40497527, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 114.79055303, 8.682e-05, 344.37165909, 0.00026046, 1147.90553031, 0.00086821, -114.79055303, -8.682e-05, -344.37165909, -0.00026046, -1147.90553031, -0.00086821, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.35, 5.15, 0.0)
    ops.node(121012, 13.35, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.32, 29768114.55131588, 12403381.06304828, 0.01171867, 0.00469333, 0.01877333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 670.68551922, 0.00064121, 811.27188252, 0.04359604, 81.12718825, 0.12245659, -670.68551922, -0.00064121, -811.27188252, -0.04359604, -81.12718825, -0.12245659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 418.25198006, 0.00095733, 505.92425438, 0.03481931, 50.59242544, 0.07967561, -418.25198006, -0.00095733, -505.92425438, -0.03481931, -50.59242544, -0.07967561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 670.20397673, 0.01282411, 670.20397673, 0.03847232, 469.14278371, -13335.47826947, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 167.55099418, 0.00016463, 502.65298255, 0.0004939, 1675.50994183, 0.00164635, -167.55099418, -0.00016463, -502.65298255, -0.0004939, -1675.50994183, -0.00164635, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 380.4883593, 0.01914656, 380.4883593, 0.05743967, 266.34185151, -5075.28607378, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 95.12208983, 9.347e-05, 285.36626948, 0.0002804, 951.22089825, 0.00093466, -95.12208983, -9.347e-05, -285.36626948, -0.0002804, -951.22089825, -0.00093466, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 16.35, 5.15, 0.0)
    ops.node(121013, 16.35, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.32, 29558680.10729924, 12316116.71137469, 0.01171867, 0.00469333, 0.01877333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 677.23226852, 0.00064317, 819.5468754, 0.04348878, 81.95468754, 0.1219585, -677.23226852, -0.00064317, -819.5468754, -0.04348878, -81.95468754, -0.1219585, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 426.67746932, 0.00095459, 516.34011409, 0.03473048, 51.63401141, 0.07936447, -426.67746932, -0.00095459, -516.34011409, -0.03473048, -51.63401141, -0.07936447, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 667.23378567, 0.01286334, 667.23378567, 0.03859003, 467.06364997, -13348.35169995, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 166.80844642, 0.00016507, 500.42533925, 0.0004952, 1668.08446418, 0.00165066, -166.80844642, -0.00016507, -500.42533925, -0.0004952, -1668.08446418, -0.00165066, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 378.57468306, 0.01909185, 378.57468306, 0.05727556, 265.00227814, -5079.25680424, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 94.64367076, 9.366e-05, 283.93101229, 0.00028097, 946.43670764, 0.00093655, -94.64367076, -9.366e-05, -283.93101229, -0.00028097, -946.43670764, -0.00093655, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 20.8, 5.15, 0.0)
    ops.node(121014, 20.8, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.4275, 28532222.42798179, 11888426.01165908, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 1131.10039729, 0.0006131, 1372.83305064, 0.04343442, 137.28330506, 0.1146578, -1131.10039729, -0.0006131, -1372.83305064, -0.04343442, -137.28330506, -0.1146578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 742.07510172, 0.00088393, 900.66737501, 0.03890774, 90.0667375, 0.09263713, -742.07510172, -0.00088393, -900.66737501, -0.03890774, -90.0667375, -0.09263713, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 1087.58834285, 0.01226196, 1087.58834285, 0.03678589, 761.31184, -30887.99160148, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 271.89708571, 0.00020865, 815.69125714, 0.00062594, 2718.97085713, 0.00208645, -271.89708571, -0.00020865, -815.69125714, -0.00062594, -2718.97085713, -0.00208645, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 450.97030321, 0.01767867, 450.97030321, 0.05303601, 315.67921225, -5689.81642897, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 112.7425758, 8.652e-05, 338.22772741, 0.00025955, 1127.42575804, 0.00086515, -112.7425758, -8.652e-05, -338.22772741, -0.00025955, -1127.42575804, -0.00086515, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 25.25, 5.15, 0.0)
    ops.node(121015, 25.25, 5.15, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.4275, 29524053.25041422, 12301688.85433926, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 1129.71259019, 0.00060813, 1368.47652209, 0.04345617, 136.84765221, 0.11630285, -1129.71259019, -0.00060813, -1368.47652209, -0.04345617, -136.84765221, -0.11630285, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 736.11287978, 0.0008755, 891.68979998, 0.03892303, 89.16898, 0.09387702, -736.11287978, -0.0008755, -891.68979998, -0.03892303, -89.16898, -0.09387702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 1114.6930259, 0.01216256, 1114.6930259, 0.03648767, 780.28511813, -31205.12232294, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 278.67325648, 0.00020666, 836.01976943, 0.00061998, 2786.73256475, 0.00206661, -278.67325648, -0.00020666, -836.01976943, -0.00061998, -2786.73256475, -0.00206661, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 464.65853233, 0.01751, 464.65853233, 0.05253001, 325.26097263, -5732.76978638, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 116.16463308, 8.615e-05, 348.49389925, 0.00025844, 1161.64633084, 0.00086147, -116.16463308, -8.615e-05, -348.49389925, -0.00025844, -1161.64633084, -0.00086147, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 29.7, 5.15, 0.0)
    ops.node(121016, 29.7, 5.15, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.245, 28709464.04057002, 11962276.68357084, 0.00686927, 0.00275115, 0.01100458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 376.8683796, 0.00064606, 456.70937093, 0.03132047, 45.67093709, 0.09194048, -376.8683796, -0.00064606, -456.70937093, -0.03132047, -45.67093709, -0.09194048, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 227.72597942, 0.00099412, 275.97058929, 0.02551657, 27.59705893, 0.06116326, -227.72597942, -0.00099412, -275.97058929, -0.02551657, -27.59705893, -0.06116326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 412.29063645, 0.01292118, 412.29063645, 0.03876355, 288.60344551, -6845.18191125, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 103.07265911, 0.00013716, 309.21797734, 0.00041148, 1030.72659112, 0.0013716, -103.07265911, -0.00013716, -309.21797734, -0.00041148, -1030.72659112, -0.0013716, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 254.83773442, 0.01988245, 254.83773442, 0.05964735, 178.38641409, -2843.4821288, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 63.7094336, 8.478e-05, 191.12830081, 0.00025434, 637.09433604, 0.00084779, -63.7094336, -8.478e-05, -191.12830081, -0.00025434, -637.09433604, -0.00084779, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 10.3, 0.0)
    ops.node(121017, 0.0, 10.3, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.1, 30201579.21782729, 12583991.34076137, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 63.39162562, 0.00130989, 76.40746958, 0.01555207, 7.64074696, 0.05115679, -63.39162562, -0.00130989, -76.40746958, -0.01555207, -7.64074696, -0.05115679, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 93.2423724, 0.00087482, 112.38730136, 0.01741506, 11.23873014, 0.06818551, -93.2423724, -0.00087482, -112.38730136, -0.01741506, -11.23873014, -0.06818551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 115.85507076, 0.02619788, 115.85507076, 0.07859364, 81.09854953, -1228.35945849, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 28.96376769, 8.976e-05, 86.89130307, 0.00026929, 289.63767691, 0.00089764, -28.96376769, -8.976e-05, -86.89130307, -0.00026929, -289.63767691, -0.00089764, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 141.56299942, 0.0174965, 141.56299942, 0.05248949, 99.09409959, -2060.69835128, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 35.39074985, 0.00010968, 106.17224956, 0.00032905, 353.90749854, 0.00109682, -35.39074985, -0.00010968, -106.17224956, -0.00032905, -353.90749854, -0.00109682, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 4.45, 10.3, 0.0)
    ops.node(121018, 4.45, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.2275, 30441083.63528915, 12683784.84803715, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 291.39694924, 0.00100358, 351.78544659, 0.03573117, 35.17854466, 0.08844923, -291.39694924, -0.00100358, -351.78544659, -0.03573117, -35.17854466, -0.08844923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 414.58106843, 0.00067396, 500.49798627, 0.04392275, 50.04979863, 0.13264205, -414.58106843, -0.00067396, -500.49798627, -0.04392275, -50.04979863, -0.13264205, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 309.00044837, 0.02007155, 309.00044837, 0.06021464, 216.30031386, -4793.41972578, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 77.25011209, 0.00010441, 231.75033628, 0.00031322, 772.50112093, 0.00104408, -77.25011209, -0.00010441, -231.75033628, -0.00031322, -772.50112093, -0.00104408, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 482.22959587, 0.01347918, 482.22959587, 0.04043754, 337.56071711, -11743.55181619, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 120.55739897, 0.00016294, 361.6721969, 0.00048882, 1205.57398968, 0.0016294, -120.55739897, -0.00016294, -361.6721969, -0.00048882, -1205.57398968, -0.0016294, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.9, 10.3, 0.0)
    ops.node(121019, 8.9, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.2275, 29481137.17334965, 12283807.15556235, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 267.73180062, 0.00105409, 323.87438869, 0.03690564, 32.38743887, 0.08840382, -267.73180062, -0.00105409, -323.87438869, -0.03690564, -32.38743887, -0.08840382, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 418.41113217, 0.00069626, 506.15074242, 0.04534479, 50.61507424, 0.13201117, -418.41113217, -0.00069626, -506.15074242, -0.04534479, -50.61507424, -0.13201117, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 299.44560961, 0.02108176, 299.44560961, 0.06324527, 209.61192673, -4671.51251405, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 74.8614024, 0.00010447, 224.58420721, 0.00031342, 748.61402402, 0.00104474, -74.8614024, -0.00010447, -224.58420721, -0.00031342, -748.61402402, -0.00104474, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 468.31658319, 0.01392518, 468.31658319, 0.04177555, 327.82160823, -11389.61171815, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 117.0791458, 0.00016339, 351.23743739, 0.00049017, 1170.79145797, 0.00163392, -117.0791458, -0.00016339, -351.23743739, -0.00049017, -1170.79145797, -0.00163392, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 13.35, 10.3, 0.0)
    ops.node(121020, 13.35, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1925, 30412020.66071639, 12671675.27529849, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 170.32191909, 0.00094282, 205.6533288, 0.02338353, 20.56533288, 0.06735906, -170.32191909, -0.00094282, -205.6533288, -0.02338353, -20.56533288, -0.06735906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 214.80139975, 0.00070061, 259.35958874, 0.02678322, 25.93595887, 0.08960976, -214.80139975, -0.00070061, -259.35958874, -0.02678322, -25.93595887, -0.08960976, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 231.29592939, 0.0188564, 231.29592939, 0.05656921, 161.90715057, -2913.8986146, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 57.82398235, 9.245e-05, 173.47194704, 0.00027735, 578.23982347, 0.0009245, -57.82398235, -9.245e-05, -173.47194704, -0.00027735, -578.23982347, -0.0009245, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 298.13061607, 0.01401211, 298.13061607, 0.04203632, 208.69143125, -5259.39206993, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 74.53265402, 0.00011916, 223.59796205, 0.00035749, 745.32654018, 0.00119164, -74.53265402, -0.00011916, -223.59796205, -0.00035749, -745.32654018, -0.00119164, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 16.35, 10.3, 0.0)
    ops.node(121021, 16.35, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1925, 28274496.97854435, 11781040.40772681, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 171.25489132, 0.00096159, 207.62750285, 0.02360706, 20.76275029, 0.06516808, -171.25489132, -0.00096159, -207.62750285, -0.02360706, -20.76275029, -0.06516808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 214.58100432, 0.00071314, 260.15559465, 0.02703375, 26.01555946, 0.08641075, -214.58100432, -0.00071314, -260.15559465, -0.02703375, -26.01555946, -0.08641075, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 220.25332704, 0.01923179, 220.25332704, 0.05769536, 154.17732893, -2961.0173615, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 55.06333176, 9.469e-05, 165.18999528, 0.00028408, 550.63331761, 0.00094692, -55.06333176, -9.469e-05, -165.18999528, -0.00028408, -550.63331761, -0.00094692, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 286.808584, 0.01426287, 286.808584, 0.04278862, 200.7660088, -5358.93589752, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 71.702146, 0.00012331, 215.106438, 0.00036992, 717.02146, 0.00123305, -71.702146, -0.00012331, -215.106438, -0.00036992, -717.02146, -0.00123305, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 20.8, 10.3, 0.0)
    ops.node(121022, 20.8, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.2275, 29505554.99546578, 12293981.24811074, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 269.07935914, 0.00103892, 325.48897446, 0.0369291, 32.54889745, 0.0884601, -269.07935914, -0.00103892, -325.48897446, -0.0369291, -32.54889745, -0.0884601, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 418.01241429, 0.00069087, 505.64425482, 0.04538752, 50.56442548, 0.13210912, -418.01241429, -0.00069087, -505.64425482, -0.04538752, -50.56442548, -0.13210912, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 305.5451238, 0.02077837, 305.5451238, 0.0623351, 213.88158666, -4921.18649592, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 76.38628095, 0.00010651, 229.15884285, 0.00031954, 763.8628095, 0.00106514, -76.38628095, -0.00010651, -229.15884285, -0.00031954, -763.8628095, -0.00106514, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 479.54767503, 0.01381737, 479.54767503, 0.04145211, 335.68337252, -12115.40590799, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 119.88691876, 0.00016717, 359.66075628, 0.00050151, 1198.86918758, 0.00167172, -119.88691876, -0.00016717, -359.66075628, -0.00050151, -1198.86918758, -0.00167172, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 25.25, 10.3, 0.0)
    ops.node(121023, 25.25, 10.3, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2275, 28186091.72620538, 11744204.88591891, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 297.59720764, 0.00105872, 360.80519452, 0.03563662, 36.08051945, 0.08524777, -297.59720764, -0.00105872, -360.80519452, -0.03563662, -36.08051945, -0.08524777, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 421.67517902, 0.00070236, 511.2366349, 0.04376472, 51.12366349, 0.12725541, -421.67517902, -0.00070236, -511.2366349, -0.04376472, -51.12366349, -0.12725541, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 290.03311676, 0.02117449, 290.03311676, 0.06352346, 203.02318173, -4644.43464166, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 72.50827919, 0.00010584, 217.52483757, 0.00031752, 725.0827919, 0.00105839, -72.50827919, -0.00010584, -217.52483757, -0.00031752, -725.0827919, -0.00105839, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 455.89183714, 0.01404724, 455.89183714, 0.04214173, 319.124286, -11311.11237806, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 113.97295928, 0.00016636, 341.91887785, 0.00049909, 1139.72959284, 0.00166365, -113.97295928, -0.00016636, -341.91887785, -0.00049909, -1139.72959284, -0.00166365, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 29.7, 10.3, 0.0)
    ops.node(121024, 29.7, 10.3, 3.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1, 29334061.25741038, 12222525.52392099, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 64.80443469, 0.00133217, 78.23262455, 0.01496047, 7.82326246, 0.04957465, -64.80443469, -0.00133217, -78.23262455, -0.01496047, -7.82326246, -0.04957465, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 94.78995095, 0.0008922, 114.43146875, 0.0167195, 11.44314688, 0.0660775, -94.78995095, -0.0008922, -114.43146875, -0.0167195, -11.44314688, -0.0660775, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 111.64910206, 0.02664342, 111.64910206, 0.07993026, 78.15437144, -1185.38055052, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 27.91227551, 8.906e-05, 83.73682654, 0.00026719, 279.12275514, 0.00089063, -27.91227551, -8.906e-05, -83.73682654, -0.00026719, -279.12275514, -0.00089063, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 136.43484566, 0.01784406, 136.43484566, 0.05353218, 95.50439196, -1971.81734076, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 34.10871141, 0.00010884, 102.32613424, 0.00032651, 341.08711414, 0.00108835, -34.10871141, -0.00010884, -102.32613424, -0.00032651, -341.08711414, -0.00108835, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.5)
    ops.node(122001, 0.0, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1, 28364455.65409087, 11818523.18920453, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 44.49477972, 0.00114753, 53.96220706, 0.0156928, 5.39622071, 0.05242369, -44.49477972, -0.00114753, -53.96220706, -0.0156928, -5.39622071, -0.05242369, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 80.72869551, 0.00078926, 97.90583548, 0.01768149, 9.79058355, 0.07005782, -80.72869551, -0.00078926, -97.90583548, -0.01768149, -9.79058355, -0.07005782, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 105.63574349, 0.02295059, 105.63574349, 0.06885177, 73.94502045, -1516.85574893, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 26.40893587, 7.24e-05, 79.22680762, 0.0002172, 264.08935873, 0.00072399, -26.40893587, -7.24e-05, -79.22680762, -0.0002172, -264.08935873, -0.00072399, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 131.43042113, 0.01578518, 131.43042113, 0.04735554, 92.00129479, -2742.76828809, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 32.85760528, 9.008e-05, 98.57281584, 0.00027023, 328.57605281, 0.00090078, -32.85760528, -9.008e-05, -98.57281584, -0.00027023, -328.57605281, -0.00090078, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.45, 0.0, 3.525)
    ops.node(122002, 4.45, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.2275, 28502347.76707625, 11875978.23628177, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 131.11601517, 0.00087643, 159.27034741, 0.01731622, 15.92703474, 0.04570061, -131.11601517, -0.00087643, -159.27034741, -0.01731622, -15.92703474, -0.04570061, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 296.53827656, 0.00062324, 360.21346642, 0.02018762, 36.02134664, 0.06307587, -296.53827656, -0.00062324, -360.21346642, -0.02018762, -36.02134664, -0.06307587, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 195.22779267, 0.01752861, 195.22779267, 0.05258582, 136.65945487, -2019.34393841, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 48.80694817, 5.853e-05, 146.4208445, 0.00017559, 488.06948168, 0.0005853, -48.80694817, -5.853e-05, -146.4208445, -0.00017559, -488.06948168, -0.0005853, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 319.30634981, 0.01246473, 319.30634981, 0.0373942, 223.51444487, -4174.63048223, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 79.82658745, 9.573e-05, 239.47976236, 0.00028719, 798.26587452, 0.00095729, -79.82658745, -9.573e-05, -239.47976236, -0.00028719, -798.26587452, -0.00095729, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.9, 0.0, 3.525)
    ops.node(122003, 8.9, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.2275, 29711434.97458602, 12379764.57274417, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 131.45990437, 0.00086908, 159.28768565, 0.01731008, 15.92876857, 0.04638843, -131.45990437, -0.00086908, -159.28768565, -0.01731008, -15.92876857, -0.04638843, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 296.81882032, 0.00061896, 359.65021559, 0.02018478, 35.96502156, 0.06412158, -296.81882032, -0.00061896, -359.65021559, -0.02018478, -35.96502156, -0.06412158, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 204.12857751, 0.01738168, 204.12857751, 0.05214504, 142.89000426, -2047.37954042, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 51.03214438, 5.871e-05, 153.09643313, 0.00017612, 510.32144378, 0.00058708, -51.03214438, -5.871e-05, -153.09643313, -0.00017612, -510.32144378, -0.00058708, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 333.27085382, 0.01237913, 333.27085382, 0.03713738, 233.28959767, -4249.56733325, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 83.31771345, 9.585e-05, 249.95314036, 0.00028755, 833.17713455, 0.00095849, -83.31771345, -9.585e-05, -249.95314036, -0.00028755, -833.17713455, -0.00095849, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 20.8, 0.0, 3.525)
    ops.node(122006, 20.8, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.2275, 28835944.71810736, 12014976.96587807, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 131.97092732, 0.00087611, 160.20533207, 0.01759705, 16.02053321, 0.04618385, -131.97092732, -0.00087611, -160.20533207, -0.01759705, -16.02053321, -0.04618385, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 298.44343856, 0.00062375, 362.29365928, 0.02052272, 36.22936593, 0.06371681, -298.44343856, -0.00062375, -362.29365928, -0.02052272, -36.22936593, -0.06371681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 199.09809484, 0.01752214, 199.09809484, 0.05256643, 139.36866639, -2078.07419882, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 49.77452371, 5.9e-05, 149.32357113, 0.000177, 497.7452371, 0.00058999, -49.77452371, -5.9e-05, -149.32357113, -0.000177, -497.7452371, -0.00058999, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 325.79270393, 0.01247494, 325.79270393, 0.03742482, 228.05489275, -4331.78176575, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 81.44817598, 9.654e-05, 244.34452795, 0.00028963, 814.48175983, 0.00096543, -81.44817598, -9.654e-05, -244.34452795, -0.00028963, -814.48175983, -0.00096543, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 25.25, 0.0, 3.525)
    ops.node(122007, 25.25, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.2275, 28414397.05274494, 11839332.10531039, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 132.73503132, 0.00087775, 161.2634986, 0.01734575, 16.12634986, 0.04567531, -132.73503132, -0.00087775, -161.2634986, -0.01734575, -16.12634986, -0.04567531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 300.46361483, 0.00062614, 365.04164159, 0.02022409, 36.50416416, 0.06302948, -300.46361483, -0.00062614, -365.04164159, -0.02022409, -36.50416416, -0.06302948, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 196.41441513, 0.01755508, 196.41441513, 0.05266523, 137.49009059, -2082.18083991, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 49.10360378, 5.907e-05, 147.31081135, 0.0001772, 491.03603783, 0.00059068, -49.10360378, -5.907e-05, -147.31081135, -0.0001772, -491.03603783, -0.00059068, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 321.69415664, 0.0125228, 321.69415664, 0.0375684, 225.18590965, -4342.79452598, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 80.42353916, 9.674e-05, 241.27061748, 0.00029023, 804.23539161, 0.00096743, -80.42353916, -9.674e-05, -241.27061748, -0.00029023, -804.23539161, -0.00096743, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 29.7, 0.0, 3.5)
    ops.node(122008, 29.7, 0.0, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1, 28819413.93867648, 12008089.1411152, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 44.56908673, 0.00114392, 54.01055526, 0.01545779, 5.40105553, 0.05265731, -44.56908673, -0.00114392, -54.01055526, -0.01545779, -5.40105553, -0.05265731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 80.82554251, 0.00078707, 97.94754058, 0.01741056, 9.79475406, 0.07045512, -80.82554251, -0.00078707, -97.94754058, -0.01741056, -9.79475406, -0.07045512, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 106.26127727, 0.02287842, 106.26127727, 0.06863527, 74.38289409, -1487.97985432, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 26.56531932, 7.168e-05, 79.69595795, 0.00021503, 265.65319317, 0.00071678, -26.56531932, -7.168e-05, -79.69595795, -0.00021503, -265.65319317, -0.00071678, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 131.62652262, 0.01574143, 131.62652262, 0.0472243, 92.13856583, -2680.69832877, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 32.90663066, 8.879e-05, 98.71989197, 0.00026636, 329.06630655, 0.00088788, -32.90663066, -8.879e-05, -98.71989197, -0.00026636, -329.06630655, -0.00088788, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 5.15, 3.5)
    ops.node(122009, 0.0, 5.15, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.245, 29154531.46772906, 12147721.44488711, 0.00686927, 0.00275115, 0.01100458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 338.87483273, 0.00060253, 411.21746486, 0.02450881, 41.12174649, 0.07640152, -338.87483273, -0.00060253, -411.21746486, -0.02450881, -41.12174649, -0.07640152, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 137.21505391, 0.00086326, 166.50757494, 0.02030285, 16.65075749, 0.05207402, -137.21505391, -0.00086326, -166.50757494, -0.02030285, -16.65075749, -0.05207402, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 391.85070592, 0.01205053, 391.85070592, 0.03615159, 274.29549414, -5950.1468138, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 97.96267648, 0.00010665, 293.88802944, 0.00031994, 979.62676479, 0.00106646, -97.96267648, -0.00010665, -293.88802944, -0.00031994, -979.62676479, -0.00106646, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 221.60847958, 0.01726515, 221.60847958, 0.05179545, 155.12593571, -2471.11466089, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 55.40211989, 6.031e-05, 166.20635968, 0.00018094, 554.02119895, 0.00060313, -55.40211989, -6.031e-05, -166.20635968, -0.00018094, -554.02119895, -0.00060313, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 4.45, 5.15, 3.525)
    ops.node(122010, 4.45, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.4275, 29422481.4410108, 12259367.26708784, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 751.11521162, 0.00056673, 911.61953928, 0.03185631, 91.16195393, 0.08672909, -751.11521162, -0.00056673, -911.61953928, -0.03185631, -91.16195393, -0.08672909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 283.65113706, 0.00073862, 344.2639889, 0.02576116, 34.42639889, 0.05805367, -283.65113706, -0.00073862, -344.2639889, -0.02576116, -34.42639889, -0.05805367, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 788.25704041, 0.01133462, 788.25704041, 0.03400386, 551.77992829, -12504.6421894, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 197.0642601, 0.00012183, 591.19278031, 0.00036549, 1970.64260102, 0.00121828, -197.0642601, -0.00012183, -591.19278031, -0.00036549, -1970.64260102, -0.00121828, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 404.44601936, 0.01477236, 404.44601936, 0.04431708, 283.11221355, -4534.2606182, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 101.11150484, 6.251e-05, 303.33451452, 0.00018753, 1011.11504841, 0.00062509, -101.11150484, -6.251e-05, -303.33451452, -0.00018753, -1011.11504841, -0.00062509, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.9, 5.15, 3.525)
    ops.node(122011, 8.9, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.4275, 28763916.87455272, 11984965.36439697, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 760.07015279, 0.00057483, 923.82110174, 0.031809, 92.38211017, 0.08609206, -760.07015279, -0.00057483, -923.82110174, -0.031809, -92.38211017, -0.08609206, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 286.53980811, 0.00075582, 348.27248544, 0.02573404, 34.82724854, 0.05767951, -286.53980811, -0.00075582, -348.27248544, -0.02573404, -34.82724854, -0.05767951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 769.58525373, 0.01149664, 769.58525373, 0.03448993, 538.70967761, -12351.46739137, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 192.39631343, 0.00012167, 577.1889403, 0.000365, 1923.96313433, 0.00121666, -192.39631343, -0.00012167, -577.1889403, -0.000365, -1923.96313433, -0.00121666, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 394.61743315, 0.01511633, 394.61743315, 0.045349, 276.2322032, -4490.54070812, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 98.65435829, 6.239e-05, 295.96307486, 0.00018716, 986.54358287, 0.00062386, -98.65435829, -6.239e-05, -295.96307486, -0.00018716, -986.54358287, -0.00062386, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.35, 5.15, 3.525)
    ops.node(122012, 13.35, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.32, 29813771.69456388, 12422404.87273495, 0.01171867, 0.00469333, 0.01877333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 548.53596531, 0.00059211, 664.68153451, 0.03324277, 66.46815345, 0.09263595, -548.53596531, -0.00059211, -664.68153451, -0.03324277, -66.46815345, -0.09263595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 222.19526543, 0.0008149, 269.24230921, 0.02711711, 26.92423092, 0.06268009, -222.19526543, -0.0008149, -269.24230921, -0.02711711, -26.92423092, -0.06268009, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 613.40376159, 0.01184225, 613.40376159, 0.03552674, 429.38263311, -10613.9016585, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 153.3509404, 0.00012499, 460.05282119, 0.00037497, 1533.50940397, 0.0012499, -153.3509404, -0.00012499, -460.05282119, -0.00037497, -1533.50940397, -0.0012499, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 317.22570984, 0.016298, 317.22570984, 0.048894, 222.05799689, -4122.48751104, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 79.30642746, 6.464e-05, 237.91928238, 0.00019392, 793.06427461, 0.00064639, -79.30642746, -6.464e-05, -237.91928238, -0.00019392, -793.06427461, -0.00064639, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 16.35, 5.15, 3.525)
    ops.node(122013, 16.35, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.32, 29456380.08809245, 12273491.70337186, 0.01171867, 0.00469333, 0.01877333, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 547.25934053, 0.00059035, 663.67439053, 0.03324014, 66.36743905, 0.09226308, -547.25934053, -0.00059035, -663.67439053, -0.03324014, -66.36743905, -0.09226308, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 221.6464017, 0.0008095, 268.79585175, 0.02711102, 26.87958517, 0.0624523, -221.6464017, -0.0008095, -268.79585175, -0.02711102, -26.87958517, -0.0624523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 603.57881645, 0.01180693, 603.57881645, 0.03542078, 422.50517151, -10379.18618619, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 150.89470411, 0.00012448, 452.68411233, 0.00037344, 1508.94704111, 0.0012448, -150.89470411, -0.00012448, -452.68411233, -0.00037344, -1508.94704111, -0.0012448, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 312.13678982, 0.01619002, 312.13678982, 0.04857007, 218.49575288, -4049.26685066, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 78.03419746, 6.437e-05, 234.10259237, 0.00019312, 780.34197456, 0.00064374, -78.03419746, -6.437e-05, -234.10259237, -0.00019312, -780.34197456, -0.00064374, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 20.8, 5.15, 3.525)
    ops.node(122014, 20.8, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.4275, 29505534.20344594, 12293972.58476914, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 768.27993982, 0.00057418, 932.273721, 0.03147157, 93.2273721, 0.08641514, -768.27993982, -0.00057418, -932.273721, -0.03147157, -93.2273721, -0.08641514, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 289.82500514, 0.00075171, 351.6898229, 0.02546061, 35.16898229, 0.05779478, -289.82500514, -0.00075171, -351.6898229, -0.02546061, -35.16898229, -0.05779478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 786.55450059, 0.01148365, 786.55450059, 0.03445095, 550.58815041, -12237.59472611, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 196.63862515, 0.00012122, 589.91587544, 0.00036367, 1966.38625147, 0.00121223, -196.63862515, -0.00012122, -589.91587544, -0.00036367, -1966.38625147, -0.00121223, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 403.76464123, 0.01503422, 403.76464123, 0.04510266, 282.63524886, -4458.00097466, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 100.94116031, 6.223e-05, 302.82348092, 0.00018668, 1009.41160308, 0.00062228, -100.94116031, -6.223e-05, -302.82348092, -0.00018668, -1009.41160308, -0.00062228, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 25.25, 5.15, 3.525)
    ops.node(122015, 25.25, 5.15, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.4275, 29240689.8067724, 12183620.75282183, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 761.37149883, 0.00057635, 924.44797743, 0.03208159, 92.44479774, 0.08679668, -761.37149883, -0.00057635, -924.44797743, -0.03208159, -92.44479774, -0.08679668, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 287.16551056, 0.00076142, 348.6728566, 0.02595642, 34.86728566, 0.05815613, -287.16551056, -0.00076142, -348.6728566, -0.02595642, -34.86728566, -0.05815613, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 788.59430614, 0.01152704, 788.59430614, 0.03458111, 552.0160143, -12854.32618217, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 197.14857654, 0.00012264, 591.44572961, 0.00036791, 1971.48576536, 0.00122638, -197.14857654, -0.00012264, -591.44572961, -0.00036791, -1971.48576536, -0.00122638, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 404.33274604, 0.01522832, 404.33274604, 0.04568495, 283.03292223, -4633.85684159, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 101.08318651, 6.288e-05, 303.24955953, 0.00018864, 1010.8318651, 0.0006288, -101.08318651, -6.288e-05, -303.24955953, -0.00018864, -1010.8318651, -0.0006288, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 29.7, 5.15, 3.5)
    ops.node(122016, 29.7, 5.15, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.245, 30227655.90669308, 12594856.62778878, 0.00686927, 0.00275115, 0.01100458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 336.90238719, 0.00059939, 407.82036412, 0.02457402, 40.78203641, 0.07744932, -336.90238719, -0.00059939, -407.82036412, -0.02457402, -40.78203641, -0.07744932, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 136.68710751, 0.00086124, 165.45975355, 0.02035641, 16.54597535, 0.05272916, -136.68710751, -0.00086124, -165.45975355, -0.02035641, -16.54597535, -0.05272916, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 411.2063898, 0.01198783, 411.2063898, 0.03596349, 287.84447286, -6335.85281819, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 102.80159745, 0.00010794, 308.40479235, 0.00032382, 1028.01597449, 0.00107941, -102.80159745, -0.00010794, -308.40479235, -0.00032382, -1028.01597449, -0.00107941, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 232.62091731, 0.01722477, 232.62091731, 0.0516743, 162.83464212, -2594.95952535, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 58.15522933, 6.106e-05, 174.46568799, 0.00018319, 581.55229328, 0.00061062, -58.15522933, -6.106e-05, -174.46568799, -0.00018319, -581.55229328, -0.00061062, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 10.3, 3.5)
    ops.node(122017, 0.0, 10.3, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.1, 29673107.50280973, 12363794.79283739, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 48.09492579, 0.00110146, 58.18740265, 0.01547857, 5.81874026, 0.05348955, -48.09492579, -0.00110146, -58.18740265, -0.01547857, -5.81874026, -0.05348955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 74.03832414, 0.00076729, 89.57489188, 0.01746422, 8.95748919, 0.07166588, -74.03832414, -0.00076729, -89.57489188, -0.01746422, -8.95748919, -0.07166588, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 109.00847644, 0.02202924, 109.00847644, 0.06608771, 76.30593351, -1495.89812024, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 27.25211911, 7.142e-05, 81.75635733, 0.00021425, 272.52119109, 0.00071416, -27.25211911, -7.142e-05, -81.75635733, -0.00021425, -272.52119109, -0.00071416, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 134.49189105, 0.01534571, 134.49189105, 0.04603714, 94.14432374, -2697.70761794, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 33.62297276, 8.811e-05, 100.86891829, 0.00026433, 336.22972763, 0.00088111, -33.62297276, -8.811e-05, -100.86891829, -0.00026433, -336.22972763, -0.00088111, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 4.45, 10.3, 3.525)
    ops.node(122018, 4.45, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.2275, 28635075.94096793, 11931281.64206997, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 130.0782253, 0.00088017, 157.96979913, 0.01727583, 15.79697991, 0.04574181, -130.0782253, -0.00088017, -157.96979913, -0.01727583, -15.79697991, -0.04574181, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 293.93099284, 0.0006229, 356.95612998, 0.02013477, 35.695613, 0.0631463, -293.93099284, -0.0006229, -356.95612998, -0.02013477, -35.695613, -0.0631463, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 195.48533385, 0.0176034, 195.48533385, 0.05281019, 136.8397337, -1997.45325632, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 48.87133346, 5.834e-05, 146.61400039, 0.00017501, 488.71333463, 0.00058335, -48.87133346, -5.834e-05, -146.61400039, -0.00017501, -488.71333463, -0.00058335, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 319.50618905, 0.01245807, 319.50618905, 0.0373742, 223.65433234, -4116.22370943, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 79.87654726, 9.534e-05, 239.62964179, 0.00028603, 798.76547263, 0.00095345, -79.87654726, -9.534e-05, -239.62964179, -0.00028603, -798.76547263, -0.00095345, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.9, 10.3, 3.525)
    ops.node(122019, 8.9, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.2275, 29963530.92484351, 12484804.55201813, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 142.49197605, 0.0008893, 172.55460539, 0.01986399, 17.25546054, 0.04907395, -142.49197605, -0.0008893, -172.55460539, -0.01986399, -17.25546054, -0.04907395, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 299.56887117, 0.00062706, 362.77122254, 0.02320814, 36.27712225, 0.06734381, -299.56887117, -0.00062706, -362.77122254, -0.02320814, -36.27712225, -0.06734381, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 207.18195692, 0.01778594, 207.18195692, 0.05335781, 145.02736984, -2095.1212519, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 51.79548923, 5.908e-05, 155.38646769, 0.00017725, 517.9548923, 0.00059085, -51.79548923, -5.908e-05, -155.38646769, -0.00017725, -517.9548923, -0.00059085, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 338.39832133, 0.01254124, 338.39832133, 0.03762372, 236.87882493, -4377.51703784, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 84.59958033, 9.651e-05, 253.798741, 0.00028952, 845.99580332, 0.00096505, -84.59958033, -9.651e-05, -253.798741, -0.00028952, -845.99580332, -0.00096505, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 13.35, 10.3, 3.525)
    ops.node(122020, 13.35, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1925, 31136101.84242232, 12973375.76767597, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 110.6153236, 0.00082178, 133.56601536, 0.0179122, 13.35660154, 0.05622572, -110.6153236, -0.00082178, -133.56601536, -0.0179122, -13.35660154, -0.05622572, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 198.4107532, 0.00063523, 239.57741882, 0.02029161, 23.95774188, 0.07368147, -198.4107532, -0.00063523, -239.57741882, -0.02029161, -23.95774188, -0.07368147, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 203.44396776, 0.01643556, 203.44396776, 0.04930667, 142.41077743, -2643.87873638, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 50.86099194, 6.599e-05, 152.58297582, 0.00019796, 508.6099194, 0.00065985, -50.86099194, -6.599e-05, -152.58297582, -0.00019796, -508.6099194, -0.00065985, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 284.75466375, 0.01270454, 284.75466375, 0.03811362, 199.32826463, -4808.24180206, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 71.18866594, 9.236e-05, 213.56599782, 0.00027707, 711.88665938, 0.00092357, -71.18866594, -9.236e-05, -213.56599782, -0.00027707, -711.88665938, -0.00092357, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 16.35, 10.3, 3.525)
    ops.node(122021, 16.35, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1925, 29493935.56057769, 12289139.81690737, 0.00475217, 0.00533786, 0.00216161, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 110.75516933, 0.00082521, 134.27780591, 0.01842185, 13.42778059, 0.05571174, -110.75516933, -0.00082521, -134.27780591, -0.01842185, -13.42778059, -0.05571174, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 199.02749942, 0.00063904, 241.29777508, 0.02087764, 24.12977751, 0.07284107, -199.02749942, -0.00063904, -241.29777508, -0.02087764, -24.12977751, -0.07284107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 194.91503664, 0.01650419, 194.91503664, 0.04951258, 136.44052565, -2689.17937133, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 48.72875916, 6.674e-05, 146.18627748, 0.00020022, 487.28759159, 0.00066739, -48.72875916, -6.674e-05, -146.18627748, -0.00020022, -487.28759159, -0.00066739, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 273.90850671, 0.01278072, 273.90850671, 0.03834216, 191.7359547, -4904.30920245, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 68.47712668, 9.379e-05, 205.43138003, 0.00028136, 684.77126678, 0.00093786, -68.47712668, -9.379e-05, -205.43138003, -0.00028136, -684.77126678, -0.00093786, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 20.8, 10.3, 3.525)
    ops.node(122022, 20.8, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.2275, 30597044.86677891, 12748768.69449121, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 141.84682816, 0.00086485, 171.50722776, 0.01954926, 17.15072278, 0.04907199, -141.84682816, -0.00086485, -171.50722776, -0.01954926, -17.15072278, -0.04907199, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 297.55181689, 0.00061582, 359.77037972, 0.02285145, 35.97703797, 0.06745971, -297.55181689, -0.00061582, -359.77037972, -0.02285145, -35.97703797, -0.06745971, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 210.87111793, 0.01729695, 210.87111793, 0.05189084, 147.60978255, -2071.35789909, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 52.71777948, 5.889e-05, 158.15333845, 0.00017667, 527.17779483, 0.00058891, -52.71777948, -5.889e-05, -158.15333845, -0.00017667, -527.17779483, -0.00058891, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 343.87242313, 0.01231646, 343.87242313, 0.03694938, 240.71069619, -4313.77741348, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 85.96810578, 9.604e-05, 257.90431735, 0.00028811, 859.68105783, 0.00096036, -85.96810578, -9.604e-05, -257.90431735, -0.00028811, -859.68105783, -0.00096036, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 25.25, 10.3, 3.525)
    ops.node(122023, 25.25, 10.3, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2275, 29135056.63365114, 12139606.93068798, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 132.53663985, 0.00086877, 160.79402955, 0.01716917, 16.07940295, 0.04593018, -132.53663985, -0.00086877, -160.79402955, -0.01716917, -16.07940295, -0.04593018, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 299.67061839, 0.00062125, 363.56170129, 0.02001975, 36.35617013, 0.06347705, -299.67061839, -0.00062125, -363.56170129, -0.02001975, -36.35617013, -0.06347705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 199.07710218, 0.01737548, 199.07710218, 0.05212645, 139.35397153, -2006.38336279, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 49.76927555, 5.839e-05, 149.30782664, 0.00017516, 497.69275545, 0.00058388, -49.76927555, -5.839e-05, -149.30782664, -0.00017516, -497.69275545, -0.00058388, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 325.12065262, 0.01242503, 325.12065262, 0.03727509, 227.58445683, -4140.03897038, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 81.28016315, 9.536e-05, 243.84048946, 0.00028607, 812.80163154, 0.00095355, -81.28016315, -9.536e-05, -243.84048946, -0.00028607, -812.80163154, -0.00095355, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 29.7, 10.3, 3.5)
    ops.node(122024, 29.7, 10.3, 5.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1, 29643926.87312956, 12351636.19713732, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 47.00117325, 0.00110463, 56.86756901, 0.0154741, 5.6867569, 0.05345872, -47.00117325, -0.00110463, -56.86756901, -0.0154741, -5.6867569, -0.05345872, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 72.74461138, 0.000764, 88.0150201, 0.01745207, 8.80150201, 0.07161614, -72.74461138, -0.000764, -88.0150201, -0.01745207, -8.80150201, -0.07161614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 108.52292097, 0.02209254, 108.52292097, 0.06627763, 75.96604468, -1479.93179566, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 27.13073024, 7.117e-05, 81.39219072, 0.0002135, 271.30730242, 0.00071168, -27.13073024, -7.117e-05, -81.39219072, -0.0002135, -271.30730242, -0.00071168, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 133.76773745, 0.01527995, 133.76773745, 0.04583985, 93.63741621, -2663.41913556, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 33.44193436, 8.772e-05, 100.32580308, 0.00026317, 334.41934361, 0.00087723, -33.44193436, -8.772e-05, -100.32580308, -0.00026317, -334.41934361, -0.00087723, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.2)
    ops.node(123001, 0.0, 0.0, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0875, 29332768.68434987, 12221986.95181245, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 37.73724015, 0.00111337, 45.78827182, 0.01692231, 4.57882718, 0.06124825, -37.73724015, -0.00111337, -45.78827182, -0.01692231, -4.57882718, -0.06124825, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 60.00305495, 0.00084149, 72.80437519, 0.01847052, 7.28043752, 0.07587144, -60.00305495, -0.00084149, -72.80437519, -0.01847052, -7.28043752, -0.07587144, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 96.89613336, 0.02226741, 96.89613336, 0.06680222, 67.82729335, -1728.88541968, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 24.22403334, 7.339e-05, 72.67210002, 0.00022017, 242.24033339, 0.00073391, -24.22403334, -7.339e-05, -72.67210002, -0.00022017, -242.24033339, -0.00073391, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 114.1113689, 0.01682985, 114.1113689, 0.05048954, 79.87795823, -2811.16262432, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 28.52784222, 8.643e-05, 85.58352667, 0.00025929, 285.27842224, 0.0008643, -28.52784222, -8.643e-05, -85.58352667, -0.00025929, -285.27842224, -0.0008643, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.45, 0.0, 6.225)
    ops.node(123002, 4.45, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1375, 29353371.1610828, 12230571.31711783, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 66.02872662, 0.00115363, 80.05875688, 0.01882761, 8.00587569, 0.05070708, -66.02872662, -0.00115363, -80.05875688, -0.01882761, -8.00587569, -0.05070708, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 173.72919561, 0.00066177, 210.64382348, 0.02312375, 21.06438235, 0.07941983, -173.72919561, -0.00066177, -210.64382348, -0.02312375, -21.06438235, -0.07941983, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 130.05916171, 0.02307256, 130.05916171, 0.06921769, 91.0414132, -1526.39580674, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 32.51479043, 6.264e-05, 97.54437128, 0.00018793, 325.14790428, 0.00062644, -32.51479043, -6.264e-05, -97.54437128, -0.00018793, -325.14790428, -0.00062644, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 208.68885588, 0.0132355, 208.68885588, 0.03970649, 146.08219912, -4252.02688625, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 52.17221397, 0.00010052, 156.51664191, 0.00030155, 521.72213971, 0.00100516, -52.17221397, -0.00010052, -156.51664191, -0.00030155, -521.72213971, -0.00100516, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.9, 0.0, 6.225)
    ops.node(123003, 8.9, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.1375, 30174667.91990622, 12572778.29996092, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 67.04354992, 0.00112416, 81.13772475, 0.01824223, 8.11377248, 0.05061076, -67.04354992, -0.00112416, -81.13772475, -0.01824223, -8.11377248, -0.05061076, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 175.90146009, 0.00065542, 212.88019906, 0.02241089, 21.28801991, 0.07957059, -175.90146009, -0.00065542, -212.88019906, -0.02241089, -21.28801991, -0.07957059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 131.2258354, 0.02248312, 131.2258354, 0.06744936, 91.85808478, -1441.43404474, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 32.80645885, 6.149e-05, 98.41937655, 0.00018446, 328.06458849, 0.00061485, -32.80645885, -6.149e-05, -98.41937655, -0.00018446, -328.06458849, -0.00061485, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 208.22856533, 0.01310846, 208.22856533, 0.03932537, 145.75999573, -3941.47936758, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 52.05714133, 9.756e-05, 156.171424, 0.00029269, 520.57141332, 0.00097564, -52.05714133, -9.756e-05, -156.171424, -0.00029269, -520.57141332, -0.00097564, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 20.8, 0.0, 6.225)
    ops.node(123006, 20.8, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.1375, 29573095.02816795, 12322122.92840331, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 67.87717539, 0.00116774, 82.26063786, 0.0184399, 8.22606379, 0.05045526, -67.87717539, -0.00116774, -82.26063786, -0.0184399, -8.22606379, -0.05045526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 178.52929042, 0.00067181, 216.36040721, 0.02262312, 21.63604072, 0.07915915, -178.52929042, -0.00067181, -216.36040721, -0.02262312, -21.63604072, -0.07915915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 129.26979356, 0.02335472, 129.26979356, 0.07006417, 90.48885549, -1461.32470258, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 32.31744839, 6.18e-05, 96.95234517, 0.0001854, 323.17448389, 0.00061801, -32.31744839, -6.18e-05, -96.95234517, -0.0001854, -323.17448389, -0.00061801, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 206.14743646, 0.01343621, 206.14743646, 0.04030862, 144.30320552, -4013.92220579, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 51.53685912, 9.855e-05, 154.61057735, 0.00029566, 515.36859115, 0.00098554, -51.53685912, -9.855e-05, -154.61057735, -0.00029566, -515.36859115, -0.00098554, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 25.25, 0.0, 6.225)
    ops.node(123007, 25.25, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1375, 31020624.39152125, 12925260.16313385, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 65.9767196, 0.00117881, 79.67564452, 0.01802132, 7.96756445, 0.05084331, -65.9767196, -0.00117881, -79.67564452, -0.01802132, -7.96756445, -0.05084331, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 173.48240234, 0.00066423, 209.50302323, 0.02206949, 20.95030232, 0.08002997, -173.48240234, -0.00066423, -209.50302323, -0.02206949, -20.95030232, -0.08002997, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 135.19815784, 0.02357611, 135.19815784, 0.07072833, 94.63871049, -1457.93421416, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 33.79953946, 6.162e-05, 101.39861838, 0.00018486, 337.99539461, 0.00061619, -33.79953946, -6.162e-05, -101.39861838, -0.00018486, -337.99539461, -0.00061619, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 213.79655471, 0.01328468, 213.79655471, 0.03985405, 149.65758829, -4001.56234801, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 53.44913868, 9.744e-05, 160.34741603, 0.00029232, 534.49138677, 0.00097441, -53.44913868, -9.744e-05, -160.34741603, -0.00029232, -534.49138677, -0.00097441, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 29.7, 0.0, 6.2)
    ops.node(123008, 29.7, 0.0, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0875, 29592332.04092986, 12330138.35038744, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 37.86979793, 0.0011311, 45.92228738, 0.01652235, 4.59222874, 0.06104603, -37.86979793, -0.0011311, -45.92228738, -0.01652235, -4.59222874, -0.06104603, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 60.14008826, 0.00085119, 72.92804735, 0.01801445, 7.29280473, 0.07567143, -60.14008826, -0.00085119, -72.92804735, -0.01801445, -7.29280473, -0.07567143, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 96.34977902, 0.02262191, 96.34977902, 0.06786572, 67.44484531, -1662.18433755, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 24.08744476, 7.234e-05, 72.26233427, 0.00021701, 240.87444755, 0.00072337, -24.08744476, -7.234e-05, -72.26233427, -0.00021701, -240.87444755, -0.00072337, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 113.07748906, 0.01702386, 113.07748906, 0.05107158, 79.15424234, -2692.2022441, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 28.26937227, 8.49e-05, 84.8081168, 0.00025469, 282.69372266, 0.00084896, -28.26937227, -8.49e-05, -84.8081168, -0.00025469, -282.69372266, -0.00084896, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 5.15, 6.2)
    ops.node(123009, 0.0, 5.15, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.15, 28288363.00231304, 11786817.91763043, 0.00230675, 0.00085938, 0.00495, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 171.97190135, 0.00063491, 209.03042554, 0.02797436, 20.90304255, 0.09477677, -171.97190135, -0.00063491, -209.03042554, -0.02797436, -20.90304255, -0.09477677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 62.01090921, 0.00114507, 75.37374791, 0.0218219, 7.53737479, 0.05626038, -62.01090921, -0.00114507, -75.37374791, -0.0218219, -7.53737479, -0.05626038, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 254.16102581, 0.01269825, 254.16102581, 0.03809476, 177.91271806, -6490.01723888, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 63.54025645, 0.00011644, 190.62076935, 0.00034932, 635.40256452, 0.00116441, -63.54025645, -0.00011644, -190.62076935, -0.00034932, -635.40256452, -0.00116441, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 142.01831818, 0.02290137, 142.01831818, 0.0687041, 99.41282273, -1917.5088106, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 35.50457955, 6.506e-05, 106.51373864, 0.00019519, 355.04579546, 0.00065064, -35.50457955, -6.506e-05, -106.51373864, -0.00019519, -355.04579546, -0.00065064, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 4.45, 5.15, 6.225)
    ops.node(123010, 4.45, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.2975, 29193245.06808516, 12163852.11170215, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 471.5870689, 0.00057733, 572.89486293, 0.03507778, 57.28948629, 0.10288598, -471.5870689, -0.00057733, -572.89486293, -0.03507778, -57.28948629, -0.10288598, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 160.86068485, 0.0008735, 195.41727515, 0.02697279, 19.54172751, 0.06195073, -160.86068485, -0.0008735, -195.41727515, -0.02697279, -19.54172751, -0.06195073, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 595.25091738, 0.01154659, 595.25091738, 0.03463978, 416.67564216, -13813.11824607, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 148.81272934, 0.00013324, 446.43818803, 0.00039971, 1488.12729344, 0.00133238, -148.81272934, -0.00013324, -446.43818803, -0.00039971, -1488.12729344, -0.00133238, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 276.31500658, 0.01746991, 276.31500658, 0.05240974, 193.4205046, -3743.93436398, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 69.07875164, 6.185e-05, 207.23625493, 0.00018555, 690.78751644, 0.00061849, -69.07875164, -6.185e-05, -207.23625493, -0.00018555, -690.78751644, -0.00061849, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.9, 5.15, 6.225)
    ops.node(123011, 8.9, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.2975, 30428713.35648407, 12678630.5652017, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 477.59480996, 0.00058027, 578.43836656, 0.03438044, 57.84383666, 0.10332742, -477.59480996, -0.00058027, -578.43836656, -0.03438044, -57.84383666, -0.10332742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 162.80621728, 0.00088338, 197.18254978, 0.02645292, 19.71825498, 0.06201828, -162.80621728, -0.00088338, -197.18254978, -0.02645292, -19.71825498, -0.06201828, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 617.39350608, 0.01160539, 617.39350608, 0.03481618, 432.17545426, -13842.80625633, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 154.34837652, 0.00013258, 463.04512956, 0.00039775, 1543.4837652, 0.00132583, -154.34837652, -0.00013258, -463.04512956, -0.00039775, -1543.4837652, -0.00132583, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 287.3582151, 0.01766767, 287.3582151, 0.05300301, 201.15075057, -3750.29791775, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 71.83955378, 6.171e-05, 215.51866133, 0.00018513, 718.39553776, 0.00061709, -71.83955378, -6.171e-05, -215.51866133, -0.00018513, -718.39553776, -0.00061709, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.35, 5.15, 6.225)
    ops.node(123012, 13.35, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.2625, 29284838.15243782, 12202015.89684909, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 378.71184806, 0.00060299, 459.98438355, 0.03511779, 45.99843835, 0.10307297, -378.71184806, -0.00060299, -459.98438355, -0.03511779, -45.99843835, -0.10307297, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 149.41563081, 0.00089689, 181.48060902, 0.02794212, 18.1480609, 0.06604719, -149.41563081, -0.00089689, -181.48060902, -0.02794212, -18.1480609, -0.06604719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 486.07621346, 0.01205972, 486.07621346, 0.03617916, 340.25334942, -11730.35174294, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 121.51905336, 0.00012292, 364.55716009, 0.00036877, 1215.19053365, 0.00122922, -121.51905336, -0.00012292, -364.55716009, -0.00036877, -1215.19053365, -0.00122922, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 253.51993346, 0.01793787, 253.51993346, 0.05381361, 177.46395343, -3770.39474605, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 63.37998337, 6.411e-05, 190.1399501, 0.00019233, 633.79983366, 0.00064112, -63.37998337, -6.411e-05, -190.1399501, -0.00019233, -633.79983366, -0.00064112, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 16.35, 5.15, 6.225)
    ops.node(123013, 16.35, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.2625, 27840061.29149565, 11600025.53812319, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 375.30495261, 0.00059945, 457.22303586, 0.0358461, 45.72230359, 0.1022355, -375.30495261, -0.00059945, -457.22303586, -0.0358461, -45.72230359, -0.1022355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 148.37082598, 0.00088291, 180.75583339, 0.02850159, 18.07558334, 0.06572867, -148.37082598, -0.00088291, -180.75583339, -0.02850159, -18.07558334, -0.06572867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 470.46043618, 0.01198907, 470.46043618, 0.0359672, 329.32230532, -12087.68721051, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 117.61510904, 0.00012515, 352.84532713, 0.00037544, 1176.15109044, 0.00125147, -117.61510904, -0.00012515, -352.84532713, -0.00037544, -1176.15109044, -0.00125147, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 244.36561304, 0.0176581, 244.36561304, 0.05297431, 171.05592913, -3864.81043782, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 61.09140326, 6.5e-05, 183.27420978, 0.00019501, 610.91403259, 0.00065004, -61.09140326, -6.5e-05, -183.27420978, -0.00019501, -610.91403259, -0.00065004, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 20.8, 5.15, 6.225)
    ops.node(123014, 20.8, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.2975, 28895389.69429726, 12039745.70595719, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 477.97193809, 0.00058941, 581.03658704, 0.03480637, 58.1036587, 0.10231093, -477.97193809, -0.00058941, -581.03658704, -0.03480637, -58.1036587, -0.10231093, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 162.42182184, 0.0009103, 197.44468974, 0.02679514, 19.74446897, 0.06161645, -162.42182184, -0.0009103, -197.44468974, -0.02679514, -19.74446897, -0.06161645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 586.83462042, 0.01178818, 586.83462042, 0.03536453, 410.7842343, -13512.69201009, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 146.70865511, 0.00013271, 440.12596532, 0.00039812, 1467.08655106, 0.00132708, -146.70865511, -0.00013271, -440.12596532, -0.00039812, -1467.08655106, -0.00132708, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 272.39278699, 0.01820603, 272.39278699, 0.0546181, 190.67495089, -3679.45746973, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 68.09819675, 6.16e-05, 204.29459024, 0.0001848, 680.98196748, 0.00061599, -68.09819675, -6.16e-05, -204.29459024, -0.0001848, -680.98196748, -0.00061599, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 25.25, 5.15, 6.225)
    ops.node(123015, 25.25, 5.15, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.2975, 28198308.26073333, 11749295.10863889, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 472.61821271, 0.00058712, 575.36182232, 0.03507865, 57.53618223, 0.10182298, -472.61821271, -0.00058712, -575.36182232, -0.03507865, -57.53618223, -0.10182298, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 160.58077215, 0.00090489, 195.4898123, 0.02699744, 19.54898123, 0.06142659, -160.58077215, -0.00090489, -195.4898123, -0.02699744, -19.54898123, -0.06142659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 576.32412986, 0.01174241, 576.32412986, 0.03522722, 403.4268909, -13648.70838642, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 144.08103246, 0.00013355, 432.24309739, 0.00040066, 1440.81032465, 0.00133553, -144.08103246, -0.00013355, -432.24309739, -0.00040066, -1440.81032465, -0.00133553, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 267.00769928, 0.01809785, 267.00769928, 0.05429356, 186.9053895, -3708.66749073, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 66.75192482, 6.187e-05, 200.25577446, 0.00018562, 667.51924821, 0.00061874, -66.75192482, -6.187e-05, -200.25577446, -0.00018562, -667.51924821, -0.00061874, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 29.7, 5.15, 6.2)
    ops.node(123016, 29.7, 5.15, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.15, 31794396.62053964, 13247665.25855818, 0.00230675, 0.00085938, 0.00495, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 173.8072086, 0.00062542, 209.49724275, 0.02693826, 20.94972428, 0.09783903, -173.8072086, -0.00062542, -209.49724275, -0.02693826, -20.94972428, -0.09783903, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 62.80164568, 0.00112247, 75.69750251, 0.02102288, 7.56975025, 0.05757417, -62.80164568, -0.00112247, -75.69750251, -0.02102288, -7.56975025, -0.05757417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 277.52122111, 0.01250842, 277.52122111, 0.03752527, 194.26485478, -6562.20714592, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 69.38030528, 0.00011312, 208.14091583, 0.00033937, 693.80305277, 0.00113123, -69.38030528, -0.00011312, -208.14091583, -0.00033937, -693.80305277, -0.00113123, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 158.18340317, 0.02244946, 158.18340317, 0.06734839, 110.72838222, -1933.84800112, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 39.54585079, 6.448e-05, 118.63755238, 0.00019344, 395.45850792, 0.00064479, -39.54585079, -6.448e-05, -118.63755238, -0.00019344, -395.45850792, -0.00064479, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 10.3, 6.2)
    ops.node(123017, 0.0, 10.3, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0875, 31213971.14753272, 13005821.31147197, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 37.86276346, 0.00109828, 45.72521195, 0.01649409, 4.57252119, 0.06211441, -37.86276346, -0.00109828, -45.72521195, -0.01649409, -4.57252119, -0.06211441, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 60.07568817, 0.00083083, 72.5507946, 0.01799916, 7.25507946, 0.07707627, -60.07568817, -0.00083083, -72.5507946, -0.01799916, -7.25507946, -0.07707627, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 101.70895603, 0.02196551, 101.70895603, 0.06589654, 71.19626922, -1720.95709155, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 25.42723901, 7.239e-05, 76.28171702, 0.00021718, 254.27239008, 0.00072393, -25.42723901, -7.239e-05, -76.28171702, -0.00021718, -254.27239008, -0.00072393, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 118.86674103, 0.01661652, 118.86674103, 0.04984957, 83.20671872, -2797.01053161, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 29.71668526, 8.461e-05, 89.15005578, 0.00025382, 297.16685259, 0.00084606, -29.71668526, -8.461e-05, -89.15005578, -0.00025382, -297.16685259, -0.00084606, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 4.45, 10.3, 6.225)
    ops.node(123018, 4.45, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1375, 30248916.66944319, 12603715.27893466, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 66.11571206, 0.00117261, 80.00049947, 0.0185905, 8.00004995, 0.05100078, -66.11571206, -0.00117261, -80.00049947, -0.0185905, -8.00004995, -0.05100078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 173.97172753, 0.00066503, 210.50707407, 0.02280154, 21.05070741, 0.08003497, -173.97172753, -0.00066503, -210.50707407, -0.02280154, -21.05070741, -0.08003497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 132.66311876, 0.02345223, 132.66311876, 0.07035669, 92.86418313, -1484.52959958, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 33.16577969, 6.201e-05, 99.49733907, 0.00018602, 331.65779689, 0.00062006, -33.16577969, -6.201e-05, -99.49733907, -0.00018602, -331.65779689, -0.00062006, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 211.11442276, 0.0133006, 211.11442276, 0.0399018, 147.78009593, -4098.63971035, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 52.77860569, 9.867e-05, 158.33581707, 0.00029602, 527.78605689, 0.00098674, -52.77860569, -9.867e-05, -158.33581707, -0.00029602, -527.78605689, -0.00098674, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.9, 10.3, 6.225)
    ops.node(123019, 8.9, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1375, 29723133.21736702, 12384638.84056959, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 75.51735404, 0.00122412, 91.48912456, 0.02048828, 9.14891246, 0.05259426, -75.51735404, -0.00122412, -91.48912456, -0.02048828, -9.14891246, -0.05259426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 183.33958325, 0.00069071, 222.1155413, 0.02517365, 22.21155413, 0.08186972, -183.33958325, -0.00069071, -222.1155413, -0.02517365, -22.21155413, -0.08186972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 129.2112307, 0.02448246, 129.2112307, 0.07344738, 90.44786149, -1435.72567222, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 32.30280767, 6.146e-05, 96.90842302, 0.00018438, 323.02807675, 0.00061461, -32.30280767, -6.146e-05, -96.90842302, -0.00018438, -323.02807675, -0.00061461, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 205.46693242, 0.01381423, 205.46693242, 0.04144269, 143.82685269, -3920.71948708, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 51.3667331, 9.773e-05, 154.10019931, 0.0002932, 513.66733104, 0.00097733, -51.3667331, -9.773e-05, -154.10019931, -0.0002932, -513.66733104, -0.00097733, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 13.35, 10.3, 6.225)
    ops.node(123020, 13.35, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.125, 30140039.15801616, 12558349.6491734, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 67.71904324, 0.00109123, 82.00096538, 0.01959225, 8.20009654, 0.06022468, -67.71904324, -0.00109123, -82.00096538, -0.01959225, -8.20009654, -0.06022468, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 118.41239376, 0.0006737, 143.38552549, 0.02387787, 14.33855255, 0.09341498, -118.41239376, -0.0006737, -143.38552549, -0.02387787, -14.33855255, -0.09341498, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 136.16184103, 0.02182469, 136.16184103, 0.06547408, 95.31328872, -2150.04641022, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 34.04046026, 7.026e-05, 102.12138077, 0.00021078, 340.40460258, 0.00070258, -34.04046026, -7.026e-05, -102.12138077, -0.00021078, -340.40460258, -0.00070258, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 206.90651389, 0.0134741, 206.90651389, 0.04042229, 144.83455972, -5930.15605837, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 51.72662847, 0.00010676, 155.17988542, 0.00032029, 517.26628473, 0.00106762, -51.72662847, -0.00010676, -155.17988542, -0.00032029, -517.26628473, -0.00106762, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 16.35, 10.3, 6.225)
    ops.node(123021, 16.35, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.125, 28658988.31722701, 11941245.13217792, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 66.4875533, 0.00112097, 80.77409531, 0.0192351, 8.07740953, 0.0588081, -66.4875533, -0.00112097, -80.77409531, -0.0192351, -8.07740953, -0.0588081, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 117.15241019, 0.00068279, 142.32558542, 0.02340173, 14.23255854, 0.09112575, -117.15241019, -0.00068279, -142.32558542, -0.02340173, -14.23255854, -0.09112575, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 126.24839626, 0.02241936, 126.24839626, 0.06725809, 88.37387738, -1930.44464836, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 31.56209906, 6.851e-05, 94.68629719, 0.00020553, 315.62099064, 0.0006851, -31.56209906, -6.851e-05, -94.68629719, -0.00020553, -315.62099064, -0.0006851, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 191.54363257, 0.01365582, 191.54363257, 0.04096745, 134.0805428, -5204.75268904, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 47.88590814, 0.00010394, 143.65772443, 0.00031183, 478.85908143, 0.00103942, -47.88590814, -0.00010394, -143.65772443, -0.00031183, -478.85908143, -0.00103942, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 20.8, 10.3, 6.225)
    ops.node(123022, 20.8, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.1375, 29015982.99376784, 12089992.91406994, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 71.91687341, 0.00123707, 87.25944138, 0.02124957, 8.72594414, 0.0529128, -71.91687341, -0.00123707, -87.25944138, -0.02124957, -8.72594414, -0.0529128, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 176.22063306, 0.00068505, 213.81510723, 0.02611907, 21.38151072, 0.08203329, -176.22063306, -0.00068505, -213.81510723, -0.02611907, -21.38151072, -0.08203329, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 128.46526632, 0.02474132, 128.46526632, 0.07422396, 89.92568643, -1517.71149233, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 32.11631658, 6.26e-05, 96.34894974, 0.00018779, 321.16316581, 0.00062595, -32.11631658, -6.26e-05, -96.34894974, -0.00018779, -321.16316581, -0.00062595, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 206.41094613, 0.01370109, 206.41094613, 0.04110328, 144.48766229, -4220.15369733, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 51.60273653, 0.00010057, 154.8082096, 0.00030172, 516.02736533, 0.00100575, -51.60273653, -0.00010057, -154.8082096, -0.00030172, -516.02736533, -0.00100575, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 25.25, 10.3, 6.225)
    ops.node(123023, 25.25, 10.3, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1375, 29547375.95342891, 12311406.64726205, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 65.93920838, 0.00117564, 79.91654262, 0.01857214, 7.99165426, 0.05057179, -65.93920838, -0.00117564, -79.91654262, -0.01857214, -7.99165426, -0.05057179, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 173.6386295, 0.00066682, 210.44533708, 0.02277615, 21.04453371, 0.07928444, -173.6386295, -0.00066682, -210.44533708, -0.02277615, -21.04453371, -0.07928444, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 129.69495764, 0.02351273, 129.69495764, 0.07053818, 90.78647035, -1481.63004078, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 32.42373941, 6.206e-05, 97.27121823, 0.00018617, 324.2373941, 0.00062058, -32.42373941, -6.206e-05, -97.27121823, -0.00018617, -324.2373941, -0.00062058, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 207.17719101, 0.01333647, 207.17719101, 0.04000942, 145.02403371, -4088.04201927, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 51.79429775, 9.913e-05, 155.38289326, 0.0002974, 517.94297752, 0.00099133, -51.79429775, -9.913e-05, -155.38289326, -0.0002974, -517.94297752, -0.00099133, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 29.7, 10.3, 6.2)
    ops.node(123024, 29.7, 10.3, 8.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0875, 29170535.41267037, 12154389.75527932, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 38.62443494, 0.00111107, 46.88135631, 0.01678574, 4.68813563, 0.06098466, -38.62443494, -0.00111107, -46.88135631, -0.01678574, -4.68813563, -0.06098466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 61.58018213, 0.00084513, 74.74445812, 0.01832443, 7.47444581, 0.07556086, -61.58018213, -0.00084513, -74.74445812, -0.01832443, -7.47444581, -0.07556086, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 96.469223, 0.02222143, 96.469223, 0.06666429, 67.5284561, -1728.41726661, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 24.11730575, 7.347e-05, 72.35191725, 0.00022042, 241.17305751, 0.00073474, -24.11730575, -7.347e-05, -72.35191725, -0.00022042, -241.17305751, -0.00073474, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 113.68106986, 0.01690265, 113.68106986, 0.05070795, 79.5767489, -2810.326881, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 28.42026746, 8.658e-05, 85.26080239, 0.00025975, 284.20267465, 0.00086583, -28.42026746, -8.658e-05, -85.26080239, -0.00025975, -284.20267465, -0.00086583, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.9)
    ops.node(124001, 0.0, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0875, 28037298.35132778, 11682207.64638657, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 30.7998426, 0.00109088, 37.62970121, 0.01807914, 3.76297012, 0.06722749, -30.7998426, -0.00109088, -37.62970121, -0.01807914, -3.76297012, -0.06722749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 50.08703882, 0.00082579, 61.19382913, 0.01976991, 6.11938291, 0.08341572, -50.08703882, -0.00082579, -61.19382913, -0.01976991, -6.11938291, -0.08341572, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 86.49646463, 0.02181759, 86.49646463, 0.06545277, 60.54752524, -3570.71652949, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 21.62411616, 6.854e-05, 64.87234847, 0.00020562, 216.24116157, 0.00068541, -21.62411616, -6.854e-05, -64.87234847, -0.00020562, -216.24116157, -0.00068541, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 103.40920237, 0.01651578, 103.40920237, 0.04954733, 72.38644166, -6544.46248138, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 25.85230059, 8.194e-05, 77.55690178, 0.00024583, 258.52300592, 0.00081943, -25.85230059, -8.194e-05, -77.55690178, -0.00024583, -258.52300592, -0.00081943, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.45, 0.0, 8.925)
    ops.node(124002, 4.45, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1375, 31434178.94242973, 13097574.55934572, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 54.79336813, 0.00110337, 66.30784974, 0.01572137, 6.63078497, 0.0482228, -54.79336813, -0.00110337, -66.30784974, -0.01572137, -6.63078497, -0.0482228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 147.85262409, 0.00063913, 178.92292292, 0.01897515, 17.89229229, 0.07461129, -147.85262409, -0.00063913, -178.92292292, -0.01897515, -17.89229229, -0.07461129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 114.2343908, 0.02206738, 114.2343908, 0.06620214, 79.96407356, -1615.36373307, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 28.5585977, 5.138e-05, 85.6757931, 0.00015414, 285.58597701, 0.00051379, -28.5585977, -5.138e-05, -85.6757931, -0.00015414, -285.58597701, -0.00051379, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 184.46025677, 0.01278262, 184.46025677, 0.03834786, 129.12217974, -5918.51491406, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 46.11506419, 8.296e-05, 138.34519257, 0.00024889, 461.15064191, 0.00082965, -46.11506419, -8.296e-05, -138.34519257, -0.00024889, -461.15064191, -0.00082965, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.9, 0.0, 8.925)
    ops.node(124003, 8.9, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.1375, 29363664.02316358, 12234860.00965149, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 53.90169433, 0.00109285, 65.61700346, 0.01641715, 6.56170035, 0.04856993, -53.90169433, -0.00109285, -65.61700346, -0.01641715, -6.56170035, -0.04856993, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 145.62632229, 0.00063683, 177.27759791, 0.0198588, 17.72775979, 0.07489813, -145.62632229, -0.00063683, -177.27759791, -0.0198588, -17.72775979, -0.07489813, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 107.2176652, 0.02185695, 107.2176652, 0.06557086, 75.05236564, -1705.37329857, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 26.8044163, 5.162e-05, 80.4132489, 0.00015487, 268.044163, 0.00051624, -26.8044163, -5.162e-05, -80.4132489, -0.00015487, -268.044163, -0.00051624, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 176.10131792, 0.0127367, 176.10131792, 0.03821009, 123.27092255, -6298.32007808, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 44.02532948, 8.479e-05, 132.07598844, 0.00025437, 440.25329481, 0.0008479, -44.02532948, -8.479e-05, -132.07598844, -0.00025437, -440.25329481, -0.0008479, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 20.8, 0.0, 8.925)
    ops.node(124006, 20.8, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.1375, 29502791.1085671, 12292829.62856962, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 54.213483, 0.00112979, 65.97252228, 0.01626123, 6.59725223, 0.0484407, -54.213483, -0.00112979, -65.97252228, -0.01626123, -6.59725223, -0.0484407, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 146.73539507, 0.00064766, 178.56266716, 0.01962771, 17.85626672, 0.07471274, -146.73539507, -0.00064766, -178.56266716, -0.01962771, -17.85626672, -0.07471274, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 106.64240393, 0.02259575, 106.64240393, 0.06778726, 74.64968275, -1643.70364291, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 26.66060098, 5.11e-05, 79.98180295, 0.00015331, 266.60600982, 0.00051105, -26.66060098, -5.11e-05, -79.98180295, -0.00015331, -266.60600982, -0.00051105, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 174.9883018, 0.01295327, 174.9883018, 0.03885981, 122.49181126, -6037.93414609, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 43.74707545, 8.386e-05, 131.24122635, 0.00025157, 437.47075449, 0.00083857, -43.74707545, -8.386e-05, -131.24122635, -0.00025157, -437.47075449, -0.00083857, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 25.25, 0.0, 8.925)
    ops.node(124007, 25.25, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1375, 29091600.08226525, 12121500.03427719, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 54.68377442, 0.00111409, 66.61556059, 0.01671686, 6.66155606, 0.0488159, -54.68377442, -0.00111409, -66.61556059, -0.01671686, -6.66155606, -0.0488159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 147.83473923, 0.000646, 180.09170239, 0.02021726, 18.00917024, 0.0751646, -147.83473923, -0.000646, -180.09170239, -0.02021726, -18.00917024, -0.0751646, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 109.1611525, 0.02228183, 109.1611525, 0.06684549, 76.41280675, -1734.42113819, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 27.29028813, 5.305e-05, 81.87086438, 0.00015915, 272.90288126, 0.00053051, -27.29028813, -5.305e-05, -81.87086438, -0.00015915, -272.90288126, -0.00053051, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 175.5408772, 0.01292002, 175.5408772, 0.03876007, 122.87861404, -6421.20668557, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 43.8852193, 8.531e-05, 131.6556579, 0.00025593, 438.852193, 0.00085311, -43.8852193, -8.531e-05, -131.6556579, -0.00025593, -438.852193, -0.00085311, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 29.7, 0.0, 8.9)
    ops.node(124008, 29.7, 0.0, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0875, 28929448.73600231, 12053936.9733343, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 30.82781455, 0.00105356, 37.58256091, 0.01799903, 3.75825609, 0.06739423, -30.82781455, -0.00105356, -37.58256091, -0.01799903, -3.75825609, -0.06739423, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 50.16749572, 0.00080427, 61.15979971, 0.01970068, 6.11597997, 0.08366614, -50.16749572, -0.00080427, -61.15979971, -0.01970068, -6.11597997, -0.08366614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 90.43360334, 0.02107119, 90.43360334, 0.06321357, 63.30352233, -3830.94780919, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 22.60840083, 6.945e-05, 67.8252025, 0.00020835, 226.08400834, 0.00069451, -22.60840083, -6.945e-05, -67.8252025, -0.00020835, -226.08400834, -0.00069451, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 108.03083089, 0.01608533, 108.03083089, 0.04825598, 75.62158162, -7037.98536067, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 27.00770772, 8.297e-05, 81.02312316, 0.0002489, 270.07707721, 0.00082965, -27.00770772, -8.297e-05, -81.02312316, -0.0002489, -270.07707721, -0.00082965, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 5.15, 8.9)
    ops.node(124009, 0.0, 5.15, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.15, 29240683.46867206, 12183618.11194669, 0.00230675, 0.00085938, 0.00495, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 142.52900505, 0.0006141, 173.58486947, 0.01903945, 17.35848695, 0.07425159, -142.52900505, -0.0006141, -173.58486947, -0.01903945, -17.35848695, -0.07425159, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 50.17257023, 0.00108714, 61.10474883, 0.01546772, 6.11047488, 0.04613702, -50.17257023, -0.00108714, -61.10474883, -0.01546772, -6.11047488, -0.04613702, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 201.2721542, 0.01228191, 201.2721542, 0.03684574, 140.89050794, -7386.56954126, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 50.31803855, 8.921e-05, 150.95411565, 0.00026762, 503.18038551, 0.00089207, -50.31803855, -8.921e-05, -150.95411565, -0.00026762, -503.18038551, -0.00089207, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 113.06812592, 0.02174288, 113.06812592, 0.06522863, 79.14768814, -1716.42307264, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 28.26703148, 5.011e-05, 84.80109444, 0.00015034, 282.67031479, 0.00050114, -28.26703148, -5.011e-05, -84.80109444, -0.00015034, -282.67031479, -0.00050114, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 4.45, 5.15, 8.925)
    ops.node(124010, 4.45, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.2975, 30357664.43954884, 12649026.84981202, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 403.92101038, 0.00056397, 490.53936701, 0.01535123, 49.0539367, 0.05143908, -403.92101038, -0.00056397, -490.53936701, -0.01535123, -49.0539367, -0.05143908, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 134.13599676, 0.00084788, 162.90062971, 0.0130256, 16.29006297, 0.03579449, -134.13599676, -0.00084788, -162.90062971, -0.0130256, -16.29006297, -0.03579449, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 433.27964387, 0.01127948, 433.27964387, 0.03383843, 303.29575071, -5837.30687912, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 108.31991097, 9.326e-05, 324.9597329, 0.00027979, 1083.19910966, 0.00093263, -108.31991097, -9.326e-05, -324.9597329, -0.00027979, -1083.19910966, -0.00093263, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 208.43063323, 0.01695766, 208.43063323, 0.05087298, 145.90144326, -1509.69194631, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 52.10765831, 4.486e-05, 156.32297492, 0.00013459, 521.07658307, 0.00044864, -52.10765831, -4.486e-05, -156.32297492, -0.00013459, -521.07658307, -0.00044864, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.9, 5.15, 8.925)
    ops.node(124011, 8.9, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.2975, 30059672.92295786, 12524863.71789911, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 401.71735206, 0.00056228, 488.2779721, 0.01495336, 48.82779721, 0.05099558, -401.71735206, -0.00056228, -488.2779721, -0.01495336, -48.82779721, -0.05099558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 133.44298613, 0.00084294, 162.1968041, 0.0126944, 16.21968041, 0.0354345, -133.44298613, -0.00084294, -162.1968041, -0.0126944, -16.21968041, -0.0354345, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 423.45512169, 0.01124557, 423.45512169, 0.03373671, 296.41858518, -5368.16485949, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 105.86378042, 9.205e-05, 317.59134127, 0.00027616, 1058.63780423, 0.00092052, -105.86378042, -9.205e-05, -317.59134127, -0.00027616, -1058.63780423, -0.00092052, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 203.92149701, 0.01685876, 203.92149701, 0.05057627, 142.74504791, -1411.05968737, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 50.98037425, 4.433e-05, 152.94112276, 0.00013299, 509.80374254, 0.00044329, -50.98037425, -4.433e-05, -152.94112276, -0.00013299, -509.80374254, -0.00044329, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.35, 5.15, 8.925)
    ops.node(124012, 13.35, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.2625, 29223038.73213694, 12176266.13839039, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 321.19521997, 0.00058324, 391.26248506, 0.01534057, 39.12624851, 0.05116451, -321.19521997, -0.00058324, -391.26248506, -0.01534057, -39.12624851, -0.05116451, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 124.00807063, 0.00085871, 151.05986286, 0.01328604, 15.10598629, 0.0371171, -124.00807063, -0.00085871, -151.05986286, -0.01328604, -15.10598629, -0.0371171, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 329.77672808, 0.01166478, 329.77672808, 0.03499435, 230.84370965, -4554.50953621, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 82.44418202, 8.357e-05, 247.33254606, 0.00025072, 824.44182019, 0.00083572, -82.44418202, -8.357e-05, -247.33254606, -0.00025072, -824.44182019, -0.00083572, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 178.04840252, 0.01717427, 178.04840252, 0.05152282, 124.63388177, -1440.37917163, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 44.51210063, 4.512e-05, 133.53630189, 0.00013536, 445.12100631, 0.00045121, -44.51210063, -4.512e-05, -133.53630189, -0.00013536, -445.12100631, -0.00045121, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 16.35, 5.15, 8.925)
    ops.node(124013, 16.35, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.2625, 27588891.6174261, 11495371.50726088, 0.00757989, 0.00294766, 0.01353516, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 328.38419236, 0.00059088, 401.59101291, 0.01588334, 40.15910129, 0.05136659, -328.38419236, -0.00059088, -401.59101291, -0.01588334, -40.15910129, -0.05136659, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 127.19138356, 0.00086499, 155.54621003, 0.01374296, 15.554621, 0.03734738, -127.19138356, -0.00086499, -155.54621003, -0.01374296, -15.554621, -0.03734738, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 309.66831222, 0.01181751, 309.66831222, 0.03545254, 216.76781855, -4709.56325479, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 77.41707806, 8.312e-05, 232.25123417, 0.00024937, 774.17078055, 0.00083125, -77.41707806, -8.312e-05, -232.25123417, -0.00024937, -774.17078055, -0.00083125, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 166.58414711, 0.01729988, 166.58414711, 0.05189963, 116.60890298, -1481.0129889, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 41.64603678, 4.472e-05, 124.93811033, 0.00013415, 416.46036778, 0.00044716, -41.64603678, -4.472e-05, -124.93811033, -0.00013415, -416.46036778, -0.00044716, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 20.8, 5.15, 8.925)
    ops.node(124014, 20.8, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.2975, 30239701.23109622, 12599875.51295676, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 402.1549003, 0.00056174, 488.56018125, 0.01503747, 48.85601812, 0.05110749, -402.1549003, -0.00056174, -488.56018125, -0.01503747, -48.85601812, -0.05110749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 133.64230511, 0.00084098, 162.35611889, 0.01276215, 16.23561189, 0.03551979, -133.64230511, -0.00084098, -162.35611889, -0.01276215, -16.23561189, -0.03551979, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 426.94232627, 0.0112347, 426.94232627, 0.0337041, 298.85962839, -5399.98967489, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 106.73558157, 9.226e-05, 320.2067447, 0.00027677, 1067.35581567, 0.00092257, -106.73558157, -9.226e-05, -320.2067447, -0.00027677, -1067.35581567, -0.00092257, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 205.63720915, 0.0168195, 205.63720915, 0.05045851, 143.94604641, -1417.77627094, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 51.40930229, 4.444e-05, 154.22790687, 0.00013331, 514.09302288, 0.00044436, -51.40930229, -4.444e-05, -154.22790687, -0.00013331, -514.09302288, -0.00044436, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 25.25, 5.15, 8.925)
    ops.node(124015, 25.25, 5.15, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.2975, 28955036.54104822, 12064598.55877009, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 415.42525808, 0.00057421, 506.43525478, 0.01539605, 50.64352548, 0.05125135, -415.42525808, -0.00057421, -506.43525478, -0.01539605, -50.64352548, -0.05125135, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 138.19322891, 0.00086396, 168.46814614, 0.01307017, 16.84681461, 0.03569234, -138.19322891, -0.00086396, -168.46814614, -0.01307017, -16.84681461, -0.03569234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 408.26215981, 0.01148414, 408.26215981, 0.03445241, 285.78351186, -5776.71357975, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 102.06553995, 9.213e-05, 306.19661985, 0.0002764, 1020.65539951, 0.00092135, -102.06553995, -9.213e-05, -306.19661985, -0.0002764, -1020.65539951, -0.00092135, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 195.97302286, 0.01727926, 195.97302286, 0.05183777, 137.181116, -1496.99710739, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 48.99325572, 4.423e-05, 146.97976715, 0.00013268, 489.93255715, 0.00044226, -48.99325572, -4.423e-05, -146.97976715, -0.00013268, -489.93255715, -0.00044226, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 29.7, 5.15, 8.9)
    ops.node(124016, 29.7, 5.15, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.15, 29679217.27517597, 12366340.53132332, 0.00230675, 0.00085938, 0.00495, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 141.79223345, 0.00061127, 172.48779827, 0.01903998, 17.24877983, 0.07438578, -141.79223345, -0.00061127, -172.48779827, -0.01903998, -17.24877983, -0.07438578, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 49.88726195, 0.00108286, 60.68699086, 0.01546606, 6.06869909, 0.0462096, -49.88726195, -0.00108286, -60.68699086, -0.01546606, -6.06869909, -0.0462096, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 203.7101883, 0.01222536, 203.7101883, 0.03667607, 142.59713181, -7341.84838452, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 50.92754707, 8.895e-05, 152.78264122, 0.00026686, 509.27547074, 0.00088954, -50.92754707, -8.895e-05, -152.78264122, -0.00026686, -509.27547074, -0.00088954, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 115.52156338, 0.02165714, 115.52156338, 0.06497143, 80.86509437, -1707.43881943, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 28.88039085, 5.044e-05, 86.64117254, 0.00015133, 288.80390846, 0.00050445, -28.88039085, -5.044e-05, -86.64117254, -0.00015133, -288.80390846, -0.00050445, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 10.3, 8.9)
    ops.node(124017, 0.0, 10.3, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0875, 27817500.66166507, 11590625.27569378, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 31.2350827, 0.00105913, 38.18065424, 0.01834271, 3.81806542, 0.06742509, -31.2350827, -0.00105913, -38.18065424, -0.01834271, -3.81806542, -0.06742509, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 50.94589966, 0.000811, 62.2744559, 0.02008444, 6.22744559, 0.08364482, -50.94589966, -0.000811, -62.2744559, -0.02008444, -6.22744559, -0.08364482, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 88.10447246, 0.02118269, 88.10447246, 0.06354806, 61.67313072, -3899.04115234, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 22.02611812, 7.037e-05, 66.07835435, 0.0002111, 220.26118115, 0.00070367, -22.02611812, -7.037e-05, -66.07835435, -0.0002111, -220.26118115, -0.00070367, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 105.87693648, 0.01622, 105.87693648, 0.04865999, 74.11385553, -7167.21635265, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 26.46923412, 8.456e-05, 79.40770236, 0.00025368, 264.69234119, 0.00084561, -26.46923412, -8.456e-05, -79.40770236, -0.00025368, -264.69234119, -0.00084561, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 4.45, 10.3, 8.925)
    ops.node(124018, 4.45, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1375, 29866529.81731981, 12444387.42388326, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 54.69519547, 0.00112139, 66.4938205, 0.01649028, 6.64938205, 0.04873712, -54.69519547, -0.00112139, -66.4938205, -0.01649028, -6.64938205, -0.04873712, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 147.88105062, 0.00064651, 179.78134917, 0.0199244, 17.97813492, 0.07512474, -147.88105062, -0.00064651, -179.78134917, -0.0199244, -17.97813492, -0.07512474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 112.11928763, 0.02242782, 112.11928763, 0.06728347, 78.48350134, -1735.11781505, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 28.02982191, 5.307e-05, 84.08946572, 0.00015922, 280.29821907, 0.00053075, -28.02982191, -5.307e-05, -84.08946572, -0.00015922, -280.29821907, -0.00053075, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 179.61662911, 0.01293012, 179.61662911, 0.03879035, 125.73164038, -6424.15579821, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 44.90415728, 8.503e-05, 134.71247183, 0.00025508, 449.04157278, 0.00085027, -44.90415728, -8.503e-05, -134.71247183, -0.00025508, -449.04157278, -0.00085027, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.9, 10.3, 8.925)
    ops.node(124019, 8.9, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1375, 29242134.9825918, 12184222.90941325, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 60.4514618, 0.00120659, 73.61346052, 0.0144612, 7.36134605, 0.04186017, -60.4514618, -0.00120659, -73.61346052, -0.0144612, -7.36134605, -0.04186017, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 150.64204969, 0.00067078, 183.44109883, 0.01693032, 18.34410988, 0.06141771, -150.64204969, -0.00067078, -183.44109883, -0.01693032, -18.34410988, -0.06141771, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 75.16775656, 0.02413188, 75.16775656, 0.07239565, 52.61742959, -1124.37089839, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 18.79193914, 3.634e-05, 56.37581742, 0.00010903, 187.9193914, 0.00036343, -18.79193914, -3.634e-05, -56.37581742, -0.00010903, -187.9193914, -0.00036343, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 156.50503919, 0.01341565, 156.50503919, 0.04024694, 109.55352743, -3878.7984273, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 39.1262598, 7.567e-05, 117.37877939, 0.000227, 391.26259797, 0.00075668, -39.1262598, -7.567e-05, -117.37877939, -0.000227, -391.26259797, -0.00075668, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 13.35, 10.3, 8.925)
    ops.node(124020, 13.35, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.125, 29487427.62516078, 12286428.17715032, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 39.66366596, 0.00107309, 48.2789003, 0.01587273, 4.82789003, 0.05437271, -39.66366596, -0.00107309, -48.2789003, -0.01587273, -4.82789003, -0.05437271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 100.5029763, 0.00065445, 122.33294768, 0.01898169, 12.23329477, 0.08291097, -100.5029763, -0.00065445, -122.33294768, -0.01898169, -12.23329477, -0.08291097, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 111.26027278, 0.02146175, 111.26027278, 0.06438525, 77.88219094, -2647.17485025, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 27.81506819, 5.868e-05, 83.44520458, 0.00017604, 278.15068194, 0.0005868, -27.81506819, -5.868e-05, -83.44520458, -0.00017604, -278.15068194, -0.0005868, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 166.56824477, 0.01308903, 166.56824477, 0.03926708, 116.59777134, -8899.15970862, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 41.64206119, 8.785e-05, 124.92618358, 0.00026355, 416.42061192, 0.0008785, -41.64206119, -8.785e-05, -124.92618358, -0.00026355, -416.42061192, -0.0008785, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 16.35, 10.3, 8.925)
    ops.node(124021, 16.35, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.125, 29304343.46012599, 12210143.10838583, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 39.76789534, 0.00105289, 48.42910767, 0.01557561, 4.84291077, 0.0540384, -39.76789534, -0.00105289, -48.42910767, -0.01557561, -4.84291077, -0.0540384, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 100.98592403, 0.00064957, 122.98006085, 0.01863389, 12.29800608, 0.0825014, -100.98592403, -0.00064957, -122.98006085, -0.01863389, -12.29800608, -0.0825014, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 109.26935604, 0.02105774, 109.26935604, 0.06317321, 76.48854923, -2511.73017484, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 27.31733901, 5.799e-05, 81.95201703, 0.00017397, 273.1733901, 0.0005799, -27.31733901, -5.799e-05, -81.95201703, -0.00017397, -273.1733901, -0.0005799, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 163.12947949, 0.0129914, 163.12947949, 0.03897421, 114.19063564, -8403.07363364, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 40.78236987, 8.657e-05, 122.34710961, 0.00025972, 407.82369871, 0.00086574, -40.78236987, -8.657e-05, -122.34710961, -0.00025972, -407.82369871, -0.00086574, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 20.8, 10.3, 8.925)
    ops.node(124022, 20.8, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.1375, 29156999.72786552, 12148749.88661063, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 61.82998293, 0.0011699, 75.30853145, 0.01411884, 7.53085314, 0.04150342, -61.82998293, -0.0011699, -75.30853145, -0.01411884, -7.53085314, -0.04150342, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 152.55266026, 0.00066471, 185.80818349, 0.01654929, 18.58081835, 0.0610133, -152.55266026, -0.00066471, -185.80818349, -0.01654929, -18.58081835, -0.0610133, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 74.828153, 0.02339801, 74.828153, 0.07019403, 52.3797071, -1083.21510529, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 18.70703825, 3.628e-05, 56.12111475, 0.00010885, 187.07038249, 0.00036284, -18.70703825, -3.628e-05, -56.12111475, -0.00010885, -187.07038249, -0.00036284, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 154.54955922, 0.01329426, 154.54955922, 0.03988277, 108.18469145, -3710.918056, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 38.6373898, 7.494e-05, 115.91216941, 0.00022482, 386.37389805, 0.00074941, -38.6373898, -7.494e-05, -115.91216941, -0.00022482, -386.37389805, -0.00074941, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 25.25, 10.3, 8.925)
    ops.node(124023, 25.25, 10.3, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1375, 29607508.99708243, 12336462.08211768, 0.00204719, 0.00381276, 0.00078776, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 55.44843876, 0.00107019, 67.45662755, 0.01663042, 6.74566276, 0.04882964, -55.44843876, -0.00107019, -67.45662755, -0.01663042, -6.74566276, -0.04882964, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 149.13819335, 0.00063521, 181.43629987, 0.02015311, 18.14362999, 0.07527194, -149.13819335, -0.00063521, -181.43629987, -0.02015311, -18.14362999, -0.07527194, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 111.63794155, 0.02140387, 111.63794155, 0.06421161, 78.14655909, -1738.98666041, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 27.90948539, 5.331e-05, 83.72845617, 0.00015993, 279.09485389, 0.00053309, -27.90948539, -5.331e-05, -83.72845617, -0.00015993, -279.09485389, -0.00053309, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 178.36667787, 0.01270427, 178.36667787, 0.03811281, 124.85667451, -6440.53460515, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 44.59166947, 8.517e-05, 133.77500841, 0.00025552, 445.91669469, 0.00085174, -44.59166947, -8.517e-05, -133.77500841, -0.00025552, -445.91669469, -0.00085174, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 29.7, 10.3, 8.9)
    ops.node(124024, 29.7, 10.3, 11.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0875, 31247713.66914677, 13019880.69547782, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 31.19105635, 0.00105911, 37.77762021, 0.01717921, 3.77776202, 0.06708653, -31.19105635, -0.00105911, -37.77762021, -0.01717921, -3.77776202, -0.06708653, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 50.59423184, 0.0008059, 61.27813223, 0.01878192, 6.12781322, 0.08341056, -50.59423184, -0.0008059, -61.27813223, -0.01878192, -6.12781322, -0.08341056, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 95.06844217, 0.02118225, 95.06844217, 0.06354675, 66.54790952, -3623.01892414, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 23.76711054, 6.759e-05, 71.30133163, 0.00020278, 237.67110542, 0.00067594, -23.76711054, -6.759e-05, -71.30133163, -0.00020278, -237.67110542, -0.00067594, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 112.12070498, 0.01611809, 112.12070498, 0.04835427, 78.48449349, -6643.60564439, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 28.03017625, 7.972e-05, 84.09052874, 0.00023915, 280.30176246, 0.00079718, -28.03017625, -7.972e-05, -84.09052874, -0.00023915, -280.30176246, -0.00079718, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.35, 0.0, 0.0)
    ops.node(124025, 13.35, 0.0, 1.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4062, 170004, 124025, 0.21, 28440869.5059365, 11850362.29414021, 0.00545409, 0.00693, 0.00235812, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24062, 262.1303785, 0.00076387, 317.76681055, 0.0366815, 31.77668105, 0.09041974, -262.1303785, -0.00076387, -317.76681055, -0.0366815, -31.77668105, -0.09041974, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14062, 347.08245379, 0.00062517, 420.74972374, 0.04416569, 42.07497237, 0.12899718, -347.08245379, -0.00062517, -420.74972374, -0.04416569, -42.07497237, -0.12899718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24062, 4062, 0.0, 333.10839108, 0.01527749, 333.10839108, 0.04583247, 233.17587376, -9913.01193807, 0.05, 2, 0, 70004, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44062, 83.27709777, 6.525e-05, 249.83129331, 0.00019576, 832.77097771, 0.00065254, -83.27709777, -6.525e-05, -249.83129331, -0.00019576, -832.77097771, -0.00065254, 0.4, 0.3, 0.003, 0.0, 0.0, 24062, 2)
    ops.limitCurve('ThreePoint', 14062, 4062, 0.0, 522.73890887, 0.0125035, 522.73890887, 0.0375105, 365.91723621, -21948.80021092, 0.05, 2, 0, 70004, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34062, 130.68472722, 0.0001024, 392.05418165, 0.00030721, 1306.84727217, 0.00102402, -130.68472722, -0.0001024, -392.05418165, -0.00030721, -1306.84727217, -0.00102402, 0.4, 0.3, 0.003, 0.0, 0.0, 14062, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4062, 99999, 'P', 44062, 'Vy', 34062, 'Vz', 24062, 'My', 14062, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4062, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4062, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 13.35, 0.0, 1.85)
    ops.node(121004, 13.35, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 174025, 121004, 0.21, 29066461.71069028, 12111025.71278762, 0.00545409, 0.00693, 0.00235812, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 134.79250256, 0.00072209, 163.33184867, 0.03466252, 16.33318487, 0.09042644, -134.79250256, -0.00072209, -163.33184867, -0.03466252, -16.33318487, -0.09042644, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 278.81736789, 0.00060106, 337.85080978, 0.04174476, 33.78508098, 0.129774, -278.81736789, -0.00060106, -337.85080978, -0.04174476, -33.78508098, -0.129774, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 335.58500787, 0.01444172, 335.58500787, 0.04332517, 234.90950551, -10273.43432732, 0.05, 2, 0, 74025, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 83.89625197, 6.432e-05, 251.6887559, 0.00019297, 838.96251967, 0.00064325, -83.89625197, -6.432e-05, -251.6887559, -0.00019297, -838.96251967, -0.00064325, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 526.40665973, 0.01202121, 526.40665973, 0.03606364, 368.48466181, -23156.91233027, 0.05, 2, 0, 74025, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 131.60166493, 0.0001009, 394.8049948, 0.0003027, 1316.01664933, 0.00100901, -131.60166493, -0.0001009, -394.8049948, -0.0003027, -1316.01664933, -0.00100901, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 16.35, 0.0, 0.0)
    ops.node(124026, 16.35, 0.0, 1.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 170005, 124026, 0.21, 28002062.98764221, 11667526.24485092, 0.00545409, 0.00693, 0.00235812, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 261.54614643, 0.00077889, 317.27125231, 0.03622155, 31.72712523, 0.08924277, -261.54614643, -0.00077889, -317.27125231, -0.03622155, -31.72712523, -0.08924277, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 348.01154906, 0.00063249, 422.15900137, 0.04359723, 42.21590014, 0.12729685, -348.01154906, -0.00063249, -422.15900137, -0.04359723, -42.21590014, -0.12729685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 324.1647449, 0.01557781, 324.1647449, 0.04673344, 226.91532143, -9446.40430187, 0.05, 2, 0, 70005, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 81.04118623, 6.45e-05, 243.12355868, 0.00019349, 810.41186225, 0.00064497, -81.04118623, -6.45e-05, -243.12355868, -0.00019349, -810.41186225, -0.00064497, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 508.38781265, 0.0126497, 508.38781265, 0.03794911, 355.87146885, -20760.73341756, 0.05, 2, 0, 70005, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 127.09695316, 0.00010115, 381.29085949, 0.00030345, 1270.96953162, 0.00101151, -127.09695316, -0.00010115, -381.29085949, -0.00030345, -1270.96953162, -0.00101151, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 16.35, 0.0, 1.85)
    ops.node(121005, 16.35, 0.0, 2.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 174026, 121005, 0.21, 30064246.19062177, 12526769.24609241, 0.00545409, 0.00693, 0.00235812, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 135.6785688, 0.00071185, 164.06510215, 0.03431431, 16.40651021, 0.09137173, -135.6785688, -0.00071185, -164.06510215, -0.03431431, -16.40651021, -0.09137173, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 280.42369911, 0.00059618, 339.09366266, 0.04133018, 33.90936627, 0.13140135, -280.42369911, -0.00059618, -339.09366266, -0.04133018, -33.90936627, -0.13140135, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 341.76258774, 0.01423691, 341.76258774, 0.04271074, 239.23381142, -10035.72199575, 0.05, 2, 0, 74026, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 85.44064694, 6.333e-05, 256.32194081, 0.00019, 854.40646935, 0.00063335, -85.44064694, -6.333e-05, -256.32194081, -0.00019, -854.40646935, -0.00063335, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 534.71463325, 0.0119235, 534.71463325, 0.03577051, 374.30024328, -22545.60897282, 0.05, 2, 0, 74026, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 133.67865831, 9.909e-05, 401.03597494, 0.00029728, 1336.78658314, 0.00099092, -133.67865831, -9.909e-05, -401.03597494, -0.00029728, -1336.78658314, -0.00099092, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.35, 0.0, 3.525)
    ops.node(124027, 13.35, 0.0, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4067, 171004, 124027, 0.21, 29855066.03650594, 12439610.84854414, 0.00545409, 0.00693, 0.00235812, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24067, 171.94891203, 0.00069308, 208.29558398, 0.04124759, 20.8295584, 0.12423294, -171.94891203, -0.00069308, -208.29558398, -0.04124759, -20.8295584, -0.12423294, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14067, 251.13040291, 0.00060634, 304.21450949, 0.04320879, 30.42145095, 0.13648126, -251.13040291, -0.00060634, -304.21450949, -0.04320879, -30.42145095, -0.13648126, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24067, 4067, 0.0, 374.02050709, 0.01386169, 374.02050709, 0.04158508, 261.81435496, -13840.29516391, 0.05, 2, 0, 71004, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44067, 93.50512677, 5.799e-05, 280.51538031, 0.00017396, 935.05126771, 0.00057986, -93.50512677, -5.799e-05, -280.51538031, -0.00017396, -935.05126771, -0.00057986, 0.4, 0.3, 0.003, 0.0, 0.0, 24067, 2)
    ops.limitCurve('ThreePoint', 14067, 4067, 0.0, 657.43199576, 0.01212679, 657.43199576, 0.03638037, 460.20239703, -65498.52879007, 0.05, 2, 0, 71004, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34067, 164.35799894, 0.00010192, 493.07399682, 0.00030577, 1643.57998939, 0.00101925, -164.35799894, -0.00010192, -493.07399682, -0.00030577, -1643.57998939, -0.00101925, 0.4, 0.3, 0.003, 0.0, 0.0, 14067, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4067, 99999, 'P', 44067, 'Vy', 34067, 'Vz', 24067, 'My', 14067, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4067, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4067, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 13.35, 0.0, 4.925)
    ops.node(122004, 13.35, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 174027, 122004, 0.21, 28802750.10365355, 12001145.87652231, 0.00545409, 0.00693, 0.00235812, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 141.94182336, 0.00068767, 172.45447965, 0.04112942, 17.24544796, 0.12414828, -141.94182336, -0.00068767, -172.45447965, -0.04112942, -17.24544796, -0.12414828, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 216.6501215, 0.00060325, 263.2225167, 0.04308725, 26.32225167, 0.13639739, -216.6501215, -0.00060325, -263.2225167, -0.04308725, -26.32225167, -0.13639739, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 353.55538603, 0.01375338, 353.55538603, 0.04126013, 247.48877022, -13935.0543914, 0.05, 2, 0, 74027, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 88.38884651, 5.682e-05, 265.16653952, 0.00017045, 883.88846508, 0.00056816, -88.38884651, -5.682e-05, -265.16653952, -0.00017045, -883.88846508, -0.00056816, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 625.28934977, 0.01206506, 625.28934977, 0.03619518, 437.70254484, -67455.23543355, 0.05, 2, 0, 74027, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 156.32233744, 0.00010048, 468.96701232, 0.00030145, 1563.22337442, 0.00100483, -156.32233744, -0.00010048, -468.96701232, -0.00030145, -1563.22337442, -0.00100483, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 16.35, 0.0, 3.525)
    ops.node(124028, 16.35, 0.0, 4.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 171005, 124028, 0.21, 29308508.27293496, 12211878.44705623, 0.00545409, 0.00693, 0.00235812, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 171.52949267, 0.00069086, 208.04171952, 0.04097347, 20.80417195, 0.12313191, -171.52949267, -0.00069086, -208.04171952, -0.04097347, -20.80417195, -0.12313191, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 249.72191694, 0.00060544, 302.87839248, 0.04292227, 30.28783925, 0.13526532, -249.72191694, -0.00060544, -302.87839248, -0.04292227, -30.28783925, -0.13526532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 364.18030845, 0.01381711, 364.18030845, 0.04145133, 254.92621592, -13274.87932214, 0.05, 2, 0, 71005, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 91.04507711, 5.751e-05, 273.13523134, 0.00017254, 910.45077113, 0.00057513, -91.04507711, -5.751e-05, -273.13523134, -0.00017254, -910.45077113, -0.00057513, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 639.87022084, 0.01210882, 639.87022084, 0.03632647, 447.90915459, -62341.63197394, 0.05, 2, 0, 71005, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 159.96755521, 0.00010105, 479.90266563, 0.00030316, 1599.67555211, 0.00101052, -159.96755521, -0.00010105, -479.90266563, -0.00030316, -1599.67555211, -0.00101052, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 16.35, 0.0, 4.925)
    ops.node(122005, 16.35, 0.0, 5.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 174028, 122005, 0.21, 29822002.39648008, 12425834.3318667, 0.00545409, 0.00693, 0.00235812, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 142.33034169, 0.00069356, 172.5347304, 0.04041124, 17.25347304, 0.12487127, -142.33034169, -0.00069356, -172.5347304, -0.04041124, -17.25347304, -0.12487127, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 218.64580267, 0.00060557, 265.0453457, 0.04232894, 26.50453457, 0.13725889, -218.64580267, -0.00060557, -265.0453457, -0.04232894, -26.50453457, -0.13725889, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 364.09106105, 0.01387114, 364.09106105, 0.04161343, 254.86374273, -13944.51317551, 0.05, 2, 0, 74028, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 91.02276526, 5.651e-05, 273.06829578, 0.00016953, 910.22765261, 0.00056509, -91.02276526, -5.651e-05, -273.06829578, -0.00016953, -910.22765261, -0.00056509, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 638.07707457, 0.01211139, 638.07707457, 0.03633418, 446.6539522, -67508.75045545, 0.05, 2, 0, 74028, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 159.51926864, 9.903e-05, 478.55780593, 0.0002971, 1595.19268642, 0.00099034, -159.51926864, -9.903e-05, -478.55780593, -0.0002971, -1595.19268642, -0.00099034, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.35, 0.0, 6.225)
    ops.node(124029, 13.35, 0.0, 7.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4072, 172004, 124029, 0.125, 29864763.85110749, 12443651.60462812, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24072, 65.32859134, 0.00086051, 79.10719646, 0.03759903, 7.91071965, 0.10549587, -65.32859134, -0.00086051, -79.10719646, -0.03759903, -7.91071965, -0.10549587, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14072, 155.89859876, 0.00062431, 188.77953478, 0.04814104, 18.87795348, 0.14814104, -155.89859876, -0.00062431, -188.77953478, -0.04814104, -18.87795348, -0.14814104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24072, 4072, 0.0, 199.17828289, 0.0172101, 199.17828289, 0.05163031, 139.42479802, -9810.38877215, 0.05, 2, 0, 72004, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44072, 49.79457072, 5.186e-05, 149.38371217, 0.00015558, 497.94570722, 0.00051861, -49.79457072, -5.186e-05, -149.38371217, -0.00015558, -497.94570722, -0.00051861, 0.4, 0.3, 0.003, 0.0, 0.0, 24072, 2)
    ops.limitCurve('ThreePoint', 14072, 4072, 0.0, 368.41529612, 0.0124862, 368.41529612, 0.03745859, 257.89070729, -30431.54153396, 0.05, 2, 0, 72004, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34072, 92.10382403, 9.593e-05, 276.31147209, 0.00028778, 921.03824031, 0.00095926, -92.10382403, -9.593e-05, -276.31147209, -0.00028778, -921.03824031, -0.00095926, 0.4, 0.3, 0.003, 0.0, 0.0, 14072, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4072, 99999, 'P', 44072, 'Vy', 34072, 'Vz', 24072, 'My', 14072, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4072, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4072, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 13.35, 0.0, 7.5)
    ops.node(123004, 13.35, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 174029, 123004, 0.125, 28663243.73848553, 11943018.22436897, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 68.94850464, 0.0008481, 83.80514822, 0.03872988, 8.38051482, 0.10747955, -68.94850464, -0.0008481, -83.80514822, -0.03872988, -8.38051482, -0.10747955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 134.31922395, 0.00062257, 163.26158966, 0.04961796, 16.32615897, 0.14961796, -134.31922395, -0.00062257, -163.26158966, -0.04961796, -16.32615897, -0.14961796, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 193.34786819, 0.01696193, 193.34786819, 0.0508858, 135.34350773, -11503.19891681, 0.05, 2, 0, 74029, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 48.33696705, 5.245e-05, 145.01090114, 0.00015736, 483.36967047, 0.00052453, -48.33696705, -5.245e-05, -145.01090114, -0.00015736, -483.36967047, -0.00052453, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 359.38194999, 0.01245148, 359.38194999, 0.03735443, 251.567365, -37348.05492021, 0.05, 2, 0, 74029, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 89.8454875, 9.75e-05, 269.5364625, 0.00029249, 898.45487499, 0.00097496, -89.8454875, -9.75e-05, -269.5364625, -0.00029249, -898.45487499, -0.00097496, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 16.35, 0.0, 6.225)
    ops.node(124030, 16.35, 0.0, 7.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 172005, 124030, 0.125, 30559715.08953976, 12733214.62064156, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 65.41765718, 0.0008677, 79.0832639, 0.03765908, 7.90832639, 0.10640478, -65.41765718, -0.0008677, -79.0832639, -0.03765908, -7.90832639, -0.10640478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 156.01690733, 0.00062551, 188.60850093, 0.0482106, 18.86085009, 0.1482106, -156.01690733, -0.00062551, -188.60850093, -0.0482106, -18.86085009, -0.1482106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 206.63653536, 0.01735393, 206.63653536, 0.05206179, 144.64557475, -10448.72896893, 0.05, 2, 0, 72005, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 51.65913384, 5.258e-05, 154.97740152, 0.00015774, 516.59133841, 0.00052579, -51.65913384, -5.258e-05, -154.97740152, -0.00015774, -516.59133841, -0.00052579, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 382.35986119, 0.01251014, 382.35986119, 0.03753042, 267.65190284, -32684.8872257, 0.05, 2, 0, 72005, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 95.5899653, 9.729e-05, 286.7698959, 0.00029188, 955.89965298, 0.00097292, -95.5899653, -9.729e-05, -286.7698959, -0.00029188, -955.89965298, -0.00097292, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 16.35, 0.0, 7.5)
    ops.node(123005, 16.35, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174030, 123005, 0.125, 30179067.18952144, 12574611.32896727, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 68.33986646, 0.0007868, 82.77975966, 0.03824284, 8.27797597, 0.10870457, -68.33986646, -0.0007868, -82.77975966, -0.03824284, -8.27797597, -0.10870457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 131.71742845, 0.00059708, 159.54870319, 0.04904182, 15.95487032, 0.14904182, -131.71742845, -0.00059708, -159.54870319, -0.04904182, -15.95487032, -0.14904182, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 200.44851203, 0.01573595, 200.44851203, 0.04720786, 140.31395842, -11585.00653381, 0.05, 2, 0, 74030, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 50.11212801, 5.165e-05, 150.33638402, 0.00015494, 501.12128008, 0.00051648, -50.11212801, -5.165e-05, -150.33638402, -0.00015494, -501.12128008, -0.00051648, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 371.51083913, 0.0119415, 371.51083913, 0.0358245, 260.05758739, -37642.92656323, 0.05, 2, 0, 74030, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 92.87770978, 9.572e-05, 278.63312935, 0.00028717, 928.77709782, 0.00095724, -92.87770978, -9.572e-05, -278.63312935, -0.00028717, -928.77709782, -0.00095724, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.35, 0.0, 8.925)
    ops.node(124031, 13.35, 0.0, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 173004, 124031, 0.125, 28529746.39561564, 11887394.33150652, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 55.25592621, 0.00082792, 67.37473881, 0.02472657, 6.73747388, 0.06840658, -55.25592621, -0.00082792, -67.37473881, -0.02472657, -6.73747388, -0.06840658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 134.87924107, 0.00061126, 164.46115848, 0.0305852, 16.44611585, 0.10533783, -134.87924107, -0.00061126, -164.46115848, -0.0305852, -16.44611585, -0.10533783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 132.66906445, 0.01655839, 132.66906445, 0.04967516, 92.86834511, -6179.69397548, 0.05, 2, 0, 73004, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 33.16726611, 3.616e-05, 99.50179834, 0.00010848, 331.67266112, 0.0003616, -33.16726611, -3.616e-05, -99.50179834, -0.00010848, -331.67266112, -0.0003616, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 240.57983889, 0.01222517, 240.57983889, 0.0366755, 168.40588722, -20413.92526331, 0.05, 2, 0, 73004, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 60.14495972, 6.557e-05, 180.43487917, 0.00019672, 601.44959723, 0.00065572, -60.14495972, -6.557e-05, -180.43487917, -0.00019672, -601.44959723, -0.00065572, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 13.35, 0.0, 10.2)
    ops.node(124004, 13.35, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 174031, 124004, 0.125, 30502924.87761529, 12709552.03233971, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 53.4082621, 0.0008063, 64.8544809, 0.01945227, 6.48544809, 0.05866225, -53.4082621, -0.0008063, -64.8544809, -0.01945227, -6.48544809, -0.05866225, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 131.028247, 0.0006026, 159.10963227, 0.02369297, 15.91096323, 0.08880121, -131.028247, -0.0006026, -159.10963227, -0.02369297, -15.91096323, -0.08880121, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 125.31292287, 0.01612597, 125.31292287, 0.0483779, 87.71904601, -6585.72552691, 0.05, 2, 0, 74031, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 31.32823072, 3.195e-05, 93.98469215, 9.584e-05, 313.28230716, 0.00031946, -31.32823072, -3.195e-05, -93.98469215, -9.584e-05, -313.28230716, -0.00031946, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 224.30797027, 0.01205199, 224.30797027, 0.03615598, 157.01557919, -23209.86420736, 0.05, 2, 0, 74031, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 56.07699257, 5.718e-05, 168.2309777, 0.00017155, 560.76992567, 0.00057182, -56.07699257, -5.718e-05, -168.2309777, -0.00017155, -560.76992567, -0.00057182, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 16.35, 0.0, 8.925)
    ops.node(124032, 16.35, 0.0, 9.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 173005, 124032, 0.125, 30093328.57870268, 12538886.90779278, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 54.79978864, 0.000806, 66.55371306, 0.0244205, 6.65537131, 0.06861692, -54.79978864, -0.000806, -66.55371306, -0.0244205, -6.65537131, -0.06861692, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 133.50812118, 0.00060036, 162.14407771, 0.03021791, 16.21440777, 0.10585432, -133.50812118, -0.00060036, -162.14407771, -0.03021791, -16.21440777, -0.10585432, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 139.51796777, 0.01612008, 139.51796777, 0.04836024, 97.66257744, -6199.27539036, 0.05, 2, 0, 73005, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 34.87949194, 3.605e-05, 104.63847582, 0.00010815, 348.79491942, 0.00036051, -34.87949194, -3.605e-05, -104.63847582, -0.00010815, -348.79491942, -0.00036051, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 252.1697033, 0.01200725, 252.1697033, 0.03602175, 176.51879231, -20485.11023642, 0.05, 2, 0, 73005, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 63.04242583, 6.516e-05, 189.12727748, 0.00019548, 630.42425826, 0.0006516, -63.04242583, -6.516e-05, -189.12727748, -0.00019548, -630.42425826, -0.0006516, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 16.35, 0.0, 10.2)
    ops.node(124005, 16.35, 0.0, 11.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174032, 124005, 0.125, 30243504.65360117, 12601460.27233382, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 52.24342825, 0.00079347, 63.48822709, 0.02024133, 6.34882271, 0.05941983, -52.24342825, -0.00079347, -63.48822709, -0.02024133, -6.34882271, -0.05941983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 128.19891469, 0.00059582, 155.79226097, 0.02467921, 15.5792261, 0.08973517, -128.19891469, -0.00059582, -155.79226097, -0.02467921, -15.5792261, -0.08973517, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 126.67010639, 0.01586949, 126.67010639, 0.04760847, 88.66907447, -7307.37015012, 0.05, 2, 0, 74032, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 31.6675266, 3.257e-05, 95.00257979, 9.771e-05, 316.67526597, 0.00032569, -31.6675266, -3.257e-05, -95.00257979, -9.771e-05, -316.67526597, -0.00032569, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 227.37939626, 0.01191646, 227.37939626, 0.03574939, 159.16557738, -25923.95842165, 0.05, 2, 0, 74032, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 56.84484906, 5.846e-05, 170.53454719, 0.00017539, 568.44849064, 0.00058462, -56.84484906, -5.846e-05, -170.53454719, -0.00017539, -568.44849064, -0.00058462, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 4080, '-orient', 0, 0, 1, 0, 1, 0)
