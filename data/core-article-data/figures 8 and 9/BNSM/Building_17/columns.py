import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 8.5, 0.0, 0.0)
    ops.node(121003, 8.5, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.175, 27740401.98307873, 11558500.8262828, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 170.13311527, 0.00101907, 205.83784152, 0.03711426, 20.58378415, 0.09294726, -170.13311527, -0.00101907, -205.83784152, -0.03711426, -20.58378415, -0.09294726, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 199.13454302, 0.00078819, 240.92560959, 0.04186808, 24.09256096, 0.11775291, -199.13454302, -0.00078819, -240.92560959, -0.04186808, -24.09256096, -0.11775291, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 240.15942279, 0.02038137, 240.15942279, 0.06114411, 168.11159596, -4522.25161137, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 60.0398557, 9.795e-05, 180.11956709, 0.00029386, 600.39855698, 0.00097952, -60.0398557, -9.795e-05, -180.11956709, -0.00029386, -600.39855698, -0.00097952, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 312.75997139, 0.01576389, 312.75997139, 0.04729166, 218.93197997, -7249.34943508, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 78.18999285, 0.00012756, 234.56997854, 0.00038269, 781.89992848, 0.00127563, -78.18999285, -0.00012756, -234.56997854, -0.00038269, -781.89992848, -0.00127563, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.85, 0.0, 0.0)
    ops.node(121004, 13.85, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.075, 31407283.37034314, 13086368.07097631, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 48.47050983, 0.00136846, 58.13554702, 0.01865986, 5.8135547, 0.06119719, -48.47050983, -0.00136846, -58.13554702, -0.01865986, -5.8135547, -0.06119719, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 63.28323064, 0.00114405, 75.90192972, 0.01950785, 7.59019297, 0.06857133, -63.28323064, -0.00114405, -75.90192972, -0.01950785, -7.59019297, -0.06857133, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 103.93384546, 0.02736914, 103.93384546, 0.08210743, 72.75369182, -1451.84038618, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 25.98346137, 8.736e-05, 77.9503841, 0.00026209, 259.83461366, 0.00087364, -25.98346137, -8.736e-05, -77.9503841, -0.00026209, -259.83461366, -0.00087364, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 112.50599522, 0.0228809, 112.50599522, 0.06864271, 78.75419666, -1758.177417, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 28.12649881, 9.457e-05, 84.37949642, 0.00028371, 281.26498806, 0.00094569, -28.12649881, -9.457e-05, -84.37949642, -0.00028371, -281.26498806, -0.00094569, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.2, 0.0)
    ops.node(121005, 0.0, 4.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.075, 30869879.35122587, 12862449.72967745, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 64.07604109, 0.00108463, 76.88396228, 0.01839502, 7.68839623, 0.06556222, -64.07604109, -0.00108463, -76.88396228, -0.01839502, -7.68839623, -0.06556222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 48.92481738, 0.00128555, 58.7042169, 0.01758507, 5.87042169, 0.05847834, -48.92481738, -0.00128555, -58.7042169, -0.01758507, -5.87042169, -0.05847834, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 107.71785512, 0.02169258, 107.71785512, 0.06507774, 75.40249858, -1591.55442727, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 26.92946378, 9.212e-05, 80.78839134, 0.00027636, 269.2946378, 0.00092121, -26.92946378, -9.212e-05, -80.78839134, -0.00027636, -269.2946378, -0.00092121, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 99.88973726, 0.02571108, 99.88973726, 0.07713325, 69.92281608, -1332.64571766, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 24.97243432, 8.543e-05, 74.91730295, 0.00025628, 249.72434315, 0.00085426, -24.97243432, -8.543e-05, -74.91730295, -0.00025628, -249.72434315, -0.00085426, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 3.15, 4.2, 0.0)
    ops.node(121006, 3.15, 4.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.165, 30799367.16867132, 12833069.65361305, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 295.77833358, 0.00075744, 355.31411192, 0.05177899, 35.53141119, 0.14257864, -295.77833358, -0.00075744, -355.31411192, -0.05177899, -35.53141119, -0.14257864, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 196.17522818, 0.00116786, 235.66238317, 0.04208901, 23.56623832, 0.09589413, -196.17522818, -0.00116786, -235.66238317, -0.04208901, -23.56623832, -0.09589413, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 415.94127447, 0.01514873, 415.94127447, 0.04544619, 291.15889213, -10794.02779906, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 103.98531862, 0.00016206, 311.95595586, 0.00048618, 1039.85318619, 0.00162058, -103.98531862, -0.00016206, -311.95595586, -0.00048618, -1039.85318619, -0.00162058, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 266.16069232, 0.02335726, 266.16069232, 0.07007178, 186.31248463, -4798.16563881, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 66.54017308, 0.0001037, 199.62051924, 0.0003111, 665.40173081, 0.00103701, -66.54017308, -0.0001037, -199.62051924, -0.0003111, -665.40173081, -0.00103701, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.5, 4.2, 0.0)
    ops.node(121007, 8.5, 4.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.28, 30362611.69571528, 12651088.20654804, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 577.46533046, 0.00068953, 696.3505465, 0.04595444, 69.63505465, 0.12173296, -577.46533046, -0.00068953, -696.3505465, -0.04595444, -69.63505465, -0.12173296, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 451.75351328, 0.00094085, 544.75790885, 0.04375564, 54.47579089, 0.11016326, -451.75351328, -0.00094085, -544.75790885, -0.04375564, -54.47579089, -0.11016326, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 689.42761596, 0.01379069, 689.42761596, 0.04137208, 482.59933117, -16797.42065584, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 172.35690399, 0.00016057, 517.07071197, 0.0004817, 1723.56903989, 0.00160567, -172.35690399, -0.00016057, -517.07071197, -0.0004817, -1723.56903989, -0.00160567, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 339.18455467, 0.01881697, 339.18455467, 0.05645092, 237.42918827, -4698.62765143, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 84.79613867, 7.9e-05, 254.388416, 0.00023699, 847.96138666, 0.00078996, -84.79613867, -7.9e-05, -254.388416, -0.00023699, -847.96138666, -0.00078996, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.85, 4.2, 0.0)
    ops.node(121008, 13.85, 4.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.15, 29667241.18818079, 12361350.49507533, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 190.68073879, 0.00077876, 229.79599904, 0.03281432, 22.9795999, 0.09607235, -190.68073879, -0.00077876, -229.79599904, -0.03281432, -22.9795999, -0.09607235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 138.75928364, 0.0011185, 167.22364519, 0.02802337, 16.72236452, 0.06983599, -138.75928364, -0.0011185, -167.22364519, -0.02802337, -16.72236452, -0.06983599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 264.21589394, 0.0155752, 264.21589394, 0.04672559, 184.95112576, -5057.75348829, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 66.05397349, 0.00011756, 198.16192046, 0.00035268, 660.53973485, 0.00117559, -66.05397349, -0.00011756, -198.16192046, -0.00035268, -660.53973485, -0.00117559, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 191.71079746, 0.02237004, 191.71079746, 0.06711012, 134.19755822, -2776.538277, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 47.92769936, 8.53e-05, 143.78309809, 0.0002559, 479.27699365, 0.00085299, -47.92769936, -8.53e-05, -143.78309809, -0.0002559, -479.27699365, -0.00085299, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.4, 0.0)
    ops.node(121009, 0.0, 8.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.075, 31745954.51912984, 13227481.04963744, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 63.49634737, 0.00111297, 76.06096961, 0.0192274, 7.60609696, 0.06808036, -63.49634737, -0.00111297, -76.06096961, -0.0192274, -7.60609696, -0.06808036, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 48.73299686, 0.00132919, 58.37625543, 0.01838578, 5.83762554, 0.06074059, -48.73299686, -0.00132919, -58.37625543, -0.01838578, -5.83762554, -0.06074059, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 110.17035745, 0.0222594, 110.17035745, 0.06677819, 77.11925021, -1610.25680248, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 27.54258936, 9.162e-05, 82.62776808, 0.00027485, 275.42589361, 0.00091618, -27.54258936, -9.162e-05, -82.62776808, -0.00027485, -275.42589361, -0.00091618, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 102.25494187, 0.02658371, 102.25494187, 0.07975112, 71.57845931, -1345.4251502, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 25.56373547, 8.504e-05, 76.6912064, 0.00025511, 255.63735468, 0.00085035, -25.56373547, -8.504e-05, -76.6912064, -0.00025511, -255.63735468, -0.00085035, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 3.15, 8.4, 0.0)
    ops.node(121010, 3.15, 8.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.165, 30205609.85479016, 12585670.77282923, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 303.31244853, 0.00081119, 364.92550994, 0.04892863, 36.49255099, 0.13897117, -303.31244853, -0.00081119, -364.92550994, -0.04892863, -36.49255099, -0.13897117, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 198.59123765, 0.0012885, 238.9318639, 0.03988044, 23.89318639, 0.09323693, -198.59123765, -0.0012885, -238.9318639, -0.03988044, -23.89318639, -0.09323693, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 361.28252115, 0.01622378, 361.28252115, 0.04867133, 252.8977648, -8024.24909573, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 90.32063029, 0.00014353, 270.96189086, 0.00043059, 903.20630287, 0.00143529, -90.32063029, -0.00014353, -270.96189086, -0.00043059, -903.20630287, -0.00143529, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 235.02763817, 0.02577007, 235.02763817, 0.0773102, 164.51934672, -3747.31646567, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 58.75690954, 9.337e-05, 176.27072863, 0.00028011, 587.56909542, 0.00093371, -58.75690954, -9.337e-05, -176.27072863, -0.00028011, -587.56909542, -0.00093371, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.5, 8.4, 0.0)
    ops.node(121011, 8.5, 8.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.28, 30030246.22341901, 12512602.59309125, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 568.37034238, 0.00068331, 685.85130234, 0.04660384, 68.58513023, 0.1216819, -568.37034238, -0.00068331, -685.85130234, -0.04660384, -68.58513023, -0.1216819, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 443.68030645, 0.00093156, 535.38809701, 0.04436648, 53.5388097, 0.11016026, -443.68030645, -0.00093156, -535.38809701, -0.04436648, -53.5388097, -0.11016026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 697.11093558, 0.0136663, 697.11093558, 0.0409989, 487.9776549, -17684.60442671, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 174.27773389, 0.00016415, 522.83320168, 0.00049246, 1742.77733895, 0.00164154, -174.27773389, -0.00016415, -522.83320168, -0.00049246, -1742.77733895, -0.00164154, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 341.02305005, 0.01863123, 341.02305005, 0.05589368, 238.71613503, -4876.7353465, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 85.25576251, 8.03e-05, 255.76728753, 0.00024091, 852.55762512, 0.00080303, -85.25576251, -8.03e-05, -255.76728753, -0.00024091, -852.55762512, -0.00080303, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.85, 8.4, 0.0)
    ops.node(121012, 13.85, 8.4, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.15, 31755276.53861723, 13231365.22442385, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 185.36191325, 0.00077217, 222.43415354, 0.0322432, 22.24341535, 0.09985242, -185.36191325, -0.00077217, -222.43415354, -0.0322432, -22.24341535, -0.09985242, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 128.73834311, 0.00114766, 154.48591287, 0.02757841, 15.44859129, 0.0722671, -128.73834311, -0.00114766, -154.48591287, -0.02757841, -15.44859129, -0.0722671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 272.70646383, 0.01544343, 272.70646383, 0.0463303, 190.89452468, -4914.1983409, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 68.17661596, 0.00011336, 204.52984787, 0.00034008, 681.76615957, 0.00113358, -68.17661596, -0.00011336, -204.52984787, -0.00034008, -681.76615957, -0.00113358, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 199.78750419, 0.02295329, 199.78750419, 0.06885988, 139.85125293, -2712.63292739, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 49.94687605, 8.305e-05, 149.84062814, 0.00024914, 499.46876047, 0.00083047, -49.94687605, -8.305e-05, -149.84062814, -0.00024914, -499.46876047, -0.00083047, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 12.6, 0.0)
    ops.node(121013, 0.0, 12.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.075, 31310018.02162411, 13045840.84234338, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 65.04428251, 0.00108592, 77.98878721, 0.01950333, 7.79887872, 0.06763567, -65.04428251, -0.00108592, -77.98878721, -0.01950333, -7.79887872, -0.06763567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 49.5357415, 0.00128344, 59.39388143, 0.01862532, 5.93938814, 0.06035537, -49.5357415, -0.00128344, -59.39388143, -0.01862532, -5.93938814, -0.06035537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 111.56055115, 0.02171831, 111.56055115, 0.06515493, 78.09238581, -1697.13092702, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 27.89013779, 9.407e-05, 83.67041336, 0.0002822, 278.90137788, 0.00094066, -27.89013779, -9.407e-05, -83.67041336, -0.0002822, -278.90137788, -0.00094066, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 103.23641206, 0.02566871, 103.23641206, 0.07700613, 72.26548844, -1411.5229785, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 25.80910301, 8.705e-05, 77.42730904, 0.00026114, 258.09103014, 0.00087047, -25.80910301, -8.705e-05, -77.42730904, -0.00026114, -258.09103014, -0.00087047, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 3.15, 12.6, 0.0)
    ops.node(121014, 3.15, 12.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.165, 29173225.20600023, 12155510.50250009, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 292.84940974, 0.00077214, 352.90378338, 0.05216411, 35.29037834, 0.13862332, -292.84940974, -0.00077214, -352.90378338, -0.05216411, -35.29037834, -0.13862332, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 196.21315811, 0.00119157, 236.45041971, 0.0424098, 23.64504197, 0.09364292, -196.21315811, -0.00119157, -236.45041971, -0.0424098, -23.64504197, -0.09364292, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 391.72631782, 0.01544274, 391.72631782, 0.04632821, 274.20842247, -10237.40665807, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 97.93157945, 0.00016113, 293.79473836, 0.00048339, 979.31579454, 0.00161131, -97.93157945, -0.00016113, -293.79473836, -0.00048339, -979.31579454, -0.00161131, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 250.03129109, 0.02383139, 250.03129109, 0.07149418, 175.02190377, -4562.1428091, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 62.50782277, 0.00010285, 187.52346832, 0.00030854, 625.07822774, 0.00102847, -62.50782277, -0.00010285, -187.52346832, -0.00030854, -625.07822774, -0.00102847, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.5, 12.6, 0.0)
    ops.node(121015, 8.5, 12.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.28, 31236704.02526855, 13015293.3438619, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 581.71640605, 0.00069579, 700.08479014, 0.04878984, 70.00847901, 0.12628739, -581.71640605, -0.00069579, -700.08479014, -0.04878984, -70.00847901, -0.12628739, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 446.69048086, 0.00096, 537.58362029, 0.0464508, 53.75836203, 0.11436487, -446.69048086, -0.00096, -537.58362029, -0.0464508, -53.75836203, -0.11436487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 798.52465374, 0.01391579, 798.52465374, 0.04174737, 558.96725762, -24346.84672316, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 199.63116343, 0.00018077, 598.8934903, 0.00054231, 1996.31163435, 0.00180772, -199.63116343, -0.00018077, -598.8934903, -0.00054231, -1996.31163435, -0.00180772, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 383.64018312, 0.0192, 383.64018312, 0.05759999, 268.54812819, -6180.32905118, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 95.91004578, 8.685e-05, 287.73013734, 0.00026055, 959.10045781, 0.00086849, -95.91004578, -8.685e-05, -287.73013734, -0.00026055, -959.10045781, -0.00086849, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.85, 12.6, 0.0)
    ops.node(121016, 13.85, 12.6, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.15, 29536797.98176469, 12306999.15906862, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 187.60490677, 0.00077348, 226.13664159, 0.02894367, 22.61366416, 0.09189549, -187.60490677, -0.00077348, -226.13664159, -0.02894367, -22.61366416, -0.09189549, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 135.23458105, 0.00111728, 163.01009666, 0.02477583, 16.30100967, 0.06638605, -135.23458105, -0.00111728, -163.01009666, -0.02477583, -16.30100967, -0.06638605, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 237.15698834, 0.01546968, 237.15698834, 0.04640903, 166.00989184, -3870.15701325, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 59.28924709, 0.00010599, 177.86774126, 0.00031796, 592.89247085, 0.00105985, -59.28924709, -0.00010599, -177.86774126, -0.00031796, -592.89247085, -0.00105985, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 175.29277063, 0.02234553, 175.29277063, 0.06703659, 122.70493944, -2241.87935049, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 43.82319266, 7.834e-05, 131.46957797, 0.00023502, 438.23192658, 0.00078338, -43.82319266, -7.834e-05, -131.46957797, -0.00023502, -438.23192658, -0.00078338, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 16.8, 0.0)
    ops.node(121017, 0.0, 16.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.075, 32686810.6782801, 13619504.44928337, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 66.41608028, 0.00105716, 79.37617201, 0.01912321, 7.9376172, 0.06942499, -66.41608028, -0.00105716, -79.37617201, -0.01912321, -7.9376172, -0.06942499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 50.45018899, 0.00124164, 60.29477894, 0.01825268, 6.02947789, 0.0618636, -50.45018899, -0.00124164, -60.29477894, -0.01825268, -6.02947789, -0.0618636, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 112.97944368, 0.02114318, 112.97944368, 0.06342953, 79.08561057, -1627.46198342, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 28.24486092, 9.125e-05, 84.73458276, 0.00027375, 282.44860919, 0.0009125, -28.24486092, -9.125e-05, -84.73458276, -0.00027375, -282.44860919, -0.0009125, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 104.98222204, 0.02483277, 104.98222204, 0.07449832, 73.48755543, -1358.52777355, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 26.24555551, 8.479e-05, 78.73666653, 0.00025437, 262.45555509, 0.0008479, -26.24555551, -8.479e-05, -78.73666653, -0.00025437, -262.45555509, -0.0008479, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 3.15, 16.8, 0.0)
    ops.node(121018, 3.15, 16.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.165, 33207291.86222024, 13836371.60925843, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 287.76372674, 0.00072776, 343.77801236, 0.04992496, 34.37780124, 0.1483954, -287.76372674, -0.00072776, -343.77801236, -0.04992496, -34.37780124, -0.1483954, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 187.84134049, 0.00112233, 224.40535992, 0.04058028, 22.44053599, 0.09893088, -187.84134049, -0.00112233, -224.40535992, -0.04058028, -22.44053599, -0.09893088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 393.75620212, 0.01455526, 393.75620212, 0.04366577, 275.62934148, -8709.24454954, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 98.43905053, 0.00014229, 295.31715159, 0.00042687, 984.3905053, 0.0014229, -98.43905053, -0.00014229, -295.31715159, -0.00042687, -984.3905053, -0.0014229, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 257.56328431, 0.02244669, 257.56328431, 0.06734008, 180.29429902, -4001.59270267, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 64.39082108, 9.307e-05, 193.17246323, 0.00027922, 643.90821078, 0.00093075, -64.39082108, -9.307e-05, -193.17246323, -0.00027922, -643.90821078, -0.00093075, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.5, 16.8, 0.0)
    ops.node(121019, 8.5, 16.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.28, 31145958.86428956, 12977482.86012065, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 556.07956468, 0.00066789, 669.37785451, 0.04645979, 66.93778545, 0.12378681, -556.07956468, -0.00066789, -669.37785451, -0.04645979, -66.93778545, -0.12378681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 425.25779269, 0.00091288, 511.90183377, 0.04422614, 51.19018338, 0.11199077, -425.25779269, -0.00091288, -511.90183377, -0.04422614, -51.19018338, -0.11199077, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 700.35112627, 0.01335784, 700.35112627, 0.04007353, 490.24578839, -16782.7543183, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 175.08778157, 0.00015901, 525.2633447, 0.00047703, 1750.87781567, 0.00159009, -175.08778157, -0.00015901, -525.2633447, -0.00047703, -1750.87781567, -0.00159009, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 345.93803941, 0.01825763, 345.93803941, 0.05477288, 242.15662759, -4695.67247706, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 86.48450985, 7.854e-05, 259.45352956, 0.00023563, 864.84509853, 0.00078542, -86.48450985, -7.854e-05, -259.45352956, -0.00023563, -864.84509853, -0.00078542, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 13.85, 16.8, 0.0)
    ops.node(121020, 13.85, 16.8, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.15, 33143914.22527458, 13809964.26053108, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 193.28602979, 0.00075805, 231.07509701, 0.02759756, 23.1075097, 0.09759794, -193.28602979, -0.00075805, -231.07509701, -0.02759756, -23.1075097, -0.09759794, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 139.47590346, 0.00108455, 166.74463207, 0.02362554, 16.67446321, 0.06989476, -139.47590346, -0.00108455, -166.74463207, -0.02362554, -16.67446321, -0.06989476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 265.66236481, 0.0151609, 265.66236481, 0.0454827, 185.96365537, -4232.43556791, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 66.4155912, 0.0001058, 199.24677361, 0.00031741, 664.15591202, 0.00105804, -66.4155912, -0.0001058, -199.24677361, -0.00031741, -664.15591202, -0.00105804, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 197.60502593, 0.02169097, 197.60502593, 0.06507291, 138.32351815, -2406.53427329, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 49.40125648, 7.87e-05, 148.20376944, 0.0002361, 494.01256482, 0.00078699, -49.40125648, -7.87e-05, -148.20376944, -0.0002361, -494.01256482, -0.00078699, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 21.0, 0.0)
    ops.node(121021, 0.0, 21.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.075, 28648574.50466887, 11936906.04361203, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 64.19342807, 0.00116638, 77.27890074, 0.01596437, 7.72789007, 0.05892398, -64.19342807, -0.00116638, -77.27890074, -0.01596437, -7.72789007, -0.05892398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 48.9891472, 0.00139229, 58.97531193, 0.01532612, 5.89753119, 0.05257147, -48.9891472, -0.00139229, -58.97531193, -0.01532612, -5.89753119, -0.05257147, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 95.73285882, 0.02332766, 95.73285882, 0.06998297, 67.01300117, -1373.06183829, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 23.9332147, 8.822e-05, 71.79964411, 0.00026466, 239.33214705, 0.00088219, -23.9332147, -8.822e-05, -71.79964411, -0.00026466, -239.33214705, -0.00088219, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 83.79084789, 0.02784576, 83.79084789, 0.08353728, 58.65359352, -1164.11121203, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 20.94771197, 7.721e-05, 62.84313592, 0.00023164, 209.47711972, 0.00077214, -20.94771197, -7.721e-05, -62.84313592, -0.00023164, -209.47711972, -0.00077214, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 3.15, 21.0, 0.0)
    ops.node(121022, 3.15, 21.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.165, 31197573.65977765, 12998989.02490735, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 293.33008915, 0.00076165, 352.22665942, 0.04835499, 35.22266594, 0.14148725, -293.33008915, -0.00076165, -352.22665942, -0.04835499, -35.22266594, -0.14148725, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 192.93085589, 0.00118468, 231.66866743, 0.03935627, 23.16686674, 0.09454363, -192.93085589, -0.00118468, -231.66866743, -0.03935627, -23.16686674, -0.09454363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 356.15275602, 0.01523305, 356.15275602, 0.04569915, 249.30692921, -7380.51675763, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 89.038189, 0.00013699, 267.11456701, 0.00041098, 890.38189005, 0.00136992, -89.038189, -0.00013699, -267.11456701, -0.00041098, -890.38189005, -0.00136992, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 233.79621071, 0.02369358, 233.79621071, 0.07108074, 163.6573475, -3506.353574, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 58.44905268, 8.993e-05, 175.34715803, 0.00026979, 584.49052678, 0.00089929, -58.44905268, -8.993e-05, -175.34715803, -0.00026979, -584.49052678, -0.00089929, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 8.5, 21.0, 0.0)
    ops.node(121023, 8.5, 21.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.28, 28469704.83172237, 11862377.01321765, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 534.84312881, 0.00066473, 647.10823127, 0.04695295, 64.71082313, 0.11835613, -534.84312881, -0.00066473, -647.10823127, -0.04695295, -64.71082313, -0.11835613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 413.35563454, 0.00090637, 500.12016447, 0.04468908, 50.01201645, 0.10726242, -413.35563454, -0.00090637, -500.12016447, -0.04468908, -50.01201645, -0.10726242, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 666.08377372, 0.01329468, 666.08377372, 0.03988404, 466.25864161, -17002.6354451, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 166.52094343, 0.00016544, 499.56283029, 0.00049633, 1665.20943431, 0.00165445, -166.52094343, -0.00016544, -499.56283029, -0.00049633, -1665.20943431, -0.00165445, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 324.18288641, 0.01812731, 324.18288641, 0.05438193, 226.92802049, -4739.93950049, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 81.0457216, 8.052e-05, 243.13716481, 0.00024157, 810.45721603, 0.00080522, -81.0457216, -8.052e-05, -243.13716481, -0.00024157, -810.45721603, -0.00080522, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 13.85, 21.0, 0.0)
    ops.node(121024, 13.85, 21.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.15, 30835971.22915247, 12848321.34548019, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 173.95715562, 0.00073474, 209.1847318, 0.03145123, 20.91847318, 0.09726645, -173.95715562, -0.00073474, -209.1847318, -0.03145123, -20.91847318, -0.09726645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 122.49632175, 0.00104246, 147.30270865, 0.02683951, 14.73027086, 0.0703424, -122.49632175, -0.00104246, -147.30270865, -0.02683951, -14.73027086, -0.0703424, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 267.93449838, 0.01469473, 267.93449838, 0.04408419, 187.55414887, -4930.43591782, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 66.9836246, 0.0001147, 200.95087379, 0.00034409, 669.83624595, 0.00114695, -66.9836246, -0.0001147, -200.95087379, -0.00034409, -669.83624595, -0.00114695, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 195.59778986, 0.02084918, 195.59778986, 0.06254753, 136.9184529, -2719.87016316, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 48.89944747, 8.373e-05, 146.6983424, 0.00025119, 488.99447465, 0.0008373, -48.89944747, -8.373e-05, -146.6983424, -0.00025119, -488.99447465, -0.0008373, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 25.2, 0.0)
    ops.node(121025, 0.0, 25.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.0625, 28831162.20095946, 12012984.25039978, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 33.64359901, 0.00126065, 40.67453191, 0.01819764, 4.06745319, 0.06768576, -33.64359901, -0.00126065, -40.67453191, -0.01819764, -4.06745319, -0.06768576, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 33.64359901, 0.00126065, 40.67453191, 0.01819764, 4.06745319, 0.06768576, -33.64359901, -0.00126065, -40.67453191, -0.01819764, -4.06745319, -0.06768576, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 77.35311202, 0.02521305, 77.35311202, 0.07563916, 54.14717841, -1213.33578407, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 19.338278, 8.5e-05, 58.01483401, 0.00025499, 193.38278004, 0.00084996, -19.338278, -8.5e-05, -58.01483401, -0.00025499, -193.38278004, -0.00084996, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 77.35311202, 0.02521305, 77.35311202, 0.07563916, 54.14717841, -1213.33578407, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 19.338278, 8.5e-05, 58.01483401, 0.00025499, 193.38278004, 0.00084996, -19.338278, -8.5e-05, -58.01483401, -0.00025499, -193.38278004, -0.00084996, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 3.15, 25.2, 0.0)
    ops.node(121026, 3.15, 25.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.12, 29112165.54338898, 12130068.97641208, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 111.83024329, 0.00107362, 134.87344499, 0.0397282, 13.4873445, 0.10807962, -111.83024329, -0.00107362, -134.87344499, -0.0397282, -13.4873445, -0.10807962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 123.56049419, 0.00086294, 149.02077493, 0.04389321, 14.90207749, 0.1320434, -123.56049419, -0.00086294, -149.02077493, -0.04389321, -14.90207749, -0.1320434, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 192.31160541, 0.02147232, 192.31160541, 0.06441696, 134.61812379, -3906.77141822, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 48.07790135, 0.000109, 144.23370406, 0.00032699, 480.77901353, 0.00108997, -48.07790135, -0.000109, -144.23370406, -0.00032699, -480.77901353, -0.00108997, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 227.73327049, 0.01725887, 227.73327049, 0.05177661, 159.41328934, -5752.18035875, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 56.93331762, 0.00012907, 170.79995287, 0.00038722, 569.33317622, 0.00129073, -56.93331762, -0.00012907, -170.79995287, -0.00038722, -569.33317622, -0.00129073, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 8.5, 25.2, 0.0)
    ops.node(121027, 8.5, 25.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.175, 31634465.25138603, 13181027.18807751, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 191.1269578, 0.00103267, 229.64914615, 0.04206768, 22.96491461, 0.10559163, -191.1269578, -0.00103267, -229.64914615, -0.04206768, -22.96491461, -0.10559163, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 232.98688775, 0.00079491, 279.94606544, 0.04749681, 27.99460654, 0.1338347, -232.98688775, -0.00079491, -279.94606544, -0.04749681, -27.99460654, -0.1338347, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 270.38035457, 0.02065337, 270.38035457, 0.06196011, 189.2662482, -4947.27135553, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 67.59508864, 9.67e-05, 202.78526593, 0.00029011, 675.95088642, 0.00096703, -67.59508864, -9.67e-05, -202.78526593, -0.00029011, -675.95088642, -0.00096703, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 350.38984524, 0.01589826, 350.38984524, 0.04769477, 245.27289167, -8020.31081378, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 87.59746131, 0.00012532, 262.79238393, 0.00037596, 875.9746131, 0.00125319, -87.59746131, -0.00012532, -262.79238393, -0.00037596, -875.9746131, -0.00125319, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 13.85, 25.2, 0.0)
    ops.node(121028, 13.85, 25.2, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.075, 29797622.31469679, 12415675.96445699, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 51.4667769, 0.00128783, 61.91298374, 0.01681311, 6.19129837, 0.05689064, -51.4667769, -0.00128783, -61.91298374, -0.01681311, -6.19129837, -0.05689064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 58.41372032, 0.00108931, 70.26994761, 0.01757745, 7.02699476, 0.06380375, -58.41372032, -0.00108931, -70.26994761, -0.01757745, -7.02699476, -0.06380375, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 92.90792103, 0.02575664, 92.90792103, 0.07726993, 65.03554472, -1217.76919028, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 23.22698026, 8.231e-05, 69.68094077, 0.00024694, 232.26980258, 0.00082314, -23.22698026, -8.231e-05, -69.68094077, -0.00024694, -232.26980258, -0.00082314, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 100.04385228, 0.0217862, 100.04385228, 0.06535861, 70.03069659, -1450.30407777, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 25.01096307, 8.864e-05, 75.03288921, 0.00026591, 250.10963069, 0.00088637, -25.01096307, -8.864e-05, -75.03288921, -0.00026591, -250.10963069, -0.00088637, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.5, 0.0, 3.0)
    ops.node(122003, 8.5, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.175, 28932777.84087041, 12055324.10036267, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 105.99395466, 0.00093848, 128.42647686, 0.01876029, 12.84264769, 0.05611658, -105.99395466, -0.00093848, -128.42647686, -0.01876029, -12.84264769, -0.05611658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 187.23353359, 0.00073407, 226.85957087, 0.02066571, 22.68595709, 0.06937659, -187.23353359, -0.00073407, -226.85957087, -0.02066571, -22.68595709, -0.06937659, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 171.84136761, 0.01876952, 171.84136761, 0.05630855, 120.28895733, -2014.18527488, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 42.9603419, 6.72e-05, 128.88102571, 0.0002016, 429.60341902, 0.00067199, -42.9603419, -6.72e-05, -128.88102571, -0.0002016, -429.60341902, -0.00067199, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 215.69611237, 0.01468132, 215.69611237, 0.04404397, 150.98727866, -3006.09353873, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 53.92402809, 8.435e-05, 161.77208428, 0.00025305, 539.24028092, 0.00084349, -53.92402809, -8.435e-05, -161.77208428, -0.00025305, -539.24028092, -0.00084349, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.85, 0.0, 3.0)
    ops.node(122004, 13.85, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.075, 29763467.94681929, 12401444.97784137, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 45.80282025, 0.00122213, 55.29446963, 0.02478929, 5.52944696, 0.07770534, -45.80282025, -0.00122213, -55.29446963, -0.02478929, -5.52944696, -0.07770534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 51.5740375, 0.00103883, 62.26164753, 0.02614112, 6.22616475, 0.08760176, -51.5740375, -0.00103883, -62.26164753, -0.02614112, -6.22616475, -0.08760176, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 102.31239996, 0.02444256, 102.31239996, 0.07332768, 71.61867997, -1777.5289757, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 25.57809999, 9.075e-05, 76.73429997, 0.00027225, 255.7809999, 0.0009075, -25.57809999, -9.075e-05, -76.73429997, -0.00027225, -255.7809999, -0.0009075, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 112.22206904, 0.02077654, 112.22206904, 0.06232962, 78.55544833, -2244.17985664, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 28.05551726, 9.954e-05, 84.16655178, 0.00029862, 280.55517261, 0.0009954, -28.05551726, -9.954e-05, -84.16655178, -0.00029862, -280.55517261, -0.0009954, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.2, 3.0)
    ops.node(122005, 0.0, 4.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.075, 30459682.73689429, 12691534.47370596, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 54.06970229, 0.00107561, 65.13580085, 0.016581, 6.51358008, 0.06770357, -54.06970229, -0.00107561, -65.13580085, -0.016581, -6.51358008, -0.06770357, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 47.84169988, 0.00126988, 57.6331532, 0.01586979, 5.76331532, 0.06019232, -47.84169988, -0.00126988, -57.6331532, -0.01586979, -5.76331532, -0.06019232, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 97.20720807, 0.02151228, 97.20720807, 0.06453685, 68.04504565, -1434.7651368, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 24.30180202, 8.425e-05, 72.90540606, 0.00025275, 243.01802018, 0.00084251, -24.30180202, -8.425e-05, -72.90540606, -0.00025275, -243.01802018, -0.00084251, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 83.60511305, 0.02539761, 83.60511305, 0.07619283, 58.52357913, -1180.81686486, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 20.90127826, 7.246e-05, 62.70383479, 0.00021739, 209.01278262, 0.00072462, -20.90127826, -7.246e-05, -62.70383479, -0.00021739, -209.01278262, -0.00072462, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 3.15, 4.2, 3.0)
    ops.node(122006, 3.15, 4.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.165, 31022146.02594959, 12925894.177479, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 212.80733235, 0.00071013, 256.23967943, 0.0338932, 25.62396794, 0.10355683, -212.80733235, -0.00071013, -256.23967943, -0.0338932, -25.62396794, -0.10355683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 101.038211, 0.00108113, 121.65933622, 0.02811507, 12.16593362, 0.07095737, -101.038211, -0.00108113, -121.65933622, -0.02811507, -12.16593362, -0.07095737, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 278.94637559, 0.0142026, 278.94637559, 0.0426078, 195.26246291, -4538.26218581, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 69.7365939, 0.0001079, 209.20978169, 0.00032371, 697.36593897, 0.00107902, -69.7365939, -0.0001079, -209.20978169, -0.00032371, -697.36593897, -0.00107902, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 189.06381432, 0.02162251, 189.06381432, 0.06486752, 132.34467003, -2261.59805518, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 47.26595358, 7.313e-05, 141.79786074, 0.0002194, 472.65953581, 0.00073134, -47.26595358, -7.313e-05, -141.79786074, -0.0002194, -472.65953581, -0.00073134, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.5, 4.2, 3.0)
    ops.node(122007, 8.5, 4.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.28, 29648948.29106077, 12353728.45460865, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 424.10094859, 0.00067913, 513.37830849, 0.02588799, 51.33783085, 0.07127611, -424.10094859, -0.00067913, -513.37830849, -0.02588799, -51.33783085, -0.07127611, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 195.64440235, 0.0009407, 236.82944515, 0.02234317, 23.68294452, 0.05312625, -195.64440235, -0.0009407, -236.82944515, -0.02234317, -23.68294452, -0.05312625, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 426.52316473, 0.01358259, 426.52316473, 0.04074777, 298.56621531, -4522.70571487, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 106.63079118, 0.00010173, 319.89237355, 0.00030518, 1066.30791182, 0.00101728, -106.63079118, -0.00010173, -319.89237355, -0.00030518, -1066.30791182, -0.00101728, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 256.40864757, 0.01881392, 256.40864757, 0.05644175, 179.4860533, -2478.44438262, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 64.10216189, 6.115e-05, 192.30648568, 0.00018346, 641.02161893, 0.00061155, -64.10216189, -6.115e-05, -192.30648568, -0.00018346, -641.02161893, -0.00061155, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.85, 4.2, 3.0)
    ops.node(122008, 13.85, 4.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.15, 31852761.18597458, 13271983.82748941, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 171.29553403, 0.00070525, 205.9970262, 0.02919359, 20.59970262, 0.10198957, -171.29553403, -0.00070525, -205.9970262, -0.02919359, -20.59970262, -0.10198957, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 84.02638554, 0.00099061, 101.04866797, 0.02491637, 10.1048668, 0.07303343, -84.02638554, -0.00099061, -101.04866797, -0.02491637, -10.1048668, -0.07303343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 242.91294533, 0.01410502, 242.91294533, 0.04231507, 170.03906173, -4341.35123371, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 60.72823633, 0.00010066, 182.184709, 0.00030199, 607.28236332, 0.00100665, -60.72823633, -0.00010066, -182.184709, -0.00030199, -607.28236332, -0.00100665, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 179.64328391, 0.01981227, 179.64328391, 0.0594368, 125.75029874, -2310.20288962, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 44.91082098, 7.445e-05, 134.73246293, 0.00022334, 449.10820978, 0.00074445, -44.91082098, -7.445e-05, -134.73246293, -0.00022334, -449.10820978, -0.00074445, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.4, 3.0)
    ops.node(122009, 0.0, 8.4, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.075, 31093670.5558692, 12955696.0649455, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 58.25235197, 0.00105816, 70.09799213, 0.01740042, 7.00979921, 0.06990108, -58.25235197, -0.00105816, -70.09799213, -0.01740042, -7.00979921, -0.06990108, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 43.90000233, 0.00124696, 52.82708618, 0.01663488, 5.28270862, 0.06215219, -43.90000233, -0.00124696, -52.82708618, -0.01663488, -5.28270862, -0.06215219, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 98.29219536, 0.0211631, 98.29219536, 0.0634893, 68.80453675, -1442.44775747, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 24.57304884, 8.345e-05, 73.71914652, 0.00025036, 245.7304884, 0.00083455, -24.57304884, -8.345e-05, -73.71914652, -0.00025036, -245.7304884, -0.00083455, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 89.3034465, 0.02493915, 89.3034465, 0.07481746, 62.51241255, -1183.26448221, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 22.32586163, 7.582e-05, 66.97758488, 0.00022747, 223.25861626, 0.00075823, -22.32586163, -7.582e-05, -66.97758488, -0.00022747, -223.25861626, -0.00075823, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 3.15, 8.4, 3.0)
    ops.node(122010, 3.15, 8.4, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.165, 31197529.69108484, 12998970.70461868, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 216.73601483, 0.00071517, 260.95205489, 0.03489964, 26.09520549, 0.1055947, -216.73601483, -0.00071517, -260.95205489, -0.03489964, -26.09520549, -0.1055947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 102.71273665, 0.00107411, 123.66703205, 0.02892389, 12.3667032, 0.07240051, -102.71273665, -0.00107411, -123.66703205, -0.02892389, -12.3667032, -0.07240051, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 292.15496026, 0.0143033, 292.15496026, 0.04290991, 204.50847218, -5300.01899971, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 73.03874006, 0.00011238, 219.11622019, 0.00033713, 730.38740065, 0.00112376, -73.03874006, -0.00011238, -219.11622019, -0.00033713, -730.38740065, -0.00112376, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 196.17891034, 0.02148225, 196.17891034, 0.06444675, 137.32523724, -2527.12426451, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 49.04472759, 7.546e-05, 147.13418276, 0.00022638, 490.44727585, 0.00075459, -49.04472759, -7.546e-05, -147.13418276, -0.00022638, -490.44727585, -0.00075459, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.5, 8.4, 3.0)
    ops.node(122011, 8.5, 8.4, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.28, 30639979.47479929, 12766658.1144997, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 408.8082271, 0.00064821, 493.74524425, 0.02820846, 49.37452443, 0.07453355, -408.8082271, -0.00064821, -493.74524425, -0.02820846, -49.37452443, -0.07453355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 189.43709499, 0.00088679, 228.79594523, 0.02428562, 22.87959452, 0.05570416, -189.43709499, -0.00088679, -228.79594523, -0.02428562, -22.87959452, -0.05570416, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 462.83337305, 0.01296419, 462.83337305, 0.03889256, 323.98336114, -5546.72797897, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 115.70834326, 0.00010682, 347.12502979, 0.00032045, 1157.08343264, 0.00106818, -115.70834326, -0.00010682, -347.12502979, -0.00032045, -1157.08343264, -0.00106818, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 277.73854821, 0.0177358, 277.73854821, 0.05320741, 194.41698374, -2906.58099461, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 69.43463705, 6.41e-05, 208.30391116, 0.0001923, 694.34637052, 0.000641, -69.43463705, -6.41e-05, -208.30391116, -0.0001923, -694.34637052, -0.000641, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.85, 8.4, 3.0)
    ops.node(122012, 13.85, 8.4, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.15, 32743280.02781167, 13643033.34492153, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 168.76338761, 0.00072079, 202.43199143, 0.02960222, 20.24319914, 0.10360667, -168.76338761, -0.00072079, -202.43199143, -0.02960222, -20.24319914, -0.10360667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 83.63586266, 0.00103772, 100.3213699, 0.0252936, 10.03213699, 0.07420945, -83.63586266, -0.00103772, -100.3213699, -0.0252936, -10.03213699, -0.07420945, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 252.72850539, 0.01441575, 252.72850539, 0.04324726, 176.90995377, -4599.66195159, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 63.18212635, 0.00010188, 189.54637904, 0.00030565, 631.82126347, 0.00101884, -63.18212635, -0.00010188, -189.54637904, -0.00030565, -631.82126347, -0.00101884, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 186.81650561, 0.02075432, 186.81650561, 0.06226295, 130.77155393, -2422.97224541, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 46.7041264, 7.531e-05, 140.11237921, 0.00022594, 467.04126402, 0.00075312, -46.7041264, -7.531e-05, -140.11237921, -0.00022594, -467.04126402, -0.00075312, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 12.6, 3.0)
    ops.node(122013, 0.0, 12.6, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.075, 31552901.56802548, 13147042.32001062, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 57.60097754, 0.00103551, 69.23742344, 0.0203218, 6.92374234, 0.07343459, -57.60097754, -0.00103551, -69.23742344, -0.0203218, -6.92374234, -0.07343459, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 43.44534524, 0.00121902, 52.22209576, 0.01937905, 5.22220958, 0.06542706, -43.44534524, -0.00121902, -52.22209576, -0.01937905, -5.22220958, -0.06542706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 106.83559338, 0.02071025, 106.83559338, 0.06213075, 74.78491536, -1747.85753312, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 26.70889834, 8.939e-05, 80.12669503, 0.00026816, 267.08898344, 0.00089388, -26.70889834, -8.939e-05, -80.12669503, -0.00026816, -267.08898344, -0.00089388, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 98.61821767, 0.02438044, 98.61821767, 0.07314133, 69.03275237, -1412.89218743, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 24.65455442, 8.251e-05, 73.96366325, 0.00024754, 246.54554417, 0.00082513, -24.65455442, -8.251e-05, -73.96366325, -0.00024754, -246.54554417, -0.00082513, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 3.15, 12.6, 3.0)
    ops.node(122014, 3.15, 12.6, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.165, 29383932.72866164, 12243305.30360902, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 211.23780454, 0.00073783, 255.31607699, 0.03519545, 25.5316077, 0.10258412, -211.23780454, -0.00073783, -255.31607699, -0.03519545, -25.5316077, -0.10258412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 99.83371492, 0.00114068, 120.66567582, 0.02921298, 12.06656758, 0.07065621, -99.83371492, -0.00114068, -120.66567582, -0.02921298, -12.06656758, -0.07065621, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 270.06065096, 0.01475657, 270.06065096, 0.0442697, 189.04245567, -4767.62653966, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 67.51516274, 0.00011029, 202.54548822, 0.00033087, 675.15162739, 0.00110289, -67.51516274, -0.00011029, -202.54548822, -0.00033087, -675.15162739, -0.00110289, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 181.34583687, 0.0228135, 181.34583687, 0.06844051, 126.94208581, -2325.48625659, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 45.33645922, 7.406e-05, 136.00937765, 0.00022218, 453.36459218, 0.00074059, -45.33645922, -7.406e-05, -136.00937765, -0.00022218, -453.36459218, -0.00074059, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.5, 12.6, 3.0)
    ops.node(122015, 8.5, 12.6, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.28, 32173567.68366997, 13405653.20152915, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 409.92235861, 0.00062575, 493.04482222, 0.02804159, 49.30448222, 0.07561086, -409.92235861, -0.00062575, -493.04482222, -0.02804159, -49.30448222, -0.07561086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 189.75790508, 0.00083736, 228.23627599, 0.02411358, 22.8236276, 0.05637595, -189.75790508, -0.00083736, -228.23627599, -0.02411358, -22.8236276, -0.05637595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 484.61990932, 0.01251494, 484.61990932, 0.03754481, 339.23393653, -5549.07248476, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 121.15497733, 0.00010651, 363.46493199, 0.00031954, 1211.54977331, 0.00106515, -121.15497733, -0.00010651, -363.46493199, -0.00031954, -1211.54977331, -0.00106515, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 291.10989174, 0.01674711, 291.10989174, 0.05024133, 203.77692422, -2907.55078166, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 72.77747294, 6.398e-05, 218.33241881, 0.00019195, 727.77472935, 0.00063983, -72.77747294, -6.398e-05, -218.33241881, -0.00019195, -727.77472935, -0.00063983, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.85, 12.6, 3.0)
    ops.node(122016, 13.85, 12.6, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.15, 34740952.45671548, 14475396.85696478, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 173.30097085, 0.00071611, 206.48268644, 0.02777934, 20.64826864, 0.10408625, -173.30097085, -0.00071611, -206.48268644, -0.02777934, -20.64826864, -0.10408625, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 85.6700564, 0.00102069, 102.0731927, 0.02374957, 10.20731927, 0.0741873, -85.6700564, -0.00102069, -102.0731927, -0.02374957, -10.20731927, -0.0741873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 263.42550066, 0.01432228, 263.42550066, 0.04296683, 184.39785046, -4562.05190987, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 65.85637516, 0.00010009, 197.56912549, 0.00030027, 658.56375165, 0.0010009, -65.85637516, -0.00010009, -197.56912549, -0.00030027, -658.56375165, -0.0010009, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 196.19074152, 0.02041376, 196.19074152, 0.06124129, 137.33351906, -2406.58821304, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 49.04768538, 7.454e-05, 147.14305614, 0.00022363, 490.47685379, 0.00074544, -49.04768538, -7.454e-05, -147.14305614, -0.00022363, -490.47685379, -0.00074544, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 16.8, 3.0)
    ops.node(122017, 0.0, 16.8, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.075, 31173006.9773976, 12988752.907249, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 57.29586812, 0.00110721, 68.9341884, 0.02012951, 6.89341884, 0.07273821, -57.29586812, -0.00110721, -68.9341884, -0.02012951, -6.89341884, -0.07273821, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 43.49405579, 0.00131964, 52.32885957, 0.01923109, 5.23288596, 0.06484207, -43.49405579, -0.00131964, -52.32885957, -0.01923109, -5.23288596, -0.06484207, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 105.06770453, 0.02214411, 105.06770453, 0.06643234, 73.54739317, -1710.82053593, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 26.26692613, 8.898e-05, 78.8007784, 0.00026694, 262.66926132, 0.0008898, -26.26692613, -8.898e-05, -78.8007784, -0.00026694, -262.66926132, -0.0008898, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 96.99489001, 0.02639277, 96.99489001, 0.07917831, 67.89642301, -1385.13176643, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 24.2487225, 8.214e-05, 72.74616751, 0.00024643, 242.48722502, 0.00082144, -24.2487225, -8.214e-05, -72.74616751, -0.00024643, -242.48722502, -0.00082144, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 3.15, 16.8, 3.0)
    ops.node(122018, 3.15, 16.8, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.165, 33548430.65450311, 13978512.77270963, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 208.11809478, 0.00072344, 248.89899539, 0.03338892, 24.88989954, 0.10745812, -208.11809478, -0.00072344, -248.89899539, -0.03338892, -24.88989954, -0.10745812, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 99.06655848, 0.00114358, 118.47872675, 0.02775585, 11.84787267, 0.07330752, -99.06655848, -0.00114358, -118.47872675, -0.02775585, -11.84787267, -0.07330752, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 298.22682273, 0.01446887, 298.22682273, 0.04340661, 208.75877591, -4791.78669739, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 74.55670568, 0.00010667, 223.67011705, 0.00032002, 745.56705682, 0.00106673, -74.55670568, -0.00010667, -223.67011705, -0.00032002, -745.56705682, -0.00106673, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 203.23761856, 0.02287164, 203.23761856, 0.06861491, 142.26633299, -2334.6874445, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 50.80940464, 7.27e-05, 152.42821392, 0.00021809, 508.0940464, 0.00072696, -50.80940464, -7.27e-05, -152.42821392, -0.00021809, -508.0940464, -0.00072696, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.5, 16.8, 3.0)
    ops.node(122019, 8.5, 16.8, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.28, 30419003.01311731, 12674584.58879888, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 431.65001952, 0.00065682, 521.61114274, 0.0244707, 52.16111427, 0.07059664, -431.65001952, -0.00065682, -521.61114274, -0.0244707, -52.16111427, -0.07059664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 198.19046843, 0.00088336, 239.49577678, 0.02110149, 23.94957768, 0.05238497, -198.19046843, -0.00088336, -239.49577678, -0.02110149, -23.94957768, -0.05238497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 430.81236624, 0.01313646, 430.81236624, 0.03940938, 301.56865637, -4254.42431774, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 107.70309156, 0.00010015, 323.10927468, 0.00030045, 1077.03091561, 0.0010015, -107.70309156, -0.00010015, -323.10927468, -0.00030045, -1077.03091561, -0.0010015, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 259.31024279, 0.01766724, 259.31024279, 0.05300171, 181.51716995, -2364.56253559, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 64.8275607, 6.028e-05, 194.48268209, 0.00018084, 648.27560696, 0.00060281, -64.8275607, -6.028e-05, -194.48268209, -0.00018084, -648.27560696, -0.00060281, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 13.85, 16.8, 3.0)
    ops.node(122020, 13.85, 16.8, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.15, 31490873.63180486, 13121197.34658536, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 170.47373112, 0.00072456, 205.20687309, 0.0334118, 20.52068731, 0.10567983, -170.47373112, -0.00072456, -205.20687309, -0.0334118, -20.52068731, -0.10567983, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 83.96136311, 0.00103582, 101.06805706, 0.02848799, 10.10680571, 0.07625609, -83.96136311, -0.00103582, -101.06805706, -0.02848799, -10.10680571, -0.07625609, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 268.63586529, 0.01449125, 268.63586529, 0.04347375, 188.0451057, -5912.31581412, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 67.15896632, 0.0001126, 201.47689897, 0.00033781, 671.58966322, 0.00112604, -67.15896632, -0.0001126, -201.47689897, -0.00033781, -671.58966322, -0.00112604, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 194.56128188, 0.02071644, 194.56128188, 0.06214933, 136.19289731, -2988.38929658, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 48.64032047, 8.155e-05, 145.92096141, 0.00024466, 486.40320469, 0.00081554, -48.64032047, -8.155e-05, -145.92096141, -0.00024466, -486.40320469, -0.00081554, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 21.0, 3.0)
    ops.node(122021, 0.0, 21.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.075, 30833253.78289012, 12847189.07620422, 0.00077515, 0.00042969, 0.00061875, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 56.86829385, 0.00111921, 68.47316455, 0.02059843, 6.84731645, 0.07273756, -56.86829385, -0.00111921, -68.47316455, -0.02059843, -6.84731645, -0.07273756, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 43.24617093, 0.00133777, 52.07123297, 0.01967945, 5.2071233, 0.06488333, -43.24617093, -0.00133777, -52.07123297, -0.01967945, -5.2071233, -0.06488333, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 106.35601319, 0.02238429, 106.35601319, 0.06715287, 74.44920924, -1800.67087682, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 26.5890033, 9.106e-05, 79.7670099, 0.00027319, 265.89003299, 0.00091064, -26.5890033, -9.106e-05, -79.7670099, -0.00027319, -265.89003299, -0.00091064, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 97.93512253, 0.02675546, 97.93512253, 0.08026639, 68.55458577, -1452.44045667, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 24.48378063, 8.385e-05, 73.4513419, 0.00025156, 244.83780632, 0.00083854, -24.48378063, -8.385e-05, -73.4513419, -0.00025156, -244.83780632, -0.00083854, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 3.15, 21.0, 3.0)
    ops.node(122022, 3.15, 21.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.165, 30876581.74064044, 12865242.39193352, 0.00326155, 0.00136125, 0.00457531, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 215.55009111, 0.00072857, 259.72376712, 0.03383852, 25.97237671, 0.10399816, -215.55009111, -0.00072857, -259.72376712, -0.03383852, -25.97237671, -0.10399816, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 101.99514818, 0.0011116, 122.89748511, 0.02808597, 12.28974851, 0.07123331, -101.99514818, -0.0011116, -122.89748511, -0.02808597, -12.28974851, -0.07123331, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 274.62214375, 0.01457147, 274.62214375, 0.04371441, 192.23550062, -4513.48572949, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 68.65553594, 0.00010673, 205.96660781, 0.00032019, 686.55535937, 0.0010673, -68.65553594, -0.00010673, -205.96660781, -0.00032019, -686.55535937, -0.0010673, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 186.11637949, 0.02223196, 186.11637949, 0.06669589, 130.28146565, -2228.38178902, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 46.52909487, 7.233e-05, 139.58728462, 0.000217, 465.29094873, 0.00072333, -46.52909487, -7.233e-05, -139.58728462, -0.000217, -465.29094873, -0.00072333, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 8.5, 21.0, 3.0)
    ops.node(122023, 8.5, 21.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.28, 32628585.07440268, 13595243.78100112, 0.0096051, 0.00410667, 0.01257667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 418.0897989, 0.00062811, 502.17763347, 0.02378008, 50.21776335, 0.07167658, -418.0897989, -0.00062811, -502.17763347, -0.02378008, -50.21776335, -0.07167658, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 193.15151409, 0.00083671, 231.99889235, 0.02049287, 23.19988923, 0.05297718, -193.15151409, -0.00083671, -231.99889235, -0.02049287, -23.19988923, -0.05297718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 460.81691036, 0.01256218, 460.81691036, 0.03768655, 322.57183725, -4196.88545154, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 115.20422759, 9.987e-05, 345.61268277, 0.00029961, 1152.04227589, 0.00099871, -115.20422759, -9.987e-05, -345.61268277, -0.00029961, -1152.04227589, -0.00099871, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 277.78693644, 0.01673413, 277.78693644, 0.0502024, 194.45085551, -2340.03107884, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 69.44673411, 6.02e-05, 208.34020233, 0.00018061, 694.46734109, 0.00060203, -69.44673411, -6.02e-05, -208.34020233, -0.00018061, -694.46734109, -0.00060203, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 13.85, 21.0, 3.0)
    ops.node(122024, 13.85, 21.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.15, 31340563.46419737, 13058568.11008224, 0.00281737, 0.0012375, 0.0034375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 178.05670903, 0.00074075, 214.41805713, 0.0330904, 21.44180571, 0.1051325, -178.05670903, -0.00074075, -214.41805713, -0.0330904, -21.44180571, -0.1051325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 87.01952993, 0.00105031, 104.78997754, 0.02821896, 10.47899775, 0.07583772, -87.01952993, -0.00105031, -104.78997754, -0.02821896, -10.47899775, -0.07583772, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 264.31533156, 0.01481503, 264.31533156, 0.04444509, 185.02073209, -5700.62754396, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 66.07883289, 0.00011132, 198.23649867, 0.00033397, 660.78832891, 0.00111324, -66.07883289, -0.00011132, -198.23649867, -0.00033397, -660.78832891, -0.00111324, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 191.75576198, 0.02100612, 191.75576198, 0.06301837, 134.22903339, -2897.96083054, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 47.9389405, 8.076e-05, 143.81682149, 0.00024229, 479.38940496, 0.00080764, -47.9389405, -8.076e-05, -143.81682149, -0.00024229, -479.38940496, -0.00080764, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 25.2, 3.0)
    ops.node(122025, 0.0, 25.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.0625, 34483736.1112569, 14368223.37969038, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 31.05975894, 0.00120638, 37.07215217, 0.01730125, 3.70721522, 0.07671829, -31.05975894, -0.00120638, -37.07215217, -0.01730125, -3.70721522, -0.07671829, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 31.05975894, 0.00120638, 37.07215217, 0.01730125, 3.70721522, 0.07671829, -31.05975894, -0.00120638, -37.07215217, -0.01730125, -3.70721522, -0.07671829, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 86.90188106, 0.02412755, 86.90188106, 0.07238265, 60.83131674, -1378.57215965, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 21.72547026, 7.984e-05, 65.17641079, 0.00023951, 217.25470265, 0.00079836, -21.72547026, -7.984e-05, -65.17641079, -0.00023951, -217.25470265, -0.00079836, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 86.90188106, 0.02412755, 86.90188106, 0.07238265, 60.83131674, -1378.57215965, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 21.72547026, 7.984e-05, 65.17641079, 0.00023951, 217.25470265, 0.00079836, -21.72547026, -7.984e-05, -65.17641079, -0.00023951, -217.25470265, -0.00079836, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 3.15, 25.2, 3.0)
    ops.node(122026, 3.15, 25.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.12, 31381350.19339714, 13075562.58058214, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 93.46143739, 0.00105837, 112.53309305, 0.04165107, 11.25330931, 0.12137673, -93.46143739, -0.00105837, -112.53309305, -0.04165107, -11.25330931, -0.12137673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 106.24043705, 0.00085188, 127.91976373, 0.04603966, 12.79197637, 0.14603966, -106.24043705, -0.00085188, -127.91976373, -0.04603966, -12.79197637, -0.14603966, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 203.81500429, 0.02116731, 203.81500429, 0.06350194, 142.670503, -4953.05595301, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 50.95375107, 0.00010716, 152.86125322, 0.00032149, 509.53751072, 0.00107164, -50.95375107, -0.00010716, -152.86125322, -0.00032149, -509.53751072, -0.00107164, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 242.37878265, 0.01703759, 242.37878265, 0.05111278, 169.66514785, -7650.58688355, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 60.59469566, 0.00012744, 181.78408699, 0.00038232, 605.94695662, 0.0012744, -60.59469566, -0.00012744, -181.78408699, -0.00038232, -605.94695662, -0.0012744, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 8.5, 25.2, 3.0)
    ops.node(122027, 8.5, 25.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.175, 28676680.34297918, 11948616.80957466, 0.00405757, 0.00401042, 0.0019651, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 117.80545477, 0.00103461, 142.80282103, 0.03307455, 14.2802821, 0.07894084, -117.80545477, -0.00103461, -142.80282103, -0.03307455, -14.2802821, -0.07894084, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 191.62736797, 0.00080598, 232.28914811, 0.03693037, 23.22891481, 0.09789819, -191.62736797, -0.00080598, -232.28914811, -0.03693037, -23.22891481, -0.09789819, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 207.62846229, 0.02069215, 207.62846229, 0.06207645, 145.3399236, -3526.55145292, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 51.90711557, 8.192e-05, 155.72134672, 0.00024576, 519.07115573, 0.00081919, -51.90711557, -8.192e-05, -155.72134672, -0.00024576, -519.07115573, -0.00081919, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 267.17200358, 0.0161196, 267.17200358, 0.0483588, 187.02040251, -5707.71543234, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 66.7930009, 0.00010541, 200.37900269, 0.00031624, 667.93000895, 0.00105412, -66.7930009, -0.00010541, -200.37900269, -0.00031624, -667.93000895, -0.00105412, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 13.85, 25.2, 3.0)
    ops.node(122028, 13.85, 25.2, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.075, 30540629.80366812, 12725262.41819505, 0.00077515, 0.00061875, 0.00042969, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 44.54112685, 0.00117427, 53.68657006, 0.02242397, 5.36865701, 0.07652025, -44.54112685, -0.00117427, -53.68657006, -0.02242397, -5.36865701, -0.07652025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 50.27627783, 0.00099883, 60.5992956, 0.0236327, 6.05992956, 0.08646415, -50.27627783, -0.00099883, -60.5992956, -0.0236327, -6.05992956, -0.08646415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 98.96018903, 0.02348531, 98.96018903, 0.07045593, 69.27213232, -1556.52427093, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 24.74004726, 8.554e-05, 74.22014177, 0.00025663, 247.40047256, 0.00085543, -24.74004726, -8.554e-05, -74.22014177, -0.00025663, -247.40047256, -0.00085543, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 107.8401315, 0.01997654, 107.8401315, 0.05992963, 75.48809205, -1946.86087095, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 26.96003287, 9.322e-05, 80.88009862, 0.00027966, 269.60032875, 0.00093219, -26.96003287, -9.322e-05, -80.88009862, -0.00027966, -269.60032875, -0.00093219, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.5, 0.0, 5.75)
    ops.node(123003, 8.5, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.1, 33180308.59191259, 13825128.57996358, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 45.85652045, 0.00119951, 54.94450336, 0.01529855, 5.49445034, 0.05546466, -45.85652045, -0.00119951, -54.94450336, -0.01529855, -5.49445034, -0.05546466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 82.6044258, 0.00081744, 98.97521894, 0.01719145, 9.89752189, 0.07446621, -82.6044258, -0.00081744, -98.97521894, -0.01719145, -9.89752189, -0.07446621, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 113.89150093, 0.02399012, 113.89150093, 0.07197035, 79.72405065, -1201.75125819, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 28.47287523, 6.796e-05, 85.4186257, 0.00020389, 284.72875233, 0.00067964, -28.47287523, -6.796e-05, -85.4186257, -0.00020389, -284.72875233, -0.00067964, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 135.1708534, 0.01634884, 135.1708534, 0.04904653, 94.61959738, -2048.83448118, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 33.79271335, 8.066e-05, 101.37814005, 0.00024199, 337.92713349, 0.00080662, -33.79271335, -8.066e-05, -101.37814005, -0.00024199, -337.92713349, -0.00080662, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.85, 0.0, 5.75)
    ops.node(123004, 13.85, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 30732571.37929501, 12805238.07470626, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 30.32210858, 0.00135206, 36.61081362, 0.02134781, 3.66108136, 0.07743319, -30.32210858, -0.00135206, -36.61081362, -0.02134781, -3.66108136, -0.07743319, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 30.32210858, 0.00135206, 36.61081362, 0.02134781, 3.66108136, 0.07743319, -30.32210858, -0.00135206, -36.61081362, -0.02134781, -3.66108136, -0.07743319, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 85.69970239, 0.02704113, 85.69970239, 0.08112338, 59.98979167, -1698.307718, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 21.4249256, 8.834e-05, 64.27477679, 0.00026502, 214.24925598, 0.00088342, -21.4249256, -8.834e-05, -64.27477679, -0.00026502, -214.24925598, -0.00088342, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 85.69970239, 0.02704113, 85.69970239, 0.08112338, 59.98979167, -1698.307718, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 21.4249256, 8.834e-05, 64.27477679, 0.00026502, 214.24925598, 0.00088342, -21.4249256, -8.834e-05, -64.27477679, -0.00026502, -214.24925598, -0.00088342, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.2, 5.75)
    ops.node(123005, 0.0, 4.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 27774971.16689382, 11572904.65287242, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 29.6974585, 0.00137851, 36.02501621, 0.01983388, 3.60250162, 0.07029857, -29.6974585, -0.00137851, -36.02501621, -0.01983388, -3.60250162, -0.07029857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 29.6974585, 0.00137851, 36.02501621, 0.01983388, 3.60250162, 0.07029857, -29.6974585, -0.00137851, -36.02501621, -0.01983388, -3.60250162, -0.07029857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 77.1596835, 0.02757025, 77.1596835, 0.08271076, 54.01177845, -1420.66329432, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 19.28992087, 8.801e-05, 57.86976262, 0.00026402, 192.89920874, 0.00088008, -19.28992087, -8.801e-05, -57.86976262, -0.00026402, -192.89920874, -0.00088008, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 77.1596835, 0.02757025, 77.1596835, 0.08271076, 54.01177845, -1420.66329432, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 19.28992087, 8.801e-05, 57.86976262, 0.00026402, 192.89920874, 0.00088008, -19.28992087, -8.801e-05, -57.86976262, -0.00026402, -192.89920874, -0.00088008, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 3.15, 4.2, 5.75)
    ops.node(123006, 3.15, 4.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.125, 29920603.87423344, 12466918.2809306, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 147.84378752, 0.00075997, 178.67938725, 0.03077282, 17.86793873, 0.09517235, -147.84378752, -0.00075997, -178.67938725, -0.03077282, -17.86793873, -0.09517235, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 65.13465969, 0.00129661, 78.71971678, 0.02522629, 7.87197168, 0.06285669, -65.13465969, -0.00129661, -78.71971678, -0.02522629, -7.87197168, -0.06285669, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 194.59631944, 0.0151994, 194.59631944, 0.04559821, 136.21742361, -3770.49103268, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 48.64907986, 0.00010302, 145.94723958, 0.00030906, 486.4907986, 0.0010302, -48.64907986, -0.00010302, -145.94723958, -0.00030906, -486.4907986, -0.0010302, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 132.98623164, 0.02593223, 132.98623164, 0.07779668, 93.09036215, -1618.37371982, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 33.24655791, 7.04e-05, 99.73967373, 0.00021121, 332.46557909, 0.00070403, -33.24655791, -7.04e-05, -99.73967373, -0.00021121, -332.46557909, -0.00070403, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.5, 4.2, 5.75)
    ops.node(123007, 8.5, 4.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.21, 28494389.09857085, 11872662.12440452, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 267.34139718, 0.00070026, 324.72115712, 0.02054242, 32.47211571, 0.0633018, -267.34139718, -0.00070026, -324.72115712, -0.02054242, -32.47211571, -0.0633018, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 128.00770537, 0.00098149, 155.48213126, 0.01799769, 15.54821313, 0.04769725, -128.00770537, -0.00098149, -155.48213126, -0.01799769, -15.54821313, -0.04769725, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 256.97385799, 0.01400529, 256.97385799, 0.04201587, 179.88170059, -2846.84114719, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 64.2434645, 8.503e-05, 192.73039349, 0.00025509, 642.43464497, 0.00085031, -64.2434645, -8.503e-05, -192.73039349, -0.00025509, -642.43464497, -0.00085031, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 173.35881774, 0.0196298, 173.35881774, 0.05888941, 121.35117242, -1592.83131862, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 43.33970444, 5.736e-05, 130.01911331, 0.00017209, 433.39704436, 0.00057363, -43.33970444, -5.736e-05, -130.01911331, -0.00017209, -433.39704436, -0.00057363, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.85, 4.2, 5.75)
    ops.node(123008, 13.85, 4.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1, 36225502.4401664, 15093959.35006933, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 82.63290826, 0.00080674, 97.90738495, 0.01473713, 9.7907385, 0.07449552, -82.63290826, -0.00080674, -97.90738495, -0.01473713, -9.7907385, -0.07449552, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 45.95251154, 0.00118416, 54.44671296, 0.0131791, 5.4446713, 0.05508695, -45.95251154, -0.00118416, -54.44671296, -0.0131791, -5.4446713, -0.05508695, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 141.79448573, 0.01613474, 141.79448573, 0.04840422, 99.25614001, -1921.29616096, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 35.44862143, 7.75e-05, 106.3458643, 0.0002325, 354.48621433, 0.00077502, -35.44862143, -7.75e-05, -106.3458643, -0.0002325, -354.48621433, -0.00077502, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 113.44516564, 0.02368316, 113.44516564, 0.07104947, 79.41161595, -1135.19701359, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 28.36129141, 6.201e-05, 85.08387423, 0.00018602, 283.6129141, 0.00062006, -28.36129141, -6.201e-05, -85.08387423, -0.00018602, -283.6129141, -0.00062006, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.4, 5.75)
    ops.node(123009, 0.0, 8.4, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 34914939.33983225, 14547891.39159677, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 30.74446887, 0.0011714, 36.62823688, 0.01939013, 3.66282369, 0.07870212, -30.74446887, -0.0011714, -36.62823688, -0.01939013, -3.66282369, -0.07870212, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 30.74446887, 0.0011714, 36.62823688, 0.01939013, 3.66282369, 0.07870212, -30.74446887, -0.0011714, -36.62823688, -0.01939013, -3.66282369, -0.07870212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 92.37086724, 0.02342791, 92.37086724, 0.07028373, 64.65960707, -1561.18356339, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 23.09271681, 8.381e-05, 69.27815043, 0.00025144, 230.92716811, 0.00083813, -23.09271681, -8.381e-05, -69.27815043, -0.00025144, -230.92716811, -0.00083813, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 92.37086724, 0.02342791, 92.37086724, 0.07028373, 64.65960707, -1561.18356339, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 23.09271681, 8.381e-05, 69.27815043, 0.00025144, 230.92716811, 0.00083813, -23.09271681, -8.381e-05, -69.27815043, -0.00025144, -230.92716811, -0.00083813, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 3.15, 8.4, 5.75)
    ops.node(123010, 3.15, 8.4, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.125, 32789356.50358199, 13662231.87649249, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 146.38700793, 0.00073534, 175.66800796, 0.02824113, 17.5668008, 0.09718221, -146.38700793, -0.00073534, -175.66800796, -0.02824113, -17.5668008, -0.09718221, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 64.54593602, 0.00123968, 77.45670987, 0.02317044, 7.74567099, 0.0634546, -64.54593602, -0.00123968, -77.45670987, -0.02317044, -7.74567099, -0.0634546, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 198.65288349, 0.01470679, 198.65288349, 0.04412036, 139.05701844, -3437.75337668, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 49.66322087, 9.597e-05, 148.98966262, 0.0002879, 496.63220872, 0.00095966, -49.66322087, -9.597e-05, -148.98966262, -0.0002879, -496.63220872, -0.00095966, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 139.24374254, 0.02479358, 139.24374254, 0.07438075, 97.47061978, -1485.8971285, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 34.81093564, 6.727e-05, 104.43280691, 0.0002018, 348.10935636, 0.00067266, -34.81093564, -6.727e-05, -104.43280691, -0.0002018, -348.10935636, -0.00067266, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.5, 8.4, 5.75)
    ops.node(123011, 8.5, 8.4, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.21, 31659380.94517132, 13191408.72715472, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 265.32211419, 0.00070133, 319.85727108, 0.02112827, 31.98572711, 0.06635913, -265.32211419, -0.00070133, -319.85727108, -0.02112827, -31.98572711, -0.06635913, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 128.09682731, 0.00100315, 154.42625936, 0.01852085, 15.44262594, 0.04993704, -128.09682731, -0.00100315, -154.42625936, -0.01852085, -15.44262594, -0.04993704, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 290.07624622, 0.01402664, 290.07624622, 0.04207991, 203.05337235, -3073.03084033, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 72.51906156, 8.639e-05, 217.55718467, 0.00025917, 725.19061555, 0.00086388, -72.51906156, -8.639e-05, -217.55718467, -0.00025917, -725.19061555, -0.00086388, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 196.37735509, 0.02006307, 196.37735509, 0.0601892, 137.46414856, -1691.1105696, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 49.09433877, 5.848e-05, 147.28301632, 0.00017545, 490.94338772, 0.00058484, -49.09433877, -5.848e-05, -147.28301632, -0.00017545, -490.94338772, -0.00058484, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.85, 8.4, 5.75)
    ops.node(123012, 13.85, 8.4, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1, 32553738.24122203, 13564057.60050918, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 78.808884, 0.00079857, 94.62392548, 0.01891276, 9.46239255, 0.07583665, -78.808884, -0.00079857, -94.62392548, -0.01891276, -9.46239255, -0.07583665, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 43.82733309, 0.00117787, 52.62242135, 0.01677533, 5.26224214, 0.05669538, -43.82733309, -0.00117787, -52.62242135, -0.01677533, -5.26224214, -0.05669538, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 139.60280505, 0.01597131, 139.60280505, 0.04791393, 97.72196353, -2384.57182199, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 34.90070126, 8.491e-05, 104.70210379, 0.00025473, 349.00701262, 0.0008491, -34.90070126, -8.491e-05, -104.70210379, -0.00025473, -349.00701262, -0.0008491, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 115.77700976, 0.02355746, 115.77700976, 0.07067237, 81.04390683, -1355.51823368, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 28.94425244, 7.042e-05, 86.83275732, 0.00021126, 289.4425244, 0.00070418, -28.94425244, -7.042e-05, -86.83275732, -0.00021126, -289.4425244, -0.00070418, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 12.6, 5.75)
    ops.node(123013, 0.0, 12.6, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 29433028.67200749, 12263761.94666979, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 31.86061242, 0.00123794, 38.56917517, 0.01874015, 3.85691752, 0.07279271, -31.86061242, -0.00123794, -38.56917517, -0.01874015, -3.85691752, -0.07279271, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 31.86061242, 0.00123794, 38.56917517, 0.01874015, 3.85691752, 0.07279271, -31.86061242, -0.00123794, -38.56917517, -0.01874015, -3.85691752, -0.07279271, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 78.07588742, 0.02475871, 78.07588742, 0.07427612, 54.6531212, -1386.27328896, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 19.51897186, 8.404e-05, 58.55691557, 0.00025211, 195.18971856, 0.00084036, -19.51897186, -8.404e-05, -58.55691557, -0.00025211, -195.18971856, -0.00084036, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 78.07588742, 0.02475871, 78.07588742, 0.07427612, 54.6531212, -1386.27328896, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 19.51897186, 8.404e-05, 58.55691557, 0.00025211, 195.18971856, 0.00084036, -19.51897186, -8.404e-05, -58.55691557, -0.00025211, -195.18971856, -0.00084036, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 3.15, 12.6, 5.75)
    ops.node(123014, 3.15, 12.6, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.125, 30170868.96795686, 12571195.40331536, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 145.75193413, 0.00076756, 176.13437468, 0.03080049, 17.61343747, 0.09644886, -145.75193413, -0.00076756, -176.13437468, -0.03080049, -17.61343747, -0.09644886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 63.96782115, 0.00132368, 77.30211092, 0.02526937, 7.73021109, 0.06362951, -63.96782115, -0.00132368, -77.30211092, -0.02526937, -7.73021109, -0.06362951, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 197.14554184, 0.0153512, 197.14554184, 0.04605361, 138.00187929, -4018.9037265, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 49.28638546, 0.0001035, 147.85915638, 0.00031051, 492.86385461, 0.00103503, -49.28638546, -0.0001035, -147.85915638, -0.00031051, -492.86385461, -0.00103503, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 134.21693687, 0.02647368, 134.21693687, 0.07942103, 93.95185581, -1675.14779226, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 33.55423422, 7.047e-05, 100.66270266, 0.0002114, 335.54234218, 0.00070465, -33.55423422, -7.047e-05, -100.66270266, -0.0002114, -335.54234218, -0.00070465, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.5, 12.6, 5.75)
    ops.node(123015, 8.5, 12.6, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.21, 31286074.76146504, 13035864.48394377, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 271.49174924, 0.00067934, 327.63867184, 0.02425543, 32.76386718, 0.06924325, -271.49174924, -0.00067934, -327.63867184, -0.02425543, -32.76386718, -0.06924325, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 130.3395943, 0.00093882, 157.29498847, 0.02115715, 15.72949885, 0.05240454, -130.3395943, -0.00093882, -157.29498847, -0.02115715, -15.72949885, -0.05240454, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 304.39650925, 0.01358681, 304.39650925, 0.04076042, 213.07755648, -3912.01637997, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 76.09912731, 9.173e-05, 228.29738194, 0.0002752, 760.99127314, 0.00091735, -76.09912731, -9.173e-05, -228.29738194, -0.0002752, -760.99127314, -0.00091735, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 204.28096897, 0.01877637, 204.28096897, 0.05632911, 142.99667828, -2049.4913959, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 51.07024224, 6.156e-05, 153.21072672, 0.00018469, 510.70242241, 0.00061563, -51.07024224, -6.156e-05, -153.21072672, -0.00018469, -510.70242241, -0.00061563, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.85, 12.6, 5.75)
    ops.node(123016, 13.85, 12.6, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1, 30493132.69180626, 12705471.95491927, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 82.64584942, 0.00084564, 99.77761051, 0.01724051, 9.97776105, 0.07196025, -82.64584942, -0.00084564, -99.77761051, -0.01724051, -9.97776105, -0.07196025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 45.6895975, 0.00124441, 55.1606511, 0.01536142, 5.51606511, 0.05373573, -45.6895975, -0.00124441, -55.1606511, -0.01536142, -5.51606511, -0.05373573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 125.48176203, 0.01691281, 125.48176203, 0.05073843, 87.83723342, -2021.62776185, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 31.37044051, 8.148e-05, 94.11132152, 0.00024444, 313.70440508, 0.00081479, -31.37044051, -8.148e-05, -94.11132152, -0.00024444, -313.70440508, -0.00081479, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 102.2238088, 0.02488828, 102.2238088, 0.07466485, 71.55666616, -1183.28339297, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 25.5559522, 6.638e-05, 76.6678566, 0.00019913, 255.55952201, 0.00066377, -25.5559522, -6.638e-05, -76.6678566, -0.00019913, -255.55952201, -0.00066377, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 16.8, 5.75)
    ops.node(123017, 0.0, 16.8, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 28169917.09349846, 11737465.45562436, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 30.09110114, 0.00123588, 36.50931782, 0.01824879, 3.65093178, 0.07051134, -30.09110114, -0.00123588, -36.50931782, -0.01824879, -3.65093178, -0.07051134, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 30.09110114, 0.00123588, 36.50931782, 0.01824879, 3.65093178, 0.07051134, -30.09110114, -0.00123588, -36.50931782, -0.01824879, -3.65093178, -0.07051134, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 70.31093799, 0.02471754, 70.31093799, 0.07415263, 49.21765659, -1288.21651081, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 17.5777345, 7.907e-05, 52.73320349, 0.00023722, 175.77734497, 0.00079072, -17.5777345, -7.907e-05, -52.73320349, -0.00023722, -175.77734497, -0.00079072, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 70.31093799, 0.02471754, 70.31093799, 0.07415263, 49.21765659, -1288.21651081, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 17.5777345, 7.907e-05, 52.73320349, 0.00023722, 175.77734497, 0.00079072, -17.5777345, -7.907e-05, -52.73320349, -0.00023722, -175.77734497, -0.00079072, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 3.15, 16.8, 5.75)
    ops.node(123018, 3.15, 16.8, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.125, 35409311.70032092, 14753879.87513372, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 152.21541358, 0.00074133, 180.97931568, 0.02574055, 18.09793157, 0.0971087, -152.21541358, -0.00074133, -180.97931568, -0.02574055, -18.09793157, -0.0971087, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 67.23486815, 0.00124357, 79.94013313, 0.02117581, 7.99401331, 0.06287817, -67.23486815, -0.00124357, -79.94013313, -0.02117581, -7.99401331, -0.06287817, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 210.3366899, 0.01482657, 210.3366899, 0.04447972, 147.23568293, -3394.76707898, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 52.58417247, 9.409e-05, 157.75251742, 0.00028228, 525.84172474, 0.00094092, -52.58417247, -9.409e-05, -157.75251742, -0.00028228, -525.84172474, -0.00094092, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 149.57263179, 0.02487142, 149.57263179, 0.07461425, 104.70084225, -1471.75599888, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 37.39315795, 6.691e-05, 112.17947384, 0.00020073, 373.93157947, 0.0006691, -37.39315795, -6.691e-05, -112.17947384, -0.00020073, -373.93157947, -0.0006691, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.5, 16.8, 5.75)
    ops.node(123019, 8.5, 16.8, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.21, 30898239.49953636, 12874266.45814015, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 274.72493022, 0.00068938, 331.88691035, 0.02192836, 33.18869103, 0.06665151, -274.72493022, -0.00068938, -331.88691035, -0.02192836, -33.18869103, -0.06665151, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 131.74537562, 0.0009554, 159.15761861, 0.01916949, 15.91576186, 0.05023304, -131.74537562, -0.0009554, -159.15761861, -0.01916949, -15.91576186, -0.05023304, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 290.44618569, 0.01378751, 290.44618569, 0.04136253, 203.31232999, -3404.30720749, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 72.61154642, 8.863e-05, 217.83463927, 0.00026589, 726.11546424, 0.00088629, -72.61154642, -8.863e-05, -217.83463927, -0.00026589, -726.11546424, -0.00088629, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 195.67940104, 0.01910804, 195.67940104, 0.05732413, 136.97558073, -1833.6808309, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 48.91985026, 5.971e-05, 146.75955078, 0.00017913, 489.19850261, 0.00059711, -48.91985026, -5.971e-05, -146.75955078, -0.00017913, -489.19850261, -0.00059711, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 13.85, 16.8, 5.75)
    ops.node(123020, 13.85, 16.8, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1, 31191729.16530515, 12996553.81887715, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 82.5301647, 0.00081263, 99.46829993, 0.02085555, 9.94682999, 0.07638361, -82.5301647, -0.00081263, -99.46829993, -0.02085555, -9.94682999, -0.07638361, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 45.63591562, 0.00117508, 55.00203422, 0.01843328, 5.50020342, 0.05737445, -45.63591562, -0.00117508, -55.00203422, -0.01843328, -5.50020342, -0.05737445, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 142.61565794, 0.01625264, 142.61565794, 0.04875792, 99.83096056, -2757.78111275, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 35.65391448, 9.053e-05, 106.96174345, 0.00027159, 356.53914485, 0.0009053, -35.65391448, -9.053e-05, -106.96174345, -0.00027159, -356.53914485, -0.0009053, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 116.05139112, 0.02350151, 116.05139112, 0.07050454, 81.23597378, -1530.29045643, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 29.01284778, 7.367e-05, 87.03854334, 0.000221, 290.1284778, 0.00073668, -29.01284778, -7.367e-05, -87.03854334, -0.000221, -290.1284778, -0.00073668, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 21.0, 5.75)
    ops.node(123021, 0.0, 21.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 30328327.43030292, 12636803.09595955, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 30.56942465, 0.00120236, 36.93469505, 0.01732429, 3.69346951, 0.07248715, -30.56942465, -0.00120236, -36.93469505, -0.01732429, -3.69346951, -0.07248715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 30.56942465, 0.00120236, 36.93469505, 0.01732429, 3.69346951, 0.07248715, -30.56942465, -0.00120236, -36.93469505, -0.01732429, -3.69346951, -0.07248715, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 69.5365536, 0.02404711, 69.5365536, 0.07214132, 48.67558752, -1209.64917943, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 17.3841384, 7.264e-05, 52.1524152, 0.00021791, 173.84138399, 0.00072636, -17.3841384, -7.264e-05, -52.1524152, -0.00021791, -173.84138399, -0.00072636, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 69.5365536, 0.02404711, 69.5365536, 0.07214132, 48.67558752, -1209.64917943, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 17.3841384, 7.264e-05, 52.1524152, 0.00021791, 173.84138399, 0.00072636, -17.3841384, -7.264e-05, -52.1524152, -0.00021791, -173.84138399, -0.00072636, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 3.15, 21.0, 5.75)
    ops.node(123022, 3.15, 21.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.125, 29991180.37062142, 12496325.15442559, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 144.54819922, 0.00073637, 174.74899503, 0.03195331, 17.4748995, 0.09733552, -144.54819922, -0.00073637, -174.74899503, -0.03195331, -17.4748995, -0.09733552, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 63.85572561, 0.00122892, 77.1972528, 0.02611864, 7.71972528, 0.06432325, -63.85572561, -0.00122892, -77.1972528, -0.02611864, -7.71972528, -0.06432325, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 198.35790214, 0.01472742, 198.35790214, 0.04418226, 138.8505315, -4136.4445159, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 49.58947554, 0.00010476, 148.76842661, 0.00031429, 495.89475535, 0.00104764, -49.58947554, -0.00010476, -148.76842661, -0.00031429, -495.89475535, -0.00104764, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 134.53768913, 0.02457847, 134.53768913, 0.0737354, 94.17638239, -1713.02909283, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 33.63442228, 7.106e-05, 100.90326685, 0.00021317, 336.34422283, 0.00071057, -33.63442228, -7.106e-05, -100.90326685, -0.00021317, -336.34422283, -0.00071057, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 8.5, 21.0, 5.75)
    ops.node(123023, 8.5, 21.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.21, 30639966.19199067, 12766652.57999611, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 266.18833768, 0.00067499, 321.78944876, 0.02415515, 32.17894488, 0.06869482, -266.18833768, -0.00067499, -321.78944876, -0.02415515, -32.17894488, -0.06869482, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 127.83734635, 0.00093439, 154.53986291, 0.02107045, 15.45398629, 0.05200657, -127.83734635, -0.00093439, -154.53986291, -0.02107045, -15.45398629, -0.05200657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 292.7042727, 0.01349983, 292.7042727, 0.04049948, 204.89299089, -3621.79431897, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 73.17606818, 9.007e-05, 219.52820453, 0.00027021, 731.76068175, 0.00090071, -73.17606818, -9.007e-05, -219.52820453, -0.00027021, -731.76068175, -0.00090071, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 196.68968888, 0.01868774, 196.68968888, 0.05606322, 137.68278222, -1926.49540145, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 49.17242222, 6.053e-05, 147.51726666, 0.00018158, 491.72422221, 0.00060526, -49.17242222, -6.053e-05, -147.51726666, -0.00018158, -491.72422221, -0.00060526, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 13.85, 21.0, 5.75)
    ops.node(123024, 13.85, 21.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.1, 33025542.08895647, 13760642.5370652, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 83.93551002, 0.00081306, 100.63271159, 0.0197364, 10.06327116, 0.0770942, -83.93551002, -0.00081306, -100.63271159, -0.0197364, -10.06327116, -0.0770942, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 46.44839347, 0.00117516, 55.68832289, 0.01746934, 5.56883229, 0.05769368, -46.44839347, -0.00117516, -55.68832289, -0.01746934, -5.56883229, -0.05769368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 148.04398464, 0.01626123, 148.04398464, 0.0487837, 103.63078925, -2738.0688964, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 37.01099616, 8.876e-05, 111.03298848, 0.00026627, 370.10996159, 0.00088758, -37.01099616, -8.876e-05, -111.03298848, -0.00026627, -370.10996159, -0.00088758, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 121.6195377, 0.02350314, 121.6195377, 0.07050942, 85.13367639, -1521.11034668, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 30.40488443, 7.292e-05, 91.21465328, 0.00021875, 304.04884425, 0.00072915, -30.40488443, -7.292e-05, -91.21465328, -0.00021875, -304.04884425, -0.00072915, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 25.2, 5.75)
    ops.node(123025, 0.0, 25.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 32380365.31471355, 13491818.88113065, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 27.44100025, 0.00118333, 33.04891417, 0.01867089, 3.30489142, 0.07991044, -27.44100025, -0.00118333, -33.04891417, -0.01867089, -3.30489142, -0.07991044, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 27.44100025, 0.00118333, 33.04891417, 0.01867089, 3.30489142, 0.07991044, -27.44100025, -0.00118333, -33.04891417, -0.01867089, -3.30489142, -0.07991044, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 80.25848686, 0.02366664, 80.25848686, 0.07099992, 56.1809408, -1768.3371513, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 20.06462171, 7.852e-05, 60.19386514, 0.00023557, 200.64621714, 0.00078523, -20.06462171, -7.852e-05, -60.19386514, -0.00023557, -200.64621714, -0.00078523, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 80.25848686, 0.02366664, 80.25848686, 0.07099992, 56.1809408, -1768.3371513, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 20.06462171, 7.852e-05, 60.19386514, 0.00023557, 200.64621714, 0.00078523, -20.06462171, -7.852e-05, -60.19386514, -0.00023557, -200.64621714, -0.00078523, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 3.15, 25.2, 5.75)
    ops.node(123026, 3.15, 25.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0875, 30602999.13451618, 12751249.63938174, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 53.9241682, 0.00124177, 65.12446333, 0.0240015, 6.51244633, 0.07506444, -53.9241682, -0.00124177, -65.12446333, -0.0240015, -6.51244633, -0.07506444, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 67.90491825, 0.00092739, 82.00907879, 0.02645125, 8.20090788, 0.0934686, -67.90491825, -0.00092739, -82.00907879, -0.02645125, -8.20090788, -0.0934686, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 109.39279427, 0.02483535, 109.39279427, 0.07450606, 76.57495599, -1833.04849877, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 27.34819857, 8.089e-05, 82.0445957, 0.00024266, 273.48198568, 0.00080888, -27.34819857, -8.089e-05, -82.0445957, -0.00024266, -273.48198568, -0.00080888, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 129.09241908, 0.01854771, 129.09241908, 0.05564313, 90.36469336, -2910.04201104, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 32.27310477, 9.545e-05, 96.81931431, 0.00028636, 322.7310477, 0.00095454, -32.27310477, -9.545e-05, -96.81931431, -0.00028636, -322.7310477, -0.00095454, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 8.5, 25.2, 5.75)
    ops.node(123027, 8.5, 25.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.1, 27276067.01378705, 11365027.92241127, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 53.32309888, 0.00136298, 64.72501969, 0.02565869, 6.47250197, 0.0666074, -53.32309888, -0.00136298, -64.72501969, -0.02565869, -6.47250197, -0.0666074, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 90.37126285, 0.00091188, 109.69508317, 0.02935943, 10.96950832, 0.08889337, -90.37126285, -0.00091188, -109.69508317, -0.02935943, -10.96950832, -0.08889337, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 104.96514788, 0.02725956, 104.96514788, 0.08177868, 73.47560352, -1537.10985124, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 26.24128697, 7.62e-05, 78.72386091, 0.00022859, 262.4128697, 0.00076195, -26.24128697, -7.62e-05, -78.72386091, -0.00022859, -262.4128697, -0.00076195, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 131.71369244, 0.01823761, 131.71369244, 0.05471284, 92.19958471, -2759.14731764, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 32.92842311, 9.561e-05, 98.78526933, 0.00028684, 329.2842311, 0.00095612, -32.92842311, -9.561e-05, -98.78526933, -0.00028684, -329.2842311, -0.00095612, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 13.85, 25.2, 5.75)
    ops.node(123028, 13.85, 25.2, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 32769380.76241527, 13653908.65100636, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 30.25227959, 0.00119016, 36.31848783, 0.02100391, 3.63184878, 0.07903382, -30.25227959, -0.00119016, -36.31848783, -0.02100391, -3.63184878, -0.07903382, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 30.25227959, 0.00119016, 36.31848783, 0.02100391, 3.63184878, 0.07903382, -30.25227959, -0.00119016, -36.31848783, -0.02100391, -3.63184878, -0.07903382, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 88.75103338, 0.02380328, 88.75103338, 0.07140983, 62.12572337, -1647.05150526, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 22.18775835, 8.58e-05, 66.56327504, 0.0002574, 221.87758346, 0.00085801, -22.18775835, -8.58e-05, -66.56327504, -0.0002574, -221.87758346, -0.00085801, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 88.75103338, 0.02380328, 88.75103338, 0.07140983, 62.12572337, -1647.05150526, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 22.18775835, 8.58e-05, 66.56327504, 0.0002574, 221.87758346, 0.00085801, -22.18775835, -8.58e-05, -66.56327504, -0.0002574, -221.87758346, -0.00085801, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.5, 0.0, 8.5)
    ops.node(124003, 8.5, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.1, 30044257.62528654, 12518440.67720272, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 34.12806833, 0.00129535, 41.45005796, 0.01993663, 4.1450058, 0.06400249, -34.12806833, -0.00129535, -41.45005796, -0.01993663, -4.1450058, -0.06400249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 63.41503849, 0.00085801, 77.02038672, 0.02250717, 7.70203867, 0.08534277, -63.41503849, -0.00085801, -77.02038672, -0.02250717, -7.70203867, -0.08534277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 100.98927094, 0.0259069, 100.98927094, 0.0777207, 70.69248966, -2376.88282785, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 25.24731774, 6.655e-05, 75.74195321, 0.00019966, 252.47317735, 0.00066555, -25.24731774, -6.655e-05, -75.74195321, -0.00019966, -252.47317735, -0.00066555, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 126.73374068, 0.01716022, 126.73374068, 0.05148066, 88.71361848, -5255.66520176, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 31.68343517, 8.352e-05, 95.05030551, 0.00025056, 316.8343517, 0.00083521, -31.68343517, -8.352e-05, -95.05030551, -0.00025056, -316.8343517, -0.00083521, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.85, 0.0, 8.5)
    ops.node(124004, 13.85, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 31565896.55974474, 13152456.89989364, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 23.40134323, 0.00109086, 28.30455698, 0.01804335, 2.8304557, 0.08207234, -23.40134323, -0.00109086, -28.30455698, -0.01804335, -2.8304557, -0.08207234, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 23.40134323, 0.00109086, 28.30455698, 0.01804335, 2.8304557, 0.08207234, -23.40134323, -0.00109086, -28.30455698, -0.01804335, -2.8304557, -0.08207234, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 64.58027761, 0.02181712, 64.58027761, 0.06545136, 45.20619432, -2422.05737456, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 16.1450694, 6.481e-05, 48.4352082, 0.00019444, 161.45069401, 0.00064814, -16.1450694, -6.481e-05, -48.4352082, -0.00019444, -161.45069401, -0.00064814, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 64.58027761, 0.02181712, 64.58027761, 0.06545136, 45.20619432, -2422.05737456, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 16.1450694, 6.481e-05, 48.4352082, 0.00019444, 161.45069401, 0.00064814, -16.1450694, -6.481e-05, -48.4352082, -0.00019444, -161.45069401, -0.00064814, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.2, 8.5)
    ops.node(124005, 0.0, 4.2, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 27729973.64045276, 11554155.68352198, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 22.93966557, 0.00131761, 27.99894993, 0.02376741, 2.79989499, 0.08418168, -22.93966557, -0.00131761, -27.99894993, -0.02376741, -2.79989499, -0.08418168, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 22.93966557, 0.00131761, 27.99894993, 0.02376741, 2.79989499, 0.08418168, -22.93966557, -0.00131761, -27.99894993, -0.02376741, -2.79989499, -0.08418168, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 75.18487389, 0.02635221, 75.18487389, 0.07905663, 52.62941173, -2751.73541476, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 18.79621847, 8.589e-05, 56.38865542, 0.00025768, 187.96218473, 0.00085895, -18.79621847, -8.589e-05, -56.38865542, -0.00025768, -187.96218473, -0.00085895, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 75.18487389, 0.02635221, 75.18487389, 0.07905663, 52.62941173, -2751.73541476, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 18.79621847, 8.589e-05, 56.38865542, 0.00025768, 187.96218473, 0.00085895, -18.79621847, -8.589e-05, -56.38865542, -0.00025768, -187.96218473, -0.00085895, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 3.15, 4.2, 8.5)
    ops.node(124006, 3.15, 4.2, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.125, 31965593.52345823, 13318997.30144093, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 122.58724564, 0.0007337, 147.98879984, 0.02064758, 14.79887998, 0.07522469, -122.58724564, -0.0007337, -147.98879984, -0.02064758, -14.79887998, -0.07522469, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 52.73731158, 0.00124089, 63.6651179, 0.01750522, 6.36651179, 0.05126943, -52.73731158, -0.00124089, -63.6651179, -0.01750522, -6.36651179, -0.05126943, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 161.33676534, 0.01467402, 161.33676534, 0.04402206, 112.93573574, -3825.67390582, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 40.33419134, 7.995e-05, 121.00257401, 0.00023984, 403.34191335, 0.00079948, -40.33419134, -7.995e-05, -121.00257401, -0.00023984, -403.34191335, -0.00079948, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 104.11058781, 0.02481787, 104.11058781, 0.0744536, 72.87741147, -1334.80810498, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 26.02764695, 5.159e-05, 78.08294086, 0.00015477, 260.27646953, 0.0005159, -26.02764695, -5.159e-05, -78.08294086, -0.00015477, -260.27646953, -0.0005159, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.5, 4.2, 8.5)
    ops.node(124007, 8.5, 4.2, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.21, 30643008.21673224, 12767920.0903051, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 216.1495911, 0.0006549, 262.17953567, 0.02160424, 26.21795357, 0.0648278, -216.1495911, -0.0006549, -262.17953567, -0.02160424, -26.21795357, -0.0648278, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 100.62414951, 0.00090921, 122.05247608, 0.01904909, 12.20524761, 0.04976615, -100.62414951, -0.00090921, -122.05247608, -0.01904909, -12.20524761, -0.04976615, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 261.45023212, 0.01309801, 261.45023212, 0.03929403, 183.01516248, -5528.39006502, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 65.36255803, 8.045e-05, 196.08767409, 0.00024134, 653.62558029, 0.00080446, -65.36255803, -8.045e-05, -196.08767409, -0.00024134, -653.62558029, -0.00080446, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 175.48621373, 0.0181842, 175.48621373, 0.05455259, 122.84034961, -2340.68800713, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 43.87155343, 5.4e-05, 131.6146603, 0.00016199, 438.71553433, 0.00053995, -43.87155343, -5.4e-05, -131.6146603, -0.00016199, -438.71553433, -0.00053995, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.85, 4.2, 8.5)
    ops.node(124008, 13.85, 4.2, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1, 31159251.63887655, 12983021.51619856, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 62.38463257, 0.00077805, 75.52596868, 0.0179022, 7.55259687, 0.08117059, -62.38463257, -0.00077805, -75.52596868, -0.0179022, -7.55259687, -0.08117059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 33.45302378, 0.00112495, 40.49991035, 0.01586992, 4.04999104, 0.06023929, -33.45302378, -0.00112495, -40.49991035, -0.01586992, -4.04999104, -0.06023929, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 115.61382304, 0.01556095, 115.61382304, 0.04668286, 80.92967613, -3480.11290602, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 28.90345576, 7.347e-05, 86.71036728, 0.0002204, 289.03455761, 0.00073466, -28.90345576, -7.347e-05, -86.71036728, -0.0002204, -289.03455761, -0.00073466, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 89.80032081, 0.02249903, 89.80032081, 0.06749708, 62.86022457, -1626.12746815, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 22.4500802, 5.706e-05, 67.35024061, 0.00017119, 224.50080204, 0.00057063, -22.4500802, -5.706e-05, -67.35024061, -0.00017119, -224.50080204, -0.00057063, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.4, 8.5)
    ops.node(124009, 0.0, 8.4, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 30773524.16792804, 12822301.73663668, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 23.90935316, 0.00120462, 28.98790224, 0.0183913, 2.89879022, 0.08209004, -23.90935316, -0.00120462, -28.98790224, -0.0183913, -2.89879022, -0.08209004, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 23.90935316, 0.00120462, 28.98790224, 0.0183913, 2.89879022, 0.08209004, -23.90935316, -0.00120462, -28.98790224, -0.0183913, -2.89879022, -0.08209004, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 66.48181701, 0.0240923, 66.48181701, 0.07227691, 46.5372719, -2451.48139128, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 16.62045425, 6.844e-05, 49.86136275, 0.00020532, 166.20454251, 0.0006844, -16.62045425, -6.844e-05, -49.86136275, -0.00020532, -166.20454251, -0.0006844, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 66.48181701, 0.0240923, 66.48181701, 0.07227691, 46.5372719, -2451.48139128, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 16.62045425, 6.844e-05, 49.86136275, 0.00020532, 166.20454251, 0.0006844, -16.62045425, -6.844e-05, -49.86136275, -0.00020532, -166.20454251, -0.0006844, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 3.15, 8.4, 8.5)
    ops.node(124010, 3.15, 8.4, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.125, 30464840.46705861, 12693683.52794109, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 114.88661591, 0.00074115, 139.36503752, 0.02029599, 13.93650375, 0.074848, -114.88661591, -0.00074115, -139.36503752, -0.02029599, -13.93650375, -0.074848, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 48.98564085, 0.00129541, 59.4228111, 0.0172665, 5.94228111, 0.05101518, -48.98564085, -0.00129541, -59.4228111, -0.0172665, -5.94228111, -0.05101518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 148.91005283, 0.01482299, 148.91005283, 0.04446897, 104.23703698, -3753.78379911, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 37.22751321, 7.742e-05, 111.68253962, 0.00023227, 372.27513207, 0.00077425, -37.22751321, -7.742e-05, -111.68253962, -0.00023227, -372.27513207, -0.00077425, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 88.99467609, 0.02590825, 88.99467609, 0.07772474, 62.29627326, -1283.81795354, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 22.24866902, 4.627e-05, 66.74600707, 0.00013882, 222.48669022, 0.00046272, -22.24866902, -4.627e-05, -66.74600707, -0.00013882, -222.48669022, -0.00046272, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.5, 8.4, 8.5)
    ops.node(124011, 8.5, 8.4, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.21, 31413547.41988742, 13088978.09161976, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 221.20883023, 0.00067065, 267.69240662, 0.02031931, 26.76924066, 0.06370938, -221.20883023, -0.00067065, -267.69240662, -0.02031931, -26.76924066, -0.06370938, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 103.13150353, 0.000941, 124.80297621, 0.01795463, 12.48029762, 0.04879001, -103.13150353, -0.000941, -124.80297621, -0.01795463, -12.48029762, -0.04879001, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 262.28163428, 0.0134131, 262.28163428, 0.04023929, 183.597144, -4918.34156879, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 65.57040857, 7.872e-05, 196.71122571, 0.00023617, 655.7040857, 0.00078722, -65.57040857, -7.872e-05, -196.71122571, -0.00023617, -655.7040857, -0.00078722, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 176.87753626, 0.01881998, 176.87753626, 0.05645993, 123.81427538, -2108.43287924, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 44.21938407, 5.309e-05, 132.6581522, 0.00015927, 442.19384066, 0.00053089, -44.21938407, -5.309e-05, -132.6581522, -0.00015927, -442.19384066, -0.00053089, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.85, 8.4, 8.5)
    ops.node(124012, 13.85, 8.4, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1, 34990466.72894374, 14579361.13705989, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 63.05806937, 0.00077339, 75.31062109, 0.01670923, 7.53106211, 0.08113361, -63.05806937, -0.00077339, -75.31062109, -0.01670923, -7.53106211, -0.08113361, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 33.94608994, 0.00112437, 40.54201377, 0.01484612, 4.05420138, 0.06002618, -33.94608994, -0.00112437, -40.54201377, -0.01484612, -4.05420138, -0.06002618, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 128.29439212, 0.01546782, 128.29439212, 0.04640347, 89.80607449, -3545.60329231, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 32.07359803, 7.26e-05, 96.22079409, 0.00021779, 320.73598031, 0.00072598, -32.07359803, -7.26e-05, -96.22079409, -0.00021779, -320.73598031, -0.00072598, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 104.29788763, 0.02248732, 104.29788763, 0.06746195, 73.00852134, -1654.09568211, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 26.07447191, 5.902e-05, 78.22341572, 0.00017706, 260.74471907, 0.00059019, -26.07447191, -5.902e-05, -78.22341572, -0.00017706, -260.74471907, -0.00059019, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 12.6, 8.5)
    ops.node(124013, 0.0, 12.6, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 28986713.76592508, 12077797.40246878, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 23.24380603, 0.00117631, 28.31801128, 0.02369648, 2.83180113, 0.08670051, -23.24380603, -0.00117631, -28.31801128, -0.02369648, -2.83180113, -0.08670051, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 23.24380603, 0.00117631, 28.31801128, 0.02369648, 2.83180113, 0.08670051, -23.24380603, -0.00117631, -28.31801128, -0.02369648, -2.83180113, -0.08670051, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 76.77214157, 0.02352615, 76.77214157, 0.07057845, 53.7404991, -3710.18142553, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 19.19303539, 8.391e-05, 57.57910618, 0.00025172, 191.93035392, 0.00083905, -19.19303539, -8.391e-05, -57.57910618, -0.00025172, -191.93035392, -0.00083905, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 76.77214157, 0.02352615, 76.77214157, 0.07057845, 53.7404991, -3710.18142553, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 19.19303539, 8.391e-05, 57.57910618, 0.00025172, 191.93035392, 0.00083905, -19.19303539, -8.391e-05, -57.57910618, -0.00025172, -191.93035392, -0.00083905, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 3.15, 12.6, 8.5)
    ops.node(124014, 3.15, 12.6, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.125, 30275935.9935401, 12614973.33064171, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 117.91841168, 0.00072243, 143.11852827, 0.02104212, 14.31185283, 0.07552335, -117.91841168, -0.00072243, -143.11852827, -0.02104212, -14.31185283, -0.07552335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 50.69822327, 0.00120893, 61.53284289, 0.01780469, 6.15328429, 0.05150959, -50.69822327, -0.00120893, -61.53284289, -0.01780469, -6.15328429, -0.05150959, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 147.40492052, 0.01444866, 147.40492052, 0.04334597, 103.18344436, -3685.62404542, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 36.85123013, 7.712e-05, 110.55369039, 0.00023136, 368.5123013, 0.0007712, -36.85123013, -7.712e-05, -110.55369039, -0.00023136, -368.5123013, -0.0007712, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 91.78171507, 0.02417862, 91.78171507, 0.07253585, 64.24720055, -1263.87435375, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 22.94542877, 4.802e-05, 68.8362863, 0.00014406, 229.45428767, 0.00048019, -22.94542877, -4.802e-05, -68.8362863, -0.00014406, -229.45428767, -0.00048019, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.5, 12.6, 8.5)
    ops.node(124015, 8.5, 12.6, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.21, 28099157.52460898, 11707982.30192041, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 216.27513858, 0.00068469, 264.06821331, 0.02075192, 26.40682133, 0.06328059, -216.27513858, -0.00068469, -264.06821331, -0.02075192, -26.40682133, -0.06328059, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 100.4404653, 0.00096911, 122.63607547, 0.01834518, 12.26360755, 0.0485684, -100.4404653, -0.00096911, -122.63607547, -0.01834518, -12.26360755, -0.0485684, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 228.0388387, 0.01369385, 228.0388387, 0.04108155, 159.62718709, -4372.09543658, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 57.00970967, 7.652e-05, 171.02912902, 0.00022955, 570.09709674, 0.00076518, -57.00970967, -7.652e-05, -171.02912902, -0.00022955, -570.09709674, -0.00076518, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 153.11043092, 0.01938221, 153.11043092, 0.05814662, 107.17730164, -1899.13386955, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 38.27760773, 5.138e-05, 114.83282319, 0.00015413, 382.7760773, 0.00051376, -38.27760773, -5.138e-05, -114.83282319, -0.00015413, -382.7760773, -0.00051376, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.85, 12.6, 8.5)
    ops.node(124016, 13.85, 12.6, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1, 32390218.73811891, 13495924.47421621, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 61.89779675, 0.0008381, 74.64348608, 0.0165975, 7.46434861, 0.0803003, -61.89779675, -0.0008381, -74.64348608, -0.0165975, -7.46434861, -0.0803003, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 33.588563, 0.00127638, 40.5049544, 0.01484622, 4.05049544, 0.05952023, -33.588563, -0.00127638, -40.5049544, -0.01484622, -4.05049544, -0.05952023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 115.78973438, 0.01676197, 115.78973438, 0.05028591, 81.05281407, -3100.18660447, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 28.9474336, 7.078e-05, 86.84230079, 0.00021235, 289.47433596, 0.00070782, -28.9474336, -7.078e-05, -86.84230079, -0.00021235, -289.47433596, -0.00070782, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 89.00060868, 0.02552766, 89.00060868, 0.07658298, 62.30042607, -1463.4101618, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 22.25015217, 5.441e-05, 66.75045651, 0.00016322, 222.50152169, 0.00054406, -22.25015217, -5.441e-05, -66.75045651, -0.00016322, -222.50152169, -0.00054406, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 16.8, 8.5)
    ops.node(124017, 0.0, 16.8, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 31941059.28846615, 13308774.70352756, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 22.5260408, 0.00110051, 27.21206406, 0.01803338, 2.72120641, 0.08210272, -22.5260408, -0.00110051, -27.21206406, -0.01803338, -2.72120641, -0.08210272, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 22.5260408, 0.00110051, 27.21206406, 0.01803338, 2.72120641, 0.08210272, -22.5260408, -0.00110051, -27.21206406, -0.01803338, -2.72120641, -0.08210272, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 64.65952706, 0.0220103, 64.65952706, 0.06603089, 45.26166894, -2335.26387363, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 16.16488177, 6.413e-05, 48.4946453, 0.00019239, 161.64881766, 0.00064131, -16.16488177, -6.413e-05, -48.4946453, -0.00019239, -161.64881766, -0.00064131, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 64.65952706, 0.0220103, 64.65952706, 0.06603089, 45.26166894, -2335.26387363, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 16.16488177, 6.413e-05, 48.4946453, 0.00019239, 161.64881766, 0.00064131, -16.16488177, -6.413e-05, -48.4946453, -0.00019239, -161.64881766, -0.00064131, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 3.15, 16.8, 8.5)
    ops.node(124018, 3.15, 16.8, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.125, 29729058.49416246, 12387107.70590102, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 114.28902048, 0.00072656, 138.91879011, 0.01952313, 13.89187901, 0.07378884, -114.28902048, -0.00072656, -138.91879011, -0.01952313, -13.89187901, -0.07378884, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 48.84296966, 0.00124266, 59.3688372, 0.01659444, 5.93688372, 0.050166, -48.84296966, -0.00124266, -59.3688372, -0.01659444, -5.93688372, -0.050166, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 141.16098988, 0.01453112, 141.16098988, 0.04359337, 98.81269291, -3310.74388272, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 35.29024747, 7.521e-05, 105.87074241, 0.00022564, 352.90247469, 0.00075212, -35.29024747, -7.521e-05, -105.87074241, -0.00022564, -352.90247469, -0.00075212, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 78.87726033, 0.02485314, 78.87726033, 0.07455941, 55.21408223, -1153.68047663, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 19.71931508, 4.203e-05, 59.15794525, 0.00012608, 197.19315082, 0.00042027, -19.71931508, -4.203e-05, -59.15794525, -0.00012608, -197.19315082, -0.00042027, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.5, 16.8, 8.5)
    ops.node(124019, 8.5, 16.8, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.21, 30782272.0230338, 12825946.67626408, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 222.65783639, 0.00065575, 269.96327326, 0.0192416, 26.99632733, 0.06249655, -222.65783639, -0.00065575, -269.96327326, -0.0192416, -26.99632733, -0.06249655, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 103.49928206, 0.00090125, 125.48853173, 0.0169946, 12.54885317, 0.04773396, -103.49928206, -0.00090125, -125.48853173, -0.0169946, -12.54885317, -0.04773396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 248.84777834, 0.01311491, 248.84777834, 0.03934473, 174.19344484, -4174.56330098, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 62.21194459, 7.622e-05, 186.63583376, 0.00022867, 622.11944586, 0.00076222, -62.21194459, -7.622e-05, -186.63583376, -0.00022867, -622.11944586, -0.00076222, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 168.29749065, 0.01802491, 168.29749065, 0.05407474, 117.80824345, -1823.09004311, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 42.07437266, 5.155e-05, 126.22311799, 0.00015465, 420.74372662, 0.00051549, -42.07437266, -5.155e-05, -126.22311799, -0.00015465, -420.74372662, -0.00051549, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 13.85, 16.8, 8.5)
    ops.node(124020, 13.85, 16.8, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1, 31870350.82702997, 13279312.84459582, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 62.45158181, 0.00076794, 75.43985845, 0.0196234, 7.54398584, 0.08315122, -62.45158181, -0.00076794, -75.43985845, -0.0196234, -7.54398584, -0.08315122, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 33.50604006, 0.0011048, 40.47440986, 0.01734054, 4.04744099, 0.06189185, -33.50604006, -0.0011048, -40.47440986, -0.01734054, -4.04744099, -0.06189185, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 121.80800621, 0.01535873, 121.80800621, 0.0460762, 85.26560435, -3929.93415603, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 30.45200155, 7.568e-05, 91.35600466, 0.00022703, 304.52001553, 0.00075675, -30.45200155, -7.568e-05, -91.35600466, -0.00022703, -304.52001553, -0.00075675, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 99.99013099, 0.02209606, 99.99013099, 0.06628819, 69.9930917, -1817.80389938, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 24.99753275, 6.212e-05, 74.99259825, 0.00018636, 249.97532749, 0.00062121, -24.99753275, -6.212e-05, -74.99259825, -0.00018636, -249.97532749, -0.00062121, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 21.0, 8.5)
    ops.node(124021, 0.0, 21.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 31961813.47337841, 13317422.28057434, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 24.05746416, 0.00113744, 29.06009859, 0.01961228, 2.90600986, 0.0836877, -24.05746416, -0.00113744, -29.06009859, -0.01961228, -2.90600986, -0.0836877, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 24.05746416, 0.00113744, 29.06009859, 0.01961228, 2.90600986, 0.0836877, -24.05746416, -0.00113744, -29.06009859, -0.01961228, -2.90600986, -0.0836877, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 76.72001322, 0.02274879, 76.72001322, 0.06824636, 53.70400925, -2896.80810387, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 19.18000331, 7.604e-05, 57.54000992, 0.00022813, 191.80003305, 0.00076044, -19.18000331, -7.604e-05, -57.54000992, -0.00022813, -191.80003305, -0.00076044, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 76.72001322, 0.02274879, 76.72001322, 0.06824636, 53.70400925, -2896.80810387, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 19.18000331, 7.604e-05, 57.54000992, 0.00022813, 191.80003305, 0.00076044, -19.18000331, -7.604e-05, -57.54000992, -0.00022813, -191.80003305, -0.00076044, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 3.15, 21.0, 8.5)
    ops.node(124022, 3.15, 21.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.125, 29441770.02975371, 12267404.17906405, 0.00178813, 0.00071615, 0.00286458, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 119.64871074, 0.00074284, 145.54194411, 0.02060254, 14.55419441, 0.07474835, -119.64871074, -0.00074284, -145.54194411, -0.02060254, -14.55419441, -0.07474835, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 51.34845433, 0.00125516, 62.46079732, 0.01747524, 6.24607973, 0.05097263, -51.34845433, -0.00125516, -62.46079732, -0.01747524, -6.24607973, -0.05097263, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 146.10890561, 0.01485672, 146.10890561, 0.04457016, 102.27623392, -3914.85753139, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 36.5272264, 7.861e-05, 109.5816792, 0.00023582, 365.27226401, 0.00078608, -36.5272264, -7.861e-05, -109.5816792, -0.00023582, -365.27226401, -0.00078608, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 86.44174767, 0.02510328, 86.44174767, 0.07530985, 60.50922337, -1330.84522474, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 21.61043692, 4.651e-05, 64.83131076, 0.00013952, 216.10436918, 0.00046507, -21.61043692, -4.651e-05, -64.83131076, -0.00013952, -216.10436918, -0.00046507, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 8.5, 21.0, 8.5)
    ops.node(124023, 8.5, 21.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.21, 33466619.38917395, 13944424.74548914, 0.00545409, 0.00235812, 0.00693, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 215.05786655, 0.00066752, 258.43874093, 0.01943065, 25.84387409, 0.06318999, -215.05786655, -0.00066752, -258.43874093, -0.01943065, -25.84387409, -0.06318999, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 101.18440189, 0.00095266, 121.59503786, 0.01719951, 12.15950379, 0.04829732, -101.18440189, -0.00095266, -121.59503786, -0.01719951, -12.15950379, -0.04829732, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 276.33492281, 0.01335049, 276.33492281, 0.04005147, 193.43444597, -4467.61948316, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 69.0837307, 7.785e-05, 207.25119211, 0.00023356, 690.83730703, 0.00077852, -69.0837307, -7.785e-05, -207.25119211, -0.00023356, -690.83730703, -0.00077852, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 187.56204235, 0.01905317, 187.56204235, 0.0571595, 131.29342964, -1935.83612286, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 46.89051059, 5.284e-05, 140.67153176, 0.00015853, 468.90510587, 0.00052842, -46.89051059, -5.284e-05, -140.67153176, -0.00015853, -468.90510587, -0.00052842, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 13.85, 21.0, 8.5)
    ops.node(124024, 13.85, 21.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.1, 32638099.83738373, 13599208.26557655, 0.00127345, 0.00057292, 0.00146667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 60.64820281, 0.00079336, 73.07520964, 0.02094329, 7.30752096, 0.08472547, -60.64820281, -0.00079336, -73.07520964, -0.02094329, -7.30752096, -0.08472547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 32.74550596, 0.00118067, 39.45516276, 0.01853102, 3.94551628, 0.06326071, -32.74550596, -0.00118067, -39.45516276, -0.01853102, -3.94551628, -0.06326071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 130.32875402, 0.01586713, 130.32875402, 0.0476014, 91.23012781, -4669.28718295, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 32.5821885, 7.906e-05, 97.74656551, 0.00023719, 325.82188504, 0.00079064, -32.5821885, -7.906e-05, -97.74656551, -0.00023719, -325.82188504, -0.00079064, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 106.20856884, 0.02361332, 106.20856884, 0.07083996, 74.34599819, -2130.98414974, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 26.55214221, 6.443e-05, 79.65642663, 0.0001933, 265.52142209, 0.00064432, -26.55214221, -6.443e-05, -79.65642663, -0.0001933, -265.52142209, -0.00064432, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 25.2, 8.5)
    ops.node(124025, 0.0, 25.2, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 29168162.10824942, 12153400.87843726, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 22.58805404, 0.00116333, 27.53217193, 0.02001952, 2.75321719, 0.08487526, -22.58805404, -0.00116333, -27.53217193, -0.02001952, -2.75321719, -0.08487526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 22.58805404, 0.00116333, 27.53217193, 0.02001952, 2.75321719, 0.08487526, -22.58805404, -0.00116333, -27.53217193, -0.02001952, -2.75321719, -0.08487526, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 68.96799026, 0.02326654, 68.96799026, 0.06979961, 48.27759318, -4762.10013068, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 17.24199756, 7.491e-05, 51.72599269, 0.00022472, 172.41997565, 0.00074907, -17.24199756, -7.491e-05, -51.72599269, -0.00022472, -172.41997565, -0.00074907, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 68.96799026, 0.02326654, 68.96799026, 0.06979961, 48.27759318, -4762.10013068, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 17.24199756, 7.491e-05, 51.72599269, 0.00022472, 172.41997565, 0.00074907, -17.24199756, -7.491e-05, -51.72599269, -0.00022472, -172.41997565, -0.00074907, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 3.15, 25.2, 8.5)
    ops.node(124026, 3.15, 25.2, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0875, 33342350.53081751, 13892646.0545073, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 33.4236574, 0.0011238, 40.18086541, 0.01583196, 4.01808654, 0.06555482, -33.4236574, -0.0011238, -40.18086541, -0.01583196, -4.01808654, -0.06555482, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 54.11027849, 0.00085686, 65.04966799, 0.01725838, 6.5049668, 0.08164817, -54.11027849, -0.00085686, -65.04966799, -0.01725838, -6.5049668, -0.08164817, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 89.35161966, 0.02247598, 89.35161966, 0.06742795, 62.54613376, -2020.63458328, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 22.33790491, 6.064e-05, 67.01371474, 0.00018192, 223.37904914, 0.00060641, -22.33790491, -6.064e-05, -67.01371474, -0.00018192, -223.37904914, -0.00060641, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 108.02875833, 0.01713722, 108.02875833, 0.05141167, 75.62013083, -3567.54528431, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 27.00718958, 7.332e-05, 81.02156875, 0.00021995, 270.07189584, 0.00073316, -27.00718958, -7.332e-05, -81.02156875, -0.00021995, -270.07189584, -0.00073316, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 8.5, 25.2, 8.5)
    ops.node(124027, 8.5, 25.2, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.1, 32452913.84218792, 13522047.43424497, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 43.12608912, 0.00124307, 51.99602315, 0.01573915, 5.19960232, 0.05517883, -43.12608912, -0.00124307, -51.99602315, -0.01573915, -5.19960232, -0.05517883, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 73.89578438, 0.00084302, 89.09425811, 0.01755465, 8.90942581, 0.07282003, -73.89578438, -0.00084302, -89.09425811, -0.01755465, -8.90942581, -0.07282003, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 69.32514743, 0.02486132, 69.32514743, 0.07458396, 48.5276032, -1276.33787086, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 17.33128686, 4.23e-05, 51.99386057, 0.00012689, 173.31286857, 0.00042296, -17.33128686, -4.23e-05, -51.99386057, -0.00012689, -173.31286857, -0.00042296, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 111.44884372, 0.01686039, 111.44884372, 0.05058118, 78.0141906, -2667.93986658, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 27.86221093, 6.8e-05, 83.58663279, 0.00020399, 278.62210929, 0.00067997, -27.86221093, -6.8e-05, -83.58663279, -0.00020399, -278.62210929, -0.00067997, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 13.85, 25.2, 8.5)
    ops.node(124028, 13.85, 25.2, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 32777624.47073738, 13657343.52947391, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 24.29835043, 0.00110655, 29.27138719, 0.01824805, 2.92713872, 0.08261433, -24.29835043, -0.00110655, -29.27138719, -0.01824805, -2.92713872, -0.08261433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 24.29835043, 0.00110655, 29.27138719, 0.01824805, 2.92713872, 0.08261433, -24.29835043, -0.00110655, -29.27138719, -0.01824805, -2.92713872, -0.08261433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 74.9722366, 0.02213097, 74.9722366, 0.0663929, 52.48056562, -2857.5290098, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 18.74305915, 7.246e-05, 56.22917745, 0.00021738, 187.4305915, 0.00072462, -18.74305915, -7.246e-05, -56.22917745, -0.00021738, -187.4305915, -0.00072462, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 74.9722366, 0.02213097, 74.9722366, 0.0663929, 52.48056562, -2857.5290098, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 18.74305915, 7.246e-05, 56.22917745, 0.00021738, 187.4305915, 0.00072462, -18.74305915, -7.246e-05, -56.22917745, -0.00021738, -187.4305915, -0.00072462, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124029, 0.0, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 170001, 124029, 0.0625, 31377253.01256163, 13073855.42190068, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 34.88854927, 0.00092407, 41.95836775, 0.02354829, 4.19583677, 0.08717604, -34.88854927, -0.00092407, -41.95836775, -0.02354829, -4.19583677, -0.08717604, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 34.88854927, 0.00092407, 41.95836775, 0.02354829, 4.19583677, 0.08717604, -34.88854927, -0.00092407, -41.95836775, -0.02354829, -4.19583677, -0.08717604, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 100.89937798, 0.01848146, 100.89937798, 0.05544437, 70.62956458, -3327.03091525, 0.05, 2, 0, 70001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 25.22484449, 5.094e-05, 75.67453348, 0.00015281, 252.24844494, 0.00050936, -25.22484449, -5.094e-05, -75.67453348, -0.00015281, -252.24844494, -0.00050936, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 100.89937798, 0.01848146, 100.89937798, 0.05544437, 70.62956458, -3327.03091525, 0.05, 2, 0, 70001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 25.22484449, 5.094e-05, 75.67453348, 0.00015281, 252.24844494, 0.00050936, -25.22484449, -5.094e-05, -75.67453348, -0.00015281, -252.24844494, -0.00050936, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 1.575)
    ops.node(121001, 0.0, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174029, 121001, 0.0625, 29766670.20121895, 12402779.2505079, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 31.622485, 0.00085799, 38.22479827, 0.0367828, 3.82247983, 0.11850186, -31.622485, -0.00085799, -38.22479827, -0.0367828, -3.82247983, -0.11850186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 31.622485, 0.00085799, 38.22479827, 0.0367828, 3.82247983, 0.11850186, -31.622485, -0.00085799, -38.22479827, -0.0367828, -3.82247983, -0.11850186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 121.21012972, 0.01715976, 121.21012972, 0.05147927, 84.8470908, -6787.99800674, 0.05, 2, 0, 74029, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 30.30253243, 6.45e-05, 90.90759729, 0.0001935, 303.02532429, 0.00064501, -30.30253243, -6.45e-05, -90.90759729, -0.0001935, -303.02532429, -0.00064501, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 121.21012972, 0.01715976, 121.21012972, 0.05147927, 84.8470908, -6787.99800674, 0.05, 2, 0, 74029, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 30.30253243, 6.45e-05, 90.90759729, 0.0001935, 303.02532429, 0.00064501, -30.30253243, -6.45e-05, -90.90759729, -0.0001935, -303.02532429, -0.00064501, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 3.15, 0.0, 0.0)
    ops.node(124030, 3.15, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 170002, 124030, 0.12, 33893999.72372704, 14122499.88488627, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 116.06612394, 0.00076001, 138.36259122, 0.04070496, 13.83625912, 0.11817814, -116.06612394, -0.00076001, -138.36259122, -0.04070496, -13.83625912, -0.11817814, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 128.63627413, 0.0006674, 153.34748511, 0.04513411, 15.33474851, 0.14504826, -128.63627413, -0.0006674, -153.34748511, -0.04513411, -15.33474851, -0.14504826, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 273.00763508, 0.0152002, 273.00763508, 0.04560059, 191.10534456, -9462.53452872, 0.05, 2, 0, 70002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 68.25190877, 6.645e-05, 204.75572631, 0.00019936, 682.51908771, 0.00066452, -68.25190877, -6.645e-05, -204.75572631, -0.00019936, -682.51908771, -0.00066452, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 364.01018011, 0.01334796, 364.01018011, 0.04004389, 254.80712608, -14099.57722606, 0.05, 2, 0, 70002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 91.00254503, 8.86e-05, 273.00763508, 0.00026581, 910.02545027, 0.00088602, -91.00254503, -8.86e-05, -273.00763508, -0.00026581, -910.02545027, -0.00088602, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 3.15, 0.0, 1.575)
    ops.node(121002, 3.15, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 174030, 121002, 0.12, 31611656.73258133, 13171523.63857556, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 88.4363843, 0.00082161, 106.16435173, 0.04025742, 10.61643517, 0.11484841, -88.4363843, -0.00082161, -106.16435173, -0.04025742, -10.61643517, -0.11484841, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 107.21515632, 0.00070768, 128.70751849, 0.04460762, 12.87075185, 0.14080473, -107.21515632, -0.00070768, -128.70751849, -0.04460762, -12.87075185, -0.14080473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 262.42871585, 0.01643216, 262.42871585, 0.04929649, 183.7001011, -10193.8063778, 0.05, 2, 0, 74030, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 65.60717896, 6.849e-05, 196.82153689, 0.00020547, 656.07178964, 0.00068489, -65.60717896, -6.849e-05, -196.82153689, -0.00020547, -656.07178964, -0.00068489, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 349.90495447, 0.01415364, 349.90495447, 0.04246092, 244.93346813, -15395.04888406, 0.05, 2, 0, 74030, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 87.47623862, 9.132e-05, 262.42871585, 0.00027395, 874.76238618, 0.00091318, -87.47623862, -9.132e-05, -262.42871585, -0.00027395, -874.76238618, -0.00091318, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.0)
    ops.node(124031, 0.0, 0.0, 3.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 171001, 124031, 0.0625, 30441945.88297385, 12684144.11790577, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 31.19193519, 0.00088734, 37.67287904, 0.02393123, 3.7672879, 0.09008581, -31.19193519, -0.00088734, -37.67287904, -0.02393123, -3.7672879, -0.09008581, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 31.19193519, 0.00088734, 37.67287904, 0.02393123, 3.7672879, 0.09008581, -31.19193519, -0.00088734, -37.67287904, -0.02393123, -3.7672879, -0.09008581, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 96.87143469, 0.01774687, 96.87143469, 0.05324062, 67.81000428, -3778.58119126, 0.05, 2, 0, 71001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 24.21785867, 5.041e-05, 72.65357601, 0.00015122, 242.17858672, 0.00050406, -24.21785867, -5.041e-05, -72.65357601, -0.00015122, -242.17858672, -0.00050406, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 96.87143469, 0.01774687, 96.87143469, 0.05324062, 67.81000428, -3778.58119126, 0.05, 2, 0, 71001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 24.21785867, 5.041e-05, 72.65357601, 0.00015122, 242.17858672, 0.00050406, -24.21785867, -5.041e-05, -72.65357601, -0.00015122, -242.17858672, -0.00050406, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 4.3)
    ops.node(122001, 0.0, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174031, 122001, 0.0625, 30013489.38920699, 12505620.57883625, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 28.29582475, 0.00089747, 34.2624046, 0.02065358, 3.42624046, 0.07789923, -28.29582475, -0.00089747, -34.2624046, -0.02065358, -3.42624046, -0.07789923, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 28.29582475, 0.00089747, 34.2624046, 0.02065358, 3.42624046, 0.07789923, -28.29582475, -0.00089747, -34.2624046, -0.02065358, -3.42624046, -0.07789923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 86.02384236, 0.01794944, 86.02384236, 0.05384831, 60.21668965, -3273.7862574, 0.05, 2, 0, 74031, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 21.50596059, 4.54e-05, 64.51788177, 0.0001362, 215.0596059, 0.000454, -21.50596059, -4.54e-05, -64.51788177, -0.0001362, -215.0596059, -0.000454, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 86.02384236, 0.01794944, 86.02384236, 0.05384831, 60.21668965, -3273.7862574, 0.05, 2, 0, 74031, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 21.50596059, 4.54e-05, 64.51788177, 0.0001362, 215.0596059, 0.000454, -21.50596059, -4.54e-05, -64.51788177, -0.0001362, -215.0596059, -0.000454, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 3.15, 0.0, 3.0)
    ops.node(124032, 3.15, 0.0, 3.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 171002, 124032, 0.12, 33834038.1359603, 14097515.88998346, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 81.21834878, 0.00077402, 97.03518655, 0.03905475, 9.70351866, 0.12123921, -81.21834878, -0.00077402, -97.03518655, -0.03905475, -9.70351866, -0.12123921, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 97.7967641, 0.00067367, 116.84215932, 0.04328776, 11.68421593, 0.14328776, -97.7967641, -0.00067367, -116.84215932, -0.04328776, -11.68421593, -0.14328776, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 256.57583542, 0.01548034, 256.57583542, 0.04644103, 179.60308479, -9843.04363409, 0.05, 2, 0, 71002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 64.14395885, 6.256e-05, 192.43187656, 0.00018769, 641.43958854, 0.00062563, -64.14395885, -6.256e-05, -192.43187656, -0.00018769, -641.43958854, -0.00062563, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 342.10111389, 0.01347332, 342.10111389, 0.04041996, 239.47077972, -15101.49990975, 0.05, 2, 0, 71002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 85.52527847, 8.342e-05, 256.57583542, 0.00025025, 855.25278472, 0.00083417, -85.52527847, -8.342e-05, -256.57583542, -0.00025025, -855.25278472, -0.00083417, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4081, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 3.15, 0.0, 4.3)
    ops.node(122002, 3.15, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4082, 174032, 122002, 0.12, 30796377.9843172, 12831824.16013217, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24082, 76.93833318, 0.00079725, 92.78662107, 0.04237888, 9.27866211, 0.12145731, -76.93833318, -0.00079725, -92.78662107, -0.04237888, -9.27866211, -0.12145731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14082, 92.47403319, 0.00068908, 111.52247159, 0.04697773, 11.15224716, 0.14697773, -92.47403319, -0.00068908, -111.52247159, -0.04697773, -11.15224716, -0.14697773, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24082, 4082, 0.0, 238.95319077, 0.01594503, 238.95319077, 0.04783509, 167.26723354, -10495.68595816, 0.05, 2, 0, 74032, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44082, 59.73829769, 6.401e-05, 179.21489307, 0.00019204, 597.38297691, 0.00064013, -59.73829769, -6.401e-05, -179.21489307, -0.00019204, -597.38297691, -0.00064013, 0.4, 0.3, 0.003, 0.0, 0.0, 24082, 2)
    ops.limitCurve('ThreePoint', 14082, 4082, 0.0, 318.60425435, 0.01378151, 318.60425435, 0.04134454, 223.02297805, -16304.71026043, 0.05, 2, 0, 74032, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34082, 79.65106359, 8.535e-05, 238.95319077, 0.00025605, 796.51063588, 0.0008535, -79.65106359, -8.535e-05, -238.95319077, -0.00025605, -796.51063588, -0.0008535, 0.4, 0.3, 0.003, 0.0, 0.0, 14082, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4082, 99999, 'P', 44082, 'Vy', 34082, 'Vz', 24082, 'My', 14082, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4082, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4082, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.75)
    ops.node(124033, 0.0, 0.0, 6.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4084, 172001, 124033, 0.0625, 31362291.85588434, 13067621.60661848, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24084, 28.93446388, 0.00088774, 34.93365675, 0.02027634, 3.49336567, 0.07973811, -28.93446388, -0.00088774, -34.93365675, -0.02027634, -3.49336567, -0.07973811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14084, 28.93446388, 0.00088774, 34.93365675, 0.02027634, 3.49336567, 0.07973811, -28.93446388, -0.00088774, -34.93365675, -0.02027634, -3.49336567, -0.07973811, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24084, 4084, 0.0, 89.75932713, 0.01775488, 89.75932713, 0.05326465, 62.83152899, -3708.48378541, 0.05, 2, 0, 72001, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44084, 22.43983178, 4.533e-05, 67.31949535, 0.000136, 224.39831783, 0.00045334, -22.43983178, -4.533e-05, -67.31949535, -0.000136, -224.39831783, -0.00045334, 0.4, 0.3, 0.003, 0.0, 0.0, 24084, 2)
    ops.limitCurve('ThreePoint', 14084, 4084, 0.0, 89.75932713, 0.01775488, 89.75932713, 0.05326465, 62.83152899, -3708.48378541, 0.05, 2, 0, 72001, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34084, 22.43983178, 4.533e-05, 67.31949535, 0.000136, 224.39831783, 0.00045334, -22.43983178, -4.533e-05, -67.31949535, -0.000136, -224.39831783, -0.00045334, 0.4, 0.3, 0.003, 0.0, 0.0, 14084, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4084, 99999, 'P', 44084, 'Vy', 34084, 'Vz', 24084, 'My', 14084, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4084, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4084, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 0.0, 0.0, 7.05)
    ops.node(123001, 0.0, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 174033, 123001, 0.0625, 31692084.99597235, 13205035.41498848, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 24.96509566, 0.00085159, 30.1583049, 0.02027276, 3.01583049, 0.08274243, -24.96509566, -0.00085159, -30.1583049, -0.02027276, -3.01583049, -0.08274243, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 24.96509566, 0.00085159, 30.1583049, 0.02027276, 3.01583049, 0.08274243, -24.96509566, -0.00085159, -30.1583049, -0.02027276, -3.01583049, -0.08274243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 85.93100213, 0.01703175, 85.93100213, 0.05109526, 60.15170149, -4638.11186103, 0.05, 2, 0, 74033, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 21.48275053, 4.295e-05, 64.44825159, 0.00012885, 214.82750531, 0.00042949, -21.48275053, -4.295e-05, -64.44825159, -0.00012885, -214.82750531, -0.00042949, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 85.93100213, 0.01703175, 85.93100213, 0.05109526, 60.15170149, -4638.11186103, 0.05, 2, 0, 74033, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 21.48275053, 4.295e-05, 64.44825159, 0.00012885, 214.82750531, 0.00042949, -21.48275053, -4.295e-05, -64.44825159, -0.00012885, -214.82750531, -0.00042949, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 3.15, 0.0, 5.75)
    ops.node(124034, 3.15, 0.0, 6.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 172002, 124034, 0.0875, 32980557.88211738, 13741899.11754891, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 47.63390303, 0.00089283, 57.10888992, 0.02858196, 5.71088899, 0.09433137, -47.63390303, -0.00089283, -57.10888992, -0.02858196, -5.71088899, -0.09433137, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 63.67387004, 0.00072628, 76.33940962, 0.03197358, 7.63394096, 0.11955957, -63.67387004, -0.00072628, -76.33940962, -0.03197358, -7.63394096, -0.11955957, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 140.78005086, 0.01785663, 140.78005086, 0.05356989, 98.5460356, -4728.00047695, 0.05, 2, 0, 72002, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 35.19501271, 4.83e-05, 105.58503814, 0.00014489, 351.95012714, 0.00048296, -35.19501271, -4.83e-05, -105.58503814, -0.00014489, -351.95012714, -0.00048296, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 197.0920712, 0.01452555, 197.0920712, 0.04357666, 137.96444984, -7612.03725057, 0.05, 2, 0, 72002, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 49.2730178, 6.761e-05, 147.8190534, 0.00020284, 492.730178, 0.00067614, -49.2730178, -6.761e-05, -147.8190534, -0.00020284, -492.730178, -0.00067614, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 3.15, 0.0, 7.05)
    ops.node(123002, 3.15, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 174034, 123002, 0.0875, 31767458.65881805, 13236441.10784085, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 53.66384662, 0.00090747, 64.63767786, 0.02856044, 6.46376779, 0.09504412, -53.66384662, -0.00090747, -64.63767786, -0.02856044, -6.46376779, -0.09504412, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 67.641244, 0.00073356, 81.47334219, 0.03194005, 8.14733422, 0.12050417, -67.641244, -0.00073356, -81.47334219, -0.03194005, -8.14733422, -0.12050417, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 129.70169675, 0.01814948, 129.70169675, 0.05444845, 90.79118773, -4576.76320062, 0.05, 2, 0, 74034, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 32.42542419, 4.619e-05, 97.27627256, 0.00013858, 324.25424188, 0.00046195, -32.42542419, -4.619e-05, -97.27627256, -0.00013858, -324.25424188, -0.00046195, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 181.58237545, 0.01467115, 181.58237545, 0.04401344, 127.10766282, -7489.23255582, 0.05, 2, 0, 74034, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 45.39559386, 6.467e-05, 136.18678159, 0.00019402, 453.95593863, 0.00064672, -45.39559386, -6.467e-05, -136.18678159, -0.00019402, -453.95593863, -0.00064672, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.5)
    ops.node(124035, 0.0, 0.0, 9.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4089, 173001, 124035, 0.0625, 29484751.74447232, 12285313.22686347, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24089, 25.98303127, 0.00085992, 31.60733186, 0.02223065, 3.16073319, 0.08498701, -25.98303127, -0.00085992, -31.60733186, -0.02223065, -3.16073319, -0.08498701, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14089, 25.98303127, 0.00085992, 31.60733186, 0.02223065, 3.16073319, 0.08498701, -25.98303127, -0.00085992, -31.60733186, -0.02223065, -3.16073319, -0.08498701, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24089, 4089, 0.0, 83.92810802, 0.01719845, 83.92810802, 0.05159534, 58.74967561, -6818.51752027, 0.05, 2, 0, 73001, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44089, 20.982027, 4.509e-05, 62.94608101, 0.00013527, 209.82027004, 0.00045088, -20.982027, -4.509e-05, -62.94608101, -0.00013527, -209.82027004, -0.00045088, 0.4, 0.3, 0.003, 0.0, 0.0, 24089, 2)
    ops.limitCurve('ThreePoint', 14089, 4089, 0.0, 83.92810802, 0.01719845, 83.92810802, 0.05159534, 58.74967561, -6818.51752027, 0.05, 2, 0, 73001, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34089, 20.982027, 4.509e-05, 62.94608101, 0.00013527, 209.82027004, 0.00045088, -20.982027, -4.509e-05, -62.94608101, -0.00013527, -209.82027004, -0.00045088, 0.4, 0.3, 0.003, 0.0, 0.0, 14089, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4089, 99999, 'P', 44089, 'Vy', 34089, 'Vz', 24089, 'My', 14089, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4089, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4089, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 0.0, 0.0, 9.8)
    ops.node(124001, 0.0, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 174035, 124001, 0.0625, 31607616.96291844, 13169840.40121602, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 20.25755567, 0.00088414, 24.53071936, 0.02138741, 2.45307194, 0.0879614, -20.25755567, -0.00088414, -24.53071936, -0.02138741, -2.45307194, -0.0879614, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 20.25755567, 0.00088414, 24.53071936, 0.02138741, 2.45307194, 0.0879614, -20.25755567, -0.00088414, -24.53071936, -0.02138741, -2.45307194, -0.0879614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 82.38245152, 0.0176828, 82.38245152, 0.0530484, 57.66771606, -43187.35689004, 0.05, 2, 0, 74035, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 20.59561288, 4.129e-05, 61.78683864, 0.00012386, 205.9561288, 0.00041286, -20.59561288, -4.129e-05, -61.78683864, -0.00012386, -205.9561288, -0.00041286, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 82.38245152, 0.0176828, 82.38245152, 0.0530484, 57.66771606, -43187.35689004, 0.05, 2, 0, 74035, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 20.59561288, 4.129e-05, 61.78683864, 0.00012386, 205.9561288, 0.00041286, -20.59561288, -4.129e-05, -61.78683864, -0.00012386, -205.9561288, -0.00041286, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 3.15, 0.0, 8.5)
    ops.node(124036, 3.15, 0.0, 9.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 173002, 124036, 0.0875, 31122678.4260865, 12967782.67753604, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 35.40546477, 0.00088239, 42.85031153, 0.02072919, 4.28503115, 0.07785066, -35.40546477, -0.00088239, -42.85031153, -0.02072919, -4.28503115, -0.07785066, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 57.11825273, 0.00072169, 69.12873309, 0.02297885, 6.91287331, 0.09794769, -57.11825273, -0.00072169, -69.12873309, -0.02297885, -6.91287331, -0.09794769, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 103.82941794, 0.01764787, 103.82941794, 0.0529436, 72.68059256, -4115.02870849, 0.05, 2, 0, 73002, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 25.95735449, 3.775e-05, 77.87206346, 0.00011324, 259.57354485, 0.00037746, -25.95735449, -3.775e-05, -77.87206346, -0.00011324, -259.57354485, -0.00037746, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 145.36118512, 0.01443371, 145.36118512, 0.04330112, 101.75282958, -7126.75510953, 0.05, 2, 0, 73002, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 36.34029628, 5.284e-05, 109.02088884, 0.00015853, 363.40296279, 0.00052844, -36.34029628, -5.284e-05, -109.02088884, -0.00015853, -363.40296279, -0.00052844, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 3.15, 0.0, 9.8)
    ops.node(124002, 3.15, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 174036, 124002, 0.0875, 31398933.49469465, 13082888.95612277, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 31.9027318, 0.00082419, 38.62265748, 0.02185733, 3.86226575, 0.0810534, -31.9027318, -0.00082419, -38.62265748, -0.02185733, -3.86226575, -0.0810534, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 51.94416035, 0.00068354, 62.88557125, 0.02427112, 6.28855712, 0.10196277, -51.94416035, -0.00068354, -62.88557125, -0.02427112, -6.28855712, -0.10196277, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 105.79415139, 0.01648384, 105.79415139, 0.04945152, 74.05590597, -7838.49946657, 0.05, 2, 0, 74036, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 26.44853785, 3.812e-05, 79.34561354, 0.00011437, 264.48537847, 0.00038122, -26.44853785, -3.812e-05, -79.34561354, -0.00011437, -264.48537847, -0.00038122, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 148.11181194, 0.01367086, 148.11181194, 0.04101257, 103.67826836, -14434.1793291, 0.05, 2, 0, 74036, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 37.02795299, 5.337e-05, 111.08385896, 0.00016011, 370.27952986, 0.00053371, -37.02795299, -5.337e-05, -111.08385896, -0.00016011, -370.27952986, -0.00053371, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4092, '-orient', 0, 0, 1, 0, 1, 0)
