import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1, 24563224.2069678, 10234676.75290325, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 87.10116285, 0.0014988, 105.86298527, 0.02141362, 10.58629853, 0.05193023, -87.10116285, -0.0014988, -105.86298527, -0.02141362, -10.58629853, -0.05193023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 123.01814652, 0.00099196, 149.51658286, 0.02412014, 14.95165829, 0.06763522, -123.01814652, -0.00099196, -149.51658286, -0.02412014, -14.95165829, -0.06763522, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 82.77223106, 0.0299761, 82.77223106, 0.0899283, 57.94056174, -1140.25167665, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 20.69305776, 6.672e-05, 62.07917329, 0.00020016, 206.93057765, 0.00066721, -20.69305776, -6.672e-05, -62.07917329, -0.00020016, -206.93057765, -0.00066721, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 106.80918817, 0.01983921, 106.80918817, 0.05951763, 74.76643172, -1914.76514083, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 26.70229704, 8.61e-05, 80.10689113, 0.00025829, 267.02297044, 0.00086097, -26.70229704, -8.61e-05, -80.10689113, -0.00025829, -267.02297044, -0.00086097, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 14.65, 0.0, 0.0)
    ops.node(121004, 14.65, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.1, 27810128.47716095, 11587553.5321504, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 83.58218274, 0.00145117, 101.3745839, 0.02559851, 10.13745839, 0.06091144, -83.58218274, -0.00145117, -101.3745839, -0.02559851, -10.13745839, -0.06091144, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 121.10064324, 0.00094769, 146.87971667, 0.02899134, 14.68797167, 0.07934571, -121.10064324, -0.00094769, -146.87971667, -0.02899134, -14.68797167, -0.07934571, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 103.7276292, 0.02902339, 103.7276292, 0.08707018, 72.60934044, -1421.77208213, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 25.9319073, 7.385e-05, 77.7957219, 0.00022155, 259.31907301, 0.00073851, -25.9319073, -7.385e-05, -77.7957219, -0.00022155, -259.31907301, -0.00073851, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 128.6983986, 0.01895376, 128.6983986, 0.05686128, 90.08887902, -2506.01139922, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 32.17459965, 9.163e-05, 96.52379895, 0.00027489, 321.7459965, 0.0009163, -32.17459965, -9.163e-05, -96.52379895, -0.00027489, -321.7459965, -0.0009163, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.15, 0.0)
    ops.node(121005, 0.0, 4.15, 2.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.22, 27334274.68746622, 11389281.11977759, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 303.01232512, 0.00075908, 368.62007986, 0.03577536, 36.86200799, 0.09075608, -303.01232512, -0.00075908, -368.62007986, -0.03577536, -36.86200799, -0.09075608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 296.28320759, 0.00092761, 360.43398432, 0.03247278, 36.04339843, 0.07539346, -296.28320759, -0.00092761, -360.43398432, -0.03247278, -36.04339843, -0.07539346, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 288.20710024, 0.01518152, 288.20710024, 0.04554457, 201.74497017, -4968.41230631, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 72.05177506, 9.489e-05, 216.15532518, 0.00028468, 720.51775059, 0.00094894, -72.05177506, -9.489e-05, -216.15532518, -0.00028468, -720.51775059, -0.00094894, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 218.33683602, 0.01855211, 218.33683602, 0.05565633, 152.83578521, -3283.84377919, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 54.584209, 7.189e-05, 163.75262701, 0.00021567, 545.84209004, 0.00071889, -54.584209, -7.189e-05, -163.75262701, -0.00021567, -545.84209004, -0.00071889, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 5.9, 4.15, 0.0)
    ops.node(121006, 5.9, 4.15, 2.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.24, 27271838.44193284, 11363266.01747202, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 393.758182, 0.00073561, 478.60168596, 0.0378271, 47.8601686, 0.0911788, -393.758182, -0.00073561, -478.60168596, -0.0378271, -47.8601686, -0.0911788, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 362.8657632, 0.00094454, 441.05284406, 0.03346607, 44.10528441, 0.07252264, -362.8657632, -0.00094454, -441.05284406, -0.03346607, -44.10528441, -0.07252264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 351.82090171, 0.01471213, 351.82090171, 0.0441364, 246.2746312, -6122.1572939, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 87.95522543, 0.00010643, 263.86567628, 0.00031929, 879.55225428, 0.00106429, -87.95522543, -0.00010643, -263.86567628, -0.00031929, -879.55225428, -0.00106429, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 244.25933778, 0.01889076, 244.25933778, 0.05667227, 170.98153644, -3640.14686592, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 61.06483444, 7.389e-05, 183.19450333, 0.00022167, 610.64834445, 0.00073891, -61.06483444, -7.389e-05, -183.19450333, -0.00022167, -610.64834445, -0.00073891, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.75, 4.15, 0.0)
    ops.node(121007, 8.75, 4.15, 2.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.24, 26885105.66811134, 11202127.36171306, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 391.78691653, 0.00075479, 476.4306887, 0.0391219, 47.64306887, 0.09180222, -391.78691653, -0.00075479, -476.4306887, -0.0391219, -47.64306887, -0.09180222, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 353.60743894, 0.0009836, 430.00270952, 0.03462359, 43.00027095, 0.07318867, -353.60743894, -0.0009836, -430.00270952, -0.03462359, -43.00027095, -0.07318867, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 353.71796448, 0.01509586, 353.71796448, 0.04528757, 247.60257513, -6427.80955357, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 88.42949112, 0.00010854, 265.28847336, 0.00032563, 884.29491119, 0.00108542, -88.42949112, -0.00010854, -265.28847336, -0.00032563, -884.29491119, -0.00108542, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 245.34157212, 0.01967208, 245.34157212, 0.05901625, 171.73910048, -3797.01208018, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 61.33539303, 7.529e-05, 184.00617909, 0.00022586, 613.35393029, 0.00075286, -61.33539303, -7.529e-05, -184.00617909, -0.00022586, -613.35393029, -0.00075286, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 14.65, 4.15, 0.0)
    ops.node(121008, 14.65, 4.15, 2.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.22, 26269377.68789311, 10945574.03662213, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 304.01447879, 0.00078419, 370.32826192, 0.03812842, 37.03282619, 0.09134966, -304.01447879, -0.00078419, -370.32826192, -0.03812842, -37.03282619, -0.09134966, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 296.24320033, 0.00096515, 360.86185738, 0.03460751, 36.08618574, 0.07615465, -296.24320033, -0.00096515, -360.86185738, -0.03460751, -36.08618574, -0.07615465, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 301.28060363, 0.01568374, 301.28060363, 0.04705122, 210.89642254, -6195.06427373, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 75.32015091, 0.00010322, 225.96045272, 0.00030966, 753.20150907, 0.0010322, -75.32015091, -0.00010322, -225.96045272, -0.00030966, -753.20150907, -0.0010322, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 227.389575, 0.01930293, 227.389575, 0.05790879, 159.1727025, -4004.90232309, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 56.84739375, 7.79e-05, 170.54218125, 0.00023371, 568.47393749, 0.00077905, -56.84739375, -7.79e-05, -170.54218125, -0.00023371, -568.47393749, -0.00077905, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.3, 0.0)
    ops.node(121009, 0.0, 8.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.12, 28110010.77032863, 11712504.48763693, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 78.9799681, 0.00116712, 95.89697032, 0.02072972, 9.58969703, 0.05803121, -78.9799681, -0.00116712, -95.89697032, -0.02072972, -9.58969703, -0.05803121, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 102.56907805, 0.00092185, 124.53871621, 0.02231425, 12.45387162, 0.06842918, -102.56907805, -0.00092185, -124.53871621, -0.02231425, -12.45387162, -0.06842918, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 114.51678262, 0.02334238, 114.51678262, 0.07002714, 80.16174783, -1421.50402392, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 28.62919565, 6.722e-05, 85.88758696, 0.00020166, 286.29195654, 0.00067219, -28.62919565, -6.722e-05, -85.88758696, -0.00020166, -286.29195654, -0.00067219, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 128.39214464, 0.01843703, 128.39214464, 0.05531108, 89.87450125, -1984.89910781, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 32.09803616, 7.536e-05, 96.29410848, 0.00022609, 320.98036161, 0.00075364, -32.09803616, -7.536e-05, -96.29410848, -0.00022609, -320.98036161, -0.00075364, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 5.9, 8.3, 0.0)
    ops.node(121010, 5.9, 8.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.135, 26746085.64158459, 11144202.35066025, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 104.93713251, 0.00115956, 127.47619865, 0.02148773, 12.74761987, 0.05853038, -104.93713251, -0.00115956, -127.47619865, -0.02148773, -12.74761987, -0.05853038, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 131.61224351, 0.00084744, 159.88076001, 0.02403214, 15.988076, 0.07463281, -131.61224351, -0.00084744, -159.88076001, -0.02403214, -15.988076, -0.07463281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 135.1877499, 0.02319122, 135.1877499, 0.06957366, 94.63142493, -1924.39523063, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 33.79693748, 7.413e-05, 101.39081243, 0.0002224, 337.96937476, 0.00074132, -33.79693748, -7.413e-05, -101.39081243, -0.0002224, -337.96937476, -0.00074132, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 166.98936111, 0.01694875, 166.98936111, 0.05084626, 116.89255278, -3140.2865695, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 41.74734028, 9.157e-05, 125.24202084, 0.00027471, 417.47340278, 0.00091571, -41.74734028, -9.157e-05, -125.24202084, -0.00027471, -417.47340278, -0.00091571, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.75, 8.3, 0.0)
    ops.node(121011, 8.75, 8.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.135, 26590806.84649917, 11079502.85270799, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 109.17806923, 0.00117548, 132.64687652, 0.02223002, 13.26468765, 0.05904638, -109.17806923, -0.00117548, -132.64687652, -0.02223002, -13.26468765, -0.05904638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 135.24897983, 0.00086336, 164.32196368, 0.02487651, 16.43219637, 0.07516807, -135.24897983, -0.00086336, -164.32196368, -0.02487651, -16.43219637, -0.07516807, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 140.21046747, 0.02350953, 140.21046747, 0.07052858, 98.14732723, -2144.08627694, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 35.05261687, 7.734e-05, 105.1578506, 0.00023201, 350.52616866, 0.00077336, -35.05261687, -7.734e-05, -105.1578506, -0.00023201, -350.52616866, -0.00077336, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 174.79299216, 0.01726721, 174.79299216, 0.05180163, 122.35509451, -3563.22853748, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 43.69824804, 9.641e-05, 131.09474412, 0.00028923, 436.98248039, 0.0009641, -43.69824804, -9.641e-05, -131.09474412, -0.00028923, -436.98248039, -0.0009641, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 14.65, 8.3, 0.0)
    ops.node(121012, 14.65, 8.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.12, 28118265.11555659, 11715943.79814858, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 77.74578557, 0.00109129, 94.39717308, 0.0230896, 9.43971731, 0.06039948, -77.74578557, -0.00109129, -94.39717308, -0.0230896, -9.43971731, -0.06039948, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 100.41345831, 0.0008716, 121.91974824, 0.02492753, 12.19197482, 0.07105284, -100.41345831, -0.0008716, -121.91974824, -0.02492753, -12.19197482, -0.07105284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 123.03446455, 0.02182581, 123.03446455, 0.06547743, 86.12412518, -1755.04514424, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 30.75861614, 7.22e-05, 92.27584841, 0.00021659, 307.58616136, 0.00072198, -30.75861614, -7.22e-05, -92.27584841, -0.00021659, -307.58616136, -0.00072198, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 139.73945994, 0.01743195, 139.73945994, 0.05229586, 97.81762196, -2513.96283326, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 34.93486499, 8.2e-05, 104.80459496, 0.000246, 349.34864985, 0.00082, -34.93486499, -8.2e-05, -104.80459496, -0.000246, -349.34864985, -0.00082, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.05)
    ops.node(122001, 0.0, 0.0, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1, 27724003.17264619, 11551667.98860258, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 98.87414755, 0.00143033, 120.26296494, 0.03904327, 12.02629649, 0.09531662, -98.87414755, -0.00143033, -120.26296494, -0.03904327, -12.02629649, -0.09531662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 132.66097767, 0.00094741, 161.35868579, 0.04539191, 16.13586858, 0.12899719, -132.66097767, -0.00094741, -161.35868579, -0.04539191, -16.13586858, -0.12899719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 121.11876141, 0.02860667, 121.11876141, 0.08582002, 84.78313299, -2642.64936211, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 30.27969035, 8.65e-05, 90.83907106, 0.0002595, 302.79690353, 0.00086501, -30.27969035, -8.65e-05, -90.83907106, -0.0002595, -302.79690353, -0.00086501, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 159.03175451, 0.01894827, 159.03175451, 0.0568448, 111.32222816, -5409.93431036, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 39.75793863, 0.00011358, 119.27381588, 0.00034073, 397.57938628, 0.00113578, -39.75793863, -0.00011358, -119.27381588, -0.00034073, -397.57938628, -0.00113578, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 14.65, 0.0, 3.05)
    ops.node(122004, 14.65, 0.0, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.1, 25831942.59450376, 10763309.41437657, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 95.33562489, 0.00164914, 116.24223173, 0.03917948, 11.62422317, 0.09244979, -95.33562489, -0.00164914, -116.24223173, -0.03917948, -11.62422317, -0.09244979, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 132.07396376, 0.00104431, 161.03709729, 0.0453912, 16.10370973, 0.12453487, -132.07396376, -0.00104431, -161.03709729, -0.0453912, -16.10370973, -0.12453487, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 113.82897191, 0.03298287, 113.82897191, 0.09894861, 79.68028034, -2524.79814119, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 28.45724298, 8.725e-05, 85.37172893, 0.00026175, 284.57242978, 0.00087249, -28.45724298, -8.725e-05, -85.37172893, -0.00026175, -284.57242978, -0.00087249, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 150.55110108, 0.02088611, 150.55110108, 0.06265834, 105.38577076, -5140.50543207, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 37.63777527, 0.0001154, 112.91332581, 0.00034619, 376.3777527, 0.00115396, -37.63777527, -0.0001154, -112.91332581, -0.00034619, -376.3777527, -0.00115396, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.15, 3.025)
    ops.node(122005, 0.0, 4.15, 5.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.22, 27659086.01206975, 11524619.17169573, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 230.15907101, 0.00070688, 280.43274098, 0.03839751, 28.0432741, 0.09736993, -230.15907101, -0.00070688, -280.43274098, -0.03839751, -28.0432741, -0.09736993, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 138.1637598, 0.00085173, 168.3428843, 0.03480615, 16.83428843, 0.08084295, -138.1637598, -0.00085173, -168.3428843, -0.03480615, -16.83428843, -0.08084295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 311.73071217, 0.0141375, 311.73071217, 0.0424125, 218.21149852, -7919.50991075, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 77.93267804, 0.00010143, 233.79803413, 0.0003043, 779.32678042, 0.00101434, -77.93267804, -0.00010143, -233.79803413, -0.0003043, -779.32678042, -0.00101434, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 235.11772242, 0.01703462, 235.11772242, 0.05110387, 164.58240569, -4880.03840585, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 58.77943061, 7.651e-05, 176.33829182, 0.00022952, 587.79430605, 0.00076505, -58.77943061, -7.651e-05, -176.33829182, -0.00022952, -587.79430605, -0.00076505, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 5.9, 4.15, 3.025)
    ops.node(122006, 5.9, 4.15, 5.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.24, 26153874.46889042, 10897447.69537101, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 275.00553613, 0.00072734, 335.54687137, 0.01639688, 33.55468714, 0.04962981, -275.00553613, -0.00072734, -335.54687137, -0.01639688, -33.55468714, -0.04962981, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 151.66751272, 0.00092737, 185.05649049, 0.01502626, 18.50564905, 0.04089395, -151.66751272, -0.00092737, -185.05649049, -0.01502626, -18.50564905, -0.04089395, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 242.67142816, 0.01454688, 242.67142816, 0.04364064, 169.86999971, -2324.08191433, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 60.66785704, 7.655e-05, 182.00357112, 0.00022965, 606.67857041, 0.00076548, -60.66785704, -7.655e-05, -182.00357112, -0.00022965, -606.67857041, -0.00076548, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 170.44776146, 0.01854739, 170.44776146, 0.05564218, 119.31343302, -1533.1832192, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 42.61194037, 5.377e-05, 127.8358211, 0.0001613, 426.11940365, 0.00053766, -42.61194037, -5.377e-05, -127.8358211, -0.0001613, -426.11940365, -0.00053766, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.75, 4.15, 3.025)
    ops.node(122007, 8.75, 4.15, 5.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.24, 28943108.3151231, 12059628.46463462, 0.00751249, 0.00352, 0.00792, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 264.0218184, 0.00067931, 320.65786016, 0.01953457, 32.06578602, 0.05493292, -264.0218184, -0.00067931, -320.65786016, -0.01953457, -32.06578602, -0.05493292, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 146.58208494, 0.00085806, 178.02580855, 0.01782334, 17.80258086, 0.04537655, -146.58208494, -0.00085806, -178.02580855, -0.01782334, -17.80258086, -0.04537655, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 285.3581181, 0.01358621, 285.3581181, 0.04075862, 199.75068267, -2992.80782772, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 71.33952953, 8.134e-05, 214.01858858, 0.00024402, 713.39529525, 0.00081339, -71.33952953, -8.134e-05, -214.01858858, -0.00024402, -713.39529525, -0.00081339, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 200.21845497, 0.0171612, 200.21845497, 0.05148359, 140.15291848, -1891.18606524, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 50.05461374, 5.707e-05, 150.16384123, 0.00017121, 500.54613743, 0.00057071, -50.05461374, -5.707e-05, -150.16384123, -0.00017121, -500.54613743, -0.00057071, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 14.65, 4.15, 3.025)
    ops.node(122008, 14.65, 4.15, 5.225)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.22, 29403977.48437407, 12251657.28515586, 0.00648267, 0.00322667, 0.00610042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 235.48750997, 0.00072207, 285.8974178, 0.03671659, 28.58974178, 0.09745061, -235.48750997, -0.00072207, -285.8974178, -0.03671659, -28.58974178, -0.09745061, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 141.81564124, 0.00087562, 172.17357149, 0.03330205, 17.21735715, 0.08071405, -141.81564124, -0.00087562, -172.17357149, -0.03330205, -17.21735715, -0.08071405, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 315.08258197, 0.01444143, 315.08258197, 0.04332428, 220.55780738, -7075.05716472, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 78.77064549, 9.644e-05, 236.31193648, 0.00028932, 787.70645493, 0.00096441, -78.77064549, -9.644e-05, -236.31193648, -0.00028932, -787.70645493, -0.00096441, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 238.32195629, 0.01751232, 238.32195629, 0.05253695, 166.8253694, -4396.9417607, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 59.58048907, 7.295e-05, 178.74146722, 0.00021884, 595.80489072, 0.00072946, -59.58048907, -7.295e-05, -178.74146722, -0.00021884, -595.80489072, -0.00072946, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.3, 3.05)
    ops.node(122009, 0.0, 8.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.12, 27578734.12184899, 11491139.21743708, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 109.30484452, 0.00121433, 133.13471923, 0.03984169, 13.31347192, 0.09787655, -109.30484452, -0.00121433, -133.13471923, -0.03984169, -13.31347192, -0.09787655, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 124.6905947, 0.00095435, 151.87476263, 0.04366784, 15.18747626, 0.11733577, -124.6905947, -0.00095435, -151.87476263, -0.04366784, -15.18747626, -0.11733577, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 153.53696054, 0.02428658, 153.53696054, 0.07285974, 107.47587238, -4226.61197849, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 38.38424014, 9.186e-05, 115.15272041, 0.00027558, 383.84240135, 0.00091859, -38.38424014, -9.186e-05, -115.15272041, -0.00027558, -383.84240135, -0.00091859, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 182.3956525, 0.01908691, 182.3956525, 0.05726072, 127.67695675, -6698.32073583, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 45.59891313, 0.00010912, 136.79673938, 0.00032737, 455.98913126, 0.00109125, -45.59891313, -0.00010912, -136.79673938, -0.00032737, -455.98913126, -0.00109125, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 5.9, 8.3, 3.05)
    ops.node(122010, 5.9, 8.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.135, 29347858.64705681, 12228274.43627367, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 110.09400265, 0.00110046, 133.52460606, 0.02993211, 13.35246061, 0.08331733, -110.09400265, -0.00110046, -133.52460606, -0.02993211, -13.35246061, -0.08331733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 132.8351841, 0.0008103, 161.1056479, 0.03397716, 16.11056479, 0.10840354, -132.8351841, -0.0008103, -161.1056479, -0.03397716, -16.11056479, -0.10840354, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 160.07387366, 0.02200923, 160.07387366, 0.06602768, 112.05171156, -3065.35371209, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 40.01846841, 8e-05, 120.05540524, 0.00023999, 400.18468415, 0.00079997, -40.01846841, -8e-05, -120.05540524, -0.00023999, -400.18468415, -0.00079997, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 202.01632278, 0.01620605, 202.01632278, 0.04861815, 141.41142594, -5589.10156948, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 50.50408069, 0.00010096, 151.51224208, 0.00030287, 505.04080694, 0.00100958, -50.50408069, -0.00010096, -151.51224208, -0.00030287, -505.04080694, -0.00100958, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.75, 8.3, 3.05)
    ops.node(122011, 8.75, 8.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.135, 25367381.45314012, 10569742.27214172, 0.002377, 0.00250594, 0.00111375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 103.65094559, 0.001095, 126.46867835, 0.02912789, 12.64686784, 0.07726736, -103.65094559, -0.001095, -126.46867835, -0.02912789, -12.64686784, -0.07726736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 124.28438833, 0.00080545, 151.64436989, 0.03305344, 15.16443699, 0.10016652, -124.28438833, -0.00080545, -151.64436989, -0.03305344, -15.16443699, -0.10016652, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 139.79100478, 0.02190002, 139.79100478, 0.06570005, 97.85370334, -2786.79188175, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 34.94775119, 8.082e-05, 104.84325358, 0.00024247, 349.47751195, 0.00080823, -34.94775119, -8.082e-05, -104.84325358, -0.00024247, -349.47751195, -0.00080823, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 178.49214832, 0.01610897, 178.49214832, 0.04832691, 124.94450382, -5026.37748841, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 44.62303708, 0.0001032, 133.86911124, 0.0003096, 446.23037079, 0.00103199, -44.62303708, -0.0001032, -133.86911124, -0.0003096, -446.23037079, -0.00103199, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 14.65, 8.3, 3.05)
    ops.node(122012, 14.65, 8.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.12, 27624437.34542678, 11510182.22726116, 0.00194385, 0.00176, 0.00099, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 108.4121504, 0.0011572, 132.03704737, 0.0357499, 13.20370474, 0.09384088, -108.4121504, -0.0011572, -132.03704737, -0.0357499, -13.20370474, -0.09384088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 122.6693602, 0.00091711, 149.40115164, 0.03916915, 14.94011516, 0.11290832, -122.6693602, -0.00091711, -149.40115164, -0.03916915, -14.94011516, -0.11290832, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 134.26024662, 0.023144, 134.26024662, 0.06943201, 93.98217263, -2881.44891127, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 33.56506165, 8.019e-05, 100.69518496, 0.00024058, 335.65061654, 0.00080193, -33.56506165, -8.019e-05, -100.69518496, -0.00024058, -335.65061654, -0.00080193, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 156.64148933, 0.01834223, 156.64148933, 0.0550267, 109.64904253, -4453.1923087, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 39.16037233, 9.356e-05, 117.481117, 0.00028068, 391.60372332, 0.00093562, -39.16037233, -9.356e-05, -117.481117, -0.00028068, -391.60372332, -0.00093562, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.8)
    ops.node(123001, 0.0, 0.0, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0875, 25208998.17220958, 10503749.23842066, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 61.04158158, 0.00151385, 74.68405489, 0.02579106, 7.46840549, 0.06827408, -61.04158158, -0.00151385, -74.68405489, -0.02579106, -7.46840549, -0.06827408, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 80.61328409, 0.00110229, 98.62993026, 0.02817455, 9.86299303, 0.08318893, -80.61328409, -0.00110229, -98.62993026, -0.02817455, -9.86299303, -0.08318893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 82.15506478, 0.03027696, 82.15506478, 0.09083088, 57.50854534, -1728.79786518, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 20.53876619, 7.375e-05, 61.61629858, 0.00022124, 205.38766194, 0.00073746, -20.53876619, -7.375e-05, -61.61629858, -0.00022124, -205.38766194, -0.00073746, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 98.30379915, 0.02204584, 98.30379915, 0.06613752, 68.8126594, -2883.27367639, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 24.57594979, 8.824e-05, 73.72784936, 0.00026472, 245.75949787, 0.00088241, -24.57594979, -8.824e-05, -73.72784936, -0.00026472, -245.75949787, -0.00088241, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 14.65, 0.0, 5.8)
    ops.node(123004, 14.65, 0.0, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0875, 27304250.14761152, 11376770.89483813, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 57.5157996, 0.00141411, 70.16026268, 0.02795979, 7.01602627, 0.0724365, -57.5157996, -0.00141411, -70.16026268, -0.02795979, -7.01602627, -0.0724365, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 76.71973152, 0.00102677, 93.58605034, 0.03062867, 9.35860503, 0.08822482, -76.71973152, -0.00102677, -93.58605034, -0.03062867, -9.35860503, -0.08822482, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 91.72980086, 0.02828228, 91.72980086, 0.08484683, 64.2108606, -2024.85879916, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 22.93245022, 7.602e-05, 68.79735065, 0.00022806, 229.32450215, 0.00076022, -22.93245022, -7.602e-05, -68.79735065, -0.00022806, -229.32450215, -0.00076022, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 109.70146383, 0.02053548, 109.70146383, 0.06160643, 76.79102468, -3420.32981265, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 27.42536596, 9.092e-05, 82.27609788, 0.00027275, 274.25365958, 0.00090916, -27.42536596, -9.092e-05, -82.27609788, -0.00027275, -274.25365958, -0.00090916, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.15, 5.775)
    ops.node(123005, 0.0, 4.15, 7.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.175, 25529056.92288116, 10637107.05120048, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 142.14728032, 0.00076748, 174.0085204, 0.02455404, 17.40085204, 0.06854091, -142.14728032, -0.00076748, -174.0085204, -0.02455404, -17.40085204, -0.06854091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 86.54007086, 0.00098949, 105.93737462, 0.02240908, 10.59373746, 0.05671308, -86.54007086, -0.00098949, -105.93737462, -0.02240908, -10.59373746, -0.05671308, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 174.66581578, 0.01534965, 174.66581578, 0.04604896, 122.26607104, -3525.07688897, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 43.66645394, 7.741e-05, 130.99936183, 0.00023223, 436.66453944, 0.00077411, -43.66645394, -7.741e-05, -130.99936183, -0.00023223, -436.66453944, -0.00077411, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 137.69684114, 0.01978977, 137.69684114, 0.05936931, 96.3877888, -2115.63109346, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 34.42421028, 6.103e-05, 103.27263085, 0.00018308, 344.24210284, 0.00061026, -34.42421028, -6.103e-05, -103.27263085, -0.00018308, -344.24210284, -0.00061026, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 5.9, 4.15, 5.775)
    ops.node(123006, 5.9, 4.15, 7.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.175, 25777876.2481099, 10740781.77004579, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 156.44915992, 0.00078944, 191.14509047, 0.02005437, 19.11450905, 0.0570451, -156.44915992, -0.00078944, -191.14509047, -0.02005437, -19.11450905, -0.0570451, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 95.70539047, 0.0010152, 116.93009747, 0.01847146, 11.69300975, 0.04774861, -95.70539047, -0.0010152, -116.93009747, -0.01847146, -11.69300975, -0.04774861, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 169.58891215, 0.0157887, 169.58891215, 0.04736611, 118.71223851, -2570.02866482, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 42.39722804, 7.444e-05, 127.19168412, 0.00022331, 423.97228038, 0.00074435, -42.39722804, -7.444e-05, -127.19168412, -0.00022331, -423.97228038, -0.00074435, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 134.99365382, 0.02030396, 134.99365382, 0.06091189, 94.49555767, -1644.6752481, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 33.74841345, 5.925e-05, 101.24524036, 0.00017775, 337.48413455, 0.00059251, -33.74841345, -5.925e-05, -101.24524036, -0.00017775, -337.48413455, -0.00059251, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.75, 4.15, 5.775)
    ops.node(123007, 8.75, 4.15, 7.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.175, 28011290.64789016, 11671371.10328757, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 157.08614191, 0.00078078, 191.26275438, 0.01968247, 19.12627544, 0.05854559, -157.08614191, -0.00078078, -191.26275438, -0.01968247, -19.12627544, -0.05854559, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 96.33729617, 0.00100693, 117.29702182, 0.01813405, 11.72970218, 0.04889315, -96.33729617, -0.00100693, -117.29702182, -0.01813405, -11.72970218, -0.04889315, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 182.10651444, 0.01561566, 182.10651444, 0.04684699, 127.47456011, -2562.14277894, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 45.52662861, 7.356e-05, 136.57988583, 0.00022067, 455.2662861, 0.00073556, -45.52662861, -7.356e-05, -136.57988583, -0.00022067, -455.2662861, -0.00073556, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 145.77571466, 0.02013861, 145.77571466, 0.06041584, 102.04300026, -1640.25892015, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 36.44392867, 5.888e-05, 109.331786, 0.00017664, 364.43928665, 0.00058882, -36.44392867, -5.888e-05, -109.331786, -0.00017664, -364.43928665, -0.00058882, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 14.65, 4.15, 5.775)
    ops.node(123008, 14.65, 4.15, 7.975)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.175, 26384825.93716229, 10993677.47381762, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 147.86340119, 0.00073939, 180.78242443, 0.02557137, 18.07824244, 0.07030379, -147.86340119, -0.00073939, -180.78242443, -0.02557137, -18.07824244, -0.07030379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 90.01054601, 0.00093281, 110.04971211, 0.02329381, 11.00497121, 0.05817923, -90.01054601, -0.00093281, -110.04971211, -0.02329381, -11.00497121, -0.05817923, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 184.86158211, 0.01478772, 184.86158211, 0.04436316, 129.40310748, -3907.45924079, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 46.21539553, 7.927e-05, 138.64618658, 0.00023782, 462.15395528, 0.00079272, -46.21539553, -7.927e-05, -138.64618658, -0.00023782, -462.15395528, -0.00079272, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 145.58586896, 0.01865626, 145.58586896, 0.05596877, 101.91010827, -2322.47952682, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 36.39646724, 6.243e-05, 109.18940172, 0.00018729, 363.96467239, 0.0006243, -36.39646724, -6.243e-05, -109.18940172, -0.00018729, -363.96467239, -0.0006243, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.3, 5.8)
    ops.node(123009, 0.0, 8.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0875, 25619034.26883273, 10674597.61201364, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 71.40371262, 0.00139915, 87.32052227, 0.0299375, 8.73205223, 0.08076495, -71.40371262, -0.00139915, -87.32052227, -0.0299375, -8.73205223, -0.08076495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 87.99481532, 0.00103429, 107.60999602, 0.03303859, 10.7609996, 0.09974686, -87.99481532, -0.00103429, -107.60999602, -0.03303859, -10.7609996, -0.09974686, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 86.74374473, 0.02798302, 86.74374473, 0.08394906, 60.72062131, -1962.48716032, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 21.68593618, 7.662e-05, 65.05780855, 0.00022985, 216.85936182, 0.00076618, -21.68593618, -7.662e-05, -65.05780855, -0.00022985, -216.85936182, -0.00076618, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 104.34307104, 0.0206858, 104.34307104, 0.0620574, 73.04014973, -3306.90984134, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 26.08576776, 9.216e-05, 78.25730328, 0.00027649, 260.85767759, 0.00092163, -26.08576776, -9.216e-05, -78.25730328, -0.00027649, -260.85767759, -0.00092163, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 5.9, 8.3, 5.8)
    ops.node(123010, 5.9, 8.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0875, 26354583.35465271, 10981076.39777196, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 39.28036747, 0.00126378, 47.90164922, 0.01920066, 4.79016492, 0.06054011, -39.28036747, -0.00126378, -47.90164922, -0.01920066, -4.79016492, -0.06054011, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 52.58653072, 0.00093606, 64.12825822, 0.02093802, 6.41282582, 0.07447152, -52.58653072, -0.00093606, -64.12825822, -0.02093802, -6.41282582, -0.07447152, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 86.37839474, 0.02527565, 86.37839474, 0.07582694, 60.46487632, -1519.09830856, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 21.59459868, 7.417e-05, 64.78379605, 0.0002225, 215.94598684, 0.00074166, -21.59459868, -7.417e-05, -64.78379605, -0.0002225, -215.94598684, -0.00074166, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 102.31096229, 0.01872125, 102.31096229, 0.05616376, 71.61767361, -2438.1517523, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 25.57774057, 8.785e-05, 76.73322172, 0.00026354, 255.77740573, 0.00087846, -25.57774057, -8.785e-05, -76.73322172, -0.00026354, -255.77740573, -0.00087846, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.75, 8.3, 5.8)
    ops.node(123011, 8.75, 8.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.0875, 26971058.91961571, 11237941.21650655, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 41.30231575, 0.00125527, 50.32592528, 0.02092971, 5.03259253, 0.06296041, -41.30231575, -0.00125527, -50.32592528, -0.02092971, -5.03259253, -0.06296041, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 54.78596078, 0.00093988, 66.75543776, 0.02287944, 6.67554378, 0.07730808, -54.78596078, -0.00093988, -66.75543776, -0.02287944, -6.67554378, -0.07730808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 91.82636053, 0.02510548, 91.82636053, 0.07531643, 64.27845237, -1726.48843763, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 22.95659013, 7.704e-05, 68.86977039, 0.00023113, 229.56590131, 0.00077042, -22.95659013, -7.704e-05, -68.86977039, -0.00023113, -229.56590131, -0.00077042, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 109.33681554, 0.01879765, 109.33681554, 0.05639295, 76.53577088, -2807.22325922, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 27.33420388, 9.173e-05, 82.00261165, 0.0002752, 273.34203885, 0.00091733, -27.33420388, -9.173e-05, -82.00261165, -0.0002752, -273.34203885, -0.00091733, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 14.65, 8.3, 5.8)
    ops.node(123012, 14.65, 8.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0875, 27469101.87824628, 11445459.11593595, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 73.77663586, 0.00144295, 89.96961843, 0.03158199, 8.99696184, 0.08440826, -73.77663586, -0.00144295, -89.96961843, -0.03158199, -8.99696184, -0.08440826, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 91.68739122, 0.00106007, 111.81154448, 0.03485945, 11.18115445, 0.10419107, -91.68739122, -0.00106007, -111.81154448, -0.03485945, -11.18115445, -0.10419107, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 92.7873386, 0.02885908, 92.7873386, 0.08657725, 64.95113702, -2069.14145879, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 23.19683465, 7.644e-05, 69.59050395, 0.00022931, 231.96834651, 0.00076437, -23.19683465, -7.644e-05, -69.59050395, -0.00022931, -231.96834651, -0.00076437, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 111.01988317, 0.02120134, 111.01988317, 0.06360401, 77.71391822, -3500.93808576, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 27.75497079, 9.146e-05, 83.26491238, 0.00027437, 277.54970793, 0.00091456, -27.75497079, -9.146e-05, -83.26491238, -0.00027437, -277.54970793, -0.00091456, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.55)
    ops.node(124001, 0.0, 0.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0875, 26253179.92213515, 10938824.96755631, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 53.77538251, 0.00139428, 65.98512164, 0.03322795, 6.59851216, 0.09171408, -53.77538251, -0.00139428, -65.98512164, -0.03322795, -6.59851216, -0.09171408, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 70.91154451, 0.00102046, 87.0120615, 0.03672029, 8.70120615, 0.11348018, -70.91154451, -0.00102046, -87.0120615, -0.03672029, -8.70120615, -0.11348018, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 84.38249289, 0.0278856, 84.38249289, 0.0836568, 59.06774502, -5123.9442127, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 21.09562322, 7.273e-05, 63.28686967, 0.0002182, 210.95623222, 0.00072732, -21.09562322, -7.273e-05, -63.28686967, -0.0002182, -210.95623222, -0.00072732, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 102.46923324, 0.02040921, 102.46923324, 0.06122764, 71.72846326, -9581.52816464, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 25.61730831, 8.832e-05, 76.85192493, 0.00026497, 256.17308309, 0.00088322, -25.61730831, -8.832e-05, -76.85192493, -0.00026497, -256.17308309, -0.00088322, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 14.65, 0.0, 8.55)
    ops.node(124004, 14.65, 0.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0875, 28204584.60188689, 11751910.25078621, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 57.52021552, 0.00139325, 70.27992652, 0.03131066, 7.02799265, 0.09036695, -57.52021552, -0.00139325, -70.27992652, -0.03131066, -7.02799265, -0.09036695, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 75.42043207, 0.00102671, 92.1509486, 0.03457754, 9.21509486, 0.11208574, -75.42043207, -0.00102671, -92.1509486, -0.03457754, -9.21509486, -0.11208574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 87.09637861, 0.02786508, 87.09637861, 0.08359523, 60.96746503, -4714.56364844, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 21.77409465, 6.988e-05, 65.32228396, 0.00020963, 217.74094652, 0.00069878, -21.77409465, -6.988e-05, -65.32228396, -0.00020963, -217.74094652, -0.00069878, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 104.38024459, 0.02053421, 104.38024459, 0.06160264, 73.06617121, -8798.17913979, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 26.09506115, 8.374e-05, 78.28518344, 0.00025123, 260.95061148, 0.00083744, -26.09506115, -8.374e-05, -78.28518344, -0.00025123, -260.95061148, -0.00083744, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.15, 8.525)
    ops.node(124005, 0.0, 4.15, 10.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.175, 27532434.52446334, 11471847.71852639, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 127.82813247, 0.00076058, 156.4330821, 0.02995537, 15.64330821, 0.08887835, -127.82813247, -0.00076058, -156.4330821, -0.02995537, -15.64330821, -0.08887835, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 76.67016827, 0.00098197, 93.8271607, 0.0270864, 9.38271607, 0.07227432, -76.67016827, -0.00098197, -93.8271607, -0.0270864, -9.38271607, -0.07227432, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 184.63013933, 0.01521162, 184.63013933, 0.04563487, 129.24109753, -9583.83218872, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 46.15753483, 7.587e-05, 138.4726045, 0.00022762, 461.57534832, 0.00075873, -46.15753483, -7.587e-05, -138.4726045, -0.00022762, -461.57534832, -0.00075873, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 144.89247599, 0.01963935, 144.89247599, 0.05891804, 101.42473319, -5037.38059506, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 36.223119, 5.954e-05, 108.66935699, 0.00017863, 362.23118997, 0.00059543, -36.223119, -5.954e-05, -108.66935699, -0.00017863, -362.23118997, -0.00059543, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 5.9, 4.15, 8.525)
    ops.node(124006, 5.9, 4.15, 10.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.175, 27624398.41257858, 11510166.00524108, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 137.28318469, 0.00075556, 167.85191669, 0.01882794, 16.78519167, 0.06161471, -137.28318469, -0.00075556, -167.85191669, -0.01882794, -16.78519167, -0.06161471, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 82.58965596, 0.0009628, 100.97982563, 0.01733847, 10.09798256, 0.05120303, -82.58965596, -0.0009628, -100.97982563, -0.01733847, -10.09798256, -0.05120303, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 162.85179454, 0.01511123, 162.85179454, 0.04533368, 113.99625618, -3793.85491433, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 40.71294864, 6.67e-05, 122.13884591, 0.0002001, 407.12948635, 0.000667, -40.71294864, -6.67e-05, -122.13884591, -0.0002001, -407.12948635, -0.000667, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 130.12115711, 0.01925603, 130.12115711, 0.05776808, 91.08480998, -2130.92031708, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 32.53028928, 5.329e-05, 97.59086783, 0.00015988, 325.30289277, 0.00053294, -32.53028928, -5.329e-05, -97.59086783, -0.00015988, -325.30289277, -0.00053294, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.75, 4.15, 8.525)
    ops.node(124007, 8.75, 4.15, 10.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.175, 27130705.82017782, 11304460.75840742, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 131.9941648, 0.00075865, 161.55529878, 0.02165068, 16.15552988, 0.06428253, -131.9941648, -0.00075865, -161.55529878, -0.02165068, -16.15552988, -0.06428253, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 79.45816789, 0.00097631, 97.25345111, 0.01990692, 9.72534511, 0.05364886, -79.45816789, -0.00097631, -97.25345111, -0.01990692, -9.72534511, -0.05364886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 168.31827265, 0.01517294, 168.31827265, 0.04551882, 117.82279086, -4690.05244819, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 42.07956816, 7.019e-05, 126.23870449, 0.00021058, 420.79568163, 0.00070194, -42.07956816, -7.019e-05, -126.23870449, -0.00021058, -420.79568163, -0.00070194, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 133.50240418, 0.01952629, 133.50240418, 0.05857886, 93.45168293, -2599.43648835, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 33.37560105, 5.567e-05, 100.12680314, 0.00016702, 333.75601046, 0.00055674, -33.37560105, -5.567e-05, -100.12680314, -0.00016702, -333.75601046, -0.00055674, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 14.65, 4.15, 8.525)
    ops.node(124008, 14.65, 4.15, 10.775)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.175, 28993110.08850084, 12080462.53687535, 0.00405757, 0.0019651, 0.00401042, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 131.82759564, 0.0007425, 160.75692803, 0.03124322, 16.0756928, 0.09052351, -131.82759564, -0.0007425, -160.75692803, -0.03124322, -16.0756928, -0.09052351, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 79.07210276, 0.00094651, 96.42433567, 0.02821864, 9.64243357, 0.07368058, -79.07210276, -0.00094651, -96.42433567, -0.02821864, -9.64243357, -0.07368058, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 205.05247237, 0.01484995, 205.05247237, 0.04454986, 143.53673066, -12177.07841584, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 51.26311809, 8.002e-05, 153.78935428, 0.00024006, 512.63118093, 0.0008002, -51.26311809, -8.002e-05, -153.78935428, -0.00024006, -512.63118093, -0.0008002, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 160.53160393, 0.01893023, 160.53160393, 0.0567907, 112.37212275, -6350.72442724, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 40.13290098, 6.265e-05, 120.39870295, 0.00018794, 401.32900983, 0.00062646, -40.13290098, -6.265e-05, -120.39870295, -0.00018794, -401.32900983, -0.00062646, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.3, 8.55)
    ops.node(124009, 0.0, 8.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0875, 27939068.65764095, 11641278.60735039, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 57.26486271, 0.00152895, 70.01212128, 0.03244411, 7.00121213, 0.09143247, -57.26486271, -0.00152895, -70.01212128, -0.03244411, -7.00121213, -0.09143247, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 75.89860836, 0.00109425, 92.79377129, 0.03576402, 9.27937713, 0.11318305, -75.89860836, -0.00109425, -92.79377129, -0.03576402, -9.27937713, -0.11318305, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 90.83215601, 0.03057898, 90.83215601, 0.09173693, 63.5825092, -5632.34231588, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 22.708039, 7.357e-05, 68.124117, 0.0002207, 227.08039002, 0.00073567, -22.708039, -7.357e-05, -68.124117, -0.0002207, -227.08039002, -0.00073567, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 109.87253767, 0.021885, 109.87253767, 0.065655, 76.91077637, -10555.37674444, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 27.46813442, 8.899e-05, 82.40440325, 0.00026697, 274.68134417, 0.00088989, -27.46813442, -8.899e-05, -82.40440325, -0.00026697, -274.68134417, -0.00088989, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 5.9, 8.3, 8.55)
    ops.node(124010, 5.9, 8.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0875, 26018517.25641327, 10841048.85683887, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 33.95005643, 0.00124057, 41.65029379, 0.02189051, 4.16502938, 0.07026454, -33.95005643, -0.00124057, -41.65029379, -0.02189051, -4.16502938, -0.07026454, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 44.76682184, 0.00092705, 54.92041775, 0.02395443, 5.49204178, 0.08659751, -44.76682184, -0.00092705, -54.92041775, -0.02395443, -5.49204178, -0.08659751, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 81.10171846, 0.02481136, 81.10171846, 0.07443407, 56.77120292, -3356.53295988, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 20.27542962, 7.053e-05, 60.82628885, 0.0002116, 202.75429616, 0.00070535, -20.27542962, -7.053e-05, -60.82628885, -0.0002116, -202.75429616, -0.00070535, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 97.77667268, 0.01854099, 97.77667268, 0.05562296, 68.44367088, -6137.45881216, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 24.44416817, 8.504e-05, 73.33250451, 0.00025511, 244.44168171, 0.00085037, -24.44416817, -8.504e-05, -73.33250451, -0.00025511, -244.44168171, -0.00085037, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.75, 8.3, 8.55)
    ops.node(124011, 8.75, 8.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.0875, 28488648.32723416, 11870270.13634757, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 31.97753705, 0.0012564, 39.02525896, 0.01989883, 3.9025259, 0.0691183, -31.97753705, -0.0012564, -39.02525896, -0.01989883, -3.9025259, -0.0691183, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 43.02786668, 0.00091898, 52.51103726, 0.02170772, 5.25110373, 0.08544562, -43.02786668, -0.00091898, -52.51103726, -0.02170772, -5.25110373, -0.08544562, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 83.28250364, 0.02512809, 83.28250364, 0.07538428, 58.29775255, -2838.60013341, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 20.82062591, 6.615e-05, 62.46187773, 0.00019845, 208.20625909, 0.00066151, -20.82062591, -6.615e-05, -62.46187773, -0.00019845, -208.20625909, -0.00066151, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 98.43525324, 0.01837966, 98.43525324, 0.05513898, 68.90467727, -5158.40332759, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 24.60881331, 7.819e-05, 73.82643993, 0.00023456, 246.0881331, 0.00078187, -24.60881331, -7.819e-05, -73.82643993, -0.00023456, -246.0881331, -0.00078187, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 14.65, 8.3, 8.55)
    ops.node(124012, 14.65, 8.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0875, 30761984.08654795, 12817493.36939498, 0.0010204, 0.00098255, 0.0005013, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 57.18934609, 0.00131492, 69.39237951, 0.03316844, 6.93923795, 0.09276031, -57.18934609, -0.00131492, -69.39237951, -0.03316844, -6.93923795, -0.09276031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 74.6743988, 0.00096924, 90.60838382, 0.03669133, 9.06083838, 0.11490243, -74.6743988, -0.00096924, -90.60838382, -0.03669133, -9.06083838, -0.11490243, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 102.7679128, 0.02629839, 102.7679128, 0.07889518, 71.93753896, -6718.85139414, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 25.6919782, 7.56e-05, 77.0759346, 0.00022679, 256.91978199, 0.00075596, -25.6919782, -7.56e-05, -77.0759346, -0.00022679, -256.91978199, -0.00075596, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 123.71152389, 0.01938482, 123.71152389, 0.05815446, 86.59806672, -12639.80723775, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 30.92788097, 9.1e-05, 92.78364292, 0.00027301, 309.27880972, 0.00091002, -30.92788097, -9.1e-05, -92.78364292, -0.00027301, -309.27880972, -0.00091002, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 5.9, 0.0, 0.0)
    ops.node(124013, 5.9, 0.0, 1.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4030, 170002, 124013, 0.165, 27602684.34676113, 11501118.47781714, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24030, 169.43929947, 0.00091244, 205.63593288, 0.04451921, 20.56359329, 0.10055489, -169.43929947, -0.00091244, -205.63593288, -0.04451921, -20.56359329, -0.10055489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14030, 250.57423564, 0.00069645, 304.10339787, 0.05506651, 30.41033979, 0.14963037, -250.57423564, -0.00069645, -304.10339787, -0.05506651, -30.41033979, -0.14963037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24030, 4030, 0.0, 267.04615495, 0.01824884, 267.04615495, 0.05474652, 186.93230846, -10137.81658584, 0.05, 2, 0, 70002, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 44030, 66.76153874, 5.805e-05, 200.28461621, 0.00017414, 667.61538737, 0.00058048, -66.76153874, -5.805e-05, -200.28461621, -0.00017414, -667.61538737, -0.00058048, 0.4, 0.3, 0.003, 0.0, 0.0, 24030, 2)
    ops.limitCurve('ThreePoint', 14030, 4030, 0.0, 433.20355689, 0.01392896, 433.20355689, 0.04178688, 303.24248983, -25329.72850615, 0.05, 2, 0, 70002, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 34030, 108.30088922, 9.417e-05, 324.90266767, 0.0002825, 1083.00889224, 0.00094166, -108.30088922, -9.417e-05, -324.90266767, -0.0002825, -1083.00889224, -0.00094166, 0.4, 0.3, 0.003, 0.0, 0.0, 14030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4030, 99999, 'P', 44030, 'Vy', 34030, 'Vz', 24030, 'My', 14030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 4030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174013, 5.9, 0.0, 1.55)
    ops.node(121002, 5.9, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4031, 174013, 121002, 0.165, 29706044.79564267, 12377518.66485111, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24031, 147.71742506, 0.00091502, 178.74771628, 0.04154381, 17.87477163, 0.10215642, -147.71742506, -0.00091502, -178.74771628, -0.04154381, -17.87477163, -0.10215642, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14031, 231.87857064, 0.00068682, 280.58819019, 0.05134386, 28.05881902, 0.15134386, -231.87857064, -0.00068682, -280.58819019, -0.05134386, -28.05881902, -0.15134386, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24031, 4031, 0.0, 251.13131402, 0.01830033, 251.13131402, 0.05490099, 175.79191981, -7453.55602753, 0.05, 2, 0, 74013, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44031, 62.7828285, 5.072e-05, 188.34848551, 0.00015217, 627.82828504, 0.00050723, -62.7828285, -5.072e-05, -188.34848551, -0.00015217, -627.82828504, -0.00050723, 0.4, 0.3, 0.003, 0.0, 0.0, 24031, 2)
    ops.limitCurve('ThreePoint', 14031, 4031, 0.0, 399.26107352, 0.01373634, 399.26107352, 0.04120901, 279.48275146, -17920.00808636, 0.05, 2, 0, 74013, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34031, 99.81526838, 8.064e-05, 299.44580514, 0.00024193, 998.1526838, 0.00080642, -99.81526838, -8.064e-05, -299.44580514, -0.00024193, -998.1526838, -0.00080642, 0.4, 0.3, 0.003, 0.0, 0.0, 14031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4031, 99999, 'P', 44031, 'Vy', 34031, 'Vz', 24031, 'My', 14031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174013, 74013, 174013, 4031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 8.75, 0.0, 0.0)
    ops.node(124014, 8.75, 0.0, 1.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4032, 170003, 124014, 0.165, 26935038.34657495, 11222932.64440623, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24032, 158.99924418, 0.00099786, 193.11459201, 0.04416819, 19.3114592, 0.09887878, -158.99924418, -0.00099786, -193.11459201, -0.04416819, -19.3114592, -0.09887878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14032, 246.12097385, 0.00072452, 298.92941753, 0.05455043, 29.89294175, 0.1468781, -246.12097385, -0.00072452, -298.92941753, -0.05455043, -29.89294175, -0.1468781, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24032, 4032, 0.0, 264.07645991, 0.0199572, 264.07645991, 0.05987159, 184.85352193, -10300.98118175, 0.05, 2, 0, 70003, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 44032, 66.01911498, 5.883e-05, 198.05734493, 0.00017648, 660.19114976, 0.00058825, -66.01911498, -5.883e-05, -198.05734493, -0.00017648, -660.19114976, -0.00058825, 0.4, 0.3, 0.003, 0.0, 0.0, 24032, 2)
    ops.limitCurve('ThreePoint', 14032, 4032, 0.0, 429.53345221, 0.01449049, 429.53345221, 0.04347148, 300.67341655, -25802.86605742, 0.05, 2, 0, 70003, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 34032, 107.38336305, 9.568e-05, 322.15008916, 0.00028705, 1073.83363053, 0.00095682, -107.38336305, -9.568e-05, -322.15008916, -0.00028705, -1073.83363053, -0.00095682, 0.4, 0.3, 0.003, 0.0, 0.0, 14032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4032, 99999, 'P', 44032, 'Vy', 34032, 'Vz', 24032, 'My', 14032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 4032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174014, 8.75, 0.0, 1.55)
    ops.node(121003, 8.75, 0.0, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4033, 174014, 121003, 0.165, 27884144.93644137, 11618393.72351724, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24033, 148.17341194, 0.00087196, 179.88899224, 0.0433608, 17.98889922, 0.10115251, -148.17341194, -0.00087196, -179.88899224, -0.0433608, -17.98889922, -0.10115251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14033, 225.84024134, 0.00067213, 274.17991454, 0.05364833, 27.41799145, 0.15117561, -225.84024134, -0.00067213, -274.17991454, -0.05364833, -27.41799145, -0.15117561, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24033, 4033, 0.0, 248.89087048, 0.01743918, 248.89087048, 0.05231753, 174.22360933, -8502.64573484, 0.05, 2, 0, 74014, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44033, 62.22271762, 5.356e-05, 186.66815286, 0.00016067, 622.2271762, 0.00053555, -62.22271762, -5.356e-05, -186.66815286, -0.00016067, -622.2271762, -0.00053555, 0.4, 0.3, 0.003, 0.0, 0.0, 24033, 2)
    ops.limitCurve('ThreePoint', 14033, 4033, 0.0, 400.12821103, 0.01344261, 400.12821103, 0.04032784, 280.08974772, -20920.13865954, 0.05, 2, 0, 74014, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34033, 100.03205276, 8.61e-05, 300.09615827, 0.00025829, 1000.32052757, 0.00086098, -100.03205276, -8.61e-05, -300.09615827, -0.00025829, -1000.32052757, -0.00086098, 0.4, 0.3, 0.003, 0.0, 0.0, 14033, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4033, 99999, 'P', 44033, 'Vy', 34033, 'Vz', 24033, 'My', 14033, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174014, 74014, 174014, 4033, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4033, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 5.9, 0.0, 3.05)
    ops.node(124015, 5.9, 0.0, 3.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4035, 171002, 124015, 0.165, 27301843.93728144, 11375768.3072006, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24035, 101.52463603, 0.00093789, 123.57890428, 0.04253284, 12.35789043, 0.10244715, -101.52463603, -0.00093789, -123.57890428, -0.04253284, -12.35789043, -0.10244715, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14035, 174.88382219, 0.00068944, 212.87395816, 0.05255111, 21.28739582, 0.15255111, -174.88382219, -0.00068944, -212.87395816, -0.05255111, -21.28739582, -0.15255111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24035, 4035, 0.0, 239.23312925, 0.01875783, 239.23312925, 0.05627348, 167.46319048, -9332.64161339, 0.05, 2, 0, 71002, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 44035, 59.80828231, 5.258e-05, 179.42484694, 0.00015773, 598.08282314, 0.00052575, -59.80828231, -5.258e-05, -179.42484694, -0.00015773, -598.08282314, -0.00052575, 0.4, 0.3, 0.003, 0.0, 0.0, 24035, 2)
    ops.limitCurve('ThreePoint', 14035, 4035, 0.0, 386.29821286, 0.01378884, 386.29821286, 0.04136651, 270.408749, -24119.05887559, 0.05, 2, 0, 71002, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 34035, 96.57455322, 8.489e-05, 289.72365965, 0.00025468, 965.74553216, 0.00084895, -96.57455322, -8.489e-05, -289.72365965, -0.00025468, -965.74553216, -0.00084895, 0.4, 0.3, 0.003, 0.0, 0.0, 14035, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4035, 99999, 'P', 44035, 'Vy', 34035, 'Vz', 24035, 'My', 14035, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4035, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 4035, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174015, 5.9, 0.0, 4.3)
    ops.node(122002, 5.9, 0.0, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4036, 174015, 122002, 0.165, 27340209.43542022, 11391753.93142509, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24036, 116.42491912, 0.00091736, 141.81705157, 0.0422202, 14.18170516, 0.10358739, -116.42491912, -0.00091736, -141.81705157, -0.0422202, -14.18170516, -0.10358739, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14036, 189.41931723, 0.00068975, 230.73143862, 0.05218722, 23.07314386, 0.15218722, -189.41931723, -0.00068975, -230.73143862, -0.05218722, -23.07314386, -0.15218722, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24036, 4036, 0.0, 226.49838433, 0.01834716, 226.49838433, 0.05504147, 158.54886903, -8487.33683897, 0.05, 2, 0, 74015, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44036, 56.62459608, 4.971e-05, 169.87378825, 0.00014912, 566.24596082, 0.00049707, -56.62459608, -4.971e-05, -169.87378825, -0.00014912, -566.24596082, -0.00049707, 0.4, 0.3, 0.003, 0.0, 0.0, 24036, 2)
    ops.limitCurve('ThreePoint', 14036, 4036, 0.0, 363.869979, 0.01379501, 363.869979, 0.04138502, 254.7089853, -21992.23626652, 0.05, 2, 0, 74015, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34036, 90.96749475, 7.985e-05, 272.90248425, 0.00023956, 909.67494751, 0.00079854, -90.96749475, -7.985e-05, -272.90248425, -0.00023956, -909.67494751, -0.00079854, 0.4, 0.3, 0.003, 0.0, 0.0, 14036, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4036, 99999, 'P', 44036, 'Vy', 34036, 'Vz', 24036, 'My', 14036, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174015, 74015, 174015, 4036, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4036, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.75, 0.0, 3.05)
    ops.node(124016, 8.75, 0.0, 3.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4037, 171003, 124016, 0.165, 28891551.43561214, 12038146.43150506, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24037, 107.81225116, 0.00090911, 130.86747876, 0.04309629, 13.08674788, 0.10526121, -107.81225116, -0.00090911, -130.86747876, -0.04309629, -13.08674788, -0.10526121, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14037, 182.76725102, 0.00068413, 221.85131174, 0.0532842, 22.18513117, 0.1532842, -182.76725102, -0.00068413, -221.85131174, -0.0532842, -22.18513117, -0.1532842, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24037, 4037, 0.0, 257.77212769, 0.01818221, 257.77212769, 0.05454664, 180.44048938, -10356.32762129, 0.05, 2, 0, 71003, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 44037, 64.44303192, 5.353e-05, 193.32909577, 0.0001606, 644.43031923, 0.00053532, -64.44303192, -5.353e-05, -193.32909577, -0.0001606, -644.43031923, -0.00053532, 0.4, 0.3, 0.003, 0.0, 0.0, 24037, 2)
    ops.limitCurve('ThreePoint', 14037, 4037, 0.0, 416.04915721, 0.01368255, 416.04915721, 0.04104764, 291.23441005, -27147.15451773, 0.05, 2, 0, 71003, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 34037, 104.0122893, 8.64e-05, 312.03686791, 0.00025921, 1040.12289303, 0.00086402, -104.0122893, -8.64e-05, -312.03686791, -0.00025921, -1040.12289303, -0.00086402, 0.4, 0.3, 0.003, 0.0, 0.0, 14037, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4037, 99999, 'P', 44037, 'Vy', 34037, 'Vz', 24037, 'My', 14037, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4037, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 4037, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174016, 8.75, 0.0, 4.3)
    ops.node(122003, 8.75, 0.0, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4038, 174016, 122003, 0.165, 27751050.16911313, 11562937.57046381, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24038, 120.94986667, 0.00091131, 147.22844287, 0.04475171, 14.72284429, 0.10668862, -120.94986667, -0.00091131, -147.22844287, -0.04475171, -14.72284429, -0.10668862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14038, 194.37423311, 0.00069163, 236.60559919, 0.05535299, 23.66055992, 0.15535299, -194.37423311, -0.00069163, -236.60559919, -0.05535299, -23.66055992, -0.15535299, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24038, 4038, 0.0, 259.33397898, 0.0182263, 259.33397898, 0.05467889, 181.53378529, -12719.55231659, 0.05, 2, 0, 74016, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44038, 64.83349475, 5.607e-05, 194.50048424, 0.00016821, 648.33494746, 0.0005607, -64.83349475, -5.607e-05, -194.50048424, -0.00016821, -648.33494746, -0.0005607, 0.4, 0.3, 0.003, 0.0, 0.0, 24038, 2)
    ops.limitCurve('ThreePoint', 14038, 4038, 0.0, 422.99087686, 0.01383259, 422.99087686, 0.04149776, 296.0936138, -34657.00500978, 0.05, 2, 0, 74016, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34038, 105.74771921, 9.145e-05, 317.24315764, 0.00027436, 1057.47719215, 0.00091454, -105.74771921, -9.145e-05, -317.24315764, -0.00027436, -1057.47719215, -0.00091454, 0.4, 0.3, 0.003, 0.0, 0.0, 14038, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4038, 99999, 'P', 44038, 'Vy', 34038, 'Vz', 24038, 'My', 14038, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174016, 74016, 174016, 4038, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4038, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 5.9, 0.0, 5.8)
    ops.node(124017, 5.9, 0.0, 6.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4040, 172002, 124017, 0.125, 30534227.3739001, 12722594.73912504, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24040, 68.14460169, 0.00105911, 82.47281636, 0.03124173, 8.24728164, 0.08248095, -68.14460169, -0.00105911, -82.47281636, -0.03124173, -8.24728164, -0.08248095, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14040, 135.12846122, 0.00069706, 163.54083068, 0.0391004, 16.35408307, 0.12983069, -135.12846122, -0.00069706, -163.54083068, -0.0391004, -16.35408307, -0.12983069, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24040, 4040, 0.0, 150.56987062, 0.02118225, 150.56987062, 0.06354675, 105.39890944, -4482.2532245, 0.05, 2, 0, 72002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44040, 37.64246766, 3.905e-05, 112.92740297, 0.00011716, 376.42467656, 0.00039055, -37.64246766, -3.905e-05, -112.92740297, -0.00011716, -376.42467656, -0.00039055, 0.4, 0.3, 0.003, 0.0, 0.0, 24040, 2)
    ops.limitCurve('ThreePoint', 14040, 4040, 0.0, 274.78325492, 0.01394113, 274.78325492, 0.0418234, 192.34827844, -12764.07566363, 0.05, 2, 0, 72002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34040, 68.69581373, 7.127e-05, 206.08744119, 0.00021382, 686.9581373, 0.00071274, -68.69581373, -7.127e-05, -206.08744119, -0.00021382, -686.9581373, -0.00071274, 0.4, 0.3, 0.003, 0.0, 0.0, 14040, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4040, 99999, 'P', 44040, 'Vy', 34040, 'Vz', 24040, 'My', 14040, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4040, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4040, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 5.9, 0.0, 7.05)
    ops.node(123002, 5.9, 0.0, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 174017, 123002, 0.125, 27787165.49197738, 11577985.62165724, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 75.74445305, 0.0010593, 92.32606351, 0.03562093, 9.23260635, 0.08616231, -75.74445305, -0.0010593, -92.32606351, -0.03562093, -9.23260635, -0.08616231, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 141.86281947, 0.00070644, 172.91874392, 0.0446815, 17.29187439, 0.13417608, -141.86281947, -0.00070644, -172.91874392, -0.0446815, -17.29187439, -0.13417608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 146.86435454, 0.02118596, 146.86435454, 0.06355787, 102.80504818, -6304.3043675, 0.05, 2, 0, 74017, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 36.71608864, 4.186e-05, 110.14826591, 0.00012558, 367.16088636, 0.0004186, -36.71608864, -4.186e-05, -110.14826591, -0.00012558, -367.16088636, -0.0004186, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 271.36794021, 0.01412872, 271.36794021, 0.04238615, 189.95755815, -19589.41413344, 0.05, 2, 0, 74017, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 67.84198505, 7.735e-05, 203.52595516, 0.00023204, 678.41985052, 0.00077346, -67.84198505, -7.735e-05, -203.52595516, -0.00023204, -678.41985052, -0.00077346, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.75, 0.0, 5.8)
    ops.node(124018, 8.75, 0.0, 6.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 172003, 124018, 0.125, 25392268.25933572, 10580111.77472322, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 71.33993964, 0.00116531, 87.15241579, 0.03453002, 8.71524158, 0.08062445, -71.33993964, -0.00116531, -87.15241579, -0.03453002, -8.71524158, -0.08062445, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 138.66191682, 0.0007574, 169.39628896, 0.04320954, 16.9396289, 0.12482984, -138.66191682, -0.0007574, -169.39628896, -0.04320954, -16.9396289, -0.12482984, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 137.2536991, 0.02330611, 137.2536991, 0.06991833, 96.07758937, -5400.13601832, 0.05, 2, 0, 72003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 34.31342478, 4.281e-05, 102.94027433, 0.00012843, 343.13424776, 0.0004281, -34.31342478, -4.281e-05, -102.94027433, -0.00012843, -343.13424776, -0.0004281, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 254.16682321, 0.01514804, 254.16682321, 0.04544412, 177.91677624, -15888.64796288, 0.05, 2, 0, 72003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 63.5417058, 7.928e-05, 190.62511741, 0.00023783, 635.41705802, 0.00079276, -63.5417058, -7.928e-05, -190.62511741, -0.00023783, -635.41705802, -0.00079276, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 8.75, 0.0, 7.05)
    ops.node(123003, 8.75, 0.0, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 174018, 123003, 0.125, 27042734.91592156, 11267806.21496732, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 71.84620072, 0.00113007, 87.69168257, 0.03663061, 8.76916826, 0.08651388, -71.84620072, -0.00113007, -87.69168257, -0.03663061, -8.76916826, -0.08651388, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 137.85442465, 0.00072178, 168.25783863, 0.04589146, 16.82578386, 0.13422075, -137.85442465, -0.00072178, -168.25783863, -0.04589146, -16.82578386, -0.13422075, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 144.57353181, 0.02260145, 144.57353181, 0.06780436, 101.20147226, -6412.14937402, 0.05, 2, 0, 74018, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 36.14338295, 4.234e-05, 108.43014885, 0.00012702, 361.43382951, 0.00042341, -36.14338295, -4.234e-05, -108.43014885, -0.00012702, -361.43382951, -0.00042341, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 267.64212868, 0.01443556, 267.64212868, 0.04330669, 187.34949007, -19969.83993096, 0.05, 2, 0, 74018, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 66.91053217, 7.838e-05, 200.73159651, 0.00023515, 669.10532169, 0.00078384, -66.91053217, -7.838e-05, -200.73159651, -0.00023515, -669.10532169, -0.00078384, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 5.9, 0.0, 8.55)
    ops.node(124019, 5.9, 0.0, 9.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4045, 173002, 124019, 0.125, 29380084.67565384, 12241701.9481891, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24045, 61.11770366, 0.00098136, 74.40313899, 0.03506564, 7.4403139, 0.09021938, -61.11770366, -0.00098136, -74.40313899, -0.03506564, -7.4403139, -0.09021938, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14045, 118.57341412, 0.00067333, 144.34826054, 0.04404101, 14.43482605, 0.14170282, -118.57341412, -0.00067333, -144.34826054, -0.04404101, -14.43482605, -0.14170282, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24045, 4045, 0.0, 145.67430845, 0.01962721, 145.67430845, 0.05888162, 101.97201591, -10263.10287746, 0.05, 2, 0, 73002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44045, 36.41857711, 3.927e-05, 109.25573134, 0.00011781, 364.18577112, 0.00039269, -36.41857711, -3.927e-05, -109.25573134, -0.00011781, -364.18577112, -0.00039269, 0.4, 0.3, 0.003, 0.0, 0.0, 24045, 2)
    ops.limitCurve('ThreePoint', 14045, 4045, 0.0, 268.87740874, 0.01346666, 268.87740874, 0.04039998, 188.21418612, -36123.71660896, 0.05, 2, 0, 73002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34045, 67.21935219, 7.248e-05, 201.65805656, 0.00021744, 672.19352185, 0.00072481, -67.21935219, -7.248e-05, -201.65805656, -0.00021744, -672.19352185, -0.00072481, 0.4, 0.3, 0.003, 0.0, 0.0, 14045, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4045, 99999, 'P', 44045, 'Vy', 34045, 'Vz', 24045, 'My', 14045, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4045, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4045, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 5.9, 0.0, 9.8)
    ops.node(124002, 5.9, 0.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 174019, 124002, 0.125, 27212692.94175111, 11338622.05906296, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 59.53398338, 0.00103988, 72.92881493, 0.03759737, 7.29288149, 0.0938533, -59.53398338, -0.00103988, -72.92881493, -0.03759737, -7.29288149, -0.0938533, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 115.28833691, 0.0006997, 141.22760328, 0.0472142, 14.12276033, 0.14682767, -115.28833691, -0.0006997, -141.22760328, -0.0472142, -14.12276033, -0.14682767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 138.08338202, 0.02079769, 138.08338202, 0.06239307, 96.65836741, -21218.20176876, 0.05, 2, 0, 74019, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 34.52084551, 4.019e-05, 103.56253652, 0.00012056, 345.20845505, 0.00040188, -34.52084551, -4.019e-05, -103.56253652, -0.00012056, -345.20845505, -0.00040188, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 256.99555102, 0.01399392, 256.99555102, 0.04198176, 179.89688571, -79912.04549492, 0.05, 2, 0, 74019, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 64.24888775, 7.48e-05, 192.74666326, 0.00022439, 642.48887754, 0.00074796, -64.24888775, -7.48e-05, -192.74666326, -0.00022439, -642.48887754, -0.00074796, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.75, 0.0, 8.55)
    ops.node(124020, 8.75, 0.0, 9.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 173003, 124020, 0.125, 24593834.09550582, 10247430.87312743, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 64.98247635, 0.00108632, 79.87730042, 0.03709209, 7.98773004, 0.09001654, -64.98247635, -0.00108632, -79.87730042, -0.03709209, -7.98773004, -0.09001654, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 122.84971135, 0.00073218, 151.00845415, 0.04654471, 15.10084542, 0.14025906, -122.84971135, -0.00073218, -151.00845415, -0.04654471, -15.10084542, -0.14025906, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 125.16781654, 0.02172645, 125.16781654, 0.06517936, 87.61747158, -9900.41464816, 0.05, 2, 0, 73003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 31.29195413, 4.031e-05, 93.8758624, 0.00012092, 312.91954134, 0.00040308, -31.29195413, -4.031e-05, -93.8758624, -0.00012092, -312.91954134, -0.00040308, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 233.25541265, 0.0146437, 233.25541265, 0.04393109, 163.27878886, -34763.6433894, 0.05, 2, 0, 73003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 58.31385316, 7.512e-05, 174.94155949, 0.00022535, 583.13853163, 0.00075116, -58.31385316, -7.512e-05, -174.94155949, -0.00022535, -583.13853163, -0.00075116, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 8.75, 0.0, 9.8)
    ops.node(124003, 8.75, 0.0, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 174020, 124003, 0.125, 26493722.11040679, 11039050.87933616, 0.00178813, 0.00286458, 0.00071615, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 58.13532898, 0.0010338, 71.32509825, 0.03763416, 7.13250983, 0.09372638, -58.13532898, -0.0010338, -71.32509825, -0.03763416, -7.13250983, -0.09372638, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 112.65121837, 0.00069574, 138.20957684, 0.0472648, 13.82095768, 0.14658838, -112.65121837, -0.00069574, -138.20957684, -0.0472648, -13.82095768, -0.14658838, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 134.19438533, 0.02067608, 134.19438533, 0.06202825, 93.93606973, -20636.84599866, 0.05, 2, 0, 74020, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 33.54859633, 4.012e-05, 100.645789, 0.00012035, 335.48596332, 0.00040116, -33.54859633, -4.012e-05, -100.645789, -0.00012035, -335.48596332, -0.00040116, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 250.02296147, 0.01391472, 250.02296147, 0.04174415, 175.01607303, -77656.08444314, 0.05, 2, 0, 74020, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 62.50574037, 7.474e-05, 187.5172211, 0.00022422, 625.05740368, 0.00074742, -62.50574037, -7.474e-05, -187.5172211, -0.00022422, -625.05740368, -0.00074742, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
