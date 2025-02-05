import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(121001, 0.0, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1225, 23059682.11080355, 9608200.87950148, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20001, 62.75577554, 0.00070844, 76.36074355, 0.03862892, 7.63607435, 0.08666645, -62.75577554, -0.00070844, -76.36074355, -0.03862892, -7.63607435, -0.08666645, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10001, 59.75571278, 0.00070844, 72.71029032, 0.03862892, 7.27102903, 0.08666645, -59.75571278, -0.00070844, -72.71029032, -0.03862892, -7.27102903, -0.08666645, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20001, 1, 0.0, 111.8800392, 0.01416876, 111.8800392, 0.04250628, 78.31602744, -1776.16984361, 0.05, 2, 0, 70001, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 40001, 27.9700098, 8.27e-05, 83.9100294, 0.00024809, 279.700098, 0.00082698, -27.9700098, -8.27e-05, -83.9100294, -0.00024809, -279.700098, -0.00082698, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
    ops.limitCurve('ThreePoint', 10001, 1, 0.0, 111.8800392, 0.01416876, 111.8800392, 0.04250628, 78.31602744, -1776.16984361, 0.05, 2, 0, 70001, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 30001, 27.9700098, 8.27e-05, 83.9100294, 0.00024809, 279.700098, 0.00082698, -27.9700098, -8.27e-05, -83.9100294, -0.00024809, -279.700098, -0.00082698, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 7.25, 0.0, 0.0)
    ops.node(121002, 7.25, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2, 170002, 121002, 0.2025, 27779840.65496076, 11574933.60623365, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20002, 146.65913156, 0.00058355, 177.93069077, 0.04111181, 17.79306908, 0.10758671, -146.65913156, -0.00058355, -177.93069077, -0.04111181, -17.79306908, -0.10758671, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10002, 162.21327911, 0.00058355, 196.80138902, 0.04111181, 19.6801389, 0.10758671, -162.21327911, -0.00058355, -196.80138902, -0.04111181, -19.6801389, -0.10758671, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20002, 2, 0.0, 206.0662572, 0.011671, 206.0662572, 0.03501299, 144.24638004, -2627.6204529, 0.05, 2, 0, 70002, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 40002, 51.5165643, 7.649e-05, 154.5496929, 0.00022946, 515.16564301, 0.00076486, -51.5165643, -7.649e-05, -154.5496929, -0.00022946, -515.16564301, -0.00076486, 0.4, 0.3, 0.003, 0.0, 0.0, 20002, 2)
    ops.limitCurve('ThreePoint', 10002, 2, 0.0, 206.0662572, 0.011671, 206.0662572, 0.03501299, 144.24638004, -2627.6204529, 0.05, 2, 0, 70002, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 30002, 51.5165643, 7.649e-05, 154.5496929, 0.00022946, 515.16564301, 0.00076486, -51.5165643, -7.649e-05, -154.5496929, -0.00022946, -515.16564301, -0.00076486, 0.4, 0.3, 0.003, 0.0, 0.0, 10002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2, 99999, 'P', 40002, 'Vy', 30002, 'Vz', 20002, 'My', 10002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 2, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 2, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 24.9, 0.0, 0.0)
    ops.node(121005, 24.9, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.2025, 27069896.11427422, 11279123.38094759, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 138.47532913, 0.00055194, 168.14563739, 0.04213061, 16.81456374, 0.10695873, -138.47532913, -0.00055194, -168.14563739, -0.04213061, -16.81456374, -0.10695873, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 152.97863575, 0.00055194, 185.75648368, 0.04213061, 18.57564837, 0.10695873, -152.97863575, -0.00055194, -185.75648368, -0.04213061, -18.57564837, -0.10695873, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 209.01285244, 0.0110389, 209.01285244, 0.03311669, 146.30899671, -2883.17900763, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 52.25321311, 7.961e-05, 156.75963933, 0.00023884, 522.53213111, 0.00079614, -52.25321311, -7.961e-05, -156.75963933, -0.00023884, -522.53213111, -0.00079614, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 209.01285244, 0.0110389, 209.01285244, 0.03311669, 146.30899671, -2883.17900763, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 52.25321311, 7.961e-05, 156.75963933, 0.00023884, 522.53213111, 0.00079614, -52.25321311, -7.961e-05, -156.75963933, -0.00023884, -522.53213111, -0.00079614, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 32.15, 0.0, 0.0)
    ops.node(121006, 32.15, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1225, 26977200.55969074, 11240500.23320447, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 66.5255967, 0.00064935, 80.85822829, 0.0408121, 8.08582283, 0.0990731, -66.5255967, -0.00064935, -80.85822829, -0.0408121, -8.08582283, -0.0990731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 63.00581387, 0.00064935, 76.58012456, 0.0408121, 7.65801246, 0.0990731, -63.00581387, -0.00064935, -76.58012456, -0.0408121, -7.65801246, -0.0990731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 129.48704317, 0.01298691, 129.48704317, 0.03896074, 90.64093022, -1956.27250856, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 32.37176079, 8.181e-05, 97.11528238, 0.00024544, 323.71760793, 0.00081813, -32.37176079, -8.181e-05, -97.11528238, -0.00024544, -323.71760793, -0.00081813, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 129.48704317, 0.01298691, 129.48704317, 0.03896074, 90.64093022, -1956.27250856, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 32.37176079, 8.181e-05, 97.11528238, 0.00024544, 323.71760793, 0.00081813, -32.37176079, -8.181e-05, -97.11528238, -0.00024544, -323.71760793, -0.00081813, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 0.0, 3.55, 0.0)
    ops.node(121007, 0.0, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 26405407.80327706, 11002253.25136544, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 106.80827665, 0.00067617, 129.64893473, 0.04792663, 12.96489347, 0.1158269, -106.80827665, -0.00067617, -129.64893473, -0.04792663, -12.96489347, -0.1158269, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 106.80827665, 0.00067617, 129.64893473, 0.04792663, 12.96489347, 0.1158269, -106.80827665, -0.00067617, -129.64893473, -0.04792663, -12.96489347, -0.1158269, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 165.4792685, 0.01352337, 165.4792685, 0.0405701, 115.83548795, -2313.51389736, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 41.36981712, 8.178e-05, 124.10945137, 0.00024535, 413.69817124, 0.00081783, -41.36981712, -8.178e-05, -124.10945137, -0.00024535, -413.69817124, -0.00081783, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 165.4792685, 0.01352337, 165.4792685, 0.0405701, 115.83548795, -2313.51389736, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 41.36981712, 8.178e-05, 124.10945137, 0.00024535, 413.69817124, 0.00081783, -41.36981712, -8.178e-05, -124.10945137, -0.00024535, -413.69817124, -0.00081783, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 7.25, 3.55, 0.0)
    ops.node(121008, 7.25, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.2025, 25503508.75089377, 10626461.97953907, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 190.33256394, 0.00063859, 230.5874169, 0.04289688, 23.05874169, 0.09763796, -190.33256394, -0.00063859, -230.5874169, -0.04289688, -23.05874169, -0.09763796, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 214.4273332, 0.00063859, 259.77816854, 0.04289688, 25.97781685, 0.09763796, -214.4273332, -0.00063859, -259.77816854, -0.04289688, -25.97781685, -0.09763796, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 207.49700021, 0.01277184, 207.49700021, 0.03831553, 145.24790015, -2851.52709262, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 51.87425005, 8.389e-05, 155.62275016, 0.00025167, 518.74250052, 0.00083891, -51.87425005, -8.389e-05, -155.62275016, -0.00025167, -518.74250052, -0.00083891, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 207.49700021, 0.01277184, 207.49700021, 0.03831553, 145.24790015, -2851.52709262, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 51.87425005, 8.389e-05, 155.62275016, 0.00025167, 518.74250052, 0.00083891, -51.87425005, -8.389e-05, -155.62275016, -0.00025167, -518.74250052, -0.00083891, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 14.5, 3.55, 0.0)
    ops.node(121009, 14.5, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.16, 28230383.34066348, 11762659.72527645, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 160.01105913, 0.00068389, 193.48113296, 0.04935975, 19.3481133, 0.11821083, -160.01105913, -0.00068389, -193.48113296, -0.04935975, -19.3481133, -0.11821083, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 165.50903046, 0.00068389, 200.12913422, 0.04935975, 20.01291342, 0.11821083, -165.50903046, -0.00068389, -200.12913422, -0.04935975, -20.01291342, -0.11821083, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 197.21162552, 0.01367776, 197.21162552, 0.04103328, 138.04813787, -2940.33702172, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 49.30290638, 9.116e-05, 147.90871914, 0.00027349, 493.02906381, 0.00091165, -49.30290638, -9.116e-05, -147.90871914, -0.00027349, -493.02906381, -0.00091165, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 197.21162552, 0.01367776, 197.21162552, 0.04103328, 138.04813787, -2940.33702172, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 49.30290638, 9.116e-05, 147.90871914, 0.00027349, 493.02906381, 0.00091165, -49.30290638, -9.116e-05, -147.90871914, -0.00027349, -493.02906381, -0.00091165, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 17.65, 3.55, 0.0)
    ops.node(121010, 17.65, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.16, 26200863.45402438, 10917026.43917683, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 148.97507286, 0.00066367, 180.40820747, 0.04637864, 18.04082075, 0.10885057, -148.97507286, -0.00066367, -180.40820747, -0.04637864, -18.04082075, -0.10885057, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 153.98016699, 0.00066367, 186.46935611, 0.04637864, 18.64693561, 0.10885057, -153.98016699, -0.00066367, -186.46935611, -0.04637864, -18.64693561, -0.10885057, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 172.89787993, 0.01327344, 172.89787993, 0.03982032, 121.02851595, -2423.23075314, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 43.22446998, 8.612e-05, 129.67340995, 0.00025835, 432.24469982, 0.00086116, -43.22446998, -8.612e-05, -129.67340995, -0.00025835, -432.24469982, -0.00086116, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 172.89787993, 0.01327344, 172.89787993, 0.03982032, 121.02851595, -2423.23075314, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 43.22446998, 8.612e-05, 129.67340995, 0.00025835, 432.24469982, 0.00086116, -43.22446998, -8.612e-05, -129.67340995, -0.00025835, -432.24469982, -0.00086116, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 24.9, 3.55, 0.0)
    ops.node(121011, 24.9, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.2025, 25973024.81783127, 10822093.67409636, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 182.07623857, 0.00061264, 220.57774588, 0.0453621, 22.05777459, 0.10165071, -182.07623857, -0.00061264, -220.57774588, -0.0453621, -22.05777459, -0.10165071, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 204.0496312, 0.00061264, 247.1975918, 0.0453621, 24.71975918, 0.10165071, -204.0496312, -0.00061264, -247.1975918, -0.0453621, -24.71975918, -0.10165071, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 208.76442898, 0.01225279, 208.76442898, 0.03675838, 146.13510028, -2805.22205271, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 52.19110724, 8.288e-05, 156.57332173, 0.00024863, 521.91107244, 0.00082878, -52.19110724, -8.288e-05, -156.57332173, -0.00024863, -521.91107244, -0.00082878, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 208.76442898, 0.01225279, 208.76442898, 0.03675838, 146.13510028, -2805.22205271, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 52.19110724, 8.288e-05, 156.57332173, 0.00024863, 521.91107244, 0.00082878, -52.19110724, -8.288e-05, -156.57332173, -0.00024863, -521.91107244, -0.00082878, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 32.15, 3.55, 0.0)
    ops.node(121012, 32.15, 3.55, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.16, 28242818.79137745, 11767841.16307394, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 102.65671223, 0.00060533, 124.36782984, 0.05153184, 12.43678298, 0.12449879, -102.65671223, -0.00060533, -124.36782984, -0.05153184, -12.43678298, -0.12449879, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 102.65671223, 0.00060533, 124.36782984, 0.05153184, 12.43678298, 0.12449879, -102.65671223, -0.00060533, -124.36782984, -0.05153184, -12.43678298, -0.12449879, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 203.28070632, 0.01210665, 203.28070632, 0.03631995, 142.29649443, -3473.99617892, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 50.82017658, 9.393e-05, 152.46052974, 0.00028179, 508.2017658, 0.00093929, -50.82017658, -9.393e-05, -152.46052974, -0.00028179, -508.2017658, -0.00093929, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 203.28070632, 0.01210665, 203.28070632, 0.03631995, 142.29649443, -3473.99617892, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 50.82017658, 9.393e-05, 152.46052974, 0.00028179, 508.2017658, 0.00093929, -50.82017658, -9.393e-05, -152.46052974, -0.00028179, -508.2017658, -0.00093929, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 7.1, 0.0)
    ops.node(121013, 0.0, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.16, 27650893.35929574, 11521205.56637323, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 105.25321308, 0.00065871, 127.61241899, 0.04922566, 12.7612419, 0.12068023, -105.25321308, -0.00065871, -127.61241899, -0.04922566, -12.7612419, -0.12068023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 105.25321308, 0.00065871, 127.61241899, 0.04922566, 12.7612419, 0.12068023, -105.25321308, -0.00065871, -127.61241899, -0.04922566, -12.7612419, -0.12068023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 187.1116159, 0.0131742, 187.1116159, 0.0395226, 130.97813113, -2914.19023421, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 46.77790397, 8.831e-05, 140.33371192, 0.00026493, 467.77903974, 0.00088308, -46.77790397, -8.831e-05, -140.33371192, -0.00026493, -467.77903974, -0.00088308, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 187.1116159, 0.0131742, 187.1116159, 0.0395226, 130.97813113, -2914.19023421, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 46.77790397, 8.831e-05, 140.33371192, 0.00026493, 467.77903974, 0.00088308, -46.77790397, -8.831e-05, -140.33371192, -0.00026493, -467.77903974, -0.00088308, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 7.25, 7.1, 0.0)
    ops.node(121014, 7.25, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.2025, 24869145.18893842, 10362143.82872434, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 187.77782118, 0.00060335, 227.45926168, 0.04461132, 22.74592617, 0.09713303, -187.77782118, -0.00060335, -227.45926168, -0.04461132, -22.74592617, -0.09713303, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 204.03640253, 0.00060335, 247.15362647, 0.04461132, 24.71536265, 0.09713303, -204.03640253, -0.00060335, -247.15362647, -0.04461132, -24.71536265, -0.09713303, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 216.40246794, 0.01206699, 216.40246794, 0.03620098, 151.48172756, -3271.77579467, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 54.10061699, 8.972e-05, 162.30185096, 0.00026917, 541.00616985, 0.00089724, -54.10061699, -8.972e-05, -162.30185096, -0.00026917, -541.00616985, -0.00089724, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 216.40246794, 0.01206699, 216.40246794, 0.03620098, 151.48172756, -3271.77579467, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 54.10061699, 8.972e-05, 162.30185096, 0.00026917, 541.00616985, 0.00089724, -54.10061699, -8.972e-05, -162.30185096, -0.00026917, -541.00616985, -0.00089724, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 14.5, 7.1, 0.0)
    ops.node(121015, 14.5, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 27553831.27838653, 11480763.03266105, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 125.88787439, 0.00064093, 152.53043242, 0.04603065, 15.25304324, 0.11561099, -125.88787439, -0.00064093, -152.53043242, -0.04603065, -15.25304324, -0.11561099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 130.41792515, 0.00064093, 158.01921047, 0.04603065, 15.80192105, 0.11561099, -130.41792515, -0.00064093, -158.01921047, -0.04603065, -15.80192105, -0.11561099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 173.07781151, 0.01281851, 173.07781151, 0.03845553, 121.15446806, -2323.27890746, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 43.26945288, 8.197e-05, 129.80835863, 0.00024592, 432.69452877, 0.00081973, -43.26945288, -8.197e-05, -129.80835863, -0.00024592, -432.69452877, -0.00081973, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 173.07781151, 0.01281851, 173.07781151, 0.03845553, 121.15446806, -2323.27890746, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 43.26945288, 8.197e-05, 129.80835863, 0.00024592, 432.69452877, 0.00081973, -43.26945288, -8.197e-05, -129.80835863, -0.00024592, -432.69452877, -0.00081973, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 17.65, 7.1, 0.0)
    ops.node(121016, 17.65, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.16, 25335490.09793978, 10556454.20747491, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 127.1471048, 0.00065738, 154.25020753, 0.04644678, 15.42502075, 0.10891808, -127.1471048, -0.00065738, -154.25020753, -0.04644678, -15.42502075, -0.10891808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 131.9926674, 0.00065738, 160.12866648, 0.04644678, 16.01286665, 0.10891808, -131.9926674, -0.00065738, -160.12866648, -0.04644678, -16.01286665, -0.10891808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 167.35382445, 0.01314761, 167.35382445, 0.03944284, 117.14767711, -2478.25396897, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 41.83845611, 8.62e-05, 125.51536834, 0.00025861, 418.38456112, 0.00086202, -41.83845611, -8.62e-05, -125.51536834, -0.00025861, -418.38456112, -0.00086202, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 167.35382445, 0.01314761, 167.35382445, 0.03944284, 117.14767711, -2478.25396897, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 41.83845611, 8.62e-05, 125.51536834, 0.00025861, 418.38456112, 0.00086202, -41.83845611, -8.62e-05, -125.51536834, -0.00025861, -418.38456112, -0.00086202, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 24.9, 7.1, 0.0)
    ops.node(121017, 24.9, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.2025, 29494634.06406985, 12289430.8600291, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 204.78071364, 0.00060091, 247.21557684, 0.04436433, 24.72155768, 0.10999924, -204.78071364, -0.00060091, -247.21557684, -0.04436433, -24.72155768, -0.10999924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 222.8640147, 0.00060091, 269.04611754, 0.04436433, 26.90461175, 0.10999924, -222.8640147, -0.00060091, -269.04611754, -0.04436433, -26.90461175, -0.10999924, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 224.80573163, 0.01201813, 224.80573163, 0.03605439, 157.36401214, -2645.79457669, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 56.20143291, 7.859e-05, 168.60429872, 0.00023577, 562.01432907, 0.0007859, -56.20143291, -7.859e-05, -168.60429872, -0.00023577, -562.01432907, -0.0007859, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 224.80573163, 0.01201813, 224.80573163, 0.03605439, 157.36401214, -2645.79457669, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 56.20143291, 7.859e-05, 168.60429872, 0.00023577, 562.01432907, 0.0007859, -56.20143291, -7.859e-05, -168.60429872, -0.00023577, -562.01432907, -0.0007859, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 32.15, 7.1, 0.0)
    ops.node(121018, 32.15, 7.1, 2.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.16, 30201907.96195455, 12584128.31748106, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 103.92966609, 0.00062545, 125.46901875, 0.04944046, 12.54690187, 0.12671474, -103.92966609, -0.00062545, -125.46901875, -0.04944046, -12.54690187, -0.12671474, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 103.92966609, 0.00062545, 125.46901875, 0.04944046, 12.54690187, 0.12671474, -103.92966609, -0.00062545, -125.46901875, -0.04944046, -12.54690187, -0.12671474, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 194.75040327, 0.0125091, 194.75040327, 0.03752729, 136.32528229, -2734.4620003, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 48.68760082, 8.415e-05, 146.06280245, 0.00025245, 486.87600818, 0.0008415, -48.68760082, -8.415e-05, -146.06280245, -0.00025245, -486.87600818, -0.0008415, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 194.75040327, 0.0125091, 194.75040327, 0.03752729, 136.32528229, -2734.4620003, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 48.68760082, 8.415e-05, 146.06280245, 0.00025245, 486.87600818, 0.0008415, -48.68760082, -8.415e-05, -146.06280245, -0.00025245, -486.87600818, -0.0008415, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 0.0, 10.65, 0.0)
    ops.node(121019, 0.0, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.1225, 27433849.34831724, 11430770.56179885, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 74.44051184, 0.00072434, 90.42785837, 0.03599013, 9.04278584, 0.09514823, -74.44051184, -0.00072434, -90.42785837, -0.03599013, -9.04278584, -0.09514823, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 70.23374011, 0.00072434, 85.31761197, 0.03599013, 8.5317612, 0.09514823, -70.23374011, -0.00072434, -85.31761197, -0.03599013, -8.5317612, -0.09514823, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 116.61424776, 0.01448688, 116.61424776, 0.04346063, 81.62997343, -1410.46648912, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 29.15356194, 7.245e-05, 87.46068582, 0.00021736, 291.5356194, 0.00072453, -29.15356194, -7.245e-05, -87.46068582, -0.00021736, -291.5356194, -0.00072453, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 116.61424776, 0.01448688, 116.61424776, 0.04346063, 81.62997343, -1410.46648912, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 29.15356194, 7.245e-05, 87.46068582, 0.00021736, 291.5356194, 0.00072453, -29.15356194, -7.245e-05, -87.46068582, -0.00021736, -291.5356194, -0.00072453, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 7.25, 10.65, 0.0)
    ops.node(121020, 7.25, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.2025, 30115486.64328622, 12548119.43470259, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 157.91342781, 0.00062385, 190.79424816, 0.04286477, 19.07942482, 0.11385133, -157.91342781, -0.00062385, -190.79424816, -0.04286477, -19.07942482, -0.11385133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 175.11594431, 0.00062385, 211.57868206, 0.04286477, 21.15786821, 0.11385133, -175.11594431, -0.00062385, -211.57868206, -0.04286477, -21.15786821, -0.11385133, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 215.22438698, 0.01247705, 215.22438698, 0.03743115, 150.65707089, -2457.1936725, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 53.80609674, 7.369e-05, 161.41829023, 0.00022107, 538.06096745, 0.0007369, -53.80609674, -7.369e-05, -161.41829023, -0.00022107, -538.06096745, -0.0007369, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 215.22438698, 0.01247705, 215.22438698, 0.03743115, 150.65707089, -2457.1936725, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 53.80609674, 7.369e-05, 161.41829023, 0.00022107, 538.06096745, 0.0007369, -53.80609674, -7.369e-05, -161.41829023, -0.00022107, -538.06096745, -0.0007369, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 14.5, 10.65, 0.0)
    ops.node(121021, 14.5, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.1225, 24201301.1982156, 10083875.4992565, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 81.55351809, 0.00072828, 98.89332808, 0.03512381, 9.88933281, 0.08105009, -81.55351809, -0.00072828, -98.89332808, -0.03512381, -9.88933281, -0.08105009, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 81.55351809, 0.00072828, 98.89332808, 0.03512381, 9.88933281, 0.08105009, -81.55351809, -0.00072828, -98.89332808, -0.03512381, -9.88933281, -0.08105009, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 131.3617744, 0.01456554, 131.3617744, 0.04369663, 91.95324208, -2149.15469931, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 32.8404436, 9.252e-05, 98.5213308, 0.00027755, 328.404436, 0.00092518, -32.8404436, -9.252e-05, -98.5213308, -0.00027755, -328.404436, -0.00092518, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 131.3617744, 0.01456554, 131.3617744, 0.04369663, 91.95324208, -2149.15469931, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 32.8404436, 9.252e-05, 98.5213308, 0.00027755, 328.404436, 0.00092518, -32.8404436, -9.252e-05, -98.5213308, -0.00027755, -328.404436, -0.00092518, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 17.65, 10.65, 0.0)
    ops.node(121022, 17.65, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 27502072.27622139, 11459196.78175891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 80.98822007, 0.00069161, 98.12450226, 0.03370019, 9.81245023, 0.08868355, -80.98822007, -0.00069161, -98.12450226, -0.03370019, -9.81245023, -0.08868355, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 80.98822007, 0.00069161, 98.12450226, 0.03370019, 9.81245023, 0.08868355, -80.98822007, -0.00069161, -98.12450226, -0.03370019, -9.81245023, -0.08868355, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 126.31749017, 0.01383212, 126.31749017, 0.04149637, 88.42224312, -1572.85566625, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 31.57937254, 7.829e-05, 94.73811763, 0.00023486, 315.79372544, 0.00078288, -31.57937254, -7.829e-05, -94.73811763, -0.00023486, -315.79372544, -0.00078288, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 126.31749017, 0.01383212, 126.31749017, 0.04149637, 88.42224312, -1572.85566625, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 31.57937254, 7.829e-05, 94.73811763, 0.00023486, 315.79372544, 0.00078288, -31.57937254, -7.829e-05, -94.73811763, -0.00023486, -315.79372544, -0.00078288, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 24.9, 10.65, 0.0)
    ops.node(121023, 24.9, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.2025, 23975001.20258065, 9989583.83440861, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 146.02872566, 0.00062413, 177.52829724, 0.04470911, 17.75282972, 0.10043138, -146.02872566, -0.00062413, -177.52829724, -0.04470911, -17.75282972, -0.10043138, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 162.54283558, 0.00062413, 197.6046336, 0.04470911, 19.76046336, 0.10043138, -162.54283558, -0.00062413, -197.6046336, -0.04470911, -19.76046336, -0.10043138, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 187.71366511, 0.01248256, 187.71366511, 0.03744767, 131.39956557, -2740.67775392, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 46.92841628, 8.073e-05, 140.78524883, 0.00024219, 469.28416277, 0.00080731, -46.92841628, -8.073e-05, -140.78524883, -0.00024219, -469.28416277, -0.00080731, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 187.71366511, 0.01248256, 187.71366511, 0.03744767, 131.39956557, -2740.67775392, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 46.92841628, 8.073e-05, 140.78524883, 0.00024219, 469.28416277, 0.00080731, -46.92841628, -8.073e-05, -140.78524883, -0.00024219, -469.28416277, -0.00080731, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 32.15, 10.65, 0.0)
    ops.node(121024, 32.15, 10.65, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 27025307.15290509, 11260544.64704379, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 71.45603012, 0.00069861, 86.8461166, 0.03601364, 8.68461166, 0.0943716, -71.45603012, -0.00069861, -86.8461166, -0.03601364, -8.68461166, -0.0943716, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 67.50184117, 0.00069861, 82.0402807, 0.03601364, 8.20402807, 0.0943716, -67.50184117, -0.00069861, -82.0402807, -0.03601364, -8.20402807, -0.0943716, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 115.21731907, 0.01397214, 115.21731907, 0.04191641, 80.65212335, -1411.67563026, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 28.80432977, 7.267e-05, 86.4129893, 0.000218, 288.04329768, 0.00072668, -28.80432977, -7.267e-05, -86.4129893, -0.000218, -288.04329768, -0.00072668, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 115.21731907, 0.01397214, 115.21731907, 0.04191641, 80.65212335, -1411.67563026, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 28.80432977, 7.267e-05, 86.4129893, 0.000218, 288.04329768, 0.00072668, -28.80432977, -7.267e-05, -86.4129893, -0.000218, -288.04329768, -0.00072668, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.225)
    ops.node(122001, 0.0, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1001, 171001, 122001, 0.1225, 24433034.88105787, 10180431.20044078, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21001, 79.06863832, 0.00078714, 96.6124626, 0.05631508, 9.66124626, 0.138894, -79.06863832, -0.00078714, -96.6124626, -0.05631508, -9.66124626, -0.138894, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11001, 69.06075653, 0.00078714, 84.38402252, 0.05631508, 8.43840225, 0.138894, -69.06075653, -0.00078714, -84.38402252, -0.05631508, -8.43840225, -0.138894, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21001, 1001, 0.0, 151.23576541, 0.01574282, 151.23576541, 0.04722845, 105.86503579, -4265.29420301, 0.05, 2, 0, 71001, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 41001, 37.80894135, 0.0001055, 113.42682406, 0.00031651, 378.08941352, 0.00105505, -37.80894135, -0.0001055, -113.42682406, -0.00031651, -378.08941352, -0.00105505, 0.4, 0.3, 0.003, 0.0, 0.0, 21001, 2)
    ops.limitCurve('ThreePoint', 11001, 1001, 0.0, 151.23576541, 0.01574282, 151.23576541, 0.04722845, 105.86503579, -4265.29420301, 0.05, 2, 0, 71001, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 31001, 37.80894135, 0.0001055, 113.42682406, 0.00031651, 378.08941352, 0.00105505, -37.80894135, -0.0001055, -113.42682406, -0.00031651, -378.08941352, -0.00105505, 0.4, 0.3, 0.003, 0.0, 0.0, 11001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1001, 99999, 'P', 41001, 'Vy', 31001, 'Vz', 21001, 'My', 11001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 1001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 1001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 7.25, 0.0, 3.225)
    ops.node(122002, 7.25, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1002, 171002, 122002, 0.2025, 24791109.24488717, 10329628.85203632, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21002, 122.08583045, 0.00058749, 149.00916677, 0.02311245, 14.90091668, 0.06090486, -122.08583045, -0.00058749, -149.00916677, -0.02311245, -14.90091668, -0.06090486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11002, 101.53071569, 0.00058749, 123.92107496, 0.02311245, 12.3921075, 0.06090486, -101.53071569, -0.00058749, -123.92107496, -0.02311245, -12.3921075, -0.06090486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21002, 1002, 0.0, 147.91613675, 0.01174985, 147.91613675, 0.03524955, 103.54129573, -1527.34490148, 0.05, 2, 0, 71002, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 41002, 36.97903419, 6.152e-05, 110.93710257, 0.00018456, 369.79034188, 0.00061521, -36.97903419, -6.152e-05, -110.93710257, -0.00018456, -369.79034188, -0.00061521, 0.4, 0.3, 0.003, 0.0, 0.0, 21002, 2)
    ops.limitCurve('ThreePoint', 11002, 1002, 0.0, 147.91613675, 0.01174985, 147.91613675, 0.03524955, 103.54129573, -1527.34490148, 0.05, 2, 0, 71002, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 31002, 36.97903419, 6.152e-05, 110.93710257, 0.00018456, 369.79034188, 0.00061521, -36.97903419, -6.152e-05, -110.93710257, -0.00018456, -369.79034188, -0.00061521, 0.4, 0.3, 0.003, 0.0, 0.0, 11002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1002, 99999, 'P', 41002, 'Vy', 31002, 'Vz', 21002, 'My', 11002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 1002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 1002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 24.9, 0.0, 3.225)
    ops.node(122005, 24.9, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.2025, 28081799.69338064, 11700749.87224193, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 122.31497882, 0.00054651, 148.70836373, 0.02563251, 14.87083637, 0.06737792, -122.31497882, -0.00054651, -148.70836373, -0.02563251, -14.87083637, -0.06737792, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 101.32716551, 0.00054651, 123.19175566, 0.02563251, 12.31917557, 0.06737792, -101.32716551, -0.00054651, -123.19175566, -0.02563251, -12.31917557, -0.06737792, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 172.14971511, 0.01093015, 172.14971511, 0.03279046, 120.50480058, -1713.24815102, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 43.03742878, 6.321e-05, 129.11228633, 0.00018963, 430.37428778, 0.0006321, -43.03742878, -6.321e-05, -129.11228633, -0.00018963, -430.37428778, -0.0006321, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 172.14971511, 0.01093015, 172.14971511, 0.03279046, 120.50480058, -1713.24815102, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 43.03742878, 6.321e-05, 129.11228633, 0.00018963, 430.37428778, 0.0006321, -43.03742878, -6.321e-05, -129.11228633, -0.00018963, -430.37428778, -0.0006321, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 32.15, 0.0, 3.225)
    ops.node(122006, 32.15, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1225, 25671816.96329775, 10696590.40137406, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 71.79043964, 0.00066502, 87.63404812, 0.05484409, 8.76340481, 0.14100547, -71.79043964, -0.00066502, -87.63404812, -0.05484409, -8.76340481, -0.14100547, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 62.53692572, 0.00066502, 76.33835347, 0.05484409, 7.63383535, 0.14100547, -62.53692572, -0.00066502, -76.33835347, -0.05484409, -7.63383535, -0.14100547, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 138.16877225, 0.0133003, 138.16877225, 0.0399009, 96.71814058, -3132.1757331, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 34.54219306, 9.174e-05, 103.62657919, 0.00027521, 345.42193064, 0.00091738, -34.54219306, -9.174e-05, -103.62657919, -0.00027521, -345.42193064, -0.00091738, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 138.16877225, 0.0133003, 138.16877225, 0.0399009, 96.71814058, -3132.1757331, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 34.54219306, 9.174e-05, 103.62657919, 0.00027521, 345.42193064, 0.00091738, -34.54219306, -9.174e-05, -103.62657919, -0.00027521, -345.42193064, -0.00091738, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 0.0, 3.55, 3.25)
    ops.node(122007, 0.0, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 24562320.24335422, 10234300.10139759, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 111.36478924, 0.00067806, 135.81172581, 0.05087501, 13.58117258, 0.12072486, -111.36478924, -0.00067806, -135.81172581, -0.05087501, -13.58117258, -0.12072486, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 103.66083719, 0.00067806, 126.41659266, 0.05087501, 12.64165927, 0.12072486, -103.66083719, -0.00067806, -126.41659266, -0.05087501, -12.64165927, -0.12072486, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 153.30486586, 0.0135613, 153.30486586, 0.04068389, 107.3134061, -2545.42068287, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 38.32621647, 8.145e-05, 114.9786494, 0.00024435, 383.26216466, 0.00081451, -38.32621647, -8.145e-05, -114.9786494, -0.00024435, -383.26216466, -0.00081451, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 153.30486586, 0.0135613, 153.30486586, 0.04068389, 107.3134061, -2545.42068287, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 38.32621647, 8.145e-05, 114.9786494, 0.00024435, 383.26216466, 0.00081451, -38.32621647, -8.145e-05, -114.9786494, -0.00024435, -383.26216466, -0.00081451, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 7.25, 3.55, 3.25)
    ops.node(122008, 7.25, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.2025, 25627691.6281012, 10678204.84504217, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 136.66795523, 0.00058039, 166.2690345, 0.03400318, 16.62690345, 0.078835, -136.66795523, -0.00058039, -166.2690345, -0.03400318, -16.62690345, -0.078835, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 121.41410715, 0.00058039, 147.71133685, 0.03400318, 14.77113368, 0.078835, -121.41410715, -0.00058039, -147.71133685, -0.03400318, -14.77113368, -0.078835, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 169.06150825, 0.01160772, 169.06150825, 0.03482316, 118.34305577, -1876.79121135, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 42.26537706, 6.802e-05, 126.79613119, 0.00020406, 422.65377062, 0.00068021, -42.26537706, -6.802e-05, -126.79613119, -0.00020406, -422.65377062, -0.00068021, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 169.06150825, 0.01160772, 169.06150825, 0.03482316, 118.34305577, -1876.79121135, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 42.26537706, 6.802e-05, 126.79613119, 0.00020406, 422.65377062, 0.00068021, -42.26537706, -6.802e-05, -126.79613119, -0.00020406, -422.65377062, -0.00068021, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 14.5, 3.55, 3.25)
    ops.node(122009, 14.5, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.16, 26532138.40400457, 11055057.66833524, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 100.0111615, 0.00059116, 121.55250033, 0.0491951, 12.15525003, 0.12030286, -100.0111615, -0.00059116, -121.55250033, -0.0491951, -12.15525003, -0.12030286, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 90.94820684, 0.00059116, 110.53748178, 0.0491951, 11.05374818, 0.12030286, -90.94820684, -0.00059116, -110.53748178, -0.0491951, -11.05374818, -0.12030286, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 184.48228975, 0.01182323, 184.48228975, 0.03546968, 129.13760282, -3219.42777577, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 46.12057244, 9.074e-05, 138.36171731, 0.00027222, 461.20572437, 0.00090739, -46.12057244, -9.074e-05, -138.36171731, -0.00027222, -461.20572437, -0.00090739, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 184.48228975, 0.01182323, 184.48228975, 0.03546968, 129.13760282, -3219.42777577, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 46.12057244, 9.074e-05, 138.36171731, 0.00027222, 461.20572437, 0.00090739, -46.12057244, -9.074e-05, -138.36171731, -0.00027222, -461.20572437, -0.00090739, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 17.65, 3.55, 3.25)
    ops.node(122010, 17.65, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.16, 27270427.59172032, 11362678.1632168, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 106.38554726, 0.0006405, 129.20013702, 0.04896506, 12.9200137, 0.12203986, -106.38554726, -0.0006405, -129.20013702, -0.04896506, -12.9200137, -0.12203986, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 96.72871417, 0.0006405, 117.47237709, 0.04896506, 11.74723771, 0.12203986, -96.72871417, -0.0006405, -117.47237709, -0.04896506, -11.74723771, -0.12203986, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 185.00377433, 0.01281006, 185.00377433, 0.03843017, 129.50264203, -3093.6770341, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 46.25094358, 8.853e-05, 138.75283075, 0.0002656, 462.50943582, 0.00088532, -46.25094358, -8.853e-05, -138.75283075, -0.0002656, -462.50943582, -0.00088532, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 185.00377433, 0.01281006, 185.00377433, 0.03843017, 129.50264203, -3093.6770341, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 46.25094358, 8.853e-05, 138.75283075, 0.0002656, 462.50943582, 0.00088532, -46.25094358, -8.853e-05, -138.75283075, -0.0002656, -462.50943582, -0.00088532, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 24.9, 3.55, 3.25)
    ops.node(122011, 24.9, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.2025, 25479924.09391183, 10616635.03912993, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 144.26105092, 0.00059952, 175.52033087, 0.0322899, 17.55203309, 0.07682607, -144.26105092, -0.00059952, -175.52033087, -0.0322899, -17.55203309, -0.07682607, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 127.11413937, 0.00059952, 154.65793198, 0.0322899, 15.4657932, 0.07682607, -127.11413937, -0.00059952, -154.65793198, -0.0322899, -15.4657932, -0.07682607, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 164.2647931, 0.01199039, 164.2647931, 0.03597117, 114.98535517, -1756.642046, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 41.06619827, 6.647e-05, 123.19859482, 0.00019942, 410.66198274, 0.00066474, -41.06619827, -6.647e-05, -123.19859482, -0.00019942, -410.66198274, -0.00066474, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 164.2647931, 0.01199039, 164.2647931, 0.03597117, 114.98535517, -1756.642046, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 41.06619827, 6.647e-05, 123.19859482, 0.00019942, 410.66198274, 0.00066474, -41.06619827, -6.647e-05, -123.19859482, -0.00019942, -410.66198274, -0.00066474, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 32.15, 3.55, 3.25)
    ops.node(122012, 32.15, 3.55, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.16, 28372971.32706002, 11822071.38627501, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 110.05777875, 0.00064312, 133.65793759, 0.05244804, 13.36579376, 0.13167266, -110.05777875, -0.00064312, -133.65793759, -0.05244804, -13.36579376, -0.13167266, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 102.90730197, 0.00064312, 124.97415357, 0.05244804, 12.49741536, 0.13167266, -102.90730197, -0.00064312, -124.97415357, -0.05244804, -12.49741536, -0.13167266, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 174.806729, 0.01286242, 174.806729, 0.03858727, 122.3647103, -2745.75601875, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 43.70168225, 8.04e-05, 131.10504675, 0.0002412, 437.0168225, 0.00080401, -43.70168225, -8.04e-05, -131.10504675, -0.0002412, -437.0168225, -0.00080401, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 174.806729, 0.01286242, 174.806729, 0.03858727, 122.3647103, -2745.75601875, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 43.70168225, 8.04e-05, 131.10504675, 0.0002412, 437.0168225, 0.00080401, -43.70168225, -8.04e-05, -131.10504675, -0.0002412, -437.0168225, -0.00080401, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 7.1, 3.25)
    ops.node(122013, 0.0, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.16, 27364793.8075369, 11401997.41980704, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 108.79467924, 0.00065015, 132.33880301, 0.05051919, 13.2338803, 0.12769893, -108.79467924, -0.00065015, -132.33880301, -0.05051919, -13.2338803, -0.12769893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 101.76460806, 0.00065015, 123.78736271, 0.05051919, 12.37873627, 0.12769893, -101.76460806, -0.00065015, -123.78736271, -0.05051919, -12.37873627, -0.12769893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 157.52660175, 0.01300298, 157.52660175, 0.03900893, 110.26862123, -2199.71442354, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 39.38165044, 7.512e-05, 118.14495131, 0.00022537, 393.81650438, 0.00075123, -39.38165044, -7.512e-05, -118.14495131, -0.00022537, -393.81650438, -0.00075123, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 157.52660175, 0.01300298, 157.52660175, 0.03900893, 110.26862123, -2199.71442354, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 39.38165044, 7.512e-05, 118.14495131, 0.00022537, 393.81650438, 0.00075123, -39.38165044, -7.512e-05, -118.14495131, -0.00022537, -393.81650438, -0.00075123, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 7.25, 7.1, 3.25)
    ops.node(122014, 7.25, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.2025, 27502014.1356547, 11459172.55652279, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 138.54612314, 0.00057554, 168.25590992, 0.03403439, 16.82559099, 0.08217817, -138.54612314, -0.00057554, -168.25590992, -0.03403439, -16.82559099, -0.08217817, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 123.27508413, 0.00057554, 149.71015414, 0.03403439, 14.97101541, 0.08217817, -123.27508413, -0.00057554, -149.71015414, -0.03403439, -14.97101541, -0.08217817, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 183.10743745, 0.0115108, 183.10743745, 0.03453241, 128.17520621, -1980.55850632, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 45.77685936, 6.865e-05, 137.33057809, 0.00020595, 457.76859362, 0.00068651, -45.77685936, -6.865e-05, -137.33057809, -0.00020595, -457.76859362, -0.00068651, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 183.10743745, 0.0115108, 183.10743745, 0.03453241, 128.17520621, -1980.55850632, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 45.77685936, 6.865e-05, 137.33057809, 0.00020595, 457.76859362, 0.00068651, -45.77685936, -6.865e-05, -137.33057809, -0.00020595, -457.76859362, -0.00068651, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 14.5, 7.1, 3.25)
    ops.node(122015, 14.5, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 26768059.92980502, 11153358.30408542, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 96.95213926, 0.00058884, 117.94353131, 0.05015381, 11.79435313, 0.12440554, -96.95213926, -0.00058884, -117.94353131, -0.05015381, -11.79435313, -0.12440554, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 87.74957244, 0.00058884, 106.74848976, 0.05015381, 10.67484898, 0.12440554, -87.74957244, -0.00058884, -106.74848976, -0.05015381, -10.67484898, -0.12440554, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 180.18897241, 0.01177682, 180.18897241, 0.03533046, 126.13228069, -3194.39640093, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 45.0472431, 8.785e-05, 135.14172931, 0.00026354, 450.47243103, 0.00087846, -45.0472431, -8.785e-05, -135.14172931, -0.00026354, -450.47243103, -0.00087846, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 180.18897241, 0.01177682, 180.18897241, 0.03533046, 126.13228069, -3194.39640093, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 45.0472431, 8.785e-05, 135.14172931, 0.00026354, 450.47243103, 0.00087846, -45.0472431, -8.785e-05, -135.14172931, -0.00026354, -450.47243103, -0.00087846, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 17.65, 7.1, 3.25)
    ops.node(122016, 17.65, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.16, 29571098.93943129, 12321291.22476304, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 97.78401015, 0.00058557, 118.41047812, 0.05001137, 11.84104781, 0.13012186, -97.78401015, -0.00058557, -118.41047812, -0.05001137, -11.84104781, -0.13012186, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 88.87380969, 0.00058557, 107.62076828, 0.05001137, 10.76207683, 0.13012186, -88.87380969, -0.00058557, -107.62076828, -0.05001137, -10.76207683, -0.13012186, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 199.71826733, 0.01171136, 199.71826733, 0.03513409, 139.80278713, -3508.05890235, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 49.92956683, 8.814e-05, 149.78870049, 0.00026441, 499.29566831, 0.00088138, -49.92956683, -8.814e-05, -149.78870049, -0.00026441, -499.29566831, -0.00088138, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 199.71826733, 0.01171136, 199.71826733, 0.03513409, 139.80278713, -3508.05890235, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 49.92956683, 8.814e-05, 149.78870049, 0.00026441, 499.29566831, 0.00088138, -49.92956683, -8.814e-05, -149.78870049, -0.00026441, -499.29566831, -0.00088138, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 24.9, 7.1, 3.25)
    ops.node(122017, 24.9, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.2025, 27973264.05106907, 11655526.68794545, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 133.37523143, 0.00059436, 161.86927686, 0.03603527, 16.18692769, 0.08489657, -133.37523143, -0.00059436, -161.86927686, -0.03603527, -16.18692769, -0.08489657, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 120.55732257, 0.00059436, 146.31297293, 0.03603527, 14.63129729, 0.08489657, -120.55732257, -0.00059436, -146.31297293, -0.03603527, -14.63129729, -0.08489657, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 192.57281376, 0.01188713, 192.57281376, 0.0356614, 134.80096963, -2198.05997299, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 48.14320344, 7.098e-05, 144.42961032, 0.00021295, 481.4320344, 0.00070983, -48.14320344, -7.098e-05, -144.42961032, -0.00021295, -481.4320344, -0.00070983, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 192.57281376, 0.01188713, 192.57281376, 0.0356614, 134.80096963, -2198.05997299, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 48.14320344, 7.098e-05, 144.42961032, 0.00021295, 481.4320344, 0.00070983, -48.14320344, -7.098e-05, -144.42961032, -0.00021295, -481.4320344, -0.00070983, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 32.15, 7.1, 3.25)
    ops.node(122018, 32.15, 7.1, 5.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.16, 25139062.19864048, 10474609.24943353, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 99.1207081, 0.00063042, 120.84703779, 0.05166025, 12.08470378, 0.1232472, -99.1207081, -0.00063042, -120.84703779, -0.05166025, -12.08470378, -0.1232472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 93.05500969, 0.00063042, 113.45179517, 0.05166025, 11.34517952, 0.1232472, -93.05500969, -0.00063042, -113.45179517, -0.05166025, -11.34517952, -0.1232472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 163.74921453, 0.01260844, 163.74921453, 0.03782533, 114.62445017, -2906.97632603, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 40.93730363, 8.5e-05, 122.8119109, 0.00025501, 409.37303632, 0.00085004, -40.93730363, -8.5e-05, -122.8119109, -0.00025501, -409.37303632, -0.00085004, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 163.74921453, 0.01260844, 163.74921453, 0.03782533, 114.62445017, -2906.97632603, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 40.93730363, 8.5e-05, 122.8119109, 0.00025501, 409.37303632, 0.00085004, -40.93730363, -8.5e-05, -122.8119109, -0.00025501, -409.37303632, -0.00085004, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 0.0, 10.65, 3.225)
    ops.node(122019, 0.0, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.1225, 28802688.24714015, 12001120.10297506, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 82.50383391, 0.00069075, 100.22518012, 0.05354084, 10.02251801, 0.14645819, -82.50383391, -0.00069075, -100.22518012, -0.05354084, -10.02251801, -0.14645819, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 71.05563679, 0.00069075, 86.31797648, 0.05354084, 8.63179765, 0.14645819, -71.05563679, -0.00069075, -86.31797648, -0.05354084, -8.63179765, -0.14645819, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 145.63954428, 0.01381494, 145.63954428, 0.04144481, 101.947681, -2931.35504265, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 36.40988607, 8.619e-05, 109.22965821, 0.00025856, 364.09886071, 0.00086187, -36.40988607, -8.619e-05, -109.22965821, -0.00025856, -364.09886071, -0.00086187, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 145.63954428, 0.01381494, 145.63954428, 0.04144481, 101.947681, -2931.35504265, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 36.40988607, 8.619e-05, 109.22965821, 0.00025856, 364.09886071, 0.00086187, -36.40988607, -8.619e-05, -109.22965821, -0.00025856, -364.09886071, -0.00086187, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 7.25, 10.65, 3.225)
    ops.node(122020, 7.25, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.2025, 32318170.82684648, 13465904.51118603, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 120.90548493, 0.00050554, 145.49035347, 0.02773033, 14.54903535, 0.07260261, -120.90548493, -0.00050554, -145.49035347, -0.02773033, -14.54903535, -0.07260261, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 106.84013506, 0.00050554, 128.56496149, 0.02773033, 12.85649615, 0.07260261, -106.84013506, -0.00050554, -128.56496149, -0.02773033, -12.85649615, -0.07260261, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 188.38075238, 0.01011086, 188.38075238, 0.03033259, 131.86652667, -1406.27623478, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 47.0951881, 6.01e-05, 141.28556429, 0.00018031, 470.95188095, 0.00060103, -47.0951881, -6.01e-05, -141.28556429, -0.00018031, -470.95188095, -0.00060103, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 188.38075238, 0.01011086, 188.38075238, 0.03033259, 131.86652667, -1406.27623478, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 47.0951881, 6.01e-05, 141.28556429, 0.00018031, 470.95188095, 0.00060103, -47.0951881, -6.01e-05, -141.28556429, -0.00018031, -470.95188095, -0.00060103, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 14.5, 10.65, 3.225)
    ops.node(122021, 14.5, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.1225, 27469593.70963404, 11445664.04568085, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 61.31046378, 0.00063151, 74.52445165, 0.03363411, 7.45244517, 0.09405812, -61.31046378, -0.00063151, -74.52445165, -0.03363411, -7.45244517, -0.09405812, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 54.16478127, 0.00063151, 65.83869007, 0.03363411, 6.58386901, 0.09405812, -54.16478127, -0.00063151, -65.83869007, -0.03363411, -6.58386901, -0.09405812, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 121.55070581, 0.01263011, 121.55070581, 0.03789032, 85.08549407, -1644.25542706, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 30.38767645, 7.542e-05, 91.16302936, 0.00022627, 303.87676454, 0.00075422, -30.38767645, -7.542e-05, -91.16302936, -0.00022627, -303.87676454, -0.00075422, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 121.55070581, 0.01263011, 121.55070581, 0.03789032, 85.08549407, -1644.25542706, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 30.38767645, 7.542e-05, 91.16302936, 0.00022627, 303.87676454, 0.00075422, -30.38767645, -7.542e-05, -91.16302936, -0.00022627, -303.87676454, -0.00075422, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 17.65, 10.65, 3.225)
    ops.node(122022, 17.65, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 30668497.86614798, 12778540.77756166, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 59.91328672, 0.00059293, 72.37227166, 0.03655122, 7.23722717, 0.10168758, -59.91328672, -0.00059293, -72.37227166, -0.03655122, -7.23722717, -0.10168758, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 53.17828954, 0.00059293, 64.23672992, 0.03655122, 6.42367299, 0.10168758, -53.17828954, -0.00059293, -64.23672992, -0.03655122, -6.42367299, -0.10168758, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 138.02185274, 0.01185863, 138.02185274, 0.03557589, 96.61529692, -1838.96262544, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 34.50546318, 7.671e-05, 103.51638955, 0.00023013, 345.05463185, 0.0007671, -34.50546318, -7.671e-05, -103.51638955, -0.00023013, -345.05463185, -0.0007671, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 138.02185274, 0.01185863, 138.02185274, 0.03557589, 96.61529692, -1838.96262544, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 34.50546318, 7.671e-05, 103.51638955, 0.00023013, 345.05463185, 0.0007671, -34.50546318, -7.671e-05, -103.51638955, -0.00023013, -345.05463185, -0.0007671, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 24.9, 10.65, 3.225)
    ops.node(122023, 24.9, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.2025, 26479004.57992667, 11032918.57496945, 0.00577505, 0.00375891, 0.00375891, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 125.28314879, 0.00054282, 152.68042086, 0.03009034, 15.26804209, 0.07012688, -125.28314879, -0.00054282, -152.68042086, -0.03009034, -15.26804209, -0.07012688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 109.4602063, 0.00054282, 133.3972727, 0.03009034, 13.33972727, 0.07012688, -109.4602063, -0.00054282, -133.3972727, -0.03009034, -13.33972727, -0.07012688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 158.2954636, 0.01085647, 158.2954636, 0.0325694, 110.80682452, -1560.74438459, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 39.5738659, 6.164e-05, 118.7215977, 0.00018492, 395.73865899, 0.00061641, -39.5738659, -6.164e-05, -118.7215977, -0.00018492, -395.73865899, -0.00061641, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 158.2954636, 0.01085647, 158.2954636, 0.0325694, 110.80682452, -1560.74438459, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 39.5738659, 6.164e-05, 118.7215977, 0.00018492, 395.73865899, 0.00061641, -39.5738659, -6.164e-05, -118.7215977, -0.00018492, -395.73865899, -0.00061641, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 32.15, 10.65, 3.225)
    ops.node(122024, 32.15, 10.65, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 27890818.18734644, 11621174.24472768, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 81.36963632, 0.00072611, 99.01962323, 0.05477324, 9.90196232, 0.14600776, -81.36963632, -0.00072611, -99.01962323, -0.05477324, -9.90196232, -0.14600776, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 70.66548754, 0.00072611, 85.99362451, 0.05477324, 8.59936245, 0.14600776, -70.66548754, -0.00072611, -85.99362451, -0.05477324, -8.59936245, -0.14600776, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 145.60779428, 0.01452228, 145.60779428, 0.04356684, 101.925456, -3123.12413561, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 36.40194857, 8.899e-05, 109.20584571, 0.00026696, 364.0194857, 0.00088985, -36.40194857, -8.899e-05, -109.20584571, -0.00026696, -364.0194857, -0.00088985, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 145.60779428, 0.01452228, 145.60779428, 0.04356684, 101.925456, -3123.12413561, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 36.40194857, 8.899e-05, 109.20584571, 0.00026696, 364.0194857, 0.00088985, -36.40194857, -8.899e-05, -109.20584571, -0.00026696, -364.0194857, -0.00088985, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.125)
    ops.node(123001, 0.0, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2001, 172001, 123001, 0.0625, 27021734.7892512, 11259056.162188, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22001, 28.46516284, 0.00090454, 34.64571564, 0.0257246, 3.46457156, 0.07856738, -28.46516284, -0.00090454, -34.64571564, -0.0257246, -3.46457156, -0.07856738, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12001, 28.46516284, 0.00090454, 34.64571564, 0.0257246, 3.46457156, 0.07856738, -28.46516284, -0.00090454, -34.64571564, -0.0257246, -3.46457156, -0.07856738, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22001, 2001, 0.0, 41.10106052, 0.01809081, 41.10106052, 0.05427242, 28.77074237, -566.98919382, 0.05, 2, 0, 72001, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 42001, 10.27526513, 5.081e-05, 30.82579539, 0.00015244, 102.75265131, 0.00050815, -10.27526513, -5.081e-05, -30.82579539, -0.00015244, -102.75265131, -0.00050815, 0.4, 0.3, 0.003, 0.0, 0.0, 22001, 2)
    ops.limitCurve('ThreePoint', 12001, 2001, 0.0, 41.10106052, 0.01809081, 41.10106052, 0.05427242, 28.77074237, -566.98919382, 0.05, 2, 0, 72001, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 32001, 10.27526513, 5.081e-05, 30.82579539, 0.00015244, 102.75265131, 0.00050815, -10.27526513, -5.081e-05, -30.82579539, -0.00015244, -102.75265131, -0.00050815, 0.4, 0.3, 0.003, 0.0, 0.0, 12001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2001, 99999, 'P', 42001, 'Vy', 32001, 'Vz', 22001, 'My', 12001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 2001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 2001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 7.25, 0.0, 6.125)
    ops.node(123002, 7.25, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2002, 172002, 123002, 0.1225, 27078712.61291431, 11282796.92204763, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22002, 59.17263101, 0.00065551, 72.05142465, 0.02435331, 7.20514246, 0.06584598, -59.17263101, -0.00065551, -72.05142465, -0.02435331, -7.20514246, -0.06584598, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12002, 52.07419759, 0.00065551, 63.40803272, 0.02435331, 6.34080327, 0.06584598, -52.07419759, -0.00065551, -63.40803272, -0.02435331, -6.34080327, -0.06584598, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22002, 2002, 0.0, 103.55965786, 0.01311021, 103.55965786, 0.03933062, 72.4917605, -1132.26910326, 0.05, 2, 0, 72002, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 42002, 25.88991447, 6.519e-05, 77.6697434, 0.00019556, 258.89914465, 0.00065186, -25.88991447, -6.519e-05, -77.6697434, -0.00019556, -258.89914465, -0.00065186, 0.4, 0.3, 0.003, 0.0, 0.0, 22002, 2)
    ops.limitCurve('ThreePoint', 12002, 2002, 0.0, 103.55965786, 0.01311021, 103.55965786, 0.03933062, 72.4917605, -1132.26910326, 0.05, 2, 0, 72002, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 32002, 25.88991447, 6.519e-05, 77.6697434, 0.00019556, 258.89914465, 0.00065186, -25.88991447, -6.519e-05, -77.6697434, -0.00019556, -258.89914465, -0.00065186, 0.4, 0.3, 0.003, 0.0, 0.0, 12002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2002, 99999, 'P', 42002, 'Vy', 32002, 'Vz', 22002, 'My', 12002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 2002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 2002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 24.9, 0.0, 6.125)
    ops.node(123005, 24.9, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.1225, 29415860.18708752, 12256608.41128647, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 55.29986777, 0.00061404, 67.05282385, 0.01786346, 6.70528238, 0.06161536, -55.29986777, -0.00061404, -67.05282385, -0.01786346, -6.70528238, -0.06161536, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 49.31781813, 0.00061404, 59.79940107, 0.01786346, 5.97994011, 0.06161536, -49.31781813, -0.00061404, -59.79940107, -0.01786346, -5.97994011, -0.06161536, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 101.04937972, 0.01228075, 101.04937972, 0.03684224, 70.73456581, -787.28552225, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 25.26234493, 5.855e-05, 75.78703479, 0.00017566, 252.6234493, 0.00058553, -25.26234493, -5.855e-05, -75.78703479, -0.00017566, -252.6234493, -0.00058553, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 101.04937972, 0.01228075, 101.04937972, 0.03684224, 70.73456581, -787.28552225, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 25.26234493, 5.855e-05, 75.78703479, 0.00017566, 252.6234493, 0.00058553, -25.26234493, -5.855e-05, -75.78703479, -0.00017566, -252.6234493, -0.00058553, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 32.15, 0.0, 6.125)
    ops.node(123006, 32.15, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 27691366.73448351, 11538069.47270146, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 27.59450297, 0.00091116, 33.55347059, 0.03188778, 3.35534706, 0.08571911, -27.59450297, -0.00091116, -33.55347059, -0.03188778, -3.35534706, -0.08571911, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 27.59450297, 0.00091116, 33.55347059, 0.03188778, 3.35534706, 0.08571911, -27.59450297, -0.00091116, -33.55347059, -0.03188778, -3.35534706, -0.08571911, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 60.30376797, 0.01822311, 60.30376797, 0.05466932, 42.21263758, -792.87163237, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 15.07594199, 7.275e-05, 45.22782598, 0.00021826, 150.75941993, 0.00072753, -15.07594199, -7.275e-05, -45.22782598, -0.00021826, -150.75941993, -0.00072753, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 60.30376797, 0.01822311, 60.30376797, 0.05466932, 42.21263758, -792.87163237, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 15.07594199, 7.275e-05, 45.22782598, 0.00021826, 150.75941993, 0.00072753, -15.07594199, -7.275e-05, -45.22782598, -0.00021826, -150.75941993, -0.00072753, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 0.0, 3.55, 6.15)
    ops.node(123007, 0.0, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 31959918.2927652, 13316632.6219855, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 73.49500869, 0.00067408, 88.57773263, 0.0530278, 8.85777326, 0.15072531, -73.49500869, -0.00067408, -88.57773263, -0.0530278, -8.85777326, -0.15072531, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 73.49500869, 0.00067408, 88.57773263, 0.0530278, 8.85777326, 0.15072531, -73.49500869, -0.00067408, -88.57773263, -0.0530278, -8.85777326, -0.15072531, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 157.56871705, 0.01348167, 157.56871705, 0.040445, 110.29810193, -2999.57090769, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 39.39217926, 8.403e-05, 118.17653779, 0.0002521, 393.92179262, 0.00084035, -39.39217926, -8.403e-05, -118.17653779, -0.0002521, -393.92179262, -0.00084035, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 157.56871705, 0.01348167, 157.56871705, 0.040445, 110.29810193, -2999.57090769, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 39.39217926, 8.403e-05, 118.17653779, 0.0002521, 393.92179262, 0.00084035, -39.39217926, -8.403e-05, -118.17653779, -0.0002521, -393.92179262, -0.00084035, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 7.25, 3.55, 6.15)
    ops.node(123008, 7.25, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.1225, 27745440.79391793, 11560600.33079914, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 74.70984292, 0.00068752, 90.66464955, 0.02563497, 9.06646495, 0.064991, -74.70984292, -0.00068752, -90.66464955, -0.02563497, -9.06646495, -0.064991, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 70.47035713, 0.00068752, 85.51979207, 0.02563497, 8.55197921, 0.064991, -70.47035713, -0.00068752, -85.51979207, -0.02563497, -8.55197921, -0.064991, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 107.05688485, 0.01375041, 107.05688485, 0.04125123, 74.9398194, -1042.32178462, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 26.76422121, 6.577e-05, 80.29266364, 0.00019731, 267.64221213, 0.00065768, -26.76422121, -6.577e-05, -80.29266364, -0.00019731, -267.64221213, -0.00065768, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 107.05688485, 0.01375041, 107.05688485, 0.04125123, 74.9398194, -1042.32178462, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 26.76422121, 6.577e-05, 80.29266364, 0.00019731, 267.64221213, 0.00065768, -26.76422121, -6.577e-05, -80.29266364, -0.00019731, -267.64221213, -0.00065768, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 14.5, 3.55, 6.15)
    ops.node(123009, 14.5, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.1225, 24236924.1569918, 10098718.39874659, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 63.99736138, 0.0006767, 78.02810588, 0.03950409, 7.80281059, 0.09362631, -63.99736138, -0.0006767, -78.02810588, -0.03950409, -7.80281059, -0.09362631, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 60.39180666, 0.0006767, 73.63207143, 0.03950409, 7.36320714, 0.09362631, -60.39180666, -0.0006767, -73.63207143, -0.03950409, -7.36320714, -0.09362631, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 114.36854879, 0.01353409, 114.36854879, 0.04060226, 80.05798415, -1837.16022243, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 28.5921372, 8.043e-05, 85.77641159, 0.00024129, 285.92137198, 0.00080431, -28.5921372, -8.043e-05, -85.77641159, -0.00024129, -285.92137198, -0.00080431, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 114.36854879, 0.01353409, 114.36854879, 0.04060226, 80.05798415, -1837.16022243, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 28.5921372, 8.043e-05, 85.77641159, 0.00024129, 285.92137198, 0.00080431, -28.5921372, -8.043e-05, -85.77641159, -0.00024129, -285.92137198, -0.00080431, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 17.65, 3.55, 6.15)
    ops.node(123010, 17.65, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.1225, 26637972.97810646, 11099155.40754436, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 66.92717282, 0.00075708, 81.46917228, 0.03647402, 8.14691723, 0.09603499, -66.92717282, -0.00075708, -81.46917228, -0.03647402, -8.14691723, -0.09603499, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 63.62417838, 0.00075708, 77.44850009, 0.03647402, 7.74485001, 0.09603499, -63.62417838, -0.00075708, -77.44850009, -0.03647402, -7.74485001, -0.09603499, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 111.28569451, 0.01514165, 111.28569451, 0.04542495, 77.89998616, -1399.24233668, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 27.82142363, 7.121e-05, 83.46427088, 0.00021363, 278.21423628, 0.00071209, -27.82142363, -7.121e-05, -83.46427088, -0.00021363, -278.21423628, -0.00071209, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 111.28569451, 0.01514165, 111.28569451, 0.04542495, 77.89998616, -1399.24233668, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 27.82142363, 7.121e-05, 83.46427088, 0.00021363, 278.21423628, 0.00071209, -27.82142363, -7.121e-05, -83.46427088, -0.00021363, -278.21423628, -0.00071209, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 24.9, 3.55, 6.15)
    ops.node(123011, 24.9, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 30165103.66561431, 12568793.19400596, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 69.89346749, 0.00068421, 84.45202654, 0.02295581, 8.44520265, 0.06501119, -69.89346749, -0.00068421, -84.45202654, -0.02295581, -8.44520265, -0.06501119, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 66.60099906, 0.00068421, 80.47374872, 0.02295581, 8.04737487, 0.06501119, -66.60099906, -0.00068421, -80.47374872, -0.02295581, -8.04737487, -0.06501119, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 110.34068429, 0.01368427, 110.34068429, 0.0410528, 77.238479, -888.89282185, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 27.58517107, 6.235e-05, 82.75551322, 0.00018705, 275.85171073, 0.00062348, -27.58517107, -6.235e-05, -82.75551322, -0.00018705, -275.85171073, -0.00062348, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 110.34068429, 0.01368427, 110.34068429, 0.0410528, 77.238479, -888.89282185, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 27.58517107, 6.235e-05, 82.75551322, 0.00018705, 275.85171073, 0.00062348, -27.58517107, -6.235e-05, -82.75551322, -0.00018705, -275.85171073, -0.00062348, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 32.15, 3.55, 6.15)
    ops.node(123012, 32.15, 3.55, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.1225, 26889488.3976437, 11203953.49901821, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 69.56265, 0.00068463, 84.80199624, 0.05490958, 8.48019962, 0.14449764, -69.56265, -0.00068463, -84.80199624, -0.05490958, -8.48019962, -0.14449764, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 69.56265, 0.00068463, 84.80199624, 0.05490958, 8.48019962, 0.14449764, -69.56265, -0.00068463, -84.80199624, -0.05490958, -8.48019962, -0.14449764, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 142.7166821, 0.01369266, 142.7166821, 0.04107798, 99.90167747, -3215.1421487, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 35.67917053, 9.047e-05, 107.03751158, 0.0002714, 356.79170525, 0.00090466, -35.67917053, -9.047e-05, -107.03751158, -0.0002714, -356.79170525, -0.00090466, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 142.7166821, 0.01369266, 142.7166821, 0.04107798, 99.90167747, -3215.1421487, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 35.67917053, 9.047e-05, 107.03751158, 0.0002714, 356.79170525, 0.00090466, -35.67917053, -9.047e-05, -107.03751158, -0.0002714, -356.79170525, -0.00090466, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 7.1, 6.15)
    ops.node(123013, 0.0, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.1225, 23102799.87197462, 9626166.61332276, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 65.86984882, 0.0007466, 80.53642602, 0.05669758, 8.0536426, 0.13533632, -65.86984882, -0.0007466, -80.53642602, -0.05669758, -8.0536426, -0.13533632, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 65.86984882, 0.0007466, 80.53642602, 0.05669758, 8.0536426, 0.13533632, -65.86984882, -0.0007466, -80.53642602, -0.05669758, -8.0536426, -0.13533632, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 134.37334724, 0.01493206, 134.37334724, 0.04479617, 94.06134307, -3474.66189719, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 33.59333681, 9.914e-05, 100.78001043, 0.00029742, 335.93336809, 0.00099139, -33.59333681, -9.914e-05, -100.78001043, -0.00029742, -335.93336809, -0.00099139, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 134.37334724, 0.01493206, 134.37334724, 0.04479617, 94.06134307, -3474.66189719, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 33.59333681, 9.914e-05, 100.78001043, 0.00029742, 335.93336809, 0.00099139, -33.59333681, -9.914e-05, -100.78001043, -0.00029742, -335.93336809, -0.00099139, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 7.25, 7.1, 6.15)
    ops.node(123014, 7.25, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.1225, 25830910.97060874, 10762879.57108697, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 68.40491281, 0.00068427, 83.16880263, 0.0319062, 8.31688026, 0.07521285, -68.40491281, -0.00068427, -83.16880263, -0.0319062, -8.31688026, -0.07521285, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 64.91281346, 0.00068427, 78.92300055, 0.0319062, 7.89230005, 0.07521285, -64.91281346, -0.00068427, -78.92300055, -0.0319062, -7.89230005, -0.07521285, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 111.26820834, 0.01368537, 111.26820834, 0.04105612, 77.88774584, -1379.73066345, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 27.81705208, 7.342e-05, 83.45115625, 0.00022027, 278.17052084, 0.00073422, -27.81705208, -7.342e-05, -83.45115625, -0.00022027, -278.17052084, -0.00073422, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 111.26820834, 0.01368537, 111.26820834, 0.04105612, 77.88774584, -1379.73066345, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 27.81705208, 7.342e-05, 83.45115625, 0.00022027, 278.17052084, 0.00073422, -27.81705208, -7.342e-05, -83.45115625, -0.00022027, -278.17052084, -0.00073422, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 14.5, 7.1, 6.15)
    ops.node(123015, 14.5, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 24006188.75395412, 10002578.64748088, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 66.36649428, 0.00073215, 81.04524394, 0.03663294, 8.10452439, 0.09269157, -66.36649428, -0.00073215, -81.04524394, -0.03663294, -8.10452439, -0.09269157, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 62.34028762, 0.00073215, 76.1285325, 0.03663294, 7.61285325, 0.09269157, -62.34028762, -0.00073215, -76.1285325, -0.03663294, -7.61285325, -0.09269157, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 103.20429582, 0.01464306, 103.20429582, 0.04392919, 72.24300707, -1525.91502361, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 25.80107395, 7.328e-05, 77.40322186, 0.00021983, 258.01073955, 0.00073277, -25.80107395, -7.328e-05, -77.40322186, -0.00021983, -258.01073955, -0.00073277, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 103.20429582, 0.01464306, 103.20429582, 0.04392919, 72.24300707, -1525.91502361, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 25.80107395, 7.328e-05, 77.40322186, 0.00021983, 258.01073955, 0.00073277, -25.80107395, -7.328e-05, -77.40322186, -0.00021983, -258.01073955, -0.00073277, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 17.65, 7.1, 6.15)
    ops.node(123016, 17.65, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.1225, 34411675.39313839, 14338198.08047433, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 63.19217051, 0.00064317, 75.50525637, 0.03825385, 7.55052564, 0.10833027, -63.19217051, -0.00064317, -75.50525637, -0.03825385, -7.55052564, -0.10833027, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 59.98015351, 0.00064317, 71.66737321, 0.03825385, 7.16673732, 0.10833027, -59.98015351, -0.00064317, -71.66737321, -0.03825385, -7.16673732, -0.10833027, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 153.95348272, 0.01286336, 153.95348272, 0.03859008, 107.7674379, -2113.64533629, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 38.48837068, 7.626e-05, 115.46511204, 0.00022877, 384.8837068, 0.00076257, -38.48837068, -7.626e-05, -115.46511204, -0.00022877, -384.8837068, -0.00076257, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 153.95348272, 0.01286336, 153.95348272, 0.03859008, 107.7674379, -2113.64533629, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 38.48837068, 7.626e-05, 115.46511204, 0.00022877, 384.8837068, 0.00076257, -38.48837068, -7.626e-05, -115.46511204, -0.00022877, -384.8837068, -0.00076257, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 24.9, 7.1, 6.15)
    ops.node(123017, 24.9, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.1225, 32561254.49185663, 13567189.37160693, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 71.47676858, 0.00063623, 85.8244147, 0.02656127, 8.58244147, 0.07872893, -71.47676858, -0.00063623, -85.8244147, -0.02656127, -8.58244147, -0.07872893, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 67.79830455, 0.00063623, 81.4075667, 0.02656127, 8.14075667, 0.07872893, -67.79830455, -0.00063623, -81.4075667, -0.02656127, -8.14075667, -0.07872893, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 122.589971, 0.01272464, 122.589971, 0.03817391, 85.8129797, -973.28779657, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 30.64749275, 6.417e-05, 91.94247825, 0.00019252, 306.47492751, 0.00064172, -30.64749275, -6.417e-05, -91.94247825, -0.00019252, -306.47492751, -0.00064172, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 122.589971, 0.01272464, 122.589971, 0.03817391, 85.8129797, -973.28779657, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 30.64749275, 6.417e-05, 91.94247825, 0.00019252, 306.47492751, 0.00064172, -30.64749275, -6.417e-05, -91.94247825, -0.00019252, -306.47492751, -0.00064172, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 32.15, 7.1, 6.15)
    ops.node(123018, 32.15, 7.1, 8.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.1225, 29633539.74791497, 12347308.2282979, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 65.25791325, 0.000622, 79.14116618, 0.05376063, 7.91411662, 0.14839218, -65.25791325, -0.000622, -79.14116618, -0.05376063, -7.91411662, -0.14839218, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 65.25791325, 0.000622, 79.14116618, 0.05376063, 7.91411662, 0.14839218, -65.25791325, -0.000622, -79.14116618, -0.05376063, -7.91411662, -0.14839218, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 131.00921682, 0.01244005, 131.00921682, 0.03732016, 91.70645177, -2014.82937581, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 32.75230421, 7.536e-05, 98.25691262, 0.00022607, 327.52304205, 0.00075355, -32.75230421, -7.536e-05, -98.25691262, -0.00022607, -327.52304205, -0.00075355, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 131.00921682, 0.01244005, 131.00921682, 0.03732016, 91.70645177, -2014.82937581, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 32.75230421, 7.536e-05, 98.25691262, 0.00022607, 327.52304205, 0.00075355, -32.75230421, -7.536e-05, -98.25691262, -0.00022607, -327.52304205, -0.00075355, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 0.0, 10.65, 6.125)
    ops.node(123019, 0.0, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 28114982.58111627, 11714576.07546511, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 29.38703695, 0.00082961, 35.70833698, 0.02886965, 3.5708337, 0.08328323, -29.38703695, -0.00082961, -35.70833698, -0.02886965, -3.5708337, -0.08328323, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 29.38703695, 0.00082961, 35.70833698, 0.02886965, 3.5708337, 0.08328323, -29.38703695, -0.00082961, -35.70833698, -0.02886965, -3.5708337, -0.08328323, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 55.92014012, 0.01659212, 55.92014012, 0.04977637, 39.14409808, -703.86881974, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 13.98003503, 6.645e-05, 41.94010509, 0.00019934, 139.80035029, 0.00066448, -13.98003503, -6.645e-05, -41.94010509, -0.00019934, -139.80035029, -0.00066448, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 55.92014012, 0.01659212, 55.92014012, 0.04977637, 39.14409808, -703.86881974, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 13.98003503, 6.645e-05, 41.94010509, 0.00019934, 139.80035029, 0.00066448, -13.98003503, -6.645e-05, -41.94010509, -0.00019934, -139.80035029, -0.00066448, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 7.25, 10.65, 6.125)
    ops.node(123020, 7.25, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.1225, 29314702.52674033, 12214459.38614181, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 66.30330778, 0.00069374, 80.41244202, 0.02320221, 8.0412442, 0.0668699, -66.30330778, -0.00069374, -80.41244202, -0.02320221, -8.0412442, -0.0668699, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 62.65959342, 0.00069374, 75.99335677, 0.02320221, 7.59933568, 0.0668699, -62.65959342, -0.00069374, -75.99335677, -0.02320221, -7.59933568, -0.0668699, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 101.62736201, 0.01387479, 101.62736201, 0.04162437, 71.13915341, -814.99382428, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 25.4068405, 5.909e-05, 76.22052151, 0.00017727, 254.06840502, 0.00059091, -25.4068405, -5.909e-05, -76.22052151, -0.00017727, -254.06840502, -0.00059091, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 101.62736201, 0.01387479, 101.62736201, 0.04162437, 71.13915341, -814.99382428, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 25.4068405, 5.909e-05, 76.22052151, 0.00017727, 254.06840502, 0.00059091, -25.4068405, -5.909e-05, -76.22052151, -0.00017727, -254.06840502, -0.00059091, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 14.5, 10.65, 6.125)
    ops.node(123021, 14.5, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 25202093.65485706, 10500872.35619044, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 23.11453575, 0.00086537, 28.09928013, 0.02303387, 2.80992801, 0.06843546, -23.11453575, -0.00086537, -28.09928013, -0.02303387, -2.80992801, -0.06843546, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 23.11453575, 0.00086537, 28.09928013, 0.02303387, 2.80992801, 0.06843546, -23.11453575, -0.00086537, -28.09928013, -0.02303387, -2.80992801, -0.06843546, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 55.60643644, 0.01730747, 55.60643644, 0.05192241, 38.92450551, -692.5243879, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 13.90160911, 7.371e-05, 41.70482733, 0.00022114, 139.0160911, 0.00073712, -13.90160911, -7.371e-05, -41.70482733, -0.00022114, -139.0160911, -0.00073712, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 55.60643644, 0.01730747, 55.60643644, 0.05192241, 38.92450551, -692.5243879, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 13.90160911, 7.371e-05, 41.70482733, 0.00022114, 139.0160911, 0.00073712, -13.90160911, -7.371e-05, -41.70482733, -0.00022114, -139.0160911, -0.00073712, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 17.65, 10.65, 6.125)
    ops.node(123022, 17.65, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 26155674.19322466, 10898197.58051028, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 22.58330393, 0.00085487, 27.44146009, 0.02115451, 2.74414601, 0.06865608, -22.58330393, -0.00085487, -27.44146009, -0.02115451, -2.74414601, -0.06865608, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 22.58330393, 0.00085487, 27.44146009, 0.02115451, 2.74414601, 0.06865608, -22.58330393, -0.00085487, -27.44146009, -0.02115451, -2.74414601, -0.06865608, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 51.31679932, 0.01709731, 51.31679932, 0.05129194, 35.92175952, -712.50189027, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 12.82919983, 6.555e-05, 38.48759949, 0.00019664, 128.29199829, 0.00065546, -12.82919983, -6.555e-05, -38.48759949, -0.00019664, -128.29199829, -0.00065546, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 51.31679932, 0.01709731, 51.31679932, 0.05129194, 35.92175952, -712.50189027, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 12.82919983, 6.555e-05, 38.48759949, 0.00019664, 128.29199829, 0.00065546, -12.82919983, -6.555e-05, -38.48759949, -0.00019664, -128.29199829, -0.00065546, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 24.9, 10.65, 6.125)
    ops.node(123023, 24.9, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 27619181.81829989, 11507992.42429162, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 60.47233024, 0.00058122, 73.57414819, 0.02971477, 7.35741482, 0.0717931, -60.47233024, -0.00058122, -73.57414819, -0.02971477, -7.35741482, -0.0717931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 56.82751447, 0.00058122, 69.13965369, 0.02971477, 6.91396537, 0.0717931, -56.82751447, -0.00058122, -69.13965369, -0.02971477, -6.91396537, -0.0717931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 109.88005175, 0.01162445, 109.88005175, 0.03487335, 76.91603623, -1292.36342261, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 27.47001294, 6.781e-05, 82.41003881, 0.00020343, 274.70012938, 0.00067811, -27.47001294, -6.781e-05, -82.41003881, -0.00020343, -274.70012938, -0.00067811, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 109.88005175, 0.01162445, 109.88005175, 0.03487335, 76.91603623, -1292.36342261, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 27.47001294, 6.781e-05, 82.41003881, 0.00020343, 274.70012938, 0.00067811, -27.47001294, -6.781e-05, -82.41003881, -0.00020343, -274.70012938, -0.00067811, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 32.15, 10.65, 6.125)
    ops.node(123024, 32.15, 10.65, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 26575855.65737681, 11073273.19057367, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 28.75641908, 0.00086851, 35.0197185, 0.03119648, 3.50197185, 0.08333122, -28.75641908, -0.00086851, -35.0197185, -0.03119648, -3.50197185, -0.08333122, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 28.75641908, 0.00086851, 35.0197185, 0.03119648, 3.50197185, 0.08333122, -28.75641908, -0.00086851, -35.0197185, -0.03119648, -3.50197185, -0.08333122, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 59.71065457, 0.01737029, 59.71065457, 0.05211086, 41.7974582, -848.38166224, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 14.92766364, 7.506e-05, 44.78299092, 0.00022518, 149.27663641, 0.00075061, -14.92766364, -7.506e-05, -44.78299092, -0.00022518, -149.27663641, -0.00075061, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 59.71065457, 0.01737029, 59.71065457, 0.05211086, 41.7974582, -848.38166224, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 14.92766364, 7.506e-05, 44.78299092, 0.00022518, 149.27663641, 0.00075061, -14.92766364, -7.506e-05, -44.78299092, -0.00022518, -149.27663641, -0.00075061, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.025)
    ops.node(124001, 0.0, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3001, 173001, 124001, 0.0625, 23597312.5093995, 9832213.54558312, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23001, 24.15048973, 0.00081629, 29.73188857, 0.04030522, 2.97318886, 0.11308992, -24.15048973, -0.00081629, -29.73188857, -0.04030522, -2.97318886, -0.11308992, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13001, 24.15048973, 0.00081629, 29.73188857, 0.04030522, 2.97318886, 0.11308992, -24.15048973, -0.00081629, -29.73188857, -0.04030522, -2.97318886, -0.11308992, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23001, 3001, 0.0, 51.1855446, 0.01632588, 51.1855446, 0.04897765, 35.82988122, -1797.75248017, 0.05, 2, 0, 73001, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 43001, 12.79638615, 7.247e-05, 38.38915845, 0.0002174, 127.9638615, 0.00072466, -12.79638615, -7.247e-05, -38.38915845, -0.0002174, -127.9638615, -0.00072466, 0.4, 0.3, 0.003, 0.0, 0.0, 23001, 2)
    ops.limitCurve('ThreePoint', 13001, 3001, 0.0, 51.1855446, 0.01632588, 51.1855446, 0.04897765, 35.82988122, -1797.75248017, 0.05, 2, 0, 73001, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 33001, 12.79638615, 7.247e-05, 38.38915845, 0.0002174, 127.9638615, 0.00072466, -12.79638615, -7.247e-05, -38.38915845, -0.0002174, -127.9638615, -0.00072466, 0.4, 0.3, 0.003, 0.0, 0.0, 13001, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3001, 99999, 'P', 43001, 'Vy', 33001, 'Vz', 23001, 'My', 13001, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 3001, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 3001, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 7.25, 0.0, 9.025)
    ops.node(124002, 7.25, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3002, 173002, 124002, 0.1225, 33255265.40187414, 13856360.58411422, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23002, 42.39049289, 0.00055264, 50.99025477, 0.02062441, 5.09902548, 0.0707284, -42.39049289, -0.00055264, -50.99025477, -0.02062441, -5.09902548, -0.0707284, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13002, 35.99651045, 0.00055264, 43.29912472, 0.02062441, 4.32991247, 0.0707284, -35.99651045, -0.00055264, -43.29912472, -0.02062441, -4.32991247, -0.0707284, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23002, 3002, 0.0, 110.51821324, 0.01105278, 110.51821324, 0.03315834, 77.36274927, -1342.97291495, 0.05, 2, 0, 73002, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 43002, 27.62955331, 5.665e-05, 82.88865993, 0.00016994, 276.2955331, 0.00056646, -27.62955331, -5.665e-05, -82.88865993, -0.00016994, -276.2955331, -0.00056646, 0.4, 0.3, 0.003, 0.0, 0.0, 23002, 2)
    ops.limitCurve('ThreePoint', 13002, 3002, 0.0, 110.51821324, 0.01105278, 110.51821324, 0.03315834, 77.36274927, -1342.97291495, 0.05, 2, 0, 73002, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 33002, 27.62955331, 5.665e-05, 82.88865993, 0.00016994, 276.2955331, 0.00056646, -27.62955331, -5.665e-05, -82.88865993, -0.00016994, -276.2955331, -0.00056646, 0.4, 0.3, 0.003, 0.0, 0.0, 13002, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3002, 99999, 'P', 43002, 'Vy', 33002, 'Vz', 23002, 'My', 13002, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 3002, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 3002, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 24.9, 0.0, 9.025)
    ops.node(124005, 24.9, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.1225, 27107208.33806206, 11294670.14085919, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 43.89285973, 0.00057931, 53.72660521, 0.01895964, 5.37266052, 0.0675566, -43.89285973, -0.00057931, -53.72660521, -0.01895964, -5.37266052, -0.0675566, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 36.75644311, 0.00057931, 44.99134758, 0.01895964, 4.49913476, 0.0675566, -36.75644311, -0.00057931, -44.99134758, -0.01895964, -4.49913476, -0.0675566, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 83.38913, 0.01158619, 83.38913, 0.03475858, 58.372391, -1020.78823997, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 20.8472825, 5.243e-05, 62.5418475, 0.0001573, 208.47282499, 0.00052435, -20.8472825, -5.243e-05, -62.5418475, -0.0001573, -208.47282499, -0.00052435, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 83.38913, 0.01158619, 83.38913, 0.03475858, 58.372391, -1020.78823997, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 20.8472825, 5.243e-05, 62.5418475, 0.0001573, 208.47282499, 0.00052435, -20.8472825, -5.243e-05, -62.5418475, -0.0001573, -208.47282499, -0.00052435, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 32.15, 0.0, 9.025)
    ops.node(124006, 32.15, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 27494344.3588389, 11455976.81618288, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 22.5718479, 0.00081924, 27.60582006, 0.0349335, 2.76058201, 0.11064667, -22.5718479, -0.00081924, -27.60582006, -0.0349335, -2.76058201, -0.11064667, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 22.5718479, 0.00081924, 27.60582006, 0.0349335, 2.76058201, 0.11064667, -22.5718479, -0.00081924, -27.60582006, -0.0349335, -2.76058201, -0.11064667, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 52.10066468, 0.01638478, 52.10066468, 0.04915435, 36.47046527, -1214.41309819, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 13.02516617, 6.331e-05, 39.07549851, 0.00018992, 130.25166169, 0.00063307, -13.02516617, -6.331e-05, -39.07549851, -0.00018992, -130.25166169, -0.00063307, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 52.10066468, 0.01638478, 52.10066468, 0.04915435, 36.47046527, -1214.41309819, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 13.02516617, 6.331e-05, 39.07549851, 0.00018992, 130.25166169, 0.00063307, -13.02516617, -6.331e-05, -39.07549851, -0.00018992, -130.25166169, -0.00063307, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 0.0, 3.55, 9.05)
    ops.node(124007, 0.0, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 26360696.51085193, 10983623.5461883, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 62.52110346, 0.00067842, 76.64830695, 0.06484392, 7.6648307, 0.16484392, -62.52110346, -0.00067842, -76.64830695, -0.06484392, -7.6648307, -0.16484392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 57.95240417, 0.00067842, 71.04726912, 0.06484392, 7.10472691, 0.16484392, -57.95240417, -0.00067842, -71.04726912, -0.06484392, -7.10472691, -0.16484392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 150.61752437, 0.01356845, 150.61752437, 0.04070535, 105.43226706, -10354.46963957, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 37.65438109, 9.739e-05, 112.96314328, 0.00029217, 376.54381093, 0.0009739, -37.65438109, -9.739e-05, -112.96314328, -0.00029217, -376.54381093, -0.0009739, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 150.61752437, 0.01356845, 150.61752437, 0.04070535, 105.43226706, -10354.46963957, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 37.65438109, 9.739e-05, 112.96314328, 0.00029217, 376.54381093, 0.0009739, -37.65438109, -9.739e-05, -112.96314328, -0.00029217, -376.54381093, -0.0009739, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 7.25, 3.55, 9.05)
    ops.node(124008, 7.25, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.1225, 25922359.48376984, 10800983.11823743, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 46.9421095, 0.00063859, 57.51039826, 0.02488668, 5.75103983, 0.06539785, -46.9421095, -0.00063859, -57.51039826, -0.02488668, -5.75103983, -0.06539785, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 44.20153972, 0.00063859, 54.15283165, 0.02488668, 5.41528317, 0.06539785, -44.20153972, -0.00063859, -54.15283165, -0.02488668, -5.41528317, -0.06539785, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 85.34645308, 0.01277171, 85.34645308, 0.03831512, 59.74251716, -1026.18408737, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 21.33661327, 5.612e-05, 64.00983981, 0.00016836, 213.36613271, 0.00056118, -21.33661327, -5.612e-05, -64.00983981, -0.00016836, -213.36613271, -0.00056118, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 85.34645308, 0.01277171, 85.34645308, 0.03831512, 59.74251716, -1026.18408737, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 21.33661327, 5.612e-05, 64.00983981, 0.00016836, 213.36613271, 0.00056118, -21.33661327, -5.612e-05, -64.00983981, -0.00016836, -213.36613271, -0.00056118, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 14.5, 3.55, 9.05)
    ops.node(124009, 14.5, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.1225, 26768042.52338123, 11153351.05140885, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 50.2898283, 0.00064061, 61.54368087, 0.0366501, 6.15436809, 0.09252497, -50.2898283, -0.00064061, -61.54368087, -0.0366501, -6.15436809, -0.09252497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 46.99621713, 0.00064061, 57.51302573, 0.0366501, 5.75130257, 0.09252497, -46.99621713, -0.00064061, -57.51302573, -0.0366501, -5.75130257, -0.09252497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 108.97966137, 0.01281212, 108.97966137, 0.03843637, 76.28576296, -2526.34302919, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 27.24491534, 6.939e-05, 81.73474603, 0.00020818, 272.44915343, 0.00069394, -27.24491534, -6.939e-05, -81.73474603, -0.00020818, -272.44915343, -0.00069394, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 108.97966137, 0.01281212, 108.97966137, 0.03843637, 76.28576296, -2526.34302919, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 27.24491534, 6.939e-05, 81.73474603, 0.00020818, 272.44915343, 0.00069394, -27.24491534, -6.939e-05, -81.73474603, -0.00020818, -272.44915343, -0.00069394, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 17.65, 3.55, 9.05)
    ops.node(124010, 17.65, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.1225, 29954296.43260404, 12480956.84691835, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 48.03457031, 0.00058122, 58.35671438, 0.03391398, 5.83567144, 0.09140688, -48.03457031, -0.00058122, -58.35671438, -0.03391398, -5.83567144, -0.09140688, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 44.90105397, 0.00058122, 54.54983702, 0.03391398, 5.4549837, 0.09140688, -44.90105397, -0.00058122, -54.54983702, -0.03391398, -5.4549837, -0.09140688, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 108.66318609, 0.01162449, 108.66318609, 0.03487347, 76.06423027, -1671.9859388, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 27.16579652, 6.183e-05, 81.49738957, 0.0001855, 271.65796524, 0.00061833, -27.16579652, -6.183e-05, -81.49738957, -0.0001855, -271.65796524, -0.00061833, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 108.66318609, 0.01162449, 108.66318609, 0.03487347, 76.06423027, -1671.9859388, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 27.16579652, 6.183e-05, 81.49738957, 0.0001855, 271.65796524, 0.00061833, -27.16579652, -6.183e-05, -81.49738957, -0.0001855, -271.65796524, -0.00061833, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 24.9, 3.55, 9.05)
    ops.node(124011, 24.9, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 29080830.63540678, 12117012.76475282, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 57.83175297, 0.00063473, 70.39955699, 0.01833677, 7.0399557, 0.06033446, -57.83175297, -0.00063473, -70.39955699, -0.01833677, -7.0399557, -0.06033446, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 53.63569942, 0.00063473, 65.29163105, 0.01833677, 6.52916311, 0.06033446, -53.63569942, -0.00063473, -65.29163105, -0.01833677, -6.52916311, -0.06033446, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 85.72849435, 0.01269464, 85.72849435, 0.03808393, 60.00994605, -702.85356478, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 21.43212359, 5.025e-05, 64.29637077, 0.00015074, 214.32123588, 0.00050247, -21.43212359, -5.025e-05, -64.29637077, -0.00015074, -214.32123588, -0.00050247, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 85.72849435, 0.01269464, 85.72849435, 0.03808393, 60.00994605, -702.85356478, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 21.43212359, 5.025e-05, 64.29637077, 0.00015074, 214.32123588, 0.00050247, -21.43212359, -5.025e-05, -64.29637077, -0.00015074, -214.32123588, -0.00050247, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 32.15, 3.55, 9.05)
    ops.node(124012, 32.15, 3.55, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.1225, 26719613.75397731, 11133172.39749055, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 67.52264274, 0.00066772, 82.72221623, 0.06198046, 8.27222162, 0.16198046, -67.52264274, -0.00066772, -82.72221623, -0.06198046, -8.27222162, -0.16198046, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 62.05118079, 0.00066772, 76.01910983, 0.06198046, 7.60191098, 0.16198046, -62.05118079, -0.00066772, -76.01910983, -0.06198046, -7.60191098, -0.16198046, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 130.28680006, 0.01335438, 130.28680006, 0.04006314, 91.20076004, -6456.06236269, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 32.57170001, 8.311e-05, 97.71510004, 0.00024934, 325.71700015, 0.00083112, -32.57170001, -8.311e-05, -97.71510004, -0.00024934, -325.71700015, -0.00083112, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 130.28680006, 0.01335438, 130.28680006, 0.04006314, 91.20076004, -6456.06236269, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 32.57170001, 8.311e-05, 97.71510004, 0.00024934, 325.71700015, 0.00083112, -32.57170001, -8.311e-05, -97.71510004, -0.00024934, -325.71700015, -0.00083112, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 7.1, 9.05)
    ops.node(124013, 0.0, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.1225, 22483132.19678178, 9367971.74865908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 71.309323, 0.00072082, 87.90993181, 0.06637778, 8.79099318, 0.16411915, -71.309323, -0.00072082, -87.90993181, -0.06637778, -8.79099318, -0.16411915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 65.00741179, 0.00072082, 80.14095348, 0.06637778, 8.01409535, 0.16411915, -65.00741179, -0.00072082, -80.14095348, -0.06637778, -8.01409535, -0.16411915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 132.2711061, 0.01441649, 132.2711061, 0.04324948, 92.58977427, -9155.60070885, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 33.06777652, 0.00010028, 99.20332957, 0.00030083, 330.67776524, 0.00100277, -33.06777652, -0.00010028, -99.20332957, -0.00030083, -330.67776524, -0.00100277, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 132.2711061, 0.01441649, 132.2711061, 0.04324948, 92.58977427, -9155.60070885, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 33.06777652, 0.00010028, 99.20332957, 0.00030083, 330.67776524, 0.00100277, -33.06777652, -0.00010028, -99.20332957, -0.00030083, -330.67776524, -0.00100277, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 7.25, 7.1, 9.05)
    ops.node(124014, 7.25, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.1225, 29606464.11343613, 12336026.71393172, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 51.39484544, 0.00061525, 62.48121553, 0.02173284, 6.24812155, 0.0639188, -51.39484544, -0.00061525, -62.48121553, -0.02173284, -6.24812155, -0.0639188, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 48.08188434, 0.00061525, 58.45361637, 0.02173284, 5.84536164, 0.0639188, -48.08188434, -0.00061525, -58.45361637, -0.02173284, -5.84536164, -0.0639188, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 94.48218569, 0.01230499, 94.48218569, 0.03691496, 66.13752998, -856.65511419, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 23.62054642, 5.439e-05, 70.86163927, 0.00016318, 236.20546423, 0.00054395, -23.62054642, -5.439e-05, -70.86163927, -0.00016318, -236.20546423, -0.00054395, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 94.48218569, 0.01230499, 94.48218569, 0.03691496, 66.13752998, -856.65511419, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 23.62054642, 5.439e-05, 70.86163927, 0.00016318, 236.20546423, 0.00054395, -23.62054642, -5.439e-05, -70.86163927, -0.00016318, -236.20546423, -0.00054395, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 14.5, 7.1, 9.05)
    ops.node(124015, 14.5, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 25991204.53560818, 10829668.55650341, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 46.96404205, 0.00063456, 57.59137394, 0.03125531, 5.75913739, 0.08771689, -46.96404205, -0.00063456, -57.59137394, -0.03125531, -5.75913739, -0.08771689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 43.88074272, 0.00063456, 53.81036539, 0.03125531, 5.38103654, 0.08771689, -43.88074272, -0.00063456, -53.81036539, -0.03125531, -5.38103654, -0.08771689, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 85.69017434, 0.01269113, 85.69017434, 0.03807339, 59.98312204, -1297.70740322, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 21.42254359, 5.62e-05, 64.26763076, 0.00016859, 214.22543586, 0.00056195, -21.42254359, -5.62e-05, -64.26763076, -0.00016859, -214.22543586, -0.00056195, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 85.69017434, 0.01269113, 85.69017434, 0.03807339, 59.98312204, -1297.70740322, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 21.42254359, 5.62e-05, 64.26763076, 0.00016859, 214.22543586, 0.00056195, -21.42254359, -5.62e-05, -64.26763076, -0.00016859, -214.22543586, -0.00056195, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 17.65, 7.1, 9.05)
    ops.node(124016, 17.65, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.1225, 27990546.91930006, 11662727.88304169, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 48.86291325, 0.0006053, 59.67995637, 0.0302952, 5.96799564, 0.08776506, -48.86291325, -0.0006053, -59.67995637, -0.0302952, -5.96799564, -0.08776506, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 45.44203256, 0.0006053, 55.50177711, 0.0302952, 5.55017771, 0.08776506, -45.44203256, -0.0006053, -55.50177711, -0.0302952, -5.55017771, -0.08776506, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 92.58765641, 0.01210609, 92.58765641, 0.03631827, 64.81135949, -1307.59821707, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 23.1469141, 5.638e-05, 69.44074231, 0.00016914, 231.46914102, 0.00056381, -23.1469141, -5.638e-05, -69.44074231, -0.00016914, -231.46914102, -0.00056381, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 92.58765641, 0.01210609, 92.58765641, 0.03631827, 64.81135949, -1307.59821707, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 23.1469141, 5.638e-05, 69.44074231, 0.00016914, 231.46914102, 0.00056381, -23.1469141, -5.638e-05, -69.44074231, -0.00016914, -231.46914102, -0.00056381, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 24.9, 7.1, 9.05)
    ops.node(124017, 24.9, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.1225, 23046680.22652193, 9602783.42771747, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 49.03070355, 0.00065759, 60.27751114, 0.02033012, 6.02775111, 0.05869946, -49.03070355, -0.00065759, -60.27751114, -0.02033012, -6.02775111, -0.05869946, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 45.8344862, 0.00065759, 56.34813601, 0.02033012, 5.6348136, 0.05869946, -45.8344862, -0.00065759, -56.34813601, -0.02033012, -5.6348136, -0.05869946, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 65.65667944, 0.01315182, 65.65667944, 0.03945547, 45.95967561, -659.62273601, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 16.41416986, 4.856e-05, 49.24250958, 0.00014568, 164.14169859, 0.00048558, -16.41416986, -4.856e-05, -49.24250958, -0.00014568, -164.14169859, -0.00048558, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 65.65667944, 0.01315182, 65.65667944, 0.03945547, 45.95967561, -659.62273601, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 16.41416986, 4.856e-05, 49.24250958, 0.00014568, 164.14169859, 0.00048558, -16.41416986, -4.856e-05, -49.24250958, -0.00014568, -164.14169859, -0.00048558, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 32.15, 7.1, 9.05)
    ops.node(124018, 32.15, 7.1, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.1225, 28523863.52428275, 11884943.13511781, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 69.64735022, 0.00064972, 84.98649573, 0.05955783, 8.49864957, 0.15955783, -69.64735022, -0.00064972, -84.98649573, -0.05955783, -8.49864957, -0.15955783, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 63.87048729, 0.00064972, 77.93733542, 0.05955783, 7.79373354, 0.15955783, -63.87048729, -0.00064972, -77.93733542, -0.05955783, -7.79373354, -0.15955783, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 131.1094867, 0.01299445, 131.1094867, 0.03898336, 91.77664069, -5628.80595751, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 32.77737167, 7.835e-05, 98.33211502, 0.00023504, 327.77371674, 0.00078347, -32.77737167, -7.835e-05, -98.33211502, -0.00023504, -327.77371674, -0.00078347, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 131.1094867, 0.01299445, 131.1094867, 0.03898336, 91.77664069, -5628.80595751, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 32.77737167, 7.835e-05, 98.33211502, 0.00023504, 327.77371674, 0.00078347, -32.77737167, -7.835e-05, -98.33211502, -0.00023504, -327.77371674, -0.00078347, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 0.0, 10.65, 9.025)
    ops.node(124019, 0.0, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 26772029.03571403, 11155012.09821418, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 22.57334898, 0.00079795, 27.64907129, 0.04138405, 2.76490713, 0.11668124, -22.57334898, -0.00079795, -27.64907129, -0.04138405, -2.76490713, -0.11668124, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 22.57334898, 0.00079795, 27.64907129, 0.04138405, 2.76490713, 0.11668124, -22.57334898, -0.00079795, -27.64907129, -0.04138405, -2.76490713, -0.11668124, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 57.89446245, 0.01595896, 57.89446245, 0.04787688, 40.52612372, -1973.70252407, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 14.47361561, 7.224e-05, 43.42084684, 0.00021673, 144.73615614, 0.00072245, -14.47361561, -7.224e-05, -43.42084684, -0.00021673, -144.73615614, -0.00072245, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 57.89446245, 0.01595896, 57.89446245, 0.04787688, 40.52612372, -1973.70252407, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 14.47361561, 7.224e-05, 43.42084684, 0.00021673, 144.73615614, 0.00072245, -14.47361561, -7.224e-05, -43.42084684, -0.00021673, -144.73615614, -0.00072245, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 7.25, 10.65, 9.025)
    ops.node(124020, 7.25, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.1225, 27451413.94877585, 11438089.14532327, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 47.29712884, 0.00066378, 57.85148943, 0.01981076, 5.78514894, 0.06256681, -47.29712884, -0.00066378, -57.85148943, -0.01981076, -5.78514894, -0.06256681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 44.35763135, 0.00066378, 54.25604268, 0.01981076, 5.42560427, 0.06256681, -44.35763135, -0.00066378, -54.25604268, -0.01981076, -5.42560427, -0.06256681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 78.76379209, 0.01327558, 78.76379209, 0.03982674, 55.13465446, -811.18954969, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 19.69094802, 4.891e-05, 59.07284407, 0.00014672, 196.90948023, 0.00048905, -19.69094802, -4.891e-05, -59.07284407, -0.00014672, -196.90948023, -0.00048905, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 78.76379209, 0.01327558, 78.76379209, 0.03982674, 55.13465446, -811.18954969, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 19.69094802, 4.891e-05, 59.07284407, 0.00014672, 196.90948023, 0.00048905, -19.69094802, -4.891e-05, -59.07284407, -0.00014672, -196.90948023, -0.00048905, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 14.5, 10.65, 9.025)
    ops.node(124021, 14.5, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 26943253.81275643, 11226355.75531518, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 15.42365034, 0.00081805, 18.87074902, 0.02642092, 1.8870749, 0.08782518, -15.42365034, -0.00081805, -18.87074902, -0.02642092, -1.8870749, -0.08782518, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 15.42365034, 0.00081805, 18.87074902, 0.02642092, 1.8870749, 0.08782518, -15.42365034, -0.00081805, -18.87074902, -0.02642092, -1.8870749, -0.08782518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 52.95408888, 0.01636108, 52.95408888, 0.04908325, 37.06786222, -1085.52931421, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 13.23852222, 6.566e-05, 39.71556666, 0.00019698, 132.38522221, 0.0006566, -13.23852222, -6.566e-05, -39.71556666, -0.00019698, -132.38522221, -0.0006566, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 52.95408888, 0.01636108, 52.95408888, 0.04908325, 37.06786222, -1085.52931421, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 13.23852222, 6.566e-05, 39.71556666, 0.00019698, 132.38522221, 0.0006566, -13.23852222, -6.566e-05, -39.71556666, -0.00019698, -132.38522221, -0.0006566, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 17.65, 10.65, 9.025)
    ops.node(124022, 17.65, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 26538877.70942988, 11057865.71226245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 15.69392249, 0.00074123, 19.21604926, 0.02193862, 1.92160493, 0.08306925, -15.69392249, -0.00074123, -19.21604926, -0.02193862, -1.92160493, -0.08306925, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 15.69392249, 0.00074123, 19.21604926, 0.02193862, 1.92160493, 0.08306925, -15.69392249, -0.00074123, -19.21604926, -0.02193862, -1.92160493, -0.08306925, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 36.64697044, 0.01482461, 36.64697044, 0.04447383, 25.65287931, -695.18664907, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 9.16174261, 4.613e-05, 27.48522783, 0.0001384, 91.6174261, 0.00046132, -9.16174261, -4.613e-05, -27.48522783, -0.0001384, -91.6174261, -0.00046132, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 36.64697044, 0.01482461, 36.64697044, 0.04447383, 25.65287931, -695.18664907, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 9.16174261, 4.613e-05, 27.48522783, 0.0001384, 91.6174261, 0.00046132, -9.16174261, -4.613e-05, -27.48522783, -0.0001384, -91.6174261, -0.00046132, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 24.9, 10.65, 9.025)
    ops.node(124023, 24.9, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 27788151.92654342, 11578396.63605976, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 48.07601376, 0.00069042, 58.76074276, 0.02581377, 5.87607428, 0.06867085, -48.07601376, -0.00069042, -58.76074276, -0.02581377, -5.87607428, -0.06867085, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 45.21401261, 0.00069042, 55.26267168, 0.02581377, 5.52626717, 0.06867085, -45.21401261, -0.00069042, -55.26267168, -0.02581377, -5.52626717, -0.06867085, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 93.10782451, 0.01380847, 93.10782451, 0.04142541, 65.17547715, -1533.63665671, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 23.27695613, 5.711e-05, 69.83086838, 0.00017133, 232.76956127, 0.00057111, -23.27695613, -5.711e-05, -69.83086838, -0.00017133, -232.76956127, -0.00057111, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 93.10782451, 0.01380847, 93.10782451, 0.04142541, 65.17547715, -1533.63665671, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 23.27695613, 5.711e-05, 69.83086838, 0.00017133, 232.76956127, 0.00057111, -23.27695613, -5.711e-05, -69.83086838, -0.00017133, -232.76956127, -0.00057111, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 32.15, 10.65, 9.025)
    ops.node(124024, 32.15, 10.65, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 32666965.51696637, 13611235.63206932, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 25.53288478, 0.00072687, 30.77691551, 0.03882459, 3.07769155, 0.11652809, -25.53288478, -0.00072687, -30.77691551, -0.03882459, -3.07769155, -0.11652809, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 25.53288478, 0.00072687, 30.77691551, 0.03882459, 3.07769155, 0.11652809, -25.53288478, -0.00072687, -30.77691551, -0.03882459, -3.07769155, -0.11652809, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 73.03160791, 0.01453746, 73.03160791, 0.04361239, 51.12212554, -2532.05585741, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 18.25790198, 7.469e-05, 54.77370593, 0.00022406, 182.57901978, 0.00074688, -18.25790198, -7.469e-05, -54.77370593, -0.00022406, -182.57901978, -0.00074688, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 73.03160791, 0.01453746, 73.03160791, 0.04361239, 51.12212554, -2532.05585741, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 18.25790198, 7.469e-05, 54.77370593, 0.00022406, 182.57901978, 0.00074688, -18.25790198, -7.469e-05, -54.77370593, -0.00022406, -182.57901978, -0.00074688, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170003, 14.5, 0.0, 0.0)
    ops.node(124025, 14.5, 0.0, 1.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170003, 124025, 0.16, 24631035.14650325, 10262931.31104302, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 134.15434412, 0.00054399, 162.93281837, 0.04235819, 16.29328184, 0.10438641, -134.15434412, -0.00054399, -162.93281837, -0.04235819, -16.29328184, -0.10438641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 134.15434412, 0.00054399, 162.93281837, 0.04235819, 16.29328184, 0.10438641, -134.15434412, -0.00054399, -162.93281837, -0.04235819, -16.29328184, -0.10438641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 224.66334419, 0.0108798, 224.66334419, 0.03263939, 157.26434093, -4727.53821967, 0.05, 2, 0, 70003, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 56.16583605, 5.952e-05, 168.49750814, 0.00017855, 561.65836048, 0.00059515, -56.16583605, -5.952e-05, -168.49750814, -0.00017855, -561.65836048, -0.00059515, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 224.66334419, 0.0108798, 224.66334419, 0.03263939, 157.26434093, -4727.53821967, 0.05, 2, 0, 70003, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 56.16583605, 5.952e-05, 168.49750814, 0.00017855, 561.65836048, 0.00059515, -56.16583605, -5.952e-05, -168.49750814, -0.00017855, -561.65836048, -0.00059515, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 14.5, 0.0, 1.65)
    ops.node(121003, 14.5, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121003, 0.16, 26292419.84018135, 10955174.9334089, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 109.56565893, 0.00051653, 133.1343546, 0.05415618, 13.31343546, 0.15392624, -109.56565893, -0.00051653, -133.1343546, -0.05415618, -13.31343546, -0.15392624, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 90.28139563, 0.00051653, 109.70184871, 0.04658067, 10.97018487, 0.11610718, -90.28139563, -0.00051653, -109.70184871, -0.04658067, -10.97018487, -0.11610718, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 267.65288233, 0.01033058, 267.65288233, 0.03099175, 187.35701763, -7564.92580605, 0.05, 2, 0, 74025, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 66.91322058, 6.642e-05, 200.73966175, 0.00019927, 669.13220583, 0.00066424, -66.91322058, -6.642e-05, -200.73966175, -0.00019927, -669.13220583, -0.00066424, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 320.38299834, 0.01033058, 320.38299834, 0.03099175, 224.26809884, -13397.49046229, 0.05, 2, 0, 74025, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 80.09574959, 7.951e-05, 240.28724876, 0.00023853, 800.95749586, 0.0007951, -80.09574959, -7.951e-05, -240.28724876, -0.00023853, -800.95749586, -0.0007951, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 17.65, 0.0, 0.0)
    ops.node(124026, 17.65, 0.0, 1.25)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170004, 124026, 0.16, 23508457.79235074, 9795190.74681281, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 129.74111381, 0.00054238, 157.48571354, 0.04378236, 15.74857135, 0.10130054, -129.74111381, -0.00054238, -157.48571354, -0.04378236, -15.74857135, -0.10130054, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 129.74111381, 0.00054238, 157.48571354, 0.04378236, 15.74857135, 0.10130054, -129.74111381, -0.00054238, -157.48571354, -0.04378236, -15.74857135, -0.10130054, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 230.83298052, 0.01084752, 230.83298052, 0.03254256, 161.58308636, -5852.51351527, 0.05, 2, 0, 70004, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 57.70824513, 6.407e-05, 173.12473539, 0.00019221, 577.0824513, 0.0006407, -57.70824513, -6.407e-05, -173.12473539, -0.00019221, -577.0824513, -0.0006407, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 230.83298052, 0.01084752, 230.83298052, 0.03254256, 161.58308636, -5852.51351527, 0.05, 2, 0, 70004, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 57.70824513, 6.407e-05, 173.12473539, 0.00019221, 577.0824513, 0.0006407, -57.70824513, -6.407e-05, -173.12473539, -0.00019221, -577.0824513, -0.0006407, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 17.65, 0.0, 1.65)
    ops.node(121004, 17.65, 0.0, 2.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121004, 0.16, 29094105.69573174, 12122544.03988823, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 115.05989791, 0.00052349, 139.302046, 0.051985, 13.9302046, 0.151985, -115.05989791, -0.00052349, -139.302046, -0.051985, -13.9302046, -0.151985, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 94.91198166, 0.00052349, 114.90913407, 0.04471711, 11.49091341, 0.12123757, -94.91198166, -0.00052349, -114.90913407, -0.04471711, -11.49091341, -0.12123757, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 285.45043718, 0.01046982, 285.45043718, 0.03140945, 199.81530603, -7081.20431425, 0.05, 2, 0, 74026, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 71.3626093, 6.402e-05, 214.08782789, 0.00019206, 713.62609296, 0.00064019, -71.3626093, -6.402e-05, -214.08782789, -0.00019206, -713.62609296, -0.00064019, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 335.59023715, 0.01046982, 335.59023715, 0.03140945, 234.913166, -12433.92121242, 0.05, 2, 0, 74026, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 83.89755929, 7.526e-05, 251.69267786, 0.00022579, 838.97559287, 0.00075264, -83.89755929, -7.526e-05, -251.69267786, -0.00022579, -838.97559287, -0.00075264, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 14.5, 0.0, 3.225)
    ops.node(124027, 14.5, 0.0, 4.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171003, 124027, 0.16, 28491030.86908226, 11871262.86211761, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 92.82815148, 0.00051403, 112.70475336, 0.0461384, 11.27047534, 0.12548171, -92.82815148, -0.00051403, -112.70475336, -0.0461384, -11.27047534, -0.12548171, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 78.85993121, 0.00051403, 95.74562193, 0.0461384, 9.57456219, 0.12548171, -78.85993121, -0.00051403, -95.74562193, -0.0461384, -9.57456219, -0.12548171, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 263.16769621, 0.0102806, 263.16769621, 0.03084181, 184.21738735, -6734.15677261, 0.05, 2, 0, 71003, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 65.79192405, 6.027e-05, 197.37577216, 0.00018081, 657.91924053, 0.00060271, -65.79192405, -6.027e-05, -197.37577216, -0.00018081, -657.91924053, -0.00060271, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 263.16769621, 0.0102806, 263.16769621, 0.03084181, 184.21738735, -6734.15677261, 0.05, 2, 0, 71003, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 65.79192405, 6.027e-05, 197.37577216, 0.00018081, 657.91924053, 0.00060271, -65.79192405, -6.027e-05, -197.37577216, -0.00018081, -657.91924053, -0.00060271, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 14.5, 0.0, 4.55)
    ops.node(122003, 14.5, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122003, 0.16, 25583262.33364213, 10659692.63901755, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 88.38114762, 0.00052848, 107.81847077, 0.04618429, 10.78184708, 0.12101706, -88.38114762, -0.00052848, -107.81847077, -0.04618429, -10.78184708, -0.12101706, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 74.66220009, 0.00052848, 91.08236829, 0.04618429, 9.10823683, 0.12101706, -74.66220009, -0.00052848, -91.08236829, -0.04618429, -9.10823683, -0.12101706, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 228.80628849, 0.01056958, 228.80628849, 0.03170875, 160.16440194, -6162.23922361, 0.05, 2, 0, 74027, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 57.20157212, 5.836e-05, 171.60471637, 0.00017507, 572.01572123, 0.00058357, -57.20157212, -5.836e-05, -171.60471637, -0.00017507, -572.01572123, -0.00058357, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 228.80628849, 0.01056958, 228.80628849, 0.03170875, 160.16440194, -6162.23922361, 0.05, 2, 0, 74027, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 57.20157212, 5.836e-05, 171.60471637, 0.00017507, 572.01572123, 0.00058357, -57.20157212, -5.836e-05, -171.60471637, -0.00017507, -572.01572123, -0.00058357, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 17.65, 0.0, 3.225)
    ops.node(124028, 17.65, 0.0, 4.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171004, 124028, 0.16, 26954743.1905279, 11231142.99605329, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 93.67911048, 0.00053573, 114.0098479, 0.04460791, 11.40098479, 0.12075629, -93.67911048, -0.00053573, -114.0098479, -0.04460791, -11.40098479, -0.12075629, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 79.70016858, 0.00053573, 96.99712188, 0.04460791, 9.69971219, 0.12075629, -79.70016858, -0.00053573, -96.99712188, -0.04460791, -9.69971219, -0.12075629, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 238.72670583, 0.01071465, 238.72670583, 0.03214394, 167.10869408, -5581.88551247, 0.05, 2, 0, 71004, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 59.68167646, 5.779e-05, 179.04502938, 0.00017337, 596.81676458, 0.00057789, -59.68167646, -5.779e-05, -179.04502938, -0.00017337, -596.81676458, -0.00057789, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 238.72670583, 0.01071465, 238.72670583, 0.03214394, 167.10869408, -5581.88551247, 0.05, 2, 0, 71004, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 59.68167646, 5.779e-05, 179.04502938, 0.00017337, 596.81676458, 0.00057789, -59.68167646, -5.779e-05, -179.04502938, -0.00017337, -596.81676458, -0.00057789, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 17.65, 0.0, 4.55)
    ops.node(122004, 17.65, 0.0, 5.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122004, 0.16, 28396476.63343848, 11831865.2639327, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 79.16648487, 0.00046298, 96.20002708, 0.04456712, 9.62000271, 0.12536373, -79.16648487, -0.00046298, -96.20002708, -0.04456712, -9.62000271, -0.12536373, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 67.50703299, 0.00046298, 82.03191555, 0.04456712, 8.20319155, 0.12536373, -67.50703299, -0.00046298, -82.03191555, -0.04456712, -8.20319155, -0.12536373, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 244.14002685, 0.0092596, 244.14002685, 0.02777879, 170.8980188, -5469.99322179, 0.05, 2, 0, 74028, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 61.03500671, 5.61e-05, 183.10502014, 0.0001683, 610.35006713, 0.00056099, -61.03500671, -5.61e-05, -183.10502014, -0.0001683, -610.35006713, -0.00056099, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 244.14002685, 0.0092596, 244.14002685, 0.02777879, 170.8980188, -5469.99322179, 0.05, 2, 0, 74028, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 61.03500671, 5.61e-05, 183.10502014, 0.0001683, 610.35006713, 0.00056099, -61.03500671, -5.61e-05, -183.10502014, -0.0001683, -610.35006713, -0.00056099, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 14.5, 0.0, 6.125)
    ops.node(124029, 14.5, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172003, 124029, 0.1225, 28518804.09476491, 11882835.03948538, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 58.11256113, 0.00050573, 70.6330002, 0.04746337, 7.06330002, 0.13979811, -58.11256113, -0.00050573, -70.6330002, -0.04746337, -7.06330002, -0.13979811, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 50.34723272, 0.00050573, 61.19462006, 0.04746337, 6.11946201, 0.13979811, -50.34723272, -0.00050573, -61.19462006, -0.04746337, -6.11946201, -0.13979811, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 182.23764134, 0.01011455, 182.23764134, 0.03034364, 127.56634894, -5627.90909998, 0.05, 2, 0, 72003, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 45.55941034, 5.446e-05, 136.67823101, 0.00016338, 455.59410336, 0.00054459, -45.55941034, -5.446e-05, -136.67823101, -0.00016338, -455.59410336, -0.00054459, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 182.23764134, 0.01011455, 182.23764134, 0.03034364, 127.56634894, -5627.90909998, 0.05, 2, 0, 72003, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 45.55941034, 5.446e-05, 136.67823101, 0.00016338, 455.59410336, 0.00054459, -45.55941034, -5.446e-05, -136.67823101, -0.00016338, -455.59410336, -0.00054459, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 14.5, 0.0, 7.45)
    ops.node(123003, 14.5, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123003, 0.1225, 25213321.69776824, 10505550.70740344, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 55.72577871, 0.00056043, 68.15190852, 0.04605263, 6.81519085, 0.1347106, -55.72577871, -0.00056043, -68.15190852, -0.04605263, -6.81519085, -0.1347106, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 48.32741657, 0.00056043, 59.10380706, 0.04605263, 5.91038071, 0.1347106, -48.32741657, -0.00056043, -59.10380706, -0.04605263, -5.91038071, -0.1347106, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 151.58636426, 0.01120857, 151.58636426, 0.0336257, 106.11045498, -4910.23433433, 0.05, 2, 0, 74029, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 37.89659107, 5.124e-05, 113.6897732, 0.00015371, 378.96591066, 0.00051238, -37.89659107, -5.124e-05, -113.6897732, -0.00015371, -378.96591066, -0.00051238, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 151.58636426, 0.01120857, 151.58636426, 0.0336257, 106.11045498, -4910.23433433, 0.05, 2, 0, 74029, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 37.89659107, 5.124e-05, 113.6897732, 0.00015371, 378.96591066, 0.00051238, -37.89659107, -5.124e-05, -113.6897732, -0.00015371, -378.96591066, -0.00051238, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 17.65, 0.0, 6.125)
    ops.node(124030, 17.65, 0.0, 7.05)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172004, 124030, 0.1225, 30556383.90219208, 12731826.62591337, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 54.2858344, 0.00049645, 65.67653194, 0.04557922, 6.56765319, 0.14115238, -54.2858344, -0.00049645, -65.67653194, -0.04557922, -6.56765319, -0.14115238, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 47.98055365, 0.00049645, 58.04822565, 0.04557922, 5.80482256, 0.14115238, -47.98055365, -0.00049645, -58.04822565, -0.04557922, -5.80482256, -0.14115238, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 187.96628533, 0.00992909, 187.96628533, 0.02978728, 131.57639973, -4988.97401221, 0.05, 2, 0, 72004, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 46.99157133, 5.243e-05, 140.974714, 0.00015728, 469.91571333, 0.00052425, -46.99157133, -5.243e-05, -140.974714, -0.00015728, -469.91571333, -0.00052425, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 187.96628533, 0.00992909, 187.96628533, 0.02978728, 131.57639973, -4988.97401221, 0.05, 2, 0, 72004, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 46.99157133, 5.243e-05, 140.974714, 0.00015728, 469.91571333, 0.00052425, -46.99157133, -5.243e-05, -140.974714, -0.00015728, -469.91571333, -0.00052425, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 17.65, 0.0, 7.45)
    ops.node(123004, 17.65, 0.0, 8.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123004, 0.1225, 29428727.98414889, 12261969.99339537, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 51.50548333, 0.0005035, 62.53857333, 0.05142735, 6.25385733, 0.14784622, -51.50548333, -0.0005035, -62.53857333, -0.05142735, -6.25385733, -0.14784622, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 45.18681992, 0.0005035, 54.86637671, 0.05142735, 5.48663767, 0.14784622, -45.18681992, -0.0005035, -54.86637671, -0.05142735, -5.48663767, -0.14784622, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 198.97957498, 0.01007, 198.97957498, 0.03020999, 139.28570249, -8324.70779285, 0.05, 2, 0, 74030, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 49.74489375, 5.762e-05, 149.23468124, 0.00017287, 497.44893746, 0.00057624, -49.74489375, -5.762e-05, -149.23468124, -0.00017287, -497.44893746, -0.00057624, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 198.97957498, 0.01007, 198.97957498, 0.03020999, 139.28570249, -8324.70779285, 0.05, 2, 0, 74030, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 49.74489375, 5.762e-05, 149.23468124, 0.00017287, 497.44893746, 0.00057624, -49.74489375, -5.762e-05, -149.23468124, -0.00017287, -497.44893746, -0.00057624, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 14.5, 0.0, 9.025)
    ops.node(124031, 14.5, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173003, 124031, 0.1225, 24862671.30155714, 10359446.37564881, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 45.82759797, 0.00050613, 56.30056064, 0.02959107, 5.63005606, 0.08532731, -45.82759797, -0.00050613, -56.30056064, -0.02959107, -5.63005606, -0.08532731, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 38.21942262, 0.00050613, 46.95369201, 0.02959107, 4.6953692, 0.08532731, -38.21942262, -0.00050613, -46.95369201, -0.02959107, -4.6953692, -0.08532731, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 120.40720844, 0.01012267, 120.40720844, 0.03036802, 84.28504591, -4065.84284095, 0.05, 2, 0, 73003, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 30.10180211, 4.127e-05, 90.30540633, 0.00012382, 301.0180211, 0.00041273, -30.10180211, -4.127e-05, -90.30540633, -0.00012382, -301.0180211, -0.00041273, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 120.40720844, 0.01012267, 120.40720844, 0.03036802, 84.28504591, -4065.84284095, 0.05, 2, 0, 73003, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 30.10180211, 4.127e-05, 90.30540633, 0.00012382, 301.0180211, 0.00041273, -30.10180211, -4.127e-05, -90.30540633, -0.00012382, -301.0180211, -0.00041273, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 14.5, 0.0, 10.35)
    ops.node(124003, 14.5, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124003, 0.1225, 30386348.21305013, 12660978.42210422, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 42.97164092, 0.0004872, 52.20610725, 0.03578066, 5.22061073, 0.11108982, -42.97164092, -0.0004872, -52.20610725, -0.03578066, -5.22061073, -0.11108982, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 35.77735146, 0.0004872, 43.4657883, 0.03578066, 4.34657883, 0.11108982, -35.77735146, -0.0004872, -43.4657883, -0.03578066, -4.34657883, -0.11108982, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 150.58283031, 0.0097441, 150.58283031, 0.02923229, 105.40798122, -8023.04835383, 0.05, 2, 0, 74031, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 37.64570758, 4.223e-05, 112.93712273, 0.0001267, 376.45707578, 0.00042234, -37.64570758, -4.223e-05, -112.93712273, -0.0001267, -376.45707578, -0.00042234, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 150.58283031, 0.0097441, 150.58283031, 0.02923229, 105.40798122, -8023.04835383, 0.05, 2, 0, 74031, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 37.64570758, 4.223e-05, 112.93712273, 0.0001267, 376.45707578, 0.00042234, -37.64570758, -4.223e-05, -112.93712273, -0.0001267, -376.45707578, -0.00042234, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 17.65, 0.0, 9.025)
    ops.node(124032, 17.65, 0.0, 9.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173004, 124032, 0.1225, 29178619.189666, 12157757.99569417, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 42.84649976, 0.0004969, 52.1824866, 0.02992028, 5.21824866, 0.08786064, -42.84649976, -0.0004969, -52.1824866, -0.02992028, -5.21824866, -0.08786064, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 36.75238375, 0.0004969, 44.76050047, 0.02992028, 4.47605005, 0.08786064, -36.75238375, -0.0004969, -44.76050047, -0.02992028, -4.47605005, -0.08786064, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 141.26483449, 0.00993793, 141.26483449, 0.0298138, 98.88538414, -3797.2510281, 0.05, 2, 0, 73004, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 35.31620862, 4.126e-05, 105.94862587, 0.00012378, 353.16208623, 0.0004126, -35.31620862, -4.126e-05, -105.94862587, -0.00012378, -353.16208623, -0.0004126, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 141.26483449, 0.00993793, 141.26483449, 0.0298138, 98.88538414, -3797.2510281, 0.05, 2, 0, 73004, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 35.31620862, 4.126e-05, 105.94862587, 0.00012378, 353.16208623, 0.0004126, -35.31620862, -4.126e-05, -105.94862587, -0.00012378, -353.16208623, -0.0004126, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 17.65, 0.0, 10.35)
    ops.node(124004, 17.65, 0.0, 11.35)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124004, 0.1225, 29617636.84838444, 12340682.02016018, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 41.08859307, 0.00047606, 50.02800835, 0.03648062, 5.00280083, 0.11162784, -41.08859307, -0.00047606, -50.02800835, -0.03648062, -5.00280083, -0.11162784, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 34.20200251, 0.00047606, 41.64314081, 0.03648062, 4.16431408, 0.11162784, -34.20200251, -0.00047606, -41.64314081, -0.03648062, -4.16431408, -0.11162784, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 149.05672309, 0.00952112, 149.05672309, 0.02856336, 104.33970616, -8951.08157669, 0.05, 2, 0, 74032, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 37.26418077, 4.289e-05, 111.79254231, 0.00012867, 372.64180771, 0.00042891, -37.26418077, -4.289e-05, -111.79254231, -0.00012867, -372.64180771, -0.00042891, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 149.05672309, 0.00952112, 149.05672309, 0.02856336, 104.33970616, -8951.08157669, 0.05, 2, 0, 74032, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 37.26418077, 4.289e-05, 111.79254231, 0.00012867, 372.64180771, 0.00042891, -37.26418077, -4.289e-05, -111.79254231, -0.00012867, -372.64180771, -0.00042891, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 4081, '-orient', 0, 0, 1, 0, 1, 0)
