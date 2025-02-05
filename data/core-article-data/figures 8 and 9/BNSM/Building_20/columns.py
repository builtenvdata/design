import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 8.15, 0.0, 0.0)
    ops.node(121003, 8.15, 0.0, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1225, 27822730.79933828, 11592804.49972428, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 127.11266458, 0.00102889, 153.94333346, 0.01682742, 15.39433335, 0.05406683, -127.11266458, -0.00102889, -153.94333346, -0.01682742, -15.39433335, -0.05406683, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 138.82352514, 0.00102889, 168.12609737, 0.01682742, 16.81260974, 0.05406683, -138.82352514, -0.00102889, -168.12609737, -0.01682742, -16.81260974, -0.05406683, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 138.42566884, 0.0205779, 138.42566884, 0.0617337, 96.89796819, -1679.805006, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 34.60641721, 9.796e-05, 103.81925163, 0.00029389, 346.06417209, 0.00097962, -34.60641721, -9.796e-05, -103.81925163, -0.00029389, -346.06417209, -0.00097962, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 138.42566884, 0.0205779, 138.42566884, 0.0617337, 96.89796819, -1679.805006, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 34.60641721, 9.796e-05, 103.81925163, 0.00029389, 346.06417209, 0.00097962, -34.60641721, -9.796e-05, -103.81925163, -0.00029389, -346.06417209, -0.00097962, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.45, 0.0, 0.0)
    ops.node(121004, 13.45, 0.0, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.09, 29604556.89257659, 12335232.03857358, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 59.42901319, 0.00111941, 71.9076015, 0.01694283, 7.19076015, 0.06381019, -59.42901319, -0.00111941, -71.9076015, -0.01694283, -7.19076015, -0.06381019, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 68.51920711, 0.00111941, 82.90650604, 0.01694283, 8.2906506, 0.06381019, -68.51920711, -0.00111941, -82.90650604, -0.01694283, -8.2906506, -0.06381019, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 109.53789381, 0.0223882, 109.53789381, 0.06716459, 76.67652566, -1490.67728003, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 27.38447345, 9.916e-05, 82.15342035, 0.00029748, 273.84473452, 0.00099161, -27.38447345, -9.916e-05, -82.15342035, -0.00029748, -273.84473452, -0.00099161, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 109.53789381, 0.0223882, 109.53789381, 0.06716459, 76.67652566, -1490.67728003, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 27.38447345, 9.916e-05, 82.15342035, 0.00029748, 273.84473452, 0.00099161, -27.38447345, -9.916e-05, -82.15342035, -0.00029748, -273.84473452, -0.00099161, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 3.85, 0.0)
    ops.node(121005, 0.0, 3.85, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 29350185.11536952, 12229243.79807063, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 80.20768577, 0.00114934, 96.95162815, 0.017468, 9.69516281, 0.06198497, -80.20768577, -0.00114934, -96.95162815, -0.017468, -9.69516281, -0.06198497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 89.64234361, 0.00114934, 108.35583997, 0.017468, 10.835584, 0.06198497, -89.64234361, -0.00114934, -108.35583997, -0.017468, -10.835584, -0.06198497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 111.95277558, 0.02298686, 111.95277558, 0.06896058, 78.3669429, -1455.76744215, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 27.98819389, 0.00010223, 83.96458168, 0.00030668, 279.88193895, 0.00102225, -27.98819389, -0.00010223, -83.96458168, -0.00030668, -279.88193895, -0.00102225, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 111.95277558, 0.02298686, 111.95277558, 0.06896058, 78.3669429, -1455.76744215, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 27.98819389, 0.00010223, 83.96458168, 0.00030668, 279.88193895, 0.00102225, -27.98819389, -0.00010223, -83.96458168, -0.00030668, -279.88193895, -0.00102225, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.85, 3.85, 0.0)
    ops.node(121006, 2.85, 3.85, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1225, 29316645.48374938, 12215268.95156224, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 156.42866437, 0.0010612, 188.68418144, 0.02056598, 18.86841814, 0.05768663, -156.42866437, -0.0010612, -188.68418144, -0.02056598, -18.86841814, -0.05768663, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 168.76894956, 0.0010612, 203.56902765, 0.02056598, 20.35690276, 0.05768663, -168.76894956, -0.0010612, -203.56902765, -0.02056598, -20.35690276, -0.05768663, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 148.44074893, 0.02122395, 148.44074893, 0.06367184, 103.90852425, -1686.41571213, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 37.11018723, 9.97e-05, 111.3305617, 0.00029909, 371.10187232, 0.00099697, -37.11018723, -9.97e-05, -111.3305617, -0.00029909, -371.10187232, -0.00099697, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 148.44074893, 0.02122395, 148.44074893, 0.06367184, 103.90852425, -1686.41571213, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 37.11018723, 9.97e-05, 111.3305617, 0.00029909, 371.10187232, 0.00099697, -37.11018723, -9.97e-05, -111.3305617, -0.00029909, -371.10187232, -0.00099697, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.15, 3.85, 0.0)
    ops.node(121007, 8.15, 3.85, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.1225, 29108038.54940441, 12128349.39558517, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 161.74366639, 0.00109238, 194.89905393, 0.01970078, 19.48990539, 0.05511023, -161.74366639, -0.00109238, -194.89905393, -0.01970078, -19.48990539, -0.05511023, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 174.15883147, 0.00109238, 209.85916942, 0.01970078, 20.98591694, 0.05511023, -174.15883147, -0.00109238, -209.85916942, -0.01970078, -20.98591694, -0.05511023, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 147.31897139, 0.02184768, 147.31897139, 0.06554303, 103.12327998, -1614.48350484, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 36.82974285, 9.965e-05, 110.48922855, 0.00029896, 368.29742848, 0.00099652, -36.82974285, -9.965e-05, -110.48922855, -0.00029896, -368.29742848, -0.00099652, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 147.31897139, 0.02184768, 147.31897139, 0.06554303, 103.12327998, -1614.48350484, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 36.82974285, 9.965e-05, 110.48922855, 0.00029896, 368.29742848, 0.00099652, -36.82974285, -9.965e-05, -110.48922855, -0.00029896, -368.29742848, -0.00099652, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.45, 3.85, 0.0)
    ops.node(121008, 13.45, 3.85, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1225, 28772788.93017679, 11988662.05424033, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 137.42943206, 0.00105909, 166.29909399, 0.02515021, 16.6299094, 0.07141613, -137.42943206, -0.00105909, -166.29909399, -0.02515021, -16.6299094, -0.07141613, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 156.08465198, 0.00105909, 188.8731971, 0.02515021, 18.88731971, 0.07141613, -156.08465198, -0.00105909, -188.8731971, -0.02515021, -18.88731971, -0.07141613, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 155.09706385, 0.0211818, 155.09706385, 0.0635454, 108.5679447, -2163.93268659, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 38.77426596, 0.00010614, 116.32279789, 0.00031841, 387.74265964, 0.00106136, -38.77426596, -0.00010614, -116.32279789, -0.00031841, -387.74265964, -0.00106136, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 155.09706385, 0.0211818, 155.09706385, 0.0635454, 108.5679447, -2163.93268659, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 38.77426596, 0.00010614, 116.32279789, 0.00031841, 387.74265964, 0.00106136, -38.77426596, -0.00010614, -116.32279789, -0.00031841, -387.74265964, -0.00106136, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 7.7, 0.0)
    ops.node(121009, 0.0, 7.7, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.0625, 29763744.8946366, 12401560.37276525, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 42.45399167, 0.00135347, 51.19026307, 0.01777799, 5.11902631, 0.06719167, -42.45399167, -0.00135347, -51.19026307, -0.01777799, -5.11902631, -0.06719167, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 46.27088713, 0.00135347, 55.79260727, 0.01777799, 5.57926073, 0.06719167, -46.27088713, -0.00135347, -55.79260727, -0.01777799, -5.57926073, -0.06719167, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 87.8179009, 0.0270694, 87.8179009, 0.0812082, 61.47253063, -1228.10748434, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 21.95447522, 0.00011387, 65.86342567, 0.0003416, 219.54475225, 0.00113866, -21.95447522, -0.00011387, -65.86342567, -0.0003416, -219.54475225, -0.00113866, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 87.8179009, 0.0270694, 87.8179009, 0.0812082, 61.47253063, -1228.10748434, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 21.95447522, 0.00011387, 65.86342567, 0.0003416, 219.54475225, 0.00113866, -21.95447522, -0.00011387, -65.86342567, -0.0003416, -219.54475225, -0.00113866, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.85, 7.7, 0.0)
    ops.node(121010, 2.85, 7.7, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 29032683.72199382, 12096951.55083076, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 153.56127142, 0.00106389, 185.57524576, 0.02529707, 18.55752458, 0.07072314, -153.56127142, -0.00106389, -185.57524576, -0.02529707, -18.55752458, -0.07072314, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 166.07820762, 0.00106389, 200.70167374, 0.02529707, 20.07016737, 0.07072314, -166.07820762, -0.00106389, -200.70167374, -0.02529707, -20.07016737, -0.07072314, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 156.95521581, 0.0212778, 156.95521581, 0.06383341, 109.86865107, -2094.65471649, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 39.23880395, 0.00010645, 117.71641186, 0.00031934, 392.38803953, 0.00106446, -39.23880395, -0.00010645, -117.71641186, -0.00031934, -392.38803953, -0.00106446, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 156.95521581, 0.0212778, 156.95521581, 0.06383341, 109.86865107, -2094.65471649, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 39.23880395, 0.00010645, 117.71641186, 0.00031934, 392.38803953, 0.00106446, -39.23880395, -0.00010645, -117.71641186, -0.00031934, -392.38803953, -0.00106446, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.15, 7.7, 0.0)
    ops.node(121011, 8.15, 7.7, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.1225, 28948284.03663175, 12061785.01526323, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 161.36666682, 0.0010836, 194.48384114, 0.0199202, 19.44838411, 0.05508246, -161.36666682, -0.0010836, -194.48384114, -0.0199202, -19.44838411, -0.05508246, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 173.88002421, 0.0010836, 209.56530659, 0.0199202, 20.95653066, 0.05508246, -173.88002421, -0.0010836, -209.56530659, -0.0199202, -20.95653066, -0.05508246, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 147.17676232, 0.02167198, 147.17676232, 0.06501593, 103.02373362, -1626.57501543, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 36.79419058, 0.00010011, 110.38257174, 0.00030032, 367.9419058, 0.00100105, -36.79419058, -0.00010011, -110.38257174, -0.00030032, -367.9419058, -0.00100105, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 147.17676232, 0.02167198, 147.17676232, 0.06501593, 103.02373362, -1626.57501543, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 36.79419058, 0.00010011, 110.38257174, 0.00030032, 367.9419058, 0.00100105, -36.79419058, -0.00010011, -110.38257174, -0.00030032, -367.9419058, -0.00100105, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.45, 7.7, 0.0)
    ops.node(121012, 13.45, 7.7, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29768114.55131588, 12403381.06304828, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 134.83584068, 0.0010282, 162.87331448, 0.02572263, 16.28733145, 0.07339802, -134.83584068, -0.0010282, -162.87331448, -0.02572263, -16.28733145, -0.07339802, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 152.79127905, 0.0010282, 184.56236796, 0.02572263, 18.4562368, 0.07339802, -152.79127905, -0.0010282, -184.56236796, -0.02572263, -18.4562368, -0.07339802, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 160.64700449, 0.02056406, 160.64700449, 0.06169219, 112.45290314, -2231.59327592, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 40.16175112, 0.00010626, 120.48525337, 0.00031877, 401.61751123, 0.00106258, -40.16175112, -0.00010626, -120.48525337, -0.00031877, -401.61751123, -0.00106258, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 160.64700449, 0.02056406, 160.64700449, 0.06169219, 112.45290314, -2231.59327592, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 40.16175112, 0.00010626, 120.48525337, 0.00031877, 401.61751123, 0.00106258, -40.16175112, -0.00010626, -120.48525337, -0.00031877, -401.61751123, -0.00106258, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 11.55, 0.0)
    ops.node(121013, 0.0, 11.55, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.0625, 29558680.10729924, 12316116.71137469, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 41.3592377, 0.00137038, 49.88773437, 0.01769863, 4.98877344, 0.06676376, -41.3592377, -0.00137038, -49.88773437, -0.01769863, -4.98877344, -0.06676376, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 44.8014305, 0.00137038, 54.03972578, 0.01769863, 5.40397258, 0.06676376, -44.8014305, -0.00137038, -54.03972578, -0.01769863, -5.40397258, -0.06676376, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 87.64294541, 0.02740756, 87.64294541, 0.08222269, 61.35006179, -1235.67587732, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 21.91073635, 0.00011443, 65.73220906, 0.00034328, 219.10736353, 0.00114427, -21.91073635, -0.00011443, -65.73220906, -0.00034328, -219.10736353, -0.00114427, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 87.64294541, 0.02740756, 87.64294541, 0.08222269, 61.35006179, -1235.67587732, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 21.91073635, 0.00011443, 65.73220906, 0.00034328, 219.10736353, 0.00114427, -21.91073635, -0.00011443, -65.73220906, -0.00034328, -219.10736353, -0.00114427, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.85, 11.55, 0.0)
    ops.node(121014, 2.85, 11.55, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 28532222.42798179, 11888426.01165908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 165.18075909, 0.0010702, 199.76521296, 0.0258763, 19.9765213, 0.0705008, -165.18075909, -0.0010702, -199.76521296, -0.0258763, -19.9765213, -0.0705008, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 171.37694883, 0.0010702, 207.25871988, 0.0258763, 20.72587199, 0.0705008, -171.37694883, -0.0010702, -207.25871988, -0.0258763, -20.72587199, -0.0705008, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 157.36761049, 0.021404, 157.36761049, 0.06421201, 110.15732734, -2171.42421645, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 39.34190262, 0.0001086, 118.02570787, 0.00032579, 393.41902622, 0.00108598, -39.34190262, -0.0001086, -118.02570787, -0.00032579, -393.41902622, -0.00108598, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 157.36761049, 0.021404, 157.36761049, 0.06421201, 110.15732734, -2171.42421645, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 39.34190262, 0.0001086, 118.02570787, 0.00032579, 393.41902622, 0.00108598, -39.34190262, -0.0001086, -118.02570787, -0.00032579, -393.41902622, -0.00108598, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.15, 11.55, 0.0)
    ops.node(121015, 8.15, 11.55, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.1225, 29524053.25041422, 12301688.85433926, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 175.39989706, 0.00108764, 211.2331143, 0.01993072, 21.12331143, 0.05596466, -175.39989706, -0.00108764, -211.2331143, -0.01993072, -21.12331143, -0.05596466, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 181.66794965, 0.00108764, 218.78169496, 0.01993072, 21.8781695, 0.05596466, -181.66794965, -0.00108764, -218.78169496, -0.01993072, -21.8781695, -0.05596466, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 149.24340641, 0.02175278, 149.24340641, 0.06525835, 104.47038449, -1623.52511211, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 37.3108516, 9.953e-05, 111.93255481, 0.00029859, 373.10851602, 0.00099531, -37.3108516, -9.953e-05, -111.93255481, -0.00029859, -373.10851602, -0.00099531, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 149.24340641, 0.02175278, 149.24340641, 0.06525835, 104.47038449, -1623.52511211, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 37.3108516, 9.953e-05, 111.93255481, 0.00029859, 373.10851602, 0.00099531, -37.3108516, -9.953e-05, -111.93255481, -0.00029859, -373.10851602, -0.00099531, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.45, 11.55, 0.0)
    ops.node(121016, 13.45, 11.55, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 28709464.04057002, 11962276.68357084, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 150.30754389, 0.00106214, 181.9006113, 0.02572947, 18.19006113, 0.07189999, -150.30754389, -0.00106214, -181.9006113, -0.02572947, -18.19006113, -0.07189999, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 162.72005859, 0.00106214, 196.92210625, 0.02572947, 19.69221062, 0.07189999, -162.72005859, -0.00106214, -196.92210625, -0.02572947, -19.69221062, -0.07189999, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 154.00063104, 0.02124283, 154.00063104, 0.06372848, 107.80044173, -2132.99947529, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 38.50015776, 0.00010562, 115.50047328, 0.00031685, 385.00157759, 0.00105618, -38.50015776, -0.00010562, -115.50047328, -0.00031685, -385.00157759, -0.00105618, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 154.00063104, 0.02124283, 154.00063104, 0.06372848, 107.80044173, -2132.99947529, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 38.50015776, 0.00010562, 115.50047328, 0.00031685, 385.00157759, 0.00105618, -38.50015776, -0.00010562, -115.50047328, -0.00031685, -385.00157759, -0.00105618, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 15.4, 0.0)
    ops.node(121017, 0.0, 15.4, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.0625, 30201579.21782729, 12583991.34076137, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 42.22041577, 0.00133077, 50.86768468, 0.01733106, 5.08676847, 0.06746275, -42.22041577, -0.00133077, -50.86768468, -0.01733106, -5.08676847, -0.06746275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 46.01689076, 0.00133077, 55.44172521, 0.01733106, 5.54417252, 0.06746275, -46.01689076, -0.00133077, -55.44172521, -0.01733106, -5.54417252, -0.06746275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 87.76040816, 0.02661535, 87.76040816, 0.07984604, 61.43228571, -1197.18637826, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 21.94010204, 0.00011214, 65.82030612, 0.00033642, 219.40102041, 0.00112141, -21.94010204, -0.00011214, -65.82030612, -0.00033642, -219.40102041, -0.00112141, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 87.76040816, 0.02661535, 87.76040816, 0.07984604, 61.43228571, -1197.18637826, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 21.94010204, 0.00011214, 65.82030612, 0.00033642, 219.40102041, 0.00112141, -21.94010204, -0.00011214, -65.82030612, -0.00033642, -219.40102041, -0.00112141, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.85, 15.4, 0.0)
    ops.node(121018, 2.85, 15.4, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 30441083.63528915, 12683784.84803715, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 165.43819134, 0.00106388, 199.40813907, 0.02579225, 19.94081391, 0.07324166, -165.43819134, -0.00106388, -199.40813907, -0.02579225, -19.94081391, -0.07324166, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 171.42149131, 0.00106388, 206.62000898, 0.02579225, 20.6620009, 0.07324166, -171.42149131, -0.00106388, -206.62000898, -0.02579225, -20.6620009, -0.07324166, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 163.12876469, 0.02127755, 163.12876469, 0.06383266, 114.19013528, -2124.7268151, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 40.78219117, 0.00010551, 122.34657351, 0.00031654, 407.82191171, 0.00105514, -40.78219117, -0.00010551, -122.34657351, -0.00031654, -407.82191171, -0.00105514, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 163.12876469, 0.02127755, 163.12876469, 0.06383266, 114.19013528, -2124.7268151, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 40.78219117, 0.00010551, 122.34657351, 0.00031654, 407.82191171, 0.00105514, -40.78219117, -0.00010551, -122.34657351, -0.00031654, -407.82191171, -0.00105514, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.15, 15.4, 0.0)
    ops.node(121019, 8.15, 15.4, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.1225, 29481137.17334965, 12283807.15556235, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 183.99053682, 0.00110109, 221.59268189, 0.02512668, 22.15926819, 0.06772275, -183.99053682, -0.00110109, -221.59268189, -0.02512668, -22.15926819, -0.06772275, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 183.99053682, 0.00110109, 221.59268189, 0.02512668, 22.15926819, 0.06772275, -183.99053682, -0.00110109, -221.59268189, -0.02512668, -22.15926819, -0.06772275, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 163.9122933, 0.02202179, 163.9122933, 0.06606536, 114.73860531, -2036.05148608, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 40.97807333, 0.00010947, 122.93421998, 0.00032842, 409.78073326, 0.00109473, -40.97807333, -0.00010947, -122.93421998, -0.00032842, -409.78073326, -0.00109473, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 163.9122933, 0.02202179, 163.9122933, 0.06606536, 114.73860531, -2036.05148608, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 40.97807333, 0.00010947, 122.93421998, 0.00032842, 409.78073326, 0.00109473, -40.97807333, -0.00010947, -122.93421998, -0.00032842, -409.78073326, -0.00109473, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 13.45, 15.4, 0.0)
    ops.node(121020, 13.45, 15.4, 3.15)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 30412020.66071639, 12671675.27529849, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 153.29379699, 0.00107017, 184.92265845, 0.02514657, 18.49226584, 0.0736497, -153.29379699, -0.00107017, -184.92265845, -0.02514657, -18.49226584, -0.0736497, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 165.67984875, 0.00107017, 199.86430425, 0.02514657, 19.98643043, 0.0736497, -165.67984875, -0.00107017, -199.86430425, -0.02514657, -19.98643043, -0.0736497, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 159.31287764, 0.02140344, 159.31287764, 0.06421033, 111.51901435, -2096.88286096, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 39.82821941, 0.00010314, 119.48465823, 0.00030943, 398.2821941, 0.00103145, -39.82821941, -0.00010314, -119.48465823, -0.00030943, -398.2821941, -0.00103145, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 159.31287764, 0.02140344, 159.31287764, 0.06421033, 111.51901435, -2096.88286096, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 39.82821941, 0.00010314, 119.48465823, 0.00030943, 398.2821941, 0.00103145, -39.82821941, -0.00010314, -119.48465823, -0.00030943, -398.2821941, -0.00103145, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 19.25, 0.0)
    ops.node(121021, 0.0, 19.25, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.0625, 28274496.97854435, 11781040.40772681, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 36.22285884, 0.00134688, 43.97816966, 0.01922081, 4.39781697, 0.07295595, -36.22285884, -0.00134688, -43.97816966, -0.01922081, -4.39781697, -0.07295595, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 39.64434799, 0.00134688, 48.13219933, 0.01922081, 4.81321993, 0.07295595, -39.64434799, -0.00134688, -48.13219933, -0.01922081, -4.81321993, -0.07295595, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 82.19404537, 0.02693759, 82.19404537, 0.08081278, 57.53583176, -1503.19582859, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 20.54851134, 0.00011219, 61.64553403, 0.00033656, 205.48511343, 0.00112187, -20.54851134, -0.00011219, -61.64553403, -0.00033656, -205.48511343, -0.00112187, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 82.19404537, 0.02693759, 82.19404537, 0.08081278, 57.53583176, -1503.19582859, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 20.54851134, 0.00011219, 61.64553403, 0.00033656, 205.48511343, 0.00112187, -20.54851134, -0.00011219, -61.64553403, -0.00033656, -205.48511343, -0.00112187, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 2.85, 19.25, 0.0)
    ops.node(121022, 2.85, 19.25, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.09, 29505554.99546578, 12293981.24811074, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 94.60054646, 0.00118788, 114.22357702, 0.01769698, 11.4223577, 0.06134583, -94.60054646, -0.00118788, -114.22357702, -0.01769698, -11.4223577, -0.06134583, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 99.48321791, 0.00118788, 120.11906303, 0.01769698, 12.0119063, 0.06134583, -99.48321791, -0.00118788, -120.11906303, -0.01769698, -12.0119063, -0.06134583, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 113.90673005, 0.0237576, 113.90673005, 0.07127281, 79.73471104, -1443.84378974, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 28.47668251, 0.00010346, 85.43004754, 0.00031039, 284.76682513, 0.00103462, -28.47668251, -0.00010346, -85.43004754, -0.00031039, -284.76682513, -0.00103462, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 113.90673005, 0.0237576, 113.90673005, 0.07127281, 79.73471104, -1443.84378974, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 28.47668251, 0.00010346, 85.43004754, 0.00031039, 284.76682513, 0.00103462, -28.47668251, -0.00010346, -85.43004754, -0.00031039, -284.76682513, -0.00103462, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 8.15, 19.25, 0.0)
    ops.node(121023, 8.15, 19.25, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.1225, 28186091.72620538, 11744204.88591891, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 149.81515789, 0.00106887, 181.35690861, 0.02523726, 18.13569086, 0.06995216, -149.81515789, -0.00106887, -181.35690861, -0.02523726, -18.13569086, -0.06995216, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 143.68009159, 0.00106887, 173.93017907, 0.02523726, 17.39301791, 0.06995216, -143.68009159, -0.00106887, -173.93017907, -0.02523726, -17.39301791, -0.06995216, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 152.3651834, 0.02137749, 152.3651834, 0.06413246, 106.65562838, -2092.68655074, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 38.09129585, 0.00010644, 114.27388755, 0.00031931, 380.91295851, 0.00106437, -38.09129585, -0.00010644, -114.27388755, -0.00031931, -380.91295851, -0.00106437, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 152.3651834, 0.02137749, 152.3651834, 0.06413246, 106.65562838, -2092.68655074, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 38.09129585, 0.00010644, 114.27388755, 0.00031931, 380.91295851, 0.00106437, -38.09129585, -0.00010644, -114.27388755, -0.00031931, -380.91295851, -0.00106437, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 13.45, 19.25, 0.0)
    ops.node(121024, 13.45, 19.25, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.09, 29334061.25741038, 12222525.52392099, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 83.97107473, 0.00114732, 101.65792573, 0.01761957, 10.16579257, 0.06417664, -83.97107473, -0.00114732, -101.65792573, -0.01761957, -10.16579257, -0.06417664, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 83.97107473, 0.00114732, 101.65792573, 0.01761957, 10.16579257, 0.06417664, -83.97107473, -0.00114732, -101.65792573, -0.01761957, -10.16579257, -0.06417664, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 109.17471348, 0.02294637, 109.17471348, 0.0688391, 76.42229944, -1504.65217445, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 27.29367837, 9.974e-05, 81.88103511, 0.00029923, 272.9367837, 0.00099744, -27.29367837, -9.974e-05, -81.88103511, -0.00029923, -272.9367837, -0.00099744, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 109.17471348, 0.02294637, 109.17471348, 0.0688391, 76.42229944, -1504.65217445, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 27.29367837, 9.974e-05, 81.88103511, 0.00029923, 272.9367837, 0.00099744, -27.29367837, -9.974e-05, -81.88103511, -0.00029923, -272.9367837, -0.00099744, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.15, 0.0, 3.6)
    ops.node(122003, 8.15, 0.0, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1225, 28364455.65409087, 11818523.18920453, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 87.19535584, 0.00089235, 105.83737448, 0.01639154, 10.58373745, 0.05786366, -87.19535584, -0.00089235, -105.83737448, -0.01639154, -10.58373745, -0.05786366, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 76.16062884, 0.00089235, 92.44346695, 0.01639154, 9.24434669, 0.05786366, -76.16062884, -0.00089235, -92.44346695, -0.01639154, -9.24434669, -0.05786366, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 136.19834452, 0.01784701, 136.19834452, 0.05354103, 95.33884117, -2192.49726326, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 34.04958613, 7.902e-05, 102.14875839, 0.00023707, 340.49586131, 0.00079023, -34.04958613, -7.902e-05, -102.14875839, -0.00023707, -340.49586131, -0.00079023, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 136.19834452, 0.01784701, 136.19834452, 0.05354103, 95.33884117, -2192.49726326, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 34.04958613, 7.902e-05, 102.14875839, 0.00023707, 340.49586131, 0.00079023, -34.04958613, -7.902e-05, -102.14875839, -0.00023707, -340.49586131, -0.00079023, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.45, 0.0, 3.6)
    ops.node(122004, 13.45, 0.0, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.09, 28502347.76707625, 11875978.23628177, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 51.64209055, 0.00098202, 62.76120567, 0.01726204, 6.27612057, 0.06610698, -51.64209055, -0.00098202, -62.76120567, -0.01726204, -6.27612057, -0.06610698, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 47.23106979, 0.00098202, 57.40044319, 0.01726204, 5.74004432, 0.06610698, -47.23106979, -0.00098202, -57.40044319, -0.01726204, -5.74004432, -0.06610698, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 104.4757302, 0.01964036, 104.4757302, 0.05892109, 73.13301114, -2081.36305438, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 26.11893255, 8.211e-05, 78.35679765, 0.00024632, 261.18932549, 0.00082107, -26.11893255, -8.211e-05, -78.35679765, -0.00024632, -261.18932549, -0.00082107, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 104.4757302, 0.01964036, 104.4757302, 0.05892109, 73.13301114, -2081.36305438, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 26.11893255, 8.211e-05, 78.35679765, 0.00024632, 261.18932549, 0.00082107, -26.11893255, -8.211e-05, -78.35679765, -0.00024632, -261.18932549, -0.00082107, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 3.85, 3.55)
    ops.node(122005, 0.0, 3.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 29711434.97458602, 12379764.57274417, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 57.80641677, 0.00098162, 69.98696549, 0.01741159, 6.99869655, 0.06557689, -57.80641677, -0.00098162, -69.98696549, -0.01741159, -6.99869655, -0.06557689, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 67.22673317, 0.00098162, 81.39226262, 0.01741159, 8.13922626, 0.06557689, -67.22673317, -0.00098162, -81.39226262, -0.01741159, -8.13922626, -0.06557689, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 110.41208273, 0.01963249, 110.41208273, 0.05889748, 77.28845791, -1948.51843432, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 27.60302068, 8.324e-05, 82.80906204, 0.00024973, 276.03020681, 0.00083242, -27.60302068, -8.324e-05, -82.80906204, -0.00024973, -276.03020681, -0.00083242, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 110.41208273, 0.01963249, 110.41208273, 0.05889748, 77.28845791, -1948.51843432, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 27.60302068, 8.324e-05, 82.80906204, 0.00024973, 276.03020681, 0.00083242, -27.60302068, -8.324e-05, -82.80906204, -0.00024973, -276.03020681, -0.00083242, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.85, 3.85, 3.55)
    ops.node(122006, 2.85, 3.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1225, 28835944.71810736, 12014976.96587807, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 98.63253781, 0.00090997, 119.42729226, 0.02421401, 11.94272923, 0.07159427, -98.63253781, -0.00090997, -119.42729226, -0.02421401, -11.94272923, -0.07159427, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 93.17111889, 0.00090997, 112.81443927, 0.02421401, 11.28144393, 0.07159427, -93.17111889, -0.00090997, -112.81443927, -0.02421401, -11.28144393, -0.07159427, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 154.6665136, 0.01819949, 154.6665136, 0.05459846, 108.26655952, -2675.7128448, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 38.6666284, 8.827e-05, 115.9998852, 0.00026481, 386.666284, 0.00088271, -38.6666284, -8.827e-05, -115.9998852, -0.00026481, -386.666284, -0.00088271, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 154.6665136, 0.01819949, 154.6665136, 0.05459846, 108.26655952, -2675.7128448, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 38.6666284, 8.827e-05, 115.9998852, 0.00026481, 386.666284, 0.00088271, -38.6666284, -8.827e-05, -115.9998852, -0.00026481, -386.666284, -0.00088271, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.15, 3.85, 3.55)
    ops.node(122007, 8.15, 3.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.1225, 28414397.05274494, 11839332.10531039, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 103.54271157, 0.00092793, 125.33480433, 0.0158104, 12.53348043, 0.04947205, -103.54271157, -0.00092793, -125.33480433, -0.0158104, -12.53348043, -0.04947205, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 97.80506714, 0.00092793, 118.3895879, 0.0158104, 11.83895879, 0.04947205, -97.80506714, -0.00092793, -118.3895879, -0.0158104, -11.83895879, -0.04947205, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 128.81940282, 0.01855852, 128.81940282, 0.05567557, 90.17358197, -1613.60550222, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 32.2048507, 7.461e-05, 96.61455211, 0.00022383, 322.04850704, 0.0007461, -32.2048507, -7.461e-05, -96.61455211, -0.00022383, -322.04850704, -0.0007461, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 128.81940282, 0.01855852, 128.81940282, 0.05567557, 90.17358197, -1613.60550222, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 32.2048507, 7.461e-05, 96.61455211, 0.00022383, 322.04850704, 0.0007461, -32.2048507, -7.461e-05, -96.61455211, -0.00022383, -322.04850704, -0.0007461, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.45, 3.85, 3.55)
    ops.node(122008, 13.45, 3.85, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1225, 28819413.93867648, 12008089.1411152, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 93.43941637, 0.00089671, 113.36112159, 0.02474122, 11.33611216, 0.07490377, -93.43941637, -0.00089671, -113.36112159, -0.02474122, -11.33611216, -0.07490377, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 87.84585264, 0.00089671, 106.57498483, 0.02474122, 10.65749848, 0.07490377, -87.84585264, -0.00089671, -106.57498483, -0.02474122, -10.65749848, -0.07490377, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 149.48990116, 0.01793413, 149.48990116, 0.05380238, 104.64293081, -2840.76371516, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 37.37247529, 8.537e-05, 112.11742587, 0.0002561, 373.7247529, 0.00085365, -37.37247529, -8.537e-05, -112.11742587, -0.0002561, -373.7247529, -0.00085365, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 149.48990116, 0.01793413, 149.48990116, 0.05380238, 104.64293081, -2840.76371516, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 37.37247529, 8.537e-05, 112.11742587, 0.0002561, 373.7247529, 0.00085365, -37.37247529, -8.537e-05, -112.11742587, -0.0002561, -373.7247529, -0.00085365, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 7.7, 3.55)
    ops.node(122009, 0.0, 7.7, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.0625, 29154531.46772906, 12147721.44488711, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 37.66201168, 0.00115083, 45.59894742, 0.01860826, 4.55989474, 0.07166087, -37.66201168, -0.00115083, -45.59894742, -0.01860826, -4.55989474, -0.07166087, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 41.30681121, 0.00115083, 50.01185621, 0.01860826, 5.00118562, 0.07166087, -41.30681121, -0.00115083, -50.01185621, -0.01860826, -5.00118562, -0.07166087, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 83.77947496, 0.02301656, 83.77947496, 0.06904968, 58.64563247, -1623.85352934, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 20.94486874, 9.269e-05, 62.83460622, 0.00027808, 209.44868739, 0.00092692, -20.94486874, -9.269e-05, -62.83460622, -0.00027808, -209.44868739, -0.00092692, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 83.77947496, 0.02301656, 83.77947496, 0.06904968, 58.64563247, -1623.85352934, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 20.94486874, 9.269e-05, 62.83460622, 0.00027808, 209.44868739, 0.00092692, -20.94486874, -9.269e-05, -62.83460622, -0.00027808, -209.44868739, -0.00092692, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.85, 7.7, 3.55)
    ops.node(122010, 2.85, 7.7, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 29422481.4410108, 12259367.26708784, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 97.75250562, 0.00090375, 118.36679251, 0.02457007, 11.83667925, 0.07434846, -97.75250562, -0.00090375, -118.36679251, -0.02457007, -11.83667925, -0.07434846, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 91.94863828, 0.00090375, 111.33899147, 0.02457007, 11.13389915, 0.07434846, -91.94863828, -0.00090375, -111.33899147, -0.02457007, -11.13389915, -0.07434846, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 154.23935552, 0.01807506, 154.23935552, 0.05422518, 107.96754886, -2786.34664077, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 38.55983888, 8.627e-05, 115.67951664, 0.00025882, 385.59838879, 0.00086272, -38.55983888, -8.627e-05, -115.67951664, -0.00025882, -385.59838879, -0.00086272, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 154.23935552, 0.01807506, 154.23935552, 0.05422518, 107.96754886, -2786.34664077, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 38.55983888, 8.627e-05, 115.67951664, 0.00025882, 385.59838879, 0.00086272, -38.55983888, -8.627e-05, -115.67951664, -0.00025882, -385.59838879, -0.00086272, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.15, 7.7, 3.55)
    ops.node(122011, 8.15, 7.7, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.1225, 28763916.87455272, 11984965.36439697, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 105.10807373, 0.00091751, 127.16339658, 0.01567853, 12.71633966, 0.04974372, -105.10807373, -0.00091751, -127.16339658, -0.01567853, -12.71633966, -0.04974372, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 99.10477021, 0.00091751, 119.90039157, 0.01567853, 11.99003916, 0.04974372, -99.10477021, -0.00091751, -119.90039157, -0.01567853, -11.99003916, -0.04974372, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 130.10784769, 0.01835011, 130.10784769, 0.05505032, 91.07549338, -1613.9884437, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 32.52696192, 7.444e-05, 97.58088577, 0.00022332, 325.26961922, 0.00074441, -32.52696192, -7.444e-05, -97.58088577, -0.00022332, -325.26961922, -0.00074441, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 130.10784769, 0.01835011, 130.10784769, 0.05505032, 91.07549338, -1613.9884437, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 32.52696192, 7.444e-05, 97.58088577, 0.00022332, 325.26961922, 0.00074441, -32.52696192, -7.444e-05, -97.58088577, -0.00022332, -325.26961922, -0.00074441, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.45, 7.7, 3.55)
    ops.node(122012, 13.45, 7.7, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 29813771.69456388, 12422404.87273495, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 93.32690741, 0.00089751, 112.99132144, 0.02462953, 11.29913214, 0.07587162, -93.32690741, -0.00089751, -112.99132144, -0.02462953, -11.29913214, -0.07587162, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 87.87127325, 0.00089751, 106.38615974, 0.02462953, 10.63861597, 0.07587162, -87.87127325, -0.00089751, -106.38615974, -0.02462953, -10.63861597, -0.07587162, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 152.89458158, 0.01795026, 152.89458158, 0.05385077, 107.02620711, -2829.34168781, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 38.2236454, 8.44e-05, 114.67093619, 0.00025319, 382.23645396, 0.00084398, -38.2236454, -8.44e-05, -114.67093619, -0.00025319, -382.23645396, -0.00084398, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 152.89458158, 0.01795026, 152.89458158, 0.05385077, 107.02620711, -2829.34168781, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 38.2236454, 8.44e-05, 114.67093619, 0.00025319, 382.23645396, 0.00084398, -38.2236454, -8.44e-05, -114.67093619, -0.00025319, -382.23645396, -0.00084398, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 11.55, 3.55)
    ops.node(122013, 0.0, 11.55, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.0625, 29456380.08809245, 12273491.70337186, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 31.24833418, 0.00115991, 37.81175305, 0.01743689, 3.78117531, 0.07090759, -31.24833418, -0.00115991, -37.81175305, -0.01743689, -3.78117531, -0.07090759, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 31.24833418, 0.00115991, 37.81175305, 0.01743689, 3.78117531, 0.07090759, -31.24833418, -0.00115991, -37.81175305, -0.01743689, -3.78117531, -0.07090759, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 82.33037262, 0.0231982, 82.33037262, 0.06959459, 57.63126084, -1522.50533281, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 20.58259316, 9.016e-05, 61.74777947, 0.00027047, 205.82593156, 0.00090155, -20.58259316, -9.016e-05, -61.74777947, -0.00027047, -205.82593156, -0.00090155, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 82.33037262, 0.0231982, 82.33037262, 0.06959459, 57.63126084, -1522.50533281, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 20.58259316, 9.016e-05, 61.74777947, 0.00027047, 205.82593156, 0.00090155, -20.58259316, -9.016e-05, -61.74777947, -0.00027047, -205.82593156, -0.00090155, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.85, 11.55, 3.55)
    ops.node(122014, 2.85, 11.55, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 29505534.20344594, 12293972.58476914, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 96.3932815, 0.00089843, 116.70112077, 0.02433205, 11.67011208, 0.07420682, -96.3932815, -0.00089843, -116.70112077, -0.02433205, -11.67011208, -0.07420682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 90.76730983, 0.00089843, 109.88988674, 0.02433205, 10.98898867, 0.07420682, -90.76730983, -0.00089843, -109.88988674, -0.02433205, -10.98898867, -0.07420682, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 154.4182842, 0.01796858, 154.4182842, 0.05390574, 108.09279894, -2780.07380631, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 38.60457105, 8.613e-05, 115.81371315, 0.00025839, 386.0457105, 0.00086129, -38.60457105, -8.613e-05, -115.81371315, -0.00025839, -386.0457105, -0.00086129, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 154.4182842, 0.01796858, 154.4182842, 0.05390574, 108.09279894, -2780.07380631, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 38.60457105, 8.613e-05, 115.81371315, 0.00025839, 386.0457105, 0.00086129, -38.60457105, -8.613e-05, -115.81371315, -0.00025839, -386.0457105, -0.00086129, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.15, 11.55, 3.55)
    ops.node(122015, 8.15, 11.55, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.1225, 29240689.8067724, 12183620.75282183, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 104.32165432, 0.00089819, 126.11282451, 0.01615712, 12.61128245, 0.05074673, -104.32165432, -0.00089819, -126.11282451, -0.01615712, -12.61128245, -0.05074673, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 98.36076018, 0.00089819, 118.90679234, 0.01615712, 11.89067923, 0.05074673, -98.36076018, -0.00089819, -118.90679234, -0.01615712, -11.89067923, -0.05074673, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 132.97664567, 0.01796377, 132.97664567, 0.05389132, 93.08365197, -1651.53519198, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 33.24416142, 7.484e-05, 99.73248425, 0.00022452, 332.44161417, 0.00074841, -33.24416142, -7.484e-05, -99.73248425, -0.00022452, -332.44161417, -0.00074841, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 132.97664567, 0.01796377, 132.97664567, 0.05389132, 93.08365197, -1651.53519198, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 33.24416142, 7.484e-05, 99.73248425, 0.00022452, 332.44161417, 0.00074841, -33.24416142, -7.484e-05, -99.73248425, -0.00022452, -332.44161417, -0.00074841, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.45, 11.55, 3.55)
    ops.node(122016, 13.45, 11.55, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 30227655.90669308, 12594856.62778878, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 94.31659821, 0.00087908, 114.08071473, 0.02477198, 11.40807147, 0.07642508, -94.31659821, -0.00087908, -114.08071473, -0.02477198, -11.40807147, -0.07642508, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 88.62226706, 0.00087908, 107.19313205, 0.02477198, 10.7193132, 0.07642508, -88.62226706, -0.00087908, -107.19313205, -0.02477198, -10.7193132, -0.07642508, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 156.55206977, 0.0175817, 156.55206977, 0.05274509, 109.58644884, -2943.53157304, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 39.13801744, 8.523e-05, 117.41405233, 0.0002557, 391.38017442, 0.00085233, -39.13801744, -8.523e-05, -117.41405233, -0.0002557, -391.38017442, -0.00085233, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 156.55206977, 0.0175817, 156.55206977, 0.05274509, 109.58644884, -2943.53157304, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 39.13801744, 8.523e-05, 117.41405233, 0.0002557, 391.38017442, 0.00085233, -39.13801744, -8.523e-05, -117.41405233, -0.0002557, -391.38017442, -0.00085233, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 15.4, 3.55)
    ops.node(122017, 0.0, 15.4, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.0625, 29673107.50280973, 12363794.79283739, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 37.08991391, 0.0012106, 44.86077368, 0.01849202, 4.48607737, 0.07225358, -37.08991391, -0.0012106, -44.86077368, -0.01849202, -4.48607737, -0.07225358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 40.21676734, 0.0012106, 48.64274698, 0.01849202, 4.8642747, 0.07225358, -40.21676734, -0.0012106, -48.64274698, -0.01849202, -4.8642747, -0.07225358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 84.76788784, 0.02421198, 84.76788784, 0.07263594, 59.33752148, -1624.62783552, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 21.19197196, 9.215e-05, 63.57591588, 0.00027644, 211.91971959, 0.00092146, -21.19197196, -9.215e-05, -63.57591588, -0.00027644, -211.91971959, -0.00092146, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 84.76788784, 0.02421198, 84.76788784, 0.07263594, 59.33752148, -1624.62783552, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 21.19197196, 9.215e-05, 63.57591588, 0.00027644, 211.91971959, 0.00092146, -21.19197196, -9.215e-05, -63.57591588, -0.00027644, -211.91971959, -0.00092146, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.85, 15.4, 3.55)
    ops.node(122018, 2.85, 15.4, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 28635075.94096793, 11931281.64206997, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 93.60926989, 0.00090358, 113.51908314, 0.02451756, 11.35190831, 0.07333101, -93.60926989, -0.00090358, -113.51908314, -0.02451756, -11.35190831, -0.07333101, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 88.33942896, 0.00090358, 107.1283965, 0.02451756, 10.71283965, 0.07333101, -88.33942896, -0.00090358, -107.1283965, -0.02451756, -10.71283965, -0.07333101, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 151.3136439, 0.0180716, 151.3136439, 0.05421479, 105.91955073, -2783.17856951, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 37.82841098, 8.696e-05, 113.48523293, 0.00026089, 378.28410975, 0.00086963, -37.82841098, -8.696e-05, -113.48523293, -0.00026089, -378.28410975, -0.00086963, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 151.3136439, 0.0180716, 151.3136439, 0.05421479, 105.91955073, -2783.17856951, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 37.82841098, 8.696e-05, 113.48523293, 0.00026089, 378.28410975, 0.00086963, -37.82841098, -8.696e-05, -113.48523293, -0.00026089, -378.28410975, -0.00086963, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.15, 15.4, 3.55)
    ops.node(122019, 8.15, 15.4, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.1225, 29963530.92484351, 12484804.55201813, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 116.08952045, 0.0009247, 140.14900411, 0.01986791, 14.01490041, 0.06012765, -116.08952045, -0.0009247, -140.14900411, -0.01986791, -14.01490041, -0.06012765, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 105.65185541, 0.0009247, 127.54813924, 0.01986791, 12.75481392, 0.06012765, -105.65185541, -0.0009247, -127.54813924, -0.01986791, -12.75481392, -0.06012765, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 145.17856008, 0.01849398, 145.17856008, 0.05548194, 101.62499206, -1989.9717518, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 36.29464002, 7.974e-05, 108.88392006, 0.00023921, 362.9464002, 0.00079738, -36.29464002, -7.974e-05, -108.88392006, -0.00023921, -362.9464002, -0.00079738, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 145.17856008, 0.01849398, 145.17856008, 0.05548194, 101.62499206, -1989.9717518, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 36.29464002, 7.974e-05, 108.88392006, 0.00023921, 362.9464002, 0.00079738, -36.29464002, -7.974e-05, -108.88392006, -0.00023921, -362.9464002, -0.00079738, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 13.45, 15.4, 3.55)
    ops.node(122020, 13.45, 15.4, 5.95)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 31136101.84242232, 12973375.76767597, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 93.37488851, 0.00085908, 112.68382419, 0.02435999, 11.26838242, 0.07684443, -93.37488851, -0.00085908, -112.68382419, -0.02435999, -11.26838242, -0.07684443, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 87.77074239, 0.00085908, 105.92080015, 0.02435999, 10.59208001, 0.07684443, -87.77074239, -0.00085908, -105.92080015, -0.02435999, -10.59208001, -0.07684443, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 157.87197327, 0.01718154, 157.87197327, 0.05154461, 110.51038129, -2831.98412231, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 39.46799332, 8.344e-05, 118.40397995, 0.00025033, 394.67993317, 0.00083444, -39.46799332, -8.344e-05, -118.40397995, -0.00025033, -394.67993317, -0.00083444, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 157.87197327, 0.01718154, 157.87197327, 0.05154461, 110.51038129, -2831.98412231, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 39.46799332, 8.344e-05, 118.40397995, 0.00025033, 394.67993317, 0.00083444, -39.46799332, -8.344e-05, -118.40397995, -0.00025033, -394.67993317, -0.00083444, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 19.25, 3.6)
    ops.node(122021, 0.0, 19.25, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.0625, 29493935.56057769, 12289139.81690737, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 27.36681146, 0.00111123, 33.21038972, 0.01849146, 3.32103897, 0.07693641, -27.36681146, -0.00111123, -33.21038972, -0.01849146, -3.32103897, -0.07693641, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 27.36681146, 0.00111123, 33.21038972, 0.01849146, 3.32103897, 0.07693641, -27.36681146, -0.00111123, -33.21038972, -0.01849146, -3.32103897, -0.07693641, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 80.82082825, 0.02222469, 80.82082825, 0.06667407, 56.57457977, -2020.96676243, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 20.20520706, 8.839e-05, 60.61562119, 0.00026517, 202.05207062, 0.0008839, -20.20520706, -8.839e-05, -60.61562119, -0.00026517, -202.05207062, -0.0008839, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 80.82082825, 0.02222469, 80.82082825, 0.06667407, 56.57457977, -2020.96676243, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 20.20520706, 8.839e-05, 60.61562119, 0.00026517, 202.05207062, 0.0008839, -20.20520706, -8.839e-05, -60.61562119, -0.00026517, -202.05207062, -0.0008839, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 2.85, 19.25, 3.6)
    ops.node(122022, 2.85, 19.25, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.09, 30597044.86677891, 12748768.69449121, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 55.22720076, 0.00095258, 66.70083854, 0.01702653, 6.67008385, 0.06547102, -55.22720076, -0.00095258, -66.70083854, -0.01702653, -6.67008385, -0.06547102, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 50.77806736, 0.00095258, 61.32738262, 0.01702653, 6.13273826, 0.06547102, -50.77806736, -0.00095258, -61.32738262, -0.01702653, -6.13273826, -0.06547102, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 113.1969885, 0.01905162, 113.1969885, 0.05715487, 79.23789195, -1889.72248511, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 28.29924713, 8.287e-05, 84.89774138, 0.00024861, 282.99247125, 0.00082871, -28.29924713, -8.287e-05, -84.89774138, -0.00024861, -282.99247125, -0.00082871, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 113.1969885, 0.01905162, 113.1969885, 0.05715487, 79.23789195, -1889.72248511, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 28.29924713, 8.287e-05, 84.89774138, 0.00024861, 282.99247125, 0.00082871, -28.29924713, -8.287e-05, -84.89774138, -0.00024861, -282.99247125, -0.00082871, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 8.15, 19.25, 3.6)
    ops.node(122023, 8.15, 19.25, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.1225, 29135056.63365114, 12139606.93068798, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 95.65829162, 0.00087806, 115.94439795, 0.01667415, 11.5944398, 0.05376091, -95.65829162, -0.00087806, -115.94439795, -0.01667415, -11.5944398, -0.05376091, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 89.77230325, 0.00087806, 108.81017712, 0.01667415, 10.88101771, 0.05376091, -89.77230325, -0.00087806, -108.81017712, -0.01667415, -10.88101771, -0.05376091, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 127.43166352, 0.01756128, 127.43166352, 0.05268385, 89.20216446, -1697.31339305, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 31.85791588, 7.198e-05, 95.57374764, 0.00021594, 318.57915879, 0.00071981, -31.85791588, -7.198e-05, -95.57374764, -0.00021594, -318.57915879, -0.00071981, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 127.43166352, 0.01756128, 127.43166352, 0.05268385, 89.20216446, -1697.31339305, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 31.85791588, 7.198e-05, 95.57374764, 0.00021594, 318.57915879, 0.00071981, -31.85791588, -7.198e-05, -95.57374764, -0.00021594, -318.57915879, -0.00071981, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 13.45, 19.25, 3.6)
    ops.node(122024, 13.45, 19.25, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.09, 29643926.87312956, 12351636.19713732, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 51.84718251, 0.00097879, 62.85835032, 0.01728769, 6.28583503, 0.06717733, -51.84718251, -0.00097879, -62.85835032, -0.01728769, -6.28583503, -0.06717733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 47.47754781, 0.00097879, 57.56070413, 0.01728769, 5.75607041, 0.06717733, -47.47754781, -0.00097879, -57.56070413, -0.01728769, -5.75607041, -0.06717733, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 107.22074914, 0.01957575, 107.22074914, 0.05872724, 75.0545244, -2065.47207901, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 26.80518729, 8.102e-05, 80.41556186, 0.00024306, 268.05187285, 0.0008102, -26.80518729, -8.102e-05, -80.41556186, -0.00024306, -268.05187285, -0.0008102, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 107.22074914, 0.01957575, 107.22074914, 0.05872724, 75.0545244, -2065.47207901, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 26.80518729, 8.102e-05, 80.41556186, 0.00024306, 268.05187285, 0.0008102, -26.80518729, -8.102e-05, -80.41556186, -0.00024306, -268.05187285, -0.0008102, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.15, 0.0, 6.4)
    ops.node(123003, 8.15, 0.0, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 29332768.68434987, 12221986.95181245, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 31.55915853, 0.00115604, 38.18883574, 0.01744007, 3.81888357, 0.07040024, -31.55915853, -0.00115604, -38.18883574, -0.01744007, -3.81888357, -0.07040024, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 31.55915853, 0.00115604, 38.18883574, 0.01744007, 3.81888357, 0.07040024, -31.55915853, -0.00115604, -38.18883574, -0.01744007, -3.81888357, -0.07040024, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 82.91731282, 0.02312079, 82.91731282, 0.06936236, 58.04211898, -1537.5837263, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 20.72932821, 9.118e-05, 62.18798462, 0.00027354, 207.29328205, 0.00091181, -20.72932821, -9.118e-05, -62.18798462, -0.00027354, -207.29328205, -0.00091181, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 82.91731282, 0.02312079, 82.91731282, 0.06936236, 58.04211898, -1537.5837263, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 20.72932821, 9.118e-05, 62.18798462, 0.00027354, 207.29328205, 0.00091181, -20.72932821, -9.118e-05, -62.18798462, -0.00027354, -207.29328205, -0.00091181, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.45, 0.0, 6.4)
    ops.node(123004, 13.45, 0.0, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 29353371.1610828, 12230571.31711783, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 27.31919635, 0.00112733, 33.16648063, 0.01897117, 3.31664806, 0.07745537, -27.31919635, -0.00112733, -33.16648063, -0.01897117, -3.31664806, -0.07745537, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 27.31919635, 0.00112733, 33.16648063, 0.01897117, 3.31664806, 0.07745537, -27.31919635, -0.00112733, -33.16648063, -0.01897117, -3.31664806, -0.07745537, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 80.88078107, 0.02254661, 80.88078107, 0.06763983, 56.61654675, -2076.58286998, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 20.22019527, 8.888e-05, 60.6605858, 0.00026664, 202.20195268, 0.00088879, -20.22019527, -8.888e-05, -60.6605858, -0.00026664, -202.20195268, -0.00088879, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 80.88078107, 0.02254661, 80.88078107, 0.06763983, 56.61654675, -2076.58286998, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 20.22019527, 8.888e-05, 60.6605858, 0.00026664, 202.20195268, 0.00088879, -20.22019527, -8.888e-05, -60.6605858, -0.00026664, -202.20195268, -0.00088879, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 3.85, 6.35)
    ops.node(123005, 0.0, 3.85, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 30174667.91990622, 12572778.29996092, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 34.96305164, 0.00116249, 42.30674812, 0.01836294, 4.23067481, 0.0752662, -34.96305164, -0.00116249, -42.30674812, -0.01836294, -4.23067481, -0.0752662, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 38.15090228, 0.00116249, 46.16418011, 0.01836294, 4.61641801, 0.0752662, -38.15090228, -0.00116249, -46.16418011, -0.01836294, -4.61641801, -0.0752662, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 82.29646022, 0.0232498, 82.29646022, 0.06974941, 57.60752215, -1697.41707578, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 20.57411505, 8.797e-05, 61.72234516, 0.00026392, 205.74115054, 0.00087973, -20.57411505, -8.797e-05, -61.72234516, -0.00026392, -205.74115054, -0.00087973, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 82.29646022, 0.0232498, 82.29646022, 0.06974941, 57.60752215, -1697.41707578, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 20.57411505, 8.797e-05, 61.72234516, 0.00026392, 205.74115054, 0.00087973, -20.57411505, -8.797e-05, -61.72234516, -0.00026392, -205.74115054, -0.00087973, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.85, 3.85, 6.35)
    ops.node(123006, 2.85, 3.85, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 29573095.02816795, 12322122.92840331, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 48.37806978, 0.00128386, 58.3834349, 0.01820105, 5.83834349, 0.06143947, -48.37806978, -0.00128386, -58.3834349, -0.01820105, -5.83834349, -0.06143947, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 48.37806978, 0.00128386, 58.3834349, 0.01820105, 5.83834349, 0.06143947, -48.37806978, -0.00128386, -58.3834349, -0.01820105, -5.83834349, -0.06143947, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 79.3663108, 0.02567717, 79.3663108, 0.0770315, 55.55641756, -1211.54426376, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 19.8415777, 8.657e-05, 59.5247331, 0.0002597, 198.41577699, 0.00086567, -19.8415777, -8.657e-05, -59.5247331, -0.0002597, -198.41577699, -0.00086567, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 79.3663108, 0.02567717, 79.3663108, 0.0770315, 55.55641756, -1211.54426376, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 19.8415777, 8.657e-05, 59.5247331, 0.0002597, 198.41577699, 0.00086567, -19.8415777, -8.657e-05, -59.5247331, -0.0002597, -198.41577699, -0.00086567, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.15, 3.85, 6.35)
    ops.node(123007, 8.15, 3.85, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.0625, 31020624.39152125, 12925260.16313385, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 51.38483235, 0.00125415, 61.78402576, 0.01745827, 6.17840258, 0.06158452, -51.38483235, -0.00125415, -61.78402576, -0.01745827, -6.17840258, -0.06158452, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 51.38483235, 0.00125415, 61.78402576, 0.01745827, 6.17840258, 0.06158452, -51.38483235, -0.00125415, -61.78402576, -0.01745827, -6.17840258, -0.06158452, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 80.56811023, 0.02508293, 80.56811023, 0.07524878, 56.39767716, -1183.91744227, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 20.14202756, 8.378e-05, 60.42608267, 0.00025133, 201.42027557, 0.00083777, -20.14202756, -8.378e-05, -60.42608267, -0.00025133, -201.42027557, -0.00083777, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 80.56811023, 0.02508293, 80.56811023, 0.07524878, 56.39767716, -1183.91744227, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 20.14202756, 8.378e-05, 60.42608267, 0.00025133, 201.42027557, 0.00083777, -20.14202756, -8.378e-05, -60.42608267, -0.00025133, -201.42027557, -0.00083777, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.45, 3.85, 6.35)
    ops.node(123008, 13.45, 3.85, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 29592332.04092986, 12330138.35038744, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 47.04465904, 0.00123286, 56.9178215, 0.01860477, 5.69178215, 0.06530035, -47.04465904, -0.00123286, -56.9178215, -0.01860477, -5.69178215, -0.06530035, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 47.04465904, 0.00123286, 56.9178215, 0.01860477, 5.69178215, 0.06530035, -47.04465904, -0.00123286, -56.9178215, -0.01860477, -5.69178215, -0.06530035, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 75.86760801, 0.02465729, 75.86760801, 0.07397186, 53.10732561, -1283.38306281, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 18.966902, 8.27e-05, 56.90070601, 0.00024809, 189.66902004, 0.00082697, -18.966902, -8.27e-05, -56.90070601, -0.00024809, -189.66902004, -0.00082697, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 75.86760801, 0.02465729, 75.86760801, 0.07397186, 53.10732561, -1283.38306281, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 18.966902, 8.27e-05, 56.90070601, 0.00024809, 189.66902004, 0.00082697, -18.966902, -8.27e-05, -56.90070601, -0.00024809, -189.66902004, -0.00082697, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 7.7, 6.35)
    ops.node(123009, 0.0, 7.7, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 28288363.00231304, 11786817.91763043, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 33.52045397, 0.0011538, 40.78396155, 0.01952705, 4.07839616, 0.07684564, -33.52045397, -0.0011538, -40.78396155, -0.01952705, -4.07839616, -0.07684564, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 36.93313603, 0.0011538, 44.93613365, 0.01952705, 4.49361337, 0.07684564, -36.93313603, -0.0011538, -44.93613365, -0.01952705, -4.49361337, -0.07684564, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 78.90845892, 0.0230759, 78.90845892, 0.0692277, 55.23592124, -2049.77964466, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 19.72711473, 8.998e-05, 59.18134419, 0.00026993, 197.27114729, 0.00089976, -19.72711473, -8.998e-05, -59.18134419, -0.00026993, -197.27114729, -0.00089976, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 78.90845892, 0.0230759, 78.90845892, 0.0692277, 55.23592124, -2049.77964466, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 19.72711473, 8.998e-05, 59.18134419, 0.00026993, 197.27114729, 0.00089976, -19.72711473, -8.998e-05, -59.18134419, -0.00026993, -197.27114729, -0.00089976, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.85, 7.7, 6.35)
    ops.node(123010, 2.85, 7.7, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 29193245.06808516, 12163852.11170215, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 47.06555923, 0.00131253, 56.92597874, 0.01802121, 5.69259787, 0.06277877, -47.06555923, -0.00131253, -56.92597874, -0.01802121, -5.69259787, -0.06277877, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 47.06555923, 0.00131253, 56.92597874, 0.01802121, 5.69259787, 0.06277877, -47.06555923, -0.00131253, -56.92597874, -0.01802121, -5.69259787, -0.06277877, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 72.70547318, 0.02625062, 72.70547318, 0.07875187, 50.89383123, -1201.00407686, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 18.1763683, 8.033e-05, 54.52910489, 0.000241, 181.76368296, 0.00080333, -18.1763683, -8.033e-05, -54.52910489, -0.000241, -181.76368296, -0.00080333, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 72.70547318, 0.02625062, 72.70547318, 0.07875187, 50.89383123, -1201.00407686, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 18.1763683, 8.033e-05, 54.52910489, 0.000241, 181.76368296, 0.00080333, -18.1763683, -8.033e-05, -54.52910489, -0.000241, -181.76368296, -0.00080333, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.15, 7.7, 6.35)
    ops.node(123011, 8.15, 7.7, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.0625, 30428713.35648407, 12678630.5652017, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 50.15477756, 0.00128789, 60.37951189, 0.01748328, 6.03795119, 0.06081464, -50.15477756, -0.00128789, -60.37951189, -0.01748328, -6.03795119, -0.06081464, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 50.15477756, 0.00128789, 60.37951189, 0.01748328, 6.03795119, 0.06081464, -50.15477756, -0.00128789, -60.37951189, -0.01748328, -6.03795119, -0.06081464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 78.15525044, 0.02575782, 78.15525044, 0.07727346, 54.70867531, -1165.01319909, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 19.53881261, 8.285e-05, 58.61643783, 0.00024855, 195.3881261, 0.00082849, -19.53881261, -8.285e-05, -58.61643783, -0.00024855, -195.3881261, -0.00082849, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 78.15525044, 0.02575782, 78.15525044, 0.07727346, 54.70867531, -1165.01319909, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 19.53881261, 8.285e-05, 58.61643783, 0.00024855, 195.3881261, 0.00082849, -19.53881261, -8.285e-05, -58.61643783, -0.00024855, -195.3881261, -0.00082849, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.45, 7.7, 6.35)
    ops.node(123012, 13.45, 7.7, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 29284838.15243782, 12202015.89684909, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 46.10304031, 0.00123774, 55.81253836, 0.01836384, 5.58125384, 0.06470099, -46.10304031, -0.00123774, -55.81253836, -0.01836384, -5.58125384, -0.06470099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 46.10304031, 0.00123774, 55.81253836, 0.01836384, 5.58125384, 0.06470099, -46.10304031, -0.00123774, -55.81253836, -0.01836384, -5.58125384, -0.06470099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 72.79339313, 0.02475479, 72.79339313, 0.07426438, 50.95537519, -1293.41828847, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 18.19834828, 8.018e-05, 54.59504485, 0.00024054, 181.98348282, 0.00080179, -18.19834828, -8.018e-05, -54.59504485, -0.00024054, -181.98348282, -0.00080179, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 72.79339313, 0.02475479, 72.79339313, 0.07426438, 50.95537519, -1293.41828847, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 18.19834828, 8.018e-05, 54.59504485, 0.00024054, 181.98348282, 0.00080179, -18.19834828, -8.018e-05, -54.59504485, -0.00024054, -181.98348282, -0.00080179, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 11.55, 6.35)
    ops.node(123013, 0.0, 11.55, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 27840061.29149565, 11600025.53812319, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 33.26589143, 0.00118077, 40.50848466, 0.01968626, 4.05084847, 0.07652026, -33.26589143, -0.00118077, -40.50848466, -0.01968626, -4.05084847, -0.07652026, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 36.52165777, 0.00118077, 44.47309091, 0.01968626, 4.44730909, 0.07652026, -36.52165777, -0.00118077, -44.47309091, -0.01968626, -4.44730909, -0.07652026, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 77.8472132, 0.02361547, 77.8472132, 0.07084642, 54.49304924, -2030.6921254, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 19.4618033, 9.02e-05, 58.3854099, 0.00027059, 194.61803299, 0.00090195, -19.4618033, -9.02e-05, -58.3854099, -0.00027059, -194.61803299, -0.00090195, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 77.8472132, 0.02361547, 77.8472132, 0.07084642, 54.49304924, -2030.6921254, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 19.4618033, 9.02e-05, 58.3854099, 0.00027059, 194.61803299, 0.00090195, -19.4618033, -9.02e-05, -58.3854099, -0.00027059, -194.61803299, -0.00090195, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.85, 11.55, 6.35)
    ops.node(123014, 2.85, 11.55, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 28895389.69429726, 12039745.70595719, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 46.82476806, 0.00126571, 56.6636681, 0.01855983, 5.66636681, 0.06291473, -46.82476806, -0.00126571, -56.6636681, -0.01855983, -5.66636681, -0.06291473, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 46.82476806, 0.00126571, 56.6636681, 0.01855983, 5.66636681, 0.06291473, -46.82476806, -0.00126571, -56.6636681, -0.01855983, -5.66636681, -0.06291473, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 76.42182502, 0.02531428, 76.42182502, 0.07594283, 53.49527752, -1260.01755572, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 19.10545626, 8.531e-05, 57.31636877, 0.00025593, 191.05456255, 0.0008531, -19.10545626, -8.531e-05, -57.31636877, -0.00025593, -191.05456255, -0.0008531, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 76.42182502, 0.02531428, 76.42182502, 0.07594283, 53.49527752, -1260.01755572, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 19.10545626, 8.531e-05, 57.31636877, 0.00025593, 191.05456255, 0.0008531, -19.10545626, -8.531e-05, -57.31636877, -0.00025593, -191.05456255, -0.0008531, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.15, 11.55, 6.35)
    ops.node(123015, 8.15, 11.55, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.0625, 28198308.26073333, 11749295.10863889, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 51.13939778, 0.00130845, 61.77448777, 0.01730827, 6.17744878, 0.05713189, -51.13939778, -0.00130845, -61.77448777, -0.01730827, -6.17744878, -0.05713189, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 51.13939778, 0.00130845, 61.77448777, 0.01730827, 6.17744878, 0.05713189, -51.13939778, -0.00130845, -61.77448777, -0.01730827, -6.17744878, -0.05713189, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 73.7330645, 0.02616909, 73.7330645, 0.07850726, 51.61314515, -1173.35524005, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 18.43326613, 8.434e-05, 55.29979838, 0.00025303, 184.33266125, 0.00084343, -18.43326613, -8.434e-05, -55.29979838, -0.00025303, -184.33266125, -0.00084343, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 73.7330645, 0.02616909, 73.7330645, 0.07850726, 51.61314515, -1173.35524005, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 18.43326613, 8.434e-05, 55.29979838, 0.00025303, 184.33266125, 0.00084343, -18.43326613, -8.434e-05, -55.29979838, -0.00025303, -184.33266125, -0.00084343, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.45, 11.55, 6.35)
    ops.node(123016, 13.45, 11.55, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 31794396.62053964, 13247665.25855818, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 45.82085756, 0.00123488, 55.14436541, 0.01841959, 5.51443654, 0.06732681, -45.82085756, -0.00123488, -55.14436541, -0.01841959, -5.51443654, -0.06732681, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 45.82085756, 0.00123488, 55.14436541, 0.01841959, 5.51443654, 0.06732681, -45.82085756, -0.00123488, -55.14436541, -0.01841959, -5.51443654, -0.06732681, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 81.28604907, 0.02469769, 81.28604907, 0.07409308, 56.90023435, -1303.46453901, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 20.32151227, 8.247e-05, 60.9645368, 0.0002474, 203.21512267, 0.00082466, -20.32151227, -8.247e-05, -60.9645368, -0.0002474, -203.21512267, -0.00082466, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 81.28604907, 0.02469769, 81.28604907, 0.07409308, 56.90023435, -1303.46453901, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 20.32151227, 8.247e-05, 60.9645368, 0.0002474, 203.21512267, 0.00082466, -20.32151227, -8.247e-05, -60.9645368, -0.0002474, -203.21512267, -0.00082466, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 15.4, 6.35)
    ops.node(123017, 0.0, 15.4, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 34.01604501, 0.00112467, 41.09788839, 0.01835712, 4.10978884, 0.07821905, -34.01604501, -0.00112467, -41.09788839, -0.01835712, -4.10978884, -0.07821905, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 37.4418437, 0.00112467, 45.23690844, 0.01835712, 4.52369084, 0.07821905, -37.4418437, -0.00112467, -45.23690844, -0.01835712, -4.52369084, -0.07821905, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 82.42590027, 0.02249333, 82.42590027, 0.06747999, 57.69813019, -1910.75710846, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 20.60647507, 8.518e-05, 61.8194252, 0.00025553, 206.06475067, 0.00085178, -20.60647507, -8.518e-05, -61.8194252, -0.00025553, -206.06475067, -0.00085178, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 82.42590027, 0.02249333, 82.42590027, 0.06747999, 57.69813019, -1910.75710846, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 20.60647507, 8.518e-05, 61.8194252, 0.00025553, 206.06475067, 0.00085178, -20.60647507, -8.518e-05, -61.8194252, -0.00025553, -206.06475067, -0.00085178, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.85, 15.4, 6.35)
    ops.node(123018, 2.85, 15.4, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 30248916.66944319, 12603715.27893466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 46.82133977, 0.00121879, 56.51346061, 0.01800022, 5.65134606, 0.06407563, -46.82133977, -0.00121879, -56.51346061, -0.01800022, -5.65134606, -0.06407563, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 46.82133977, 0.00121879, 56.51346061, 0.01800022, 5.65134606, 0.06407563, -46.82133977, -0.00121879, -56.51346061, -0.01800022, -5.65134606, -0.06407563, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 73.05148763, 0.02437581, 73.05148763, 0.07312744, 51.13604134, -1161.74480439, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 18.26287191, 7.79e-05, 54.78861572, 0.0002337, 182.62871907, 0.00077899, -18.26287191, -7.79e-05, -54.78861572, -0.0002337, -182.62871907, -0.00077899, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 73.05148763, 0.02437581, 73.05148763, 0.07312744, 51.13604134, -1161.74480439, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 18.26287191, 7.79e-05, 54.78861572, 0.0002337, 182.62871907, 0.00077899, -18.26287191, -7.79e-05, -54.78861572, -0.0002337, -182.62871907, -0.00077899, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.15, 15.4, 6.35)
    ops.node(123019, 8.15, 15.4, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.0625, 29723133.21736702, 12384638.84056959, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 50.58349544, 0.00125104, 60.97447842, 0.01844977, 6.09744784, 0.06076318, -50.58349544, -0.00125104, -60.97447842, -0.01844977, -6.09744784, -0.06076318, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 50.58349544, 0.00125104, 60.97447842, 0.01844977, 6.09744784, 0.06076318, -50.58349544, -0.00125104, -60.97447842, -0.01844977, -6.09744784, -0.06076318, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 78.4119345, 0.02502079, 78.4119345, 0.07506236, 54.88835415, -1190.76610407, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 19.60298362, 8.509e-05, 58.80895087, 0.00025528, 196.02983625, 0.00085094, -19.60298362, -8.509e-05, -58.80895087, -0.00025528, -196.02983625, -0.00085094, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 78.4119345, 0.02502079, 78.4119345, 0.07506236, 54.88835415, -1190.76610407, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 19.60298362, 8.509e-05, 58.80895087, 0.00025528, 196.02983625, 0.00085094, -19.60298362, -8.509e-05, -58.80895087, -0.00025528, -196.02983625, -0.00085094, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 13.45, 15.4, 6.35)
    ops.node(123020, 13.45, 15.4, 8.725)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 30140039.15801616, 12558349.6491734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 46.30822385, 0.0012601, 55.9616251, 0.0182232, 5.59616251, 0.06552489, -46.30822385, -0.0012601, -55.9616251, -0.0182232, -5.59616251, -0.06552489, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 46.30822385, 0.0012601, 55.9616251, 0.0182232, 5.59616251, 0.06552489, -46.30822385, -0.0012601, -55.9616251, -0.0182232, -5.59616251, -0.06552489, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 73.4787162, 0.02520203, 73.4787162, 0.07560609, 51.43510134, -1229.28914561, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 18.36967905, 7.864e-05, 55.10903715, 0.00023591, 183.6967905, 0.00078637, -18.36967905, -7.864e-05, -55.10903715, -0.00023591, -183.6967905, -0.00078637, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 73.4787162, 0.02520203, 73.4787162, 0.07560609, 51.43510134, -1229.28914561, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 18.36967905, 7.864e-05, 55.10903715, 0.00023591, 183.6967905, 0.00078637, -18.36967905, -7.864e-05, -55.10903715, -0.00023591, -183.6967905, -0.00078637, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 19.25, 6.4)
    ops.node(123021, 0.0, 19.25, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 28658988.31722701, 11941245.13217792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 24.84971397, 0.00110423, 30.27205536, 0.01936756, 3.02720554, 0.08059392, -24.84971397, -0.00110423, -30.27205536, -0.01936756, -3.02720554, -0.08059392, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 24.84971397, 0.00110423, 30.27205536, 0.01936756, 3.02720554, 0.08059392, -24.84971397, -0.00110423, -30.27205536, -0.01936756, -3.02720554, -0.08059392, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 76.78809288, 0.0220846, 76.78809288, 0.0662538, 53.75166501, -2764.68154963, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 19.19702322, 8.643e-05, 57.59106966, 0.00025928, 191.97023219, 0.00086426, -19.19702322, -8.643e-05, -57.59106966, -0.00025928, -191.97023219, -0.00086426, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 76.78809288, 0.0220846, 76.78809288, 0.0662538, 53.75166501, -2764.68154963, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 19.19702322, 8.643e-05, 57.59106966, 0.00025928, 191.97023219, 0.00086426, -19.19702322, -8.643e-05, -57.59106966, -0.00025928, -191.97023219, -0.00086426, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 2.85, 19.25, 6.4)
    ops.node(123022, 2.85, 19.25, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 29015982.99376784, 12089992.91406994, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 38.69313423, 0.00117412, 46.93459396, 0.0187078, 4.6934594, 0.07415396, -38.69313423, -0.00117412, -46.93459396, -0.0187078, -4.6934594, -0.07415396, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 35.35882706, 0.00117412, 42.89009469, 0.0187078, 4.28900947, 0.07415396, -35.35882706, -0.00117412, -42.89009469, -0.0187078, -4.28900947, -0.07415396, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 82.02558415, 0.02348233, 82.02558415, 0.07044698, 57.4179089, -1789.30814273, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 20.50639604, 9.118e-05, 61.51918811, 0.00027355, 205.06396037, 0.00091185, -20.50639604, -9.118e-05, -61.51918811, -0.00027355, -205.06396037, -0.00091185, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 82.02558415, 0.02348233, 82.02558415, 0.07044698, 57.4179089, -1789.30814273, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 20.50639604, 9.118e-05, 61.51918811, 0.00027355, 205.06396037, 0.00091185, -20.50639604, -9.118e-05, -61.51918811, -0.00027355, -205.06396037, -0.00091185, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 8.15, 19.25, 6.4)
    ops.node(123023, 8.15, 19.25, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.0625, 29547375.95342891, 12311406.64726205, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 46.56884494, 0.00118214, 56.32816538, 0.01891682, 5.63281654, 0.06509153, -46.56884494, -0.00118214, -56.32816538, -0.01891682, -5.63281654, -0.06509153, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 46.56884494, 0.00118214, 56.32816538, 0.01891682, 5.63281654, 0.06509153, -46.56884494, -0.00118214, -56.32816538, -0.01891682, -5.63281654, -0.06509153, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 78.56539523, 0.02364281, 78.56539523, 0.07092843, 54.99577666, -1319.40342879, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 19.64134881, 8.577e-05, 58.92404642, 0.0002573, 196.41348807, 0.00085768, -19.64134881, -8.577e-05, -58.92404642, -0.0002573, -196.41348807, -0.00085768, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 78.56539523, 0.02364281, 78.56539523, 0.07092843, 54.99577666, -1319.40342879, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 19.64134881, 8.577e-05, 58.92404642, 0.0002573, 196.41348807, 0.00085768, -19.64134881, -8.577e-05, -58.92404642, -0.0002573, -196.41348807, -0.00085768, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 13.45, 19.25, 6.4)
    ops.node(123024, 13.45, 19.25, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 29170535.41267037, 12154389.75527932, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 27.17553048, 0.00110859, 33.00569134, 0.01891417, 3.30056913, 0.07723232, -27.17553048, -0.00110859, -33.00569134, -0.01891417, -3.30056913, -0.07723232, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 27.17553048, 0.00110859, 33.00569134, 0.01891417, 3.30056913, 0.07723232, -27.17553048, -0.00110859, -33.00569134, -0.01891417, -3.30056913, -0.07723232, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 81.01964018, 0.02217189, 81.01964018, 0.06651566, 56.71374813, -2112.33239518, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 20.25491005, 8.959e-05, 60.76473014, 0.00026877, 202.54910046, 0.00089589, -20.25491005, -8.959e-05, -60.76473014, -0.00026877, -202.54910046, -0.00089589, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 81.01964018, 0.02217189, 81.01964018, 0.06651566, 56.71374813, -2112.33239518, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 20.25491005, 8.959e-05, 60.76473014, 0.00026877, 202.54910046, 0.00089589, -20.25491005, -8.959e-05, -60.76473014, -0.00026877, -202.54910046, -0.00089589, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.15, 0.0, 9.2)
    ops.node(124003, 8.15, 0.0, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 28037298.35132778, 11682207.64638657, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 24.1644374, 0.00107018, 29.50098621, 0.01965586, 2.95009862, 0.08190862, -24.1644374, -0.00107018, -29.50098621, -0.01965586, -2.95009862, -0.08190862, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 24.1644374, 0.00107018, 29.50098621, 0.01965586, 2.95009862, 0.08190862, -24.1644374, -0.00107018, -29.50098621, -0.01965586, -2.95009862, -0.08190862, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 74.96413577, 0.02140365, 74.96413577, 0.06421095, 52.47489504, -3411.87387183, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 18.74103394, 8.624e-05, 56.22310183, 0.00025873, 187.41033943, 0.00086244, -18.74103394, -8.624e-05, -56.22310183, -0.00025873, -187.41033943, -0.00086244, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 74.96413577, 0.02140365, 74.96413577, 0.06421095, 52.47489504, -3411.87387183, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 18.74103394, 8.624e-05, 56.22310183, 0.00025873, 187.41033943, 0.00086244, -18.74103394, -8.624e-05, -56.22310183, -0.00025873, -187.41033943, -0.00086244, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.45, 0.0, 9.2)
    ops.node(124004, 13.45, 0.0, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 31434178.94242973, 13097574.55934572, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 22.54490572, 0.00104385, 27.29663801, 0.01889422, 2.7296638, 0.08405948, -22.54490572, -0.00104385, -27.29663801, -0.01889422, -2.7296638, -0.08405948, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 22.54490572, 0.00104385, 27.29663801, 0.01889422, 2.7296638, 0.08405948, -22.54490572, -0.00104385, -27.29663801, -0.01889422, -2.7296638, -0.08405948, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 79.72651555, 0.02087691, 79.72651555, 0.06263072, 55.80856088, -5576.69171182, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 19.93162889, 8.181e-05, 59.79488666, 0.00024543, 199.31628887, 0.00081811, -19.93162889, -8.181e-05, -59.79488666, -0.00024543, -199.31628887, -0.00081811, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 79.72651555, 0.02087691, 79.72651555, 0.06263072, 55.80856088, -5576.69171182, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 19.93162889, 8.181e-05, 59.79488666, 0.00024543, 199.31628887, 0.00081811, -19.93162889, -8.181e-05, -59.79488666, -0.00024543, -199.31628887, -0.00081811, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 3.85, 9.175)
    ops.node(124005, 0.0, 3.85, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 29363664.02316358, 12234860.00965149, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 24.32896245, 0.00106665, 29.60413404, 0.01881931, 2.9604134, 0.08150099, -24.32896245, -0.00106665, -29.60413404, -0.01881931, -2.9604134, -0.08150099, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 24.32896245, 0.00106665, 29.60413404, 0.01881931, 2.9604134, 0.08150099, -24.32896245, -0.00106665, -29.60413404, -0.01881931, -2.9604134, -0.08150099, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 76.29071444, 0.02133291, 76.29071444, 0.06399874, 53.40350011, -3112.36319646, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 19.07267861, 8.381e-05, 57.21803583, 0.00025142, 190.72678611, 0.00083805, -19.07267861, -8.381e-05, -57.21803583, -0.00025142, -190.72678611, -0.00083805, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 76.29071444, 0.02133291, 76.29071444, 0.06399874, 53.40350011, -3112.36319646, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 19.07267861, 8.381e-05, 57.21803583, 0.00025142, 190.72678611, 0.00083805, -19.07267861, -8.381e-05, -57.21803583, -0.00025142, -190.72678611, -0.00083805, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.85, 3.85, 9.175)
    ops.node(124006, 2.85, 3.85, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 29502791.1085671, 12292829.62856962, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 40.30574833, 0.00120433, 48.96008929, 0.0192582, 4.89600893, 0.07146962, -40.30574833, -0.00120433, -48.96008929, -0.0192582, -4.89600893, -0.07146962, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 40.30574833, 0.00120433, 48.96008929, 0.0192582, 4.89600893, 0.07146962, -40.30574833, -0.00120433, -48.96008929, -0.0192582, -4.89600893, -0.07146962, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 66.13395616, 0.0240866, 66.13395616, 0.07225981, 46.29376931, -1653.94600806, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 16.53348904, 7.231e-05, 49.60046712, 0.00021692, 165.33489039, 0.00072306, -16.53348904, -7.231e-05, -49.60046712, -0.00021692, -165.33489039, -0.00072306, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 66.13395616, 0.0240866, 66.13395616, 0.07225981, 46.29376931, -1653.94600806, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 16.53348904, 7.231e-05, 49.60046712, 0.00021692, 165.33489039, 0.00072306, -16.53348904, -7.231e-05, -49.60046712, -0.00021692, -165.33489039, -0.00072306, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.15, 3.85, 9.175)
    ops.node(124007, 8.15, 3.85, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.0625, 29091600.08226525, 12121500.03427719, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 39.23069716, 0.00123097, 47.70325145, 0.02013165, 4.77032515, 0.07216012, -39.23069716, -0.00123097, -47.70325145, -0.02013165, -4.77032515, -0.07216012, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 39.23069716, 0.00123097, 47.70325145, 0.02013165, 4.77032515, 0.07216012, -39.23069716, -0.00123097, -47.70325145, -0.02013165, -4.77032515, -0.07216012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 72.09809167, 0.02461942, 72.09809167, 0.07385825, 50.46866417, -1846.93778449, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 18.02452292, 7.994e-05, 54.07356875, 0.00023982, 180.24522917, 0.0007994, -18.02452292, -7.994e-05, -54.07356875, -0.00023982, -180.24522917, -0.0007994, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 72.09809167, 0.02461942, 72.09809167, 0.07385825, 50.46866417, -1846.93778449, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 18.02452292, 7.994e-05, 54.07356875, 0.00023982, 180.24522917, 0.0007994, -18.02452292, -7.994e-05, -54.07356875, -0.00023982, -180.24522917, -0.0007994, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.45, 3.85, 9.175)
    ops.node(124008, 13.45, 3.85, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 28929448.73600231, 12053936.9733343, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 37.68235902, 0.00121356, 45.90401877, 0.02043958, 4.59040188, 0.07465095, -37.68235902, -0.00121356, -45.90401877, -0.02043958, -4.59040188, -0.07465095, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 37.68235902, 0.00121356, 45.90401877, 0.02043958, 4.59040188, 0.07465095, -37.68235902, -0.00121356, -45.90401877, -0.02043958, -4.59040188, -0.07465095, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 68.64487578, 0.02427126, 68.64487578, 0.07281378, 48.05141305, -2474.2686522, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 17.16121894, 7.654e-05, 51.48365683, 0.00022961, 171.61218945, 0.00076538, -17.16121894, -7.654e-05, -51.48365683, -0.00022961, -171.61218945, -0.00076538, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 68.64487578, 0.02427126, 68.64487578, 0.07281378, 48.05141305, -2474.2686522, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 17.16121894, 7.654e-05, 51.48365683, 0.00022961, 171.61218945, 0.00076538, -17.16121894, -7.654e-05, -51.48365683, -0.00022961, -171.61218945, -0.00076538, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 7.7, 9.175)
    ops.node(124009, 0.0, 7.7, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 29240683.46867206, 12183618.11194669, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 22.66507997, 0.00108073, 27.61547422, 0.01989796, 2.76154742, 0.0844019, -22.66507997, -0.00108073, -27.61547422, -0.01989796, -2.76154742, -0.0844019, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 22.66507997, 0.00108073, 27.61547422, 0.01989796, 2.76154742, 0.0844019, -22.66507997, -0.00108073, -27.61547422, -0.01989796, -2.76154742, -0.0844019, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 77.73988574, 0.02161457, 77.73988574, 0.0648437, 54.41792002, -5662.47998058, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 19.43497144, 8.576e-05, 58.30491431, 0.00025727, 194.34971435, 0.00085756, -19.43497144, -8.576e-05, -58.30491431, -0.00025727, -194.34971435, -0.00085756, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 77.73988574, 0.02161457, 77.73988574, 0.0648437, 54.41792002, -5662.47998058, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 19.43497144, 8.576e-05, 58.30491431, 0.00025727, 194.34971435, 0.00085756, -19.43497144, -8.576e-05, -58.30491431, -0.00025727, -194.34971435, -0.00085756, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.85, 7.7, 9.175)
    ops.node(124010, 2.85, 7.7, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 30357664.43954884, 12649026.84981202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 39.28849488, 0.00116774, 47.65650158, 0.01979686, 4.76565016, 0.07371896, -39.28849488, -0.00116774, -47.65650158, -0.01979686, -4.76565016, -0.07371896, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 39.28849488, 0.00116774, 47.65650158, 0.01979686, 4.76565016, 0.07371896, -39.28849488, -0.00116774, -47.65650158, -0.01979686, -4.76565016, -0.07371896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 71.06207011, 0.02335489, 71.06207011, 0.07006467, 49.74344908, -2043.58396927, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 17.76551753, 7.551e-05, 53.29655258, 0.00022652, 177.65517528, 0.00075506, -17.76551753, -7.551e-05, -53.29655258, -0.00022652, -177.65517528, -0.00075506, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 71.06207011, 0.02335489, 71.06207011, 0.07006467, 49.74344908, -2043.58396927, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 17.76551753, 7.551e-05, 53.29655258, 0.00022652, 177.65517528, 0.00075506, -17.76551753, -7.551e-05, -53.29655258, -0.00022652, -177.65517528, -0.00075506, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.15, 7.7, 9.175)
    ops.node(124011, 8.15, 7.7, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.0625, 30059672.92295786, 12524863.71789911, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 42.64168814, 0.00117201, 51.72762518, 0.01896037, 5.17276252, 0.07158024, -42.64168814, -0.00117201, -51.72762518, -0.01896037, -5.17276252, -0.07158024, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 42.64168814, 0.00117201, 51.72762518, 0.01896037, 5.17276252, 0.07158024, -42.64168814, -0.00117201, -51.72762518, -0.01896037, -5.17276252, -0.07158024, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 67.61080891, 0.02344025, 67.61080891, 0.07032075, 47.32756624, -1689.44774374, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 16.90270223, 7.255e-05, 50.70810668, 0.00021765, 169.02702228, 0.00072551, -16.90270223, -7.255e-05, -50.70810668, -0.00021765, -169.02702228, -0.00072551, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 67.61080891, 0.02344025, 67.61080891, 0.07032075, 47.32756624, -1689.44774374, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 16.90270223, 7.255e-05, 50.70810668, 0.00021765, 169.02702228, 0.00072551, -16.90270223, -7.255e-05, -50.70810668, -0.00021765, -169.02702228, -0.00072551, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.45, 7.7, 9.175)
    ops.node(124012, 13.45, 7.7, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 29223038.73213694, 12176266.13839039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 38.25243817, 0.00119965, 46.56454785, 0.02007179, 4.65645479, 0.07440573, -38.25243817, -0.00119965, -46.56454785, -0.02007179, -4.65645479, -0.07440573, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 38.25243817, 0.00119965, 46.56454785, 0.02007179, 4.65645479, 0.07440573, -38.25243817, -0.00119965, -46.56454785, -0.02007179, -4.65645479, -0.07440573, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 66.98136737, 0.02399303, 66.98136737, 0.07197908, 46.88695716, -2396.36849741, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 16.74534184, 7.393e-05, 50.23602553, 0.0002218, 167.45341843, 0.00073933, -16.74534184, -7.393e-05, -50.23602553, -0.0002218, -167.45341843, -0.00073933, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 66.98136737, 0.02399303, 66.98136737, 0.07197908, 46.88695716, -2396.36849741, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 16.74534184, 7.393e-05, 50.23602553, 0.0002218, 167.45341843, 0.00073933, -16.74534184, -7.393e-05, -50.23602553, -0.0002218, -167.45341843, -0.00073933, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 11.55, 9.175)
    ops.node(124013, 0.0, 11.55, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 27588891.6174261, 11495371.50726088, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 22.70824617, 0.0010896, 27.77961359, 0.02040727, 2.77796136, 0.0844009, -22.70824617, -0.0010896, -27.77961359, -0.02040727, -2.77796136, -0.0844009, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 22.70824617, 0.0010896, 27.77961359, 0.02040727, 2.77796136, 0.0844009, -22.70824617, -0.0010896, -27.77961359, -0.02040727, -2.77796136, -0.0844009, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 73.71339707, 0.02179209, 73.71339707, 0.06537626, 51.59937795, -5406.52261651, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 18.42834927, 8.618e-05, 55.2850478, 0.00025855, 184.28349267, 0.00086183, -18.42834927, -8.618e-05, -55.2850478, -0.00025855, -184.28349267, -0.00086183, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 73.71339707, 0.02179209, 73.71339707, 0.06537626, 51.59937795, -5406.52261651, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 18.42834927, 8.618e-05, 55.2850478, 0.00025855, 184.28349267, 0.00086183, -18.42834927, -8.618e-05, -55.2850478, -0.00025855, -184.28349267, -0.00086183, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.85, 11.55, 9.175)
    ops.node(124014, 2.85, 11.55, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 30239701.23109622, 12599875.51295676, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 39.66641671, 0.00118566, 48.13048259, 0.01960582, 4.81304826, 0.07347612, -39.66641671, -0.00118566, -48.13048259, -0.01960582, -4.81304826, -0.07347612, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 39.66641671, 0.00118566, 48.13048259, 0.01960582, 4.81304826, 0.07347612, -39.66641671, -0.00118566, -48.13048259, -0.01960582, -4.81304826, -0.07347612, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 69.84413759, 0.02371318, 69.84413759, 0.07113955, 48.89089631, -2038.77530913, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 17.4610344, 7.45e-05, 52.38310319, 0.0002235, 174.61034398, 0.00074501, -17.4610344, -7.45e-05, -52.38310319, -0.0002235, -174.61034398, -0.00074501, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 69.84413759, 0.02371318, 69.84413759, 0.07113955, 48.89089631, -2038.77530913, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 17.4610344, 7.45e-05, 52.38310319, 0.0002235, 174.61034398, 0.00074501, -17.4610344, -7.45e-05, -52.38310319, -0.0002235, -174.61034398, -0.00074501, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.15, 11.55, 9.175)
    ops.node(124015, 8.15, 11.55, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.0625, 28955036.54104822, 12064598.55877009, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 40.18630762, 0.00121897, 48.88061337, 0.01943055, 4.88806134, 0.07136917, -40.18630762, -0.00121897, -48.88061337, -0.01943055, -4.88806134, -0.07136917, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 40.18630762, 0.00121897, 48.88061337, 0.01943055, 4.88806134, 0.07136917, -40.18630762, -0.00121897, -48.88061337, -0.01943055, -4.88806134, -0.07136917, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 65.37270345, 0.0243793, 65.37270345, 0.0731379, 45.76089242, -1663.77341261, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 16.34317586, 7.283e-05, 49.02952759, 0.00021848, 163.43175863, 0.00072825, -16.34317586, -7.283e-05, -49.02952759, -0.00021848, -163.43175863, -0.00072825, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 65.37270345, 0.0243793, 65.37270345, 0.0731379, 45.76089242, -1663.77341261, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 16.34317586, 7.283e-05, 49.02952759, 0.00021848, 163.43175863, 0.00072825, -16.34317586, -7.283e-05, -49.02952759, -0.00021848, -163.43175863, -0.00072825, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.45, 11.55, 9.175)
    ops.node(124016, 13.45, 11.55, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 29679217.27517597, 12366340.53132332, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 39.08895707, 0.001173, 47.52690864, 0.01957176, 4.75269086, 0.0740864, -39.08895707, -0.001173, -47.52690864, -0.01957176, -4.75269086, -0.0740864, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 39.08895707, 0.001173, 47.52690864, 0.01957176, 4.75269086, 0.0740864, -39.08895707, -0.001173, -47.52690864, -0.01957176, -4.75269086, -0.0740864, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 64.81411116, 0.02345994, 64.81411116, 0.07037982, 45.36987781, -2280.48308238, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 16.20352779, 7.044e-05, 48.61058337, 0.00021132, 162.03527791, 0.00070441, -16.20352779, -7.044e-05, -48.61058337, -0.00021132, -162.03527791, -0.00070441, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 64.81411116, 0.02345994, 64.81411116, 0.07037982, 45.36987781, -2280.48308238, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 16.20352779, 7.044e-05, 48.61058337, 0.00021132, 162.03527791, 0.00070441, -16.20352779, -7.044e-05, -48.61058337, -0.00021132, -162.03527791, -0.00070441, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 15.4, 9.175)
    ops.node(124017, 0.0, 15.4, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 27817500.66166507, 11590625.27569378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 22.3957985, 0.00109014, 27.38319046, 0.01963525, 2.73831905, 0.08370719, -22.3957985, -0.00109014, -27.38319046, -0.01963525, -2.73831905, -0.08370719, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 22.3957985, 0.00109014, 27.38319046, 0.01963525, 2.73831905, 0.08370719, -22.3957985, -0.00109014, -27.38319046, -0.01963525, -2.73831905, -0.08370719, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 71.97837312, 0.02180277, 71.97837312, 0.0654083, 50.38486118, -4921.97961402, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 17.99459328, 8.346e-05, 53.98377984, 0.00025039, 179.94593279, 0.00083463, -17.99459328, -8.346e-05, -53.98377984, -0.00025039, -179.94593279, -0.00083463, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 71.97837312, 0.02180277, 71.97837312, 0.0654083, 50.38486118, -4921.97961402, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 17.99459328, 8.346e-05, 53.98377984, 0.00025039, 179.94593279, 0.00083463, -17.99459328, -8.346e-05, -53.98377984, -0.00025039, -179.94593279, -0.00083463, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.85, 15.4, 9.175)
    ops.node(124018, 2.85, 15.4, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 29866529.81731981, 12444387.42388326, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 39.42721738, 0.00118926, 47.88803262, 0.01955424, 4.78880326, 0.07325509, -39.42721738, -0.00118926, -47.88803262, -0.01955424, -4.78880326, -0.07325509, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 39.42721738, 0.00118926, 47.88803262, 0.01955424, 4.78880326, 0.07325509, -39.42721738, -0.00118926, -47.88803262, -0.01955424, -4.78880326, -0.07325509, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 67.57463516, 0.02378524, 67.57463516, 0.07135572, 47.30224461, -2005.33463116, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 16.89365879, 7.298e-05, 50.68097637, 0.00021894, 168.93658789, 0.00072981, -16.89365879, -7.298e-05, -50.68097637, -0.00021894, -168.93658789, -0.00072981, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 67.57463516, 0.02378524, 67.57463516, 0.07135572, 47.30224461, -2005.33463116, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 16.89365879, 7.298e-05, 50.68097637, 0.00021894, 168.93658789, 0.00072981, -16.89365879, -7.298e-05, -50.68097637, -0.00021894, -168.93658789, -0.00072981, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.15, 15.4, 9.175)
    ops.node(124019, 8.15, 15.4, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.0625, 29242134.9825918, 12184222.90941325, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 40.32320104, 0.00119471, 49.01440604, 0.02081795, 4.9014406, 0.07294354, -40.32320104, -0.00119471, -49.01440604, -0.02081795, -4.9014406, -0.07294354, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 40.32320104, 0.00119471, 49.01440604, 0.02081795, 4.9014406, 0.07294354, -40.32320104, -0.00119471, -49.01440604, -0.02081795, -4.9014406, -0.07294354, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 70.65610421, 0.02389427, 70.65610421, 0.0716828, 49.45927295, -1764.08111341, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 17.66402605, 7.794e-05, 52.99207816, 0.00023382, 176.64026052, 0.00077938, -17.66402605, -7.794e-05, -52.99207816, -0.00023382, -176.64026052, -0.00077938, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 70.65610421, 0.02389427, 70.65610421, 0.0716828, 49.45927295, -1764.08111341, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 17.66402605, 7.794e-05, 52.99207816, 0.00023382, 176.64026052, 0.00077938, -17.66402605, -7.794e-05, -52.99207816, -0.00023382, -176.64026052, -0.00077938, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 13.45, 15.4, 9.175)
    ops.node(124020, 13.45, 15.4, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 29487427.62516078, 12286428.17715032, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 38.39356352, 0.00122508, 46.70479955, 0.01965484, 4.67047996, 0.07409491, -38.39356352, -0.00122508, -46.70479955, -0.01965484, -4.67047996, -0.07409491, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 38.39356352, 0.00122508, 46.70479955, 0.01965484, 4.67047996, 0.07409491, -38.39356352, -0.00122508, -46.70479955, -0.01965484, -4.67047996, -0.07409491, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 65.0259616, 0.02450164, 65.0259616, 0.07350492, 45.51817312, -2305.55226052, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 16.2564904, 7.113e-05, 48.7694712, 0.00021339, 162.56490401, 0.00071131, -16.2564904, -7.113e-05, -48.7694712, -0.00021339, -162.56490401, -0.00071131, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 65.0259616, 0.02450164, 65.0259616, 0.07350492, 45.51817312, -2305.55226052, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 16.2564904, 7.113e-05, 48.7694712, 0.00021339, 162.56490401, 0.00071131, -16.2564904, -7.113e-05, -48.7694712, -0.00021339, -162.56490401, -0.00071131, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 19.25, 9.2)
    ops.node(124021, 0.0, 19.25, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 29304343.46012599, 12210143.10838583, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 21.76095275, 0.00108803, 26.52461457, 0.01983015, 2.65246146, 0.08546335, -21.76095275, -0.00108803, -26.52461457, -0.01983015, -2.65246146, -0.08546335, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 21.76095275, 0.00108803, 26.52461457, 0.01983015, 2.65246146, 0.08546335, -21.76095275, -0.00108803, -26.52461457, -0.01983015, -2.65246146, -0.08546335, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 75.44699751, 0.02176063, 75.44699751, 0.0652819, 52.81289826, -9189.91283287, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 18.86174938, 8.305e-05, 56.58524813, 0.00024914, 188.61749378, 0.00083046, -18.86174938, -8.305e-05, -56.58524813, -0.00024914, -188.61749378, -0.00083046, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 75.44699751, 0.02176063, 75.44699751, 0.0652819, 52.81289826, -9189.91283287, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 18.86174938, 8.305e-05, 56.58524813, 0.00024914, 188.61749378, 0.00083046, -18.86174938, -8.305e-05, -56.58524813, -0.00024914, -188.61749378, -0.00083046, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 2.85, 19.25, 9.2)
    ops.node(124022, 2.85, 19.25, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 29156999.72786552, 12148749.88661063, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 23.39391643, 0.00106627, 28.49805917, 0.0191378, 2.84980592, 0.0828347, -23.39391643, -0.00106627, -28.49805917, -0.0191378, -2.84980592, -0.0828347, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 23.39391643, 0.00106627, 28.49805917, 0.0191378, 2.84980592, 0.0828347, -23.39391643, -0.00106627, -28.49805917, -0.0191378, -2.84980592, -0.0828347, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 74.75046223, 0.02132544, 74.75046223, 0.06397632, 52.32532356, -3870.37108354, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 18.68761556, 8.27e-05, 56.06284668, 0.00024809, 186.87615559, 0.00082695, -18.68761556, -8.27e-05, -56.06284668, -0.00024809, -186.87615559, -0.00082695, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 74.75046223, 0.02132544, 74.75046223, 0.06397632, 52.32532356, -3870.37108354, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 18.68761556, 8.27e-05, 56.06284668, 0.00024809, 186.87615559, 0.00082695, -18.68761556, -8.27e-05, -56.06284668, -0.00024809, -186.87615559, -0.00082695, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 8.15, 19.25, 9.2)
    ops.node(124023, 8.15, 19.25, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.0625, 29607508.99708243, 12336462.08211768, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 38.31657529, 0.00123946, 46.60060448, 0.02029524, 4.66006045, 0.07492279, -38.31657529, -0.00123946, -46.60060448, -0.02029524, -4.66006045, -0.07492279, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 38.31657529, 0.00123946, 46.60060448, 0.02029524, 4.66006045, 0.07492279, -38.31657529, -0.00123946, -46.60060448, -0.02029524, -4.66006045, -0.07492279, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 71.58078157, 0.02478929, 71.58078157, 0.07436787, 50.1065471, -2617.9584578, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 17.89519539, 7.798e-05, 53.68558618, 0.00023395, 178.95195393, 0.00077984, -17.89519539, -7.798e-05, -53.68558618, -0.00023395, -178.95195393, -0.00077984, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 71.58078157, 0.02478929, 71.58078157, 0.07436787, 50.1065471, -2617.9584578, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 17.89519539, 7.798e-05, 53.68558618, 0.00023395, 178.95195393, 0.00077984, -17.89519539, -7.798e-05, -53.68558618, -0.00023395, -178.95195393, -0.00077984, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 13.45, 19.25, 9.2)
    ops.node(124024, 13.45, 19.25, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 31247713.66914677, 13019880.69547782, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 23.27742561, 0.00102092, 28.20019236, 0.01925049, 2.82001924, 0.08438061, -23.27742561, -0.00102092, -28.20019236, -0.01925049, -2.82001924, -0.08438061, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 23.27742561, 0.00102092, 28.20019236, 0.01925049, 2.82001924, 0.08438061, -23.27742561, -0.00102092, -28.20019236, -0.01925049, -2.82001924, -0.08438061, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 80.59905062, 0.02041849, 80.59905062, 0.06125546, 56.41933544, -5881.89425403, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 20.14976266, 8.32e-05, 60.44928797, 0.0002496, 201.49762655, 0.000832, -20.14976266, -8.32e-05, -60.44928797, -0.0002496, -201.49762655, -0.000832, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 80.59905062, 0.02041849, 80.59905062, 0.06125546, 56.41933544, -5881.89425403, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 20.14976266, 8.32e-05, 60.44928797, 0.0002496, 201.49762655, 0.000832, -20.14976266, -8.32e-05, -60.44928797, -0.0002496, -201.49762655, -0.000832, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124025, 0.0, 0.0, 1.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4063, 170001, 124025, 0.0625, 28440869.5059365, 11850362.29414021, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24063, 57.89920381, 0.00094019, 70.1120985, 0.02418386, 7.01120985, 0.08461472, -57.89920381, -0.00094019, -70.1120985, -0.02418386, -7.01120985, -0.08461472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14063, 54.08122051, 0.00094019, 65.48877377, 0.02418386, 6.54887738, 0.08461472, -54.08122051, -0.00094019, -65.48877377, -0.02418386, -6.54887738, -0.08461472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24063, 4063, 0.0, 92.58303187, 0.01880383, 92.58303187, 0.05641149, 64.80812231, -3378.75867618, 0.05, 2, 0, 70001, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 44063, 23.14575797, 6.281e-05, 69.4372739, 0.00018844, 231.45757966, 0.00062814, -23.14575797, -6.281e-05, -69.4372739, -0.00018844, -231.45757966, -0.00062814, 0.4, 0.3, 0.003, 0.0, 0.0, 24063, 2)
    ops.limitCurve('ThreePoint', 14063, 4063, 0.0, 92.58303187, 0.01880383, 92.58303187, 0.05641149, 64.80812231, -3378.75867618, 0.05, 2, 0, 70001, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 34063, 23.14575797, 6.281e-05, 69.4372739, 0.00018844, 231.45757966, 0.00062814, -23.14575797, -6.281e-05, -69.4372739, -0.00018844, -231.45757966, -0.00062814, 0.4, 0.3, 0.003, 0.0, 0.0, 14063, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4063, 99999, 'P', 44063, 'Vy', 34063, 'Vz', 24063, 'My', 14063, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4063, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 4063, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174025, 0.0, 0.0, 1.875)
    ops.node(121001, 0.0, 0.0, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4064, 174025, 121001, 0.0625, 29066461.71069028, 12111025.71278762, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24064, 40.8680641, 0.00088198, 49.51453077, 0.02393085, 4.95145308, 0.08844836, -40.8680641, -0.00088198, -49.51453077, -0.02393085, -4.95145308, -0.08844836, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14064, 37.23641362, 0.00088198, 45.11453108, 0.02393085, 4.51145311, 0.08844836, -37.23641362, -0.00088198, -45.11453108, -0.02393085, -4.51145311, -0.08844836, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24064, 4064, 0.0, 94.89863543, 0.01763958, 94.89863543, 0.05291873, 66.4290448, -3943.54834271, 0.05, 2, 0, 74025, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44064, 23.72465886, 6.3e-05, 71.17397657, 0.000189, 237.24658858, 0.00062999, -23.72465886, -6.3e-05, -71.17397657, -0.000189, -237.24658858, -0.00062999, 0.4, 0.3, 0.003, 0.0, 0.0, 24064, 2)
    ops.limitCurve('ThreePoint', 14064, 4064, 0.0, 94.89863543, 0.01763958, 94.89863543, 0.05291873, 66.4290448, -3943.54834271, 0.05, 2, 0, 74025, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34064, 23.72465886, 6.3e-05, 71.17397657, 0.000189, 237.24658858, 0.00062999, -23.72465886, -6.3e-05, -71.17397657, -0.000189, -237.24658858, -0.00062999, 0.4, 0.3, 0.003, 0.0, 0.0, 14064, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4064, 99999, 'P', 44064, 'Vy', 34064, 'Vz', 24064, 'My', 14064, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174025, 74025, 174025, 4064, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4064, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.85, 0.0, 0.0)
    ops.node(124026, 2.85, 0.0, 1.475)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4065, 170002, 124026, 0.1225, 28002062.98764221, 11667526.24485092, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24065, 155.41151964, 0.00078316, 188.24943685, 0.03232072, 18.82494369, 0.0889448, -155.41151964, -0.00078316, -188.24943685, -0.03232072, -18.82494369, -0.0889448, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14065, 155.41151964, 0.00078316, 188.24943685, 0.03232072, 18.82494369, 0.0889448, -155.41151964, -0.00078316, -188.24943685, -0.03232072, -18.82494369, -0.0889448, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24065, 4065, 0.0, 204.71187594, 0.01566313, 204.71187594, 0.0469894, 143.29831316, -6353.31603308, 0.05, 2, 0, 70002, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 44065, 51.17796899, 7.197e-05, 153.53390696, 0.00021592, 511.77968986, 0.00071972, -51.17796899, -7.197e-05, -153.53390696, -0.00021592, -511.77968986, -0.00071972, 0.4, 0.3, 0.003, 0.0, 0.0, 24065, 2)
    ops.limitCurve('ThreePoint', 14065, 4065, 0.0, 204.71187594, 0.01566313, 204.71187594, 0.0469894, 143.29831316, -6353.31603308, 0.05, 2, 0, 70002, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 34065, 51.17796899, 7.197e-05, 153.53390696, 0.00021592, 511.77968986, 0.00071972, -51.17796899, -7.197e-05, -153.53390696, -0.00021592, -511.77968986, -0.00071972, 0.4, 0.3, 0.003, 0.0, 0.0, 14065, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4065, 99999, 'P', 44065, 'Vy', 34065, 'Vz', 24065, 'My', 14065, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4065, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 4065, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174026, 2.85, 0.0, 1.875)
    ops.node(121002, 2.85, 0.0, 3.1)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4066, 174026, 121002, 0.1225, 30064246.19062177, 12526769.24609241, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24066, 102.28650679, 0.0007355, 123.56223691, 0.03017342, 12.35622369, 0.09192635, -102.28650679, -0.0007355, -123.56223691, -0.03017342, -12.35622369, -0.09192635, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14066, 96.37794903, 0.0007355, 116.42469123, 0.03017342, 11.64246912, 0.09192635, -96.37794903, -0.0007355, -116.42469123, -0.03017342, -11.64246912, -0.09192635, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24066, 4066, 0.0, 215.10608713, 0.01471006, 215.10608713, 0.04413019, 150.57426099, -6804.32850718, 0.05, 2, 0, 74026, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44066, 53.77652178, 7.044e-05, 161.32956535, 0.00021132, 537.76521782, 0.00070439, -53.77652178, -7.044e-05, -161.32956535, -0.00021132, -537.76521782, -0.00070439, 0.4, 0.3, 0.003, 0.0, 0.0, 24066, 2)
    ops.limitCurve('ThreePoint', 14066, 4066, 0.0, 215.10608713, 0.01471006, 215.10608713, 0.04413019, 150.57426099, -6804.32850718, 0.05, 2, 0, 74026, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34066, 53.77652178, 7.044e-05, 161.32956535, 0.00021132, 537.76521782, 0.00070439, -53.77652178, -7.044e-05, -161.32956535, -0.00021132, -537.76521782, -0.00070439, 0.4, 0.3, 0.003, 0.0, 0.0, 14066, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4066, 99999, 'P', 44066, 'Vy', 34066, 'Vz', 24066, 'My', 14066, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174026, 74026, 174026, 4066, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4066, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.6)
    ops.node(124027, 0.0, 0.0, 4.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4068, 171001, 124027, 0.0625, 29855066.03650594, 12439610.84854414, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24068, 30.25384006, 0.00080047, 36.62028196, 0.01780078, 3.6620282, 0.07366457, -30.25384006, -0.00080047, -36.62028196, -0.01780078, -3.6620282, -0.07366457, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14068, 30.25384006, 0.00080047, 36.62028196, 0.01780078, 3.6620282, 0.07366457, -30.25384006, -0.00080047, -36.62028196, -0.01780078, -3.6620282, -0.07366457, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24068, 4068, 0.0, 89.54100024, 0.01600939, 89.54100024, 0.04802816, 62.67870017, -3463.35526712, 0.05, 2, 0, 71001, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 44068, 22.38525006, 4.837e-05, 67.15575018, 0.00014511, 223.8525006, 0.00048371, -22.38525006, -4.837e-05, -67.15575018, -0.00014511, -223.8525006, -0.00048371, 0.4, 0.3, 0.003, 0.0, 0.0, 24068, 2)
    ops.limitCurve('ThreePoint', 14068, 4068, 0.0, 89.54100024, 0.01600939, 89.54100024, 0.04802816, 62.67870017, -3463.35526712, 0.05, 2, 0, 71001, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 34068, 22.38525006, 4.837e-05, 67.15575018, 0.00014511, 223.8525006, 0.00048371, -22.38525006, -4.837e-05, -67.15575018, -0.00014511, -223.8525006, -0.00048371, 0.4, 0.3, 0.003, 0.0, 0.0, 14068, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4068, 99999, 'P', 44068, 'Vy', 34068, 'Vz', 24068, 'My', 14068, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4068, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 4068, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174027, 0.0, 0.0, 4.925)
    ops.node(122001, 0.0, 0.0, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4069, 174027, 122001, 0.0625, 28802750.10365355, 12001145.87652231, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24069, 28.12860807, 0.00080409, 34.17419401, 0.01827576, 3.4174194, 0.07542433, -28.12860807, -0.00080409, -34.17419401, -0.01827576, -3.4174194, -0.07542433, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14069, 28.12860807, 0.00080409, 34.17419401, 0.01827576, 3.4174194, 0.07542433, -28.12860807, -0.00080409, -34.17419401, -0.01827576, -3.4174194, -0.07542433, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24069, 4069, 0.0, 84.771745, 0.01608182, 84.771745, 0.04824547, 59.3402215, -3813.51750879, 0.05, 2, 0, 74027, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44069, 21.19293625, 4.747e-05, 63.57880875, 0.0001424, 211.92936249, 0.00047468, -21.19293625, -4.747e-05, -63.57880875, -0.0001424, -211.92936249, -0.00047468, 0.4, 0.3, 0.003, 0.0, 0.0, 24069, 2)
    ops.limitCurve('ThreePoint', 14069, 4069, 0.0, 84.771745, 0.01608182, 84.771745, 0.04824547, 59.3402215, -3813.51750879, 0.05, 2, 0, 74027, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34069, 21.19293625, 4.747e-05, 63.57880875, 0.0001424, 211.92936249, 0.00047468, -21.19293625, -4.747e-05, -63.57880875, -0.0001424, -211.92936249, -0.00047468, 0.4, 0.3, 0.003, 0.0, 0.0, 14069, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4069, 99999, 'P', 44069, 'Vy', 34069, 'Vz', 24069, 'My', 14069, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174027, 74027, 174027, 4069, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4069, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.85, 0.0, 3.6)
    ops.node(124028, 2.85, 0.0, 4.575)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4070, 171002, 124028, 0.1225, 29308508.27293496, 12211878.44705623, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24070, 95.54506309, 0.00070795, 115.78173585, 0.02436668, 11.57817358, 0.0748022, -95.54506309, -0.00070795, -115.78173585, -0.02436668, -11.57817358, -0.0748022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14070, 89.8705763, 0.00070795, 108.90537918, 0.02436668, 10.89053792, 0.0748022, -89.8705763, -0.00070795, -108.90537918, -0.02436668, -10.89053792, -0.0748022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24070, 4070, 0.0, 198.55884841, 0.01415907, 198.55884841, 0.04247721, 138.99119389, -5616.06439252, 0.05, 2, 0, 71002, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 44070, 49.6397121, 5.575e-05, 148.91913631, 0.00016724, 496.39712103, 0.00055747, -49.6397121, -5.575e-05, -148.91913631, -0.00016724, -496.39712103, -0.00055747, 0.4, 0.3, 0.003, 0.0, 0.0, 24070, 2)
    ops.limitCurve('ThreePoint', 14070, 4070, 0.0, 198.55884841, 0.01415907, 198.55884841, 0.04247721, 138.99119389, -5616.06439252, 0.05, 2, 0, 71002, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 34070, 49.6397121, 5.575e-05, 148.91913631, 0.00016724, 496.39712103, 0.00055747, -49.6397121, -5.575e-05, -148.91913631, -0.00016724, -496.39712103, -0.00055747, 0.4, 0.3, 0.003, 0.0, 0.0, 14070, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4070, 99999, 'P', 44070, 'Vy', 34070, 'Vz', 24070, 'My', 14070, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4070, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 4070, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174028, 2.85, 0.0, 4.925)
    ops.node(122002, 2.85, 0.0, 5.9)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4071, 174028, 122002, 0.1225, 29822002.39648008, 12425834.3318667, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24071, 90.06932338, 0.00067444, 109.1048675, 0.03118533, 10.91048675, 0.09683356, -90.06932338, -0.00067444, -109.1048675, -0.03118533, -10.91048675, -0.09683356, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14071, 84.58947902, 0.00067444, 102.46689499, 0.03118533, 10.2466895, 0.09683356, -84.58947902, -0.00067444, -102.46689499, -0.03118533, -10.2466895, -0.09683356, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24071, 4071, 0.0, 223.44459746, 0.01348874, 223.44459746, 0.04046622, 156.41121822, -9020.68830371, 0.05, 2, 0, 74028, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44071, 55.86114936, 6.165e-05, 167.58344809, 0.00018496, 558.61149364, 0.00061653, -55.86114936, -6.165e-05, -167.58344809, -0.00018496, -558.61149364, -0.00061653, 0.4, 0.3, 0.003, 0.0, 0.0, 24071, 2)
    ops.limitCurve('ThreePoint', 14071, 4071, 0.0, 223.44459746, 0.01348874, 223.44459746, 0.04046622, 156.41121822, -9020.68830371, 0.05, 2, 0, 74028, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34071, 55.86114936, 6.165e-05, 167.58344809, 0.00018496, 558.61149364, 0.00061653, -55.86114936, -6.165e-05, -167.58344809, -0.00018496, -558.61149364, -0.00061653, 0.4, 0.3, 0.003, 0.0, 0.0, 14071, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4071, 99999, 'P', 44071, 'Vy', 34071, 'Vz', 24071, 'My', 14071, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174028, 74028, 174028, 4071, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4071, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 6.4)
    ops.node(124029, 0.0, 0.0, 7.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4073, 172001, 124029, 0.0625, 29864763.85110749, 12443651.60462812, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24073, 27.36135288, 0.0007718, 33.18509209, 0.01812462, 3.31850921, 0.07745264, -27.36135288, -0.0007718, -33.18509209, -0.01812462, -3.31850921, -0.07745264, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14073, 27.36135288, 0.0007718, 33.18509209, 0.01812462, 3.31850921, 0.07745264, -27.36135288, -0.0007718, -33.18509209, -0.01812462, -3.31850921, -0.07745264, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24073, 4073, 0.0, 86.14913327, 0.01543606, 86.14913327, 0.04630817, 60.30439329, -4146.21706466, 0.05, 2, 0, 72001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44073, 21.53728332, 4.652e-05, 64.61184995, 0.00013957, 215.37283316, 0.00046523, -21.53728332, -4.652e-05, -64.61184995, -0.00013957, -215.37283316, -0.00046523, 0.4, 0.3, 0.003, 0.0, 0.0, 24073, 2)
    ops.limitCurve('ThreePoint', 14073, 4073, 0.0, 86.14913327, 0.01543606, 86.14913327, 0.04630817, 60.30439329, -4146.21706466, 0.05, 2, 0, 72001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34073, 21.53728332, 4.652e-05, 64.61184995, 0.00013957, 215.37283316, 0.00046523, -21.53728332, -4.652e-05, -64.61184995, -0.00013957, -215.37283316, -0.00046523, 0.4, 0.3, 0.003, 0.0, 0.0, 14073, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4073, 99999, 'P', 44073, 'Vy', 34073, 'Vz', 24073, 'My', 14073, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4073, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4073, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 7.725)
    ops.node(123001, 0.0, 0.0, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 174029, 123001, 0.0625, 28663243.73848553, 11943018.22436897, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 24.8988412, 0.00079666, 30.33582284, 0.01848505, 3.03358228, 0.0799684, -24.8988412, -0.00079666, -30.33582284, -0.01848505, -3.03358228, -0.0799684, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 24.8988412, 0.00079666, 30.33582284, 0.01848505, 3.03358228, 0.0799684, -24.8988412, -0.00079666, -30.33582284, -0.01848505, -3.03358228, -0.0799684, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 80.32495355, 0.01593322, 80.32495355, 0.04779967, 56.22746748, -5445.1014154, 0.05, 2, 0, 74029, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 20.08123839, 4.52e-05, 60.24371516, 0.00013559, 200.81238386, 0.00045197, -20.08123839, -4.52e-05, -60.24371516, -0.00013559, -200.81238386, -0.00045197, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 80.32495355, 0.01593322, 80.32495355, 0.04779967, 56.22746748, -5445.1014154, 0.05, 2, 0, 74029, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 20.08123839, 4.52e-05, 60.24371516, 0.00013559, 200.81238386, 0.00045197, -20.08123839, -4.52e-05, -60.24371516, -0.00013559, -200.81238386, -0.00045197, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.85, 0.0, 6.4)
    ops.node(124030, 2.85, 0.0, 7.375)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 172002, 124030, 0.0625, 30559715.08953976, 12733214.62064156, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 45.97820516, 0.00087349, 55.48291973, 0.02687509, 5.54829197, 0.09202678, -45.97820516, -0.00087349, -55.48291973, -0.02687509, -5.54829197, -0.09202678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 45.97820516, 0.00087349, 55.48291973, 0.02687509, 5.54829197, 0.09202678, -45.97820516, -0.00087349, -55.48291973, -0.02687509, -5.54829197, -0.09202678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 102.49547388, 0.01746974, 102.49547388, 0.05240923, 71.74683172, -4175.38496648, 0.05, 2, 0, 72002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 25.62386847, 5.409e-05, 76.87160541, 0.00016228, 256.23868471, 0.00054092, -25.62386847, -5.409e-05, -76.87160541, -0.00016228, -256.23868471, -0.00054092, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 102.49547388, 0.01746974, 102.49547388, 0.05240923, 71.74683172, -4175.38496648, 0.05, 2, 0, 72002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 25.62386847, 5.409e-05, 76.87160541, 0.00016228, 256.23868471, 0.00054092, -25.62386847, -5.409e-05, -76.87160541, -0.00016228, -256.23868471, -0.00054092, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 2.85, 0.0, 7.725)
    ops.node(123002, 2.85, 0.0, 8.7)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 174030, 123002, 0.0625, 30179067.18952144, 12574611.32896727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 43.90112075, 0.00087266, 53.10177797, 0.02806837, 5.3101778, 0.09561033, -43.90112075, -0.00087266, -53.10177797, -0.02806837, -5.3101778, -0.09561033, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 43.90112075, 0.00087266, 53.10177797, 0.02806837, 5.3101778, 0.09561033, -43.90112075, -0.00087266, -53.10177797, -0.02806837, -5.3101778, -0.09561033, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 101.33111852, 0.01745328, 101.33111852, 0.05235983, 70.93178296, -4877.60707312, 0.05, 2, 0, 74030, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 25.33277963, 5.415e-05, 75.99833889, 0.00016246, 253.32779629, 0.00054152, -25.33277963, -5.415e-05, -75.99833889, -0.00016246, -253.32779629, -0.00054152, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 101.33111852, 0.01745328, 101.33111852, 0.05235983, 70.93178296, -4877.60707312, 0.05, 2, 0, 74030, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 25.33277963, 5.415e-05, 75.99833889, 0.00016246, 253.32779629, 0.00054152, -25.33277963, -5.415e-05, -75.99833889, -0.00016246, -253.32779629, -0.00054152, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 9.2)
    ops.node(124031, 0.0, 0.0, 10.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4078, 173001, 124031, 0.0625, 28529746.39561564, 11887394.33150652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24078, 24.05676316, 0.00076356, 29.34339133, 0.01927183, 2.93433913, 0.08222289, -24.05676316, -0.00076356, -29.34339133, -0.01927183, -2.93433913, -0.08222289, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14078, 24.05676316, 0.00076356, 29.34339133, 0.01927183, 2.93433913, 0.08222289, -24.05676316, -0.00076356, -29.34339133, -0.01927183, -2.93433913, -0.08222289, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24078, 4078, 0.0, 80.7095054, 0.01527114, 80.7095054, 0.04581342, 56.49665378, -7559.2602392, 0.05, 2, 0, 73001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44078, 20.17737635, 4.563e-05, 60.53212905, 0.00013688, 201.7737635, 0.00045625, -20.17737635, -4.563e-05, -60.53212905, -0.00013688, -201.7737635, -0.00045625, 0.4, 0.3, 0.003, 0.0, 0.0, 24078, 2)
    ops.limitCurve('ThreePoint', 14078, 4078, 0.0, 80.7095054, 0.01527114, 80.7095054, 0.04581342, 56.49665378, -7559.2602392, 0.05, 2, 0, 73001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34078, 20.17737635, 4.563e-05, 60.53212905, 0.00013688, 201.7737635, 0.00045625, -20.17737635, -4.563e-05, -60.53212905, -0.00013688, -201.7737635, -0.00045625, 0.4, 0.3, 0.003, 0.0, 0.0, 14078, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4078, 99999, 'P', 44078, 'Vy', 34078, 'Vz', 24078, 'My', 14078, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4078, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4078, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 10.525)
    ops.node(124001, 0.0, 0.0, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 174031, 124001, 0.0625, 30502924.87761529, 12709552.03233971, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 21.71005153, 0.00074468, 26.382314, 0.018984, 2.6382314, 0.08554034, -21.71005153, -0.00074468, -26.382314, -0.018984, -2.6382314, -0.08554034, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 21.71005153, 0.00074468, 26.382314, 0.018984, 2.6382314, 0.08554034, -21.71005153, -0.00074468, -26.382314, -0.018984, -2.6382314, -0.08554034, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 80.91832855, 0.01489353, 80.91832855, 0.04468058, 56.64282999, -49371.18240909, 0.05, 2, 0, 74031, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 20.22958214, 4.278e-05, 60.68874642, 0.00012835, 202.29582139, 0.00042784, -20.22958214, -4.278e-05, -60.68874642, -0.00012835, -202.29582139, -0.00042784, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 80.91832855, 0.01489353, 80.91832855, 0.04468058, 56.64282999, -49371.18240909, 0.05, 2, 0, 74031, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 20.22958214, 4.278e-05, 60.68874642, 0.00012835, 202.29582139, 0.00042784, -20.22958214, -4.278e-05, -60.68874642, -0.00012835, -202.29582139, -0.00042784, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.85, 0.0, 9.2)
    ops.node(124032, 2.85, 0.0, 10.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 173002, 124032, 0.0625, 30093328.57870268, 12538886.90779278, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 39.30621378, 0.0008553, 47.70852612, 0.01952004, 4.77085261, 0.07319766, -39.30621378, -0.0008553, -47.70852612, -0.01952004, -4.77085261, -0.07319766, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 39.30621378, 0.0008553, 47.70852612, 0.01952004, 4.77085261, 0.07319766, -39.30621378, -0.0008553, -47.70852612, -0.01952004, -4.77085261, -0.07319766, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 76.34241733, 0.01710603, 76.34241733, 0.05131809, 53.43969213, -3989.17159409, 0.05, 2, 0, 73002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 19.08560433, 4.091e-05, 57.256813, 0.00012274, 190.85604333, 0.00040914, -19.08560433, -4.091e-05, -57.256813, -0.00012274, -190.85604333, -0.00040914, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 76.34241733, 0.01710603, 76.34241733, 0.05131809, 53.43969213, -3989.17159409, 0.05, 2, 0, 73002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 19.08560433, 4.091e-05, 57.256813, 0.00012274, 190.85604333, 0.00040914, -19.08560433, -4.091e-05, -57.256813, -0.00012274, -190.85604333, -0.00040914, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 2.85, 0.0, 10.525)
    ops.node(124002, 2.85, 0.0, 11.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 174032, 124002, 0.0625, 30243504.65360117, 12601460.27233382, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 37.96738824, 0.00082307, 46.13389522, 0.01964539, 4.61338952, 0.07584651, -37.96738824, -0.00082307, -46.13389522, -0.01964539, -4.61338952, -0.07584651, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 37.96738824, 0.00082307, 46.13389522, 0.01964539, 4.61338952, 0.07584651, -37.96738824, -0.00082307, -46.13389522, -0.01964539, -4.61338952, -0.07584651, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 72.41565518, 0.01646131, 72.41565518, 0.04938392, 50.69095862, -7577.33995335, 0.05, 2, 0, 74032, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 18.10391379, 3.862e-05, 54.31174138, 0.00011585, 181.03913795, 0.00038617, -18.10391379, -3.862e-05, -54.31174138, -0.00011585, -181.03913795, -0.00038617, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 72.41565518, 0.01646131, 72.41565518, 0.04938392, 50.69095862, -7577.33995335, 0.05, 2, 0, 74032, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 18.10391379, 3.862e-05, 54.31174138, 0.00011585, 181.03913795, 0.00038617, -18.10391379, -3.862e-05, -54.31174138, -0.00011585, -181.03913795, -0.00038617, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
