import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.16, 26164800.56154356, 10902000.23397648, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 140.03084446, 0.00086349, 170.12825331, 0.01882951, 17.01282533, 0.05200826, -140.03084446, -0.00086349, -170.12825331, -0.01882951, -17.01282533, -0.05200826, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 127.50586515, 0.00086349, 154.91122838, 0.01882951, 15.49112284, 0.05200826, -127.50586515, -0.00086349, -154.91122838, -0.01882951, -15.49112284, -0.05200826, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 157.5376586, 0.01726972, 157.5376586, 0.05180916, 110.27636102, -2059.98559359, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 39.38441465, 8.128e-05, 118.15324395, 0.00024385, 393.8441465, 0.00081283, -39.38441465, -8.128e-05, -118.15324395, -0.00024385, -393.8441465, -0.00081283, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 157.5376586, 0.01726972, 157.5376586, 0.05180916, 110.27636102, -2059.98559359, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 39.38441465, 8.128e-05, 118.15324395, 0.00024385, 393.8441465, 0.00081283, -39.38441465, -8.128e-05, -118.15324395, -0.00024385, -393.8441465, -0.00081283, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 16.25, 0.0, 0.0)
    ops.node(121004, 16.25, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.16, 27840449.32158704, 11600187.21732793, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 138.62475102, 0.00085459, 168.13596691, 0.01949607, 16.81359669, 0.05489884, -138.62475102, -0.00085459, -168.13596691, -0.01949607, -16.81359669, -0.05489884, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 126.7492503, 0.00085459, 153.73234287, 0.01949607, 15.37323429, 0.05489884, -126.7492503, -0.00085459, -153.73234287, -0.01949607, -15.37323429, -0.05489884, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 168.05587335, 0.01709174, 168.05587335, 0.05127522, 117.63911134, -2157.73173253, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 42.01396834, 8.149e-05, 126.04190501, 0.00024447, 420.13968337, 0.00081491, -42.01396834, -8.149e-05, -126.04190501, -0.00024447, -420.13968337, -0.00081491, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 168.05587335, 0.01709174, 168.05587335, 0.05127522, 117.63911134, -2157.73173253, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 42.01396834, 8.149e-05, 126.04190501, 0.00024447, 420.13968337, 0.00081491, -42.01396834, -8.149e-05, -126.04190501, -0.00024447, -420.13968337, -0.00081491, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.95, 0.0)
    ops.node(121005, 0.0, 3.95, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.25, 27601235.31822017, 11500514.71592507, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 291.71153214, 0.00079615, 353.62491126, 0.02265119, 35.36249113, 0.0613852, -291.71153214, -0.00079615, -353.62491126, -0.02265119, -35.36249113, -0.0613852, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 291.71153214, 0.00079615, 353.62491126, 0.02265119, 35.36249113, 0.0613852, -291.71153214, -0.00079615, -353.62491126, -0.02265119, -35.36249113, -0.0613852, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 290.10322805, 0.01592298, 290.10322805, 0.04776894, 203.07225963, -3900.17838876, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 72.52580701, 9.081e-05, 217.57742103, 0.00027243, 725.25807011, 0.00090811, -72.52580701, -9.081e-05, -217.57742103, -0.00027243, -725.25807011, -0.00090811, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 290.10322805, 0.01592298, 290.10322805, 0.04776894, 203.07225963, -3900.17838876, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 72.52580701, 9.081e-05, 217.57742103, 0.00027243, 725.25807011, 0.00090811, -72.52580701, -9.081e-05, -217.57742103, -0.00027243, -725.25807011, -0.00090811, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 6.7, 3.95, 0.0)
    ops.node(121006, 6.7, 3.95, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.25, 27569694.28155567, 11487372.61731486, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 413.86921533, 0.00079736, 501.08011032, 0.03035046, 50.10801103, 0.0710368, -413.86921533, -0.00079736, -501.08011032, -0.03035046, -50.10801103, -0.0710368, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 413.86921533, 0.00079736, 501.08011032, 0.03035046, 50.10801103, 0.0710368, -413.86921533, -0.00079736, -501.08011032, -0.03035046, -50.10801103, -0.0710368, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 313.45769884, 0.01594713, 313.45769884, 0.0478414, 219.42038919, -4521.62791147, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 78.36442471, 9.823e-05, 235.09327413, 0.0002947, 783.6442471, 0.00098234, -78.36442471, -9.823e-05, -235.09327413, -0.0002947, -783.6442471, -0.00098234, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 313.45769884, 0.01594713, 313.45769884, 0.0478414, 219.42038919, -4521.62791147, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 78.36442471, 9.823e-05, 235.09327413, 0.0002947, 783.6442471, 0.00098234, -78.36442471, -9.823e-05, -235.09327413, -0.0002947, -783.6442471, -0.00098234, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 9.55, 3.95, 0.0)
    ops.node(121007, 9.55, 3.95, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.25, 27373518.03730932, 11405632.51554555, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 410.88219264, 0.00080866, 497.55501527, 0.03045022, 49.75550153, 0.07078987, -410.88219264, -0.00080866, -497.55501527, -0.03045022, -49.75550153, -0.07078987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 410.88219264, 0.00080866, 497.55501527, 0.03045022, 49.75550153, 0.07078987, -410.88219264, -0.00080866, -497.55501527, -0.03045022, -49.75550153, -0.07078987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 311.46057687, 0.01617327, 311.46057687, 0.04851982, 218.02240381, -4504.7223947, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 77.86514422, 9.831e-05, 233.59543265, 0.00029492, 778.65144218, 0.00098307, -77.86514422, -9.831e-05, -233.59543265, -0.00029492, -778.65144218, -0.00098307, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 311.46057687, 0.01617327, 311.46057687, 0.04851982, 218.02240381, -4504.7223947, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 77.86514422, 9.831e-05, 233.59543265, 0.00029492, 778.65144218, 0.00098307, -77.86514422, -9.831e-05, -233.59543265, -0.00029492, -778.65144218, -0.00098307, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 16.25, 3.95, 0.0)
    ops.node(121008, 16.25, 3.95, 2.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.25, 27058245.626104, 11274269.01087667, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 291.57326415, 0.00080784, 353.6561569, 0.02289001, 35.36561569, 0.06079614, -291.57326415, -0.00080784, -353.6561569, -0.02289001, -35.36561569, -0.06079614, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 291.57326415, 0.00080784, 353.6561569, 0.02289001, 35.36561569, 0.06079614, -291.57326415, -0.00080784, -353.6561569, -0.02289001, -35.36561569, -0.06079614, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 290.1305482, 0.0161568, 290.1305482, 0.04847041, 203.09138374, -4053.8502962, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 72.53263705, 9.264e-05, 217.59791115, 0.00027793, 725.3263705, 0.00092642, -72.53263705, -9.264e-05, -217.59791115, -0.00027793, -725.3263705, -0.00092642, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 290.1305482, 0.0161568, 290.1305482, 0.04847041, 203.09138374, -4053.8502962, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 72.53263705, 9.264e-05, 217.59791115, 0.00027793, 725.3263705, 0.00092642, -72.53263705, -9.264e-05, -217.59791115, -0.00027793, -725.3263705, -0.00092642, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.9, 0.0)
    ops.node(121009, 0.0, 7.9, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 27990151.46102585, 11662563.10876077, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 140.29864807, 0.00086135, 170.13131075, 0.01899598, 17.01313108, 0.05457622, -140.29864807, -0.00086135, -170.13131075, -0.01899598, -17.01313108, -0.05457622, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 128.18324613, 0.00086135, 155.4397279, 0.01899598, 15.54397279, 0.05457622, -128.18324613, -0.00086135, -155.4397279, -0.01899598, -15.54397279, -0.05457622, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 166.36053897, 0.01722702, 166.36053897, 0.05168107, 116.45237728, -2075.00635963, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 41.59013474, 8.024e-05, 124.77040423, 0.00024071, 415.90134743, 0.00080238, -41.59013474, -8.024e-05, -124.77040423, -0.00024071, -415.90134743, -0.00080238, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 166.36053897, 0.01722702, 166.36053897, 0.05168107, 116.45237728, -2075.00635963, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 41.59013474, 8.024e-05, 124.77040423, 0.00024071, 415.90134743, 0.00080238, -41.59013474, -8.024e-05, -124.77040423, -0.00024071, -415.90134743, -0.00080238, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 6.7, 7.9, 0.0)
    ops.node(121010, 6.7, 7.9, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.2025, 27302653.53285908, 11376105.63869128, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 184.41472456, 0.000806, 223.7771267, 0.02215638, 22.37771267, 0.05939886, -184.41472456, -0.000806, -223.7771267, -0.02215638, -22.37771267, -0.05939886, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 192.54308035, 0.000806, 233.64043944, 0.02215638, 23.36404394, 0.05939886, -192.54308035, -0.000806, -233.64043944, -0.02215638, -23.36404394, -0.05939886, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 217.88857081, 0.01612007, 217.88857081, 0.0483602, 152.52199956, -3001.11561088, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 54.4721427, 8.513e-05, 163.41642811, 0.00025538, 544.72142702, 0.00085125, -54.4721427, -8.513e-05, -163.41642811, -0.00025538, -544.72142702, -0.00085125, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 217.88857081, 0.01612007, 217.88857081, 0.0483602, 152.52199956, -3001.11561088, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 54.4721427, 8.513e-05, 163.41642811, 0.00025538, 544.72142702, 0.00085125, -54.4721427, -8.513e-05, -163.41642811, -0.00025538, -544.72142702, -0.00085125, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 9.55, 7.9, 0.0)
    ops.node(121011, 9.55, 7.9, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 27223283.14499593, 11343034.6437483, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 186.62749728, 0.00081031, 226.48180743, 0.02220519, 22.64818074, 0.05933624, -186.62749728, -0.00081031, -226.48180743, -0.02220519, -22.64818074, -0.05933624, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 195.00950853, 0.00081031, 236.65379755, 0.02220519, 23.66537975, 0.05933624, -195.00950853, -0.00081031, -236.65379755, -0.02220519, -23.66537975, -0.05933624, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 219.86359489, 0.01620629, 219.86359489, 0.04861887, 153.90451642, -3090.05320473, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 54.96589872, 8.615e-05, 164.89769617, 0.00025844, 549.65898722, 0.00086147, -54.96589872, -8.615e-05, -164.89769617, -0.00025844, -549.65898722, -0.00086147, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 219.86359489, 0.01620629, 219.86359489, 0.04861887, 153.90451642, -3090.05320473, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 54.96589872, 8.615e-05, 164.89769617, 0.00025844, 549.65898722, 0.00086147, -54.96589872, -8.615e-05, -164.89769617, -0.00025844, -549.65898722, -0.00086147, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 16.25, 7.9, 0.0)
    ops.node(121012, 16.25, 7.9, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 27994260.73399261, 11664275.30583026, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 139.4713896, 0.00084257, 169.12717396, 0.01940157, 16.9127174, 0.05498663, -139.4713896, -0.00084257, -169.12717396, -0.01940157, -16.9127174, -0.05498663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 127.25140718, 0.00084257, 154.30885819, 0.01940157, 15.43088582, 0.05498663, -127.25140718, -0.00084257, -154.30885819, -0.01940157, -15.43088582, -0.05498663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 169.61829345, 0.01685143, 169.61829345, 0.05055429, 118.73280541, -2187.26324505, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 42.40457336, 8.18e-05, 127.21372009, 0.00024539, 424.04573362, 0.00081797, -42.40457336, -8.18e-05, -127.21372009, -0.00024539, -424.04573362, -0.00081797, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 169.61829345, 0.01685143, 169.61829345, 0.05055429, 118.73280541, -2187.26324505, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 42.40457336, 8.18e-05, 127.21372009, 0.00024539, 424.04573362, 0.00081797, -42.40457336, -8.18e-05, -127.21372009, -0.00024539, -424.04573362, -0.00081797, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.35)
    ops.node(122001, 0.0, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.16, 27797306.29059401, 11582210.95441417, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 157.86966141, 0.00085061, 191.9987263, 0.03143098, 19.19987263, 0.08781562, -157.86966141, -0.00085061, -191.9987263, -0.03143098, -19.19987263, -0.08781562, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 133.30907868, 0.00085061, 162.1285121, 0.03143098, 16.21285121, 0.08781562, -133.30907868, -0.00085061, -162.1285121, -0.03143098, -16.21285121, -0.08781562, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 207.34564998, 0.01701217, 207.34564998, 0.0510365, 145.14195499, -4640.43811556, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 51.8364125, 0.0001007, 155.50923749, 0.0003021, 518.36412496, 0.00100699, -51.8364125, -0.0001007, -155.50923749, -0.0003021, -518.36412496, -0.00100699, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 207.34564998, 0.01701217, 207.34564998, 0.0510365, 145.14195499, -4640.43811556, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 51.8364125, 0.0001007, 155.50923749, 0.0003021, 518.36412496, 0.00100699, -51.8364125, -0.0001007, -155.50923749, -0.0003021, -518.36412496, -0.00100699, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 16.25, 0.0, 3.35)
    ops.node(122004, 16.25, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.16, 26832014.25445624, 11180005.93935677, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 156.66596077, 0.00088092, 190.80712203, 0.03146114, 19.0807122, 0.08642283, -156.66596077, -0.00088092, -190.80712203, -0.03146114, -19.0807122, -0.08642283, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 132.91158535, 0.00088092, 161.87611503, 0.03146114, 16.1876115, 0.08642283, -132.91158535, -0.00088092, -161.87611503, -0.03146114, -16.1876115, -0.08642283, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 201.24949666, 0.01761831, 201.24949666, 0.05285492, 140.87464766, -4537.72222219, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 50.31237416, 0.00010125, 150.93712249, 0.00030376, 503.12374164, 0.00101255, -50.31237416, -0.00010125, -150.93712249, -0.00030376, -503.12374164, -0.00101255, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 201.24949666, 0.01761831, 201.24949666, 0.05285492, 140.87464766, -4537.72222219, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 50.31237416, 0.00010125, 150.93712249, 0.00030376, 503.12374164, 0.00101255, -50.31237416, -0.00010125, -150.93712249, -0.00030376, -503.12374164, -0.00101255, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.95, 3.375)
    ops.node(122005, 0.0, 3.95, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.25, 27764742.8153908, 11568642.83974617, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 326.56497834, 0.00078538, 396.93458305, 0.03352002, 39.69345831, 0.09178489, -326.56497834, -0.00078538, -396.93458305, -0.03352002, -39.69345831, -0.09178489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 301.02928918, 0.00078538, 365.89635544, 0.03352002, 36.58963554, 0.09178489, -301.02928918, -0.00078538, -365.89635544, -0.03352002, -36.58963554, -0.09178489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 349.56072039, 0.0157077, 349.56072039, 0.04712309, 244.69250427, -7752.54814911, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 87.3901801, 0.00010878, 262.17054029, 0.00032634, 873.90180097, 0.00108778, -87.3901801, -0.00010878, -262.17054029, -0.00032634, -873.90180097, -0.00108778, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 349.56072039, 0.0157077, 349.56072039, 0.04712309, 244.69250427, -7752.54814911, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 87.3901801, 0.00010878, 262.17054029, 0.00032634, 873.90180097, 0.00108778, -87.3901801, -0.00010878, -262.17054029, -0.00032634, -873.90180097, -0.00108778, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 6.7, 3.95, 3.375)
    ops.node(122006, 6.7, 3.95, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.25, 26998694.20683129, 11249455.91951304, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 251.43368933, 0.00076542, 305.60161023, 0.02952503, 30.56016102, 0.07340981, -251.43368933, -0.00076542, -305.60161023, -0.02952503, -30.56016102, -0.07340981, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 234.77410506, 0.00076542, 285.35294827, 0.02952503, 28.53529483, 0.07340981, -234.77410506, -0.00076542, -285.35294827, -0.02952503, -28.53529483, -0.07340981, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 292.6325163, 0.01530833, 292.6325163, 0.045925, 204.84276141, -4628.34677911, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 73.15812908, 9.365e-05, 219.47438723, 0.00028094, 731.58129076, 0.00093647, -73.15812908, -9.365e-05, -219.47438723, -0.00028094, -731.58129076, -0.00093647, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 292.6325163, 0.01530833, 292.6325163, 0.045925, 204.84276141, -4628.34677911, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 73.15812908, 9.365e-05, 219.47438723, 0.00028094, 731.58129076, 0.00093647, -73.15812908, -9.365e-05, -219.47438723, -0.00028094, -731.58129076, -0.00093647, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 9.55, 3.95, 3.375)
    ops.node(122007, 9.55, 3.95, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.25, 28401895.65062046, 11834123.18775853, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 247.5282002, 0.00074624, 300.26075249, 0.02994949, 30.02607525, 0.07578281, -247.5282002, -0.00074624, -300.26075249, -0.02994949, -30.02607525, -0.07578281, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 231.55610212, 0.00074624, 280.88601384, 0.02994949, 28.08860138, 0.07578281, -231.55610212, -0.00074624, -280.88601384, -0.02994949, -28.08860138, -0.07578281, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 310.1724934, 0.0149249, 310.1724934, 0.04477469, 217.12074538, -4923.74319033, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 77.54312335, 9.436e-05, 232.62937005, 0.00028307, 775.4312335, 0.00094356, -77.54312335, -9.436e-05, -232.62937005, -0.00028307, -775.4312335, -0.00094356, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 310.1724934, 0.0149249, 310.1724934, 0.04477469, 217.12074538, -4923.74319033, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 77.54312335, 9.436e-05, 232.62937005, 0.00028307, 775.4312335, 0.00094356, -77.54312335, -9.436e-05, -232.62937005, -0.00028307, -775.4312335, -0.00094356, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 16.25, 3.95, 3.375)
    ops.node(122008, 16.25, 3.95, 5.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.25, 28627128.22616072, 11927970.09423363, 0.00880208, 0.00572917, 0.00572917, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 328.67655197, 0.00079352, 398.91411417, 0.03323076, 39.89141142, 0.09277461, -328.67655197, -0.00079352, -398.91411417, -0.03323076, -39.89141142, -0.09277461, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 303.46085334, 0.00079352, 368.30986807, 0.03323076, 36.83098681, 0.09277461, -303.46085334, -0.00079352, -368.30986807, -0.03323076, -36.83098681, -0.09277461, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 352.93330952, 0.01587045, 352.93330952, 0.04761135, 247.05331666, -7556.89924601, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 88.23332738, 0.00010652, 264.69998214, 0.00031956, 882.3332738, 0.00106519, -88.23332738, -0.00010652, -264.69998214, -0.00031956, -882.3332738, -0.00106519, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 352.93330952, 0.01587045, 352.93330952, 0.04761135, 247.05331666, -7556.89924601, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 88.23332738, 0.00010652, 264.69998214, 0.00031956, 882.3332738, 0.00106519, -88.23332738, -0.00010652, -264.69998214, -0.00031956, -882.3332738, -0.00106519, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.9, 3.35)
    ops.node(122009, 0.0, 7.9, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 27724384.06680581, 11551826.69450242, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 158.34170628, 0.00086445, 192.59573425, 0.03182211, 19.25957342, 0.08810548, -158.34170628, -0.00086445, -192.59573425, -0.03182211, -19.25957342, -0.08810548, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 133.9796234, 0.00086445, 162.96340711, 0.03182211, 16.29634071, 0.08810548, -133.9796234, -0.00086445, -162.96340711, -0.03182211, -16.29634071, -0.08810548, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 208.44998578, 0.01728898, 208.44998578, 0.05186695, 145.91499005, -4727.53463385, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 52.11249645, 0.0001015, 156.33748934, 0.00030451, 521.12496445, 0.00101502, -52.11249645, -0.0001015, -156.33748934, -0.00030451, -521.12496445, -0.00101502, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 208.44998578, 0.01728898, 208.44998578, 0.05186695, 145.91499005, -4727.53463385, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 52.11249645, 0.0001015, 156.33748934, 0.00030451, 521.12496445, 0.00101502, -52.11249645, -0.0001015, -156.33748934, -0.00030451, -521.12496445, -0.00101502, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 6.7, 7.9, 3.35)
    ops.node(122010, 6.7, 7.9, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.2025, 28599797.08678026, 11916582.11949178, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 183.07277479, 0.00078017, 222.3031743, 0.02299146, 22.23031743, 0.06487071, -183.07277479, -0.00078017, -222.3031743, -0.02299146, -22.23031743, -0.06487071, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 159.40130807, 0.00078017, 193.5591833, 0.02299146, 19.35591833, 0.06487071, -159.40130807, -0.00078017, -193.5591833, -0.02299146, -19.35591833, -0.06487071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 218.43868116, 0.01560341, 218.43868116, 0.04681023, 152.90707681, -3263.84388174, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 54.60967029, 8.147e-05, 163.82901087, 0.00024441, 546.0967029, 0.0008147, -54.60967029, -8.147e-05, -163.82901087, -0.00024441, -546.0967029, -0.0008147, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 218.43868116, 0.01560341, 218.43868116, 0.04681023, 152.90707681, -3263.84388174, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 54.60967029, 8.147e-05, 163.82901087, 0.00024441, 546.0967029, 0.0008147, -54.60967029, -8.147e-05, -163.82901087, -0.00024441, -546.0967029, -0.0008147, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 9.55, 7.9, 3.35)
    ops.node(122011, 9.55, 7.9, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 26589646.42101824, 11079019.34209093, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 179.00649872, 0.00077841, 218.04583969, 0.02304425, 21.80458397, 0.06279229, -179.00649872, -0.00077841, -218.04583969, -0.02304425, -21.80458397, -0.06279229, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 155.6375625, 0.00077841, 189.58039649, 0.02304425, 18.95803965, 0.06279229, -155.6375625, -0.00077841, -189.58039649, -0.02304425, -18.95803965, -0.06279229, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 205.88008229, 0.01556827, 205.88008229, 0.04670481, 144.1160576, -3222.7006712, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 51.47002057, 8.259e-05, 154.41006172, 0.00024777, 514.70020573, 0.00082591, -51.47002057, -8.259e-05, -154.41006172, -0.00024777, -514.70020573, -0.00082591, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 205.88008229, 0.01556827, 205.88008229, 0.04670481, 144.1160576, -3222.7006712, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 51.47002057, 8.259e-05, 154.41006172, 0.00024777, 514.70020573, 0.00082591, -51.47002057, -8.259e-05, -154.41006172, -0.00024777, -514.70020573, -0.00082591, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 16.25, 7.9, 3.35)
    ops.node(122012, 16.25, 7.9, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 27747346.85397518, 11561394.52248966, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 157.80634678, 0.00085121, 191.93740611, 0.03128346, 19.19374061, 0.08759882, -157.80634678, -0.00085121, -191.93740611, -0.03128346, -19.19374061, -0.08759882, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 133.26176759, 0.00085121, 162.08421605, 0.03128346, 16.20842161, 0.08759882, -133.26176759, -0.00085121, -162.08421605, -0.03128346, -16.20842161, -0.08759882, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 202.94443107, 0.01702429, 202.94443107, 0.05107288, 142.06110175, -4392.42906255, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 50.73610777, 9.874e-05, 152.2083233, 0.00029622, 507.36107767, 0.00098739, -50.73610777, -9.874e-05, -152.2083233, -0.00029622, -507.36107767, -0.00098739, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 202.94443107, 0.01702429, 202.94443107, 0.05107288, 142.06110175, -4392.42906255, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 50.73610777, 9.874e-05, 152.2083233, 0.00029622, 507.36107767, 0.00098739, -50.73610777, -9.874e-05, -152.2083233, -0.00029622, -507.36107767, -0.00098739, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.35)
    ops.node(123001, 0.0, 0.0, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.1225, 26506509.15412935, 11044378.81422056, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 98.42975543, 0.0009596, 120.12206743, 0.02674564, 12.01220674, 0.07729078, -98.42975543, -0.0009596, -120.12206743, -0.02674564, -12.01220674, -0.07729078, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 88.40515133, 0.0009596, 107.88820416, 0.02674564, 10.78882042, 0.07729078, -88.40515133, -0.0009596, -107.88820416, -0.02674564, -10.78882042, -0.07729078, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 140.19751722, 0.01919193, 140.19751722, 0.05757579, 98.13826205, -3213.93126423, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 35.0493793, 9.326e-05, 105.14813791, 0.00027979, 350.49379304, 0.00093262, -35.0493793, -9.326e-05, -105.14813791, -0.00027979, -350.49379304, -0.00093262, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 140.19751722, 0.01919193, 140.19751722, 0.05757579, 98.13826205, -3213.93126423, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 35.0493793, 9.326e-05, 105.14813791, 0.00027979, 350.49379304, 0.00093262, -35.0493793, -9.326e-05, -105.14813791, -0.00027979, -350.49379304, -0.00093262, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 16.25, 0.0, 6.35)
    ops.node(123004, 16.25, 0.0, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.1225, 27586072.2657209, 11494196.77738371, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 96.33733832, 0.00093957, 117.36911492, 0.02703582, 11.73691149, 0.07880186, -96.33733832, -0.00093957, -117.36911492, -0.02703582, -11.73691149, -0.07880186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 86.80291978, 0.00093957, 105.75320062, 0.02703582, 10.57532006, 0.07880186, -86.80291978, -0.00093957, -105.75320062, -0.02703582, -10.57532006, -0.07880186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 145.48384982, 0.01879146, 145.48384982, 0.05637439, 101.83869487, -3316.3360633, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 36.37096245, 9.299e-05, 109.11288736, 0.00027897, 363.70962455, 0.00092991, -36.37096245, -9.299e-05, -109.11288736, -0.00027897, -363.70962455, -0.00092991, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 145.48384982, 0.01879146, 145.48384982, 0.05637439, 101.83869487, -3316.3360633, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 36.37096245, 9.299e-05, 109.11288736, 0.00027897, 363.70962455, 0.00092991, -36.37096245, -9.299e-05, -109.11288736, -0.00027897, -363.70962455, -0.00092991, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.95, 6.375)
    ops.node(123005, 0.0, 3.95, 8.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.16, 26674244.54409361, 11114268.560039, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 178.01049252, 0.00095444, 216.7525506, 0.02657171, 21.67525506, 0.07574358, -178.01049252, -0.00095444, -216.7525506, -0.02657171, -21.67525506, -0.07574358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 178.01049252, 0.00095444, 216.7525506, 0.02657171, 21.67525506, 0.07574358, -178.01049252, -0.00095444, -216.7525506, -0.02657171, -21.67525506, -0.07574358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 190.32752275, 0.01908881, 190.32752275, 0.05726643, 133.22926593, -3810.92604334, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 47.58188069, 9.633e-05, 142.74564206, 0.00028898, 475.81880688, 0.00096326, -47.58188069, -9.633e-05, -142.74564206, -0.00028898, -475.81880688, -0.00096326, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 190.32752275, 0.01908881, 190.32752275, 0.05726643, 133.22926593, -3810.92604334, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 47.58188069, 9.633e-05, 142.74564206, 0.00028898, 475.81880688, 0.00096326, -47.58188069, -9.633e-05, -142.74564206, -0.00028898, -475.81880688, -0.00096326, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 6.7, 3.95, 6.375)
    ops.node(123006, 6.7, 3.95, 8.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.16, 26803919.79636461, 11168299.91515192, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 137.9585982, 0.00089415, 167.72238981, 0.02633004, 16.77223898, 0.06787697, -137.9585982, -0.00089415, -167.72238981, -0.02633004, -16.77223898, -0.06787697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 137.9585982, 0.00089415, 167.72238981, 0.02633004, 16.77223898, 0.06787697, -137.9585982, -0.00089415, -167.72238981, -0.02633004, -16.77223898, -0.06787697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 178.32449689, 0.01788293, 178.32449689, 0.05364879, 124.82714782, -2888.65473693, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 44.58112422, 8.981e-05, 133.74337267, 0.00026944, 445.81124222, 0.00089815, -44.58112422, -8.981e-05, -133.74337267, -0.00026944, -445.81124222, -0.00089815, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 178.32449689, 0.01788293, 178.32449689, 0.05364879, 124.82714782, -2888.65473693, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 44.58112422, 8.981e-05, 133.74337267, 0.00026944, 445.81124222, 0.00089815, -44.58112422, -8.981e-05, -133.74337267, -0.00026944, -445.81124222, -0.00089815, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 9.55, 3.95, 6.375)
    ops.node(123007, 9.55, 3.95, 8.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.16, 27940958.63968185, 11642066.09986744, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 138.00989738, 0.00089217, 167.53859224, 0.02632764, 16.75385922, 0.06943594, -138.00989738, -0.00089217, -167.53859224, -0.02632764, -16.75385922, -0.06943594, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 138.00989738, 0.00089217, 167.53859224, 0.02632764, 16.75385922, 0.06943594, -138.00989738, -0.00089217, -167.53859224, -0.02632764, -16.75385922, -0.06943594, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 183.56333993, 0.01784339, 183.56333993, 0.05353018, 128.49433795, -2889.50123246, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 45.89083498, 8.869e-05, 137.67250495, 0.00026607, 458.90834982, 0.00088691, -45.89083498, -8.869e-05, -137.67250495, -0.00026607, -458.90834982, -0.00088691, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 183.56333993, 0.01784339, 183.56333993, 0.05353018, 128.49433795, -2889.50123246, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 45.89083498, 8.869e-05, 137.67250495, 0.00026607, 458.90834982, 0.00088691, -45.89083498, -8.869e-05, -137.67250495, -0.00026607, -458.90834982, -0.00088691, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 16.25, 3.95, 6.375)
    ops.node(123008, 16.25, 3.95, 8.625)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.16, 27117638.0203096, 11299015.84179567, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 182.67637578, 0.00092804, 222.30748489, 0.02669807, 22.23074849, 0.07652514, -182.67637578, -0.00092804, -222.30748489, -0.02669807, -22.23074849, -0.07652514, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 182.67637578, 0.00092804, 222.30748489, 0.02669807, 22.23074849, 0.07652514, -182.67637578, -0.00092804, -222.30748489, -0.02669807, -22.23074849, -0.07652514, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 193.70503223, 0.01856075, 193.70503223, 0.05568224, 135.59352256, -3884.55860266, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 48.42625806, 9.643e-05, 145.27877417, 0.0002893, 484.26258058, 0.00096432, -48.42625806, -9.643e-05, -145.27877417, -0.0002893, -484.26258058, -0.00096432, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 193.70503223, 0.01856075, 193.70503223, 0.05568224, 135.59352256, -3884.55860266, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 48.42625806, 9.643e-05, 145.27877417, 0.0002893, 484.26258058, 0.00096432, -48.42625806, -9.643e-05, -145.27877417, -0.0002893, -484.26258058, -0.00096432, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.9, 6.35)
    ops.node(123009, 0.0, 7.9, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 26721209.98199302, 11133837.49249709, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 97.76381906, 0.00093036, 119.27264107, 0.0214691, 11.92726411, 0.06437007, -97.76381906, -0.00093036, -119.27264107, -0.0214691, -11.92726411, -0.06437007, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 87.61995339, 0.00093036, 106.89704383, 0.0214691, 10.68970438, 0.06437007, -87.61995339, -0.00093036, -106.89704383, -0.0214691, -10.68970438, -0.06437007, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 123.93332912, 0.01860721, 123.93332912, 0.05582162, 86.75333039, -2217.09114847, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 30.98333228, 8.178e-05, 92.94999684, 0.00024534, 309.83332281, 0.0008178, -30.98333228, -8.178e-05, -92.94999684, -0.00024534, -309.83332281, -0.0008178, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 123.93332912, 0.01860721, 123.93332912, 0.05582162, 86.75333039, -2217.09114847, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 30.98333228, 8.178e-05, 92.94999684, 0.00024534, 309.83332281, 0.0008178, -30.98333228, -8.178e-05, -92.94999684, -0.00024534, -309.83332281, -0.0008178, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 6.7, 7.9, 6.35)
    ops.node(123010, 6.7, 7.9, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 27102092.29440457, 11292538.4560019, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 90.22464316, 0.00094138, 109.81592069, 0.0170515, 10.98159207, 0.0530716, -90.22464316, -0.00094138, -109.81592069, -0.0170515, -10.98159207, -0.0530716, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 84.83579288, 0.00094138, 103.25694152, 0.0170515, 10.32569415, 0.0530716, -84.83579288, -0.00094138, -103.25694152, -0.0170515, -10.32569415, -0.0530716, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 119.45483863, 0.01882758, 119.45483863, 0.05648275, 83.61838704, -1644.92004432, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 29.86370966, 7.772e-05, 89.59112897, 0.00023315, 298.63709657, 0.00077717, -29.86370966, -7.772e-05, -89.59112897, -0.00023315, -298.63709657, -0.00077717, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 119.45483863, 0.01882758, 119.45483863, 0.05648275, 83.61838704, -1644.92004432, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 29.86370966, 7.772e-05, 89.59112897, 0.00023315, 298.63709657, 0.00077717, -29.86370966, -7.772e-05, -89.59112897, -0.00023315, -298.63709657, -0.00077717, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 9.55, 7.9, 6.35)
    ops.node(123011, 9.55, 7.9, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 27417240.48656357, 11423850.20273482, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 92.05499204, 0.00094042, 111.99329557, 0.01721688, 11.19932956, 0.0535525, -92.05499204, -0.00094042, -111.99329557, -0.01721688, -11.19932956, -0.0535525, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 86.42067416, 0.00094042, 105.13863387, 0.01721688, 10.51386339, 0.0535525, -86.42067416, -0.00094042, -105.13863387, -0.01721688, -10.51386339, -0.0535525, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 121.18934461, 0.01880832, 121.18934461, 0.05642496, 84.83254123, -1670.74182579, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 30.29733615, 7.794e-05, 90.89200846, 0.00023382, 302.97336153, 0.0007794, -30.29733615, -7.794e-05, -90.89200846, -0.00023382, -302.97336153, -0.0007794, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 121.18934461, 0.01880832, 121.18934461, 0.05642496, 84.83254123, -1670.74182579, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 30.29733615, 7.794e-05, 90.89200846, 0.00023382, 302.97336153, 0.0007794, -30.29733615, -7.794e-05, -90.89200846, -0.00023382, -302.97336153, -0.0007794, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 16.25, 7.9, 6.35)
    ops.node(123012, 16.25, 7.9, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 27669223.57413147, 11528843.15588811, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 99.01035527, 0.00094105, 120.60807749, 0.02159077, 12.06080775, 0.06537848, -99.01035527, -0.00094105, -120.60807749, -0.02159077, -12.06080775, -0.06537848, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 88.89329544, 0.00094105, 108.28412277, 0.02159077, 10.82841228, 0.06537848, -88.89329544, -0.00094105, -108.28412277, -0.02159077, -10.82841228, -0.06537848, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 126.66709264, 0.01882106, 126.66709264, 0.05646319, 88.66696485, -2189.10699498, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 31.66677316, 8.072e-05, 95.00031948, 0.00024216, 316.6677316, 0.00080721, -31.66677316, -8.072e-05, -95.00031948, -0.00024216, -316.6677316, -0.00080721, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 126.66709264, 0.01882106, 126.66709264, 0.05646319, 88.66696485, -2189.10699498, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 31.66677316, 8.072e-05, 95.00031948, 0.00024216, 316.6677316, 0.00080721, -31.66677316, -8.072e-05, -95.00031948, -0.00024216, -316.6677316, -0.00080721, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.35)
    ops.node(124001, 0.0, 0.0, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.1225, 27049902.24789109, 11270792.60328796, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 110.45400436, 0.0009401, 135.26662665, 0.02916304, 13.52666267, 0.08733008, -110.45400436, -0.0009401, -135.26662665, -0.02916304, -13.52666267, -0.08733008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 90.90591888, 0.0009401, 111.32721771, 0.02916304, 11.13272177, 0.08733008, -90.90591888, -0.0009401, -111.32721771, -0.02916304, -11.13272177, -0.08733008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 131.80493554, 0.01880202, 131.80493554, 0.05640605, 92.26345488, -7270.77459538, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 32.95123389, 8.592e-05, 98.85370166, 0.00025775, 329.51233886, 0.00085918, -32.95123389, -8.592e-05, -98.85370166, -0.00025775, -329.51233886, -0.00085918, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 131.80493554, 0.01880202, 131.80493554, 0.05640605, 92.26345488, -7270.77459538, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 32.95123389, 8.592e-05, 98.85370166, 0.00025775, 329.51233886, 0.00085918, -32.95123389, -8.592e-05, -98.85370166, -0.00025775, -329.51233886, -0.00085918, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 16.25, 0.0, 9.35)
    ops.node(124004, 16.25, 0.0, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.1225, 28037197.21121729, 11682165.50467387, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 113.40670016, 0.00094199, 138.57871166, 0.02855801, 13.85787117, 0.08706085, -113.40670016, -0.00094199, -138.57871166, -0.02855801, -13.85787117, -0.08706085, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 93.23367839, 0.00094199, 113.92803967, 0.02855801, 11.39280397, 0.08706085, -93.23367839, -0.00094199, -113.92803967, -0.02855801, -11.39280397, -0.08706085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 134.26494191, 0.01883981, 134.26494191, 0.05651942, 93.98545934, -7107.21395463, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 33.56623548, 8.444e-05, 100.69870643, 0.00025332, 335.66235477, 0.0008444, -33.56623548, -8.444e-05, -100.69870643, -0.00025332, -335.66235477, -0.0008444, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 134.26494191, 0.01883981, 134.26494191, 0.05651942, 93.98545934, -7107.21395463, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 33.56623548, 8.444e-05, 100.69870643, 0.00025332, 335.66235477, 0.0008444, -33.56623548, -8.444e-05, -100.69870643, -0.00025332, -335.66235477, -0.0008444, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.95, 9.375)
    ops.node(124005, 0.0, 3.95, 11.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.16, 27701102.23286538, 11542125.93036058, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 201.85322047, 0.00095373, 246.68071692, 0.03401792, 24.66807169, 0.1021643, -201.85322047, -0.00095373, -246.68071692, -0.03401792, -24.66807169, -0.1021643, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 184.45413404, 0.00095373, 225.41764713, 0.03401792, 22.54176471, 0.1021643, -184.45413404, -0.00095373, -225.41764713, -0.03401792, -22.54176471, -0.1021643, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 198.58975621, 0.01907464, 198.58975621, 0.05722391, 139.01282935, -10280.2504184, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 49.64743905, 9.678e-05, 148.94231716, 0.00029035, 496.47439052, 0.00096782, -49.64743905, -9.678e-05, -148.94231716, -0.00029035, -496.47439052, -0.00096782, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 198.58975621, 0.01907464, 198.58975621, 0.05722391, 139.01282935, -10280.2504184, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 49.64743905, 9.678e-05, 148.94231716, 0.00029035, 496.47439052, 0.00096782, -49.64743905, -9.678e-05, -148.94231716, -0.00029035, -496.47439052, -0.00096782, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 6.7, 3.95, 9.375)
    ops.node(124006, 6.7, 3.95, 11.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.16, 27747327.30093216, 11561386.3753884, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 113.13444958, 0.00085088, 138.15147798, 0.02368936, 13.8151478, 0.06671508, -113.13444958, -0.00085088, -138.15147798, -0.02368936, -13.8151478, -0.06671508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 113.13444958, 0.00085088, 138.15147798, 0.02368936, 13.8151478, 0.06671508, -113.13444958, -0.00085088, -138.15147798, -0.02368936, -13.8151478, -0.06671508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 150.715475, 0.01701754, 150.715475, 0.05105263, 105.5008325, -3316.86033956, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 37.67886875, 7.333e-05, 113.03660625, 0.00021998, 376.78868751, 0.00073328, -37.67886875, -7.333e-05, -113.03660625, -0.00021998, -376.78868751, -0.00073328, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 150.715475, 0.01701754, 150.715475, 0.05105263, 105.5008325, -3316.86033956, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 37.67886875, 7.333e-05, 113.03660625, 0.00021998, 376.78868751, 0.00073328, -37.67886875, -7.333e-05, -113.03660625, -0.00021998, -376.78868751, -0.00073328, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 9.55, 3.95, 9.375)
    ops.node(124007, 9.55, 3.95, 11.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.16, 27498264.73159692, 11457610.30483205, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 110.99417669, 0.0008562, 135.60789138, 0.02414143, 13.56078914, 0.06705279, -110.99417669, -0.0008562, -135.60789138, -0.02414143, -13.56078914, -0.06705279, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 110.99417669, 0.0008562, 135.60789138, 0.02414143, 13.56078914, 0.06705279, -110.99417669, -0.0008562, -135.60789138, -0.02414143, -13.56078914, -0.06705279, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 151.07923374, 0.01712401, 151.07923374, 0.05137204, 105.75546362, -3433.73448652, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 37.76980843, 7.417e-05, 113.3094253, 0.00022251, 377.69808434, 0.00074171, -37.76980843, -7.417e-05, -113.3094253, -0.00022251, -377.69808434, -0.00074171, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 151.07923374, 0.01712401, 151.07923374, 0.05137204, 105.75546362, -3433.73448652, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 37.76980843, 7.417e-05, 113.3094253, 0.00022251, 377.69808434, 0.00074171, -37.76980843, -7.417e-05, -113.3094253, -0.00022251, -377.69808434, -0.00074171, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 16.25, 3.95, 9.375)
    ops.node(124008, 16.25, 3.95, 11.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.16, 28426418.45423739, 11844341.02259891, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 205.4345647, 0.00093794, 250.64532289, 0.03397167, 25.06453229, 0.10249796, -205.4345647, -0.00093794, -250.64532289, -0.03397167, -25.06453229, -0.10249796, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 187.42199929, 0.00093794, 228.66866439, 0.03397167, 22.86686644, 0.10249796, -187.42199929, -0.00093794, -228.66866439, -0.03397167, -22.86686644, -0.10249796, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 205.46599811, 0.01875875, 205.46599811, 0.05627624, 143.82619868, -10853.12224988, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 51.36649953, 9.758e-05, 154.09949858, 0.00029273, 513.66499527, 0.00097578, -51.36649953, -9.758e-05, -154.09949858, -0.00029273, -513.66499527, -0.00097578, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 205.46599811, 0.01875875, 205.46599811, 0.05627624, 143.82619868, -10853.12224988, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 51.36649953, 9.758e-05, 154.09949858, 0.00029273, 513.66499527, 0.00097578, -51.36649953, -9.758e-05, -154.09949858, -0.00029273, -513.66499527, -0.00097578, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.9, 9.35)
    ops.node(124009, 0.0, 7.9, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 27904915.06573193, 11627047.94405497, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 111.68381713, 0.00096596, 136.5152963, 0.02887138, 13.65152963, 0.08733207, -111.68381713, -0.00096596, -136.5152963, -0.02887138, -13.65152963, -0.08733207, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 92.54670052, 0.00096596, 113.12328471, 0.02887138, 11.31232847, 0.08733207, -92.54670052, -0.00096596, -113.12328471, -0.02887138, -11.31232847, -0.08733207, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 135.2848887, 0.01931921, 135.2848887, 0.05795763, 94.69942209, -7373.00440752, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 33.82122217, 8.548e-05, 101.46366652, 0.00025645, 338.21222174, 0.00085484, -33.82122217, -8.548e-05, -101.46366652, -0.00025645, -338.21222174, -0.00085484, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 135.2848887, 0.01931921, 135.2848887, 0.05795763, 94.69942209, -7373.00440752, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 33.82122217, 8.548e-05, 101.46366652, 0.00025645, 338.21222174, 0.00085484, -33.82122217, -8.548e-05, -101.46366652, -0.00025645, -338.21222174, -0.00085484, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 6.7, 7.9, 9.35)
    ops.node(124010, 6.7, 7.9, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 26928738.82379294, 11220307.84324706, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 76.12462999, 0.00091341, 93.19528968, 0.01857851, 9.31952897, 0.06091773, -76.12462999, -0.00091341, -93.19528968, -0.01857851, -9.31952897, -0.06091773, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 70.7795971, 0.00091341, 86.65165343, 0.01857851, 8.66516534, 0.06091773, -70.7795971, -0.00091341, -86.65165343, -0.01857851, -8.66516534, -0.06091773, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 109.1508551, 0.01826813, 109.1508551, 0.0548044, 76.40559857, -2980.82862466, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 27.28771378, 7.147e-05, 81.86314133, 0.00021441, 272.87713776, 0.00071471, -27.28771378, -7.147e-05, -81.86314133, -0.00021441, -272.87713776, -0.00071471, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 109.1508551, 0.01826813, 109.1508551, 0.0548044, 76.40559857, -2980.82862466, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 27.28771378, 7.147e-05, 81.86314133, 0.00021441, 272.87713776, 0.00071471, -27.28771378, -7.147e-05, -81.86314133, -0.00021441, -272.87713776, -0.00071471, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 9.55, 7.9, 9.35)
    ops.node(124011, 9.55, 7.9, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 28178032.43047657, 11740846.84603191, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 74.34701926, 0.00091357, 90.77416937, 0.01815948, 9.07741694, 0.06091091, -74.34701926, -0.00091357, -90.77416937, -0.01815948, -9.07741694, -0.06091091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 69.40292455, 0.00091357, 84.73766521, 0.01815948, 8.47376652, 0.06091091, -69.40292455, -0.00091357, -84.73766521, -0.01815948, -8.47376652, -0.06091091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 112.40472612, 0.01827147, 112.40472612, 0.05481442, 78.68330828, -2879.67612992, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 28.10118153, 7.034e-05, 84.30354459, 0.00021101, 281.0118153, 0.00070338, -28.10118153, -7.034e-05, -84.30354459, -0.00021101, -281.0118153, -0.00070338, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 112.40472612, 0.01827147, 112.40472612, 0.05481442, 78.68330828, -2879.67612992, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 28.10118153, 7.034e-05, 84.30354459, 0.00021101, 281.0118153, 0.00070338, -28.10118153, -7.034e-05, -84.30354459, -0.00021101, -281.0118153, -0.00070338, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 16.25, 7.9, 9.35)
    ops.node(124012, 16.25, 7.9, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 29280730.9550745, 12200304.56461438, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 111.4910048, 0.00092397, 135.81759008, 0.02870557, 13.58175901, 0.08756685, -111.4910048, -0.00092397, -135.81759008, -0.02870557, -13.58175901, -0.08756685, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 92.0243389, 0.00092397, 112.10342897, 0.02870557, 11.2103429, 0.08756685, -92.0243389, -0.00092397, -112.10342897, -0.02870557, -11.2103429, -0.08756685, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 141.30605044, 0.01847938, 141.30605044, 0.05543813, 98.9142353, -7593.57060568, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 35.32651261, 8.509e-05, 105.97953783, 0.00025528, 353.26512609, 0.00085094, -35.32651261, -8.509e-05, -105.97953783, -0.00025528, -353.26512609, -0.00085094, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 141.30605044, 0.01847938, 141.30605044, 0.05543813, 98.9142353, -7593.57060568, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 35.32651261, 8.509e-05, 105.97953783, 0.00025528, 353.26512609, 0.00085094, -35.32651261, -8.509e-05, -105.97953783, -0.00025528, -353.26512609, -0.00085094, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 6.7, 0.0, 0.0)
    ops.node(124013, 6.7, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4030, 170002, 124013, 0.2025, 27736419.81023252, 11556841.58759688, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24030, 199.68525634, 0.00062999, 242.05969127, 0.02486064, 24.20596913, 0.07121401, -199.68525634, -0.00062999, -242.05969127, -0.02486064, -24.20596913, -0.07121401, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14030, 217.01900266, 0.00062999, 263.07176477, 0.02486064, 26.30717648, 0.07121401, -217.01900266, -0.00062999, -263.07176477, -0.02486064, -26.30717648, -0.07121401, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24030, 4030, 0.0, 373.64883531, 0.01259981, 373.64883531, 0.03779942, 261.55418471, -8665.43601161, 0.05, 2, 0, 70002, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 44030, 93.41220883, 7.185e-05, 280.23662648, 0.00021554, 934.12208827, 0.00071848, -93.41220883, -7.185e-05, -280.23662648, -0.00021554, -934.12208827, -0.00071848, 0.4, 0.3, 0.003, 0.0, 0.0, 24030, 2)
    ops.limitCurve('ThreePoint', 14030, 4030, 0.0, 373.64883531, 0.01259981, 373.64883531, 0.03779942, 261.55418471, -8665.43601161, 0.05, 2, 0, 70002, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 34030, 93.41220883, 7.185e-05, 280.23662648, 0.00021554, 934.12208827, 0.00071848, -93.41220883, -7.185e-05, -280.23662648, -0.00021554, -934.12208827, -0.00071848, 0.4, 0.3, 0.003, 0.0, 0.0, 14030, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4030, 99999, 'P', 44030, 'Vy', 34030, 'Vz', 24030, 'My', 14030, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4030, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 4030, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174013, 6.7, 0.0, 1.675)
    ops.node(121002, 6.7, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4031, 174013, 121002, 0.2025, 28773795.87523847, 11989081.6146827, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24031, 208.07931911, 0.00062825, 251.99511981, 0.02434477, 25.19951198, 0.07311742, -208.07931911, -0.00062825, -251.99511981, -0.02434477, -25.19951198, -0.07311742, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14031, 167.79172434, 0.00062825, 203.2047003, 0.02434477, 20.32047003, 0.07311742, -167.79172434, -0.00062825, -203.2047003, -0.02434477, -20.32047003, -0.07311742, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24031, 4031, 0.0, 375.19952778, 0.012565, 375.19952778, 0.03769501, 262.63966944, -8192.9918068, 0.05, 2, 0, 74013, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44031, 93.79988194, 6.954e-05, 281.39964583, 0.00020863, 937.99881945, 0.00069545, -93.79988194, -6.954e-05, -281.39964583, -0.00020863, -937.99881945, -0.00069545, 0.4, 0.3, 0.003, 0.0, 0.0, 24031, 2)
    ops.limitCurve('ThreePoint', 14031, 4031, 0.0, 375.19952778, 0.012565, 375.19952778, 0.03769501, 262.63966944, -8192.9918068, 0.05, 2, 0, 74013, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34031, 93.79988194, 6.954e-05, 281.39964583, 0.00020863, 937.99881945, 0.00069545, -93.79988194, -6.954e-05, -281.39964583, -0.00020863, -937.99881945, -0.00069545, 0.4, 0.3, 0.003, 0.0, 0.0, 14031, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4031, 99999, 'P', 44031, 'Vy', 34031, 'Vz', 24031, 'My', 14031, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174013, 74013, 174013, 4031, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4031, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 9.55, 0.0, 0.0)
    ops.node(124014, 9.55, 0.0, 1.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4032, 170003, 124014, 0.2025, 27398926.139446, 11416219.22476917, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24032, 197.45642747, 0.00064294, 239.4507834, 0.02476937, 23.94507834, 0.07053458, -197.45642747, -0.00064294, -239.4507834, -0.02476937, -23.94507834, -0.07053458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14032, 213.7271634, 0.00064294, 259.18192366, 0.02476937, 25.91819237, 0.07053458, -213.7271634, -0.00064294, -259.18192366, -0.02476937, -25.91819237, -0.07053458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24032, 4032, 0.0, 371.12315562, 0.01285872, 371.12315562, 0.03857615, 259.78620893, -8775.73772176, 0.05, 2, 0, 70003, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 44032, 92.7807889, 7.224e-05, 278.34236671, 0.00021672, 927.80788905, 0.00072241, -92.7807889, -7.224e-05, -278.34236671, -0.00021672, -927.80788905, -0.00072241, 0.4, 0.3, 0.003, 0.0, 0.0, 24032, 2)
    ops.limitCurve('ThreePoint', 14032, 4032, 0.0, 371.12315562, 0.01285872, 371.12315562, 0.03857615, 259.78620893, -8775.73772176, 0.05, 2, 0, 70003, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 34032, 92.7807889, 7.224e-05, 278.34236671, 0.00021672, 927.80788905, 0.00072241, -92.7807889, -7.224e-05, -278.34236671, -0.00021672, -927.80788905, -0.00072241, 0.4, 0.3, 0.003, 0.0, 0.0, 14032, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4032, 99999, 'P', 44032, 'Vy', 34032, 'Vz', 24032, 'My', 14032, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4032, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 4032, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174014, 9.55, 0.0, 1.675)
    ops.node(121003, 9.55, 0.0, 2.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4033, 174014, 121003, 0.2025, 27877473.28220074, 11615613.86758364, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24033, 207.76199707, 0.00062, 251.95219139, 0.02470638, 25.19521914, 0.07211111, -207.76199707, -0.00062, -251.95219139, -0.02470638, -25.19521914, -0.07211111, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14033, 166.15783996, 0.00062, 201.49898675, 0.02470638, 20.14989868, 0.07211111, -166.15783996, -0.00062, -201.49898675, -0.02470638, -20.14989868, -0.07211111, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24033, 4033, 0.0, 367.44641094, 0.01239998, 367.44641094, 0.03719993, 257.21248766, -8408.06898558, 0.05, 2, 0, 74014, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44033, 91.86160273, 7.03e-05, 275.5848082, 0.00021089, 918.61602735, 0.00070297, -91.86160273, -7.03e-05, -275.5848082, -0.00021089, -918.61602735, -0.00070297, 0.4, 0.3, 0.003, 0.0, 0.0, 24033, 2)
    ops.limitCurve('ThreePoint', 14033, 4033, 0.0, 367.44641094, 0.01239998, 367.44641094, 0.03719993, 257.21248766, -8408.06898558, 0.05, 2, 0, 74014, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34033, 91.86160273, 7.03e-05, 275.5848082, 0.00021089, 918.61602735, 0.00070297, -91.86160273, -7.03e-05, -275.5848082, -0.00021089, -918.61602735, -0.00070297, 0.4, 0.3, 0.003, 0.0, 0.0, 14033, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4033, 99999, 'P', 44033, 'Vy', 34033, 'Vz', 24033, 'My', 14033, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174014, 74014, 174014, 4033, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4033, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 6.7, 0.0, 3.35)
    ops.node(124015, 6.7, 0.0, 4.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4035, 171002, 124015, 0.2025, 27584856.71586768, 11493690.2982782, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24035, 171.41657142, 0.00062467, 208.41579654, 0.02516195, 20.84157965, 0.07529103, -171.41657142, -0.00062467, -208.41579654, -0.02516195, -20.84157965, -0.07529103, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14035, 141.17533118, 0.00062467, 171.64716839, 0.02516195, 17.16471684, 0.07529103, -141.17533118, -0.00062467, -171.64716839, -0.02516195, -17.16471684, -0.07529103, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24035, 4035, 0.0, 353.09511831, 0.01249348, 353.09511831, 0.03748044, 247.16658281, -9263.14796329, 0.05, 2, 0, 71002, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 44035, 88.27377958, 6.827e-05, 264.82133873, 0.00020481, 882.73779577, 0.00068268, -88.27377958, -6.827e-05, -264.82133873, -0.00020481, -882.73779577, -0.00068268, 0.4, 0.3, 0.003, 0.0, 0.0, 24035, 2)
    ops.limitCurve('ThreePoint', 14035, 4035, 0.0, 353.09511831, 0.01249348, 353.09511831, 0.03748044, 247.16658281, -9263.14796329, 0.05, 2, 0, 71002, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 34035, 88.27377958, 6.827e-05, 264.82133873, 0.00020481, 882.73779577, 0.00068268, -88.27377958, -6.827e-05, -264.82133873, -0.00020481, -882.73779577, -0.00068268, 0.4, 0.3, 0.003, 0.0, 0.0, 14035, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4035, 99999, 'P', 44035, 'Vy', 34035, 'Vz', 24035, 'My', 14035, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4035, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 4035, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174015, 6.7, 0.0, 4.675)
    ops.node(122002, 6.7, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4036, 174015, 122002, 0.2025, 27604231.51047998, 11501763.12936666, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24036, 170.53908835, 0.00061998, 207.46718381, 0.02510772, 20.74671838, 0.07616762, -170.53908835, -0.00061998, -207.46718381, -0.02510772, -20.74671838, -0.07616762, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14036, 138.88453589, 0.00061998, 168.958236, 0.02510772, 16.8958236, 0.07616762, -138.88453589, -0.00061998, -168.958236, -0.02510772, -16.8958236, -0.07616762, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24036, 4036, 0.0, 346.82321438, 0.01239954, 346.82321438, 0.03719861, 242.77625007, -9246.05876755, 0.05, 2, 0, 74015, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44036, 86.7058036, 6.701e-05, 260.11741079, 0.00020103, 867.05803596, 0.00067009, -86.7058036, -6.701e-05, -260.11741079, -0.00020103, -867.05803596, -0.00067009, 0.4, 0.3, 0.003, 0.0, 0.0, 24036, 2)
    ops.limitCurve('ThreePoint', 14036, 4036, 0.0, 346.82321438, 0.01239954, 346.82321438, 0.03719861, 242.77625007, -9246.05876755, 0.05, 2, 0, 74015, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34036, 86.7058036, 6.701e-05, 260.11741079, 0.00020103, 867.05803596, 0.00067009, -86.7058036, -6.701e-05, -260.11741079, -0.00020103, -867.05803596, -0.00067009, 0.4, 0.3, 0.003, 0.0, 0.0, 14036, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4036, 99999, 'P', 44036, 'Vy', 34036, 'Vz', 24036, 'My', 14036, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174015, 74015, 174015, 4036, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4036, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 9.55, 0.0, 3.35)
    ops.node(124016, 9.55, 0.0, 4.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4037, 171003, 124016, 0.2025, 28376587.9715132, 11823578.32146383, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24037, 174.93786632, 0.00062214, 212.42215377, 0.02522098, 21.24221538, 0.07639075, -174.93786632, -0.00062214, -212.42215377, -0.02522098, -21.24221538, -0.07639075, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14037, 143.40700967, 0.00062214, 174.13511724, 0.02522098, 17.41351172, 0.07639075, -143.40700967, -0.00062214, -174.13511724, -0.02522098, -17.41351172, -0.07639075, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24037, 4037, 0.0, 363.28847301, 0.01244276, 363.28847301, 0.03732829, 254.30193111, -9397.1761404, 0.05, 2, 0, 71003, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 44037, 90.82211825, 6.828e-05, 272.46635476, 0.00020484, 908.22118252, 0.00068279, -90.82211825, -6.828e-05, -272.46635476, -0.00020484, -908.22118252, -0.00068279, 0.4, 0.3, 0.003, 0.0, 0.0, 24037, 2)
    ops.limitCurve('ThreePoint', 14037, 4037, 0.0, 363.28847301, 0.01244276, 363.28847301, 0.03732829, 254.30193111, -9397.1761404, 0.05, 2, 0, 71003, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 34037, 90.82211825, 6.828e-05, 272.46635476, 0.00020484, 908.22118252, 0.00068279, -90.82211825, -6.828e-05, -272.46635476, -0.00020484, -908.22118252, -0.00068279, 0.4, 0.3, 0.003, 0.0, 0.0, 14037, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4037, 99999, 'P', 44037, 'Vy', 34037, 'Vz', 24037, 'My', 14037, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4037, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 4037, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174016, 9.55, 0.0, 4.675)
    ops.node(122003, 9.55, 0.0, 5.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4038, 174016, 122003, 0.2025, 27810862.23994924, 11587859.26664552, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24038, 172.7133646, 0.00061946, 210.04233531, 0.02556204, 21.00423353, 0.07688573, -172.7133646, -0.00061946, -210.04233531, -0.02556204, -21.00423353, -0.07688573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14038, 140.15139132, 0.00061946, 170.44266145, 0.02556204, 17.04426615, 0.07688573, -140.15139132, -0.00061946, -170.44266145, -0.02556204, -17.04426615, -0.07688573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24038, 4038, 0.0, 357.46005095, 0.0123893, 357.46005095, 0.0371679, 250.22203567, -10157.63721598, 0.05, 2, 0, 74016, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44038, 89.36501274, 6.855e-05, 268.09503822, 0.00020565, 893.65012738, 0.00068551, -89.36501274, -6.855e-05, -268.09503822, -0.00020565, -893.65012738, -0.00068551, 0.4, 0.3, 0.003, 0.0, 0.0, 24038, 2)
    ops.limitCurve('ThreePoint', 14038, 4038, 0.0, 357.46005095, 0.0123893, 357.46005095, 0.0371679, 250.22203567, -10157.63721598, 0.05, 2, 0, 74016, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34038, 89.36501274, 6.855e-05, 268.09503822, 0.00020565, 893.65012738, 0.00068551, -89.36501274, -6.855e-05, -268.09503822, -0.00020565, -893.65012738, -0.00068551, 0.4, 0.3, 0.003, 0.0, 0.0, 14038, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4038, 99999, 'P', 44038, 'Vy', 34038, 'Vz', 24038, 'My', 14038, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174016, 74016, 174016, 4038, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4038, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 6.7, 0.0, 6.35)
    ops.node(124017, 6.7, 0.0, 7.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4040, 172002, 124017, 0.1225, 29172134.69635449, 12155056.12348104, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24040, 86.17829388, 0.00069139, 104.45571832, 0.01560076, 10.44557183, 0.05801122, -86.17829388, -0.00069139, -104.45571832, -0.01560076, -10.44557183, -0.05801122, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14040, 75.42575728, 0.00069139, 91.42269244, 0.01560076, 9.14226924, 0.05801122, -75.42575728, -0.00069139, -91.42269244, -0.01560076, -9.14226924, -0.05801122, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24040, 4040, 0.0, 174.32156606, 0.01382776, 174.32156606, 0.04148328, 122.02509624, -3853.74904735, 0.05, 2, 0, 72002, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 44040, 43.58039152, 5.268e-05, 130.74117455, 0.00015805, 435.80391515, 0.00052683, -43.58039152, -5.268e-05, -130.74117455, -0.00015805, -435.80391515, -0.00052683, 0.4, 0.3, 0.003, 0.0, 0.0, 24040, 2)
    ops.limitCurve('ThreePoint', 14040, 4040, 0.0, 174.32156606, 0.01382776, 174.32156606, 0.04148328, 122.02509624, -3853.74904735, 0.05, 2, 0, 72002, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 34040, 43.58039152, 5.268e-05, 130.74117455, 0.00015805, 435.80391515, 0.00052683, -43.58039152, -5.268e-05, -130.74117455, -0.00015805, -435.80391515, -0.00052683, 0.4, 0.3, 0.003, 0.0, 0.0, 14040, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4040, 99999, 'P', 44040, 'Vy', 34040, 'Vz', 24040, 'My', 14040, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4040, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 4040, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174017, 6.7, 0.0, 7.675)
    ops.node(123002, 6.7, 0.0, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4041, 174017, 123002, 0.1225, 27828952.93729831, 11595397.05720763, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24041, 83.09825046, 0.00068505, 101.06981251, 0.02114593, 10.10698125, 0.07126379, -83.09825046, -0.00068505, -101.06981251, -0.02114593, -10.10698125, -0.07126379, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14041, 71.97074074, 0.00068505, 87.53576919, 0.02114593, 8.75357692, 0.07126379, -71.97074074, -0.00068505, -87.53576919, -0.02114593, -8.75357692, -0.07126379, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24041, 4041, 0.0, 181.49704055, 0.01370092, 181.49704055, 0.04110277, 127.04792838, -5753.77990788, 0.05, 2, 0, 74017, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44041, 45.37426014, 5.75e-05, 136.12278041, 0.0001725, 453.74260137, 0.00057499, -45.37426014, -5.75e-05, -136.12278041, -0.0001725, -453.74260137, -0.00057499, 0.4, 0.3, 0.003, 0.0, 0.0, 24041, 2)
    ops.limitCurve('ThreePoint', 14041, 4041, 0.0, 181.49704055, 0.01370092, 181.49704055, 0.04110277, 127.04792838, -5753.77990788, 0.05, 2, 0, 74017, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34041, 45.37426014, 5.75e-05, 136.12278041, 0.0001725, 453.74260137, 0.00057499, -45.37426014, -5.75e-05, -136.12278041, -0.0001725, -453.74260137, -0.00057499, 0.4, 0.3, 0.003, 0.0, 0.0, 14041, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4041, 99999, 'P', 44041, 'Vy', 34041, 'Vz', 24041, 'My', 14041, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174017, 74017, 174017, 4041, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4041, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 9.55, 0.0, 6.35)
    ops.node(124018, 9.55, 0.0, 7.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4042, 172003, 124018, 0.1225, 26602686.18153297, 11084452.57563874, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24042, 87.47768819, 0.00070615, 106.45592028, 0.01603936, 10.64559203, 0.05553391, -87.47768819, -0.00070615, -106.45592028, -0.01603936, -10.64559203, -0.05553391, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14042, 75.88846204, 0.00070615, 92.35241845, 0.01603936, 9.23524185, 0.05553391, -75.88846204, -0.00070615, -92.35241845, -0.01603936, -9.23524185, -0.05553391, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24042, 4042, 0.0, 161.9710453, 0.01412294, 161.9710453, 0.04236882, 113.37973171, -3956.42388359, 0.05, 2, 0, 72003, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 44042, 40.49276132, 5.368e-05, 121.47828397, 0.00016104, 404.92761325, 0.00053678, -40.49276132, -5.368e-05, -121.47828397, -0.00016104, -404.92761325, -0.00053678, 0.4, 0.3, 0.003, 0.0, 0.0, 24042, 2)
    ops.limitCurve('ThreePoint', 14042, 4042, 0.0, 161.9710453, 0.01412294, 161.9710453, 0.04236882, 113.37973171, -3956.42388359, 0.05, 2, 0, 72003, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 34042, 40.49276132, 5.368e-05, 121.47828397, 0.00016104, 404.92761325, 0.00053678, -40.49276132, -5.368e-05, -121.47828397, -0.00016104, -404.92761325, -0.00053678, 0.4, 0.3, 0.003, 0.0, 0.0, 14042, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4042, 99999, 'P', 44042, 'Vy', 34042, 'Vz', 24042, 'My', 14042, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4042, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 4042, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174018, 9.55, 0.0, 7.675)
    ops.node(123003, 9.55, 0.0, 8.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4043, 174018, 123003, 0.1225, 27453647.18005611, 11439019.65835671, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24043, 81.70889596, 0.00069437, 99.4399108, 0.02133177, 9.94399108, 0.07098757, -81.70889596, -0.00069437, -99.4399108, -0.02133177, -9.94399108, -0.07098757, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14043, 71.17581265, 0.00069437, 86.62112465, 0.02133177, 8.66211246, 0.07098757, -71.17581265, -0.00069437, -86.62112465, -0.02133177, -8.66211246, -0.07098757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24043, 4043, 0.0, 179.14461204, 0.01388747, 179.14461204, 0.0416624, 125.40122842, -5710.98318133, 0.05, 2, 0, 74018, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44043, 44.78615301, 5.753e-05, 134.35845903, 0.00017259, 447.86153009, 0.0005753, -44.78615301, -5.753e-05, -134.35845903, -0.00017259, -447.86153009, -0.0005753, 0.4, 0.3, 0.003, 0.0, 0.0, 24043, 2)
    ops.limitCurve('ThreePoint', 14043, 4043, 0.0, 179.14461204, 0.01388747, 179.14461204, 0.0416624, 125.40122842, -5710.98318133, 0.05, 2, 0, 74018, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34043, 44.78615301, 5.753e-05, 134.35845903, 0.00017259, 447.86153009, 0.0005753, -44.78615301, -5.753e-05, -134.35845903, -0.00017259, -447.86153009, -0.0005753, 0.4, 0.3, 0.003, 0.0, 0.0, 14043, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4043, 99999, 'P', 44043, 'Vy', 34043, 'Vz', 24043, 'My', 14043, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174018, 74018, 174018, 4043, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4043, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 6.7, 0.0, 9.35)
    ops.node(124019, 6.7, 0.0, 10.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4045, 173002, 124019, 0.1225, 28615495.08058058, 11923122.95024191, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24045, 70.50620035, 0.00066113, 85.9482463, 0.01714265, 8.59482463, 0.06520551, -70.50620035, -0.00066113, -85.9482463, -0.01714265, -8.59482463, -0.06520551, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14045, 59.77370553, 0.00066113, 72.86515426, 0.01714265, 7.28651543, 0.06520551, -59.77370553, -0.00066113, -72.86515426, -0.01714265, -7.28651543, -0.06520551, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24045, 4045, 0.0, 158.63014314, 0.01322252, 158.63014314, 0.03966755, 111.0411002, -6769.03004877, 0.05, 2, 0, 73002, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 44045, 39.65753579, 4.887e-05, 118.97260736, 0.00014662, 396.57535786, 0.00048873, -39.65753579, -4.887e-05, -118.97260736, -0.00014662, -396.57535786, -0.00048873, 0.4, 0.3, 0.003, 0.0, 0.0, 24045, 2)
    ops.limitCurve('ThreePoint', 14045, 4045, 0.0, 158.63014314, 0.01322252, 158.63014314, 0.03966755, 111.0411002, -6769.03004877, 0.05, 2, 0, 73002, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 34045, 39.65753579, 4.887e-05, 118.97260736, 0.00014662, 396.57535786, 0.00048873, -39.65753579, -4.887e-05, -118.97260736, -0.00014662, -396.57535786, -0.00048873, 0.4, 0.3, 0.003, 0.0, 0.0, 14045, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4045, 99999, 'P', 44045, 'Vy', 34045, 'Vz', 24045, 'My', 14045, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4045, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 4045, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174019, 6.7, 0.0, 10.675)
    ops.node(124002, 6.7, 0.0, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4046, 174019, 124002, 0.1225, 27539782.31906125, 11474909.29960885, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24046, 67.45989835, 0.00066622, 82.52153974, 0.0177595, 8.25215397, 0.06693099, -67.45989835, -0.00066622, -82.52153974, -0.0177595, -8.25215397, -0.06693099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14046, 56.70554289, 0.00066622, 69.36608008, 0.0177595, 6.93660801, 0.06693099, -56.70554289, -0.00066622, -69.36608008, -0.0177595, -6.93660801, -0.06693099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24046, 4046, 0.0, 150.40359195, 0.01332436, 150.40359195, 0.03997309, 105.28251437, -9985.05651485, 0.05, 2, 0, 74019, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44046, 37.60089799, 4.815e-05, 112.80269396, 0.00014445, 376.00897988, 0.00048149, -37.60089799, -4.815e-05, -112.80269396, -0.00014445, -376.00897988, -0.00048149, 0.4, 0.3, 0.003, 0.0, 0.0, 24046, 2)
    ops.limitCurve('ThreePoint', 14046, 4046, 0.0, 150.40359195, 0.01332436, 150.40359195, 0.03997309, 105.28251437, -9985.05651485, 0.05, 2, 0, 74019, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34046, 37.60089799, 4.815e-05, 112.80269396, 0.00014445, 376.00897988, 0.00048149, -37.60089799, -4.815e-05, -112.80269396, -0.00014445, -376.00897988, -0.00048149, 0.4, 0.3, 0.003, 0.0, 0.0, 14046, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4046, 99999, 'P', 44046, 'Vy', 34046, 'Vz', 24046, 'My', 14046, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174019, 74019, 174019, 4046, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4046, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 9.55, 0.0, 9.35)
    ops.node(124020, 9.55, 0.0, 10.325)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4047, 173003, 124020, 0.1225, 26181098.34604938, 10908790.97752057, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24047, 72.148235, 0.0006741, 88.38788402, 0.01754527, 8.8387884, 0.06441514, -72.148235, -0.0006741, -88.38788402, -0.01754527, -8.8387884, -0.06441514, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14047, 60.56759424, 0.0006741, 74.20058849, 0.01754527, 7.42005885, 0.06441514, -60.56759424, -0.0006741, -74.20058849, -0.01754527, -7.42005885, -0.06441514, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24047, 4047, 0.0, 145.43019615, 0.013482, 145.43019615, 0.04044599, 101.8011373, -6621.58180615, 0.05, 2, 0, 73003, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 44047, 36.35754904, 4.897e-05, 109.07264711, 0.00014692, 363.57549037, 0.00048973, -36.35754904, -4.897e-05, -109.07264711, -0.00014692, -363.57549037, -0.00048973, 0.4, 0.3, 0.003, 0.0, 0.0, 24047, 2)
    ops.limitCurve('ThreePoint', 14047, 4047, 0.0, 145.43019615, 0.013482, 145.43019615, 0.04044599, 101.8011373, -6621.58180615, 0.05, 2, 0, 73003, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 34047, 36.35754904, 4.897e-05, 109.07264711, 0.00014692, 363.57549037, 0.00048973, -36.35754904, -4.897e-05, -109.07264711, -0.00014692, -363.57549037, -0.00048973, 0.4, 0.3, 0.003, 0.0, 0.0, 14047, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4047, 99999, 'P', 44047, 'Vy', 34047, 'Vz', 24047, 'My', 14047, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4047, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 4047, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174020, 9.55, 0.0, 10.675)
    ops.node(124003, 9.55, 0.0, 11.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4048, 174020, 124003, 0.1225, 27173540.72653969, 11322308.6360582, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24048, 66.85216824, 0.00066442, 81.84304527, 0.01782437, 8.18430453, 0.06688366, -66.85216824, -0.00066442, -81.84304527, -0.01782437, -8.18430453, -0.06688366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14048, 56.18809434, 0.00066442, 68.78766792, 0.01782437, 6.87876679, 0.06688366, -56.18809434, -0.00066442, -68.78766792, -0.01782437, -6.87876679, -0.06688366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24048, 4048, 0.0, 148.56563059, 0.01328832, 148.56563059, 0.03986496, 103.99594141, -9991.42504077, 0.05, 2, 0, 74020, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44048, 37.14140765, 4.82e-05, 111.42422294, 0.0001446, 371.41407648, 0.00048201, -37.14140765, -4.82e-05, -111.42422294, -0.0001446, -371.41407648, -0.00048201, 0.4, 0.3, 0.003, 0.0, 0.0, 24048, 2)
    ops.limitCurve('ThreePoint', 14048, 4048, 0.0, 148.56563059, 0.01328832, 148.56563059, 0.03986496, 103.99594141, -9991.42504077, 0.05, 2, 0, 74020, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34048, 37.14140765, 4.82e-05, 111.42422294, 0.0001446, 371.41407648, 0.00048201, -37.14140765, -4.82e-05, -111.42422294, -0.0001446, -371.41407648, -0.00048201, 0.4, 0.3, 0.003, 0.0, 0.0, 14048, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4048, 99999, 'P', 44048, 'Vy', 34048, 'Vz', 24048, 'My', 14048, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174020, 74020, 174020, 4048, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4048, '-orient', 0, 0, 1, 0, 1, 0)
