import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.15, 24563224.2069678, 10234676.75290325, 0.00281737, 0.0034375, 0.0012375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 85.68246227, 0.00116884, 104.33992401, 0.01978829, 10.4339924, 0.04754656, -85.68246227, -0.00116884, -104.33992401, -0.01978829, -10.4339924, -0.04754656, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 140.46710021, 0.00080273, 171.05398438, 0.02251378, 17.10539844, 0.06247543, -140.46710021, -0.00080273, -171.05398438, -0.02251378, -17.10539844, -0.06247543, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 122.1768778, 0.02337671, 122.1768778, 0.07013012, 85.52381446, -1536.36043051, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 30.54421945, 6.566e-05, 91.63265835, 0.00019697, 305.4421945, 0.00065656, -30.54421945, -6.566e-05, -91.63265835, -0.00019697, -305.4421945, -0.00065656, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 164.98490343, 0.01605469, 164.98490343, 0.04816407, 115.4894324, -2737.22308398, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 41.24622586, 8.866e-05, 123.73867757, 0.00026598, 412.46225857, 0.00088661, -41.24622586, -8.866e-05, -123.73867757, -0.00026598, -412.46225857, -0.00088661, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 12.85, 0.0, 0.0)
    ops.node(121004, 12.85, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.15, 27810128.47716095, 11587553.5321504, 0.00281737, 0.0034375, 0.0012375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 86.77106236, 0.00113138, 105.3766924, 0.01887708, 10.53766924, 0.05037779, -86.77106236, -0.00113138, -105.3766924, -0.01887708, -10.53766924, -0.05037779, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 142.82434632, 0.0007794, 173.44903704, 0.02147161, 17.3449037, 0.06682099, -142.82434632, -0.0007794, -173.44903704, -0.02147161, -17.3449037, -0.06682099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 131.77735719, 0.02262767, 131.77735719, 0.06788302, 92.24415003, -1403.19127849, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 32.9443393, 6.255e-05, 98.83301789, 0.00018764, 329.44339298, 0.00062548, -32.9443393, -6.255e-05, -98.83301789, -0.00018764, -329.44339298, -0.00062548, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 174.14266555, 0.01558804, 174.14266555, 0.04676411, 121.89986589, -2442.6407416, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 43.53566639, 8.266e-05, 130.60699916, 0.00024797, 435.35666388, 0.00082656, -43.53566639, -8.266e-05, -130.60699916, -0.00024797, -435.35666388, -0.00082656, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.65, 0.0)
    ops.node(121005, 0.0, 4.65, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.28, 27334274.68746622, 11389281.11977759, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 575.0378603, 0.00069269, 699.12497907, 0.04052284, 69.91249791, 0.10075645, -575.0378603, -0.00069269, -699.12497907, -0.04052284, -69.91249791, -0.10075645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 302.5037032, 0.0011595, 367.78081891, 0.03180276, 36.77808189, 0.06414068, -302.5037032, -0.0011595, -367.78081891, -0.03180276, -36.77808189, -0.06414068, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 494.70678852, 0.0138537, 494.70678852, 0.04156111, 346.29475196, -7788.50122265, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 123.67669713, 0.00012798, 371.03009139, 0.00038394, 1236.7669713, 0.00127982, -123.67669713, -0.00012798, -371.03009139, -0.00038394, -1236.7669713, -0.00127982, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 246.69616111, 0.02319001, 246.69616111, 0.06957004, 172.68731278, -2830.74380881, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 61.67404028, 6.382e-05, 185.02212083, 0.00019146, 616.74040277, 0.00063821, -61.67404028, -6.382e-05, -185.02212083, -0.00019146, -616.74040277, -0.00063821, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 4.95, 4.65, 0.0)
    ops.node(121006, 4.95, 4.65, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.4275, 27271838.44193284, 11363266.01747202, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 990.55660131, 0.00065663, 1206.24699331, 0.0521109, 120.62469933, 0.12371735, -990.55660131, -0.00065663, -1206.24699331, -0.0521109, -120.62469933, -0.12371735, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 635.6403539, 0.00093958, 774.04891826, 0.04107069, 77.40489183, 0.08078141, -635.6403539, -0.00093958, -774.04891826, -0.04107069, -77.40489183, -0.08078141, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 855.81950878, 0.01313257, 855.81950878, 0.03939771, 599.07365614, -19369.37490683, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 213.95487719, 0.00014534, 641.86463158, 0.00043603, 2139.54877194, 0.00145344, -213.95487719, -0.00014534, -641.86463158, -0.00043603, -2139.54877194, -0.00145344, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 429.29522666, 0.01879168, 429.29522666, 0.05637503, 300.50665866, -6590.7280328, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 107.32380667, 7.291e-05, 321.97142, 0.00021872, 1073.23806665, 0.00072907, -107.32380667, -7.291e-05, -321.97142, -0.00021872, -1073.23806665, -0.00072907, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 7.9, 4.65, 0.0)
    ops.node(121007, 7.9, 4.65, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.4275, 26885105.66811134, 11202127.36171306, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 991.11838029, 0.000658, 1207.61153081, 0.05253122, 120.76115308, 0.12342906, -991.11838029, -0.000658, -1207.61153081, -0.05253122, -120.76115308, -0.12342906, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 641.33275771, 0.00093867, 781.4211185, 0.04139653, 78.14211185, 0.08071427, -641.33275771, -0.00093867, -781.4211185, -0.04139653, -78.14211185, -0.08071427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 863.77338324, 0.01315998, 863.77338324, 0.03947995, 604.64136827, -20798.32105004, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 215.94334581, 0.0001488, 647.83003743, 0.00044641, 2159.4334581, 0.00148805, -215.94334581, -0.0001488, -647.83003743, -0.00044641, -2159.4334581, -0.00148805, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 432.59784209, 0.01877337, 432.59784209, 0.05632011, 302.81848946, -6984.24080439, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 108.14946052, 7.452e-05, 324.44838157, 0.00022357, 1081.49460522, 0.00074525, -108.14946052, -7.452e-05, -324.44838157, -0.00022357, -1081.49460522, -0.00074525, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 12.85, 4.65, 0.0)
    ops.node(121008, 12.85, 4.65, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.28, 26269377.68789311, 10945574.03662213, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 570.5627848, 0.00069053, 694.5425332, 0.04097292, 69.45425332, 0.09913158, -570.5627848, -0.00069053, -694.5425332, -0.04097292, -69.45425332, -0.09913158, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 306.38844202, 0.00113786, 372.96474697, 0.03212905, 37.2964747, 0.06335298, -306.38844202, -0.00113786, -372.96474697, -0.03212905, -37.2964747, -0.06335298, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 478.74583349, 0.01381069, 478.74583349, 0.04143208, 335.12208344, -7771.74676762, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 119.68645837, 0.00012887, 359.05937511, 0.00038662, 1196.86458372, 0.00128873, -119.68645837, -0.00012887, -359.05937511, -0.00038662, -1196.86458372, -0.00128873, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 238.15236778, 0.02275723, 238.15236778, 0.06827169, 166.70665744, -2826.32407788, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 59.53809194, 6.411e-05, 178.61427583, 0.00019232, 595.38091944, 0.00064108, -59.53809194, -6.411e-05, -178.61427583, -0.00019232, -595.38091944, -0.00064108, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 9.3, 0.0)
    ops.node(121009, 0.0, 9.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.28, 28110010.77032863, 11712504.48763693, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 589.18766611, 0.00070036, 715.54313685, 0.04204511, 71.55431368, 0.10374122, -589.18766611, -0.00070036, -715.54313685, -0.04204511, -71.55431368, -0.10374122, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 310.17237858, 0.00117472, 376.69104345, 0.03298324, 37.66910435, 0.06610634, -310.17237858, -0.00117472, -376.69104345, -0.03298324, -37.66910435, -0.06610634, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 518.47536583, 0.0140071, 518.47536583, 0.04202131, 362.93275608, -8566.64878927, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 129.61884146, 0.00013043, 388.85652438, 0.00039129, 1296.18841458, 0.00130429, -129.61884146, -0.00013043, -388.85652438, -0.00039129, -1296.18841458, -0.00130429, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 258.20286134, 0.02349443, 258.20286134, 0.0704833, 180.74200294, -3027.69442146, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 64.55071533, 6.495e-05, 193.652146, 0.00019486, 645.50715335, 0.00064954, -64.55071533, -6.495e-05, -193.652146, -0.00019486, -645.50715335, -0.00064954, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 4.95, 9.3, 0.0)
    ops.node(121010, 4.95, 9.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.36, 26746085.64158459, 11144202.35066025, 0.01384148, 0.00528, 0.02673, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 849.69955342, 0.00066372, 1034.49401713, 0.05528272, 103.44940171, 0.13120594, -849.69955342, -0.00066372, -1034.49401713, -0.05528272, -103.44940171, -0.13120594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 498.01792555, 0.00102899, 606.32792183, 0.04252917, 60.63279218, 0.08210215, -498.01792555, -0.00102899, -606.32792183, -0.04252917, -60.63279218, -0.08210215, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 786.07684566, 0.01327437, 786.07684566, 0.03982311, 550.25379196, -20537.99022712, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 196.51921141, 0.00016165, 589.55763424, 0.00048494, 1965.19211414, 0.00161647, -196.51921141, -0.00016165, -589.55763424, -0.00048494, -1965.19211414, -0.00161647, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 371.67464331, 0.02057982, 371.67464331, 0.06173946, 260.17225031, -6308.53362566, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 92.91866083, 7.643e-05, 278.75598248, 0.00022929, 929.18660827, 0.0007643, -92.91866083, -7.643e-05, -278.75598248, -0.00022929, -929.18660827, -0.0007643, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 7.9, 9.3, 0.0)
    ops.node(121011, 7.9, 9.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.36, 26590806.84649917, 11079502.85270799, 0.01384148, 0.00528, 0.02673, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 862.0323138, 0.00066347, 1049.70366275, 0.05365434, 104.97036627, 0.12921153, -862.0323138, -0.00066347, -1049.70366275, -0.05365434, -104.97036627, -0.12921153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 519.28766169, 0.00100996, 632.34075077, 0.04127307, 63.23407508, 0.08065527, -519.28766169, -0.00100996, -632.34075077, -0.04127307, -63.23407508, -0.08065527, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 737.8891267, 0.01326935, 737.8891267, 0.03980804, 516.52238869, -16858.07311147, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 184.47228168, 0.00015262, 553.41684503, 0.00045787, 1844.72281676, 0.00152624, -184.47228168, -0.00015262, -553.41684503, -0.00045787, -1844.72281676, -0.00152624, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 350.08370694, 0.02019922, 350.08370694, 0.06059766, 245.05859486, -5393.23456862, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 87.52092674, 7.241e-05, 262.56278021, 0.00021723, 875.20926736, 0.00072411, -87.52092674, -7.241e-05, -262.56278021, -0.00021723, -875.20926736, -0.00072411, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 12.85, 9.3, 0.0)
    ops.node(121012, 12.85, 9.3, 2.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.28, 28118265.11555659, 11715943.79814858, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 575.72358011, 0.00068848, 699.18209574, 0.0435709, 69.91820957, 0.1052805, -575.72358011, -0.00068848, -699.18209574, -0.0435709, -69.91820957, -0.1052805, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 300.88692666, 0.00115415, 365.40930272, 0.03414566, 36.54093027, 0.067276, -300.88692666, -0.00115415, -365.40930272, -0.03414566, -36.54093027, -0.067276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 544.77973971, 0.01376962, 544.77973971, 0.04130885, 381.3458178, -10228.87568279, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 136.19493493, 0.00013701, 408.58480478, 0.00041102, 1361.94934928, 0.00137006, -136.19493493, -0.00013701, -408.58480478, -0.00041102, -1361.94934928, -0.00137006, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 269.72346348, 0.02308292, 269.72346348, 0.06924877, 188.80642443, -3454.96944773, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 67.43086587, 6.783e-05, 202.29259761, 0.0002035, 674.30865869, 0.00067832, -67.43086587, -6.783e-05, -202.29259761, -0.0002035, -674.30865869, -0.00067832, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 13.95, 0.0)
    ops.node(121013, 0.0, 13.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.15, 27724003.17264619, 11551667.98860258, 0.00281737, 0.0034375, 0.0012375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 101.57816561, 0.00116667, 123.39003515, 0.0268428, 12.33900352, 0.06357056, -101.57816561, -0.00116667, -123.39003515, -0.0268428, -12.33900352, -0.06357056, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 158.70410962, 0.00080297, 192.78262752, 0.03103686, 19.27826275, 0.0851532, -158.70410962, -0.00080297, -192.78262752, -0.03103686, -19.27826275, -0.0851532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 155.83476484, 0.02333342, 155.83476484, 0.07000025, 109.08433539, -2328.3181538, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 38.95869121, 7.42e-05, 116.87607363, 0.00022259, 389.58691211, 0.00074196, -38.95869121, -7.42e-05, -116.87607363, -0.00022259, -389.58691211, -0.00074196, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 214.56464561, 0.01605942, 214.56464561, 0.04817826, 150.19525193, -4557.84304146, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 53.6411614, 0.00010216, 160.92348421, 0.00030648, 536.41161404, 0.00102159, -53.6411614, -0.00010216, -160.92348421, -0.00030648, -536.41161404, -0.00102159, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 4.95, 13.95, 0.0)
    ops.node(121014, 4.95, 13.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2275, 25831942.59450376, 10763309.41437657, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 242.35041965, 0.00099407, 295.1845192, 0.03966297, 29.51845192, 0.08808245, -242.35041965, -0.00099407, -295.1845192, -0.03966297, -29.51845192, -0.08808245, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 328.7704778, 0.00068446, 400.44475911, 0.04884165, 40.04447591, 0.13032688, -328.7704778, -0.00068446, -400.44475911, -0.04884165, -40.04447591, -0.13032688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 263.64136291, 0.01988137, 263.64136291, 0.0596441, 184.54895404, -5594.65610444, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 65.91034073, 8.883e-05, 197.73102218, 0.00026648, 659.10340728, 0.00088826, -65.91034073, -8.883e-05, -197.73102218, -0.00026648, -659.10340728, -0.00088826, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 447.44313796, 0.01368927, 447.44313796, 0.0410678, 313.21019657, -14177.4000096, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 111.86078449, 0.00015075, 335.58235347, 0.00045226, 1118.60784491, 0.00150753, -111.86078449, -0.00015075, -335.58235347, -0.00045226, -1118.60784491, -0.00150753, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 7.9, 13.95, 0.0)
    ops.node(121015, 7.9, 13.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.2275, 27659086.01206975, 11524619.17169573, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 255.35218772, 0.00097149, 310.36206591, 0.03872693, 31.03620659, 0.09012199, -255.35218772, -0.00097149, -310.36206591, -0.03872693, -31.03620659, -0.09012199, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 340.85281322, 0.00067921, 414.28187567, 0.04769879, 41.42818757, 0.13419162, -340.85281322, -0.00067921, -414.28187567, -0.04769879, -41.42818757, -0.13419162, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 277.20627398, 0.01942983, 277.20627398, 0.05828948, 194.04439178, -5696.80673395, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 69.30156849, 8.723e-05, 207.90470548, 0.00026168, 693.01568494, 0.00087227, -69.30156849, -8.723e-05, -207.90470548, -0.00026168, -693.01568494, -0.00087227, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 468.60310516, 0.01358414, 468.60310516, 0.04075242, 328.02217361, -14479.6213893, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 117.15077629, 0.00014745, 351.45232887, 0.00044236, 1171.5077629, 0.00147452, -117.15077629, -0.00014745, -351.45232887, -0.00044236, -1171.5077629, -0.00147452, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 12.85, 13.95, 0.0)
    ops.node(121016, 12.85, 13.95, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.15, 26153874.46889042, 10897447.69537101, 0.00281737, 0.0034375, 0.0012375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 97.14843972, 0.00119611, 118.22574941, 0.02536017, 11.82257494, 0.0602039, -97.14843972, -0.00119611, -118.22574941, -0.02536017, -11.82257494, -0.0602039, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 153.28588436, 0.00081155, 186.54276492, 0.02926496, 18.65427649, 0.08060529, -153.28588436, -0.00081155, -186.54276492, -0.02926496, -18.65427649, -0.08060529, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 142.28564718, 0.02392224, 142.28564718, 0.07176673, 99.59995302, -2047.48399256, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 35.57141179, 7.181e-05, 106.71423538, 0.00021544, 355.71411794, 0.00071812, -35.57141179, -7.181e-05, -106.71423538, -0.00021544, -355.71411794, -0.00071812, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 195.34356394, 0.01623104, 195.34356394, 0.04869312, 136.74049476, -3906.99230238, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 48.83589099, 9.859e-05, 146.50767296, 0.00029577, 488.35890986, 0.00098591, -48.83589099, -9.859e-05, -146.50767296, -0.00029577, -488.35890986, -0.00098591, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.0)
    ops.node(122001, 0.0, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.15, 28943108.3151231, 12059628.46463462, 0.00281737, 0.0034375, 0.0012375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 101.57300751, 0.00118659, 123.36746807, 0.03485696, 12.33674681, 0.08452844, -101.57300751, -0.00118659, -123.36746807, -0.03485696, -12.33674681, -0.08452844, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 155.76640838, 0.00079793, 189.18911512, 0.04088916, 18.91891151, 0.1160368, -155.76640838, -0.00079793, -189.18911512, -0.04088916, -18.91891151, -0.1160368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 170.7200641, 0.02373185, 170.7200641, 0.07119554, 119.50404487, -3334.80265505, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 42.68001603, 7.786e-05, 128.04004808, 0.00023358, 426.80016025, 0.0007786, -42.68001603, -7.786e-05, -128.04004808, -0.00023358, -426.80016025, -0.0007786, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 239.18399924, 0.01595858, 239.18399924, 0.04787575, 167.42879947, -7259.22093725, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 59.79599981, 0.00010908, 179.38799943, 0.00032725, 597.95999811, 0.00109084, -59.79599981, -0.00010908, -179.38799943, -0.00032725, -597.95999811, -0.00109084, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 12.85, 0.0, 3.0)
    ops.node(122004, 12.85, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.15, 29403977.48437407, 12251657.28515586, 0.00281737, 0.0034375, 0.0012375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 94.7553604, 0.00110943, 114.97142835, 0.03559423, 11.49714284, 0.08566401, -94.7553604, -0.00110943, -114.97142835, -0.03559423, -11.49714284, -0.08566401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 146.35052879, 0.0007497, 177.57443234, 0.04181067, 17.75744323, 0.1175609, -146.35052879, -0.0007497, -177.57443234, -0.04181067, -17.75744323, -0.1175609, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 175.83392429, 0.02218863, 175.83392429, 0.0665659, 123.083747, -3519.18203101, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 43.95848107, 7.894e-05, 131.87544322, 0.00023681, 439.58481073, 0.00078935, -43.95848107, -7.894e-05, -131.87544322, -0.00023681, -439.58481073, -0.00078935, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 246.68467914, 0.01499407, 246.68467914, 0.0449822, 172.6792754, -7713.40069809, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 61.67116979, 0.00011074, 185.01350936, 0.00033222, 616.71169785, 0.00110741, -61.67116979, -0.00011074, -185.01350936, -0.00033222, -616.71169785, -0.00110741, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.65, 3.05)
    ops.node(122005, 0.0, 4.65, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.28, 27578734.12184899, 11491139.21743708, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 401.91907125, 0.00062948, 489.56615765, 0.03330038, 48.95661576, 0.08473304, -401.91907125, -0.00062948, -489.56615765, -0.03330038, -48.95661576, -0.08473304, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 149.18210049, 0.0009997, 181.71446182, 0.02666404, 18.17144618, 0.05567555, -149.18210049, -0.0009997, -181.71446182, -0.02666404, -18.17144618, -0.05567555, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 441.91953744, 0.01258957, 441.91953744, 0.0377687, 309.34367621, -6421.14338148, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 110.47988436, 0.00011331, 331.43965308, 0.00033994, 1104.79884361, 0.00113312, -110.47988436, -0.00011331, -331.43965308, -0.00033994, -1104.79884361, -0.00113312, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 222.27802846, 0.01999399, 222.27802846, 0.05998197, 155.59461992, -2254.6047258, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 55.56950711, 5.699e-05, 166.70852134, 0.00017098, 555.69507115, 0.00056994, -55.56950711, -5.699e-05, -166.70852134, -0.00017098, -555.69507115, -0.00056994, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 4.95, 4.65, 3.05)
    ops.node(122006, 4.95, 4.65, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.4275, 29347858.64705681, 12228274.43627367, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 762.2007783, 0.00062193, 925.89717976, 0.0356676, 92.58971798, 0.091664, -762.2007783, -0.00062193, -925.89717976, -0.0356676, -92.58971798, -0.091664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 285.23263052, 0.00085781, 346.49149633, 0.02888413, 34.64914963, 0.06183789, -285.23263052, -0.00085781, -346.49149633, -0.02888413, -34.64914963, -0.06183789, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 726.03572268, 0.01243864, 726.03572268, 0.03731592, 508.22500587, -9881.49520426, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 181.50893067, 0.00011458, 544.52679201, 0.00034374, 1815.08930669, 0.0011458, -181.50893067, -0.00011458, -544.52679201, -0.00034374, -1815.08930669, -0.0011458, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 369.24231627, 0.0171562, 369.24231627, 0.0514686, 258.46962139, -3621.57757894, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 92.31057907, 5.827e-05, 276.9317372, 0.00017482, 923.10579067, 0.00058273, -92.31057907, -5.827e-05, -276.9317372, -0.00017482, -923.10579067, -0.00058273, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 7.9, 4.65, 3.05)
    ops.node(122007, 7.9, 4.65, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.4275, 25367381.45314012, 10569742.27214172, 0.02028107, 0.00793547, 0.03536672, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 711.73069911, 0.00062354, 870.6755708, 0.04047099, 87.06755708, 0.0924962, -711.73069911, -0.00062354, -870.6755708, -0.04047099, -87.06755708, -0.0924962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 265.37637002, 0.00087355, 324.64065795, 0.03273988, 32.46406579, 0.06335661, -265.37637002, -0.00087355, -324.64065795, -0.03273988, -32.46406579, -0.06335661, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 682.71213463, 0.01247086, 682.71213463, 0.03741259, 477.89849424, -13731.9276236, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 170.67803366, 0.00012465, 512.03410097, 0.00037395, 1706.78033657, 0.0012465, -170.67803366, -0.00012465, -512.03410097, -0.00037395, -1706.78033657, -0.0012465, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 343.94784955, 0.01747093, 343.94784955, 0.05241278, 240.76349469, -4706.03022449, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 85.98696239, 6.28e-05, 257.96088716, 0.00018839, 859.86962388, 0.00062798, -85.98696239, -6.28e-05, -257.96088716, -0.00018839, -859.86962388, -0.00062798, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 12.85, 4.65, 3.05)
    ops.node(122008, 12.85, 4.65, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.28, 27624437.34542678, 11510182.22726116, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 422.1711524, 0.00065497, 514.19416353, 0.03400993, 51.41941635, 0.08549192, -422.1711524, -0.00065497, -514.19416353, -0.03400993, -51.41941635, -0.08549192, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 156.65877048, 0.00105207, 190.80656029, 0.02725377, 19.08065603, 0.0562931, -156.65877048, -0.00105207, -190.80656029, -0.02725377, -19.08065603, -0.0562931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 451.74089505, 0.01309937, 451.74089505, 0.03929811, 316.21862653, -6995.33573199, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 112.93522376, 0.00011564, 338.80567128, 0.00034692, 1129.35223762, 0.00115639, -112.93522376, -0.00011564, -338.80567128, -0.00034692, -1129.35223762, -0.00115639, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 226.64220299, 0.02104145, 226.64220299, 0.06312434, 158.6495421, -2402.62619433, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 56.66055075, 5.802e-05, 169.98165224, 0.00017405, 566.60550748, 0.00058017, -56.66055075, -5.802e-05, -169.98165224, -0.00017405, -566.60550748, -0.00058017, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 9.3, 3.05)
    ops.node(122009, 0.0, 9.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.28, 25208998.17220958, 10503749.23842066, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 411.88787785, 0.000665, 503.32522445, 0.03139054, 50.33252245, 0.07989302, -411.88787785, -0.000665, -503.32522445, -0.03139054, -50.33252245, -0.07989302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 152.44773317, 0.00108024, 186.29047768, 0.02521642, 18.62904777, 0.05257511, -152.44773317, -0.00108024, -186.29047768, -0.02521642, -18.62904777, -0.05257511, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 395.36988668, 0.01330001, 395.36988668, 0.03990004, 276.75892068, -5724.3889143, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 98.84247167, 0.00011091, 296.52741501, 0.00033272, 988.42471671, 0.00110906, -98.84247167, -0.00011091, -296.52741501, -0.00033272, -988.42471671, -0.00110906, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 198.47540447, 0.02160481, 198.47540447, 0.06481444, 138.93278313, -2067.43838051, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 49.61885112, 5.567e-05, 148.85655335, 0.00016702, 496.18851117, 0.00055675, -49.61885112, -5.567e-05, -148.85655335, -0.00016702, -496.18851117, -0.00055675, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 4.95, 9.3, 3.05)
    ops.node(122010, 4.95, 9.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.36, 27304250.14761152, 11376770.89483813, 0.01384148, 0.00528, 0.02673, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 607.65545448, 0.000622, 740.79671392, 0.03929227, 74.07967139, 0.09774465, -607.65545448, -0.000622, -740.79671392, -0.03929227, -74.07967139, -0.09774465, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 217.24351314, 0.00092218, 264.84297881, 0.03108022, 26.48429788, 0.0634901, -217.24351314, -0.00092218, -264.84297881, -0.03108022, -26.48429788, -0.0634901, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 600.62480459, 0.01243998, 600.62480459, 0.03731995, 420.43736321, -9470.14975174, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 150.15620115, 0.00012099, 450.46860344, 0.00036296, 1501.56201148, 0.00120986, -150.15620115, -0.00012099, -450.46860344, -0.00036296, -1501.56201148, -0.00120986, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 288.69700022, 0.01844362, 288.69700022, 0.05533086, 202.08790015, -3215.82475501, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 72.17425005, 5.815e-05, 216.52275016, 0.00017446, 721.74250054, 0.00058153, -72.17425005, -5.815e-05, -216.52275016, -0.00017446, -721.74250054, -0.00058153, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 7.9, 9.3, 3.05)
    ops.node(122011, 7.9, 9.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.36, 25529056.92288116, 10637107.05120048, 0.01384148, 0.00528, 0.02673, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 601.2361198, 0.00065077, 734.78394854, 0.03856563, 73.47839485, 0.09459691, -601.2361198, -0.00065077, -734.78394854, -0.03856563, -73.47839485, -0.09459691, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 213.71607202, 0.00101488, 261.18713446, 0.03058379, 26.11871345, 0.06165125, -213.71607202, -0.00101488, -261.18713446, -0.03058379, -26.11871345, -0.06165125, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 569.10073264, 0.01301537, 569.10073264, 0.03904611, 398.37051285, -9723.44263748, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 142.27518316, 0.00012261, 426.82554948, 0.00036782, 1422.7518316, 0.00122608, -142.27518316, -0.00012261, -426.82554948, -0.00036782, -1422.7518316, -0.00122608, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 272.7295143, 0.02029759, 272.7295143, 0.06089277, 190.91066001, -3281.32269473, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 68.18237858, 5.876e-05, 204.54713573, 0.00017627, 681.82378575, 0.00058757, -68.18237858, -5.876e-05, -204.54713573, -0.00017627, -681.82378575, -0.00058757, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 12.85, 9.3, 3.05)
    ops.node(122012, 12.85, 9.3, 5.2)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.28, 25777876.2481099, 10740781.77004579, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 427.90930449, 0.00068613, 522.59663084, 0.0309702, 52.25966308, 0.08028895, -427.90930449, -0.00068613, -522.59663084, -0.0309702, -52.25966308, -0.08028895, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 158.1034742, 0.00113015, 193.08844673, 0.02491954, 19.30884467, 0.05273865, -158.1034742, -0.00113015, -193.08844673, -0.02491954, -19.30884467, -0.05273865, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 399.89458728, 0.01372259, 399.89458728, 0.04116777, 279.92621109, -5522.9824866, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 99.97364682, 0.0001097, 299.92094046, 0.0003291, 999.7364682, 0.001097, -99.97364682, -0.0001097, -299.92094046, -0.0003291, -999.7364682, -0.001097, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 201.25298888, 0.02260302, 201.25298888, 0.06780906, 140.87709222, -2014.35487495, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 50.31324722, 5.521e-05, 150.93974166, 0.00016562, 503.1324722, 0.00055208, -50.31324722, -5.521e-05, -150.93974166, -0.00016562, -503.1324722, -0.00055208, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 13.95, 3.0)
    ops.node(122013, 0.0, 13.95, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.15, 28011290.64789016, 11671371.10328757, 0.00281737, 0.0034375, 0.0012375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 107.59717872, 0.0010986, 130.93597541, 0.03486603, 13.09359754, 0.083792, -107.59717872, -0.0010986, -130.93597541, -0.03486603, -13.09359754, -0.083792, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 158.41042621, 0.00077002, 192.77107372, 0.04097683, 19.27710737, 0.1149966, -158.41042621, -0.00077002, -192.77107372, -0.04097683, -19.27710737, -0.1149966, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 168.06249354, 0.02197191, 168.06249354, 0.06591573, 117.64374548, -3455.56282334, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 42.01562339, 7.92e-05, 126.04687016, 0.00023759, 420.15623386, 0.00079198, -42.01562339, -7.92e-05, -126.04687016, -0.00023759, -420.15623386, -0.00079198, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 236.9043751, 0.01540048, 236.9043751, 0.04620145, 165.83306257, -7572.18959463, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 59.22609378, 0.00011164, 177.67828133, 0.00033492, 592.26093775, 0.00111638, -59.22609378, -0.00011164, -177.67828133, -0.00033492, -592.26093775, -0.00111638, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 4.95, 13.95, 3.0)
    ops.node(122014, 4.95, 13.95, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2275, 26384825.93716229, 10993677.47381762, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 145.20791559, 0.00097938, 177.22244803, 0.02532264, 17.7222448, 0.06456192, -145.20791559, -0.00097938, -177.22244803, -0.02532264, -17.7222448, -0.06456192, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 220.72358476, 0.00067491, 269.38733932, 0.03046209, 26.93873393, 0.09379599, -220.72358476, -0.00067491, -269.38733932, -0.03046209, -26.93873393, -0.09379599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 202.80289579, 0.01958754, 202.80289579, 0.05876261, 141.96202705, -3118.79721657, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 50.70072395, 6.69e-05, 152.10217184, 0.00020069, 507.00723947, 0.00066897, -50.70072395, -6.69e-05, -152.10217184, -0.00020069, -507.00723947, -0.00066897, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 335.73808445, 0.01349827, 335.73808445, 0.0404948, 235.01665912, -7541.19465799, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 83.93452111, 0.00011075, 251.80356334, 0.00033224, 839.34521113, 0.00110747, -83.93452111, -0.00011075, -251.80356334, -0.00033224, -839.34521113, -0.00110747, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 7.9, 13.95, 3.0)
    ops.node(122015, 7.9, 13.95, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.2275, 25619034.26883273, 10674597.61201364, 0.00616035, 0.00881089, 0.00255464, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 141.25253331, 0.00098297, 172.55601051, 0.02760651, 17.25560105, 0.06605511, -141.25253331, -0.00098297, -172.55601051, -0.02760651, -17.25560105, -0.06605511, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 216.26181338, 0.00067342, 264.1883644, 0.0332508, 26.41883644, 0.09530852, -216.26181338, -0.00067342, -264.1883644, -0.0332508, -26.41883644, -0.09530852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 204.97188284, 0.01965939, 204.97188284, 0.05897817, 143.48031799, -3460.64205665, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 51.24297071, 6.963e-05, 153.72891213, 0.0002089, 512.4297071, 0.00069633, -51.24297071, -6.963e-05, -153.72891213, -0.0002089, -512.4297071, -0.00069633, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 341.40605588, 0.01346834, 341.40605588, 0.04040502, 238.98423912, -8533.37155149, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 85.35151397, 0.00011598, 256.05454191, 0.00034795, 853.51513971, 0.00115982, -85.35151397, -0.00011598, -256.05454191, -0.00034795, -853.51513971, -0.00115982, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 12.85, 13.95, 3.0)
    ops.node(122016, 12.85, 13.95, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.15, 26354583.35465271, 10981076.39777196, 0.00281737, 0.0034375, 0.0012375, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 99.91903056, 0.00122083, 121.9075539, 0.03220249, 12.19075539, 0.07928095, -99.91903056, -0.00122083, -121.9075539, -0.03220249, -12.19075539, -0.07928095, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 152.73808432, 0.00081708, 186.35014914, 0.03770687, 18.63501491, 0.10893156, -152.73808432, -0.00081708, -186.35014914, -0.03770687, -18.63501491, -0.10893156, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 148.91084207, 0.02441658, 148.91084207, 0.07324975, 104.23758945, -2758.08037054, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 37.22771052, 7.458e-05, 111.68313155, 0.00022375, 372.27710517, 0.00074584, -37.22771052, -7.458e-05, -111.68313155, -0.00022375, -372.27710517, -0.00074584, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 208.50175995, 0.0163416, 208.50175995, 0.0490248, 145.95123196, -5863.57523105, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 52.12543999, 0.00010443, 156.37631996, 0.00031329, 521.25439987, 0.00104431, -52.12543999, -0.00010443, -156.37631996, -0.00031329, -521.25439987, -0.00104431, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 5.75)
    ops.node(123001, 0.0, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.1, 26971058.91961571, 11237941.21650655, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 55.13742883, 0.00143689, 67.24208458, 0.02102572, 6.72420846, 0.06019727, -55.13742883, -0.00143689, -67.24208458, -0.02102572, -6.72420846, -0.06019727, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 88.86045452, 0.00094041, 108.3685316, 0.02369001, 10.83685316, 0.07954658, -88.86045452, -0.00094041, -108.3685316, -0.02369001, -10.83685316, -0.07954658, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 80.7193789, 0.02873779, 80.7193789, 0.08621336, 56.50356523, -1261.3001671, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 20.17984472, 5.926e-05, 60.53953417, 0.00017777, 201.79844724, 0.00059258, -20.17984472, -5.926e-05, -60.53953417, -0.00017777, -201.79844724, -0.00059258, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 108.95977604, 0.01880822, 108.95977604, 0.05642466, 76.27184323, -2405.10627273, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 27.23994401, 7.999e-05, 81.71983203, 0.00023997, 272.39944011, 0.0007999, -27.23994401, -7.999e-05, -81.71983203, -0.00023997, -272.39944011, -0.0007999, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 12.85, 0.0, 5.75)
    ops.node(123004, 12.85, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.1, 27469101.87824628, 11445459.11593595, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 54.53240924, 0.00138387, 66.45037896, 0.02472876, 6.6450379, 0.06432225, -54.53240924, -0.00138387, -66.45037896, -0.02472876, -6.6450379, -0.06432225, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 87.73632894, 0.00091217, 106.91096153, 0.02802389, 10.69109615, 0.08448212, -87.73632894, -0.00091217, -106.91096153, -0.02802389, -10.69109615, -0.08448212, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 96.22193629, 0.02767741, 96.22193629, 0.08303223, 67.35535541, -1584.94109873, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 24.05548407, 6.936e-05, 72.16645222, 0.00020807, 240.55484074, 0.00069358, -24.05548407, -6.936e-05, -72.16645222, -0.00020807, -240.55484074, -0.00069358, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 120.88792326, 0.01824348, 120.88792326, 0.05473044, 84.62154628, -3126.6361838, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 30.22198082, 8.714e-05, 90.66594245, 0.00026141, 302.21980815, 0.00087137, -30.22198082, -8.714e-05, -90.66594245, -0.00026141, -302.21980815, -0.00087137, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.65, 5.8)
    ops.node(123005, 0.0, 4.65, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1875, 26253179.92213515, 10938824.96755631, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 244.10033672, 0.00064151, 298.07530048, 0.0363032, 29.80753005, 0.102737, -244.10033672, -0.00064151, -298.07530048, -0.0363032, -29.80753005, -0.102737, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 72.88457335, 0.00133768, 89.00066011, 0.02673247, 8.90006601, 0.05642223, -72.88457335, -0.00133768, -89.00066011, -0.02673247, -8.90006601, -0.05642223, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 296.32165805, 0.01283013, 296.32165805, 0.0384904, 207.42516063, -6365.13730783, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 74.08041451, 0.00011919, 222.24124354, 0.00035757, 740.80414512, 0.00119192, -74.08041451, -0.00011919, -222.24124354, -0.00035757, -740.80414512, -0.00119192, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 139.06164402, 0.02675356, 139.06164402, 0.08026068, 97.34315082, -1458.6331059, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 34.76541101, 5.594e-05, 104.29623302, 0.00016781, 347.65411006, 0.00055936, -34.76541101, -5.594e-05, -104.29623302, -0.00016781, -347.65411006, -0.00055936, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 4.95, 4.65, 5.8)
    ops.node(123006, 4.95, 4.65, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.2975, 28204584.60188689, 11751910.25078621, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 457.1006317, 0.00062837, 556.85567399, 0.03514412, 55.6855674, 0.08923344, -457.1006317, -0.00062837, -556.85567399, -0.03514412, -55.6855674, -0.08923344, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 154.87767513, 0.00101775, 188.67729814, 0.0277256, 18.86772981, 0.05716383, -154.87767513, -0.00101775, -188.67729814, -0.0277256, -18.86772981, -0.05716383, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 501.2220672, 0.01256745, 501.2220672, 0.03770235, 350.85544704, -8904.42435356, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 125.3055168, 0.00011827, 375.9165504, 0.00035482, 1253.05516801, 0.00118274, -125.3055168, -0.00011827, -375.9165504, -0.00035482, -1253.05516801, -0.00118274, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 236.95347659, 0.02035505, 236.95347659, 0.06106514, 165.86743362, -2558.08992971, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 59.23836915, 5.591e-05, 177.71510744, 0.00016774, 592.38369148, 0.00055914, -59.23836915, -5.591e-05, -177.71510744, -0.00016774, -592.38369148, -0.00055914, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 7.9, 4.65, 5.8)
    ops.node(123007, 7.9, 4.65, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.2975, 27532434.52446334, 11471847.71852639, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 459.23083095, 0.00063833, 560.18975868, 0.0327482, 56.01897587, 0.08627985, -459.23083095, -0.00063833, -560.18975868, -0.0327482, -56.01897587, -0.08627985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 155.27478889, 0.00104631, 189.41094685, 0.02589252, 18.94109469, 0.05502724, -155.27478889, -0.00104631, -189.41094685, -0.02589252, -18.94109469, -0.05502724, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 469.34020802, 0.01276655, 469.34020802, 0.03829966, 328.53814561, -7324.32953391, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 117.335052, 0.00011345, 352.00515601, 0.00034036, 1173.35052005, 0.00113454, -117.335052, -0.00011345, -352.00515601, -0.00034036, -1173.35052005, -0.00113454, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 222.77394212, 0.02092618, 222.77394212, 0.06277854, 155.94175948, -2205.41759535, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 55.69348553, 5.385e-05, 167.08045659, 0.00016155, 556.93485529, 0.00053852, -55.69348553, -5.385e-05, -167.08045659, -0.00016155, -556.93485529, -0.00053852, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 12.85, 4.65, 5.8)
    ops.node(123008, 12.85, 4.65, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1875, 27624398.41257858, 11510166.00524108, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 263.59946205, 0.00067511, 321.19516035, 0.03685848, 32.11951604, 0.10529321, -263.59946205, -0.00067511, -321.19516035, -0.03685848, -32.11951604, -0.10529321, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 78.85136897, 0.00143118, 96.08015853, 0.02719745, 9.60801585, 0.05778145, -78.85136897, -0.00143118, -96.08015853, -0.02719745, -9.60801585, -0.05778145, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 324.97573127, 0.01350225, 324.97573127, 0.04050676, 227.48301189, -7680.44189555, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 81.24393282, 0.00012423, 243.73179845, 0.00037269, 812.43932818, 0.00124229, -81.24393282, -0.00012423, -243.73179845, -0.00037269, -812.43932818, -0.00124229, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 151.61112728, 0.02862357, 151.61112728, 0.08587072, 106.12778909, -1665.5237458, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 37.90278182, 5.796e-05, 113.70834546, 0.00017387, 379.02781819, 0.00057957, -37.90278182, -5.796e-05, -113.70834546, -0.00017387, -379.02781819, -0.00057957, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 9.3, 5.8)
    ops.node(123009, 0.0, 9.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1875, 27130705.82017782, 11304460.75840742, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 257.48612595, 0.00067392, 314.02872678, 0.03656127, 31.40287268, 0.10443797, -257.48612595, -0.00067392, -314.02872678, -0.03656127, -31.40287268, -0.10443797, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 76.23420454, 0.0014556, 92.97483544, 0.02701109, 9.29748354, 0.05734569, -76.23420454, -0.0014556, -92.97483544, -0.02701109, -9.29748354, -0.05734569, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 316.98001157, 0.01347834, 316.98001157, 0.04043501, 221.8860081, -7458.47494499, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 79.24500289, 0.00012338, 237.73500868, 0.00037013, 792.45002893, 0.00123377, -79.24500289, -0.00012338, -237.73500868, -0.00037013, -792.45002893, -0.00123377, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 147.78921122, 0.02911208, 147.78921122, 0.08733623, 103.45244786, -1626.17143527, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 36.94730281, 5.752e-05, 110.84190842, 0.00017257, 369.47302806, 0.00057524, -36.94730281, -5.752e-05, -110.84190842, -0.00017257, -369.47302806, -0.00057524, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 4.95, 9.3, 5.8)
    ops.node(123010, 4.95, 9.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.28, 28993110.08850084, 12080462.53687535, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 406.80965084, 0.00064383, 494.75189065, 0.03180572, 49.47518907, 0.08652225, -406.80965084, -0.00064383, -494.75189065, -0.03180572, -49.47518907, -0.08652225, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 150.31518434, 0.00101772, 182.80962975, 0.02549667, 18.28096297, 0.0563605, -150.31518434, -0.00101772, -182.80962975, -0.02549667, -18.28096297, -0.0563605, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 440.34823127, 0.01287666, 440.34823127, 0.03862997, 308.24376189, -6517.2419458, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 110.08705782, 0.0001074, 330.26117345, 0.0003222, 1100.87057817, 0.00107401, -110.08705782, -0.0001074, -330.26117345, -0.0003222, -1100.87057817, -0.00107401, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 222.58118016, 0.02035442, 222.58118016, 0.06106325, 155.80682611, -2130.92623895, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 55.64529504, 5.429e-05, 166.93588512, 0.00016286, 556.45295041, 0.00054288, -55.64529504, -5.429e-05, -166.93588512, -0.00016286, -556.45295041, -0.00054288, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 7.9, 9.3, 5.8)
    ops.node(123011, 7.9, 9.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.28, 27939068.65764095, 11641278.60735039, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 410.30842963, 0.00065706, 500.13280446, 0.03156191, 50.01328045, 0.08547734, -410.30842963, -0.00065706, -500.13280446, -0.03156191, -50.01328045, -0.08547734, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 151.44591608, 0.0010483, 184.60032811, 0.02532534, 18.46003281, 0.05573729, -151.44591608, -0.0010483, -184.60032811, -0.02532534, -18.46003281, -0.05573729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 419.79907923, 0.01314122, 419.79907923, 0.03942366, 293.85935546, -6184.25974781, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 104.94976981, 0.00010625, 314.84930943, 0.00031876, 1049.49769808, 0.00106252, -104.94976981, -0.00010625, -314.84930943, -0.00031876, -1049.49769808, -0.00106252, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 212.01778432, 0.02096601, 212.01778432, 0.06289802, 148.41244902, -2047.36849995, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 53.00444608, 5.366e-05, 159.01333824, 0.00016099, 530.04446079, 0.00053662, -53.00444608, -5.366e-05, -159.01333824, -0.00016099, -530.04446079, -0.00053662, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 12.85, 9.3, 5.8)
    ops.node(123012, 12.85, 9.3, 7.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1875, 26018517.25641327, 10841048.85683887, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 259.91925842, 0.00070607, 317.51112682, 0.03690934, 31.75111268, 0.10309373, -259.91925842, -0.00070607, -317.51112682, -0.03690934, -31.75111268, -0.10309373, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 75.78597937, 0.00161088, 92.57833318, 0.02739133, 9.25783332, 0.05696963, -75.78597937, -0.00161088, -92.57833318, -0.02739133, -9.25783332, -0.05696963, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 305.71485066, 0.01412144, 305.71485066, 0.04236433, 214.00039546, -7357.12906222, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 76.42871266, 0.00012408, 229.28613799, 0.00037224, 764.28712664, 0.00124079, -76.42871266, -0.00012408, -229.28613799, -0.00037224, -764.28712664, -0.00124079, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 141.62350609, 0.03221759, 141.62350609, 0.09665276, 99.13645426, -1610.38195589, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 35.40587652, 5.748e-05, 106.21762957, 0.00017244, 354.05876522, 0.0005748, -35.40587652, -5.748e-05, -106.21762957, -0.00017244, -354.05876522, -0.0005748, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 13.95, 5.75)
    ops.node(123013, 0.0, 13.95, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1, 28488648.32723416, 11870270.13634757, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 58.43525281, 0.00135168, 71.07770169, 0.02465258, 7.10777017, 0.06513808, -58.43525281, -0.00135168, -71.07770169, -0.02465258, -7.10777017, -0.06513808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 92.66991328, 0.0009106, 112.71902036, 0.02797122, 11.27190204, 0.08570143, -92.66991328, -0.0009106, -112.71902036, -0.02797122, -11.27190204, -0.08570143, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 102.31663073, 0.02703356, 102.31663073, 0.08110068, 71.62164151, -1776.1227248, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 25.57915768, 7.111e-05, 76.73747305, 0.00021333, 255.79157682, 0.00071111, -25.57915768, -7.111e-05, -76.73747305, -0.00021333, -255.79157682, -0.00071111, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 128.98684094, 0.01821192, 128.98684094, 0.05463575, 90.29078866, -3566.60583846, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 32.24671024, 8.965e-05, 96.74013071, 0.00026894, 322.46710235, 0.00089648, -32.24671024, -8.965e-05, -96.74013071, -0.00026894, -322.46710235, -0.00089648, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 4.95, 13.95, 5.75)
    ops.node(123014, 4.95, 13.95, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.165, 30761984.08654795, 12817493.36939498, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 93.05605784, 0.00098781, 112.63305873, 0.01910296, 11.26330587, 0.05882422, -93.05605784, -0.00098781, -112.63305873, -0.01910296, -11.26330587, -0.05882422, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 143.14230773, 0.00066467, 173.25638252, 0.02260111, 17.32563825, 0.08514738, -143.14230773, -0.00066467, -173.25638252, -0.02260111, -17.32563825, -0.08514738, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 154.32842054, 0.01975622, 154.32842054, 0.05926867, 108.02989438, -1811.29713954, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 38.58210514, 6.02e-05, 115.74631541, 0.00018061, 385.82105136, 0.00060202, -38.58210514, -6.02e-05, -115.74631541, -0.00018061, -385.82105136, -0.00060202, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 224.92385336, 0.0132935, 224.92385336, 0.03988049, 157.44669735, -4242.38080785, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 56.23096334, 8.774e-05, 168.69289002, 0.00026322, 562.3096334, 0.00087741, -56.23096334, -8.774e-05, -168.69289002, -0.00026322, -562.3096334, -0.00087741, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 7.9, 13.95, 5.75)
    ops.node(123015, 7.9, 13.95, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.165, 27602684.34676113, 11501118.47781714, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 93.18191496, 0.00105836, 113.60843175, 0.023597, 11.36084317, 0.06161516, -93.18191496, -0.00105836, -113.60843175, -0.023597, -11.36084317, -0.06161516, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 143.67053014, 0.00069834, 175.16471543, 0.02799137, 17.51647154, 0.08785589, -143.67053014, -0.00069834, -175.16471543, -0.02799137, -17.51647154, -0.08785589, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 152.01518212, 0.02116726, 152.01518212, 0.06350177, 106.41062748, -2463.95477632, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 38.00379553, 6.609e-05, 114.01138659, 0.00019826, 380.0379553, 0.00066087, -38.00379553, -6.609e-05, -114.01138659, -0.00019826, -380.0379553, -0.00066087, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 229.11874445, 0.01396676, 229.11874445, 0.04190027, 160.38312111, -6101.41408203, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 57.27968611, 9.961e-05, 171.83905833, 0.00029882, 572.79686111, 0.00099607, -57.27968611, -9.961e-05, -171.83905833, -0.00029882, -572.79686111, -0.00099607, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 12.85, 13.95, 5.75)
    ops.node(123016, 12.85, 13.95, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1, 29706044.79564267, 12377518.66485111, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 53.12239075, 0.00138651, 64.44154321, 0.02147518, 6.44415432, 0.06274878, -53.12239075, -0.00138651, -64.44154321, -0.02147518, -6.44415432, -0.06274878, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 86.25524429, 0.00089978, 104.63424129, 0.02422987, 10.46342413, 0.08308385, -86.25524429, -0.00089978, -104.63424129, -0.02422987, -10.46342413, -0.08308385, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 93.54442031, 0.02773014, 93.54442031, 0.08319042, 65.48109422, -1314.62101957, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 23.38610508, 6.235e-05, 70.15831523, 0.00018705, 233.86105077, 0.0006235, -23.38610508, -6.235e-05, -70.15831523, -0.00018705, -233.86105077, -0.0006235, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 118.26026636, 0.01799558, 118.26026636, 0.05398674, 82.78218645, -2530.37952641, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 29.56506659, 7.882e-05, 88.69519977, 0.00023647, 295.65066591, 0.00078824, -29.56506659, -7.882e-05, -88.69519977, -0.00023647, -295.65066591, -0.00078824, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 8.5)
    ops.node(124001, 0.0, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.1, 26935038.34657495, 11222932.64440623, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 61.03737783, 0.00140719, 74.76687013, 0.03286461, 7.47668701, 0.08533495, -61.03737783, -0.00140719, -74.76687013, -0.03286461, -7.47668701, -0.08533495, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 91.72226772, 0.00093636, 112.35389071, 0.03776947, 11.23538907, 0.11405432, -91.72226772, -0.00093636, -112.35389071, -0.03776947, -11.23538907, -0.11405432, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 98.13253215, 0.0281437, 98.13253215, 0.08443111, 68.6927725, -4799.05438005, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 24.53313304, 7.214e-05, 73.59939911, 0.00021641, 245.33133036, 0.00072137, -24.53313304, -7.214e-05, -73.59939911, -0.00021641, -245.33133036, -0.00072137, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 128.72315928, 0.01872729, 128.72315928, 0.05618186, 90.10621149, -11381.82983397, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 32.18078982, 9.462e-05, 96.54236946, 0.00028387, 321.80789819, 0.00094625, -32.18078982, -9.462e-05, -96.54236946, -0.00028387, -321.80789819, -0.00094625, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 12.85, 0.0, 8.5)
    ops.node(124004, 12.85, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.1, 27884144.93644137, 11618393.72351724, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 61.35262546, 0.00135337, 74.99717241, 0.02858306, 7.49971724, 0.08135081, -61.35262546, -0.00135337, -74.99717241, -0.02858306, -7.49971724, -0.08135081, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 91.74687492, 0.00090931, 112.15096574, 0.03279222, 11.21509657, 0.10950946, -91.74687492, -0.00090931, -112.15096574, -0.03279222, -11.21509657, -0.10950946, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 91.84423814, 0.0270674, 91.84423814, 0.08120221, 64.2909667, -3405.84140287, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 22.96105954, 6.522e-05, 68.88317861, 0.00019565, 229.61059535, 0.00065217, -22.96105954, -6.522e-05, -68.88317861, -0.00019565, -229.61059535, -0.00065217, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 117.07942588, 0.01818622, 117.07942588, 0.05455867, 81.95559811, -7960.32728285, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 29.26985647, 8.314e-05, 87.80956941, 0.00024941, 292.69856469, 0.00083136, -29.26985647, -8.314e-05, -87.80956941, -0.00024941, -292.69856469, -0.00083136, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.65, 8.55)
    ops.node(124005, 0.0, 4.65, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1875, 27301843.93728144, 11375768.3072006, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 211.93066573, 0.00065215, 259.38344527, 0.01837503, 25.93834453, 0.06296865, -211.93066573, -0.00065215, -259.38344527, -0.01837503, -25.93834453, -0.06296865, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 60.59065936, 0.00143726, 74.15733784, 0.01501008, 7.41573378, 0.03869283, -60.59065936, -0.00143726, -74.15733784, -0.01501008, -7.41573378, -0.03869283, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 227.84069788, 0.01304301, 227.84069788, 0.03912902, 159.48848852, -5030.38706558, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 56.96017447, 8.813e-05, 170.88052341, 0.00026438, 569.6017447, 0.00088126, -56.96017447, -8.813e-05, -170.88052341, -0.00026438, -569.6017447, -0.00088126, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 90.49595322, 0.02874523, 90.49595322, 0.08623569, 63.34716725, -904.88735932, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 22.6239883, 3.5e-05, 67.87196491, 0.00010501, 226.23988305, 0.00035003, -22.6239883, -3.5e-05, -67.87196491, -0.00010501, -226.23988305, -0.00035003, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 4.95, 4.65, 8.55)
    ops.node(124006, 4.95, 4.65, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.2975, 27340209.43542022, 11391753.93142509, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 406.73184482, 0.00062773, 497.79668733, 0.01793464, 49.77966873, 0.05362087, -406.73184482, -0.00062773, -497.79668733, -0.01793464, -49.77966873, -0.05362087, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 134.6843641, 0.00101709, 164.83939268, 0.01526982, 16.48393927, 0.03778532, -134.6843641, -0.00101709, -164.83939268, -0.01526982, -16.48393927, -0.03778532, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 367.29497733, 0.01255456, 367.29497733, 0.03766368, 257.10648413, -5064.70654818, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 91.82374433, 8.941e-05, 275.471233, 0.00026823, 918.23744334, 0.00089411, -91.82374433, -8.941e-05, -275.471233, -0.00026823, -918.23744334, -0.00089411, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 173.63945198, 0.02034183, 173.63945198, 0.06102548, 121.54761638, -1318.35687, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 43.40986299, 4.227e-05, 130.22958898, 0.00012681, 434.09862994, 0.00042269, -43.40986299, -4.227e-05, -130.22958898, -0.00012681, -434.09862994, -0.00042269, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 7.9, 4.65, 8.55)
    ops.node(124007, 7.9, 4.65, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.2975, 28891551.43561214, 12038146.43150506, 0.00900415, 0.00334068, 0.01970318, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 414.03358515, 0.00062434, 504.8849295, 0.01503521, 50.48849295, 0.05101675, -414.03358515, -0.00062434, -504.8849295, -0.01503521, -50.48849295, -0.05101675, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 137.37239354, 0.00100527, 167.51600284, 0.01287302, 16.75160028, 0.03557484, -137.37239354, -0.00100527, -167.51600284, -0.01287302, -16.75160028, -0.03557484, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 383.48184707, 0.0124868, 383.48184707, 0.03746039, 268.43729295, -4138.4900341, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 95.87046177, 8.834e-05, 287.6113853, 0.00026502, 958.70461767, 0.00088339, -95.87046177, -8.834e-05, -287.6113853, -0.00026502, -958.70461767, -0.00088339, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 168.77025622, 0.02010542, 168.77025622, 0.06031625, 118.13917935, -1121.88173145, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 42.19256406, 3.888e-05, 126.57769217, 0.00011663, 421.92564055, 0.00038878, -42.19256406, -3.888e-05, -126.57769217, -0.00011663, -421.92564055, -0.00038878, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 12.85, 4.65, 8.55)
    ops.node(124008, 12.85, 4.65, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1875, 27751050.16911313, 11562937.57046381, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 223.55402122, 0.00065614, 273.33820001, 0.02027146, 27.33382, 0.06498669, -223.55402122, -0.00065614, -273.33820001, -0.02027146, -27.33382, -0.06498669, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 65.79617659, 0.00137465, 80.44860199, 0.01639677, 8.0448602, 0.04014409, -65.79617659, -0.00137465, -80.44860199, -0.01639677, -8.0448602, -0.04014409, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 239.65875923, 0.0131228, 239.65875923, 0.03936841, 167.76113146, -6036.32394236, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 59.91468981, 9.12e-05, 179.74406942, 0.00027359, 599.14689807, 0.00091196, -59.91468981, -9.12e-05, -179.74406942, -0.00027359, -599.14689807, -0.00091196, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 92.84339955, 0.02749299, 92.84339955, 0.08247898, 64.99037968, -1045.7160325, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 23.21084989, 3.533e-05, 69.63254966, 0.00010599, 232.10849887, 0.00035329, -23.21084989, -3.533e-05, -69.63254966, -0.00010599, -232.10849887, -0.00035329, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 9.3, 8.55)
    ops.node(124009, 0.0, 9.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1875, 30534227.3739001, 12722594.73912504, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 213.11564764, 0.00061815, 258.7038611, 0.01963747, 25.87038611, 0.06497769, -213.11564764, -0.00061815, -258.7038611, -0.01963747, -25.87038611, -0.06497769, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 62.16723295, 0.00127227, 75.46561398, 0.01583795, 7.5465614, 0.0399172, -62.16723295, -0.00127227, -75.46561398, -0.01583795, -7.5465614, -0.0399172, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 263.55148278, 0.01236307, 263.55148278, 0.03708921, 184.48603795, -5798.11506428, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 65.8878707, 9.115e-05, 197.66361209, 0.00027344, 658.87870696, 0.00091147, -65.8878707, -9.115e-05, -197.66361209, -0.00027344, -658.87870696, -0.00091147, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 107.85530356, 0.02544545, 107.85530356, 0.07633635, 75.49871249, -1009.17152635, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 26.96382589, 3.73e-05, 80.89147767, 0.0001119, 269.6382589, 0.00037301, -26.96382589, -3.73e-05, -80.89147767, -0.0001119, -269.6382589, -0.00037301, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 4.95, 9.3, 8.55)
    ops.node(124010, 4.95, 9.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.28, 27787165.49197738, 11577985.62165724, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 351.78442625, 0.00063823, 430.17681283, 0.01790096, 43.01768128, 0.05382303, -351.78442625, -0.00063823, -430.17681283, -0.01790096, -43.01768128, -0.05382303, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 126.97445655, 0.00101299, 155.26971336, 0.0153809, 15.52697134, 0.03862256, -126.97445655, -0.00101299, -155.26971336, -0.0153809, -15.52697134, -0.03862256, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 334.58892325, 0.01276456, 334.58892325, 0.03829369, 234.21224628, -4997.47625799, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 83.64723081, 8.515e-05, 250.94169244, 0.00025544, 836.47230813, 0.00085148, -83.64723081, -8.515e-05, -250.94169244, -0.00025544, -836.47230813, -0.00085148, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 167.31709282, 0.02025986, 167.31709282, 0.06077957, 117.12196497, -1379.40486576, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 41.82927321, 4.258e-05, 125.48781962, 0.00012774, 418.29273205, 0.0004258, -41.82927321, -4.258e-05, -125.48781962, -0.00012774, -418.29273205, -0.0004258, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 7.9, 9.3, 8.55)
    ops.node(124011, 7.9, 9.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.28, 25392268.25933572, 10580111.77472322, 0.00829164, 0.00314417, 0.01642667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 351.86860789, 0.00066318, 432.36365248, 0.01792056, 43.23636525, 0.05331213, -351.86860789, -0.00066318, -432.36365248, -0.01792056, -43.23636525, -0.05331213, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 126.42855277, 0.00107834, 155.35091687, 0.01544179, 15.53509169, 0.03834021, -126.42855277, -0.00107834, -155.35091687, -0.01544179, -15.53509169, -0.03834021, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 299.00815586, 0.01326366, 299.00815586, 0.03979099, 209.3057091, -4826.63174844, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 74.75203896, 8.327e-05, 224.25611689, 0.00024981, 747.52038965, 0.0008327, -74.75203896, -8.327e-05, -224.25611689, -0.00024981, -747.52038965, -0.0008327, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 145.9464876, 0.02156682, 145.9464876, 0.06470045, 102.16254132, -1340.07877195, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 36.4866219, 4.064e-05, 109.4598657, 0.00012193, 364.866219, 0.00040644, -36.4866219, -4.064e-05, -109.4598657, -0.00012193, -364.866219, -0.00040644, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 12.85, 9.3, 8.55)
    ops.node(124012, 12.85, 9.3, 10.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1875, 27042734.91592156, 11267806.21496732, 0.00308678, 0.00107422, 0.00966797, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 208.691607, 0.00063093, 255.56732226, 0.02086345, 25.55673223, 0.06542251, -208.691607, -0.00063093, -255.56732226, -0.02086345, -25.55673223, -0.06542251, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 60.9397667, 0.0013142, 74.62788378, 0.016809, 7.46278838, 0.04047338, -60.9397667, -0.0013142, -74.62788378, -0.016809, -7.46278838, -0.04047338, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 234.11305177, 0.0126186, 234.11305177, 0.03785581, 163.87913624, -6259.40741189, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 58.52826294, 9.142e-05, 175.58478883, 0.00027426, 585.28262942, 0.0009142, -58.52826294, -9.142e-05, -175.58478883, -0.00027426, -585.28262942, -0.0009142, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 89.06417962, 0.02628408, 89.06417962, 0.07885224, 62.34492574, -1073.0743896, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 22.26604491, 3.478e-05, 66.79813472, 0.00010434, 222.66044906, 0.00034779, -22.26604491, -3.478e-05, -66.79813472, -0.00010434, -222.66044906, -0.00034779, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 13.95, 8.5)
    ops.node(124013, 0.0, 13.95, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1, 29380084.67565384, 12241701.9481891, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 56.54653219, 0.00129615, 68.86939138, 0.02837344, 6.88693914, 0.08159932, -56.54653219, -0.00129615, -68.86939138, -0.02837344, -6.88693914, -0.08159932, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 85.97728013, 0.0008633, 104.71381225, 0.03256777, 10.47138122, 0.10995106, -85.97728013, -0.0008633, -104.71381225, -0.03256777, -10.47138122, -0.10995106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 94.36541398, 0.02592293, 94.36541398, 0.07776879, 66.05578978, -3252.29961839, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 23.59135349, 6.36e-05, 70.77406048, 0.00019079, 235.91353494, 0.00063595, -23.59135349, -6.36e-05, -70.77406048, -0.00019079, -235.91353494, -0.00063595, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 118.60020909, 0.01726598, 118.60020909, 0.05179795, 83.02014636, -7596.79688474, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 29.65005227, 7.993e-05, 88.95015682, 0.00023978, 296.50052272, 0.00079928, -29.65005227, -7.993e-05, -88.95015682, -0.00023978, -296.50052272, -0.00079928, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 4.95, 13.95, 8.5)
    ops.node(124014, 4.95, 13.95, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.165, 27212692.94175111, 11338622.05906296, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 61.55449271, 0.00101456, 75.36844948, 0.02264308, 7.53684495, 0.06463019, -61.55449271, -0.00101456, -75.36844948, -0.02264308, -7.53684495, -0.06463019, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 128.44912107, 0.00067821, 157.27545896, 0.02686915, 15.7275459, 0.09298329, -128.44912107, -0.00067821, -157.27545896, -0.02686915, -15.7275459, -0.09298329, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 134.27378633, 0.02029111, 134.27378633, 0.06087332, 93.99165043, -4123.43859603, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 33.56844658, 5.921e-05, 100.70533975, 0.00017763, 335.68446582, 0.00059211, -33.56844658, -5.921e-05, -100.70533975, -0.00017763, -335.68446582, -0.00059211, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 202.66822802, 0.01356411, 202.66822802, 0.04069232, 141.86775962, -12250.47609199, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 50.66705701, 8.937e-05, 152.00117102, 0.00026811, 506.67057006, 0.00089371, -50.66705701, -8.937e-05, -152.00117102, -0.00026811, -506.67057006, -0.00089371, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 7.9, 13.95, 8.5)
    ops.node(124015, 7.9, 13.95, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.165, 24593834.09550582, 10247430.87312743, 0.00326155, 0.00457531, 0.00136125, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 59.78239682, 0.0010589, 73.55649131, 0.02097375, 7.35564913, 0.06220564, -59.78239682, -0.0010589, -73.55649131, -0.02097375, -7.35564913, -0.06220564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 125.25433366, 0.00069614, 154.11341459, 0.02481191, 15.41134146, 0.08973687, -125.25433366, -0.00069614, -154.11341459, -0.02481191, -15.41134146, -0.08973687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 117.21108022, 0.02117797, 117.21108022, 0.06353392, 82.04775615, -3446.12058155, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 29.30277005, 5.719e-05, 87.90831016, 0.00017157, 293.02770054, 0.0005719, -29.30277005, -5.719e-05, -87.90831016, -0.00017157, -293.02770054, -0.0005719, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 177.78453092, 0.01392275, 177.78453092, 0.04176824, 124.44917165, -10116.25216139, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 44.44613273, 8.675e-05, 133.33839819, 0.00026024, 444.46132731, 0.00086746, -44.44613273, -8.675e-05, -133.33839819, -0.00026024, -444.46132731, -0.00086746, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 12.85, 13.95, 8.5)
    ops.node(124016, 12.85, 13.95, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1, 26493722.11040679, 11039050.87933616, 0.00127345, 0.00146667, 0.00057292, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 61.01458434, 0.00142155, 74.81022747, 0.03233405, 7.48102275, 0.08474371, -61.01458434, -0.00142155, -74.81022747, -0.03233405, -7.48102275, -0.08474371, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 91.65236541, 0.00094466, 112.37533417, 0.03713971, 11.23753342, 0.11333634, -91.65236541, -0.00094466, -112.37533417, -0.03713971, -11.23753342, -0.11333634, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 95.34321538, 0.02843108, 95.34321538, 0.08529325, 66.74025076, -4670.53088426, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 23.83580384, 7.125e-05, 71.50741153, 0.00021376, 238.35803844, 0.00071254, -23.83580384, -7.125e-05, -71.50741153, -0.00021376, -238.35803844, -0.00071254, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 125.03727952, 0.01889318, 125.03727952, 0.05667954, 87.52609567, -11079.53266051, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 31.25931988, 9.345e-05, 93.77795964, 0.00028034, 312.5931988, 0.00093446, -31.25931988, -9.345e-05, -93.77795964, -0.00028034, -312.5931988, -0.00093446, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 4.95, 0.0, 0.0)
    ops.node(124017, 4.95, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 170002, 124017, 0.245, 25230855.28809975, 10512856.37004156, 0.00686927, 0.01100458, 0.00275115, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 270.20168097, 0.00090014, 329.23539823, 0.04017831, 32.92353982, 0.08474626, -270.20168097, -0.00090014, -329.23539823, -0.04017831, -32.92353982, -0.08474626, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 416.64090706, 0.00070264, 507.6686957, 0.05083412, 50.76686957, 0.13033429, -416.64090706, -0.00070264, -507.6686957, -0.05083412, -50.76686957, -0.13033429, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 342.16756687, 0.01800278, 342.16756687, 0.05400835, 239.51729681, -10127.81377684, 0.05, 2, 0, 70002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 85.54189172, 5.48e-05, 256.62567515, 0.0001644, 855.41891717, 0.00054799, -85.54189172, -5.48e-05, -256.62567515, -0.0001644, -855.41891717, -0.00054799, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 523.40673395, 0.01405277, 523.40673395, 0.04215831, 366.38471376, -27976.62238368, 0.05, 2, 0, 70002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 130.85168349, 8.383e-05, 392.55505046, 0.00025148, 1308.51683487, 0.00083826, -130.85168349, -8.383e-05, -392.55505046, -0.00025148, -1308.51683487, -0.00083826, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 4.95, 0.0, 1.575)
    ops.node(121002, 4.95, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 174017, 121002, 0.245, 32076504.83906619, 13365210.34961091, 0.00686927, 0.01100458, 0.00275115, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 143.37393532, 0.00081869, 172.60924739, 0.04154358, 17.26092474, 0.11616863, -143.37393532, -0.00081869, -172.60924739, -0.04154358, -17.26092474, -0.11616863, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 325.97630842, 0.00064973, 392.44598496, 0.04587938, 39.2445985, 0.14159104, -325.97630842, -0.00064973, -392.44598496, -0.04587938, -39.2445985, -0.14159104, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 407.76535262, 0.01637388, 407.76535262, 0.04912165, 285.43574684, -9277.45925602, 0.05, 2, 0, 74017, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 101.94133816, 5.137e-05, 305.82401447, 0.0001541, 1019.41338156, 0.00051368, -101.94133816, -5.137e-05, -305.82401447, -0.0001541, -1019.41338156, -0.00051368, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 718.31553991, 0.01299469, 718.31553991, 0.03898407, 502.82087793, -49975.8493022, 0.05, 2, 0, 74017, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 179.57888498, 9.049e-05, 538.73665493, 0.00027147, 1795.78884976, 0.00090489, -179.57888498, -9.049e-05, -538.73665493, -0.00027147, -1795.78884976, -0.00090489, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 7.9, 0.0, 0.0)
    ops.node(124018, 7.9, 0.0, 1.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 170003, 124018, 0.245, 30916043.81580766, 12881684.92325319, 0.00686927, 0.01100458, 0.00275115, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 274.75893453, 0.00080165, 331.72731373, 0.03789062, 33.17273137, 0.08999221, -274.75893453, -0.00080165, -331.72731373, -0.03789062, -33.17273137, -0.08999221, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 426.43640952, 0.00065753, 514.85352005, 0.04799489, 51.485352, 0.14093354, -426.43640952, -0.00065753, -514.85352005, -0.04799489, -51.485352, -0.14093354, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 391.30610645, 0.01603302, 391.30610645, 0.04809906, 273.91427451, -8530.73085552, 0.05, 2, 0, 70003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 97.82652661, 5.114e-05, 293.47957983, 0.00015343, 978.26526612, 0.00051145, -97.82652661, -5.114e-05, -293.47957983, -0.00015343, -978.26526612, -0.00051145, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 570.89848273, 0.01315051, 570.89848273, 0.03945152, 399.62893791, -22714.09744994, 0.05, 2, 0, 70003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 142.72462068, 7.462e-05, 428.17386205, 0.00022385, 1427.24620683, 0.00074618, -142.72462068, -7.462e-05, -428.17386205, -0.00022385, -1427.24620683, -0.00074618, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 7.9, 0.0, 1.575)
    ops.node(121003, 7.9, 0.0, 2.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4044, 174018, 121003, 0.245, 29033909.31000108, 12097462.21250045, 0.00686927, 0.01100458, 0.00275115, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24044, 143.50755804, 0.00079429, 174.09278774, 0.04438874, 17.40927877, 0.11523633, -143.50755804, -0.00079429, -174.09278774, -0.04438874, -17.40927877, -0.11523633, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14044, 326.49596036, 0.00064791, 396.08082459, 0.04906453, 39.60808246, 0.13993135, -326.49596036, -0.00064791, -396.08082459, -0.04906453, -39.60808246, -0.13993135, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24044, 4044, 0.0, 380.19036549, 0.01588572, 380.19036549, 0.04765717, 266.13325584, -10234.31132407, 0.05, 2, 0, 74018, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44044, 95.04759137, 5.291e-05, 285.14277412, 0.00015874, 950.47591372, 0.00052913, -95.04759137, -5.291e-05, -285.14277412, -0.00015874, -950.47591372, -0.00052913, 0.4, 0.3, 0.003, 0.0, 0.0, 24044, 2)
    ops.limitCurve('ThreePoint', 14044, 4044, 0.0, 701.04373041, 0.01295811, 701.04373041, 0.03887432, 490.73061129, -56686.08757215, 0.05, 2, 0, 74018, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34044, 175.2609326, 9.757e-05, 525.78279781, 0.0002927, 1752.60932604, 0.00097568, -175.2609326, -9.757e-05, -525.78279781, -0.0002927, -1752.60932604, -0.00097568, 0.4, 0.3, 0.003, 0.0, 0.0, 14044, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4044, 99999, 'P', 44044, 'Vy', 34044, 'Vz', 24044, 'My', 14044, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4044, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4044, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 4.95, 0.0, 3.0)
    ops.node(124019, 4.95, 0.0, 3.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 171002, 124019, 0.245, 28033352.68480995, 11680563.61867081, 0.00686927, 0.01100458, 0.00275115, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 128.64751813, 0.00079273, 156.5775037, 0.03976103, 15.65775037, 0.09169917, -128.64751813, -0.00079273, -156.5775037, -0.03976103, -15.65775037, -0.09169917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 319.58698328, 0.00064704, 388.97083117, 0.05038304, 38.89708312, 0.14303012, -319.58698328, -0.00064704, -388.97083117, -0.05038304, -38.89708312, -0.14303012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 360.79667374, 0.01585469, 360.79667374, 0.04756406, 252.55767161, -11357.00092682, 0.05, 2, 0, 71002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 90.19916843, 5.201e-05, 270.5975053, 0.00015602, 901.99168434, 0.00052006, -90.19916843, -5.201e-05, -270.5975053, -0.00015602, -901.99168434, -0.00052006, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 545.90378588, 0.01294087, 545.90378588, 0.03882262, 382.13265012, -33843.45779574, 0.05, 2, 0, 71002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 136.47594647, 7.869e-05, 409.42783941, 0.00023606, 1364.7594647, 0.00078688, -136.47594647, -7.869e-05, -409.42783941, -0.00023606, -1364.7594647, -0.00078688, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 4.95, 0.0, 4.325)
    ops.node(122002, 4.95, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 174019, 122002, 0.245, 28825276.99785455, 12010532.0824394, 0.00686927, 0.01100458, 0.00275115, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 133.34763837, 0.0007952, 162.12709818, 0.03814976, 16.21270982, 0.09166685, -133.34763837, -0.0007952, -162.12709818, -0.03814976, -16.21270982, -0.09166685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 306.183735, 0.00064944, 372.26516398, 0.04832579, 37.2265164, 0.14378941, -306.183735, -0.00064944, -372.26516398, -0.04832579, -37.2265164, -0.14378941, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 353.87149946, 0.01590394, 353.87149946, 0.04771183, 247.71004962, -10351.73357708, 0.05, 2, 0, 74019, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 88.46787487, 4.961e-05, 265.4036246, 0.00014882, 884.67874866, 0.00049607, -88.46787487, -4.961e-05, -265.4036246, -0.00014882, -884.67874866, -0.00049607, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 527.83209374, 0.01298878, 527.83209374, 0.03896634, 369.48246562, -30923.80595442, 0.05, 2, 0, 74019, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 131.95802343, 7.399e-05, 395.8740703, 0.00022198, 1319.58023435, 0.00073993, -131.95802343, -7.399e-05, -395.8740703, -0.00022198, -1319.58023435, -0.00073993, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 7.9, 0.0, 3.0)
    ops.node(124020, 7.9, 0.0, 3.925)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 171003, 124020, 0.245, 26061990.11829871, 10859162.54929113, 0.00686927, 0.01100458, 0.00275115, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 131.00021337, 0.0008128, 159.92759803, 0.04005698, 15.9927598, 0.08969849, -131.00021337, -0.0008128, -159.92759803, -0.04005698, -15.9927598, -0.08969849, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 326.84015349, 0.00066169, 399.01279044, 0.0507498, 39.90127904, 0.13930018, -326.84015349, -0.00066169, -399.01279044, -0.0507498, -39.90127904, -0.13930018, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 343.01335527, 0.01625594, 343.01335527, 0.04876782, 240.10934869, -11890.19621093, 0.05, 2, 0, 71003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 85.75333882, 5.318e-05, 257.26001646, 0.00015955, 857.53338819, 0.00053183, -85.75333882, -5.318e-05, -257.26001646, -0.00015955, -857.53338819, -0.00053183, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 527.36136663, 0.01323385, 527.36136663, 0.03970155, 369.15295664, -35687.67044718, 0.05, 2, 0, 71003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 131.84034166, 8.177e-05, 395.52102497, 0.0002453, 1318.40341657, 0.00081765, -131.84034166, -8.177e-05, -395.52102497, -0.0002453, -1318.40341657, -0.00081765, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4048, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 7.9, 0.0, 4.325)
    ops.node(122003, 7.9, 0.0, 5.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4049, 174020, 122003, 0.245, 26715323.71560545, 11131384.88150227, 0.00686927, 0.01100458, 0.00275115, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24049, 139.66607473, 0.00081879, 170.47194596, 0.04014546, 17.0471946, 0.09162763, -139.66607473, -0.00081879, -170.47194596, -0.04014546, -17.0471946, -0.09162763, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14049, 319.18091405, 0.00066878, 389.58202009, 0.05086218, 38.95820201, 0.14269591, -319.18091405, -0.00066878, -389.58202009, -0.05086218, -38.95820201, -0.14269591, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24049, 4049, 0.0, 343.5776143, 0.01637574, 343.5776143, 0.04912721, 240.50433001, -12119.37309298, 0.05, 2, 0, 74020, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44049, 85.89440357, 5.197e-05, 257.68321072, 0.0001559, 858.94403575, 0.00051968, -85.89440357, -5.197e-05, -257.68321072, -0.0001559, -858.94403575, -0.00051968, 0.4, 0.3, 0.003, 0.0, 0.0, 24049, 2)
    ops.limitCurve('ThreePoint', 14049, 4049, 0.0, 525.71037541, 0.01337559, 525.71037541, 0.04012677, 367.99726279, -37071.9475815, 0.05, 2, 0, 74020, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34049, 131.42759385, 7.952e-05, 394.28278156, 0.00023855, 1314.27593852, 0.00079516, -131.42759385, -7.952e-05, -394.28278156, -0.00023855, -1314.27593852, -0.00079516, 0.4, 0.3, 0.003, 0.0, 0.0, 14049, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4049, 99999, 'P', 44049, 'Vy', 34049, 'Vz', 24049, 'My', 14049, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4049, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4049, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 4.95, 0.0, 5.75)
    ops.node(124021, 4.95, 0.0, 6.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4051, 172002, 124021, 0.18, 27702802.19409181, 11542834.24753826, 0.00370786, 0.00594, 0.001485, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24051, 82.74094916, 0.00090212, 100.83858733, 0.02975807, 10.08385873, 0.07338209, -82.74094916, -0.00090212, -100.83858733, -0.02975807, -10.08385873, -0.07338209, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14051, 197.06585469, 0.0006686, 240.16937924, 0.03706083, 24.01693792, 0.11270396, -197.06585469, -0.0006686, -240.16937924, -0.03706083, -24.01693792, -0.11270396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24051, 4051, 0.0, 207.04747218, 0.01804237, 207.04747218, 0.05412712, 144.93323053, -5389.21656629, 0.05, 2, 0, 72002, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 44051, 51.76186805, 4.111e-05, 155.28560414, 0.00012332, 517.61868045, 0.00041106, -51.76186805, -4.111e-05, -155.28560414, -0.00012332, -517.61868045, -0.00041106, 0.4, 0.3, 0.003, 0.0, 0.0, 24051, 2)
    ops.limitCurve('ThreePoint', 14051, 4051, 0.0, 335.73580409, 0.01337194, 335.73580409, 0.04011583, 235.01506286, -15245.26234215, 0.05, 2, 0, 72002, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 34051, 83.93395102, 6.666e-05, 251.80185307, 0.00019997, 839.33951023, 0.00066656, -83.93395102, -6.666e-05, -251.80185307, -0.00019997, -839.33951023, -0.00066656, 0.4, 0.3, 0.003, 0.0, 0.0, 14051, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4051, 99999, 'P', 44051, 'Vy', 34051, 'Vz', 24051, 'My', 14051, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4051, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 4051, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174021, 4.95, 0.0, 7.075)
    ops.node(123002, 4.95, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4052, 174021, 123002, 0.18, 27000677.76734246, 11250282.40305936, 0.00370786, 0.00594, 0.001485, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24052, 101.90653563, 0.00086731, 124.46775567, 0.03250386, 12.44677557, 0.0768047, -101.90653563, -0.00086731, -124.46775567, -0.03250386, -12.44677557, -0.0768047, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14052, 183.90488916, 0.00065999, 224.619831, 0.04055903, 22.4619831, 0.11737574, -183.90488916, -0.00065999, -224.619831, -0.04055903, -22.4619831, -0.11737574, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24052, 4052, 0.0, 201.7911097, 0.01734628, 201.7911097, 0.05203884, 141.25377679, -6228.912401, 0.05, 2, 0, 74021, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44052, 50.44777743, 4.11e-05, 151.34333228, 0.00012331, 504.47777426, 0.00041105, -50.44777743, -4.11e-05, -151.34333228, -0.00012331, -504.47777426, -0.00041105, 0.4, 0.3, 0.003, 0.0, 0.0, 24052, 2)
    ops.limitCurve('ThreePoint', 14052, 4052, 0.0, 330.0269943, 0.01319988, 330.0269943, 0.03959964, 231.01889601, -18676.06436846, 0.05, 2, 0, 74021, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34052, 82.50674857, 6.723e-05, 247.52024572, 0.00020168, 825.06748574, 0.00067226, -82.50674857, -6.723e-05, -247.52024572, -0.00020168, -825.06748574, -0.00067226, 0.4, 0.3, 0.003, 0.0, 0.0, 14052, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4052, 99999, 'P', 44052, 'Vy', 34052, 'Vz', 24052, 'My', 14052, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174021, 74021, 174021, 4052, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4052, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 7.9, 0.0, 5.75)
    ops.node(124022, 7.9, 0.0, 6.675)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4053, 172003, 124022, 0.18, 24943545.87512372, 10393144.11463489, 0.00370786, 0.00594, 0.001485, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24053, 84.71438914, 0.00095177, 103.64778583, 0.03312247, 10.36477858, 0.07410606, -84.71438914, -0.00095177, -103.64778583, -0.03312247, -10.36477858, -0.07410606, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14053, 202.08479057, 0.00069812, 247.25009889, 0.04127082, 24.72500989, 0.11233547, -202.08479057, -0.00069812, -247.25009889, -0.04127082, -24.72500989, -0.11233547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24053, 4053, 0.0, 200.58168605, 0.01903538, 200.58168605, 0.05710613, 140.40718023, -6810.16825843, 0.05, 2, 0, 72003, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 44053, 50.14542151, 4.423e-05, 150.43626454, 0.00013268, 501.45421512, 0.00044228, -50.14542151, -4.423e-05, -150.43626454, -0.00013268, -501.45421512, -0.00044228, 0.4, 0.3, 0.003, 0.0, 0.0, 24053, 2)
    ops.limitCurve('ThreePoint', 14053, 4053, 0.0, 333.60744278, 0.01396236, 333.60744278, 0.04188707, 233.52520995, -20077.9339802, 0.05, 2, 0, 72003, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 34053, 83.4018607, 7.356e-05, 250.20558209, 0.00022068, 834.01860695, 0.0007356, -83.4018607, -7.356e-05, -250.20558209, -0.00022068, -834.01860695, -0.0007356, 0.4, 0.3, 0.003, 0.0, 0.0, 14053, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4053, 99999, 'P', 44053, 'Vy', 34053, 'Vz', 24053, 'My', 14053, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4053, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 4053, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174022, 7.9, 0.0, 7.075)
    ops.node(123003, 7.9, 0.0, 8.0)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4054, 174022, 123003, 0.18, 31353794.47060417, 13064081.02941841, 0.00370786, 0.00594, 0.001485, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24054, 94.61607753, 0.00087575, 114.37962327, 0.02928264, 11.43796233, 0.07597031, -94.61607753, -0.00087575, -114.37962327, -0.02928264, -11.43796233, -0.07597031, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14054, 179.84349047, 0.00064588, 217.40946387, 0.03647178, 21.74094639, 0.11742719, -179.84349047, -0.00064588, -217.40946387, -0.03647178, -21.74094639, -0.11742719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24054, 4054, 0.0, 230.34669322, 0.01751494, 230.34669322, 0.05254481, 161.24268525, -5812.82021963, 0.05, 2, 0, 74022, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44054, 57.58667331, 4.041e-05, 172.76001992, 0.00012122, 575.86673305, 0.00040407, -57.58667331, -4.041e-05, -172.76001992, -0.00012122, -575.86673305, -0.00040407, 0.4, 0.3, 0.003, 0.0, 0.0, 24054, 2)
    ops.limitCurve('ThreePoint', 14054, 4054, 0.0, 369.02251214, 0.01291767, 369.02251214, 0.03875302, 258.3157585, -17238.95121457, 0.05, 2, 0, 74022, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34054, 92.25562803, 6.473e-05, 276.7668841, 0.0001942, 922.55628035, 0.00064733, -92.25562803, -6.473e-05, -276.7668841, -0.0001942, -922.55628035, -0.00064733, 0.4, 0.3, 0.003, 0.0, 0.0, 14054, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4054, 99999, 'P', 44054, 'Vy', 34054, 'Vz', 24054, 'My', 14054, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174022, 74022, 174022, 4054, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4054, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 4.95, 0.0, 8.5)
    ops.node(124023, 4.95, 0.0, 9.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4056, 173002, 124023, 0.18, 27359386.6769002, 11399744.44870842, 0.00370786, 0.00594, 0.001485, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24056, 67.14963773, 0.00088812, 82.15819652, 0.02631376, 8.21581965, 0.06543607, -67.14963773, -0.00088812, -82.15819652, -0.02631376, -8.21581965, -0.06543607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14056, 163.59175147, 0.00065294, 200.15600563, 0.03221545, 20.01560056, 0.09755303, -163.59175147, -0.00065294, -200.15600563, -0.03221545, -20.01560056, -0.09755303, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24056, 4056, 0.0, 178.76275888, 0.01776232, 178.76275888, 0.05328697, 125.13393122, -6632.8072892, 0.05, 2, 0, 73002, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 44056, 44.69068972, 3.594e-05, 134.07206916, 0.00010781, 446.9068972, 0.00035936, -44.69068972, -3.594e-05, -134.07206916, -0.00010781, -446.9068972, -0.00035936, 0.4, 0.3, 0.003, 0.0, 0.0, 24056, 2)
    ops.limitCurve('ThreePoint', 14056, 4056, 0.0, 287.95262885, 0.01305885, 287.95262885, 0.03917656, 201.56684019, -22122.66965024, 0.05, 2, 0, 73002, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 34056, 71.98815721, 5.789e-05, 215.96447164, 0.00017366, 719.88157212, 0.00057887, -71.98815721, -5.789e-05, -215.96447164, -0.00017366, -719.88157212, -0.00057887, 0.4, 0.3, 0.003, 0.0, 0.0, 14056, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4056, 99999, 'P', 44056, 'Vy', 34056, 'Vz', 24056, 'My', 14056, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4056, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 4056, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174023, 4.95, 0.0, 9.825)
    ops.node(124002, 4.95, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4057, 174023, 124002, 0.18, 27619262.23555664, 11508025.93148193, 0.00370786, 0.00594, 0.001485, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24057, 66.80736241, 0.00090362, 81.76625526, 0.03404989, 8.17662553, 0.08325869, -66.80736241, -0.00090362, -81.76625526, -0.03404989, -8.17662553, -0.08325869, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14057, 164.04507752, 0.00066374, 200.77654918, 0.04246679, 20.07765492, 0.1277938, -164.04507752, -0.00066374, -200.77654918, -0.04246679, -20.07765492, -0.1277938, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24057, 4057, 0.0, 197.92369191, 0.01807239, 197.92369191, 0.05421716, 138.54658434, -19313.88054643, 0.05, 2, 0, 74023, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44057, 49.48092298, 3.941e-05, 148.44276893, 0.00011824, 494.80922978, 0.00039414, -49.48092298, -3.941e-05, -148.44276893, -0.00011824, -494.80922978, -0.00039414, 0.4, 0.3, 0.003, 0.0, 0.0, 24057, 2)
    ops.limitCurve('ThreePoint', 14057, 4057, 0.0, 327.45624921, 0.01327477, 327.45624921, 0.03982431, 229.21937445, -71697.05826601, 0.05, 2, 0, 74023, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34057, 81.8640623, 6.521e-05, 245.59218691, 0.00019563, 818.64062303, 0.00065208, -81.8640623, -6.521e-05, -245.59218691, -0.00019563, -818.64062303, -0.00065208, 0.4, 0.3, 0.003, 0.0, 0.0, 14057, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4057, 99999, 'P', 44057, 'Vy', 34057, 'Vz', 24057, 'My', 14057, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174023, 74023, 174023, 4057, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4057, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 7.9, 0.0, 8.5)
    ops.node(124024, 7.9, 0.0, 9.425)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4058, 173003, 124024, 0.18, 26854748.06555718, 11189478.36064883, 0.00370786, 0.00594, 0.001485, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24058, 70.12697711, 0.00087694, 85.89123508, 0.02460092, 8.58912351, 0.06358056, -70.12697711, -0.00087694, -85.89123508, -0.02460092, -8.58912351, -0.06358056, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14058, 170.7355597, 0.00065761, 209.11621605, 0.03010774, 20.9116216, 0.09520706, -170.7355597, -0.00065761, -209.11621605, -0.03010774, -20.9116216, -0.09520706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24058, 4058, 0.0, 170.56866786, 0.01753873, 170.56866786, 0.0526162, 119.3980675, -5749.24222304, 0.05, 2, 0, 73003, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 44058, 42.64216696, 3.493e-05, 127.92650089, 0.0001048, 426.42166964, 0.00034933, -42.64216696, -3.493e-05, -127.92650089, -0.0001048, -426.42166964, -0.00034933, 0.4, 0.3, 0.003, 0.0, 0.0, 24058, 2)
    ops.limitCurve('ThreePoint', 14058, 4058, 0.0, 273.552024, 0.01315225, 273.552024, 0.03945674, 191.4864168, -18906.34135219, 0.05, 2, 0, 73003, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 34058, 68.388006, 5.602e-05, 205.164018, 0.00016807, 683.88005999, 0.00056025, -68.388006, -5.602e-05, -205.164018, -0.00016807, -683.88005999, -0.00056025, 0.4, 0.3, 0.003, 0.0, 0.0, 14058, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4058, 99999, 'P', 44058, 'Vy', 34058, 'Vz', 24058, 'My', 14058, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4058, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 4058, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174024, 7.9, 0.0, 9.825)
    ops.node(124003, 7.9, 0.0, 10.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4059, 174024, 124003, 0.18, 26556215.30374904, 11065089.70989543, 0.00370786, 0.00594, 0.001485, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24059, 66.044691, 0.00085718, 81.02172428, 0.03626713, 8.10217243, 0.08527919, -66.044691, -0.00085718, -81.02172428, -0.03626713, -8.10217243, -0.08527919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14059, 161.89594983, 0.000649, 198.60928732, 0.04530695, 19.86092873, 0.1302928, -161.89594983, -0.000649, -198.60928732, -0.04530695, -19.86092873, -0.1302928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24059, 4059, 0.0, 198.82445248, 0.01714354, 198.82445248, 0.05143061, 139.17711674, -23319.5853434, 0.05, 2, 0, 74024, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44059, 49.70611312, 4.118e-05, 149.11833936, 0.00012353, 497.0611312, 0.00041178, -49.70611312, -4.118e-05, -149.11833936, -0.00012353, -497.0611312, -0.00041178, 0.4, 0.3, 0.003, 0.0, 0.0, 24059, 2)
    ops.limitCurve('ThreePoint', 14059, 4059, 0.0, 333.43524706, 0.01298002, 333.43524706, 0.03894007, 233.40467294, -87160.35069579, 0.05, 2, 0, 74024, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34059, 83.35881177, 6.906e-05, 250.0764353, 0.00020717, 833.58811766, 0.00069057, -83.35881177, -6.906e-05, -250.0764353, -0.00020717, -833.58811766, -0.00069057, 0.4, 0.3, 0.003, 0.0, 0.0, 14059, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4059, 99999, 'P', 44059, 'Vy', 34059, 'Vz', 24059, 'My', 14059, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174024, 74024, 174024, 4059, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4059, '-orient', 0, 0, 1, 0, 1, 0)
