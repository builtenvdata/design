import openseespy.opensees as ops


def add_columns() -> None:
    """Add components of all columns to ops domain (plastic hinges, column elements and nodes)
    """
    # Create elastic column element nodes
    ops.node(170003, 8.3, 0.0, 0.0)
    ops.node(121003, 8.3, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3, 170003, 121003, 0.1225, 27822730.79933828, 11592804.49972428, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20003, 130.94424459, 0.00111151, 158.41279637, 0.01623163, 15.84127964, 0.05229328, -130.94424459, -0.00111151, -158.41279637, -0.01623163, -15.84127964, -0.05229328, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10003, 142.76355542, 0.00111151, 172.71147811, 0.01623163, 17.27114781, 0.05229328, -142.76355542, -0.00111151, -172.71147811, -0.01623163, -17.27114781, -0.05229328, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20003, 3, 0.0, 139.02288553, 0.02223012, 139.02288553, 0.06669036, 97.31601987, -1478.49709355, 0.05, 2, 0, 70003, 21003, 2, 3)
    ops.uniaxialMaterial('LimitState', 40003, 34.75572138, 0.00010866, 104.26716415, 0.00032599, 347.55721383, 0.00108664, -34.75572138, -0.00010866, -104.26716415, -0.00032599, -347.55721383, -0.00108664, 0.4, 0.3, 0.003, 0.0, 0.0, 20003, 2)
    ops.limitCurve('ThreePoint', 10003, 3, 0.0, 139.02288553, 0.02223012, 139.02288553, 0.06669036, 97.31601987, -1478.49709355, 0.05, 2, 0, 70003, 21003, 1, 3)
    ops.uniaxialMaterial('LimitState', 30003, 34.75572138, 0.00010866, 104.26716415, 0.00032599, 347.55721383, 0.00108664, -34.75572138, -0.00010866, -104.26716415, -0.00032599, -347.55721383, -0.00108664, 0.4, 0.3, 0.003, 0.0, 0.0, 10003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3, 99999, 'P', 40003, 'Vy', 30003, 'Vz', 20003, 'My', 10003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170003, 70003, 170003, 3, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121003, 121003, 21003, 3, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170004, 13.65, 0.0, 0.0)
    ops.node(121004, 13.65, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4, 170004, 121004, 0.09, 29604556.89257659, 12335232.03857358, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20004, 72.26104155, 0.00123464, 87.37536614, 0.01770408, 8.73753661, 0.06364307, -72.26104155, -0.00123464, -87.37536614, -0.01770408, -8.73753661, -0.06364307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10004, 76.75910656, 0.00123464, 92.81425919, 0.01770408, 9.28142592, 0.06364307, -76.75910656, -0.00123464, -92.81425919, -0.01770408, -9.28142592, -0.06364307, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20004, 4, 0.0, 113.21353104, 0.02469286, 113.21353104, 0.07407859, 79.24947173, -1405.95680959, 0.05, 2, 0, 70004, 21004, 2, 3)
    ops.uniaxialMaterial('LimitState', 40004, 28.30338276, 0.0001132, 84.91014828, 0.00033959, 283.03382759, 0.00113196, -28.30338276, -0.0001132, -84.91014828, -0.00033959, -283.03382759, -0.00113196, 0.4, 0.3, 0.003, 0.0, 0.0, 20004, 2)
    ops.limitCurve('ThreePoint', 10004, 4, 0.0, 113.21353104, 0.02469286, 113.21353104, 0.07407859, 79.24947173, -1405.95680959, 0.05, 2, 0, 70004, 21004, 1, 3)
    ops.uniaxialMaterial('LimitState', 30004, 28.30338276, 0.0001132, 84.91014828, 0.00033959, 283.03382759, 0.00113196, -28.30338276, -0.0001132, -84.91014828, -0.00033959, -283.03382759, -0.00113196, 0.4, 0.3, 0.003, 0.0, 0.0, 10004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4, 99999, 'P', 40004, 'Vy', 30004, 'Vz', 20004, 'My', 10004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170004, 70004, 170004, 4, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121004, 121004, 21004, 4, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170005, 0.0, 4.25, 0.0)
    ops.node(121005, 0.0, 4.25, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 5, 170005, 121005, 0.09, 29350185.11536952, 12229243.79807063, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20005, 82.51646185, 0.00123651, 99.63596539, 0.01751476, 9.96359654, 0.06063753, -82.51646185, -0.00123651, -99.63596539, -0.01751476, -9.96359654, -0.06063753, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10005, 92.02659118, 0.00123651, 111.11913973, 0.01751476, 11.11191397, 0.06063753, -92.02659118, -0.00123651, -111.11913973, -0.01751476, -11.11191397, -0.06063753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20005, 5, 0.0, 114.30585556, 0.02473018, 114.30585556, 0.07419053, 80.01409889, -1316.71555867, 0.05, 2, 0, 70005, 21005, 2, 3)
    ops.uniaxialMaterial('LimitState', 40005, 28.57646389, 0.00011528, 85.72939167, 0.00034584, 285.7646389, 0.00115279, -28.57646389, -0.00011528, -85.72939167, -0.00034584, -285.7646389, -0.00115279, 0.4, 0.3, 0.003, 0.0, 0.0, 20005, 2)
    ops.limitCurve('ThreePoint', 10005, 5, 0.0, 114.30585556, 0.02473018, 114.30585556, 0.07419053, 80.01409889, -1316.71555867, 0.05, 2, 0, 70005, 21005, 1, 3)
    ops.uniaxialMaterial('LimitState', 30005, 28.57646389, 0.00011528, 85.72939167, 0.00034584, 285.7646389, 0.00115279, -28.57646389, -0.00011528, -85.72939167, -0.00034584, -285.7646389, -0.00115279, 0.4, 0.3, 0.003, 0.0, 0.0, 10005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 5, 99999, 'P', 40005, 'Vy', 30005, 'Vz', 20005, 'My', 10005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170005, 70005, 170005, 5, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121005, 121005, 21005, 5, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170006, 2.95, 4.25, 0.0)
    ops.node(121006, 2.95, 4.25, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 6, 170006, 121006, 0.1225, 29316645.48374938, 12215268.95156224, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20006, 160.52575947, 0.0011327, 193.41793664, 0.02034293, 19.34179366, 0.05629224, -160.52575947, -0.0011327, -193.41793664, -0.02034293, -19.34179366, -0.05629224, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10006, 173.06965421, 0.0011327, 208.5321105, 0.02034293, 20.85321105, 0.05629224, -173.06965421, -0.0011327, -208.5321105, -0.02034293, -20.85321105, -0.05629224, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20006, 6, 0.0, 151.97562156, 0.02265401, 151.97562156, 0.06796203, 106.38293509, -1563.89835329, 0.05, 2, 0, 70006, 21006, 2, 3)
    ops.uniaxialMaterial('LimitState', 40006, 37.99390539, 0.00011273, 113.98171617, 0.0003382, 379.9390539, 0.00112735, -37.99390539, -0.00011273, -113.98171617, -0.0003382, -379.9390539, -0.00112735, 0.4, 0.3, 0.003, 0.0, 0.0, 20006, 2)
    ops.limitCurve('ThreePoint', 10006, 6, 0.0, 151.97562156, 0.02265401, 151.97562156, 0.06796203, 106.38293509, -1563.89835329, 0.05, 2, 0, 70006, 21006, 1, 3)
    ops.uniaxialMaterial('LimitState', 30006, 37.99390539, 0.00011273, 113.98171617, 0.0003382, 379.9390539, 0.00112735, -37.99390539, -0.00011273, -113.98171617, -0.0003382, -379.9390539, -0.00112735, 0.4, 0.3, 0.003, 0.0, 0.0, 10006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 6, 99999, 'P', 40006, 'Vy', 30006, 'Vz', 20006, 'My', 10006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170006, 70006, 170006, 6, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121006, 121006, 21006, 6, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170007, 8.3, 4.25, 0.0)
    ops.node(121007, 8.3, 4.25, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 7, 170007, 121007, 0.16, 29108038.54940441, 12128349.39558517, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20007, 240.27135882, 0.0010457, 290.08057249, 0.02671093, 29.00805725, 0.06679414, -240.27135882, -0.0010457, -290.08057249, -0.02671093, -29.00805725, -0.06679414, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10007, 267.53145779, 0.0010457, 322.99179901, 0.02671093, 32.2991799, 0.06679414, -267.53145779, -0.0010457, -322.99179901, -0.02671093, -32.2991799, -0.06679414, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20007, 7, 0.0, 195.31201247, 0.0209139, 195.31201247, 0.0627417, 136.71840873, -2103.09971439, 0.05, 2, 0, 70007, 21007, 2, 3)
    ops.uniaxialMaterial('LimitState', 40007, 48.82800312, 0.00011172, 146.48400935, 0.00033516, 488.28003118, 0.0011172, -48.82800312, -0.00011172, -146.48400935, -0.00033516, -488.28003118, -0.0011172, 0.4, 0.3, 0.003, 0.0, 0.0, 20007, 2)
    ops.limitCurve('ThreePoint', 10007, 7, 0.0, 195.31201247, 0.0209139, 195.31201247, 0.0627417, 136.71840873, -2103.09971439, 0.05, 2, 0, 70007, 21007, 1, 3)
    ops.uniaxialMaterial('LimitState', 30007, 48.82800312, 0.00011172, 146.48400935, 0.00033516, 488.28003118, 0.0011172, -48.82800312, -0.00011172, -146.48400935, -0.00033516, -488.28003118, -0.0011172, 0.4, 0.3, 0.003, 0.0, 0.0, 10007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 7, 99999, 'P', 40007, 'Vy', 30007, 'Vz', 20007, 'My', 10007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170007, 70007, 170007, 7, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121007, 121007, 21007, 7, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170008, 13.65, 4.25, 0.0)
    ops.node(121008, 13.65, 4.25, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 8, 170008, 121008, 0.1225, 28772788.93017679, 11988662.05424033, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20008, 147.43974126, 0.00109395, 178.26131173, 0.01693316, 17.82613117, 0.05502955, -147.43974126, -0.00109395, -178.26131173, -0.01693316, -17.82613117, -0.05502955, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10008, 153.90940895, 0.00109395, 186.08343241, 0.01693316, 18.60834324, 0.05502955, -153.90940895, -0.00109395, -186.08343241, -0.01693316, -18.60834324, -0.05502955, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20008, 8, 0.0, 142.59871897, 0.02187905, 142.59871897, 0.06563715, 99.81910328, -1514.21294412, 0.05, 2, 0, 70008, 21008, 2, 3)
    ops.uniaxialMaterial('LimitState', 40008, 35.64967974, 0.00010778, 106.94903923, 0.00032334, 356.49679743, 0.00107778, -35.64967974, -0.00010778, -106.94903923, -0.00032334, -356.49679743, -0.00107778, 0.4, 0.3, 0.003, 0.0, 0.0, 20008, 2)
    ops.limitCurve('ThreePoint', 10008, 8, 0.0, 142.59871897, 0.02187905, 142.59871897, 0.06563715, 99.81910328, -1514.21294412, 0.05, 2, 0, 70008, 21008, 1, 3)
    ops.uniaxialMaterial('LimitState', 30008, 35.64967974, 0.00010778, 106.94903923, 0.00032334, 356.49679743, 0.00107778, -35.64967974, -0.00010778, -106.94903923, -0.00032334, -356.49679743, -0.00107778, 0.4, 0.3, 0.003, 0.0, 0.0, 10008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 8, 99999, 'P', 40008, 'Vy', 30008, 'Vz', 20008, 'My', 10008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170008, 70008, 170008, 8, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121008, 121008, 21008, 8, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170009, 0.0, 8.5, 0.0)
    ops.node(121009, 0.0, 8.5, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 9, 170009, 121009, 0.09, 29763744.8946366, 12401560.37276525, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20009, 72.25088595, 0.00122188, 87.31333883, 0.01765401, 8.73133388, 0.06343991, -72.25088595, -0.00122188, -87.31333883, -0.01765401, -8.73133388, -0.06343991, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10009, 76.71433792, 0.00122188, 92.70730583, 0.01765401, 9.27073058, 0.06343991, -76.71433792, -0.00122188, -92.70730583, -0.01765401, -9.27073058, -0.06343991, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20009, 9, 0.0, 112.62456946, 0.02443761, 112.62456946, 0.07331284, 78.83719862, -1348.53066326, 0.05, 2, 0, 70009, 21009, 2, 3)
    ops.uniaxialMaterial('LimitState', 40009, 28.15614237, 0.000112, 84.4684271, 0.00033601, 281.56142366, 0.00112005, -28.15614237, -0.000112, -84.4684271, -0.00033601, -281.56142366, -0.00112005, 0.4, 0.3, 0.003, 0.0, 0.0, 20009, 2)
    ops.limitCurve('ThreePoint', 10009, 9, 0.0, 112.62456946, 0.02443761, 112.62456946, 0.07331284, 78.83719862, -1348.53066326, 0.05, 2, 0, 70009, 21009, 1, 3)
    ops.uniaxialMaterial('LimitState', 30009, 28.15614237, 0.000112, 84.4684271, 0.00033601, 281.56142366, 0.00112005, -28.15614237, -0.000112, -84.4684271, -0.00033601, -281.56142366, -0.00112005, 0.4, 0.3, 0.003, 0.0, 0.0, 10009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 9, 99999, 'P', 40009, 'Vy', 30009, 'Vz', 20009, 'My', 10009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170009, 70009, 170009, 9, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121009, 121009, 21009, 9, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170010, 2.95, 8.5, 0.0)
    ops.node(121010, 2.95, 8.5, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 10, 170010, 121010, 0.1225, 29032683.72199382, 12096951.55083076, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20010, 156.93343409, 0.00116485, 189.47558997, 0.02023146, 18.947559, 0.05755177, -156.93343409, -0.00116485, -189.47558997, -0.02023146, -18.947559, -0.05755177, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10010, 169.22241473, 0.00116485, 204.31284802, 0.02023146, 20.4312848, 0.05755177, -169.22241473, -0.00116485, -204.31284802, -0.02023146, -20.4312848, -0.05755177, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20010, 10, 0.0, 144.81952161, 0.02329695, 144.81952161, 0.06989086, 101.37366513, -1489.27496979, 0.05, 2, 0, 70010, 21010, 2, 3)
    ops.uniaxialMaterial('LimitState', 40010, 36.2048804, 0.00010848, 108.61464121, 0.00032543, 362.04880402, 0.00108477, -36.2048804, -0.00010848, -108.61464121, -0.00032543, -362.04880402, -0.00108477, 0.4, 0.3, 0.003, 0.0, 0.0, 20010, 2)
    ops.limitCurve('ThreePoint', 10010, 10, 0.0, 144.81952161, 0.02329695, 144.81952161, 0.06989086, 101.37366513, -1489.27496979, 0.05, 2, 0, 70010, 21010, 1, 3)
    ops.uniaxialMaterial('LimitState', 30010, 36.2048804, 0.00010848, 108.61464121, 0.00032543, 362.04880402, 0.00108477, -36.2048804, -0.00010848, -108.61464121, -0.00032543, -362.04880402, -0.00108477, 0.4, 0.3, 0.003, 0.0, 0.0, 10010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 10, 99999, 'P', 40010, 'Vy', 30010, 'Vz', 20010, 'My', 10010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170010, 70010, 170010, 10, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121010, 121010, 21010, 10, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170011, 8.3, 8.5, 0.0)
    ops.node(121011, 8.3, 8.5, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 11, 170011, 121011, 0.16, 28948284.03663175, 12061785.01526323, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20011, 256.96154125, 0.00104973, 310.30406132, 0.02779804, 31.03040613, 0.06764363, -256.96154125, -0.00104973, -310.30406132, -0.02779804, -31.03040613, -0.06764363, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10011, 278.22347548, 0.00104973, 335.97975002, 0.02779804, 33.597975, 0.06764363, -278.22347548, -0.00104973, -335.97975002, -0.02779804, -33.597975, -0.06764363, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20011, 11, 0.0, 195.21722523, 0.02099466, 195.21722523, 0.06298398, 136.65205766, -2121.56040574, 0.05, 2, 0, 70011, 21011, 2, 3)
    ops.uniaxialMaterial('LimitState', 40011, 48.80430631, 0.00011228, 146.41291892, 0.00033685, 488.04306308, 0.00112282, -48.80430631, -0.00011228, -146.41291892, -0.00033685, -488.04306308, -0.00112282, 0.4, 0.3, 0.003, 0.0, 0.0, 20011, 2)
    ops.limitCurve('ThreePoint', 10011, 11, 0.0, 195.21722523, 0.02099466, 195.21722523, 0.06298398, 136.65205766, -2121.56040574, 0.05, 2, 0, 70011, 21011, 1, 3)
    ops.uniaxialMaterial('LimitState', 30011, 48.80430631, 0.00011228, 146.41291892, 0.00033685, 488.04306308, 0.00112282, -48.80430631, -0.00011228, -146.41291892, -0.00033685, -488.04306308, -0.00112282, 0.4, 0.3, 0.003, 0.0, 0.0, 10011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 11, 99999, 'P', 40011, 'Vy', 30011, 'Vz', 20011, 'My', 10011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170011, 70011, 170011, 11, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121011, 121011, 21011, 11, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170012, 13.65, 8.5, 0.0)
    ops.node(121012, 13.65, 8.5, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 12, 170012, 121012, 0.1225, 29768114.55131588, 12403381.06304828, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20012, 143.37531908, 0.00110962, 173.05764362, 0.01694576, 17.30576436, 0.05630904, -143.37531908, -0.00110962, -173.05764362, -0.01694576, -17.30576436, -0.05630904, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10012, 149.14575382, 0.00110962, 180.02270459, 0.01694576, 18.00227046, 0.05630904, -149.14575382, -0.00110962, -180.02270459, -0.01694576, -18.00227046, -0.05630904, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20012, 12, 0.0, 146.21912983, 0.0221924, 146.21912983, 0.06657719, 102.35339088, -1512.02539642, 0.05, 2, 0, 70012, 21012, 2, 3)
    ops.uniaxialMaterial('LimitState', 40012, 36.55478246, 0.00010682, 109.66434737, 0.00032046, 365.54782457, 0.0010682, -36.55478246, -0.00010682, -109.66434737, -0.00032046, -365.54782457, -0.0010682, 0.4, 0.3, 0.003, 0.0, 0.0, 20012, 2)
    ops.limitCurve('ThreePoint', 10012, 12, 0.0, 146.21912983, 0.0221924, 146.21912983, 0.06657719, 102.35339088, -1512.02539642, 0.05, 2, 0, 70012, 21012, 1, 3)
    ops.uniaxialMaterial('LimitState', 30012, 36.55478246, 0.00010682, 109.66434737, 0.00032046, 365.54782457, 0.0010682, -36.55478246, -0.00010682, -109.66434737, -0.00032046, -365.54782457, -0.0010682, 0.4, 0.3, 0.003, 0.0, 0.0, 10012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 12, 99999, 'P', 40012, 'Vy', 30012, 'Vz', 20012, 'My', 10012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170012, 70012, 170012, 12, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121012, 121012, 21012, 12, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170013, 0.0, 12.75, 0.0)
    ops.node(121013, 0.0, 12.75, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 13, 170013, 121013, 0.09, 29558680.10729924, 12316116.71137469, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20013, 73.0002368, 0.00120532, 88.25446629, 0.01768294, 8.82544663, 0.0632164, -73.0002368, -0.00120532, -88.25446629, -0.01768294, -8.82544663, -0.0632164, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10013, 77.72329403, 0.00120532, 93.96446003, 0.01768294, 9.396446, 0.0632164, -77.72329403, -0.00120532, -93.96446003, -0.01768294, -9.396446, -0.0632164, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20013, 13, 0.0, 112.8887728, 0.02410641, 112.8887728, 0.07231924, 79.02214096, -1375.27766747, 0.05, 2, 0, 70013, 21013, 2, 3)
    ops.uniaxialMaterial('LimitState', 40013, 28.2221932, 0.00011305, 84.6665796, 0.00033914, 282.221932, 0.00113047, -28.2221932, -0.00011305, -84.6665796, -0.00033914, -282.221932, -0.00113047, 0.4, 0.3, 0.003, 0.0, 0.0, 20013, 2)
    ops.limitCurve('ThreePoint', 10013, 13, 0.0, 112.8887728, 0.02410641, 112.8887728, 0.07231924, 79.02214096, -1375.27766747, 0.05, 2, 0, 70013, 21013, 1, 3)
    ops.uniaxialMaterial('LimitState', 30013, 28.2221932, 0.00011305, 84.6665796, 0.00033914, 282.221932, 0.00113047, -28.2221932, -0.00011305, -84.6665796, -0.00033914, -282.221932, -0.00113047, 0.4, 0.3, 0.003, 0.0, 0.0, 10013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 13, 99999, 'P', 40013, 'Vy', 30013, 'Vz', 20013, 'My', 10013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170013, 70013, 170013, 13, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121013, 121013, 21013, 13, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170014, 2.95, 12.75, 0.0)
    ops.node(121014, 2.95, 12.75, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 14, 170014, 121014, 0.1225, 28532222.42798179, 11888426.01165908, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20014, 169.62027299, 0.00113776, 204.93385282, 0.02110654, 20.49338528, 0.05770822, -169.62027299, -0.00113776, -204.93385282, -0.02110654, -20.49338528, -0.05770822, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10014, 176.00427432, 0.00113776, 212.646952, 0.02110654, 21.2646952, 0.05770822, -176.00427432, -0.00113776, -212.646952, -0.02110654, -21.2646952, -0.05770822, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20014, 14, 0.0, 144.62177912, 0.02275513, 144.62177912, 0.06826538, 101.23524538, -1532.51765256, 0.05, 2, 0, 70014, 21014, 2, 3)
    ops.uniaxialMaterial('LimitState', 40014, 36.15544478, 0.00011023, 108.46633434, 0.00033069, 361.5544478, 0.00110229, -36.15544478, -0.00011023, -108.46633434, -0.00033069, -361.5544478, -0.00110229, 0.4, 0.3, 0.003, 0.0, 0.0, 20014, 2)
    ops.limitCurve('ThreePoint', 10014, 14, 0.0, 144.62177912, 0.02275513, 144.62177912, 0.06826538, 101.23524538, -1532.51765256, 0.05, 2, 0, 70014, 21014, 1, 3)
    ops.uniaxialMaterial('LimitState', 30014, 36.15544478, 0.00011023, 108.46633434, 0.00033069, 361.5544478, 0.00110229, -36.15544478, -0.00011023, -108.46633434, -0.00033069, -361.5544478, -0.00110229, 0.4, 0.3, 0.003, 0.0, 0.0, 10014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 14, 99999, 'P', 40014, 'Vy', 30014, 'Vz', 20014, 'My', 10014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170014, 70014, 170014, 14, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121014, 121014, 21014, 14, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170015, 8.3, 12.75, 0.0)
    ops.node(121015, 8.3, 12.75, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 15, 170015, 121015, 0.16, 29524053.25041422, 12301688.85433926, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20015, 268.59085499, 0.00106941, 324.05560706, 0.02772413, 32.40556071, 0.06840648, -268.59085499, -0.00106941, -324.05560706, -0.02772413, -32.40556071, -0.06840648, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10015, 281.95441868, 0.00106941, 340.17878349, 0.02772413, 34.01787835, 0.06840648, -281.95441868, -0.00106941, -340.17878349, -0.02772413, -34.01787835, -0.06840648, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20015, 15, 0.0, 201.63198187, 0.02138826, 201.63198187, 0.06416479, 141.14238731, -2220.35097336, 0.05, 2, 0, 70015, 21015, 2, 3)
    ops.uniaxialMaterial('LimitState', 40015, 50.40799547, 0.00011371, 151.2239864, 0.00034113, 504.07995468, 0.0011371, -50.40799547, -0.00011371, -151.2239864, -0.00034113, -504.07995468, -0.0011371, 0.4, 0.3, 0.003, 0.0, 0.0, 20015, 2)
    ops.limitCurve('ThreePoint', 10015, 15, 0.0, 201.63198187, 0.02138826, 201.63198187, 0.06416479, 141.14238731, -2220.35097336, 0.05, 2, 0, 70015, 21015, 1, 3)
    ops.uniaxialMaterial('LimitState', 30015, 50.40799547, 0.00011371, 151.2239864, 0.00034113, 504.07995468, 0.0011371, -50.40799547, -0.00011371, -151.2239864, -0.00034113, -504.07995468, -0.0011371, 0.4, 0.3, 0.003, 0.0, 0.0, 10015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 15, 99999, 'P', 40015, 'Vy', 30015, 'Vz', 20015, 'My', 10015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170015, 70015, 170015, 15, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121015, 121015, 21015, 15, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170016, 13.65, 12.75, 0.0)
    ops.node(121016, 13.65, 12.75, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 16, 170016, 121016, 0.1225, 28709464.04057002, 11962276.68357084, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20016, 145.82191719, 0.00109515, 176.3217473, 0.01641322, 17.63217473, 0.05442398, -145.82191719, -0.00109515, -176.3217473, -0.01641322, -17.63217473, -0.05442398, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10016, 152.11741239, 0.00109515, 183.9339961, 0.01641322, 18.39339961, 0.05442398, -152.11741239, -0.00109515, -183.9339961, -0.01641322, -18.39339961, -0.05442398, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20016, 16, 0.0, 139.90516431, 0.02190297, 139.90516431, 0.06570891, 97.93361501, -1447.61796444, 0.05, 2, 0, 70016, 21016, 2, 3)
    ops.uniaxialMaterial('LimitState', 40016, 34.97629108, 0.00010598, 104.92887323, 0.00031793, 349.76291076, 0.00105976, -34.97629108, -0.00010598, -104.92887323, -0.00031793, -349.76291076, -0.00105976, 0.4, 0.3, 0.003, 0.0, 0.0, 20016, 2)
    ops.limitCurve('ThreePoint', 10016, 16, 0.0, 139.90516431, 0.02190297, 139.90516431, 0.06570891, 97.93361501, -1447.61796444, 0.05, 2, 0, 70016, 21016, 1, 3)
    ops.uniaxialMaterial('LimitState', 30016, 34.97629108, 0.00010598, 104.92887323, 0.00031793, 349.76291076, 0.00105976, -34.97629108, -0.00010598, -104.92887323, -0.00031793, -349.76291076, -0.00105976, 0.4, 0.3, 0.003, 0.0, 0.0, 10016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 16, 99999, 'P', 40016, 'Vy', 30016, 'Vz', 20016, 'My', 10016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170016, 70016, 170016, 16, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121016, 121016, 21016, 16, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170017, 0.0, 17.0, 0.0)
    ops.node(121017, 0.0, 17.0, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 17, 170017, 121017, 0.09, 30201579.21782729, 12583991.34076137, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20017, 73.76016021, 0.00119018, 89.05614362, 0.01756226, 8.90561436, 0.06386697, -73.76016021, -0.00119018, -89.05614362, -0.01756226, -8.90561436, -0.06386697, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10017, 78.63362792, 0.00119018, 94.94024471, 0.01756226, 9.49402447, 0.06386697, -78.63362792, -0.00119018, -94.94024471, -0.01756226, -9.49402447, -0.06386697, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20017, 17, 0.0, 113.90582383, 0.02380367, 113.90582383, 0.071411, 79.73407668, -1351.0919045, 0.05, 2, 0, 70017, 21017, 2, 3)
    ops.uniaxialMaterial('LimitState', 40017, 28.47645596, 0.00011164, 85.42936787, 0.00033491, 284.76455957, 0.00111637, -28.47645596, -0.00011164, -85.42936787, -0.00033491, -284.76455957, -0.00111637, 0.4, 0.3, 0.003, 0.0, 0.0, 20017, 2)
    ops.limitCurve('ThreePoint', 10017, 17, 0.0, 113.90582383, 0.02380367, 113.90582383, 0.071411, 79.73407668, -1351.0919045, 0.05, 2, 0, 70017, 21017, 1, 3)
    ops.uniaxialMaterial('LimitState', 30017, 28.47645596, 0.00011164, 85.42936787, 0.00033491, 284.76455957, 0.00111637, -28.47645596, -0.00011164, -85.42936787, -0.00033491, -284.76455957, -0.00111637, 0.4, 0.3, 0.003, 0.0, 0.0, 10017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 17, 99999, 'P', 40017, 'Vy', 30017, 'Vz', 20017, 'My', 10017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170017, 70017, 170017, 17, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121017, 121017, 21017, 17, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170018, 2.95, 17.0, 0.0)
    ops.node(121018, 2.95, 17.0, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 18, 170018, 121018, 0.1225, 30441083.63528915, 12683784.84803715, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20018, 167.05599259, 0.0011192, 201.19960275, 0.02566637, 20.11996027, 0.07201476, -167.05599259, -0.0011192, -201.19960275, -0.02566637, -20.11996027, -0.07201476, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10018, 173.05302808, 0.0011192, 208.42233771, 0.02566637, 20.84223377, 0.07201476, -173.05302808, -0.0011192, -208.42233771, -0.02566637, -20.84223377, -0.07201476, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20018, 18, 0.0, 165.41634278, 0.02238394, 165.41634278, 0.06715181, 115.79143994, -1910.9824752, 0.05, 2, 0, 70018, 21018, 2, 3)
    ops.uniaxialMaterial('LimitState', 40018, 41.35408569, 0.00011817, 124.06225708, 0.00035452, 413.54085694, 0.00118173, -41.35408569, -0.00011817, -124.06225708, -0.00035452, -413.54085694, -0.00118173, 0.4, 0.3, 0.003, 0.0, 0.0, 20018, 2)
    ops.limitCurve('ThreePoint', 10018, 18, 0.0, 165.41634278, 0.02238394, 165.41634278, 0.06715181, 115.79143994, -1910.9824752, 0.05, 2, 0, 70018, 21018, 1, 3)
    ops.uniaxialMaterial('LimitState', 30018, 41.35408569, 0.00011817, 124.06225708, 0.00035452, 413.54085694, 0.00118173, -41.35408569, -0.00011817, -124.06225708, -0.00035452, -413.54085694, -0.00118173, 0.4, 0.3, 0.003, 0.0, 0.0, 10018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 18, 99999, 'P', 40018, 'Vy', 30018, 'Vz', 20018, 'My', 10018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170018, 70018, 170018, 18, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121018, 121018, 21018, 18, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170019, 8.3, 17.0, 0.0)
    ops.node(121019, 8.3, 17.0, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 19, 170019, 121019, 0.16, 29481137.17334965, 12283807.15556235, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20019, 263.31143742, 0.00104921, 317.70874508, 0.03367579, 31.77087451, 0.08452383, -263.31143742, -0.00104921, -317.70874508, -0.03367579, -31.77087451, -0.08452383, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10019, 276.34844555, 0.00104921, 333.43905871, 0.03367579, 33.34390587, 0.08452383, -276.34844555, -0.00104921, -333.43905871, -0.03367579, -33.34390587, -0.08452383, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20019, 19, 0.0, 224.29402706, 0.02098425, 224.29402706, 0.06295274, 157.00581894, -2899.99276907, 0.05, 2, 0, 70019, 21019, 2, 3)
    ops.uniaxialMaterial('LimitState', 40019, 56.07350677, 0.00012667, 168.2205203, 0.00038002, 560.73506765, 0.00126674, -56.07350677, -0.00012667, -168.2205203, -0.00038002, -560.73506765, -0.00126674, 0.4, 0.3, 0.003, 0.0, 0.0, 20019, 2)
    ops.limitCurve('ThreePoint', 10019, 19, 0.0, 224.29402706, 0.02098425, 224.29402706, 0.06295274, 157.00581894, -2899.99276907, 0.05, 2, 0, 70019, 21019, 1, 3)
    ops.uniaxialMaterial('LimitState', 30019, 56.07350677, 0.00012667, 168.2205203, 0.00038002, 560.73506765, 0.00126674, -56.07350677, -0.00012667, -168.2205203, -0.00038002, -560.73506765, -0.00126674, 0.4, 0.3, 0.003, 0.0, 0.0, 10019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 19, 99999, 'P', 40019, 'Vy', 30019, 'Vz', 20019, 'My', 10019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170019, 70019, 170019, 19, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121019, 121019, 21019, 19, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170020, 13.65, 17.0, 0.0)
    ops.node(121020, 13.65, 17.0, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 20, 170020, 121020, 0.1225, 30412020.66071639, 12671675.27529849, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20020, 162.46020681, 0.00109378, 195.8425007, 0.01643681, 19.58425007, 0.05654567, -162.46020681, -0.00109378, -195.8425007, -0.01643681, -19.58425007, -0.05654567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10020, 162.46020681, 0.00109378, 195.8425007, 0.01643681, 19.58425007, 0.05654567, -162.46020681, -0.00109378, -195.8425007, -0.01643681, -19.58425007, -0.05654567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20020, 20, 0.0, 148.26075734, 0.02187552, 148.26075734, 0.06562655, 103.78253014, -1501.39588799, 0.05, 2, 0, 70020, 21020, 2, 3)
    ops.uniaxialMaterial('LimitState', 40020, 37.06518933, 0.00010602, 111.195568, 0.00031805, 370.65189335, 0.00106018, -37.06518933, -0.00010602, -111.195568, -0.00031805, -370.65189335, -0.00106018, 0.4, 0.3, 0.003, 0.0, 0.0, 20020, 2)
    ops.limitCurve('ThreePoint', 10020, 20, 0.0, 148.26075734, 0.02187552, 148.26075734, 0.06562655, 103.78253014, -1501.39588799, 0.05, 2, 0, 70020, 21020, 1, 3)
    ops.uniaxialMaterial('LimitState', 30020, 37.06518933, 0.00010602, 111.195568, 0.00031805, 370.65189335, 0.00106018, -37.06518933, -0.00010602, -111.195568, -0.00031805, -370.65189335, -0.00106018, 0.4, 0.3, 0.003, 0.0, 0.0, 10020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 20, 99999, 'P', 40020, 'Vy', 30020, 'Vz', 20020, 'My', 10020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170020, 70020, 170020, 20, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121020, 121020, 21020, 20, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170021, 0.0, 21.25, 0.0)
    ops.node(121021, 0.0, 21.25, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 21, 170021, 121021, 0.09, 28274496.97854435, 11781040.40772681, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20021, 90.75158014, 0.00127519, 109.95398127, 0.01787308, 10.99539813, 0.06167687, -90.75158014, -0.00127519, -109.95398127, -0.01787308, -10.99539813, -0.06167687, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10021, 95.52002708, 0.00127519, 115.73139832, 0.01787308, 11.57313983, 0.06167687, -95.52002708, -0.00127519, -115.73139832, -0.01787308, -11.57313983, -0.06167687, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20021, 21, 0.0, 107.17504784, 0.02550373, 107.17504784, 0.07651118, 75.02253349, -1302.50302998, 0.05, 2, 0, 70021, 21021, 2, 3)
    ops.uniaxialMaterial('LimitState', 40021, 26.79376196, 0.0001122, 80.38128588, 0.0003366, 267.9376196, 0.00112199, -26.79376196, -0.0001122, -80.38128588, -0.0003366, -267.9376196, -0.00112199, 0.4, 0.3, 0.003, 0.0, 0.0, 20021, 2)
    ops.limitCurve('ThreePoint', 10021, 21, 0.0, 107.17504784, 0.02550373, 107.17504784, 0.07651118, 75.02253349, -1302.50302998, 0.05, 2, 0, 70021, 21021, 1, 3)
    ops.uniaxialMaterial('LimitState', 30021, 26.79376196, 0.0001122, 80.38128588, 0.0003366, 267.9376196, 0.00112199, -26.79376196, -0.0001122, -80.38128588, -0.0003366, -267.9376196, -0.00112199, 0.4, 0.3, 0.003, 0.0, 0.0, 10021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 21, 99999, 'P', 40021, 'Vy', 30021, 'Vz', 20021, 'My', 10021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170021, 70021, 170021, 21, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121021, 121021, 21021, 21, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170022, 2.95, 21.25, 0.0)
    ops.node(121022, 2.95, 21.25, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 22, 170022, 121022, 0.1225, 29505554.99546578, 12293981.24811074, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20022, 168.76267754, 0.0011398, 203.60657223, 0.02527919, 20.36065722, 0.07023484, -168.76267754, -0.0011398, -203.60657223, -0.02527919, -20.36065722, -0.07023484, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10022, 174.91616102, 0.0011398, 211.03054592, 0.02527919, 21.10305459, 0.07023484, -174.91616102, -0.0011398, -211.03054592, -0.02527919, -21.10305459, -0.07023484, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20022, 22, 0.0, 160.34932208, 0.02279602, 160.34932208, 0.06838806, 112.24452546, -1866.6896285, 0.05, 2, 0, 70022, 21022, 2, 3)
    ops.uniaxialMaterial('LimitState', 40022, 40.08733052, 0.00011818, 120.26199156, 0.00035455, 400.87330521, 0.00118185, -40.08733052, -0.00011818, -120.26199156, -0.00035455, -400.87330521, -0.00118185, 0.4, 0.3, 0.003, 0.0, 0.0, 20022, 2)
    ops.limitCurve('ThreePoint', 10022, 22, 0.0, 160.34932208, 0.02279602, 160.34932208, 0.06838806, 112.24452546, -1866.6896285, 0.05, 2, 0, 70022, 21022, 1, 3)
    ops.uniaxialMaterial('LimitState', 30022, 40.08733052, 0.00011818, 120.26199156, 0.00035455, 400.87330521, 0.00118185, -40.08733052, -0.00011818, -120.26199156, -0.00035455, -400.87330521, -0.00118185, 0.4, 0.3, 0.003, 0.0, 0.0, 10022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 22, 99999, 'P', 40022, 'Vy', 30022, 'Vz', 20022, 'My', 10022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170022, 70022, 170022, 22, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121022, 121022, 21022, 22, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170023, 8.3, 21.25, 0.0)
    ops.node(121023, 8.3, 21.25, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 23, 170023, 121023, 0.16, 28186091.72620538, 11744204.88591891, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20023, 288.03768512, 0.00105457, 348.17338937, 0.03430676, 34.81733894, 0.08268857, -288.03768512, -0.00105457, -348.17338937, -0.03430676, -34.81733894, -0.08268857, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10023, 288.03768512, 0.00105457, 348.17338937, 0.03430676, 34.81733894, 0.08268857, -288.03768512, -0.00105457, -348.17338937, -0.03430676, -34.81733894, -0.08268857, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20023, 23, 0.0, 218.72805614, 0.02109143, 218.72805614, 0.0632743, 153.1096393, -2922.60472743, 0.05, 2, 0, 70023, 21023, 2, 3)
    ops.uniaxialMaterial('LimitState', 40023, 54.68201403, 0.00012921, 164.0460421, 0.00038762, 546.82014035, 0.00129206, -54.68201403, -0.00012921, -164.0460421, -0.00038762, -546.82014035, -0.00129206, 0.4, 0.3, 0.003, 0.0, 0.0, 20023, 2)
    ops.limitCurve('ThreePoint', 10023, 23, 0.0, 218.72805614, 0.02109143, 218.72805614, 0.0632743, 153.1096393, -2922.60472743, 0.05, 2, 0, 70023, 21023, 1, 3)
    ops.uniaxialMaterial('LimitState', 30023, 54.68201403, 0.00012921, 164.0460421, 0.00038762, 546.82014035, 0.00129206, -54.68201403, -0.00012921, -164.0460421, -0.00038762, -546.82014035, -0.00129206, 0.4, 0.3, 0.003, 0.0, 0.0, 10023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 23, 99999, 'P', 40023, 'Vy', 30023, 'Vz', 20023, 'My', 10023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170023, 70023, 170023, 23, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121023, 121023, 21023, 23, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170024, 13.65, 21.25, 0.0)
    ops.node(121024, 13.65, 21.25, 3.4)
    # Create elastic column element
    ops.element('elasticBeamColumn', 24, 170024, 121024, 0.1225, 29334061.25741038, 12222525.52392099, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20024, 159.60230967, 0.00107857, 192.79358165, 0.01712145, 19.27935816, 0.05595007, -159.60230967, -0.00107857, -192.79358165, -0.01712145, -19.27935816, -0.05595007, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10024, 159.60230967, 0.00107857, 192.79358165, 0.01712145, 19.27935816, 0.05595007, -159.60230967, -0.00107857, -192.79358165, -0.01712145, -19.27935816, -0.05595007, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20024, 24, 0.0, 145.1430088, 0.02157135, 145.1430088, 0.06471406, 101.60010616, -1526.99935091, 0.05, 2, 0, 70024, 21024, 2, 3)
    ops.uniaxialMaterial('LimitState', 40024, 36.2857522, 0.0001076, 108.8572566, 0.00032281, 362.85752199, 0.00107602, -36.2857522, -0.0001076, -108.8572566, -0.00032281, -362.85752199, -0.00107602, 0.4, 0.3, 0.003, 0.0, 0.0, 20024, 2)
    ops.limitCurve('ThreePoint', 10024, 24, 0.0, 145.1430088, 0.02157135, 145.1430088, 0.06471406, 101.60010616, -1526.99935091, 0.05, 2, 0, 70024, 21024, 1, 3)
    ops.uniaxialMaterial('LimitState', 30024, 36.2857522, 0.0001076, 108.8572566, 0.00032281, 362.85752199, 0.00107602, -36.2857522, -0.0001076, -108.8572566, -0.00032281, -362.85752199, -0.00107602, 0.4, 0.3, 0.003, 0.0, 0.0, 10024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 24, 99999, 'P', 40024, 'Vy', 30024, 'Vz', 20024, 'My', 10024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170024, 70024, 170024, 24, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121024, 121024, 21024, 24, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170025, 0.0, 25.5, 0.0)
    ops.node(121025, 0.0, 25.5, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 25, 170025, 121025, 0.0625, 28364455.65409087, 11818523.18920453, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20025, 36.85010284, 0.00142264, 44.69411474, 0.01867463, 4.46941147, 0.07116249, -36.85010284, -0.00142264, -44.69411474, -0.01867463, -4.46941147, -0.07116249, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10025, 40.28739958, 0.00142264, 48.8630837, 0.01867463, 4.88630837, 0.07116249, -40.28739958, -0.00142264, -48.8630837, -0.01867463, -4.88630837, -0.07116249, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20025, 25, 0.0, 80.49620308, 0.02845285, 80.49620308, 0.08535855, 56.34734215, -1192.56118888, 0.05, 2, 0, 70025, 21025, 2, 3)
    ops.uniaxialMaterial('LimitState', 40025, 20.12405077, 0.00012096, 60.37215231, 0.00036289, 201.24050769, 0.00120964, -20.12405077, -0.00012096, -60.37215231, -0.00036289, -201.24050769, -0.00120964, 0.4, 0.3, 0.003, 0.0, 0.0, 20025, 2)
    ops.limitCurve('ThreePoint', 10025, 25, 0.0, 80.49620308, 0.02845285, 80.49620308, 0.08535855, 56.34734215, -1192.56118888, 0.05, 2, 0, 70025, 21025, 1, 3)
    ops.uniaxialMaterial('LimitState', 30025, 20.12405077, 0.00012096, 60.37215231, 0.00036289, 201.24050769, 0.00120964, -20.12405077, -0.00012096, -60.37215231, -0.00036289, -201.24050769, -0.00120964, 0.4, 0.3, 0.003, 0.0, 0.0, 10025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 25, 99999, 'P', 40025, 'Vy', 30025, 'Vz', 20025, 'My', 10025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170025, 70025, 170025, 25, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121025, 121025, 21025, 25, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170026, 2.95, 25.5, 0.0)
    ops.node(121026, 2.95, 25.5, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 26, 170026, 121026, 0.09, 28502347.76707625, 11875978.23628177, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20026, 96.31347377, 0.00124565, 116.3521079, 0.01739584, 11.63521079, 0.05825678, -96.31347377, -0.00124565, -116.3521079, -0.01739584, -11.63521079, -0.05825678, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10026, 101.47021499, 0.00124565, 122.5817421, 0.01739584, 12.25817421, 0.05825678, -101.47021499, -0.00124565, -122.5817421, -0.01739584, -12.25817421, -0.05825678, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20026, 26, 0.0, 111.82590385, 0.02491293, 111.82590385, 0.0747388, 78.2781327, -1272.26277493, 0.05, 2, 0, 70026, 21026, 2, 3)
    ops.uniaxialMaterial('LimitState', 40026, 27.95647596, 0.00011613, 83.86942789, 0.0003484, 279.56475963, 0.00116132, -27.95647596, -0.00011613, -83.86942789, -0.0003484, -279.56475963, -0.00116132, 0.4, 0.3, 0.003, 0.0, 0.0, 20026, 2)
    ops.limitCurve('ThreePoint', 10026, 26, 0.0, 111.82590385, 0.02491293, 111.82590385, 0.0747388, 78.2781327, -1272.26277493, 0.05, 2, 0, 70026, 21026, 1, 3)
    ops.uniaxialMaterial('LimitState', 30026, 27.95647596, 0.00011613, 83.86942789, 0.0003484, 279.56475963, 0.00116132, -27.95647596, -0.00011613, -83.86942789, -0.0003484, -279.56475963, -0.00116132, 0.4, 0.3, 0.003, 0.0, 0.0, 10026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 26, 99999, 'P', 40026, 'Vy', 30026, 'Vz', 20026, 'My', 10026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170026, 70026, 170026, 26, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121026, 121026, 21026, 26, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170027, 8.3, 25.5, 0.0)
    ops.node(121027, 8.3, 25.5, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 27, 170027, 121027, 0.1225, 29711434.97458602, 12379764.57274417, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20027, 158.87785612, 0.00111123, 191.69297029, 0.01694786, 19.16929703, 0.05565567, -158.87785612, -0.00111123, -191.69297029, -0.01694786, -19.16929703, -0.05565567, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10027, 158.87785612, 0.00111123, 191.69297029, 0.01694786, 19.16929703, 0.05565567, -158.87785612, -0.00111123, -191.69297029, -0.01694786, -19.16929703, -0.05565567, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20027, 27, 0.0, 146.91742387, 0.0222246, 146.91742387, 0.06667379, 102.84219671, -1502.62363959, 0.05, 2, 0, 70027, 21027, 2, 3)
    ops.uniaxialMaterial('LimitState', 40027, 36.72935597, 0.00010753, 110.1880679, 0.0003226, 367.29355968, 0.00107534, -36.72935597, -0.00010753, -110.1880679, -0.0003226, -367.29355968, -0.00107534, 0.4, 0.3, 0.003, 0.0, 0.0, 20027, 2)
    ops.limitCurve('ThreePoint', 10027, 27, 0.0, 146.91742387, 0.0222246, 146.91742387, 0.06667379, 102.84219671, -1502.62363959, 0.05, 2, 0, 70027, 21027, 1, 3)
    ops.uniaxialMaterial('LimitState', 30027, 36.72935597, 0.00010753, 110.1880679, 0.0003226, 367.29355968, 0.00107534, -36.72935597, -0.00010753, -110.1880679, -0.0003226, -367.29355968, -0.00107534, 0.4, 0.3, 0.003, 0.0, 0.0, 10027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 27, 99999, 'P', 40027, 'Vy', 30027, 'Vz', 20027, 'My', 10027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170027, 70027, 170027, 27, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121027, 121027, 21027, 27, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170028, 13.65, 25.5, 0.0)
    ops.node(121028, 13.65, 25.5, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 28, 170028, 121028, 0.09, 28835944.71810736, 12014976.96587807, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 20028, 83.61612335, 0.00122262, 101.24828281, 0.01783866, 10.12482828, 0.06280374, -83.61612335, -0.00122262, -101.24828281, -0.01783866, -10.12482828, -0.06280374, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 10028, 83.61612335, 0.00122262, 101.24828281, 0.01783866, 10.12482828, 0.06280374, -83.61612335, -0.00122262, -101.24828281, -0.01783866, -10.12482828, -0.06280374, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 20028, 28, 0.0, 108.73860788, 0.0244524, 108.73860788, 0.07335721, 76.11702552, -1326.66249396, 0.05, 2, 0, 70028, 21028, 2, 3)
    ops.uniaxialMaterial('LimitState', 40028, 27.18465197, 0.00011162, 81.55395591, 0.00033486, 271.84651971, 0.0011162, -27.18465197, -0.00011162, -81.55395591, -0.00033486, -271.84651971, -0.0011162, 0.4, 0.3, 0.003, 0.0, 0.0, 20028, 2)
    ops.limitCurve('ThreePoint', 10028, 28, 0.0, 108.73860788, 0.0244524, 108.73860788, 0.07335721, 76.11702552, -1326.66249396, 0.05, 2, 0, 70028, 21028, 1, 3)
    ops.uniaxialMaterial('LimitState', 30028, 27.18465197, 0.00011162, 81.55395591, 0.00033486, 271.84651971, 0.0011162, -27.18465197, -0.00011162, -81.55395591, -0.00033486, -271.84651971, -0.0011162, 0.4, 0.3, 0.003, 0.0, 0.0, 10028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 28, 99999, 'P', 40028, 'Vy', 30028, 'Vz', 20028, 'My', 10028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170028, 70028, 170028, 28, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121028, 121028, 21028, 28, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171003, 8.3, 0.0, 3.95)
    ops.node(122003, 8.3, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1003, 171003, 122003, 0.1225, 28414397.05274494, 11839332.10531039, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21003, 87.57932276, 0.00092356, 106.21661098, 0.01579534, 10.6216611, 0.05642597, -87.57932276, -0.00092356, -106.21661098, -0.01579534, -10.6216611, -0.05642597, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11003, 76.84287027, 0.00092356, 93.19539134, 0.01579534, 9.31953913, 0.05642597, -76.84287027, -0.00092356, -93.19539134, -0.01579534, -9.31953913, -0.05642597, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21003, 1003, 0.0, 134.91602206, 0.01847117, 134.91602206, 0.05541351, 94.44121544, -1824.31985972, 0.05, 2, 0, 71003, 22003, 2, 3)
    ops.uniaxialMaterial('LimitState', 41003, 33.72900552, 8.651e-05, 101.18701655, 0.00025954, 337.29005515, 0.00086513, -33.72900552, -8.651e-05, -101.18701655, -0.00025954, -337.29005515, -0.00086513, 0.4, 0.3, 0.003, 0.0, 0.0, 21003, 2)
    ops.limitCurve('ThreePoint', 11003, 1003, 0.0, 134.91602206, 0.01847117, 134.91602206, 0.05541351, 94.44121544, -1824.31985972, 0.05, 2, 0, 71003, 22003, 1, 3)
    ops.uniaxialMaterial('LimitState', 31003, 33.72900552, 8.651e-05, 101.18701655, 0.00025954, 337.29005515, 0.00086513, -33.72900552, -8.651e-05, -101.18701655, -0.00025954, -337.29005515, -0.00086513, 0.4, 0.3, 0.003, 0.0, 0.0, 11003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1003, 99999, 'P', 41003, 'Vy', 31003, 'Vz', 21003, 'My', 11003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171003, 71003, 171003, 1003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122003, 122003, 22003, 1003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171004, 13.65, 0.0, 3.95)
    ops.node(122004, 13.65, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1004, 171004, 122004, 0.09, 28819413.93867648, 12008089.1411152, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21004, 52.38555047, 0.00101227, 63.58976121, 0.01749748, 6.35897612, 0.06585192, -52.38555047, -0.00101227, -63.58976121, -0.01749748, -6.35897612, -0.06585192, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11004, 47.90301348, 0.00101227, 58.14850013, 0.01749748, 5.81485001, 0.06585192, -47.90301348, -0.00101227, -58.14850013, -0.01749748, -5.81485001, -0.06585192, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21004, 1004, 0.0, 106.3759225, 0.02024539, 106.3759225, 0.06073618, 74.46314575, -1820.05108193, 0.05, 2, 0, 71004, 22004, 2, 3)
    ops.uniaxialMaterial('LimitState', 41004, 26.59398063, 9.154e-05, 79.78194188, 0.00027462, 265.93980626, 0.0009154, -26.59398063, -9.154e-05, -79.78194188, -0.00027462, -265.93980626, -0.0009154, 0.4, 0.3, 0.003, 0.0, 0.0, 21004, 2)
    ops.limitCurve('ThreePoint', 11004, 1004, 0.0, 106.3759225, 0.02024539, 106.3759225, 0.06073618, 74.46314575, -1820.05108193, 0.05, 2, 0, 71004, 22004, 1, 3)
    ops.uniaxialMaterial('LimitState', 31004, 26.59398063, 9.154e-05, 79.78194188, 0.00027462, 265.93980626, 0.0009154, -26.59398063, -9.154e-05, -79.78194188, -0.00027462, -265.93980626, -0.0009154, 0.4, 0.3, 0.003, 0.0, 0.0, 11004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1004, 99999, 'P', 41004, 'Vy', 31004, 'Vz', 21004, 'My', 11004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171004, 71004, 171004, 1004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122004, 122004, 22004, 1004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171005, 0.0, 4.25, 4.0)
    ops.node(122005, 0.0, 4.25, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1005, 171005, 122005, 0.09, 29154531.46772906, 12147721.44488711, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21005, 51.82545847, 0.00103872, 62.76783734, 0.01654065, 6.27678373, 0.06298924, -51.82545847, -0.00103872, -62.76783734, -0.01654065, -6.27678373, -0.06298924, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11005, 56.36328671, 0.00103872, 68.2637784, 0.01654065, 6.82637784, 0.06298924, -56.36328671, -0.00103872, -68.2637784, -0.01654065, -6.82637784, -0.06298924, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21005, 1005, 0.0, 108.71783038, 0.02077438, 108.71783038, 0.06232313, 76.10248126, -1636.24119987, 0.05, 2, 0, 71005, 22005, 2, 3)
    ops.uniaxialMaterial('LimitState', 41005, 27.17945759, 9.248e-05, 81.53837278, 0.00027744, 271.79457594, 0.0009248, -27.17945759, -9.248e-05, -81.53837278, -0.00027744, -271.79457594, -0.0009248, 0.4, 0.3, 0.003, 0.0, 0.0, 21005, 2)
    ops.limitCurve('ThreePoint', 11005, 1005, 0.0, 108.71783038, 0.02077438, 108.71783038, 0.06232313, 76.10248126, -1636.24119987, 0.05, 2, 0, 71005, 22005, 1, 3)
    ops.uniaxialMaterial('LimitState', 31005, 27.17945759, 9.248e-05, 81.53837278, 0.00027744, 271.79457594, 0.0009248, -27.17945759, -9.248e-05, -81.53837278, -0.00027744, -271.79457594, -0.0009248, 0.4, 0.3, 0.003, 0.0, 0.0, 11005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1005, 99999, 'P', 41005, 'Vy', 31005, 'Vz', 21005, 'My', 11005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171005, 71005, 171005, 1005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122005, 122005, 22005, 1005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171006, 2.95, 4.25, 4.0)
    ops.node(122006, 2.95, 4.25, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1006, 171006, 122006, 0.1225, 29422481.4410108, 12259367.26708784, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21006, 102.23412484, 0.00095265, 123.5586272, 0.01913574, 12.35586272, 0.05885808, -102.23412484, -0.00095265, -123.5586272, -0.01913574, -12.35586272, -0.05885808, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11006, 96.61651152, 0.00095265, 116.76926415, 0.01913574, 11.67692641, 0.05885808, -96.61651152, -0.00095265, -116.76926415, -0.01913574, -11.67692641, -0.05885808, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21006, 1006, 0.0, 141.72828797, 0.01905309, 141.72828797, 0.05715928, 99.20980158, -1756.14768215, 0.05, 2, 0, 71006, 22006, 2, 3)
    ops.uniaxialMaterial('LimitState', 41006, 35.43207199, 8.777e-05, 106.29621598, 0.0002633, 354.32071993, 0.00087768, -35.43207199, -8.777e-05, -106.29621598, -0.0002633, -354.32071993, -0.00087768, 0.4, 0.3, 0.003, 0.0, 0.0, 21006, 2)
    ops.limitCurve('ThreePoint', 11006, 1006, 0.0, 141.72828797, 0.01905309, 141.72828797, 0.05715928, 99.20980158, -1756.14768215, 0.05, 2, 0, 71006, 22006, 1, 3)
    ops.uniaxialMaterial('LimitState', 31006, 35.43207199, 8.777e-05, 106.29621598, 0.0002633, 354.32071993, 0.00087768, -35.43207199, -8.777e-05, -106.29621598, -0.0002633, -354.32071993, -0.00087768, 0.4, 0.3, 0.003, 0.0, 0.0, 11006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1006, 99999, 'P', 41006, 'Vy', 31006, 'Vz', 21006, 'My', 11006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171006, 71006, 171006, 1006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122006, 122006, 22006, 1006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171007, 8.3, 4.25, 4.0)
    ops.node(122007, 8.3, 4.25, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1007, 171007, 122007, 0.16, 28763916.87455272, 11984965.36439697, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21007, 142.19773482, 0.00091513, 172.28310649, 0.01833795, 17.22831065, 0.05080037, -142.19773482, -0.00091513, -172.28310649, -0.01833795, -17.22831065, -0.05080037, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11007, 142.19773482, 0.00091513, 172.28310649, 0.01833795, 17.22831065, 0.05080037, -142.19773482, -0.00091513, -172.28310649, -0.01833795, -17.22831065, -0.05080037, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21007, 1007, 0.0, 158.88712207, 0.01830258, 158.88712207, 0.05490775, 111.22098545, -1682.51940063, 0.05, 2, 0, 71007, 22007, 2, 3)
    ops.uniaxialMaterial('LimitState', 41007, 39.72178052, 7.706e-05, 119.16534155, 0.00023117, 397.21780518, 0.00077057, -39.72178052, -7.706e-05, -119.16534155, -0.00023117, -397.21780518, -0.00077057, 0.4, 0.3, 0.003, 0.0, 0.0, 21007, 2)
    ops.limitCurve('ThreePoint', 11007, 1007, 0.0, 158.88712207, 0.01830258, 158.88712207, 0.05490775, 111.22098545, -1682.51940063, 0.05, 2, 0, 71007, 22007, 1, 3)
    ops.uniaxialMaterial('LimitState', 31007, 39.72178052, 7.706e-05, 119.16534155, 0.00023117, 397.21780518, 0.00077057, -39.72178052, -7.706e-05, -119.16534155, -0.00023117, -397.21780518, -0.00077057, 0.4, 0.3, 0.003, 0.0, 0.0, 11007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1007, 99999, 'P', 41007, 'Vy', 31007, 'Vz', 21007, 'My', 11007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171007, 71007, 171007, 1007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122007, 122007, 22007, 1007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171008, 13.65, 4.25, 4.0)
    ops.node(122008, 13.65, 4.25, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1008, 171008, 122008, 0.1225, 29813771.69456388, 12422404.87273495, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21008, 88.62879603, 0.00089263, 107.24217067, 0.01573857, 10.72421707, 0.05828179, -88.62879603, -0.00089263, -107.24217067, -0.01573857, -10.72421707, -0.05828179, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11008, 77.00500877, 0.00089263, 93.17721399, 0.01573857, 9.3177214, 0.05828179, -77.00500877, -0.00089263, -93.17721399, -0.01573857, -9.3177214, -0.05828179, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21008, 1008, 0.0, 138.89438651, 0.01785268, 138.89438651, 0.05355803, 97.22607056, -1831.8420854, 0.05, 2, 0, 71008, 22008, 2, 3)
    ops.uniaxialMaterial('LimitState', 41008, 34.72359663, 8.488e-05, 104.17078988, 0.00025465, 347.23596628, 0.00084884, -34.72359663, -8.488e-05, -104.17078988, -0.00025465, -347.23596628, -0.00084884, 0.4, 0.3, 0.003, 0.0, 0.0, 21008, 2)
    ops.limitCurve('ThreePoint', 11008, 1008, 0.0, 138.89438651, 0.01785268, 138.89438651, 0.05355803, 97.22607056, -1831.8420854, 0.05, 2, 0, 71008, 22008, 1, 3)
    ops.uniaxialMaterial('LimitState', 31008, 34.72359663, 8.488e-05, 104.17078988, 0.00025465, 347.23596628, 0.00084884, -34.72359663, -8.488e-05, -104.17078988, -0.00025465, -347.23596628, -0.00084884, 0.4, 0.3, 0.003, 0.0, 0.0, 11008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1008, 99999, 'P', 41008, 'Vy', 31008, 'Vz', 21008, 'My', 11008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171008, 71008, 171008, 1008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122008, 122008, 22008, 1008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171009, 0.0, 8.5, 4.0)
    ops.node(122009, 0.0, 8.5, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1009, 171009, 122009, 0.09, 29456380.08809245, 12273491.70337186, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21009, 48.75826998, 0.00102121, 59.09758424, 0.01696944, 5.90975842, 0.06568133, -48.75826998, -0.00102121, -59.09758424, -0.01696944, -5.90975842, -0.06568133, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11009, 53.25013132, 0.00102121, 64.54195611, 0.01696944, 6.45419561, 0.06568133, -53.25013132, -0.00102121, -64.54195611, -0.01696944, -6.45419561, -0.06568133, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21009, 1009, 0.0, 106.93690439, 0.02042425, 106.93690439, 0.06127274, 74.85583308, -1729.42854504, 0.05, 2, 0, 71009, 22009, 2, 3)
    ops.uniaxialMaterial('LimitState', 41009, 26.7342261, 9.003e-05, 80.2026783, 0.0002701, 267.34226098, 0.00090033, -26.7342261, -9.003e-05, -80.2026783, -0.0002701, -267.34226098, -0.00090033, 0.4, 0.3, 0.003, 0.0, 0.0, 21009, 2)
    ops.limitCurve('ThreePoint', 11009, 1009, 0.0, 106.93690439, 0.02042425, 106.93690439, 0.06127274, 74.85583308, -1729.42854504, 0.05, 2, 0, 71009, 22009, 1, 3)
    ops.uniaxialMaterial('LimitState', 31009, 26.7342261, 9.003e-05, 80.2026783, 0.0002701, 267.34226098, 0.00090033, -26.7342261, -9.003e-05, -80.2026783, -0.0002701, -267.34226098, -0.00090033, 0.4, 0.3, 0.003, 0.0, 0.0, 11009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1009, 99999, 'P', 41009, 'Vy', 31009, 'Vz', 21009, 'My', 11009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171009, 71009, 171009, 1009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122009, 122009, 22009, 1009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171010, 2.95, 8.5, 4.0)
    ops.node(122010, 2.95, 8.5, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1010, 171010, 122010, 0.1225, 29505534.20344594, 12293972.58476914, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21010, 99.62951913, 0.00094009, 120.54059936, 0.02411132, 12.05405994, 0.07302682, -99.62951913, -0.00094009, -120.54059936, -0.02411132, -12.05405994, -0.07302682, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11010, 93.76561213, 0.00094009, 113.4459263, 0.02411132, 11.34459263, 0.07302682, -93.76561213, -0.00094009, -113.4459263, -0.02411132, -11.34459263, -0.07302682, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21010, 1010, 0.0, 156.03011639, 0.01880189, 156.03011639, 0.05640566, 109.22108147, -2448.86073584, 0.05, 2, 0, 71010, 22010, 2, 3)
    ops.uniaxialMaterial('LimitState', 41010, 39.0075291, 9.635e-05, 117.02258729, 0.00028906, 390.07529097, 0.00096353, -39.0075291, -9.635e-05, -117.02258729, -0.00028906, -390.07529097, -0.00096353, 0.4, 0.3, 0.003, 0.0, 0.0, 21010, 2)
    ops.limitCurve('ThreePoint', 11010, 1010, 0.0, 156.03011639, 0.01880189, 156.03011639, 0.05640566, 109.22108147, -2448.86073584, 0.05, 2, 0, 71010, 22010, 1, 3)
    ops.uniaxialMaterial('LimitState', 31010, 39.0075291, 9.635e-05, 117.02258729, 0.00028906, 390.07529097, 0.00096353, -39.0075291, -9.635e-05, -117.02258729, -0.00028906, -390.07529097, -0.00096353, 0.4, 0.3, 0.003, 0.0, 0.0, 11010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1010, 99999, 'P', 41010, 'Vy', 31010, 'Vz', 21010, 'My', 11010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171010, 71010, 171010, 1010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122010, 122010, 22010, 1010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171011, 8.3, 8.5, 4.0)
    ops.node(122011, 8.3, 8.5, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1011, 171011, 122011, 0.16, 29240689.8067724, 12183620.75282183, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21011, 140.16580393, 0.00089521, 169.67488362, 0.01911915, 16.96748836, 0.05200612, -140.16580393, -0.00089521, -169.67488362, -0.01911915, -16.96748836, -0.05200612, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11011, 140.16580393, 0.00089521, 169.67488362, 0.01911915, 16.96748836, 0.05200612, -140.16580393, -0.00089521, -169.67488362, -0.01911915, -16.96748836, -0.05200612, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21011, 1011, 0.0, 163.270783, 0.01790423, 163.270783, 0.05371268, 114.2895481, -1748.36261971, 0.05, 2, 0, 71011, 22011, 2, 3)
    ops.uniaxialMaterial('LimitState', 41011, 40.81769575, 7.789e-05, 122.45308725, 0.00023368, 408.17695751, 0.00077892, -40.81769575, -7.789e-05, -122.45308725, -0.00023368, -408.17695751, -0.00077892, 0.4, 0.3, 0.003, 0.0, 0.0, 21011, 2)
    ops.limitCurve('ThreePoint', 11011, 1011, 0.0, 163.270783, 0.01790423, 163.270783, 0.05371268, 114.2895481, -1748.36261971, 0.05, 2, 0, 71011, 22011, 1, 3)
    ops.uniaxialMaterial('LimitState', 31011, 40.81769575, 7.789e-05, 122.45308725, 0.00023368, 408.17695751, 0.00077892, -40.81769575, -7.789e-05, -122.45308725, -0.00023368, -408.17695751, -0.00077892, 0.4, 0.3, 0.003, 0.0, 0.0, 11011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1011, 99999, 'P', 41011, 'Vy', 31011, 'Vz', 21011, 'My', 11011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171011, 71011, 171011, 1011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122011, 122011, 22011, 1011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171012, 13.65, 8.5, 4.0)
    ops.node(122012, 13.65, 8.5, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1012, 171012, 122012, 0.1225, 30227655.90669308, 12594856.62778878, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21012, 87.50552762, 0.00091006, 105.78479317, 0.01579807, 10.57847932, 0.05871526, -87.50552762, -0.00091006, -105.78479317, -0.01579807, -10.57847932, -0.05871526, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11012, 76.61098173, 0.00091006, 92.61445623, 0.01579807, 9.26144562, 0.05871526, -76.61098173, -0.00091006, -92.61445623, -0.01579807, -9.26144562, -0.05871526, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21012, 1012, 0.0, 140.94332372, 0.01820115, 140.94332372, 0.05460346, 98.6603266, -1851.88333507, 0.05, 2, 0, 71012, 22012, 2, 3)
    ops.uniaxialMaterial('LimitState', 41012, 35.23583093, 8.496e-05, 105.70749279, 0.00025487, 352.3583093, 0.00084957, -35.23583093, -8.496e-05, -105.70749279, -0.00025487, -352.3583093, -0.00084957, 0.4, 0.3, 0.003, 0.0, 0.0, 21012, 2)
    ops.limitCurve('ThreePoint', 11012, 1012, 0.0, 140.94332372, 0.01820115, 140.94332372, 0.05460346, 98.6603266, -1851.88333507, 0.05, 2, 0, 71012, 22012, 1, 3)
    ops.uniaxialMaterial('LimitState', 31012, 35.23583093, 8.496e-05, 105.70749279, 0.00025487, 352.3583093, 0.00084957, -35.23583093, -8.496e-05, -105.70749279, -0.00025487, -352.3583093, -0.00084957, 0.4, 0.3, 0.003, 0.0, 0.0, 11012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1012, 99999, 'P', 41012, 'Vy', 31012, 'Vz', 21012, 'My', 11012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171012, 71012, 171012, 1012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122012, 122012, 22012, 1012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171013, 0.0, 12.75, 4.0)
    ops.node(122013, 0.0, 12.75, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1013, 171013, 122013, 0.09, 29673107.50280973, 12363794.79283739, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21013, 48.53296851, 0.00101318, 58.79655373, 0.01742011, 5.87965537, 0.06633845, -48.53296851, -0.00101318, -58.79655373, -0.01742011, -5.87965537, -0.06633845, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11013, 52.98965447, 0.00101318, 64.19572431, 0.01742011, 6.41957243, 0.06633845, -52.98965447, -0.00101318, -64.19572431, -0.01742011, -6.41957243, -0.06633845, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21013, 1013, 0.0, 109.22004331, 0.02026365, 109.22004331, 0.06079094, 76.45403032, -1810.89543118, 0.05, 2, 0, 71013, 22013, 2, 3)
    ops.uniaxialMaterial('LimitState', 41013, 27.30501083, 9.128e-05, 81.91503248, 0.00027385, 273.05010828, 0.00091283, -27.30501083, -9.128e-05, -81.91503248, -0.00027385, -273.05010828, -0.00091283, 0.4, 0.3, 0.003, 0.0, 0.0, 21013, 2)
    ops.limitCurve('ThreePoint', 11013, 1013, 0.0, 109.22004331, 0.02026365, 109.22004331, 0.06079094, 76.45403032, -1810.89543118, 0.05, 2, 0, 71013, 22013, 1, 3)
    ops.uniaxialMaterial('LimitState', 31013, 27.30501083, 9.128e-05, 81.91503248, 0.00027385, 273.05010828, 0.00091283, -27.30501083, -9.128e-05, -81.91503248, -0.00027385, -273.05010828, -0.00091283, 0.4, 0.3, 0.003, 0.0, 0.0, 11013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1013, 99999, 'P', 41013, 'Vy', 31013, 'Vz', 21013, 'My', 11013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171013, 71013, 171013, 1013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122013, 122013, 22013, 1013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171014, 2.95, 12.75, 4.0)
    ops.node(122014, 2.95, 12.75, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1014, 171014, 122014, 0.1225, 28635075.94096793, 11931281.64206997, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21014, 97.81595305, 0.0009622, 118.53512363, 0.02420635, 11.85351236, 0.07198343, -97.81595305, -0.0009622, -118.53512363, -0.02420635, -11.85351236, -0.07198343, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11014, 92.27068736, 0.0009622, 111.81527136, 0.02420635, 11.18152714, 0.07198343, -92.27068736, -0.0009622, -111.81527136, -0.02420635, -11.18152714, -0.07198343, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21014, 1014, 0.0, 150.67855375, 0.01924392, 150.67855375, 0.05773177, 105.47498763, -2357.39435608, 0.05, 2, 0, 71014, 22014, 2, 3)
    ops.uniaxialMaterial('LimitState', 41014, 37.66963844, 9.588e-05, 113.00891531, 0.00028763, 376.69638438, 0.00095876, -37.66963844, -9.588e-05, -113.00891531, -0.00028763, -376.69638438, -0.00095876, 0.4, 0.3, 0.003, 0.0, 0.0, 21014, 2)
    ops.limitCurve('ThreePoint', 11014, 1014, 0.0, 150.67855375, 0.01924392, 150.67855375, 0.05773177, 105.47498763, -2357.39435608, 0.05, 2, 0, 71014, 22014, 1, 3)
    ops.uniaxialMaterial('LimitState', 31014, 37.66963844, 9.588e-05, 113.00891531, 0.00028763, 376.69638438, 0.00095876, -37.66963844, -9.588e-05, -113.00891531, -0.00028763, -376.69638438, -0.00095876, 0.4, 0.3, 0.003, 0.0, 0.0, 11014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1014, 99999, 'P', 41014, 'Vy', 31014, 'Vz', 21014, 'My', 11014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171014, 71014, 171014, 1014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122014, 122014, 22014, 1014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171015, 8.3, 12.75, 4.0)
    ops.node(122015, 8.3, 12.75, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1015, 171015, 122015, 0.16, 29963530.92484351, 12484804.55201813, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21015, 141.03549902, 0.00087349, 170.47863572, 0.02190131, 17.04786357, 0.05985553, -141.03549902, -0.00087349, -170.47863572, -0.02190131, -17.04786357, -0.05985553, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11015, 141.03549902, 0.00087349, 170.47863572, 0.02190131, 17.04786357, 0.05985553, -141.03549902, -0.00087349, -170.47863572, -0.02190131, -17.04786357, -0.05985553, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21015, 1015, 0.0, 178.1295736, 0.01746971, 178.1295736, 0.05240914, 124.69070152, -2124.73661854, 0.05, 2, 0, 71015, 22015, 2, 3)
    ops.uniaxialMaterial('LimitState', 41015, 44.5323934, 8.293e-05, 133.5971802, 0.00024879, 445.32393399, 0.00082931, -44.5323934, -8.293e-05, -133.5971802, -0.00024879, -445.32393399, -0.00082931, 0.4, 0.3, 0.003, 0.0, 0.0, 21015, 2)
    ops.limitCurve('ThreePoint', 11015, 1015, 0.0, 178.1295736, 0.01746971, 178.1295736, 0.05240914, 124.69070152, -2124.73661854, 0.05, 2, 0, 71015, 22015, 1, 3)
    ops.uniaxialMaterial('LimitState', 31015, 44.5323934, 8.293e-05, 133.5971802, 0.00024879, 445.32393399, 0.00082931, -44.5323934, -8.293e-05, -133.5971802, -0.00024879, -445.32393399, -0.00082931, 0.4, 0.3, 0.003, 0.0, 0.0, 11015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1015, 99999, 'P', 41015, 'Vy', 31015, 'Vz', 21015, 'My', 11015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171015, 71015, 171015, 1015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122015, 122015, 22015, 1015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171016, 13.65, 12.75, 4.0)
    ops.node(122016, 13.65, 12.75, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1016, 171016, 122016, 0.1225, 31136101.84242232, 12973375.76767597, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21016, 88.68001739, 0.00090488, 106.96534919, 0.01549732, 10.69653492, 0.05917178, -88.68001739, -0.00090488, -106.96534919, -0.01549732, -10.69653492, -0.05917178, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11016, 77.49081727, 0.00090488, 93.46899755, 0.01549732, 9.34689976, 0.05917178, -77.49081727, -0.00090488, -93.46899755, -0.01549732, -9.34689976, -0.05917178, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21016, 1016, 0.0, 144.58168716, 0.01809765, 144.58168716, 0.05429294, 101.20718102, -1860.77240782, 0.05, 2, 0, 71016, 22016, 2, 3)
    ops.uniaxialMaterial('LimitState', 41016, 36.14542179, 8.461e-05, 108.43626537, 0.00025382, 361.45421791, 0.00084607, -36.14542179, -8.461e-05, -108.43626537, -0.00025382, -361.45421791, -0.00084607, 0.4, 0.3, 0.003, 0.0, 0.0, 21016, 2)
    ops.limitCurve('ThreePoint', 11016, 1016, 0.0, 144.58168716, 0.01809765, 144.58168716, 0.05429294, 101.20718102, -1860.77240782, 0.05, 2, 0, 71016, 22016, 1, 3)
    ops.uniaxialMaterial('LimitState', 31016, 36.14542179, 8.461e-05, 108.43626537, 0.00025382, 361.45421791, 0.00084607, -36.14542179, -8.461e-05, -108.43626537, -0.00025382, -361.45421791, -0.00084607, 0.4, 0.3, 0.003, 0.0, 0.0, 11016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1016, 99999, 'P', 41016, 'Vy', 31016, 'Vz', 21016, 'My', 11016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171016, 71016, 171016, 1016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122016, 122016, 22016, 1016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171017, 0.0, 17.0, 4.0)
    ops.node(122017, 0.0, 17.0, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1017, 171017, 122017, 0.09, 29493935.56057769, 12289139.81690737, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21017, 48.50816881, 0.00104215, 58.7896696, 0.0173758, 5.87896696, 0.06612387, -48.50816881, -0.00104215, -58.7896696, -0.0173758, -5.87896696, -0.06612387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11017, 52.77282592, 0.00104215, 63.95823788, 0.0173758, 6.39582379, 0.06612387, -52.77282592, -0.00104215, -63.95823788, -0.0173758, -6.39582379, -0.06612387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21017, 1017, 0.0, 108.40040843, 0.02084299, 108.40040843, 0.06252897, 75.8802859, -1794.52669783, 0.05, 2, 0, 71017, 22017, 2, 3)
    ops.uniaxialMaterial('LimitState', 41017, 27.10010211, 9.115e-05, 81.30030633, 0.00027345, 271.00102109, 0.00091149, -27.10010211, -9.115e-05, -81.30030633, -0.00027345, -271.00102109, -0.00091149, 0.4, 0.3, 0.003, 0.0, 0.0, 21017, 2)
    ops.limitCurve('ThreePoint', 11017, 1017, 0.0, 108.40040843, 0.02084299, 108.40040843, 0.06252897, 75.8802859, -1794.52669783, 0.05, 2, 0, 71017, 22017, 1, 3)
    ops.uniaxialMaterial('LimitState', 31017, 27.10010211, 9.115e-05, 81.30030633, 0.00027345, 271.00102109, 0.00091149, -27.10010211, -9.115e-05, -81.30030633, -0.00027345, -271.00102109, -0.00091149, 0.4, 0.3, 0.003, 0.0, 0.0, 11017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1017, 99999, 'P', 41017, 'Vy', 31017, 'Vz', 21017, 'My', 11017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171017, 71017, 171017, 1017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122017, 122017, 22017, 1017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171018, 2.95, 17.0, 4.0)
    ops.node(122018, 2.95, 17.0, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1018, 171018, 122018, 0.1225, 30597044.86677891, 12748768.69449121, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21018, 96.66623882, 0.0009643, 116.67834746, 0.0238878, 11.66783475, 0.07407086, -96.66623882, -0.0009643, -116.67834746, -0.0238878, -11.66783475, -0.07407086, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11018, 91.54247383, 0.0009643, 110.49384666, 0.0238878, 11.04938467, 0.07407086, -91.54247383, -0.0009643, -110.49384666, -0.0238878, -11.04938467, -0.07407086, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21018, 1018, 0.0, 158.39256649, 0.01928604, 158.39256649, 0.05785812, 110.87479654, -2376.90786716, 0.05, 2, 0, 71018, 22018, 2, 3)
    ops.uniaxialMaterial('LimitState', 41018, 39.59814162, 9.432e-05, 118.79442487, 0.00028297, 395.98141622, 0.00094322, -39.59814162, -9.432e-05, -118.79442487, -0.00028297, -395.98141622, -0.00094322, 0.4, 0.3, 0.003, 0.0, 0.0, 21018, 2)
    ops.limitCurve('ThreePoint', 11018, 1018, 0.0, 158.39256649, 0.01928604, 158.39256649, 0.05785812, 110.87479654, -2376.90786716, 0.05, 2, 0, 71018, 22018, 1, 3)
    ops.uniaxialMaterial('LimitState', 31018, 39.59814162, 9.432e-05, 118.79442487, 0.00028297, 395.98141622, 0.00094322, -39.59814162, -9.432e-05, -118.79442487, -0.00028297, -395.98141622, -0.00094322, 0.4, 0.3, 0.003, 0.0, 0.0, 11018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1018, 99999, 'P', 41018, 'Vy', 31018, 'Vz', 21018, 'My', 11018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171018, 71018, 171018, 1018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122018, 122018, 22018, 1018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171019, 8.3, 17.0, 4.0)
    ops.node(122019, 8.3, 17.0, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1019, 171019, 122019, 0.16, 29135056.63365114, 12139606.93068798, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21019, 144.65290439, 0.00088841, 175.1413318, 0.02137124, 17.51413318, 0.05854294, -144.65290439, -0.00088841, -175.1413318, -0.02137124, -17.51413318, -0.05854294, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11019, 144.65290439, 0.00088841, 175.1413318, 0.02137124, 17.51413318, 0.05854294, -144.65290439, -0.00088841, -175.1413318, -0.02137124, -17.51413318, -0.05854294, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21019, 1019, 0.0, 171.51258819, 0.01776815, 171.51258819, 0.05330446, 120.05881173, -2034.59235067, 0.05, 2, 0, 71019, 22019, 2, 3)
    ops.uniaxialMaterial('LimitState', 41019, 42.87814705, 8.212e-05, 128.63444114, 0.00024636, 428.78147048, 0.00082121, -42.87814705, -8.212e-05, -128.63444114, -0.00024636, -428.78147048, -0.00082121, 0.4, 0.3, 0.003, 0.0, 0.0, 21019, 2)
    ops.limitCurve('ThreePoint', 11019, 1019, 0.0, 171.51258819, 0.01776815, 171.51258819, 0.05330446, 120.05881173, -2034.59235067, 0.05, 2, 0, 71019, 22019, 1, 3)
    ops.uniaxialMaterial('LimitState', 31019, 42.87814705, 8.212e-05, 128.63444114, 0.00024636, 428.78147048, 0.00082121, -42.87814705, -8.212e-05, -128.63444114, -0.00024636, -428.78147048, -0.00082121, 0.4, 0.3, 0.003, 0.0, 0.0, 11019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1019, 99999, 'P', 41019, 'Vy', 31019, 'Vz', 21019, 'My', 11019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171019, 71019, 171019, 1019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122019, 122019, 22019, 1019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171020, 13.65, 17.0, 4.0)
    ops.node(122020, 13.65, 17.0, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1020, 171020, 122020, 0.1225, 29643926.87312956, 12351636.19713732, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21020, 88.05529519, 0.00090871, 106.58704778, 0.01631534, 10.65870478, 0.05869948, -88.05529519, -0.00090871, -106.58704778, -0.01631534, -10.65870478, -0.05869948, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11020, 76.82923448, 0.00090871, 92.99839684, 0.01631534, 9.29983968, 0.05869948, -76.82923448, -0.00090871, -92.99839684, -0.01631534, -9.29983968, -0.05869948, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21020, 1020, 0.0, 140.80964504, 0.01817416, 140.80964504, 0.05452247, 98.56675153, -1931.75254431, 0.05, 2, 0, 71020, 22020, 2, 3)
    ops.uniaxialMaterial('LimitState', 41020, 35.20241126, 8.655e-05, 105.60723378, 0.00025964, 352.02411261, 0.00086548, -35.20241126, -8.655e-05, -105.60723378, -0.00025964, -352.02411261, -0.00086548, 0.4, 0.3, 0.003, 0.0, 0.0, 21020, 2)
    ops.limitCurve('ThreePoint', 11020, 1020, 0.0, 140.80964504, 0.01817416, 140.80964504, 0.05452247, 98.56675153, -1931.75254431, 0.05, 2, 0, 71020, 22020, 1, 3)
    ops.uniaxialMaterial('LimitState', 31020, 35.20241126, 8.655e-05, 105.60723378, 0.00025964, 352.02411261, 0.00086548, -35.20241126, -8.655e-05, -105.60723378, -0.00025964, -352.02411261, -0.00086548, 0.4, 0.3, 0.003, 0.0, 0.0, 11020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1020, 99999, 'P', 41020, 'Vy', 31020, 'Vz', 21020, 'My', 11020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171020, 71020, 171020, 1020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122020, 122020, 22020, 1020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171021, 0.0, 21.25, 4.0)
    ops.node(122021, 0.0, 21.25, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1021, 171021, 122021, 0.09, 29332768.68434987, 12221986.95181245, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21021, 48.37424231, 0.00104657, 58.64762326, 0.01746316, 5.86476233, 0.06605472, -48.37424231, -0.00104657, -58.64762326, -0.01746316, -5.86476233, -0.06605472, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11021, 52.58712537, 0.00104657, 63.75520876, 0.01746316, 6.37552088, 0.06605472, -52.58712537, -0.00104657, -63.75520876, -0.01746316, -6.37552088, -0.06605472, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21021, 1021, 0.0, 108.60125639, 0.02093147, 108.60125639, 0.06279442, 76.02087947, -1825.11363042, 0.05, 2, 0, 71021, 22021, 2, 3)
    ops.uniaxialMaterial('LimitState', 41021, 27.1503141, 9.182e-05, 81.45094229, 0.00027546, 271.50314097, 0.00091819, -27.1503141, -9.182e-05, -81.45094229, -0.00027546, -271.50314097, -0.00091819, 0.4, 0.3, 0.003, 0.0, 0.0, 21021, 2)
    ops.limitCurve('ThreePoint', 11021, 1021, 0.0, 108.60125639, 0.02093147, 108.60125639, 0.06279442, 76.02087947, -1825.11363042, 0.05, 2, 0, 71021, 22021, 1, 3)
    ops.uniaxialMaterial('LimitState', 31021, 27.1503141, 9.182e-05, 81.45094229, 0.00027546, 271.50314097, 0.00091819, -27.1503141, -9.182e-05, -81.45094229, -0.00027546, -271.50314097, -0.00091819, 0.4, 0.3, 0.003, 0.0, 0.0, 11021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1021, 99999, 'P', 41021, 'Vy', 31021, 'Vz', 21021, 'My', 11021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171021, 71021, 171021, 1021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122021, 122021, 22021, 1021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171022, 2.95, 21.25, 4.0)
    ops.node(122022, 2.95, 21.25, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1022, 171022, 122022, 0.1225, 29353371.1610828, 12230571.31711783, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21022, 98.95739283, 0.00095346, 119.76307191, 0.02395482, 11.97630719, 0.07267993, -98.95739283, -0.00095346, -119.76307191, -0.02395482, -11.97630719, -0.07267993, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11022, 93.26748061, 0.00095346, 112.87686213, 0.02395482, 11.28768621, 0.07267993, -93.26748061, -0.00095346, -112.87686213, -0.02395482, -11.28768621, -0.07267993, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21022, 1022, 0.0, 152.84515633, 0.01906914, 152.84515633, 0.05720741, 106.99160943, -2338.47665998, 0.05, 2, 0, 71022, 22022, 2, 3)
    ops.uniaxialMaterial('LimitState', 41022, 38.21128908, 9.488e-05, 114.63386725, 0.00028463, 382.11289082, 0.00094875, -38.21128908, -9.488e-05, -114.63386725, -0.00028463, -382.11289082, -0.00094875, 0.4, 0.3, 0.003, 0.0, 0.0, 21022, 2)
    ops.limitCurve('ThreePoint', 11022, 1022, 0.0, 152.84515633, 0.01906914, 152.84515633, 0.05720741, 106.99160943, -2338.47665998, 0.05, 2, 0, 71022, 22022, 1, 3)
    ops.uniaxialMaterial('LimitState', 31022, 38.21128908, 9.488e-05, 114.63386725, 0.00028463, 382.11289082, 0.00094875, -38.21128908, -9.488e-05, -114.63386725, -0.00028463, -382.11289082, -0.00094875, 0.4, 0.3, 0.003, 0.0, 0.0, 11022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1022, 99999, 'P', 41022, 'Vy', 31022, 'Vz', 21022, 'My', 11022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171022, 71022, 171022, 1022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122022, 122022, 22022, 1022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171023, 8.3, 21.25, 4.0)
    ops.node(122023, 8.3, 21.25, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1023, 171023, 122023, 0.16, 30174667.91990622, 12572778.29996092, 0.00360533, 0.00234667, 0.00234667, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21023, 142.56017949, 0.00087154, 172.2422874, 0.02128153, 17.22422874, 0.05942292, -142.56017949, -0.00087154, -172.2422874, -0.02128153, -17.22422874, -0.05942292, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11023, 142.56017949, 0.00087154, 172.2422874, 0.02128153, 17.22422874, 0.05942292, -142.56017949, -0.00087154, -172.2422874, -0.02128153, -17.22422874, -0.05942292, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21023, 1023, 0.0, 176.49638871, 0.01743078, 176.49638871, 0.05229233, 123.5474721, -2033.38999764, 0.05, 2, 0, 71023, 22023, 2, 3)
    ops.uniaxialMaterial('LimitState', 41023, 44.12409718, 8.16e-05, 132.37229153, 0.00024479, 441.24097178, 0.00081596, -44.12409718, -8.16e-05, -132.37229153, -0.00024479, -441.24097178, -0.00081596, 0.4, 0.3, 0.003, 0.0, 0.0, 21023, 2)
    ops.limitCurve('ThreePoint', 11023, 1023, 0.0, 176.49638871, 0.01743078, 176.49638871, 0.05229233, 123.5474721, -2033.38999764, 0.05, 2, 0, 71023, 22023, 1, 3)
    ops.uniaxialMaterial('LimitState', 31023, 44.12409718, 8.16e-05, 132.37229153, 0.00024479, 441.24097178, 0.00081596, -44.12409718, -8.16e-05, -132.37229153, -0.00024479, -441.24097178, -0.00081596, 0.4, 0.3, 0.003, 0.0, 0.0, 11023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1023, 99999, 'P', 41023, 'Vy', 31023, 'Vz', 21023, 'My', 11023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171023, 71023, 171023, 1023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122023, 122023, 22023, 1023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171024, 13.65, 21.25, 4.0)
    ops.node(122024, 13.65, 21.25, 6.5)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1024, 171024, 122024, 0.1225, 29573095.02816795, 12322122.92840331, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21024, 90.03999857, 0.00091147, 109.00569191, 0.01620069, 10.90056919, 0.05851749, -90.03999857, -0.00091147, -109.00569191, -0.01620069, -10.90056919, -0.05851749, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11024, 78.15936403, 0.00091147, 94.62256431, 0.01620069, 9.46225643, 0.05851749, -78.15936403, -0.00091147, -94.62256431, -0.01620069, -9.46225643, -0.05851749, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21024, 1024, 0.0, 139.91614779, 0.0182294, 139.91614779, 0.0546882, 97.94130345, -1906.60896276, 0.05, 2, 0, 71024, 22024, 2, 3)
    ops.uniaxialMaterial('LimitState', 41024, 34.97903695, 8.62e-05, 104.93711084, 0.00025861, 349.79036948, 0.00086204, -34.97903695, -8.62e-05, -104.93711084, -0.00025861, -349.79036948, -0.00086204, 0.4, 0.3, 0.003, 0.0, 0.0, 21024, 2)
    ops.limitCurve('ThreePoint', 11024, 1024, 0.0, 139.91614779, 0.0182294, 139.91614779, 0.0546882, 97.94130345, -1906.60896276, 0.05, 2, 0, 71024, 22024, 1, 3)
    ops.uniaxialMaterial('LimitState', 31024, 34.97903695, 8.62e-05, 104.93711084, 0.00025861, 349.79036948, 0.00086204, -34.97903695, -8.62e-05, -104.93711084, -0.00025861, -349.79036948, -0.00086204, 0.4, 0.3, 0.003, 0.0, 0.0, 11024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1024, 99999, 'P', 41024, 'Vy', 31024, 'Vz', 21024, 'My', 11024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171024, 71024, 171024, 1024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122024, 122024, 22024, 1024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171025, 0.0, 25.5, 3.95)
    ops.node(122025, 0.0, 25.5, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1025, 171025, 122025, 0.0625, 31020624.39152125, 12925260.16313385, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21025, 28.35827324, 0.00119863, 34.26428984, 0.01798572, 3.42642898, 0.07685669, -28.35827324, -0.00119863, -34.26428984, -0.01798572, -3.42642898, -0.07685669, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11025, 28.35827324, 0.00119863, 34.26428984, 0.01798572, 3.42642898, 0.07685669, -28.35827324, -0.00119863, -34.26428984, -0.01798572, -3.42642898, -0.07685669, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21025, 1025, 0.0, 83.74195434, 0.02397257, 83.74195434, 0.0719177, 58.61936804, -1683.5653153, 0.05, 2, 0, 71025, 22025, 2, 3)
    ops.uniaxialMaterial('LimitState', 41025, 20.93548858, 9.641e-05, 62.80646575, 0.00028922, 209.35488585, 0.00096407, -20.93548858, -9.641e-05, -62.80646575, -0.00028922, -209.35488585, -0.00096407, 0.4, 0.3, 0.003, 0.0, 0.0, 21025, 2)
    ops.limitCurve('ThreePoint', 11025, 1025, 0.0, 83.74195434, 0.02397257, 83.74195434, 0.0719177, 58.61936804, -1683.5653153, 0.05, 2, 0, 71025, 22025, 1, 3)
    ops.uniaxialMaterial('LimitState', 31025, 20.93548858, 9.641e-05, 62.80646575, 0.00028922, 209.35488585, 0.00096407, -20.93548858, -9.641e-05, -62.80646575, -0.00028922, -209.35488585, -0.00096407, 0.4, 0.3, 0.003, 0.0, 0.0, 11025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1025, 99999, 'P', 41025, 'Vy', 31025, 'Vz', 21025, 'My', 11025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171025, 71025, 171025, 1025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122025, 122025, 22025, 1025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171026, 2.95, 25.5, 3.95)
    ops.node(122026, 2.95, 25.5, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1026, 171026, 122026, 0.09, 29592332.04092986, 12330138.35038744, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21026, 57.96845384, 0.00103805, 70.12318019, 0.01675176, 7.01231802, 0.06322972, -57.96845384, -0.00103805, -70.12318019, -0.01675176, -7.01231802, -0.06322972, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11026, 53.25634767, 0.00103805, 64.42304766, 0.01675176, 6.44230477, 0.06322972, -53.25634767, -0.00103805, -64.42304766, -0.01675176, -6.44230477, -0.06322972, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21026, 1026, 0.0, 111.045048, 0.02076109, 111.045048, 0.06228326, 77.7315336, -1640.13914811, 0.05, 2, 0, 71026, 22026, 2, 3)
    ops.uniaxialMaterial('LimitState', 41026, 27.761262, 9.306e-05, 83.283786, 0.00027919, 277.61262, 0.00093062, -27.761262, -9.306e-05, -83.283786, -0.00027919, -277.61262, -0.00093062, 0.4, 0.3, 0.003, 0.0, 0.0, 21026, 2)
    ops.limitCurve('ThreePoint', 11026, 1026, 0.0, 111.045048, 0.02076109, 111.045048, 0.06228326, 77.7315336, -1640.13914811, 0.05, 2, 0, 71026, 22026, 1, 3)
    ops.uniaxialMaterial('LimitState', 31026, 27.761262, 9.306e-05, 83.283786, 0.00027919, 277.61262, 0.00093062, -27.761262, -9.306e-05, -83.283786, -0.00027919, -277.61262, -0.00093062, 0.4, 0.3, 0.003, 0.0, 0.0, 11026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1026, 99999, 'P', 41026, 'Vy', 31026, 'Vz', 21026, 'My', 11026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171026, 71026, 171026, 1026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122026, 122026, 22026, 1026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171027, 8.3, 25.5, 3.95)
    ops.node(122027, 8.3, 25.5, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1027, 171027, 122027, 0.1225, 28288363.00231304, 11786817.91763043, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21027, 90.79427373, 0.00093301, 110.1382795, 0.01622439, 11.01382795, 0.05670919, -90.79427373, -0.00093301, -110.1382795, -0.01622439, -11.01382795, -0.05670919, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11027, 79.05997702, 0.00093301, 95.90395394, 0.01622439, 9.59039539, 0.05670919, -79.05997702, -0.00093301, -95.90395394, -0.01622439, -9.59039539, -0.05670919, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21027, 1027, 0.0, 136.13550325, 0.01866022, 136.13550325, 0.05598067, 95.29485227, -1887.95345682, 0.05, 2, 0, 71027, 22027, 2, 3)
    ops.uniaxialMaterial('LimitState', 41027, 34.03387581, 8.768e-05, 102.10162743, 0.00026305, 340.33875811, 0.00087684, -34.03387581, -8.768e-05, -102.10162743, -0.00026305, -340.33875811, -0.00087684, 0.4, 0.3, 0.003, 0.0, 0.0, 21027, 2)
    ops.limitCurve('ThreePoint', 11027, 1027, 0.0, 136.13550325, 0.01866022, 136.13550325, 0.05598067, 95.29485227, -1887.95345682, 0.05, 2, 0, 71027, 22027, 1, 3)
    ops.uniaxialMaterial('LimitState', 31027, 34.03387581, 8.768e-05, 102.10162743, 0.00026305, 340.33875811, 0.00087684, -34.03387581, -8.768e-05, -102.10162743, -0.00026305, -340.33875811, -0.00087684, 0.4, 0.3, 0.003, 0.0, 0.0, 11027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1027, 99999, 'P', 41027, 'Vy', 31027, 'Vz', 21027, 'My', 11027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171027, 71027, 171027, 1027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122027, 122027, 22027, 1027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171028, 13.65, 25.5, 3.95)
    ops.node(122028, 13.65, 25.5, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 1028, 171028, 122028, 0.09, 29193245.06808516, 12163852.11170215, 0.00114075, 0.0007425, 0.0007425, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 21028, 51.73325122, 0.00099847, 62.75019424, 0.01715847, 6.27501942, 0.06588558, -51.73325122, -0.00099847, -62.75019424, -0.01715847, -6.27501942, -0.06588558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 11028, 47.35892948, 0.00099847, 57.44433134, 0.01715847, 5.74443313, 0.06588558, -47.35892948, -0.00099847, -57.44433134, -0.01715847, -5.74443313, -0.06588558, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 21028, 1028, 0.0, 106.56354444, 0.01996946, 106.56354444, 0.05990837, 74.59448111, -1780.68326178, 0.05, 2, 0, 71028, 22028, 2, 3)
    ops.uniaxialMaterial('LimitState', 41028, 26.64088611, 9.053e-05, 79.92265833, 0.00027158, 266.40886109, 0.00090527, -26.64088611, -9.053e-05, -79.92265833, -0.00027158, -266.40886109, -0.00090527, 0.4, 0.3, 0.003, 0.0, 0.0, 21028, 2)
    ops.limitCurve('ThreePoint', 11028, 1028, 0.0, 106.56354444, 0.01996946, 106.56354444, 0.05990837, 74.59448111, -1780.68326178, 0.05, 2, 0, 71028, 22028, 1, 3)
    ops.uniaxialMaterial('LimitState', 31028, 26.64088611, 9.053e-05, 79.92265833, 0.00027158, 266.40886109, 0.00090527, -26.64088611, -9.053e-05, -79.92265833, -0.00027158, -266.40886109, -0.00090527, 0.4, 0.3, 0.003, 0.0, 0.0, 11028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 1028, 99999, 'P', 41028, 'Vy', 31028, 'Vz', 21028, 'My', 11028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171028, 71028, 171028, 1028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122028, 122028, 22028, 1028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172003, 8.3, 0.0, 7.05)
    ops.node(123003, 8.3, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2003, 172003, 123003, 0.0625, 30428713.35648407, 12678630.5652017, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22003, 32.84609288, 0.0012311, 39.62564625, 0.01740274, 3.96256462, 0.07062292, -32.84609288, -0.0012311, -39.62564625, -0.01740274, -3.96256462, -0.07062292, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12003, 32.84609288, 0.0012311, 39.62564625, 0.01740274, 3.96256462, 0.07062292, -32.84609288, -0.0012311, -39.62564625, -0.01740274, -3.96256462, -0.07062292, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22003, 2003, 0.0, 86.15176252, 0.02462204, 86.15176252, 0.07386611, 60.30623376, -1357.94101301, 0.05, 2, 0, 72003, 23003, 2, 3)
    ops.uniaxialMaterial('LimitState', 42003, 21.53794063, 0.00010111, 64.61382189, 0.00030333, 215.37940629, 0.0010111, -21.53794063, -0.00010111, -64.61382189, -0.00030333, -215.37940629, -0.0010111, 0.4, 0.3, 0.003, 0.0, 0.0, 22003, 2)
    ops.limitCurve('ThreePoint', 12003, 2003, 0.0, 86.15176252, 0.02462204, 86.15176252, 0.07386611, 60.30623376, -1357.94101301, 0.05, 2, 0, 72003, 23003, 1, 3)
    ops.uniaxialMaterial('LimitState', 32003, 21.53794063, 0.00010111, 64.61382189, 0.00030333, 215.37940629, 0.0010111, -21.53794063, -0.00010111, -64.61382189, -0.00030333, -215.37940629, -0.0010111, 0.4, 0.3, 0.003, 0.0, 0.0, 12003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2003, 99999, 'P', 42003, 'Vy', 32003, 'Vz', 22003, 'My', 12003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172003, 72003, 172003, 2003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123003, 123003, 23003, 2003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172004, 13.65, 0.0, 7.05)
    ops.node(123004, 13.65, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2004, 172004, 123004, 0.0625, 29284838.15243782, 12202015.89684909, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22004, 27.71299447, 0.00125123, 33.63349909, 0.01884896, 3.36334991, 0.07643295, -27.71299447, -0.00125123, -33.63349909, -0.01884896, -3.36334991, -0.07643295, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12004, 27.71299447, 0.00125123, 33.63349909, 0.01884896, 3.36334991, 0.07643295, -27.71299447, -0.00125123, -33.63349909, -0.01884896, -3.36334991, -0.07643295, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22004, 2004, 0.0, 81.49038155, 0.02502465, 81.49038155, 0.07507395, 57.04326709, -1787.03976847, 0.05, 2, 0, 72004, 23004, 2, 3)
    ops.uniaxialMaterial('LimitState', 42004, 20.37259539, 9.938e-05, 61.11778616, 0.00029813, 203.72595388, 0.00099375, -20.37259539, -9.938e-05, -61.11778616, -0.00029813, -203.72595388, -0.00099375, 0.4, 0.3, 0.003, 0.0, 0.0, 22004, 2)
    ops.limitCurve('ThreePoint', 12004, 2004, 0.0, 81.49038155, 0.02502465, 81.49038155, 0.07507395, 57.04326709, -1787.03976847, 0.05, 2, 0, 72004, 23004, 1, 3)
    ops.uniaxialMaterial('LimitState', 32004, 20.37259539, 9.938e-05, 61.11778616, 0.00029813, 203.72595388, 0.00099375, -20.37259539, -9.938e-05, -61.11778616, -0.00029813, -203.72595388, -0.00099375, 0.4, 0.3, 0.003, 0.0, 0.0, 12004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2004, 99999, 'P', 42004, 'Vy', 32004, 'Vz', 22004, 'My', 12004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172004, 72004, 172004, 2004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123004, 123004, 23004, 2004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172005, 0.0, 4.25, 7.1)
    ops.node(123005, 0.0, 4.25, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2005, 172005, 123005, 0.0625, 27840061.29149565, 11600025.53812319, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22005, 35.31748588, 0.00131613, 42.89632202, 0.01893495, 4.2896322, 0.07157602, -35.31748588, -0.00131613, -42.89632202, -0.01893495, -4.2896322, -0.07157602, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12005, 38.27872752, 0.00131613, 46.49302127, 0.01893495, 4.64930213, 0.07157602, -38.27872752, -0.00131613, -46.49302127, -0.01893495, -4.64930213, -0.07157602, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22005, 2005, 0.0, 80.15158398, 0.02632269, 80.15158398, 0.07896807, 56.10610878, -1521.3106016, 0.05, 2, 0, 72005, 23005, 2, 3)
    ops.uniaxialMaterial('LimitState', 42005, 20.03789599, 0.00010281, 60.11368798, 0.00030844, 200.37895994, 0.00102815, -20.03789599, -0.00010281, -60.11368798, -0.00030844, -200.37895994, -0.00102815, 0.4, 0.3, 0.003, 0.0, 0.0, 22005, 2)
    ops.limitCurve('ThreePoint', 12005, 2005, 0.0, 80.15158398, 0.02632269, 80.15158398, 0.07896807, 56.10610878, -1521.3106016, 0.05, 2, 0, 72005, 23005, 1, 3)
    ops.uniaxialMaterial('LimitState', 32005, 20.03789599, 0.00010281, 60.11368798, 0.00030844, 200.37895994, 0.00102815, -20.03789599, -0.00010281, -60.11368798, -0.00030844, -200.37895994, -0.00102815, 0.4, 0.3, 0.003, 0.0, 0.0, 12005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2005, 99999, 'P', 42005, 'Vy', 32005, 'Vz', 22005, 'My', 12005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172005, 72005, 172005, 2005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123005, 123005, 23005, 2005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172006, 2.95, 4.25, 7.1)
    ops.node(123006, 2.95, 4.25, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2006, 172006, 123006, 0.0625, 28895389.69429726, 12039745.70595719, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22006, 50.53022951, 0.00135468, 60.97668114, 0.01777964, 6.09766811, 0.05858129, -50.53022951, -0.00135468, -60.97668114, -0.01777964, -6.09766811, -0.05858129, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12006, 50.53022951, 0.00135468, 60.97668114, 0.01777964, 6.09766811, 0.05858129, -50.53022951, -0.00135468, -60.97668114, -0.01777964, -6.09766811, -0.05858129, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22006, 2006, 0.0, 77.24787101, 0.02709364, 77.24787101, 0.08128093, 54.07350971, -1065.09744222, 0.05, 2, 0, 72006, 23006, 2, 3)
    ops.uniaxialMaterial('LimitState', 42006, 19.31196775, 9.547e-05, 57.93590326, 0.00028641, 193.11967752, 0.00095471, -19.31196775, -9.547e-05, -57.93590326, -0.00028641, -193.11967752, -0.00095471, 0.4, 0.3, 0.003, 0.0, 0.0, 22006, 2)
    ops.limitCurve('ThreePoint', 12006, 2006, 0.0, 77.24787101, 0.02709364, 77.24787101, 0.08128093, 54.07350971, -1065.09744222, 0.05, 2, 0, 72006, 23006, 1, 3)
    ops.uniaxialMaterial('LimitState', 32006, 19.31196775, 9.547e-05, 57.93590326, 0.00028641, 193.11967752, 0.00095471, -19.31196775, -9.547e-05, -57.93590326, -0.00028641, -193.11967752, -0.00095471, 0.4, 0.3, 0.003, 0.0, 0.0, 12006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2006, 99999, 'P', 42006, 'Vy', 32006, 'Vz', 22006, 'My', 12006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172006, 72006, 172006, 2006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123006, 123006, 23006, 2006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172007, 8.3, 4.25, 7.1)
    ops.node(123007, 8.3, 4.25, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2007, 172007, 123007, 0.1225, 28198308.26073333, 11749295.10863889, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22007, 107.90056811, 0.00099734, 131.04642475, 0.01963118, 13.10464247, 0.05620242, -107.90056811, -0.00099734, -131.04642475, -0.01963118, -13.10464247, -0.05620242, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12007, 107.90056811, 0.00099734, 131.04642475, 0.01963118, 13.10464247, 0.05620242, -107.90056811, -0.00099734, -131.04642475, -0.01963118, -13.10464247, -0.05620242, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22007, 2007, 0.0, 122.22019701, 0.0199468, 122.22019701, 0.0598404, 85.55413791, -1498.42373587, 0.05, 2, 0, 72007, 23007, 2, 3)
    ops.uniaxialMaterial('LimitState', 42007, 30.55504925, 7.897e-05, 91.66514776, 0.00023692, 305.55049252, 0.00078973, -30.55504925, -7.897e-05, -91.66514776, -0.00023692, -305.55049252, -0.00078973, 0.4, 0.3, 0.003, 0.0, 0.0, 22007, 2)
    ops.limitCurve('ThreePoint', 12007, 2007, 0.0, 122.22019701, 0.0199468, 122.22019701, 0.0598404, 85.55413791, -1498.42373587, 0.05, 2, 0, 72007, 23007, 1, 3)
    ops.uniaxialMaterial('LimitState', 32007, 30.55504925, 7.897e-05, 91.66514776, 0.00023692, 305.55049252, 0.00078973, -30.55504925, -7.897e-05, -91.66514776, -0.00023692, -305.55049252, -0.00078973, 0.4, 0.3, 0.003, 0.0, 0.0, 12007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2007, 99999, 'P', 42007, 'Vy', 32007, 'Vz', 22007, 'My', 12007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172007, 72007, 172007, 2007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123007, 123007, 23007, 2007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172008, 13.65, 4.25, 7.1)
    ops.node(123008, 13.65, 4.25, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2008, 172008, 123008, 0.0625, 31794396.62053964, 13247665.25855818, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22008, 32.41794535, 0.00122298, 38.99093502, 0.01698874, 3.8990935, 0.07240253, -32.41794535, -0.00122298, -38.99093502, -0.01698874, -3.8990935, -0.07240253, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12008, 32.41794535, 0.00122298, 38.99093502, 0.01698874, 3.8990935, 0.07240253, -32.41794535, -0.00122298, -38.99093502, -0.01698874, -3.8990935, -0.07240253, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22008, 2008, 0.0, 88.10085541, 0.02445953, 88.10085541, 0.07337858, 61.67059879, -1364.7091441, 0.05, 2, 0, 72008, 23008, 2, 3)
    ops.uniaxialMaterial('LimitState', 42008, 22.02521385, 9.896e-05, 66.07564156, 0.00029687, 220.25213852, 0.00098956, -22.02521385, -9.896e-05, -66.07564156, -0.00029687, -220.25213852, -0.00098956, 0.4, 0.3, 0.003, 0.0, 0.0, 22008, 2)
    ops.limitCurve('ThreePoint', 12008, 2008, 0.0, 88.10085541, 0.02445953, 88.10085541, 0.07337858, 61.67059879, -1364.7091441, 0.05, 2, 0, 72008, 23008, 1, 3)
    ops.uniaxialMaterial('LimitState', 32008, 22.02521385, 9.896e-05, 66.07564156, 0.00029687, 220.25213852, 0.00098956, -22.02521385, -9.896e-05, -66.07564156, -0.00029687, -220.25213852, -0.00098956, 0.4, 0.3, 0.003, 0.0, 0.0, 12008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2008, 99999, 'P', 42008, 'Vy', 32008, 'Vz', 22008, 'My', 12008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172008, 72008, 172008, 2008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123008, 123008, 23008, 2008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172009, 0.0, 8.5, 7.1)
    ops.node(123009, 0.0, 8.5, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2009, 172009, 123009, 0.0625, 31213971.14753272, 13005821.31147197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22009, 34.33652087, 0.00122144, 41.4652655, 0.01892994, 4.14652655, 0.07794521, -34.33652087, -0.00122144, -41.4652655, -0.01892994, -4.14652655, -0.07794521, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12009, 37.57611887, 0.00122144, 45.3774496, 0.01892994, 4.53774496, 0.07794521, -37.57611887, -0.00122144, -45.3774496, -0.01892994, -4.53774496, -0.07794521, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22009, 2009, 0.0, 84.94455644, 0.0244288, 84.94455644, 0.07328639, 59.46118951, -1732.0419954, 0.05, 2, 0, 72009, 23009, 2, 3)
    ops.uniaxialMaterial('LimitState', 42009, 21.23613911, 9.719e-05, 63.70841733, 0.00029156, 212.3613911, 0.00097185, -21.23613911, -9.719e-05, -63.70841733, -0.00029156, -212.3613911, -0.00097185, 0.4, 0.3, 0.003, 0.0, 0.0, 22009, 2)
    ops.limitCurve('ThreePoint', 12009, 2009, 0.0, 84.94455644, 0.0244288, 84.94455644, 0.07328639, 59.46118951, -1732.0419954, 0.05, 2, 0, 72009, 23009, 1, 3)
    ops.uniaxialMaterial('LimitState', 32009, 21.23613911, 9.719e-05, 63.70841733, 0.00029156, 212.3613911, 0.00097185, -21.23613911, -9.719e-05, -63.70841733, -0.00029156, -212.3613911, -0.00097185, 0.4, 0.3, 0.003, 0.0, 0.0, 12009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2009, 99999, 'P', 42009, 'Vy', 32009, 'Vz', 22009, 'My', 12009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172009, 72009, 172009, 2009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123009, 123009, 23009, 2009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172010, 2.95, 8.5, 7.1)
    ops.node(123010, 2.95, 8.5, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2010, 172010, 123010, 0.0625, 30248916.66944319, 12603715.27893466, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22010, 48.51031174, 0.00131731, 58.50519286, 0.01791343, 5.85051929, 0.0629022, -48.51031174, -0.00131731, -58.50519286, -0.01791343, -5.85051929, -0.0629022, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12010, 48.51031174, 0.00131731, 58.50519286, 0.01791343, 5.85051929, 0.0629022, -48.51031174, -0.00131731, -58.50519286, -0.01791343, -5.85051929, -0.0629022, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22010, 2010, 0.0, 75.69897158, 0.02634627, 75.69897158, 0.07903881, 52.9892801, -1068.38975778, 0.05, 2, 0, 72010, 23010, 2, 3)
    ops.uniaxialMaterial('LimitState', 42010, 18.92474289, 8.937e-05, 56.77422868, 0.00026811, 189.24742894, 0.00089371, -18.92474289, -8.937e-05, -56.77422868, -0.00026811, -189.24742894, -0.00089371, 0.4, 0.3, 0.003, 0.0, 0.0, 22010, 2)
    ops.limitCurve('ThreePoint', 12010, 2010, 0.0, 75.69897158, 0.02634627, 75.69897158, 0.07903881, 52.9892801, -1068.38975778, 0.05, 2, 0, 72010, 23010, 1, 3)
    ops.uniaxialMaterial('LimitState', 32010, 18.92474289, 8.937e-05, 56.77422868, 0.00026811, 189.24742894, 0.00089371, -18.92474289, -8.937e-05, -56.77422868, -0.00026811, -189.24742894, -0.00089371, 0.4, 0.3, 0.003, 0.0, 0.0, 12010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2010, 99999, 'P', 42010, 'Vy', 32010, 'Vz', 22010, 'My', 12010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172010, 72010, 172010, 2010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123010, 123010, 23010, 2010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172011, 8.3, 8.5, 7.1)
    ops.node(123011, 8.3, 8.5, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2011, 172011, 123011, 0.1225, 29723133.21736702, 12384638.84056959, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22011, 106.51884037, 0.00101107, 128.983921, 0.02021048, 12.8983921, 0.05807294, -106.51884037, -0.00101107, -128.983921, -0.02021048, -12.8983921, -0.05807294, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12011, 106.51884037, 0.00101107, 128.983921, 0.02021048, 12.8983921, 0.05807294, -106.51884037, -0.00101107, -128.983921, -0.02021048, -12.8983921, -0.05807294, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22011, 2011, 0.0, 128.18868317, 0.02022146, 128.18868317, 0.06066438, 89.73207822, -1515.2105707, 0.05, 2, 0, 72011, 23011, 2, 3)
    ops.uniaxialMaterial('LimitState', 42011, 32.04717079, 7.858e-05, 96.14151238, 0.00023574, 320.47170793, 0.0007858, -32.04717079, -7.858e-05, -96.14151238, -0.00023574, -320.47170793, -0.0007858, 0.4, 0.3, 0.003, 0.0, 0.0, 22011, 2)
    ops.limitCurve('ThreePoint', 12011, 2011, 0.0, 128.18868317, 0.02022146, 128.18868317, 0.06066438, 89.73207822, -1515.2105707, 0.05, 2, 0, 72011, 23011, 1, 3)
    ops.uniaxialMaterial('LimitState', 32011, 32.04717079, 7.858e-05, 96.14151238, 0.00023574, 320.47170793, 0.0007858, -32.04717079, -7.858e-05, -96.14151238, -0.00023574, -320.47170793, -0.0007858, 0.4, 0.3, 0.003, 0.0, 0.0, 12011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2011, 99999, 'P', 42011, 'Vy', 32011, 'Vz', 22011, 'My', 12011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172011, 72011, 172011, 2011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123011, 123011, 23011, 2011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172012, 13.65, 8.5, 7.1)
    ops.node(123012, 13.65, 8.5, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2012, 172012, 123012, 0.0625, 30140039.15801616, 12558349.6491734, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22012, 31.7470577, 0.00122167, 38.33763012, 0.01783911, 3.83376301, 0.07124778, -31.7470577, -0.00122167, -38.33763012, -0.01783911, -3.83376301, -0.07124778, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12012, 31.7470577, 0.00122167, 38.33763012, 0.01783911, 3.83376301, 0.07124778, -31.7470577, -0.00122167, -38.33763012, -0.01783911, -3.83376301, -0.07124778, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22012, 2012, 0.0, 86.55461248, 0.02443337, 86.55461248, 0.07330012, 60.58822873, -1436.89170668, 0.05, 2, 0, 72012, 23012, 2, 3)
    ops.uniaxialMaterial('LimitState', 42012, 21.63865312, 0.00010256, 64.91595936, 0.00030767, 216.38653119, 0.00102556, -21.63865312, -0.00010256, -64.91595936, -0.00030767, -216.38653119, -0.00102556, 0.4, 0.3, 0.003, 0.0, 0.0, 22012, 2)
    ops.limitCurve('ThreePoint', 12012, 2012, 0.0, 86.55461248, 0.02443337, 86.55461248, 0.07330012, 60.58822873, -1436.89170668, 0.05, 2, 0, 72012, 23012, 1, 3)
    ops.uniaxialMaterial('LimitState', 32012, 21.63865312, 0.00010256, 64.91595936, 0.00030767, 216.38653119, 0.00102556, -21.63865312, -0.00010256, -64.91595936, -0.00030767, -216.38653119, -0.00102556, 0.4, 0.3, 0.003, 0.0, 0.0, 12012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2012, 99999, 'P', 42012, 'Vy', 32012, 'Vz', 22012, 'My', 12012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172012, 72012, 172012, 2012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123012, 123012, 23012, 2012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172013, 0.0, 12.75, 7.1)
    ops.node(123013, 0.0, 12.75, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2013, 172013, 123013, 0.0625, 28658988.31722701, 11941245.13217792, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22013, 34.83801388, 0.00123734, 42.3285298, 0.01902736, 4.23285298, 0.07564276, -34.83801388, -0.00123734, -42.3285298, -0.01902736, -4.23285298, -0.07564276, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12013, 38.39580716, 0.00123734, 46.65128367, 0.01902736, 4.66512837, 0.07564276, -38.39580716, -0.00123734, -46.65128367, -0.01902736, -4.66512837, -0.07564276, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22013, 2013, 0.0, 79.50939778, 0.02474672, 79.50939778, 0.07424017, 55.65657845, -1692.18003013, 0.05, 2, 0, 72013, 23013, 2, 3)
    ops.uniaxialMaterial('LimitState', 42013, 19.87734945, 9.908e-05, 59.63204834, 0.00029723, 198.77349446, 0.00099077, -19.87734945, -9.908e-05, -59.63204834, -0.00029723, -198.77349446, -0.00099077, 0.4, 0.3, 0.003, 0.0, 0.0, 22013, 2)
    ops.limitCurve('ThreePoint', 12013, 2013, 0.0, 79.50939778, 0.02474672, 79.50939778, 0.07424017, 55.65657845, -1692.18003013, 0.05, 2, 0, 72013, 23013, 1, 3)
    ops.uniaxialMaterial('LimitState', 32013, 19.87734945, 9.908e-05, 59.63204834, 0.00029723, 198.77349446, 0.00099077, -19.87734945, -9.908e-05, -59.63204834, -0.00029723, -198.77349446, -0.00099077, 0.4, 0.3, 0.003, 0.0, 0.0, 12013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2013, 99999, 'P', 42013, 'Vy', 32013, 'Vz', 22013, 'My', 12013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172013, 72013, 172013, 2013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123013, 123013, 23013, 2013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172014, 2.95, 12.75, 7.1)
    ops.node(123014, 2.95, 12.75, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2014, 172014, 123014, 0.0625, 29015982.99376784, 12089992.91406994, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22014, 48.16355258, 0.00135394, 58.21837074, 0.01822915, 5.82183707, 0.06154475, -48.16355258, -0.00135394, -58.21837074, -0.01822915, -5.82183707, -0.06154475, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12014, 48.16355258, 0.00135394, 58.21837074, 0.01822915, 5.82183707, 0.06154475, -48.16355258, -0.00135394, -58.21837074, -0.01822915, -5.82183707, -0.06154475, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22014, 2014, 0.0, 76.04160883, 0.02707875, 76.04160883, 0.08123626, 53.22912618, -1100.94579071, 0.05, 2, 0, 72014, 23014, 2, 3)
    ops.uniaxialMaterial('LimitState', 42014, 19.01040221, 9.359e-05, 57.03120662, 0.00028077, 190.10402208, 0.0009359, -19.01040221, -9.359e-05, -57.03120662, -0.00028077, -190.10402208, -0.0009359, 0.4, 0.3, 0.003, 0.0, 0.0, 22014, 2)
    ops.limitCurve('ThreePoint', 12014, 2014, 0.0, 76.04160883, 0.02707875, 76.04160883, 0.08123626, 53.22912618, -1100.94579071, 0.05, 2, 0, 72014, 23014, 1, 3)
    ops.uniaxialMaterial('LimitState', 32014, 19.01040221, 9.359e-05, 57.03120662, 0.00028077, 190.10402208, 0.0009359, -19.01040221, -9.359e-05, -57.03120662, -0.00028077, -190.10402208, -0.0009359, 0.4, 0.3, 0.003, 0.0, 0.0, 12014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2014, 99999, 'P', 42014, 'Vy', 32014, 'Vz', 22014, 'My', 12014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172014, 72014, 172014, 2014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123014, 123014, 23014, 2014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172015, 8.3, 12.75, 7.1)
    ops.node(123015, 8.3, 12.75, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2015, 172015, 123015, 0.1225, 29547375.95342891, 12311406.64726205, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22015, 109.04909185, 0.00097797, 132.09828683, 0.02358104, 13.20982868, 0.06657012, -109.04909185, -0.00097797, -132.09828683, -0.02358104, -13.20982868, -0.06657012, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12015, 109.04909185, 0.00097797, 132.09828683, 0.02358104, 13.20982868, 0.06657012, -109.04909185, -0.00097797, -132.09828683, -0.02358104, -13.20982868, -0.06657012, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22015, 2015, 0.0, 139.55649878, 0.0195594, 139.55649878, 0.05867819, 97.68954914, -1989.70173666, 0.05, 2, 0, 72015, 23015, 2, 3)
    ops.uniaxialMaterial('LimitState', 42015, 34.88912469, 8.606e-05, 104.66737408, 0.00025817, 348.89124694, 0.00086058, -34.88912469, -8.606e-05, -104.66737408, -0.00025817, -348.89124694, -0.00086058, 0.4, 0.3, 0.003, 0.0, 0.0, 22015, 2)
    ops.limitCurve('ThreePoint', 12015, 2015, 0.0, 139.55649878, 0.0195594, 139.55649878, 0.05867819, 97.68954914, -1989.70173666, 0.05, 2, 0, 72015, 23015, 1, 3)
    ops.uniaxialMaterial('LimitState', 32015, 34.88912469, 8.606e-05, 104.66737408, 0.00025817, 348.89124694, 0.00086058, -34.88912469, -8.606e-05, -104.66737408, -0.00025817, -348.89124694, -0.00086058, 0.4, 0.3, 0.003, 0.0, 0.0, 12015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2015, 99999, 'P', 42015, 'Vy', 32015, 'Vz', 22015, 'My', 12015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172015, 72015, 172015, 2015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123015, 123015, 23015, 2015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172016, 13.65, 12.75, 7.1)
    ops.node(123016, 13.65, 12.75, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2016, 172016, 123016, 0.0625, 29170535.41267037, 12154389.75527932, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22016, 32.41810187, 0.00124257, 39.22276655, 0.01749376, 3.92227665, 0.06953118, -32.41810187, -0.00124257, -39.22276655, -0.01749376, -3.92227665, -0.06953118, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12016, 32.41810187, 0.00124257, 39.22276655, 0.01749376, 3.92227665, 0.06953118, -32.41810187, -0.00124257, -39.22276655, -0.01749376, -3.92227665, -0.06953118, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22016, 2016, 0.0, 83.26257021, 0.02485135, 83.26257021, 0.07455405, 58.28379914, -1373.71923876, 0.05, 2, 0, 72016, 23016, 2, 3)
    ops.uniaxialMaterial('LimitState', 42016, 20.81564255, 0.00010193, 62.44692765, 0.0003058, 208.15642551, 0.00101934, -20.81564255, -0.00010193, -62.44692765, -0.0003058, -208.15642551, -0.00101934, 0.4, 0.3, 0.003, 0.0, 0.0, 22016, 2)
    ops.limitCurve('ThreePoint', 12016, 2016, 0.0, 83.26257021, 0.02485135, 83.26257021, 0.07455405, 58.28379914, -1373.71923876, 0.05, 2, 0, 72016, 23016, 1, 3)
    ops.uniaxialMaterial('LimitState', 32016, 20.81564255, 0.00010193, 62.44692765, 0.0003058, 208.15642551, 0.00101934, -20.81564255, -0.00010193, -62.44692765, -0.0003058, -208.15642551, -0.00101934, 0.4, 0.3, 0.003, 0.0, 0.0, 12016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2016, 99999, 'P', 42016, 'Vy', 32016, 'Vz', 22016, 'My', 12016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172016, 72016, 172016, 2016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123016, 123016, 23016, 2016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172017, 0.0, 17.0, 7.1)
    ops.node(123017, 0.0, 17.0, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2017, 172017, 123017, 0.0625, 28037298.35132778, 11682207.64638657, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22017, 27.76305462, 0.0012037, 33.77217182, 0.01853537, 3.37721718, 0.07443576, -27.76305462, -0.0012037, -33.77217182, -0.01853537, -3.37721718, -0.07443576, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12017, 27.76305462, 0.0012037, 33.77217182, 0.01853537, 3.37721718, 0.07443576, -27.76305462, -0.0012037, -33.77217182, -0.01853537, -3.37721718, -0.07443576, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22017, 2017, 0.0, 77.90689396, 0.02407392, 77.90689396, 0.07222177, 54.53482577, -1663.5153152, 0.05, 2, 0, 72017, 23017, 2, 3)
    ops.uniaxialMaterial('LimitState', 42017, 19.47672349, 9.923e-05, 58.43017047, 0.0002977, 194.76723489, 0.00099232, -19.47672349, -9.923e-05, -58.43017047, -0.0002977, -194.76723489, -0.00099232, 0.4, 0.3, 0.003, 0.0, 0.0, 22017, 2)
    ops.limitCurve('ThreePoint', 12017, 2017, 0.0, 77.90689396, 0.02407392, 77.90689396, 0.07222177, 54.53482577, -1663.5153152, 0.05, 2, 0, 72017, 23017, 1, 3)
    ops.uniaxialMaterial('LimitState', 32017, 19.47672349, 9.923e-05, 58.43017047, 0.0002977, 194.76723489, 0.00099232, -19.47672349, -9.923e-05, -58.43017047, -0.0002977, -194.76723489, -0.00099232, 0.4, 0.3, 0.003, 0.0, 0.0, 12017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2017, 99999, 'P', 42017, 'Vy', 32017, 'Vz', 22017, 'My', 12017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172017, 72017, 172017, 2017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123017, 123017, 23017, 2017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172018, 2.95, 17.0, 7.1)
    ops.node(123018, 2.95, 17.0, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2018, 172018, 123018, 0.0625, 31434178.94242973, 13097574.55934572, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22018, 49.45619966, 0.00131609, 59.48523048, 0.01752497, 5.94852305, 0.06391306, -49.45619966, -0.00131609, -59.48523048, -0.01752497, -5.94852305, -0.06391306, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12018, 49.45619966, 0.00131609, 59.48523048, 0.01752497, 5.94852305, 0.06391306, -49.45619966, -0.00131609, -59.48523048, -0.01752497, -5.94852305, -0.06391306, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22018, 2018, 0.0, 77.25091351, 0.02632173, 77.25091351, 0.07896518, 54.07563945, -1073.97729994, 0.05, 2, 0, 72018, 23018, 2, 3)
    ops.uniaxialMaterial('LimitState', 42018, 19.31272838, 8.776e-05, 57.93818513, 0.00026329, 193.12728376, 0.00087764, -19.31272838, -8.776e-05, -57.93818513, -0.00026329, -193.12728376, -0.00087764, 0.4, 0.3, 0.003, 0.0, 0.0, 22018, 2)
    ops.limitCurve('ThreePoint', 12018, 2018, 0.0, 77.25091351, 0.02632173, 77.25091351, 0.07896518, 54.07563945, -1073.97729994, 0.05, 2, 0, 72018, 23018, 1, 3)
    ops.uniaxialMaterial('LimitState', 32018, 19.31272838, 8.776e-05, 57.93818513, 0.00026329, 193.12728376, 0.00087764, -19.31272838, -8.776e-05, -57.93818513, -0.00026329, -193.12728376, -0.00087764, 0.4, 0.3, 0.003, 0.0, 0.0, 12018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2018, 99999, 'P', 42018, 'Vy', 32018, 'Vz', 22018, 'My', 12018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172018, 72018, 172018, 2018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123018, 123018, 23018, 2018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172019, 8.3, 17.0, 7.1)
    ops.node(123019, 8.3, 17.0, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2019, 172019, 123019, 0.1225, 29363664.02316358, 12234860.00965149, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22019, 109.63192596, 0.00098419, 132.85594303, 0.02327018, 13.2855943, 0.06609302, -109.63192596, -0.00098419, -132.85594303, -0.02327018, -13.2855943, -0.06609302, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12019, 109.63192596, 0.00098419, 132.85594303, 0.02327018, 13.2855943, 0.06609302, -109.63192596, -0.00098419, -132.85594303, -0.02327018, -13.2855943, -0.06609302, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22019, 2019, 0.0, 138.09750136, 0.01968378, 138.09750136, 0.05905133, 96.66825095, -1956.58841878, 0.05, 2, 0, 72019, 23019, 2, 3)
    ops.uniaxialMaterial('LimitState', 42019, 34.52437534, 8.569e-05, 103.57312602, 0.00025707, 345.24375341, 0.00085691, -34.52437534, -8.569e-05, -103.57312602, -0.00025707, -345.24375341, -0.00085691, 0.4, 0.3, 0.003, 0.0, 0.0, 22019, 2)
    ops.limitCurve('ThreePoint', 12019, 2019, 0.0, 138.09750136, 0.01968378, 138.09750136, 0.05905133, 96.66825095, -1956.58841878, 0.05, 2, 0, 72019, 23019, 1, 3)
    ops.uniaxialMaterial('LimitState', 32019, 34.52437534, 8.569e-05, 103.57312602, 0.00025707, 345.24375341, 0.00085691, -34.52437534, -8.569e-05, -103.57312602, -0.00025707, -345.24375341, -0.00085691, 0.4, 0.3, 0.003, 0.0, 0.0, 12019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2019, 99999, 'P', 42019, 'Vy', 32019, 'Vz', 22019, 'My', 12019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172019, 72019, 172019, 2019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123019, 123019, 23019, 2019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172020, 13.65, 17.0, 7.1)
    ops.node(123020, 13.65, 17.0, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2020, 172020, 123020, 0.0625, 29502791.1085671, 12292829.62856962, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22020, 42.22385559, 0.00124375, 51.05531085, 0.01859203, 5.10553108, 0.07111736, -42.22385559, -0.00124375, -51.05531085, -0.01859203, -5.10553108, -0.07111736, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12020, 38.60536771, 0.00124375, 46.67998744, 0.01859203, 4.66799874, 0.07111736, -38.60536771, -0.00124375, -46.67998744, -0.01859203, -4.66799874, -0.07111736, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22020, 2020, 0.0, 86.24030201, 0.02487503, 86.24030201, 0.0746251, 60.3682114, -1476.49085617, 0.05, 2, 0, 72020, 23020, 2, 3)
    ops.uniaxialMaterial('LimitState', 42020, 21.5600755, 0.00010439, 64.6802265, 0.00031317, 215.60075501, 0.00104391, -21.5600755, -0.00010439, -64.6802265, -0.00031317, -215.60075501, -0.00104391, 0.4, 0.3, 0.003, 0.0, 0.0, 22020, 2)
    ops.limitCurve('ThreePoint', 12020, 2020, 0.0, 86.24030201, 0.02487503, 86.24030201, 0.0746251, 60.3682114, -1476.49085617, 0.05, 2, 0, 72020, 23020, 1, 3)
    ops.uniaxialMaterial('LimitState', 32020, 21.5600755, 0.00010439, 64.6802265, 0.00031317, 215.60075501, 0.00104391, -21.5600755, -0.00010439, -64.6802265, -0.00031317, -215.60075501, -0.00104391, 0.4, 0.3, 0.003, 0.0, 0.0, 12020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2020, 99999, 'P', 42020, 'Vy', 32020, 'Vz', 22020, 'My', 12020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172020, 72020, 172020, 2020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123020, 123020, 23020, 2020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172021, 0.0, 21.25, 7.1)
    ops.node(123021, 0.0, 21.25, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2021, 172021, 123021, 0.0625, 29091600.08226525, 12121500.03427719, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22021, 34.18361788, 0.00122938, 41.49639475, 0.01881038, 4.14963948, 0.07588987, -34.18361788, -0.00122938, -41.49639475, -0.01881038, -4.14963948, -0.07588987, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12021, 37.53904492, 0.00122938, 45.56963608, 0.01881038, 4.55696361, 0.07588987, -37.53904492, -0.00122938, -45.56963608, -0.01881038, -4.55696361, -0.07588987, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22021, 2021, 0.0, 79.25740979, 0.02458767, 79.25740979, 0.073763, 55.48018685, -1630.06203129, 0.05, 2, 0, 72021, 23021, 2, 3)
    ops.uniaxialMaterial('LimitState', 42021, 19.81435245, 9.729e-05, 59.44305734, 0.00029188, 198.14352447, 0.00097294, -19.81435245, -9.729e-05, -59.44305734, -0.00029188, -198.14352447, -0.00097294, 0.4, 0.3, 0.003, 0.0, 0.0, 22021, 2)
    ops.limitCurve('ThreePoint', 12021, 2021, 0.0, 79.25740979, 0.02458767, 79.25740979, 0.073763, 55.48018685, -1630.06203129, 0.05, 2, 0, 72021, 23021, 1, 3)
    ops.uniaxialMaterial('LimitState', 32021, 19.81435245, 9.729e-05, 59.44305734, 0.00029188, 198.14352447, 0.00097294, -19.81435245, -9.729e-05, -59.44305734, -0.00029188, -198.14352447, -0.00097294, 0.4, 0.3, 0.003, 0.0, 0.0, 12021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2021, 99999, 'P', 42021, 'Vy', 32021, 'Vz', 22021, 'My', 12021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172021, 72021, 172021, 2021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123021, 123021, 23021, 2021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172022, 2.95, 21.25, 7.1)
    ops.node(123022, 2.95, 21.25, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2022, 172022, 123022, 0.0625, 28929448.73600231, 12053936.9733343, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22022, 48.52743471, 0.00130537, 58.66624631, 0.01839439, 5.86662463, 0.06158336, -48.52743471, -0.00130537, -58.66624631, -0.01839439, -5.86662463, -0.06158336, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12022, 48.52743471, 0.00130537, 58.66624631, 0.01839439, 5.86662463, 0.06158336, -48.52743471, -0.00130537, -58.66624631, -0.01839439, -5.86662463, -0.06158336, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22022, 2022, 0.0, 76.68028061, 0.02610731, 76.68028061, 0.07832192, 53.67619642, -1099.10500185, 0.05, 2, 0, 72022, 23022, 2, 3)
    ops.uniaxialMaterial('LimitState', 42022, 19.17007015, 9.466e-05, 57.51021045, 0.00028397, 191.70070151, 0.00094658, -19.17007015, -9.466e-05, -57.51021045, -0.00028397, -191.70070151, -0.00094658, 0.4, 0.3, 0.003, 0.0, 0.0, 22022, 2)
    ops.limitCurve('ThreePoint', 12022, 2022, 0.0, 76.68028061, 0.02610731, 76.68028061, 0.07832192, 53.67619642, -1099.10500185, 0.05, 2, 0, 72022, 23022, 1, 3)
    ops.uniaxialMaterial('LimitState', 32022, 19.17007015, 9.466e-05, 57.51021045, 0.00028397, 191.70070151, 0.00094658, -19.17007015, -9.466e-05, -57.51021045, -0.00028397, -191.70070151, -0.00094658, 0.4, 0.3, 0.003, 0.0, 0.0, 12022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2022, 99999, 'P', 42022, 'Vy', 32022, 'Vz', 22022, 'My', 12022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172022, 72022, 172022, 2022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123022, 123022, 23022, 2022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172023, 8.3, 21.25, 7.1)
    ops.node(123023, 8.3, 21.25, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2023, 172023, 123023, 0.1225, 29240683.46867206, 12183618.11194669, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22023, 107.94015869, 0.00097765, 130.83902855, 0.02362417, 13.08390286, 0.06633357, -107.94015869, -0.00097765, -130.83902855, -0.02362417, -13.08390286, -0.06633357, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12023, 107.94015869, 0.00097765, 130.83902855, 0.02362417, 13.08390286, 0.06633357, -107.94015869, -0.00097765, -130.83902855, -0.02362417, -13.08390286, -0.06633357, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22023, 2023, 0.0, 137.39837125, 0.0195529, 137.39837125, 0.05865871, 96.17885987, -1946.08138983, 0.05, 2, 0, 72023, 23023, 2, 3)
    ops.uniaxialMaterial('LimitState', 42023, 34.34959281, 8.562e-05, 103.04877844, 0.00025685, 343.49592812, 0.00085615, -34.34959281, -8.562e-05, -103.04877844, -0.00025685, -343.49592812, -0.00085615, 0.4, 0.3, 0.003, 0.0, 0.0, 22023, 2)
    ops.limitCurve('ThreePoint', 12023, 2023, 0.0, 137.39837125, 0.0195529, 137.39837125, 0.05865871, 96.17885987, -1946.08138983, 0.05, 2, 0, 72023, 23023, 1, 3)
    ops.uniaxialMaterial('LimitState', 32023, 34.34959281, 8.562e-05, 103.04877844, 0.00025685, 343.49592812, 0.00085615, -34.34959281, -8.562e-05, -103.04877844, -0.00025685, -343.49592812, -0.00085615, 0.4, 0.3, 0.003, 0.0, 0.0, 12023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2023, 99999, 'P', 42023, 'Vy', 32023, 'Vz', 22023, 'My', 12023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172023, 72023, 172023, 2023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123023, 123023, 23023, 2023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172024, 13.65, 21.25, 7.1)
    ops.node(123024, 13.65, 21.25, 9.6)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2024, 172024, 123024, 0.0625, 30357664.43954884, 12649026.84981202, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22024, 42.54843474, 0.00124428, 51.35697614, 0.01837399, 5.13569761, 0.07206931, -42.54843474, -0.00124428, -51.35697614, -0.01837399, -5.13569761, -0.07206931, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12024, 38.92557535, 0.00124428, 46.9840984, 0.01837399, 4.69840984, 0.07206931, -38.92557535, -0.00124428, -46.9840984, -0.01837399, -4.69840984, -0.07206931, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22024, 2024, 0.0, 88.00555872, 0.0248857, 88.00555872, 0.07465709, 61.6038911, -1482.61992581, 0.05, 2, 0, 72024, 23024, 2, 3)
    ops.uniaxialMaterial('LimitState', 42024, 22.00138968, 0.00010353, 66.00416904, 0.00031058, 220.01389679, 0.00103528, -22.00138968, -0.00010353, -66.00416904, -0.00031058, -220.01389679, -0.00103528, 0.4, 0.3, 0.003, 0.0, 0.0, 22024, 2)
    ops.limitCurve('ThreePoint', 12024, 2024, 0.0, 88.00555872, 0.0248857, 88.00555872, 0.07465709, 61.6038911, -1482.61992581, 0.05, 2, 0, 72024, 23024, 1, 3)
    ops.uniaxialMaterial('LimitState', 32024, 22.00138968, 0.00010353, 66.00416904, 0.00031058, 220.01389679, 0.00103528, -22.00138968, -0.00010353, -66.00416904, -0.00031058, -220.01389679, -0.00103528, 0.4, 0.3, 0.003, 0.0, 0.0, 12024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2024, 99999, 'P', 42024, 'Vy', 32024, 'Vz', 22024, 'My', 12024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172024, 72024, 172024, 2024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123024, 123024, 23024, 2024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172025, 0.0, 25.5, 7.05)
    ops.node(123025, 0.0, 25.5, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2025, 172025, 123025, 0.0625, 30059672.92295786, 12524863.71789911, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22025, 32.09019718, 0.00121363, 38.94359367, 0.01929389, 3.89435937, 0.08072228, -32.09019718, -0.00121363, -38.94359367, -0.01929389, -3.89435937, -0.08072228, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12025, 35.44382321, 0.00121363, 43.01344244, 0.01929389, 4.30134424, 0.08072228, -35.44382321, -0.00121363, -43.01344244, -0.01929389, -4.30134424, -0.08072228, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22025, 2025, 0.0, 79.69931528, 0.02427268, 79.69931528, 0.07281804, 55.78952069, -2289.6203457, 0.05, 2, 0, 72025, 23025, 2, 3)
    ops.uniaxialMaterial('LimitState', 42025, 19.92482882, 9.469e-05, 59.77448646, 0.00028406, 199.24828819, 0.00094686, -19.92482882, -9.469e-05, -59.77448646, -0.00028406, -199.24828819, -0.00094686, 0.4, 0.3, 0.003, 0.0, 0.0, 22025, 2)
    ops.limitCurve('ThreePoint', 12025, 2025, 0.0, 79.69931528, 0.02427268, 79.69931528, 0.07281804, 55.78952069, -2289.6203457, 0.05, 2, 0, 72025, 23025, 1, 3)
    ops.uniaxialMaterial('LimitState', 32025, 19.92482882, 9.469e-05, 59.77448646, 0.00028406, 199.24828819, 0.00094686, -19.92482882, -9.469e-05, -59.77448646, -0.00028406, -199.24828819, -0.00094686, 0.4, 0.3, 0.003, 0.0, 0.0, 12025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2025, 99999, 'P', 42025, 'Vy', 32025, 'Vz', 22025, 'My', 12025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172025, 72025, 172025, 2025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123025, 123025, 23025, 2025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172026, 2.95, 25.5, 7.05)
    ops.node(123026, 2.95, 25.5, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2026, 172026, 123026, 0.0625, 29223038.73213694, 12176266.13839039, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22026, 30.13147415, 0.00121487, 36.50970244, 0.0182397, 3.65097024, 0.07283964, -30.13147415, -0.00121487, -36.50970244, -0.0182397, -3.65097024, -0.07283964, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12026, 30.13147415, 0.00121487, 36.50970244, 0.0182397, 3.65097024, 0.07283964, -30.13147415, -0.00121487, -36.50970244, -0.0182397, -3.65097024, -0.07283964, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22026, 2026, 0.0, 82.90039609, 0.02429745, 82.90039609, 0.07289235, 58.03027726, -1535.26061157, 0.05, 2, 0, 72026, 23026, 2, 3)
    ops.uniaxialMaterial('LimitState', 42026, 20.72509902, 0.00010131, 62.17529706, 0.00030393, 207.25099021, 0.00101308, -20.72509902, -0.00010131, -62.17529706, -0.00030393, -207.25099021, -0.00101308, 0.4, 0.3, 0.003, 0.0, 0.0, 22026, 2)
    ops.limitCurve('ThreePoint', 12026, 2026, 0.0, 82.90039609, 0.02429745, 82.90039609, 0.07289235, 58.03027726, -1535.26061157, 0.05, 2, 0, 72026, 23026, 1, 3)
    ops.uniaxialMaterial('LimitState', 32026, 20.72509902, 0.00010131, 62.17529706, 0.00030393, 207.25099021, 0.00101308, -20.72509902, -0.00010131, -62.17529706, -0.00030393, -207.25099021, -0.00101308, 0.4, 0.3, 0.003, 0.0, 0.0, 12026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2026, 99999, 'P', 42026, 'Vy', 32026, 'Vz', 22026, 'My', 12026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172026, 72026, 172026, 2026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123026, 123026, 23026, 2026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172027, 8.3, 25.5, 7.05)
    ops.node(123027, 8.3, 25.5, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2027, 172027, 123027, 0.0625, 27588891.6174261, 11495371.50726088, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22027, 32.68111869, 0.00124522, 39.61528761, 0.01750508, 3.96152876, 0.06621245, -32.68111869, -0.00124522, -39.61528761, -0.01750508, -3.96152876, -0.06621245, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12027, 32.68111869, 0.00124522, 39.61528761, 0.01750508, 3.96152876, 0.06621245, -32.68111869, -0.00124522, -39.61528761, -0.01750508, -3.96152876, -0.06621245, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22027, 2027, 0.0, 81.01496772, 0.02490437, 81.01496772, 0.07471312, 56.71047741, -1365.8098615, 0.05, 2, 0, 72027, 23027, 2, 3)
    ops.uniaxialMaterial('LimitState', 42027, 20.25374193, 0.00010487, 60.76122579, 0.00031461, 202.53741931, 0.00104869, -20.25374193, -0.00010487, -60.76122579, -0.00031461, -202.53741931, -0.00104869, 0.4, 0.3, 0.003, 0.0, 0.0, 22027, 2)
    ops.limitCurve('ThreePoint', 12027, 2027, 0.0, 81.01496772, 0.02490437, 81.01496772, 0.07471312, 56.71047741, -1365.8098615, 0.05, 2, 0, 72027, 23027, 1, 3)
    ops.uniaxialMaterial('LimitState', 32027, 20.25374193, 0.00010487, 60.76122579, 0.00031461, 202.53741931, 0.00104869, -20.25374193, -0.00010487, -60.76122579, -0.00031461, -202.53741931, -0.00104869, 0.4, 0.3, 0.003, 0.0, 0.0, 12027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2027, 99999, 'P', 42027, 'Vy', 32027, 'Vz', 22027, 'My', 12027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172027, 72027, 172027, 2027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123027, 123027, 23027, 2027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172028, 13.65, 25.5, 7.05)
    ops.node(123028, 13.65, 25.5, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 2028, 172028, 123028, 0.0625, 30239701.23109622, 12599875.51295676, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 22028, 27.7583393, 0.00118995, 33.61282857, 0.01875949, 3.36128286, 0.07722996, -27.7583393, -0.00118995, -33.61282857, -0.01875949, -3.36128286, -0.07722996, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 12028, 27.7583393, 0.00118995, 33.61282857, 0.01875949, 3.36128286, 0.07722996, -27.7583393, -0.00118995, -33.61282857, -0.01875949, -3.36128286, -0.07722996, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 22028, 2028, 0.0, 82.95188657, 0.02379891, 82.95188657, 0.07139674, 58.0663206, -1767.2707537, 0.05, 2, 0, 72028, 23028, 2, 3)
    ops.uniaxialMaterial('LimitState', 42028, 20.73797164, 9.796e-05, 62.21391493, 0.00029389, 207.37971642, 0.00097963, -20.73797164, -9.796e-05, -62.21391493, -0.00029389, -207.37971642, -0.00097963, 0.4, 0.3, 0.003, 0.0, 0.0, 22028, 2)
    ops.limitCurve('ThreePoint', 12028, 2028, 0.0, 82.95188657, 0.02379891, 82.95188657, 0.07139674, 58.0663206, -1767.2707537, 0.05, 2, 0, 72028, 23028, 1, 3)
    ops.uniaxialMaterial('LimitState', 32028, 20.73797164, 9.796e-05, 62.21391493, 0.00029389, 207.37971642, 0.00097963, -20.73797164, -9.796e-05, -62.21391493, -0.00029389, -207.37971642, -0.00097963, 0.4, 0.3, 0.003, 0.0, 0.0, 12028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 2028, 99999, 'P', 42028, 'Vy', 32028, 'Vz', 22028, 'My', 12028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172028, 72028, 172028, 2028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123028, 123028, 23028, 2028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173003, 8.3, 0.0, 10.15)
    ops.node(124003, 8.3, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3003, 173003, 124003, 0.0625, 28955036.54104822, 12064598.55877009, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23003, 24.24456786, 0.00122081, 29.52512464, 0.01965439, 2.95251246, 0.081733, -24.24456786, -0.00122081, -29.52512464, -0.01965439, -2.95251246, -0.081733, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13003, 24.24456786, 0.00122081, 29.52512464, 0.01965439, 2.95251246, 0.081733, -24.24456786, -0.00122081, -29.52512464, -0.01965439, -2.95251246, -0.081733, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23003, 3003, 0.0, 77.73542159, 0.02441619, 77.73542159, 0.07324856, 54.41479511, -2845.00776652, 0.05, 2, 0, 73003, 24003, 2, 3)
    ops.uniaxialMaterial('LimitState', 43003, 19.4338554, 9.588e-05, 58.30156619, 0.00028763, 194.33855398, 0.00095876, -19.4338554, -9.588e-05, -58.30156619, -0.00028763, -194.33855398, -0.00095876, 0.4, 0.3, 0.003, 0.0, 0.0, 23003, 2)
    ops.limitCurve('ThreePoint', 13003, 3003, 0.0, 77.73542159, 0.02441619, 77.73542159, 0.07324856, 54.41479511, -2845.00776652, 0.05, 2, 0, 73003, 24003, 1, 3)
    ops.uniaxialMaterial('LimitState', 33003, 19.4338554, 9.588e-05, 58.30156619, 0.00028763, 194.33855398, 0.00095876, -19.4338554, -9.588e-05, -58.30156619, -0.00028763, -194.33855398, -0.00095876, 0.4, 0.3, 0.003, 0.0, 0.0, 13003, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3003, 99999, 'P', 43003, 'Vy', 33003, 'Vz', 23003, 'My', 13003, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173003, 73003, 173003, 3003, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124003, 124003, 24003, 3003, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173004, 13.65, 0.0, 10.15)
    ops.node(124004, 13.65, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3004, 173004, 124004, 0.0625, 29679217.27517597, 12366340.53132332, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23004, 22.71466209, 0.00112299, 27.64120968, 0.01913877, 2.76412097, 0.08361358, -22.71466209, -0.00112299, -27.64120968, -0.01913877, -2.76412097, -0.08361358, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13004, 22.71466209, 0.00112299, 27.64120968, 0.01913877, 2.76412097, 0.08361358, -22.71466209, -0.00112299, -27.64120968, -0.01913877, -2.76412097, -0.08361358, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23004, 3004, 0.0, 75.54853077, 0.02245972, 75.54853077, 0.06737916, 52.88397154, -4244.17826008, 0.05, 2, 0, 73004, 24004, 2, 3)
    ops.uniaxialMaterial('LimitState', 43004, 18.88713269, 9.09e-05, 56.66139808, 0.00027271, 188.87132692, 0.00090905, -18.88713269, -9.09e-05, -56.66139808, -0.00027271, -188.87132692, -0.00090905, 0.4, 0.3, 0.003, 0.0, 0.0, 23004, 2)
    ops.limitCurve('ThreePoint', 13004, 3004, 0.0, 75.54853077, 0.02245972, 75.54853077, 0.06737916, 52.88397154, -4244.17826008, 0.05, 2, 0, 73004, 24004, 1, 3)
    ops.uniaxialMaterial('LimitState', 33004, 18.88713269, 9.09e-05, 56.66139808, 0.00027271, 188.87132692, 0.00090905, -18.88713269, -9.09e-05, -56.66139808, -0.00027271, -188.87132692, -0.00090905, 0.4, 0.3, 0.003, 0.0, 0.0, 13004, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3004, 99999, 'P', 43004, 'Vy', 33004, 'Vz', 23004, 'My', 13004, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173004, 73004, 173004, 3004, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124004, 124004, 24004, 3004, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173005, 0.0, 4.25, 10.2)
    ops.node(124005, 0.0, 4.25, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3005, 173005, 124005, 0.0625, 27817500.66166507, 11590625.27569378, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23005, 23.45039295, 0.00122371, 28.62963614, 0.02006884, 2.86296361, 0.08133753, -23.45039295, -0.00122371, -28.62963614, -0.02006884, -2.86296361, -0.08133753, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13005, 23.45039295, 0.00122371, 28.62963614, 0.02006884, 2.86296361, 0.08133753, -23.45039295, -0.00122371, -28.62963614, -0.02006884, -2.86296361, -0.08133753, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23005, 3005, 0.0, 75.78828207, 0.02447424, 75.78828207, 0.07342271, 53.05179745, -2789.36950586, 0.05, 2, 0, 73005, 24005, 2, 3)
    ops.uniaxialMaterial('LimitState', 43005, 18.94707052, 9.73e-05, 56.84121155, 0.00029189, 189.47070517, 0.00097297, -18.94707052, -9.73e-05, -56.84121155, -0.00029189, -189.47070517, -0.00097297, 0.4, 0.3, 0.003, 0.0, 0.0, 23005, 2)
    ops.limitCurve('ThreePoint', 13005, 3005, 0.0, 75.78828207, 0.02447424, 75.78828207, 0.07342271, 53.05179745, -2789.36950586, 0.05, 2, 0, 73005, 24005, 1, 3)
    ops.uniaxialMaterial('LimitState', 33005, 18.94707052, 9.73e-05, 56.84121155, 0.00029189, 189.47070517, 0.00097297, -18.94707052, -9.73e-05, -56.84121155, -0.00029189, -189.47070517, -0.00097297, 0.4, 0.3, 0.003, 0.0, 0.0, 13005, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3005, 99999, 'P', 43005, 'Vy', 33005, 'Vz', 23005, 'My', 13005, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173005, 73005, 173005, 3005, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124005, 124005, 24005, 3005, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173006, 2.95, 4.25, 10.2)
    ops.node(124006, 2.95, 4.25, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3006, 173006, 124006, 0.0625, 29866529.81731981, 12444387.42388326, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23006, 41.6297388, 0.00128616, 50.50402602, 0.01954958, 5.0504026, 0.07140827, -41.6297388, -0.00128616, -50.50402602, -0.01954958, -5.0504026, -0.07140827, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13006, 41.6297388, 0.00128616, 50.50402602, 0.01954958, 5.0504026, 0.07140827, -41.6297388, -0.00128616, -50.50402602, -0.01954958, -5.0504026, -0.07140827, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23006, 3006, 0.0, 72.1353254, 0.02572326, 72.1353254, 0.07716978, 50.49472778, -1513.38122856, 0.05, 2, 0, 73006, 24006, 2, 3)
    ops.uniaxialMaterial('LimitState', 43006, 18.03383135, 8.625e-05, 54.10149405, 0.00025876, 180.33831351, 0.00086254, -18.03383135, -8.625e-05, -54.10149405, -0.00025876, -180.33831351, -0.00086254, 0.4, 0.3, 0.003, 0.0, 0.0, 23006, 2)
    ops.limitCurve('ThreePoint', 13006, 3006, 0.0, 72.1353254, 0.02572326, 72.1353254, 0.07716978, 50.49472778, -1513.38122856, 0.05, 2, 0, 73006, 24006, 1, 3)
    ops.uniaxialMaterial('LimitState', 33006, 18.03383135, 8.625e-05, 54.10149405, 0.00025876, 180.33831351, 0.00086254, -18.03383135, -8.625e-05, -54.10149405, -0.00025876, -180.33831351, -0.00086254, 0.4, 0.3, 0.003, 0.0, 0.0, 13006, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3006, 99999, 'P', 43006, 'Vy', 33006, 'Vz', 23006, 'My', 13006, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173006, 73006, 173006, 3006, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124006, 124006, 24006, 3006, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173007, 8.3, 4.25, 10.2)
    ops.node(124007, 8.3, 4.25, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3007, 173007, 124007, 0.1225, 29242134.9825918, 12184222.90941325, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23007, 90.46760588, 0.00095035, 110.1341079, 0.01609059, 11.01341079, 0.05131136, -90.46760588, -0.00095035, -110.1341079, -0.01609059, -11.01341079, -0.05131136, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13007, 90.46760588, 0.00095035, 110.1341079, 0.01609059, 11.01341079, 0.05131136, -90.46760588, -0.00095035, -110.1341079, -0.01609059, -11.01341079, -0.05131136, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23007, 3007, 0.0, 106.0025592, 0.01900706, 106.0025592, 0.05702117, 74.20179144, -1667.10454317, 0.05, 2, 0, 73007, 24007, 2, 3)
    ops.uniaxialMaterial('LimitState', 43007, 26.5006398, 6.605e-05, 79.5019194, 0.00019815, 265.006398, 0.00066049, -26.5006398, -6.605e-05, -79.5019194, -0.00019815, -265.006398, -0.00066049, 0.4, 0.3, 0.003, 0.0, 0.0, 23007, 2)
    ops.limitCurve('ThreePoint', 13007, 3007, 0.0, 106.0025592, 0.01900706, 106.0025592, 0.05702117, 74.20179144, -1667.10454317, 0.05, 2, 0, 73007, 24007, 1, 3)
    ops.uniaxialMaterial('LimitState', 33007, 26.5006398, 6.605e-05, 79.5019194, 0.00019815, 265.006398, 0.00066049, -26.5006398, -6.605e-05, -79.5019194, -0.00019815, -265.006398, -0.00066049, 0.4, 0.3, 0.003, 0.0, 0.0, 13007, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3007, 99999, 'P', 43007, 'Vy', 33007, 'Vz', 23007, 'My', 13007, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173007, 73007, 173007, 3007, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124007, 124007, 24007, 3007, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173008, 13.65, 4.25, 10.2)
    ops.node(124008, 13.65, 4.25, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3008, 173008, 124008, 0.0625, 29487427.62516078, 12286428.17715032, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23008, 24.30055452, 0.00115168, 29.55422387, 0.01892191, 2.95542239, 0.08128599, -24.30055452, -0.00115168, -29.55422387, -0.01892191, -2.95542239, -0.08128599, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13008, 24.30055452, 0.00115168, 29.55422387, 0.01892191, 2.95542239, 0.08128599, -24.30055452, -0.00115168, -29.55422387, -0.01892191, -2.95542239, -0.08128599, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23008, 3008, 0.0, 76.78553821, 0.02303362, 76.78553821, 0.06910087, 53.74987675, -2634.71144064, 0.05, 2, 0, 73008, 24008, 2, 3)
    ops.uniaxialMaterial('LimitState', 43008, 19.19638455, 9.299e-05, 57.58915366, 0.00027898, 191.96384552, 0.00092994, -19.19638455, -9.299e-05, -57.58915366, -0.00027898, -191.96384552, -0.00092994, 0.4, 0.3, 0.003, 0.0, 0.0, 23008, 2)
    ops.limitCurve('ThreePoint', 13008, 3008, 0.0, 76.78553821, 0.02303362, 76.78553821, 0.06910087, 53.74987675, -2634.71144064, 0.05, 2, 0, 73008, 24008, 1, 3)
    ops.uniaxialMaterial('LimitState', 33008, 19.19638455, 9.299e-05, 57.58915366, 0.00027898, 191.96384552, 0.00092994, -19.19638455, -9.299e-05, -57.58915366, -0.00027898, -191.96384552, -0.00092994, 0.4, 0.3, 0.003, 0.0, 0.0, 13008, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3008, 99999, 'P', 43008, 'Vy', 33008, 'Vz', 23008, 'My', 13008, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173008, 73008, 173008, 3008, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124008, 124008, 24008, 3008, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173009, 0.0, 8.5, 10.2)
    ops.node(124009, 0.0, 8.5, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3009, 173009, 124009, 0.0625, 29304343.46012599, 12210143.10838583, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23009, 22.89719238, 0.00117128, 27.88980385, 0.01918476, 2.78898039, 0.08344523, -22.89719238, -0.00117128, -27.88980385, -0.01918476, -2.78898039, -0.08344523, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13009, 22.89719238, 0.00117128, 27.88980385, 0.01918476, 2.78898039, 0.08344523, -22.89719238, -0.00117128, -27.88980385, -0.01918476, -2.78898039, -0.08344523, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23009, 3009, 0.0, 75.0127633, 0.02342555, 75.0127633, 0.07027665, 52.50893431, -4108.75357839, 0.05, 2, 0, 73009, 24009, 2, 3)
    ops.uniaxialMaterial('LimitState', 43009, 18.75319082, 9.141e-05, 56.25957247, 0.00027424, 187.53190824, 0.00091415, -18.75319082, -9.141e-05, -56.25957247, -0.00027424, -187.53190824, -0.00091415, 0.4, 0.3, 0.003, 0.0, 0.0, 23009, 2)
    ops.limitCurve('ThreePoint', 13009, 3009, 0.0, 75.0127633, 0.02342555, 75.0127633, 0.07027665, 52.50893431, -4108.75357839, 0.05, 2, 0, 73009, 24009, 1, 3)
    ops.uniaxialMaterial('LimitState', 33009, 18.75319082, 9.141e-05, 56.25957247, 0.00027424, 187.53190824, 0.00091415, -18.75319082, -9.141e-05, -56.25957247, -0.00027424, -187.53190824, -0.00091415, 0.4, 0.3, 0.003, 0.0, 0.0, 13009, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3009, 99999, 'P', 43009, 'Vy', 33009, 'Vz', 23009, 'My', 13009, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173009, 73009, 173009, 3009, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124009, 124009, 24009, 3009, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173010, 2.95, 8.5, 10.2)
    ops.node(124010, 2.95, 8.5, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3010, 173010, 124010, 0.0625, 29156999.72786552, 12148749.88661063, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23010, 39.09785893, 0.00130779, 47.56015254, 0.01990159, 4.75601525, 0.0728175, -39.09785893, -0.00130779, -47.56015254, -0.01990159, -4.75601525, -0.0728175, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13010, 39.09785893, 0.00130779, 47.56015254, 0.01990159, 4.75601525, 0.0728175, -39.09785893, -0.00130779, -47.56015254, -0.01990159, -4.75601525, -0.0728175, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23010, 3010, 0.0, 67.84666855, 0.02615575, 67.84666855, 0.07846726, 47.49266798, -1736.53159842, 0.05, 2, 0, 73010, 24010, 2, 3)
    ops.uniaxialMaterial('LimitState', 43010, 16.96166714, 8.31e-05, 50.88500141, 0.0002493, 169.61667137, 0.000831, -16.96166714, -8.31e-05, -50.88500141, -0.0002493, -169.61667137, -0.000831, 0.4, 0.3, 0.003, 0.0, 0.0, 23010, 2)
    ops.limitCurve('ThreePoint', 13010, 3010, 0.0, 67.84666855, 0.02615575, 67.84666855, 0.07846726, 47.49266798, -1736.53159842, 0.05, 2, 0, 73010, 24010, 1, 3)
    ops.uniaxialMaterial('LimitState', 33010, 16.96166714, 8.31e-05, 50.88500141, 0.0002493, 169.61667137, 0.000831, -16.96166714, -8.31e-05, -50.88500141, -0.0002493, -169.61667137, -0.000831, 0.4, 0.3, 0.003, 0.0, 0.0, 13010, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3010, 99999, 'P', 43010, 'Vy', 33010, 'Vz', 23010, 'My', 13010, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173010, 73010, 173010, 3010, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124010, 124010, 24010, 3010, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173011, 8.3, 8.5, 10.2)
    ops.node(124011, 8.3, 8.5, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3011, 173011, 124011, 0.1225, 29607508.99708243, 12336462.08211768, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23011, 91.06234929, 0.0009642, 110.75348505, 0.01629449, 11.07534851, 0.05160415, -91.06234929, -0.0009642, -110.75348505, -0.01629449, -11.07534851, -0.05160415, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13011, 91.06234929, 0.0009642, 110.75348505, 0.01629449, 11.07534851, 0.05160415, -91.06234929, -0.0009642, -110.75348505, -0.01629449, -11.07534851, -0.05160415, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23011, 3011, 0.0, 106.59970263, 0.0192841, 106.59970263, 0.0578523, 74.61979184, -1619.47320614, 0.05, 2, 0, 73011, 24011, 2, 3)
    ops.uniaxialMaterial('LimitState', 43011, 26.64992566, 6.56e-05, 79.94977697, 0.0001968, 266.49925657, 0.00065601, -26.64992566, -6.56e-05, -79.94977697, -0.0001968, -266.49925657, -0.00065601, 0.4, 0.3, 0.003, 0.0, 0.0, 23011, 2)
    ops.limitCurve('ThreePoint', 13011, 3011, 0.0, 106.59970263, 0.0192841, 106.59970263, 0.0578523, 74.61979184, -1619.47320614, 0.05, 2, 0, 73011, 24011, 1, 3)
    ops.uniaxialMaterial('LimitState', 33011, 26.64992566, 6.56e-05, 79.94977697, 0.0001968, 266.49925657, 0.00065601, -26.64992566, -6.56e-05, -79.94977697, -0.0001968, -266.49925657, -0.00065601, 0.4, 0.3, 0.003, 0.0, 0.0, 13011, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3011, 99999, 'P', 43011, 'Vy', 33011, 'Vz', 23011, 'My', 13011, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173011, 73011, 173011, 3011, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124011, 124011, 24011, 3011, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173012, 13.65, 8.5, 10.2)
    ops.node(124012, 13.65, 8.5, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3012, 173012, 124012, 0.0625, 31247713.66914677, 13019880.69547782, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23012, 24.3503515, 0.00115567, 29.46941776, 0.01842816, 2.94694178, 0.08157387, -24.3503515, -0.00115567, -29.46941776, -0.01842816, -2.94694178, -0.08157387, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13012, 24.3503515, 0.00115567, 29.46941776, 0.01842816, 2.94694178, 0.08157387, -24.3503515, -0.00115567, -29.46941776, -0.01842816, -2.94694178, -0.08157387, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23012, 3012, 0.0, 80.0871043, 0.02311339, 80.0871043, 0.06934018, 56.06097301, -2636.97298868, 0.05, 2, 0, 73012, 24012, 2, 3)
    ops.uniaxialMaterial('LimitState', 43012, 20.02177607, 9.153e-05, 60.06532822, 0.00027459, 200.21776075, 0.00091529, -20.02177607, -9.153e-05, -60.06532822, -0.00027459, -200.21776075, -0.00091529, 0.4, 0.3, 0.003, 0.0, 0.0, 23012, 2)
    ops.limitCurve('ThreePoint', 13012, 3012, 0.0, 80.0871043, 0.02311339, 80.0871043, 0.06934018, 56.06097301, -2636.97298868, 0.05, 2, 0, 73012, 24012, 1, 3)
    ops.uniaxialMaterial('LimitState', 33012, 20.02177607, 9.153e-05, 60.06532822, 0.00027459, 200.21776075, 0.00091529, -20.02177607, -9.153e-05, -60.06532822, -0.00027459, -200.21776075, -0.00091529, 0.4, 0.3, 0.003, 0.0, 0.0, 13012, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3012, 99999, 'P', 43012, 'Vy', 33012, 'Vz', 23012, 'My', 13012, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173012, 73012, 173012, 3012, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124012, 124012, 24012, 3012, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173013, 0.0, 12.75, 10.2)
    ops.node(124013, 0.0, 12.75, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3013, 173013, 124013, 0.0625, 28440869.5059365, 11850362.29414021, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23013, 22.64241369, 0.00115843, 27.6397467, 0.02023016, 2.76397467, 0.08421558, -22.64241369, -0.00115843, -27.6397467, -0.02023016, -2.76397467, -0.08421558, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13013, 22.64241369, 0.00115843, 27.6397467, 0.02023016, 2.76397467, 0.08421558, -22.64241369, -0.00115843, -27.6397467, -0.02023016, -2.76397467, -0.08421558, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23013, 3013, 0.0, 75.57636051, 0.02316852, 75.57636051, 0.06950557, 52.90345236, -4504.40736503, 0.05, 2, 0, 73013, 24013, 2, 3)
    ops.uniaxialMaterial('LimitState', 43013, 18.89409013, 9.49e-05, 56.68227038, 0.00028469, 188.94090128, 0.00094898, -18.89409013, -9.49e-05, -56.68227038, -0.00028469, -188.94090128, -0.00094898, 0.4, 0.3, 0.003, 0.0, 0.0, 23013, 2)
    ops.limitCurve('ThreePoint', 13013, 3013, 0.0, 75.57636051, 0.02316852, 75.57636051, 0.06950557, 52.90345236, -4504.40736503, 0.05, 2, 0, 73013, 24013, 1, 3)
    ops.uniaxialMaterial('LimitState', 33013, 18.89409013, 9.49e-05, 56.68227038, 0.00028469, 188.94090128, 0.00094898, -18.89409013, -9.49e-05, -56.68227038, -0.00028469, -188.94090128, -0.00094898, 0.4, 0.3, 0.003, 0.0, 0.0, 13013, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3013, 99999, 'P', 43013, 'Vy', 33013, 'Vz', 23013, 'My', 13013, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173013, 73013, 173013, 3013, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124013, 124013, 24013, 3013, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173014, 2.95, 12.75, 10.2)
    ops.node(124014, 2.95, 12.75, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3014, 173014, 124014, 0.0625, 29066461.71069028, 12111025.71278762, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23014, 40.16526134, 0.00126101, 48.86915623, 0.01999272, 4.88691562, 0.07285768, -40.16526134, -0.00126101, -48.86915623, -0.01999272, -4.88691562, -0.07285768, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13014, 40.16526134, 0.00126101, 48.86915623, 0.01999272, 4.88691562, 0.07285768, -40.16526134, -0.00126101, -48.86915623, -0.01999272, -4.88691562, -0.07285768, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23014, 3014, 0.0, 67.99787749, 0.02522017, 67.99787749, 0.07566051, 47.59851425, -1704.04648123, 0.05, 2, 0, 73014, 24014, 2, 3)
    ops.uniaxialMaterial('LimitState', 43014, 16.99946937, 8.354e-05, 50.99840812, 0.00025063, 169.99469373, 0.00083544, -16.99946937, -8.354e-05, -50.99840812, -0.00025063, -169.99469373, -0.00083544, 0.4, 0.3, 0.003, 0.0, 0.0, 23014, 2)
    ops.limitCurve('ThreePoint', 13014, 3014, 0.0, 67.99787749, 0.02522017, 67.99787749, 0.07566051, 47.59851425, -1704.04648123, 0.05, 2, 0, 73014, 24014, 1, 3)
    ops.uniaxialMaterial('LimitState', 33014, 16.99946937, 8.354e-05, 50.99840812, 0.00025063, 169.99469373, 0.00083544, -16.99946937, -8.354e-05, -50.99840812, -0.00025063, -169.99469373, -0.00083544, 0.4, 0.3, 0.003, 0.0, 0.0, 13014, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3014, 99999, 'P', 43014, 'Vy', 33014, 'Vz', 23014, 'My', 13014, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173014, 73014, 173014, 3014, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124014, 124014, 24014, 3014, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173015, 8.3, 12.75, 10.2)
    ops.node(124015, 8.3, 12.75, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3015, 173015, 124015, 0.1225, 28002062.98764221, 11667526.24485092, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23015, 90.10046536, 0.00097543, 110.0113166, 0.01612212, 11.00113166, 0.05100426, -90.10046536, -0.00097543, -110.0113166, -0.01612212, -11.00113166, -0.05100426, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13015, 90.10046536, 0.00097543, 110.0113166, 0.01612212, 11.00113166, 0.05100426, -90.10046536, -0.00097543, -110.0113166, -0.01612212, -11.00113166, -0.05100426, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23015, 3015, 0.0, 100.24164462, 0.01950855, 100.24164462, 0.05852565, 70.16915123, -1573.20145036, 0.05, 2, 0, 73015, 24015, 2, 3)
    ops.uniaxialMaterial('LimitState', 43015, 25.06041116, 6.523e-05, 75.18123347, 0.00019568, 250.60411155, 0.00065225, -25.06041116, -6.523e-05, -75.18123347, -0.00019568, -250.60411155, -0.00065225, 0.4, 0.3, 0.003, 0.0, 0.0, 23015, 2)
    ops.limitCurve('ThreePoint', 13015, 3015, 0.0, 100.24164462, 0.01950855, 100.24164462, 0.05852565, 70.16915123, -1573.20145036, 0.05, 2, 0, 73015, 24015, 1, 3)
    ops.uniaxialMaterial('LimitState', 33015, 25.06041116, 6.523e-05, 75.18123347, 0.00019568, 250.60411155, 0.00065225, -25.06041116, -6.523e-05, -75.18123347, -0.00019568, -250.60411155, -0.00065225, 0.4, 0.3, 0.003, 0.0, 0.0, 13015, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3015, 99999, 'P', 43015, 'Vy', 33015, 'Vz', 23015, 'My', 13015, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173015, 73015, 173015, 3015, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124015, 124015, 24015, 3015, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173016, 13.65, 12.75, 10.2)
    ops.node(124016, 13.65, 12.75, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3016, 173016, 124016, 0.0625, 30064246.19062177, 12526769.24609241, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23016, 23.9551252, 0.0012167, 29.08981928, 0.01858619, 2.90898193, 0.08122728, -23.9551252, -0.0012167, -29.08981928, -0.01858619, -2.90898193, -0.08122728, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13016, 23.9551252, 0.0012167, 29.08981928, 0.01858619, 2.90898193, 0.08122728, -23.9551252, -0.0012167, -29.08981928, -0.01858619, -2.90898193, -0.08122728, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23016, 3016, 0.0, 76.93332036, 0.02433409, 76.93332036, 0.07300228, 53.85332425, -2535.16109713, 0.05, 2, 0, 73016, 24016, 2, 3)
    ops.uniaxialMaterial('LimitState', 43016, 19.23333009, 9.139e-05, 57.69999027, 0.00027416, 192.33330089, 0.00091386, -19.23333009, -9.139e-05, -57.69999027, -0.00027416, -192.33330089, -0.00091386, 0.4, 0.3, 0.003, 0.0, 0.0, 23016, 2)
    ops.limitCurve('ThreePoint', 13016, 3016, 0.0, 76.93332036, 0.02433409, 76.93332036, 0.07300228, 53.85332425, -2535.16109713, 0.05, 2, 0, 73016, 24016, 1, 3)
    ops.uniaxialMaterial('LimitState', 33016, 19.23333009, 9.139e-05, 57.69999027, 0.00027416, 192.33330089, 0.00091386, -19.23333009, -9.139e-05, -57.69999027, -0.00027416, -192.33330089, -0.00091386, 0.4, 0.3, 0.003, 0.0, 0.0, 13016, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3016, 99999, 'P', 43016, 'Vy', 33016, 'Vz', 23016, 'My', 13016, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173016, 73016, 173016, 3016, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124016, 124016, 24016, 3016, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173017, 0.0, 17.0, 10.2)
    ops.node(124017, 0.0, 17.0, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3017, 173017, 124017, 0.0625, 29855066.03650594, 12439610.84854414, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23017, 22.34722911, 0.00113236, 27.17946042, 0.01913411, 2.71794604, 0.08355301, -22.34722911, -0.00113236, -27.17946042, -0.01913411, -2.71794604, -0.08355301, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13017, 22.34722911, 0.00113236, 27.17946042, 0.01913411, 2.71794604, 0.08355301, -22.34722911, -0.00113236, -27.17946042, -0.01913411, -2.71794604, -0.08355301, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23017, 3017, 0.0, 75.80559158, 0.0226471, 75.80559158, 0.06794131, 53.06391411, -4069.88839895, 0.05, 2, 0, 73017, 24017, 2, 3)
    ops.uniaxialMaterial('LimitState', 43017, 18.9513979, 9.068e-05, 56.85419369, 0.00027203, 189.51397896, 0.00090677, -18.9513979, -9.068e-05, -56.85419369, -0.00027203, -189.51397896, -0.00090677, 0.4, 0.3, 0.003, 0.0, 0.0, 23017, 2)
    ops.limitCurve('ThreePoint', 13017, 3017, 0.0, 75.80559158, 0.0226471, 75.80559158, 0.06794131, 53.06391411, -4069.88839895, 0.05, 2, 0, 73017, 24017, 1, 3)
    ops.uniaxialMaterial('LimitState', 33017, 18.9513979, 9.068e-05, 56.85419369, 0.00027203, 189.51397896, 0.00090677, -18.9513979, -9.068e-05, -56.85419369, -0.00027203, -189.51397896, -0.00090677, 0.4, 0.3, 0.003, 0.0, 0.0, 13017, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3017, 99999, 'P', 43017, 'Vy', 33017, 'Vz', 23017, 'My', 13017, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173017, 73017, 173017, 3017, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124017, 124017, 24017, 3017, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173018, 2.95, 17.0, 10.2)
    ops.node(124018, 2.95, 17.0, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3018, 173018, 124018, 0.0625, 28802750.10365355, 12001145.87652231, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23018, 39.25882546, 0.00128254, 47.79580045, 0.01983022, 4.77958004, 0.07254312, -39.25882546, -0.00128254, -47.79580045, -0.01983022, -4.77958004, -0.07254312, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13018, 39.25882546, 0.00128254, 47.79580045, 0.01983022, 4.77958004, 0.07254312, -39.25882546, -0.00128254, -47.79580045, -0.01983022, -4.77958004, -0.07254312, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23018, 3018, 0.0, 65.36103926, 0.02565087, 65.36103926, 0.07695262, 45.75272748, -1686.18679271, 0.05, 2, 0, 73018, 24018, 2, 3)
    ops.uniaxialMaterial('LimitState', 43018, 16.34025982, 8.104e-05, 49.02077945, 0.00024312, 163.40259816, 0.0008104, -16.34025982, -8.104e-05, -49.02077945, -0.00024312, -163.40259816, -0.0008104, 0.4, 0.3, 0.003, 0.0, 0.0, 23018, 2)
    ops.limitCurve('ThreePoint', 13018, 3018, 0.0, 65.36103926, 0.02565087, 65.36103926, 0.07695262, 45.75272748, -1686.18679271, 0.05, 2, 0, 73018, 24018, 1, 3)
    ops.uniaxialMaterial('LimitState', 33018, 16.34025982, 8.104e-05, 49.02077945, 0.00024312, 163.40259816, 0.0008104, -16.34025982, -8.104e-05, -49.02077945, -0.00024312, -163.40259816, -0.0008104, 0.4, 0.3, 0.003, 0.0, 0.0, 13018, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3018, 99999, 'P', 43018, 'Vy', 33018, 'Vz', 23018, 'My', 13018, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173018, 73018, 173018, 3018, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124018, 124018, 24018, 3018, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173019, 8.3, 17.0, 10.2)
    ops.node(124019, 8.3, 17.0, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3019, 173019, 124019, 0.1225, 29308508.27293496, 12211878.44705623, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23019, 92.2167432, 0.00094337, 112.2445118, 0.01572979, 11.22445118, 0.05096705, -92.2167432, -0.00094337, -112.2445118, -0.01572979, -11.22445118, -0.05096705, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13019, 92.2167432, 0.00094337, 112.2445118, 0.01572979, 11.22445118, 0.05096705, -92.2167432, -0.00094337, -112.2445118, -0.01572979, -11.22445118, -0.05096705, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23019, 3019, 0.0, 104.70561782, 0.01886743, 104.70561782, 0.05660229, 73.29393247, -1564.95113093, 0.05, 2, 0, 73019, 24019, 2, 3)
    ops.uniaxialMaterial('LimitState', 43019, 26.17640445, 6.509e-05, 78.52921336, 0.00019528, 261.76404454, 0.00065093, -26.17640445, -6.509e-05, -78.52921336, -0.00019528, -261.76404454, -0.00065093, 0.4, 0.3, 0.003, 0.0, 0.0, 23019, 2)
    ops.limitCurve('ThreePoint', 13019, 3019, 0.0, 104.70561782, 0.01886743, 104.70561782, 0.05660229, 73.29393247, -1564.95113093, 0.05, 2, 0, 73019, 24019, 1, 3)
    ops.uniaxialMaterial('LimitState', 33019, 26.17640445, 6.509e-05, 78.52921336, 0.00019528, 261.76404454, 0.00065093, -26.17640445, -6.509e-05, -78.52921336, -0.00019528, -261.76404454, -0.00065093, 0.4, 0.3, 0.003, 0.0, 0.0, 13019, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3019, 99999, 'P', 43019, 'Vy', 33019, 'Vz', 23019, 'My', 13019, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173019, 73019, 173019, 3019, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124019, 124019, 24019, 3019, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173020, 13.65, 17.0, 10.2)
    ops.node(124020, 13.65, 17.0, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3020, 173020, 124020, 0.0625, 29822002.39648008, 12425834.3318667, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23020, 24.34704412, 0.00114297, 29.58496003, 0.01916067, 2.958496, 0.0816881, -24.34704412, -0.00114297, -29.58496003, -0.01916067, -2.958496, -0.0816881, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13020, 24.34704412, 0.00114297, 29.58496003, 0.01916067, 2.958496, 0.0816881, -24.34704412, -0.00114297, -29.58496003, -0.01916067, -2.958496, -0.0816881, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23020, 3020, 0.0, 77.78157177, 0.0228594, 77.78157177, 0.0685782, 54.44710024, -2676.90345968, 0.05, 2, 0, 73020, 24020, 2, 3)
    ops.uniaxialMaterial('LimitState', 43020, 19.44539294, 9.314e-05, 58.33617883, 0.00027943, 194.45392943, 0.00093144, -19.44539294, -9.314e-05, -58.33617883, -0.00027943, -194.45392943, -0.00093144, 0.4, 0.3, 0.003, 0.0, 0.0, 23020, 2)
    ops.limitCurve('ThreePoint', 13020, 3020, 0.0, 77.78157177, 0.0228594, 77.78157177, 0.0685782, 54.44710024, -2676.90345968, 0.05, 2, 0, 73020, 24020, 1, 3)
    ops.uniaxialMaterial('LimitState', 33020, 19.44539294, 9.314e-05, 58.33617883, 0.00027943, 194.45392943, 0.00093144, -19.44539294, -9.314e-05, -58.33617883, -0.00027943, -194.45392943, -0.00093144, 0.4, 0.3, 0.003, 0.0, 0.0, 13020, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3020, 99999, 'P', 43020, 'Vy', 33020, 'Vz', 23020, 'My', 13020, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173020, 73020, 173020, 3020, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124020, 124020, 24020, 3020, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173021, 0.0, 21.25, 10.2)
    ops.node(124021, 0.0, 21.25, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3021, 173021, 124021, 0.0625, 29864763.85110749, 12443651.60462812, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23021, 23.00686304, 0.00114337, 27.98097781, 0.01930752, 2.79809778, 0.08372909, -23.00686304, -0.00114337, -27.98097781, -0.01930752, -2.79809778, -0.08372909, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13021, 23.00686304, 0.00114337, 27.98097781, 0.01930752, 2.79809778, 0.08372909, -23.00686304, -0.00114337, -27.98097781, -0.01930752, -2.79809778, -0.08372909, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23021, 3021, 0.0, 77.01076729, 0.02286735, 77.01076729, 0.06860206, 53.9075371, -4288.63819126, 0.05, 2, 0, 73021, 24021, 2, 3)
    ops.uniaxialMaterial('LimitState', 43021, 19.25269182, 9.209e-05, 57.75807547, 0.00027627, 192.52691822, 0.00092089, -19.25269182, -9.209e-05, -57.75807547, -0.00027627, -192.52691822, -0.00092089, 0.4, 0.3, 0.003, 0.0, 0.0, 23021, 2)
    ops.limitCurve('ThreePoint', 13021, 3021, 0.0, 77.01076729, 0.02286735, 77.01076729, 0.06860206, 53.9075371, -4288.63819126, 0.05, 2, 0, 73021, 24021, 1, 3)
    ops.uniaxialMaterial('LimitState', 33021, 19.25269182, 9.209e-05, 57.75807547, 0.00027627, 192.52691822, 0.00092089, -19.25269182, -9.209e-05, -57.75807547, -0.00027627, -192.52691822, -0.00092089, 0.4, 0.3, 0.003, 0.0, 0.0, 13021, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3021, 99999, 'P', 43021, 'Vy', 33021, 'Vz', 23021, 'My', 13021, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173021, 73021, 173021, 3021, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124021, 124021, 24021, 3021, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173022, 2.95, 21.25, 10.2)
    ops.node(124022, 2.95, 21.25, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3022, 173022, 124022, 0.0625, 28663243.73848553, 11943018.22436897, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23022, 40.33725271, 0.0012793, 49.12440373, 0.01995501, 4.91244037, 0.07258518, -40.33725271, -0.0012793, -49.12440373, -0.01995501, -4.91244037, -0.07258518, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13022, 40.33725271, 0.0012793, 49.12440373, 0.01995501, 4.91244037, 0.07258518, -40.33725271, -0.0012793, -49.12440373, -0.01995501, -4.91244037, -0.07258518, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23022, 3022, 0.0, 67.3867792, 0.02558601, 67.3867792, 0.07675802, 47.17074544, -1760.70204032, 0.05, 2, 0, 73022, 24022, 2, 3)
    ops.uniaxialMaterial('LimitState', 43022, 16.8466948, 8.396e-05, 50.5400844, 0.00025187, 168.466948, 0.00083958, -16.8466948, -8.396e-05, -50.5400844, -0.00025187, -168.466948, -0.00083958, 0.4, 0.3, 0.003, 0.0, 0.0, 23022, 2)
    ops.limitCurve('ThreePoint', 13022, 3022, 0.0, 67.3867792, 0.02558601, 67.3867792, 0.07675802, 47.17074544, -1760.70204032, 0.05, 2, 0, 73022, 24022, 1, 3)
    ops.uniaxialMaterial('LimitState', 33022, 16.8466948, 8.396e-05, 50.5400844, 0.00025187, 168.466948, 0.00083958, -16.8466948, -8.396e-05, -50.5400844, -0.00025187, -168.466948, -0.00083958, 0.4, 0.3, 0.003, 0.0, 0.0, 13022, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3022, 99999, 'P', 43022, 'Vy', 33022, 'Vz', 23022, 'My', 13022, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173022, 73022, 173022, 3022, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124022, 124022, 24022, 3022, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173023, 8.3, 21.25, 10.2)
    ops.node(124023, 8.3, 21.25, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3023, 173023, 124023, 0.1225, 30559715.08953976, 12733214.62064156, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23023, 89.36999612, 0.00097075, 108.41034098, 0.01561967, 10.8410341, 0.05114089, -89.36999612, -0.00097075, -108.41034098, -0.01561967, -10.8410341, -0.05114089, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13023, 89.36999612, 0.00097075, 108.41034098, 0.01561967, 10.8410341, 0.05114089, -89.36999612, -0.00097075, -108.41034098, -0.01561967, -10.8410341, -0.05114089, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23023, 3023, 0.0, 109.24201191, 0.01941491, 109.24201191, 0.05824474, 76.46940833, -1565.80875392, 0.05, 2, 0, 73023, 24023, 2, 3)
    ops.uniaxialMaterial('LimitState', 43023, 27.31050298, 6.513e-05, 81.93150893, 0.0001954, 273.10502976, 0.00065133, -27.31050298, -6.513e-05, -81.93150893, -0.0001954, -273.10502976, -0.00065133, 0.4, 0.3, 0.003, 0.0, 0.0, 23023, 2)
    ops.limitCurve('ThreePoint', 13023, 3023, 0.0, 109.24201191, 0.01941491, 109.24201191, 0.05824474, 76.46940833, -1565.80875392, 0.05, 2, 0, 73023, 24023, 1, 3)
    ops.uniaxialMaterial('LimitState', 33023, 27.31050298, 6.513e-05, 81.93150893, 0.0001954, 273.10502976, 0.00065133, -27.31050298, -6.513e-05, -81.93150893, -0.0001954, -273.10502976, -0.00065133, 0.4, 0.3, 0.003, 0.0, 0.0, 13023, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3023, 99999, 'P', 43023, 'Vy', 33023, 'Vz', 23023, 'My', 13023, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173023, 73023, 173023, 3023, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124023, 124023, 24023, 3023, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173024, 13.65, 21.25, 10.2)
    ops.node(124024, 13.65, 21.25, 12.75)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3024, 173024, 124024, 0.0625, 30179067.18952144, 12574611.32896727, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23024, 23.83120256, 0.0011807, 28.93026627, 0.01933531, 2.89302663, 0.08202896, -23.83120256, -0.0011807, -28.93026627, -0.01933531, -2.89302663, -0.08202896, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13024, 23.83120256, 0.0011807, 28.93026627, 0.01933531, 2.89302663, 0.08202896, -23.83120256, -0.0011807, -28.93026627, -0.01933531, -2.89302663, -0.08202896, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23024, 3024, 0.0, 79.37927622, 0.02361408, 79.37927622, 0.07084224, 55.56549335, -2781.86013633, 0.05, 2, 0, 73024, 24024, 2, 3)
    ops.uniaxialMaterial('LimitState', 43024, 19.84481905, 9.393e-05, 59.53445716, 0.0002818, 198.44819055, 0.00093932, -19.84481905, -9.393e-05, -59.53445716, -0.0002818, -198.44819055, -0.00093932, 0.4, 0.3, 0.003, 0.0, 0.0, 23024, 2)
    ops.limitCurve('ThreePoint', 13024, 3024, 0.0, 79.37927622, 0.02361408, 79.37927622, 0.07084224, 55.56549335, -2781.86013633, 0.05, 2, 0, 73024, 24024, 1, 3)
    ops.uniaxialMaterial('LimitState', 33024, 19.84481905, 9.393e-05, 59.53445716, 0.0002818, 198.44819055, 0.00093932, -19.84481905, -9.393e-05, -59.53445716, -0.0002818, -198.44819055, -0.00093932, 0.4, 0.3, 0.003, 0.0, 0.0, 13024, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3024, 99999, 'P', 43024, 'Vy', 33024, 'Vz', 23024, 'My', 13024, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173024, 73024, 173024, 3024, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124024, 124024, 24024, 3024, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173025, 0.0, 25.5, 10.15)
    ops.node(124025, 0.0, 25.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3025, 173025, 124025, 0.0625, 28529746.39561564, 11887394.33150652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23025, 22.07093453, 0.00114779, 26.95421509, 0.01976333, 2.69542151, 0.08505939, -22.07093453, -0.00114779, -26.95421509, -0.01976333, -2.69542151, -0.08505939, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13025, 22.07093453, 0.00114779, 26.95421509, 0.01976333, 2.69542151, 0.08505939, -22.07093453, -0.00114779, -26.95421509, -0.01976333, -2.69542151, -0.08505939, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23025, 3025, 0.0, 74.02060184, 0.02295574, 74.02060184, 0.06886722, 51.81442129, -7234.08325948, 0.05, 2, 0, 73025, 24025, 2, 3)
    ops.uniaxialMaterial('LimitState', 43025, 18.50515046, 9.266e-05, 55.51545138, 0.00027797, 185.05150461, 0.00092655, -18.50515046, -9.266e-05, -55.51545138, -0.00027797, -185.05150461, -0.00092655, 0.4, 0.3, 0.003, 0.0, 0.0, 23025, 2)
    ops.limitCurve('ThreePoint', 13025, 3025, 0.0, 74.02060184, 0.02295574, 74.02060184, 0.06886722, 51.81442129, -7234.08325948, 0.05, 2, 0, 73025, 24025, 1, 3)
    ops.uniaxialMaterial('LimitState', 33025, 18.50515046, 9.266e-05, 55.51545138, 0.00027797, 185.05150461, 0.00092655, -18.50515046, -9.266e-05, -55.51545138, -0.00027797, -185.05150461, -0.00092655, 0.4, 0.3, 0.003, 0.0, 0.0, 13025, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3025, 99999, 'P', 43025, 'Vy', 33025, 'Vz', 23025, 'My', 13025, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173025, 73025, 173025, 3025, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124025, 124025, 24025, 3025, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173026, 2.95, 25.5, 10.15)
    ops.node(124026, 2.95, 25.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3026, 173026, 124026, 0.0625, 30502924.87761529, 12709552.03233971, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23026, 24.06924997, 0.00113894, 29.20682233, 0.01867464, 2.92068223, 0.08241307, -24.06924997, -0.00113894, -29.20682233, -0.01867464, -2.92068223, -0.08241307, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13026, 24.06924997, 0.00113894, 29.20682233, 0.01867464, 2.92068223, 0.08241307, -24.06924997, -0.00113894, -29.20682233, -0.01867464, -2.92068223, -0.08241307, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23026, 3026, 0.0, 78.41307682, 0.02277874, 78.41307682, 0.06833621, 54.88915377, -3255.8331528, 0.05, 2, 0, 73026, 24026, 2, 3)
    ops.uniaxialMaterial('LimitState', 43026, 19.6032692, 9.18e-05, 58.80980761, 0.00027541, 196.03269204, 0.00091804, -19.6032692, -9.18e-05, -58.80980761, -0.00027541, -196.03269204, -0.00091804, 0.4, 0.3, 0.003, 0.0, 0.0, 23026, 2)
    ops.limitCurve('ThreePoint', 13026, 3026, 0.0, 78.41307682, 0.02277874, 78.41307682, 0.06833621, 54.88915377, -3255.8331528, 0.05, 2, 0, 73026, 24026, 1, 3)
    ops.uniaxialMaterial('LimitState', 33026, 19.6032692, 9.18e-05, 58.80980761, 0.00027541, 196.03269204, 0.00091804, -19.6032692, -9.18e-05, -58.80980761, -0.00027541, -196.03269204, -0.00091804, 0.4, 0.3, 0.003, 0.0, 0.0, 13026, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3026, 99999, 'P', 43026, 'Vy', 33026, 'Vz', 23026, 'My', 13026, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173026, 73026, 173026, 3026, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124026, 124026, 24026, 3026, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173027, 8.3, 25.5, 10.15)
    ops.node(124027, 8.3, 25.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3027, 173027, 124027, 0.0625, 30093328.57870268, 12538886.90779278, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23027, 24.62335662, 0.00116347, 29.89878772, 0.01857837, 2.98987877, 0.08122458, -24.62335662, -0.00116347, -29.89878772, -0.01857837, -2.98987877, -0.08122458, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13027, 24.62335662, 0.00116347, 29.89878772, 0.01857837, 2.98987877, 0.08122458, -24.62335662, -0.00116347, -29.89878772, -0.01857837, -2.98987877, -0.08122458, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23027, 3027, 0.0, 78.3882803, 0.02326941, 78.3882803, 0.06980824, 54.87179621, -2684.02246734, 0.05, 2, 0, 73027, 24027, 2, 3)
    ops.uniaxialMaterial('LimitState', 43027, 19.59707008, 9.302e-05, 58.79121023, 0.00027907, 195.97070075, 0.00093024, -19.59707008, -9.302e-05, -58.79121023, -0.00027907, -195.97070075, -0.00093024, 0.4, 0.3, 0.003, 0.0, 0.0, 23027, 2)
    ops.limitCurve('ThreePoint', 13027, 3027, 0.0, 78.3882803, 0.02326941, 78.3882803, 0.06980824, 54.87179621, -2684.02246734, 0.05, 2, 0, 73027, 24027, 1, 3)
    ops.uniaxialMaterial('LimitState', 33027, 19.59707008, 9.302e-05, 58.79121023, 0.00027907, 195.97070075, 0.00093024, -19.59707008, -9.302e-05, -58.79121023, -0.00027907, -195.97070075, -0.00093024, 0.4, 0.3, 0.003, 0.0, 0.0, 13027, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3027, 99999, 'P', 43027, 'Vy', 33027, 'Vz', 23027, 'My', 13027, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173027, 73027, 173027, 3027, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124027, 124027, 24027, 3027, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173028, 13.65, 25.5, 10.15)
    ops.node(124028, 13.65, 25.5, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 3028, 173028, 124028, 0.0625, 30243504.65360117, 12601460.27233382, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 23028, 23.09247307, 0.0011283, 28.05656945, 0.0190178, 2.80565695, 0.08364025, -23.09247307, -0.0011283, -28.05656945, -0.0190178, -2.80565695, -0.08364025, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 13028, 23.09247307, 0.0011283, 28.05656945, 0.0190178, 2.80565695, 0.08364025, -23.09247307, -0.0011283, -28.05656945, -0.0190178, -2.80565695, -0.08364025, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 23028, 3028, 0.0, 77.77928818, 0.02256597, 77.77928818, 0.06769792, 54.44550173, -4473.1206072, 0.05, 2, 0, 73028, 24028, 2, 3)
    ops.uniaxialMaterial('LimitState', 43028, 19.44482205, 9.184e-05, 58.33446614, 0.00027553, 194.44822045, 0.00091843, -19.44482205, -9.184e-05, -58.33446614, -0.00027553, -194.44822045, -0.00091843, 0.4, 0.3, 0.003, 0.0, 0.0, 23028, 2)
    ops.limitCurve('ThreePoint', 13028, 3028, 0.0, 77.77928818, 0.02256597, 77.77928818, 0.06769792, 54.44550173, -4473.1206072, 0.05, 2, 0, 73028, 24028, 1, 3)
    ops.uniaxialMaterial('LimitState', 33028, 19.44482205, 9.184e-05, 58.33446614, 0.00027553, 194.44822045, 0.00091843, -19.44482205, -9.184e-05, -58.33446614, -0.00027553, -194.44822045, -0.00091843, 0.4, 0.3, 0.003, 0.0, 0.0, 13028, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 3028, 99999, 'P', 43028, 'Vy', 33028, 'Vz', 23028, 'My', 13028, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173028, 73028, 173028, 3028, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124028, 124028, 24028, 3028, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170001, 0.0, 0.0, 0.0)
    ops.node(124029, 0.0, 0.0, 1.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4074, 170001, 124029, 0.0625, 29590400.1754636, 12329333.40644317, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24074, 59.11823411, 0.00099514, 71.37452624, 0.02398323, 7.13745262, 0.08467405, -59.11823411, -0.00099514, -71.37452624, -0.02398323, -7.13745262, -0.08467405, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14074, 55.42404111, 0.00099514, 66.91445941, 0.02398323, 6.69144594, 0.08467405, -55.42404111, -0.00099514, -66.91445941, -0.02398323, -6.69144594, -0.08467405, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24074, 4074, 0.0, 96.31513601, 0.01990281, 96.31513601, 0.05970842, 67.42059521, -2969.32666069, 0.05, 2, 0, 70001, 24029, 2, 3)
    ops.uniaxialMaterial('LimitState', 44074, 24.078784, 6.937e-05, 72.23635201, 0.00020811, 240.78784002, 0.00069369, -24.078784, -6.937e-05, -72.23635201, -0.00020811, -240.78784002, -0.00069369, 0.4, 0.3, 0.003, 0.0, 0.0, 24074, 2)
    ops.limitCurve('ThreePoint', 14074, 4074, 0.0, 96.31513601, 0.01990281, 96.31513601, 0.05970842, 67.42059521, -2969.32666069, 0.05, 2, 0, 70001, 24029, 1, 3)
    ops.uniaxialMaterial('LimitState', 34074, 24.078784, 6.937e-05, 72.23635201, 0.00020811, 240.78784002, 0.00069369, -24.078784, -6.937e-05, -72.23635201, -0.00020811, -240.78784002, -0.00069369, 0.4, 0.3, 0.003, 0.0, 0.0, 14074, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4074, 99999, 'P', 44074, 'Vy', 34074, 'Vz', 24074, 'My', 14074, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170001, 70001, 170001, 4074, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124029, 124029, 24029, 4074, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174029, 0.0, 0.0, 2.05)
    ops.node(121001, 0.0, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4075, 174029, 121001, 0.0625, 28820964.2387471, 12008735.09947796, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24075, 41.34639602, 0.00091917, 50.06981966, 0.02383478, 5.00698197, 0.08617915, -41.34639602, -0.00091917, -50.06981966, -0.02383478, -5.00698197, -0.08617915, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14075, 37.77231616, 0.00091917, 45.74166652, 0.02383478, 4.57416665, 0.08617915, -37.77231616, -0.00091917, -45.74166652, -0.02383478, -4.57416665, -0.08617915, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24075, 4075, 0.0, 95.11024131, 0.01838339, 95.11024131, 0.05515016, 66.57716892, -3360.0693844, 0.05, 2, 0, 74029, 21001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44075, 23.77756033, 7.033e-05, 71.33268098, 0.00021099, 237.77560328, 0.0007033, -23.77756033, -7.033e-05, -71.33268098, -0.00021099, -237.77560328, -0.0007033, 0.4, 0.3, 0.003, 0.0, 0.0, 24075, 2)
    ops.limitCurve('ThreePoint', 14075, 4075, 0.0, 95.11024131, 0.01838339, 95.11024131, 0.05515016, 66.57716892, -3360.0693844, 0.05, 2, 0, 74029, 21001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34075, 23.77756033, 7.033e-05, 71.33268098, 0.00021099, 237.77560328, 0.0007033, -23.77756033, -7.033e-05, -71.33268098, -0.00021099, -237.77560328, -0.0007033, 0.4, 0.3, 0.003, 0.0, 0.0, 14075, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4075, 99999, 'P', 44075, 'Vy', 34075, 'Vz', 24075, 'My', 14075, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174029, 74029, 174029, 4075, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121001, 121001, 21001, 4075, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(170002, 2.95, 0.0, 0.0)
    ops.node(124030, 2.95, 0.0, 1.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4076, 170002, 124030, 0.1225, 30754225.14864149, 12814260.47860062, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24076, 160.31365843, 0.00077486, 193.07791431, 0.03198924, 19.30779143, 0.09209464, -160.31365843, -0.00077486, -193.07791431, -0.03198924, -19.30779143, -0.09209464, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14076, 160.31365843, 0.00077486, 193.07791431, 0.03198924, 19.30779143, 0.09209464, -160.31365843, -0.00077486, -193.07791431, -0.03198924, -19.30779143, -0.09209464, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24076, 4076, 0.0, 210.06886085, 0.01549726, 210.06886085, 0.04649177, 147.04820259, -5613.29550514, 0.05, 2, 0, 70002, 24030, 2, 3)
    ops.uniaxialMaterial('LimitState', 44076, 52.51721521, 7.427e-05, 157.55164563, 0.00022282, 525.17215211, 0.00074272, -52.51721521, -7.427e-05, -157.55164563, -0.00022282, -525.17215211, -0.00074272, 0.4, 0.3, 0.003, 0.0, 0.0, 24076, 2)
    ops.limitCurve('ThreePoint', 14076, 4076, 0.0, 210.06886085, 0.01549726, 210.06886085, 0.04649177, 147.04820259, -5613.29550514, 0.05, 2, 0, 70002, 24030, 1, 3)
    ops.uniaxialMaterial('LimitState', 34076, 52.51721521, 7.427e-05, 157.55164563, 0.00022282, 525.17215211, 0.00074272, -52.51721521, -7.427e-05, -157.55164563, -0.00022282, -525.17215211, -0.00074272, 0.4, 0.3, 0.003, 0.0, 0.0, 14076, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4076, 99999, 'P', 44076, 'Vy', 34076, 'Vz', 24076, 'My', 14076, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 170002, 70002, 170002, 4076, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124030, 124030, 24030, 4076, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174030, 2.95, 0.0, 2.05)
    ops.node(121002, 2.95, 0.0, 3.45)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4077, 174030, 121002, 0.1225, 29700722.03834575, 12375300.84931073, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24077, 103.59665047, 0.00077019, 125.14054895, 0.03007696, 12.5140549, 0.08984478, -103.59665047, -0.00077019, -125.14054895, -0.03007696, -12.5140549, -0.08984478, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14077, 97.92151552, 0.00077019, 118.28521628, 0.03007696, 11.82852163, 0.08984478, -97.92151552, -0.00077019, -118.28521628, -0.03007696, -11.82852163, -0.08984478, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24077, 4077, 0.0, 204.93287212, 0.01540379, 204.93287212, 0.04621137, 143.45301048, -5942.20496876, 0.05, 2, 0, 74030, 21002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44077, 51.23321803, 7.503e-05, 153.69965409, 0.00022508, 512.3321803, 0.00075026, -51.23321803, -7.503e-05, -153.69965409, -0.00022508, -512.3321803, -0.00075026, 0.4, 0.3, 0.003, 0.0, 0.0, 24077, 2)
    ops.limitCurve('ThreePoint', 14077, 4077, 0.0, 204.93287212, 0.01540379, 204.93287212, 0.04621137, 143.45301048, -5942.20496876, 0.05, 2, 0, 74030, 21002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34077, 51.23321803, 7.503e-05, 153.69965409, 0.00022508, 512.3321803, 0.00075026, -51.23321803, -7.503e-05, -153.69965409, -0.00022508, -512.3321803, -0.00075026, 0.4, 0.3, 0.003, 0.0, 0.0, 14077, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4077, 99999, 'P', 44077, 'Vy', 34077, 'Vz', 24077, 'My', 14077, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174030, 74030, 174030, 4077, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 121002, 121002, 21002, 4077, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171001, 0.0, 0.0, 3.95)
    ops.node(124031, 0.0, 0.0, 5.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4079, 171001, 124031, 0.0625, 29146041.80335597, 12144184.08473166, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24079, 30.93497603, 0.00083858, 37.47027381, 0.01747453, 3.74702738, 0.07117052, -30.93497603, -0.00083858, -37.47027381, -0.01747453, -3.74702738, -0.07117052, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14079, 30.93497603, 0.00083858, 37.47027381, 0.01747453, 3.74702738, 0.07117052, -30.93497603, -0.00083858, -37.47027381, -0.01747453, -3.74702738, -0.07117052, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24079, 4079, 0.0, 84.44873609, 0.01677158, 84.44873609, 0.05031474, 59.11411526, -2973.93333805, 0.05, 2, 0, 71001, 24031, 2, 3)
    ops.uniaxialMaterial('LimitState', 44079, 21.11218402, 5.174e-05, 63.33655207, 0.00015521, 211.12184022, 0.00051737, -21.11218402, -5.174e-05, -63.33655207, -0.00015521, -211.12184022, -0.00051737, 0.4, 0.3, 0.003, 0.0, 0.0, 24079, 2)
    ops.limitCurve('ThreePoint', 14079, 4079, 0.0, 84.44873609, 0.01677158, 84.44873609, 0.05031474, 59.11411526, -2973.93333805, 0.05, 2, 0, 71001, 24031, 1, 3)
    ops.uniaxialMaterial('LimitState', 34079, 21.11218402, 5.174e-05, 63.33655207, 0.00015521, 211.12184022, 0.00051737, -21.11218402, -5.174e-05, -63.33655207, -0.00015521, -211.12184022, -0.00051737, 0.4, 0.3, 0.003, 0.0, 0.0, 14079, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4079, 99999, 'P', 44079, 'Vy', 34079, 'Vz', 24079, 'My', 14079, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171001, 71001, 171001, 4079, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124031, 124031, 24031, 4079, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174031, 0.0, 0.0, 5.425)
    ops.node(122001, 0.0, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4080, 174031, 122001, 0.0625, 28940206.35920764, 12058419.31633652, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24080, 28.45572162, 0.00083743, 34.53922522, 0.01830476, 3.45392252, 0.07449569, -28.45572162, -0.00083743, -34.53922522, -0.01830476, -3.45392252, -0.07449569, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14080, 28.45572162, 0.00083743, 34.53922522, 0.01830476, 3.45392252, 0.07449569, -28.45572162, -0.00083743, -34.53922522, -0.01830476, -3.45392252, -0.07449569, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24080, 4080, 0.0, 81.91810909, 0.01674864, 81.91810909, 0.05024592, 57.34267636, -3282.12108866, 0.05, 2, 0, 74031, 22001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44080, 20.47952727, 5.054e-05, 61.43858182, 0.00015163, 204.79527272, 0.00050543, -20.47952727, -5.054e-05, -61.43858182, -0.00015163, -204.79527272, -0.00050543, 0.4, 0.3, 0.003, 0.0, 0.0, 24080, 2)
    ops.limitCurve('ThreePoint', 14080, 4080, 0.0, 81.91810909, 0.01674864, 81.91810909, 0.05024592, 57.34267636, -3282.12108866, 0.05, 2, 0, 74031, 22001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34080, 20.47952727, 5.054e-05, 61.43858182, 0.00015163, 204.79527272, 0.00050543, -20.47952727, -5.054e-05, -61.43858182, -0.00015163, -204.79527272, -0.00050543, 0.4, 0.3, 0.003, 0.0, 0.0, 14080, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4080, 99999, 'P', 44080, 'Vy', 34080, 'Vz', 24080, 'My', 14080, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174031, 74031, 174031, 4080, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122001, 122001, 22001, 4080, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(171002, 2.95, 0.0, 3.95)
    ops.node(124032, 2.95, 0.0, 5.075)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4081, 171002, 124032, 0.1225, 30727009.58702559, 12802920.66126066, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24081, 97.13619513, 0.0007098, 117.26049024, 0.02400512, 11.72604902, 0.07498729, -97.13619513, -0.0007098, -117.26049024, -0.02400512, -11.72604902, -0.07498729, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14081, 91.56342931, 0.0007098, 110.53318071, 0.02400512, 11.05331807, 0.07498729, -91.56342931, -0.0007098, -110.53318071, -0.02400512, -11.05331807, -0.07498729, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24081, 4081, 0.0, 197.94240111, 0.01419596, 197.94240111, 0.04258789, 138.55968078, -5057.86458233, 0.05, 2, 0, 71002, 24032, 2, 3)
    ops.uniaxialMaterial('LimitState', 44081, 49.48560028, 5.869e-05, 148.45680083, 0.00017606, 494.85600277, 0.00058688, -49.48560028, -5.869e-05, -148.45680083, -0.00017606, -494.85600277, -0.00058688, 0.4, 0.3, 0.003, 0.0, 0.0, 24081, 2)
    ops.limitCurve('ThreePoint', 14081, 4081, 0.0, 197.94240111, 0.01419596, 197.94240111, 0.04258789, 138.55968078, -5057.86458233, 0.05, 2, 0, 71002, 24032, 1, 3)
    ops.uniaxialMaterial('LimitState', 34081, 49.48560028, 5.869e-05, 148.45680083, 0.00017606, 494.85600277, 0.00058688, -49.48560028, -5.869e-05, -148.45680083, -0.00017606, -494.85600277, -0.00058688, 0.4, 0.3, 0.003, 0.0, 0.0, 14081, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4081, 99999, 'P', 44081, 'Vy', 34081, 'Vz', 24081, 'My', 14081, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 171002, 71002, 171002, 4081, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124032, 124032, 24032, 4081, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174032, 2.95, 0.0, 5.425)
    ops.node(122002, 2.95, 0.0, 6.55)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4082, 174032, 122002, 0.1225, 29315222.80866833, 12214676.17027847, 0.00211338, 0.00137557, 0.00137557, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24082, 93.17479866, 0.00071545, 112.92713985, 0.02480361, 11.29271399, 0.07550361, -93.17479866, -0.00071545, -112.92713985, -0.02480361, -11.29271399, -0.07550361, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14082, 87.68909735, 0.00071545, 106.27851202, 0.02480361, 10.6278512, 0.07550361, -87.68909735, -0.00071545, -106.27851202, -0.02480361, -10.6278512, -0.07550361, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24082, 4082, 0.0, 186.77264977, 0.014309, 186.77264977, 0.04292701, 130.74085484, -5203.00848986, 0.05, 2, 0, 74032, 22002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44082, 46.69316244, 5.804e-05, 140.07948733, 0.00017413, 466.93162443, 0.00058043, -46.69316244, -5.804e-05, -140.07948733, -0.00017413, -466.93162443, -0.00058043, 0.4, 0.3, 0.003, 0.0, 0.0, 24082, 2)
    ops.limitCurve('ThreePoint', 14082, 4082, 0.0, 186.77264977, 0.014309, 186.77264977, 0.04292701, 130.74085484, -5203.00848986, 0.05, 2, 0, 74032, 22002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34082, 46.69316244, 5.804e-05, 140.07948733, 0.00017413, 466.93162443, 0.00058043, -46.69316244, -5.804e-05, -140.07948733, -0.00017413, -466.93162443, -0.00058043, 0.4, 0.3, 0.003, 0.0, 0.0, 14082, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4082, 99999, 'P', 44082, 'Vy', 34082, 'Vz', 24082, 'My', 14082, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174032, 74032, 174032, 4082, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 122002, 122002, 22002, 4082, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172001, 0.0, 0.0, 7.05)
    ops.node(124033, 0.0, 0.0, 8.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4084, 172001, 124033, 0.0625, 29583344.75544473, 12326393.64810197, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24084, 28.12486197, 0.00082793, 34.11580502, 0.01828871, 3.4115805, 0.07643677, -28.12486197, -0.00082793, -34.11580502, -0.01828871, -3.4115805, -0.07643677, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14084, 28.12486197, 0.00082793, 34.11580502, 0.01828871, 3.4115805, 0.07643677, -28.12486197, -0.00082793, -34.11580502, -0.01828871, -3.4115805, -0.07643677, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24084, 4084, 0.0, 82.85952433, 0.01655862, 82.85952433, 0.04967587, 58.00166703, -3606.78719717, 0.05, 2, 0, 72001, 24033, 2, 3)
    ops.uniaxialMaterial('LimitState', 44084, 20.71488108, 5.001e-05, 62.14464325, 0.00015004, 207.14881083, 0.00050013, -20.71488108, -5.001e-05, -62.14464325, -0.00015004, -207.14881083, -0.00050013, 0.4, 0.3, 0.003, 0.0, 0.0, 24084, 2)
    ops.limitCurve('ThreePoint', 14084, 4084, 0.0, 82.85952433, 0.01655862, 82.85952433, 0.04967587, 58.00166703, -3606.78719717, 0.05, 2, 0, 72001, 24033, 1, 3)
    ops.uniaxialMaterial('LimitState', 34084, 20.71488108, 5.001e-05, 62.14464325, 0.00015004, 207.14881083, 0.00050013, -20.71488108, -5.001e-05, -62.14464325, -0.00015004, -207.14881083, -0.00050013, 0.4, 0.3, 0.003, 0.0, 0.0, 14084, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4084, 99999, 'P', 44084, 'Vy', 34084, 'Vz', 24084, 'My', 14084, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172001, 72001, 172001, 4084, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124033, 124033, 24033, 4084, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174033, 0.0, 0.0, 8.525)
    ops.node(123001, 0.0, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4085, 174033, 123001, 0.0625, 29738481.21097415, 12391033.83790589, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24085, 25.01728901, 0.00080965, 30.38943711, 0.01876465, 3.03894371, 0.08023928, -25.01728901, -0.00080965, -30.38943711, -0.01876465, -3.03894371, -0.08023928, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14085, 25.01728901, 0.00080965, 30.38943711, 0.01876465, 3.03894371, 0.08023928, -25.01728901, -0.00080965, -30.38943711, -0.01876465, -3.03894371, -0.08023928, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24085, 4085, 0.0, 80.41168181, 0.01619297, 80.41168181, 0.0485789, 56.28817727, -4774.22827528, 0.05, 2, 0, 74033, 23001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44085, 20.10292045, 4.828e-05, 60.30876136, 0.00014485, 201.02920453, 0.00048282, -20.10292045, -4.828e-05, -60.30876136, -0.00014485, -201.02920453, -0.00048282, 0.4, 0.3, 0.003, 0.0, 0.0, 24085, 2)
    ops.limitCurve('ThreePoint', 14085, 4085, 0.0, 80.41168181, 0.01619297, 80.41168181, 0.0485789, 56.28817727, -4774.22827528, 0.05, 2, 0, 74033, 23001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34085, 20.10292045, 4.828e-05, 60.30876136, 0.00014485, 201.02920453, 0.00048282, -20.10292045, -4.828e-05, -60.30876136, -0.00014485, -201.02920453, -0.00048282, 0.4, 0.3, 0.003, 0.0, 0.0, 14085, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4085, 99999, 'P', 44085, 'Vy', 34085, 'Vz', 24085, 'My', 14085, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174033, 74033, 174033, 4085, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123001, 123001, 23001, 4085, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(172002, 2.95, 0.0, 7.05)
    ops.node(124034, 2.95, 0.0, 8.175)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4086, 172002, 124034, 0.0625, 30336982.25366677, 12640409.27236115, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24086, 48.07592967, 0.0009285, 57.99684093, 0.02148434, 5.79968409, 0.07420676, -48.07592967, -0.0009285, -57.99684093, -0.02148434, -5.79968409, -0.07420676, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14086, 48.07592967, 0.0009285, 57.99684093, 0.02148434, 5.79968409, 0.07420676, -48.07592967, -0.0009285, -57.99684093, -0.02148434, -5.79968409, -0.07420676, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24086, 4086, 0.0, 88.25609385, 0.01856992, 88.25609385, 0.05570977, 61.77926569, -2739.80009187, 0.05, 2, 0, 72002, 24034, 2, 3)
    ops.uniaxialMaterial('LimitState', 44086, 22.06402346, 5.195e-05, 66.19207038, 0.00015584, 220.64023461, 0.00051947, -22.06402346, -5.195e-05, -66.19207038, -0.00015584, -220.64023461, -0.00051947, 0.4, 0.3, 0.003, 0.0, 0.0, 24086, 2)
    ops.limitCurve('ThreePoint', 14086, 4086, 0.0, 88.25609385, 0.01856992, 88.25609385, 0.05570977, 61.77926569, -2739.80009187, 0.05, 2, 0, 72002, 24034, 1, 3)
    ops.uniaxialMaterial('LimitState', 34086, 22.06402346, 5.195e-05, 66.19207038, 0.00015584, 220.64023461, 0.00051947, -22.06402346, -5.195e-05, -66.19207038, -0.00015584, -220.64023461, -0.00051947, 0.4, 0.3, 0.003, 0.0, 0.0, 14086, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4086, 99999, 'P', 44086, 'Vy', 34086, 'Vz', 24086, 'My', 14086, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 172002, 72002, 172002, 4086, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124034, 124034, 24034, 4086, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174034, 2.95, 0.0, 8.525)
    ops.node(123002, 2.95, 0.0, 9.65)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4087, 174034, 123002, 0.0625, 29773823.9013276, 12405759.9588865, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24087, 45.19640237, 0.00092217, 54.68296288, 0.02190173, 5.46829629, 0.07664397, -45.19640237, -0.00092217, -54.68296288, -0.02190173, -5.46829629, -0.07664397, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14087, 45.19640237, 0.00092217, 54.68296288, 0.02190173, 5.46829629, 0.07664397, -45.19640237, -0.00092217, -54.68296288, -0.02190173, -5.46829629, -0.07664397, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24087, 4087, 0.0, 84.51877602, 0.01844349, 84.51877602, 0.05533048, 59.16314321, -2903.05817952, 0.05, 2, 0, 74034, 23002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44087, 21.129694, 5.069e-05, 63.38908201, 0.00015206, 211.29694005, 0.00050688, -21.129694, -5.069e-05, -63.38908201, -0.00015206, -211.29694005, -0.00050688, 0.4, 0.3, 0.003, 0.0, 0.0, 24087, 2)
    ops.limitCurve('ThreePoint', 14087, 4087, 0.0, 84.51877602, 0.01844349, 84.51877602, 0.05533048, 59.16314321, -2903.05817952, 0.05, 2, 0, 74034, 23002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34087, 21.129694, 5.069e-05, 63.38908201, 0.00015206, 211.29694005, 0.00050688, -21.129694, -5.069e-05, -63.38908201, -0.00015206, -211.29694005, -0.00050688, 0.4, 0.3, 0.003, 0.0, 0.0, 14087, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4087, 99999, 'P', 44087, 'Vy', 34087, 'Vz', 24087, 'My', 14087, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174034, 74034, 174034, 4087, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 123002, 123002, 23002, 4087, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173001, 0.0, 0.0, 10.15)
    ops.node(124035, 0.0, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4089, 173001, 124035, 0.0625, 28684158.68428947, 11951732.78512061, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24089, 24.83403168, 0.00079815, 30.27211594, 0.0193303, 3.02721159, 0.08184767, -24.83403168, -0.00079815, -30.27211594, -0.0193303, -3.02721159, -0.08184767, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14089, 24.83403168, 0.00079815, 30.27211594, 0.0193303, 3.02721159, 0.08184767, -24.83403168, -0.00079815, -30.27211594, -0.0193303, -3.02721159, -0.08184767, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24089, 4089, 0.0, 78.33130241, 0.01596296, 78.33130241, 0.04788888, 54.83191169, -6366.58210663, 0.05, 2, 0, 73001, 24035, 2, 3)
    ops.uniaxialMaterial('LimitState', 44089, 19.5828256, 4.876e-05, 58.74847681, 0.00014628, 195.82825604, 0.00048762, -19.5828256, -4.876e-05, -58.74847681, -0.00014628, -195.82825604, -0.00048762, 0.4, 0.3, 0.003, 0.0, 0.0, 24089, 2)
    ops.limitCurve('ThreePoint', 14089, 4089, 0.0, 78.33130241, 0.01596296, 78.33130241, 0.04788888, 54.83191169, -6366.58210663, 0.05, 2, 0, 73001, 24035, 1, 3)
    ops.uniaxialMaterial('LimitState', 34089, 19.5828256, 4.876e-05, 58.74847681, 0.00014628, 195.82825604, 0.00048762, -19.5828256, -4.876e-05, -58.74847681, -0.00014628, -195.82825604, -0.00048762, 0.4, 0.3, 0.003, 0.0, 0.0, 14089, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4089, 99999, 'P', 44089, 'Vy', 34089, 'Vz', 24089, 'My', 14089, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173001, 73001, 173001, 4089, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124035, 124035, 24035, 4089, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174035, 0.0, 0.0, 11.625)
    ops.node(124001, 0.0, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4090, 174035, 124001, 0.0625, 29698824.19555918, 12374510.08148299, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24090, 20.77632428, 0.00081056, 25.30657564, 0.01957778, 2.53065756, 0.08602214, -20.77632428, -0.00081056, -25.30657564, -0.01957778, -2.53065756, -0.08602214, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14090, 20.77632428, 0.00081056, 25.30657564, 0.01957778, 2.53065756, 0.08602214, -20.77632428, -0.00081056, -25.30657564, -0.01957778, -2.53065756, -0.08602214, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24090, 4090, 0.0, 76.82196855, 0.01621121, 76.82196855, 0.04863362, 53.77537799, -40140.5203126, 0.05, 2, 0, 74035, 24001, 2, 3)
    ops.uniaxialMaterial('LimitState', 44090, 19.20549214, 4.619e-05, 57.61647642, 0.00013856, 192.05492139, 0.00046188, -19.20549214, -4.619e-05, -57.61647642, -0.00013856, -192.05492139, -0.00046188, 0.4, 0.3, 0.003, 0.0, 0.0, 24090, 2)
    ops.limitCurve('ThreePoint', 14090, 4090, 0.0, 76.82196855, 0.01621121, 76.82196855, 0.04863362, 53.77537799, -40140.5203126, 0.05, 2, 0, 74035, 24001, 1, 3)
    ops.uniaxialMaterial('LimitState', 34090, 19.20549214, 4.619e-05, 57.61647642, 0.00013856, 192.05492139, 0.00046188, -19.20549214, -4.619e-05, -57.61647642, -0.00013856, -192.05492139, -0.00046188, 0.4, 0.3, 0.003, 0.0, 0.0, 14090, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4090, 99999, 'P', 44090, 'Vy', 34090, 'Vz', 24090, 'My', 14090, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174035, 74035, 174035, 4090, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124001, 124001, 24001, 4090, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(173002, 2.95, 0.0, 10.15)
    ops.node(124036, 2.95, 0.0, 11.275)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4091, 173002, 124036, 0.0625, 29470117.09053138, 12279215.45438807, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24091, 41.18851001, 0.00090108, 50.05487874, 0.01886116, 5.00548787, 0.07163088, -41.18851001, -0.00090108, -50.05487874, -0.01886116, -5.00548787, -0.07163088, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14091, 41.18851001, 0.00090108, 50.05487874, 0.01886116, 5.00548787, 0.07163088, -41.18851001, -0.00090108, -50.05487874, -0.01886116, -5.00548787, -0.07163088, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24091, 4091, 0.0, 66.50178104, 0.01802158, 66.50178104, 0.05406474, 46.55124673, -3130.62801973, 0.05, 2, 0, 73002, 24036, 2, 3)
    ops.uniaxialMaterial('LimitState', 44091, 16.62544526, 4.029e-05, 49.87633578, 0.00012088, 166.2544526, 0.00040294, -16.62544526, -4.029e-05, -49.87633578, -0.00012088, -166.2544526, -0.00040294, 0.4, 0.3, 0.003, 0.0, 0.0, 24091, 2)
    ops.limitCurve('ThreePoint', 14091, 4091, 0.0, 66.50178104, 0.01802158, 66.50178104, 0.05406474, 46.55124673, -3130.62801973, 0.05, 2, 0, 73002, 24036, 1, 3)
    ops.uniaxialMaterial('LimitState', 34091, 16.62544526, 4.029e-05, 49.87633578, 0.00012088, 166.2544526, 0.00040294, -16.62544526, -4.029e-05, -49.87633578, -0.00012088, -166.2544526, -0.00040294, 0.4, 0.3, 0.003, 0.0, 0.0, 14091, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4091, 99999, 'P', 44091, 'Vy', 34091, 'Vz', 24091, 'My', 14091, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 173002, 73002, 173002, 4091, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124036, 124036, 24036, 4091, '-orient', 0, 0, 1, 0, 1, 0)

    # Create elastic column element nodes
    ops.node(174036, 2.95, 0.0, 11.625)
    ops.node(124002, 2.95, 0.0, 12.8)
    # Create elastic column element
    ops.element('elasticBeamColumn', 4092, 174036, 124002, 0.0625, 29600621.32773328, 12333592.21988887, 0.00055013, 0.00035807, 0.00035807, 66666)
    # Create materials describing flexural behaviour of plastic hinge
    ops.uniaxialMaterial('Hysteretic', 24092, 38.50277006, 0.00086666, 46.8606917, 0.01953345, 4.68606917, 0.07531019, -38.50277006, -0.00086666, -46.8606917, -0.01953345, -4.68606917, -0.07531019, 1.0, 1.0, 0.0, 0.0, 0.0)
    ops.uniaxialMaterial('Hysteretic', 14092, 38.50277006, 0.00086666, 46.8606917, 0.01953345, 4.68606917, 0.07531019, -38.50277006, -0.00086666, -46.8606917, -0.01953345, -4.68606917, -0.07531019, 1.0, 1.0, 0.0, 0.0, 0.0)
    # Create new materials describing shear behaviour of plastic hinge
    ops.limitCurve('ThreePoint', 24092, 4092, 0.0, 65.86812236, 0.01733329, 65.86812236, 0.05199987, 46.10768565, -6100.20687445, 0.05, 2, 0, 74036, 24002, 2, 3)
    ops.uniaxialMaterial('LimitState', 44092, 16.46703059, 3.973e-05, 49.40109177, 0.0001192, 164.67030589, 0.00039734, -16.46703059, -3.973e-05, -49.40109177, -0.0001192, -164.67030589, -0.00039734, 0.4, 0.3, 0.003, 0.0, 0.0, 24092, 2)
    ops.limitCurve('ThreePoint', 14092, 4092, 0.0, 65.86812236, 0.01733329, 65.86812236, 0.05199987, 46.10768565, -6100.20687445, 0.05, 2, 0, 74036, 24002, 1, 3)
    ops.uniaxialMaterial('LimitState', 34092, 16.46703059, 3.973e-05, 49.40109177, 0.0001192, 164.67030589, 0.00039734, -16.46703059, -3.973e-05, -49.40109177, -0.0001192, -164.67030589, -0.00039734, 0.4, 0.3, 0.003, 0.0, 0.0, 14092, 2)
    # Create plastic hinge sections at both ends
    ops.section('Aggregator', 4092, 99999, 'P', 44092, 'Vy', 34092, 'Vz', 24092, 'My', 14092, 'Mz', 99999, 'T')
    # Create plastic hinge elements at both ends
    ops.element('zeroLengthSection', 174036, 74036, 174036, 4092, '-orient', 0, 0, 1, 0, 1, 0)
    ops.element('zeroLengthSection', 124002, 124002, 24002, 4092, '-orient', 0, 0, 1, 0, 1, 0)
