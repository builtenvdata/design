import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (1, 0, 0.5)
    # Central joint node
    ops.node(4017, 4.95, 0.0, 1.375, '-mass', 3.983530835881753, 3.983530835881753, 3.983530835881753, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 5.125, 0.0, 1.375)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 4.95, 0.0, 1.175)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(74017, 4.95, 0.0, 1.575)
    ops.element('elasticBeamColumn', 74017, 4017, 74017, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(4018, 7.9, 0.0, 1.375, '-mass', 3.983530835881753, 3.983530835881753, 3.983530835881753, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 7.725, 0.0, 1.375)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 7.9, 0.0, 1.175)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(74018, 7.9, 0.0, 1.575)
    ops.element('elasticBeamColumn', 74018, 4018, 74018, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    # Central joint node
    ops.node(4019, 4.95, 0.0, 4.125, '-mass', 3.983530835881753, 3.983530835881753, 3.983530835881753, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 5.125, 0.0, 4.125)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 4.95, 0.0, 3.925)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(74019, 4.95, 0.0, 4.325)
    ops.element('elasticBeamColumn', 74019, 4019, 74019, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(4020, 7.9, 0.0, 4.125, '-mass', 3.983530835881753, 3.983530835881753, 3.983530835881753, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 7.725, 0.0, 4.125)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 7.9, 0.0, 3.925)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(74020, 7.9, 0.0, 4.325)
    ops.element('elasticBeamColumn', 74020, 4020, 74020, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    # Central joint node
    ops.node(4021, 4.95, 0.0, 6.875, '-mass', 3.6927051478083595, 3.6927051478083595, 3.6927051478083595, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 5.1, 0.0, 6.875)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 4.95, 0.0, 6.675)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(74021, 4.95, 0.0, 7.075)
    ops.element('elasticBeamColumn', 74021, 4021, 74021, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(4022, 7.9, 0.0, 6.875, '-mass', 3.6927051478083595, 3.6927051478083595, 3.6927051478083595, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 7.75, 0.0, 6.875)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(24022, 7.9, 0.0, 6.675)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(74022, 7.9, 0.0, 7.075)
    ops.element('elasticBeamColumn', 74022, 4022, 74022, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 3.5)
    # Central joint node
    ops.node(4023, 4.95, 0.0, 9.625, '-mass', 3.6927051478083595, 3.6927051478083595, 3.6927051478083595, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34023, 5.1, 0.0, 9.625)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 4.95, 0.0, 9.425)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(74023, 4.95, 0.0, 9.825)
    ops.element('elasticBeamColumn', 74023, 4023, 74023, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(4024, 7.9, 0.0, 9.625, '-mass', 3.6927051478083595, 3.6927051478083595, 3.6927051478083595, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 7.75, 0.0, 9.625)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 7.9, 0.0, 9.425)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(74024, 7.9, 0.0, 9.825)
    ops.element('elasticBeamColumn', 74024, 4024, 74024, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 2.75, '-mass', 11.763275993883791, 11.763275993883791, 11.763275993883791, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.15, 0.0, 2.75)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.5)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.25, 2.75)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 58114.4213)
    ops.uniaxialMaterial('Elastic', 401001, 60647.63745)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 4.95, 0.0, 2.75, '-mass', 12.190646024464831, 12.190646024464831, 12.190646024464831, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 4.775, 0.0, 2.75)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 5.125, 0.0, 2.75)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 4.95, 0.0, 2.5)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 4.95, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 4.95, 0.35, 2.75)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 119502.71725)
    ops.uniaxialMaterial('Elastic', 401002, 132535.38135)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 7.9, 0.0, 2.75, '-mass', 12.190646024464831, 12.190646024464831, 12.190646024464831, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 7.725, 0.0, 2.75)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 8.075, 0.0, 2.75)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 7.9, 0.0, 2.5)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 7.9, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 7.9, 0.35, 2.75)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 119502.71725)
    ops.uniaxialMaterial('Elastic', 401003, 132535.38135)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 12.85, 0.0, 2.75, '-mass', 11.763275993883791, 11.763275993883791, 11.763275993883791, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 12.7, 0.0, 2.75)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 12.85, 0.0, 2.5)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 12.85, 0.0, 3.0)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 12.85, 0.25, 2.75)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 58114.4213)
    ops.uniaxialMaterial('Elastic', 401004, 60647.63745)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 4.65, 2.75, '-mass', 19.13327981651376, 19.13327981651376, 19.13327981651376, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.4, 4.65, 2.75)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 4.65, 2.45)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 4.65, 3.05)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 4.475, 2.75)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 4.825, 2.75)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 114939.3159)
    ops.uniaxialMaterial('Elastic', 401005, 147298.88065)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 4.95, 4.65, 2.75, '-mass', 24.471977573904176, 24.471977573904176, 24.471977573904176, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 4.475, 4.65, 2.75)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 5.425, 4.65, 2.75)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 4.95, 4.65, 2.45)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 4.95, 4.65, 3.05)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 4.95, 4.425, 2.75)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 4.95, 4.875, 2.75)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 173258.33915)
    ops.uniaxialMaterial('Elastic', 401006, 291949.4951)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 7.9, 4.65, 2.75, '-mass', 24.471977573904176, 24.471977573904176, 24.471977573904176, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 7.425, 4.65, 2.75)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 8.375, 4.65, 2.75)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 7.9, 4.65, 2.45)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 7.9, 4.65, 3.05)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 7.9, 4.425, 2.75)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 7.9, 4.875, 2.75)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 173258.33915)
    ops.uniaxialMaterial('Elastic', 401007, 291949.4951)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 12.85, 4.65, 2.75, '-mass', 19.13327981651376, 19.13327981651376, 19.13327981651376, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 12.45, 4.65, 2.75)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 12.85, 4.65, 2.45)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 12.85, 4.65, 3.05)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 12.85, 4.475, 2.75)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 12.85, 4.825, 2.75)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 114939.3159)
    ops.uniaxialMaterial('Elastic', 401008, 147298.88065)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 9.3, 2.75, '-mass', 18.917844036697243, 18.917844036697243, 18.917844036697243, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.4, 9.3, 2.75)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 9.3, 2.45)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 9.3, 3.05)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 9.125, 2.75)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 9.475, 2.75)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 114450.7376)
    ops.uniaxialMaterial('Elastic', 401009, 146697.24925)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 4.95, 9.3, 2.75, '-mass', 22.81247961264016, 22.81247961264016, 22.81247961264016, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 4.5, 9.3, 2.75)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 5.4, 9.3, 2.75)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 4.95, 9.3, 2.45)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 4.95, 9.3, 3.05)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 4.95, 9.1, 2.75)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 4.95, 9.5, 2.75)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 155541.3429)
    ops.uniaxialMaterial('Elastic', 401010, 261159.66265)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 7.9, 9.3, 2.75, '-mass', 22.81247961264016, 22.81247961264016, 22.81247961264016, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 7.45, 9.3, 2.75)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 8.35, 9.3, 2.75)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 7.9, 9.3, 2.45)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 7.9, 9.3, 3.05)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 7.9, 9.1, 2.75)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 7.9, 9.5, 2.75)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 155541.3429)
    ops.uniaxialMaterial('Elastic', 401011, 261159.66265)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 12.85, 9.3, 2.75, '-mass', 18.917844036697243, 18.917844036697243, 18.917844036697243, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 12.45, 9.3, 2.75)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 12.85, 9.3, 2.45)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 12.85, 9.3, 3.05)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 12.85, 9.125, 2.75)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 12.85, 9.475, 2.75)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 114450.7376)
    ops.uniaxialMaterial('Elastic', 401012, 146697.24925)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1013, 0.0, 13.95, 2.75, '-mass', 11.547840214067275, 11.547840214067275, 11.547840214067275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.15, 13.95, 2.75)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 13.95, 2.5)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 13.95, 3.0)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 13.7, 2.75)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301013, 57696.97245)
    ops.uniaxialMaterial('Elastic', 401013, 60226.01245)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1014, 4.95, 13.95, 2.75, '-mass', 15.016462793068293, 15.016462793068293, 15.016462793068293, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 4.775, 13.95, 2.75)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 5.125, 13.95, 2.75)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 4.95, 13.95, 2.5)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 4.95, 13.95, 3.0)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 4.95, 13.625, 2.75)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301014, 95463.85065)
    ops.uniaxialMaterial('Elastic', 401014, 109752.06885)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1015, 7.9, 13.95, 2.75, '-mass', 15.016462793068293, 15.016462793068293, 15.016462793068293, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 7.725, 13.95, 2.75)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 8.075, 13.95, 2.75)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 7.9, 13.95, 2.5)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 7.9, 13.95, 3.0)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 7.9, 13.625, 2.75)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301015, 95463.85065)
    ops.uniaxialMaterial('Elastic', 401015, 109752.06885)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1016, 12.85, 13.95, 2.75, '-mass', 11.547840214067275, 11.547840214067275, 11.547840214067275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 12.7, 13.95, 2.75)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 12.85, 13.95, 2.5)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 12.85, 13.95, 3.0)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 12.85, 13.7, 2.75)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301016, 57696.97245)
    ops.uniaxialMaterial('Elastic', 401016, 60226.01245)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 5.5, '-mass', 11.595080275229357, 11.595080275229357, 11.595080275229357, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.15, 0.0, 5.5)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 5.25)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 5.75)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.25, 5.5)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 49896.83875)
    ops.uniaxialMaterial('Elastic', 402001, 52349.15985)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 4.95, 0.0, 5.5, '-mass', 12.081318807339448, 12.081318807339448, 12.081318807339448, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 4.775, 0.0, 5.5)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 5.125, 0.0, 5.5)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 4.95, 0.0, 5.25)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 4.95, 0.0, 5.75)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 4.95, 0.35, 5.5)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 102061.5948)
    ops.uniaxialMaterial('Elastic', 402002, 112427.321)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 7.9, 0.0, 5.5, '-mass', 12.081318807339448, 12.081318807339448, 12.081318807339448, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 7.725, 0.0, 5.5)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 8.075, 0.0, 5.5)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 7.9, 0.0, 5.25)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 7.9, 0.0, 5.75)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 7.9, 0.35, 5.5)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 102061.5948)
    ops.uniaxialMaterial('Elastic', 402003, 112427.321)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 12.85, 0.0, 5.5, '-mass', 11.595080275229357, 11.595080275229357, 11.595080275229357, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 12.7, 0.0, 5.5)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 12.85, 0.0, 5.25)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 12.85, 0.0, 5.75)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 12.85, 0.25, 5.5)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 49896.83875)
    ops.uniaxialMaterial('Elastic', 402004, 52349.15985)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 4.65, 5.5, '-mass', 18.822117737003055, 18.822117737003055, 18.822117737003055, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.4, 4.65, 5.5)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 4.65, 5.2)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 4.65, 5.8)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 4.475, 5.5)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 4.825, 5.5)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 98171.09335)
    ops.uniaxialMaterial('Elastic', 402005, 126646.92555)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 4.95, 4.65, 5.5, '-mass', 24.03466870540265, 24.03466870540265, 24.03466870540265, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 4.475, 4.65, 5.5)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 5.425, 4.65, 5.5)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 4.95, 4.65, 5.2)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 4.95, 4.65, 5.8)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 4.95, 4.425, 5.5)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 4.95, 4.875, 5.5)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 149177.78965)
    ops.uniaxialMaterial('Elastic', 402006, 252049.6195)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 7.9, 4.65, 5.5, '-mass', 24.03466870540265, 24.03466870540265, 24.03466870540265, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 7.425, 4.65, 5.5)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 8.375, 4.65, 5.5)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 7.9, 4.65, 5.2)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 7.9, 4.65, 5.8)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 7.9, 4.425, 5.5)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 7.9, 4.875, 5.5)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 149177.78965)
    ops.uniaxialMaterial('Elastic', 402007, 252049.6195)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 12.85, 4.65, 5.5, '-mass', 18.822117737003055, 18.822117737003055, 18.822117737003055, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 12.45, 4.65, 5.5)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 12.85, 4.65, 5.2)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 12.85, 4.65, 5.8)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 12.85, 4.475, 5.5)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 12.85, 4.825, 5.5)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 98171.09335)
    ops.uniaxialMaterial('Elastic', 402008, 126646.92555)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 9.3, 5.5, '-mass', 18.606681957186538, 18.606681957186538, 18.606681957186538, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.4, 9.3, 5.5)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 9.3, 5.2)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 9.3, 5.8)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 9.125, 5.5)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 9.475, 5.5)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 97731.8064)
    ops.uniaxialMaterial('Elastic', 402009, 126105.7742)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 4.95, 9.3, 5.5, '-mass', 22.543366462793067, 22.543366462793067, 22.543366462793067, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 4.5, 9.3, 5.5)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 5.4, 9.3, 5.5)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 4.95, 9.3, 5.2)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 4.95, 9.3, 5.8)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 4.95, 9.1, 5.5)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 4.95, 9.5, 5.5)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 133466.4839)
    ops.uniaxialMaterial('Elastic', 402010, 224640.7798)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 7.9, 9.3, 5.5, '-mass', 22.543366462793067, 22.543366462793067, 22.543366462793067, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 7.45, 9.3, 5.5)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 8.35, 9.3, 5.5)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 7.9, 9.3, 5.2)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 7.9, 9.3, 5.8)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 7.9, 9.1, 5.5)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 7.9, 9.5, 5.5)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 133466.4839)
    ops.uniaxialMaterial('Elastic', 402011, 224640.7798)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 12.85, 9.3, 5.5, '-mass', 18.606681957186538, 18.606681957186538, 18.606681957186538, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 12.45, 9.3, 5.5)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 12.85, 9.3, 5.2)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 12.85, 9.3, 5.8)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 12.85, 9.125, 5.5)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 12.85, 9.475, 5.5)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 97731.8064)
    ops.uniaxialMaterial('Elastic', 402012, 126105.7742)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2013, 0.0, 13.95, 5.5, '-mass', 11.37964449541284, 11.37964449541284, 11.37964449541284, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.15, 13.95, 5.5)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 13.95, 5.25)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 13.95, 5.75)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 13.7, 5.5)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302013, 49520.31215)
    ops.uniaxialMaterial('Elastic', 402013, 51969.00455)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2014, 4.95, 13.95, 5.5, '-mass', 14.80621814475025, 14.80621814475025, 14.80621814475025, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 4.775, 13.95, 5.5)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 5.125, 13.95, 5.5)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 4.95, 13.95, 5.25)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 4.95, 13.95, 5.75)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 4.95, 13.625, 5.5)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302014, 82027.73365)
    ops.uniaxialMaterial('Elastic', 402014, 93684.8038)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2015, 7.9, 13.95, 5.5, '-mass', 14.80621814475025, 14.80621814475025, 14.80621814475025, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 7.725, 13.95, 5.5)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 8.075, 13.95, 5.5)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 7.9, 13.95, 5.25)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 7.9, 13.95, 5.75)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 7.9, 13.625, 5.5)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302015, 82027.73365)
    ops.uniaxialMaterial('Elastic', 402015, 93684.8038)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2016, 12.85, 13.95, 5.5, '-mass', 11.37964449541284, 11.37964449541284, 11.37964449541284, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 12.7, 13.95, 5.5)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 12.85, 13.95, 5.25)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 12.85, 13.95, 5.75)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 12.85, 13.7, 5.5)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302016, 49520.31215)
    ops.uniaxialMaterial('Elastic', 402016, 51969.00455)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 8.25, '-mass', 11.426884556574922, 11.426884556574922, 11.426884556574922, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 8.25)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 8.0)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 8.5)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.2, 8.25)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 35914.7637)
    ops.uniaxialMaterial('Elastic', 403001, 37555.95485)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 4.95, 0.0, 8.25, '-mass', 11.971991590214065, 11.971991590214065, 11.971991590214065, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 4.8, 0.0, 8.25)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 5.1, 0.0, 8.25)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 4.95, 0.0, 8.0)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 4.95, 0.0, 8.5)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 4.95, 0.3, 8.25)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 68268.28565)
    ops.uniaxialMaterial('Elastic', 403002, 77799.7354)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 7.9, 0.0, 8.25, '-mass', 11.971991590214065, 11.971991590214065, 11.971991590214065, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 7.75, 0.0, 8.25)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 8.05, 0.0, 8.25)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 7.9, 0.0, 8.0)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 7.9, 0.0, 8.5)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 7.9, 0.3, 8.25)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 68268.28565)
    ops.uniaxialMaterial('Elastic', 403003, 77799.7354)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 12.85, 0.0, 8.25, '-mass', 11.426884556574922, 11.426884556574922, 11.426884556574922, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 12.725, 0.0, 8.25)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 12.85, 0.0, 8.0)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 12.85, 0.0, 8.5)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 12.85, 0.2, 8.25)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 35914.7637)
    ops.uniaxialMaterial('Elastic', 403004, 37555.95485)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 4.65, 8.25, '-mass', 18.51095565749235, 18.51095565749235, 18.51095565749235, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.375, 4.65, 8.25)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 4.65, 7.95)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 4.65, 8.55)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 4.525, 8.25)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 4.775, 8.25)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 61834.2624)
    ops.uniaxialMaterial('Elastic', 403005, 82126.6544)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 4.95, 4.65, 8.25, '-mass', 23.59735983690112, 23.59735983690112, 23.59735983690112, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 4.525, 4.65, 8.25)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 5.375, 4.65, 8.25)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 4.95, 4.65, 7.95)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 4.95, 4.65, 8.55)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 4.95, 4.475, 8.25)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 4.95, 4.825, 8.25)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 100374.00925)
    ops.uniaxialMaterial('Elastic', 403006, 168765.6416)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 7.9, 4.65, 8.25, '-mass', 23.59735983690112, 23.59735983690112, 23.59735983690112, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 7.475, 4.65, 8.25)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 8.325, 4.65, 8.25)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 7.9, 4.65, 7.95)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 7.9, 4.65, 8.55)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 7.9, 4.475, 8.25)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 7.9, 4.825, 8.25)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 100374.00925)
    ops.uniaxialMaterial('Elastic', 403007, 168765.6416)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 12.85, 4.65, 8.25, '-mass', 18.51095565749235, 18.51095565749235, 18.51095565749235, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 12.475, 4.65, 8.25)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 12.85, 4.65, 7.95)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 12.85, 4.65, 8.55)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 12.85, 4.525, 8.25)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 12.85, 4.775, 8.25)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 61834.2624)
    ops.uniaxialMaterial('Elastic', 403008, 82126.6544)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 9.3, 8.25, '-mass', 18.295519877675837, 18.295519877675837, 18.295519877675837, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.375, 9.3, 8.25)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 9.3, 7.95)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 9.3, 8.55)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 9.175, 8.25)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 9.425, 8.25)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 61523.20265)
    ops.uniaxialMaterial('Elastic', 403009, 81734.66975)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 4.95, 9.3, 8.25, '-mass', 22.274253312945973, 22.274253312945973, 22.274253312945973, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 4.55, 9.3, 8.25)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 5.35, 9.3, 8.25)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 4.95, 9.3, 7.95)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 4.95, 9.3, 8.55)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 4.95, 9.125, 8.25)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 4.95, 9.475, 8.25)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 97188.2131)
    ops.uniaxialMaterial('Elastic', 403010, 158397.7065)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 7.9, 9.3, 8.25, '-mass', 22.274253312945973, 22.274253312945973, 22.274253312945973, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 7.5, 9.3, 8.25)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 8.3, 9.3, 8.25)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 7.9, 9.3, 7.95)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 7.9, 9.3, 8.55)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 7.9, 9.125, 8.25)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 7.9, 9.475, 8.25)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 97188.2131)
    ops.uniaxialMaterial('Elastic', 403011, 158397.7065)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 12.85, 9.3, 8.25, '-mass', 18.295519877675833, 18.295519877675833, 18.295519877675833, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 12.475, 9.3, 8.25)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 12.85, 9.3, 7.95)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 12.85, 9.3, 8.55)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 12.85, 9.175, 8.25)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 12.85, 9.425, 8.25)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 61523.20265)
    ops.uniaxialMaterial('Elastic', 403012, 81734.66975)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3013, 0.0, 13.95, 8.25, '-mass', 11.211448776758408, 11.211448776758408, 11.211448776758408, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 13.95, 8.25)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 13.95, 8.0)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 13.95, 8.5)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 13.75, 8.25)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303013, 35615.78355)
    ops.uniaxialMaterial('Elastic', 403013, 37258.077)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3014, 4.95, 13.95, 8.25, '-mass', 14.595973496432208, 14.595973496432208, 14.595973496432208, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 4.8, 13.95, 8.25)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 5.1, 13.95, 8.25)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 4.95, 13.95, 8.0)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 4.95, 13.95, 8.5)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 4.95, 13.675, 8.25)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303014, 55789.14855)
    ops.uniaxialMaterial('Elastic', 403014, 66389.5116)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3015, 7.9, 13.95, 8.25, '-mass', 14.595973496432208, 14.595973496432208, 14.595973496432208, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 7.75, 13.95, 8.25)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 8.05, 13.95, 8.25)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 7.9, 13.95, 8.0)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 7.9, 13.95, 8.5)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 7.9, 13.675, 8.25)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303015, 55789.14855)
    ops.uniaxialMaterial('Elastic', 403015, 66389.5116)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3016, 12.85, 13.95, 8.25, '-mass', 11.211448776758406, 11.211448776758406, 11.211448776758406, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 12.725, 13.95, 8.25)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 12.85, 13.95, 8.0)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 12.85, 13.95, 8.5)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 12.85, 13.75, 8.25)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303016, 35615.78355)
    ops.uniaxialMaterial('Elastic', 403016, 37258.077)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 11.0, '-mass', 6.525451070336393, 6.525451070336393, 6.525451070336393, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 11.0)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 10.8)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.2, 11.0)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 20877.98635)
    ops.uniaxialMaterial('Elastic', 404001, 27207.5478)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 4.95, 0.0, 11.0, '-mass', 7.080191131498472, 7.080191131498472, 7.080191131498472, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 4.8, 0.0, 11.0)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 5.1, 0.0, 11.0)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 4.95, 0.0, 10.8)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 4.95, 0.3, 11.0)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 40105.64845)
    ops.uniaxialMaterial('Elastic', 404002, 34495.22865)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 7.9, 0.0, 11.0, '-mass', 7.08019113149847, 7.08019113149847, 7.08019113149847, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 7.75, 0.0, 11.0)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 8.05, 0.0, 11.0)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 7.9, 0.0, 10.8)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 7.9, 0.3, 11.0)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 40105.64845)
    ops.uniaxialMaterial('Elastic', 404003, 34495.22865)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 12.85, 0.0, 11.0, '-mass', 6.525451070336391, 6.525451070336391, 6.525451070336391, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 12.725, 0.0, 11.0)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 12.85, 0.0, 10.8)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 12.85, 0.2, 11.0)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 20877.98635)
    ops.uniaxialMaterial('Elastic', 404004, 27207.5478)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 4.65, 11.0, '-mass', 12.706100917431195, 12.706100917431195, 12.706100917431195, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.375, 4.65, 11.0)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 4.65, 10.75)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 4.525, 11.0)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 4.775, 11.0)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 30146.7354)
    ops.uniaxialMaterial('Elastic', 404005, 65610.2601)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 4.95, 4.65, 11.0, '-mass', 18.933120540265037, 18.933120540265037, 18.933120540265037, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 4.525, 4.65, 11.0)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 5.375, 4.65, 11.0)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 4.95, 4.65, 10.75)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 4.95, 4.475, 11.0)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 4.95, 4.825, 11.0)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 61784.3347)
    ops.uniaxialMaterial('Elastic', 404006, 101197.98125)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 7.9, 4.65, 11.0, '-mass', 18.933120540265037, 18.933120540265037, 18.933120540265037, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 7.475, 4.65, 11.0)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 8.325, 4.65, 11.0)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 7.9, 4.65, 10.75)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 7.9, 4.475, 11.0)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 7.9, 4.825, 11.0)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 61784.3347)
    ops.uniaxialMaterial('Elastic', 404007, 101197.98125)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 12.85, 4.65, 11.0, '-mass', 12.706100917431192, 12.706100917431192, 12.706100917431192, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 12.475, 4.65, 11.0)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 12.85, 4.65, 10.75)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 12.85, 4.525, 11.0)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 12.85, 4.775, 11.0)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 30146.7354)
    ops.uniaxialMaterial('Elastic', 404008, 65610.2601)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 9.3, 11.0, '-mass', 12.49066513761468, 12.49066513761468, 12.49066513761468, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.375, 9.3, 11.0)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 9.3, 10.75)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 9.175, 11.0)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 9.425, 11.0)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 29930.44245)
    ops.uniaxialMaterial('Elastic', 404009, 65136.3415)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 4.95, 9.3, 11.0, '-mass', 18.97494138634047, 18.97494138634047, 18.97494138634047, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 4.55, 9.3, 11.0)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 5.35, 9.3, 11.0)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 4.95, 9.3, 10.75)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 4.95, 9.125, 11.0)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 4.95, 9.475, 11.0)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 57934.01685)
    ops.uniaxialMaterial('Elastic', 404010, 92046.21475)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 7.9, 9.3, 11.0, '-mass', 18.974941386340465, 18.974941386340465, 18.974941386340465, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 7.5, 9.3, 11.0)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 8.3, 9.3, 11.0)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 7.9, 9.3, 10.75)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 7.9, 9.125, 11.0)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 7.9, 9.475, 11.0)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 57934.01685)
    ops.uniaxialMaterial('Elastic', 404011, 92046.21475)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 12.85, 9.3, 11.0, '-mass', 12.490665137614677, 12.490665137614677, 12.490665137614677, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 12.475, 9.3, 11.0)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 12.85, 9.3, 10.75)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 12.85, 9.175, 11.0)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 12.85, 9.425, 11.0)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 29930.44245)
    ops.uniaxialMaterial('Elastic', 404012, 65136.3415)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4013, 0.0, 13.95, 11.0, '-mass', 6.310015290519878, 6.310015290519878, 6.310015290519878, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 13.95, 11.0)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 13.95, 10.8)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 13.75, 11.0)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304013, 20587.86125)
    ops.uniaxialMaterial('Elastic', 404013, 26860.95085)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4014, 4.95, 13.95, 11.0, '-mass', 9.705440876656473, 9.705440876656473, 9.705440876656473, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 4.8, 13.95, 11.0)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 5.1, 13.95, 11.0)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 4.95, 13.95, 10.8)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 4.95, 13.675, 11.0)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304014, 43864.89925)
    ops.uniaxialMaterial('Elastic', 404014, 39141.62705)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4015, 7.9, 13.95, 11.0, '-mass', 9.705440876656471, 9.705440876656471, 9.705440876656471, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 7.75, 13.95, 11.0)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 8.05, 13.95, 11.0)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 7.9, 13.95, 10.8)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 7.9, 13.675, 11.0)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304015, 43864.89925)
    ops.uniaxialMaterial('Elastic', 404015, 39141.62705)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4016, 12.85, 13.95, 11.0, '-mass', 6.3100152905198765, 6.3100152905198765, 6.3100152905198765, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 12.725, 13.95, 11.0)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 12.85, 13.95, 10.8)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 12.85, 13.75, 11.0)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304016, 20587.86125)
    ops.uniaxialMaterial('Elastic', 404016, 26860.95085)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)
