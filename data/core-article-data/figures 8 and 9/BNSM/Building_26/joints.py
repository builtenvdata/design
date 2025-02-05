import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (3, 0, 0.5)
    # Central joint node
    ops.node(4033, 11.55, 0.0, 1.475, '-mass', 3.784301732925582, 3.784301732925582, 3.784301732925582, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34033, 11.725, 0.0, 1.475)
    ops.element('elasticBeamColumn', 34033, 4033, 34033, 99999, 88888)
    ops.node(24033, 11.55, 0.0, 1.275)
    ops.element('elasticBeamColumn', 24033, 24033, 4033, 99999, 99999)
    ops.node(74033, 11.55, 0.0, 1.675)
    ops.element('elasticBeamColumn', 74033, 4033, 74033, 99999, 99999)

    # Joint grid ids (x, y, z): (4, 0, 0.5)
    # Central joint node
    ops.node(4034, 14.6, 0.0, 1.475, '-mass', 3.784301732925582, 3.784301732925582, 3.784301732925582, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54034, 14.425, 0.0, 1.475)
    ops.element('elasticBeamColumn', 54034, 54034, 4034, 99999, 88888)
    ops.node(24034, 14.6, 0.0, 1.275)
    ops.element('elasticBeamColumn', 24034, 24034, 4034, 99999, 99999)
    ops.node(74034, 14.6, 0.0, 1.675)
    ops.element('elasticBeamColumn', 74034, 4034, 74034, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    # Central joint node
    ops.node(4035, 11.55, 0.0, 4.425, '-mass', 3.8775739041794055, 3.8775739041794055, 3.8775739041794055, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34035, 11.725, 0.0, 4.425)
    ops.element('elasticBeamColumn', 34035, 4035, 34035, 99999, 88888)
    ops.node(24035, 11.55, 0.0, 4.175)
    ops.element('elasticBeamColumn', 24035, 24035, 4035, 99999, 99999)
    ops.node(74035, 11.55, 0.0, 4.675)
    ops.element('elasticBeamColumn', 74035, 4035, 74035, 99999, 99999)

    # Joint grid ids (x, y, z): (4, 0, 1.5)
    # Central joint node
    ops.node(4036, 14.6, 0.0, 4.425, '-mass', 3.8775739041794055, 3.8775739041794055, 3.8775739041794055, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54036, 14.425, 0.0, 4.425)
    ops.element('elasticBeamColumn', 54036, 54036, 4036, 99999, 88888)
    ops.node(24036, 14.6, 0.0, 4.175)
    ops.element('elasticBeamColumn', 24036, 24036, 4036, 99999, 99999)
    ops.node(74036, 14.6, 0.0, 4.675)
    ops.element('elasticBeamColumn', 74036, 4036, 74036, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    # Central joint node
    ops.node(4037, 11.55, 0.0, 7.375, '-mass', 3.493170234454635, 3.493170234454635, 3.493170234454635, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34037, 11.675, 0.0, 7.375)
    ops.element('elasticBeamColumn', 34037, 4037, 34037, 99999, 88888)
    ops.node(24037, 11.55, 0.0, 7.175)
    ops.element('elasticBeamColumn', 24037, 24037, 4037, 99999, 99999)
    ops.node(74037, 11.55, 0.0, 7.575)
    ops.element('elasticBeamColumn', 74037, 4037, 74037, 99999, 99999)

    # Joint grid ids (x, y, z): (4, 0, 2.5)
    # Central joint node
    ops.node(4038, 14.6, 0.0, 7.375, '-mass', 3.493170234454635, 3.493170234454635, 3.493170234454635, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54038, 14.475, 0.0, 7.375)
    ops.element('elasticBeamColumn', 54038, 54038, 4038, 99999, 88888)
    ops.node(24038, 14.6, 0.0, 7.175)
    ops.element('elasticBeamColumn', 24038, 24038, 4038, 99999, 99999)
    ops.node(74038, 14.6, 0.0, 7.575)
    ops.element('elasticBeamColumn', 74038, 4038, 74038, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    # Central joint node
    ops.node(4039, 11.55, 0.0, 10.325, '-mass', 3.493170234454635, 3.493170234454635, 3.493170234454635, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34039, 11.675, 0.0, 10.325)
    ops.element('elasticBeamColumn', 34039, 4039, 34039, 99999, 88888)
    ops.node(24039, 11.55, 0.0, 10.125)
    ops.element('elasticBeamColumn', 24039, 24039, 4039, 99999, 99999)
    ops.node(74039, 11.55, 0.0, 10.525)
    ops.element('elasticBeamColumn', 74039, 4039, 74039, 99999, 99999)

    # Joint grid ids (x, y, z): (4, 0, 3.5)
    # Central joint node
    ops.node(4040, 14.6, 0.0, 10.325, '-mass', 3.493170234454635, 3.493170234454635, 3.493170234454635, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54040, 14.475, 0.0, 10.325)
    ops.element('elasticBeamColumn', 54040, 54040, 4040, 99999, 88888)
    ops.node(24040, 14.6, 0.0, 10.125)
    ops.element('elasticBeamColumn', 24040, 24040, 4040, 99999, 99999)
    ops.node(74040, 14.6, 0.0, 10.525)
    ops.element('elasticBeamColumn', 74040, 4040, 74040, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 2.95, '-mass', 9.15369138634047, 9.15369138634047, 9.15369138634047, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.15, 0.0, 2.95)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.7)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.2)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.15, 2.95)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 48743.5042)
    ops.uniaxialMaterial('Elastic', 401001, 37154.5799)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 3.85, 0.0, 2.95, '-mass', 14.150807849133535, 14.150807849133535, 14.150807849133535, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 3.65, 0.0, 2.95)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 4.05, 0.0, 2.95)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 3.85, 0.0, 2.7)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 3.85, 0.0, 3.2)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 3.85, 0.2, 2.95)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 83668.3067)
    ops.uniaxialMaterial('Elastic', 401002, 90691.1797)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 7.7, 0.0, 2.95, '-mass', 14.150807849133535, 14.150807849133535, 14.150807849133535, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 7.5, 0.0, 2.95)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 7.9, 0.0, 2.95)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 7.7, 0.0, 2.7)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 7.7, 0.0, 3.2)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 7.7, 0.2, 2.95)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 83668.3067)
    ops.uniaxialMaterial('Elastic', 401003, 90691.1797)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 11.55, 0.0, 2.95, '-mass', 9.391458970438329, 9.391458970438329, 9.391458970438329, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 11.375, 0.0, 2.95)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(31004, 11.725, 0.0, 2.95)
    ops.element('elasticBeamColumn', 31004, 1004, 31004, 99999, 88888)
    ops.node(21004, 11.55, 0.0, 2.7)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 11.55, 0.0, 3.2)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 11.55, 0.175, 2.95)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 81496.49015)
    ops.uniaxialMaterial('Elastic', 401004, 84268.6849)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    # Central joint node
    ops.node(1005, 14.6, 0.0, 2.95, '-mass', 9.391458970438327, 9.391458970438327, 9.391458970438327, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51005, 14.425, 0.0, 2.95)
    ops.element('elasticBeamColumn', 51005, 51005, 1005, 99999, 88888)
    ops.node(31005, 14.775, 0.0, 2.95)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 14.6, 0.0, 2.7)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 14.6, 0.0, 3.2)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(41005, 14.6, 0.175, 2.95)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 81496.49015)
    ops.uniaxialMaterial('Elastic', 401005, 84268.6849)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    # Central joint node
    ops.node(1006, 18.45, 0.0, 2.95, '-mass', 14.150807849133535, 14.150807849133535, 14.150807849133535, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 18.25, 0.0, 2.95)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 18.65, 0.0, 2.95)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 18.45, 0.0, 2.7)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 18.45, 0.0, 3.2)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(41006, 18.45, 0.2, 2.95)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 83668.3067)
    ops.uniaxialMaterial('Elastic', 401006, 90691.1797)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 0, 1)
    # Central joint node
    ops.node(1007, 22.3, 0.0, 2.95, '-mass', 14.150807849133535, 14.150807849133535, 14.150807849133535, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 22.1, 0.0, 2.95)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 22.5, 0.0, 2.95)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 22.3, 0.0, 2.7)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 22.3, 0.0, 3.2)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(41007, 22.3, 0.2, 2.95)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 83668.3067)
    ops.uniaxialMaterial('Elastic', 401007, 90691.1797)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 0, 1)
    # Central joint node
    ops.node(1008, 26.15, 0.0, 2.95, '-mass', 9.153691386340467, 9.153691386340467, 9.153691386340467, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 26.0, 0.0, 2.95)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 26.15, 0.0, 2.7)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 26.15, 0.0, 3.2)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(41008, 26.15, 0.15, 2.95)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 48743.5042)
    ops.uniaxialMaterial('Elastic', 401008, 37154.5799)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1009, 0.0, 4.8, 2.95, '-mass', 15.251011722731903, 15.251011722731903, 15.251011722731903, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.2, 4.8, 2.95)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 4.8, 2.7)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 4.8, 3.2)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 4.6, 2.95)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 5.0, 2.95)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 119231.4561)
    ops.uniaxialMaterial('Elastic', 401009, 85199.13155)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1010, 3.85, 4.8, 2.95, '-mass', 21.629546381243628, 21.629546381243628, 21.629546381243628, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 3.625, 4.8, 2.95)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 4.075, 4.8, 2.95)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 3.85, 4.8, 2.7)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 3.85, 4.8, 3.2)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 3.85, 4.575, 2.95)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 3.85, 5.025, 2.95)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 160407.55025)
    ops.uniaxialMaterial('Elastic', 401010, 160407.55025)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1011, 7.7, 4.8, 2.95, '-mass', 21.629546381243628, 21.629546381243628, 21.629546381243628, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 7.475, 4.8, 2.95)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 7.925, 4.8, 2.95)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 7.7, 4.8, 2.7)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 7.7, 4.8, 3.2)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 7.7, 4.575, 2.95)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 7.7, 5.025, 2.95)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 160407.55025)
    ops.uniaxialMaterial('Elastic', 401011, 160407.55025)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1012, 11.55, 4.8, 2.95, '-mass', 20.1684365443425, 20.1684365443425, 20.1684365443425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 11.325, 4.8, 2.95)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(31012, 11.775, 4.8, 2.95)
    ops.element('elasticBeamColumn', 31012, 1012, 31012, 99999, 88888)
    ops.node(21012, 11.55, 4.8, 2.7)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 11.55, 4.8, 3.2)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 11.55, 4.575, 2.95)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 11.55, 5.025, 2.95)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 155066.97545)
    ops.uniaxialMaterial('Elastic', 401012, 155066.97545)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    # Central joint node
    ops.node(1013, 14.6, 4.8, 2.95, '-mass', 20.1684365443425, 20.1684365443425, 20.1684365443425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51013, 14.375, 4.8, 2.95)
    ops.element('elasticBeamColumn', 51013, 51013, 1013, 99999, 88888)
    ops.node(31013, 14.825, 4.8, 2.95)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 14.6, 4.8, 2.7)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 14.6, 4.8, 3.2)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 14.6, 4.575, 2.95)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 14.6, 5.025, 2.95)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301013, 155066.97545)
    ops.uniaxialMaterial('Elastic', 401013, 155066.97545)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    # Central joint node
    ops.node(1014, 18.45, 4.8, 2.95, '-mass', 21.629546381243628, 21.629546381243628, 21.629546381243628, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 18.225, 4.8, 2.95)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 18.675, 4.8, 2.95)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 18.45, 4.8, 2.7)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 18.45, 4.8, 3.2)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 18.45, 4.575, 2.95)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 18.45, 5.025, 2.95)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301014, 160407.55025)
    ops.uniaxialMaterial('Elastic', 401014, 160407.55025)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 1, 1)
    # Central joint node
    ops.node(1015, 22.3, 4.8, 2.95, '-mass', 21.629546381243628, 21.629546381243628, 21.629546381243628, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 22.075, 4.8, 2.95)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 22.525, 4.8, 2.95)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 22.3, 4.8, 2.7)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 22.3, 4.8, 3.2)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 22.3, 4.575, 2.95)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 22.3, 5.025, 2.95)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301015, 160407.55025)
    ops.uniaxialMaterial('Elastic', 401015, 160407.55025)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 1, 1)
    # Central joint node
    ops.node(1016, 26.15, 4.8, 2.95, '-mass', 15.251011722731903, 15.251011722731903, 15.251011722731903, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 25.95, 4.8, 2.95)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 26.15, 4.8, 2.7)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 26.15, 4.8, 3.2)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 26.15, 4.6, 2.95)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 26.15, 5.0, 2.95)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301016, 119231.4561)
    ops.uniaxialMaterial('Elastic', 401016, 85199.13155)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1017, 0.0, 9.6, 2.95, '-mass', 14.991990316004077, 14.991990316004077, 14.991990316004077, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31017, 0.2, 9.6, 2.95)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 0.0, 9.6, 2.7)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 0.0, 9.6, 3.2)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 0.0, 9.4, 2.95)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 0.0, 9.8, 2.95)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301017, 118814.44725)
    ops.uniaxialMaterial('Elastic', 401017, 55657.38115)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1018, 3.85, 9.6, 2.95, '-mass', 21.11150356778797, 21.11150356778797, 21.11150356778797, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 3.625, 9.6, 2.95)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(31018, 4.075, 9.6, 2.95)
    ops.element('elasticBeamColumn', 31018, 1018, 31018, 99999, 88888)
    ops.node(21018, 3.85, 9.6, 2.7)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 3.85, 9.6, 3.2)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 3.85, 9.375, 2.95)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 3.85, 9.825, 2.95)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301018, 155150.48685)
    ops.uniaxialMaterial('Elastic', 401018, 106721.4839)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1019, 7.7, 9.6, 2.95, '-mass', 21.11150356778797, 21.11150356778797, 21.11150356778797, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51019, 7.475, 9.6, 2.95)
    ops.element('elasticBeamColumn', 51019, 51019, 1019, 99999, 88888)
    ops.node(31019, 7.925, 9.6, 2.95)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 7.7, 9.6, 2.7)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 7.7, 9.6, 3.2)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 7.7, 9.375, 2.95)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    ops.node(41019, 7.7, 9.825, 2.95)
    ops.element('elasticBeamColumn', 41019, 1019, 41019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301019, 155150.48685)
    ops.uniaxialMaterial('Elastic', 401019, 106721.4839)
    ops.section('Aggregator', 11019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401019, 'My', 301019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11019, 1019, 11019, 11019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1020, 11.55, 9.6, 2.95, '-mass', 18.39809378185525, 18.39809378185525, 18.39809378185525, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 11.35, 9.6, 2.95)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(31020, 11.75, 9.6, 2.95)
    ops.element('elasticBeamColumn', 31020, 1020, 31020, 99999, 88888)
    ops.node(21020, 11.55, 9.6, 2.7)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 11.55, 9.6, 3.2)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 11.55, 9.4, 2.95)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    ops.node(41020, 11.55, 9.8, 2.95)
    ops.element('elasticBeamColumn', 41020, 1020, 41020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301020, 133943.80175)
    ops.uniaxialMaterial('Elastic', 401020, 89488.4241)
    ops.section('Aggregator', 11020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401020, 'My', 301020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11020, 1020, 11020, 11020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    # Central joint node
    ops.node(1021, 14.6, 9.6, 2.95, '-mass', 18.39809378185525, 18.39809378185525, 18.39809378185525, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51021, 14.4, 9.6, 2.95)
    ops.element('elasticBeamColumn', 51021, 51021, 1021, 99999, 88888)
    ops.node(31021, 14.8, 9.6, 2.95)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 14.6, 9.6, 2.7)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 14.6, 9.6, 3.2)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 14.6, 9.4, 2.95)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    ops.node(41021, 14.6, 9.8, 2.95)
    ops.element('elasticBeamColumn', 41021, 1021, 41021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301021, 133943.80175)
    ops.uniaxialMaterial('Elastic', 401021, 89488.4241)
    ops.section('Aggregator', 11021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401021, 'My', 301021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11021, 1021, 11021, 11021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    # Central joint node
    ops.node(1022, 18.45, 9.6, 2.95, '-mass', 21.111503567787974, 21.111503567787974, 21.111503567787974, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 18.225, 9.6, 2.95)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 18.675, 9.6, 2.95)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 18.45, 9.6, 2.7)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 18.45, 9.6, 3.2)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 18.45, 9.375, 2.95)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    ops.node(41022, 18.45, 9.825, 2.95)
    ops.element('elasticBeamColumn', 41022, 1022, 41022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301022, 155150.48685)
    ops.uniaxialMaterial('Elastic', 401022, 106721.4839)
    ops.section('Aggregator', 11022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401022, 'My', 301022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11022, 1022, 11022, 11022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 2, 1)
    # Central joint node
    ops.node(1023, 22.3, 9.6, 2.95, '-mass', 21.11150356778797, 21.11150356778797, 21.11150356778797, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 22.075, 9.6, 2.95)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 22.525, 9.6, 2.95)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 22.3, 9.6, 2.7)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 22.3, 9.6, 3.2)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 22.3, 9.375, 2.95)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    ops.node(41023, 22.3, 9.825, 2.95)
    ops.element('elasticBeamColumn', 41023, 1023, 41023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301023, 155150.48685)
    ops.uniaxialMaterial('Elastic', 401023, 106721.4839)
    ops.section('Aggregator', 11023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401023, 'My', 301023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11023, 1023, 11023, 11023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 2, 1)
    # Central joint node
    ops.node(1024, 26.15, 9.6, 2.95, '-mass', 14.991990316004074, 14.991990316004074, 14.991990316004074, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 25.95, 9.6, 2.95)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 26.15, 9.6, 2.7)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 26.15, 9.6, 3.2)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 26.15, 9.4, 2.95)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    ops.node(41024, 26.15, 9.8, 2.95)
    ops.element('elasticBeamColumn', 41024, 1024, 41024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301024, 118814.44725)
    ops.uniaxialMaterial('Elastic', 401024, 55657.38115)
    ops.section('Aggregator', 11024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401024, 'My', 301024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11024, 1024, 11024, 11024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1025, 0.0, 14.4, 2.95, '-mass', 9.153691386340471, 9.153691386340471, 9.153691386340471, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31025, 0.15, 14.4, 2.95)
    ops.element('elasticBeamColumn', 31025, 1025, 31025, 99999, 88888)
    ops.node(21025, 0.0, 14.4, 2.7)
    ops.element('elasticBeamColumn', 21025, 21025, 1025, 99999, 99999)
    ops.node(71025, 0.0, 14.4, 3.2)
    ops.element('elasticBeamColumn', 71025, 1025, 71025, 99999, 99999)
    ops.node(61025, 0.0, 14.25, 2.95)
    ops.element('elasticBeamColumn', 61025, 61025, 1025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301025, 48743.5042)
    ops.uniaxialMaterial('Elastic', 401025, 37154.5799)
    ops.section('Aggregator', 11025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401025, 'My', 301025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11025, 1025, 11025, 11025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1026, 3.85, 14.4, 2.95, '-mass', 14.150807849133537, 14.150807849133537, 14.150807849133537, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51026, 3.65, 14.4, 2.95)
    ops.element('elasticBeamColumn', 51026, 51026, 1026, 99999, 88888)
    ops.node(31026, 4.05, 14.4, 2.95)
    ops.element('elasticBeamColumn', 31026, 1026, 31026, 99999, 88888)
    ops.node(21026, 3.85, 14.4, 2.7)
    ops.element('elasticBeamColumn', 21026, 21026, 1026, 99999, 99999)
    ops.node(71026, 3.85, 14.4, 3.2)
    ops.element('elasticBeamColumn', 71026, 1026, 71026, 99999, 99999)
    ops.node(61026, 3.85, 14.2, 2.95)
    ops.element('elasticBeamColumn', 61026, 61026, 1026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301026, 83668.3067)
    ops.uniaxialMaterial('Elastic', 401026, 90691.1797)
    ops.section('Aggregator', 11026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401026, 'My', 301026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11026, 1026, 11026, 11026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1027, 7.7, 14.4, 2.95, '-mass', 14.150807849133537, 14.150807849133537, 14.150807849133537, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51027, 7.5, 14.4, 2.95)
    ops.element('elasticBeamColumn', 51027, 51027, 1027, 99999, 88888)
    ops.node(31027, 7.9, 14.4, 2.95)
    ops.element('elasticBeamColumn', 31027, 1027, 31027, 99999, 88888)
    ops.node(21027, 7.7, 14.4, 2.7)
    ops.element('elasticBeamColumn', 21027, 21027, 1027, 99999, 99999)
    ops.node(71027, 7.7, 14.4, 3.2)
    ops.element('elasticBeamColumn', 71027, 1027, 71027, 99999, 99999)
    ops.node(61027, 7.7, 14.2, 2.95)
    ops.element('elasticBeamColumn', 61027, 61027, 1027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301027, 83668.3067)
    ops.uniaxialMaterial('Elastic', 401027, 90691.1797)
    ops.section('Aggregator', 11027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401027, 'My', 301027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11027, 1027, 11027, 11027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1028, 11.55, 14.4, 2.95, '-mass', 12.34736493374108, 12.34736493374108, 12.34736493374108, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51028, 11.375, 14.4, 2.95)
    ops.element('elasticBeamColumn', 51028, 51028, 1028, 99999, 88888)
    ops.node(31028, 11.725, 14.4, 2.95)
    ops.element('elasticBeamColumn', 31028, 1028, 31028, 99999, 88888)
    ops.node(21028, 11.55, 14.4, 2.7)
    ops.element('elasticBeamColumn', 21028, 21028, 1028, 99999, 99999)
    ops.node(71028, 11.55, 14.4, 3.2)
    ops.element('elasticBeamColumn', 71028, 1028, 71028, 99999, 99999)
    ops.node(61028, 11.55, 14.225, 2.95)
    ops.element('elasticBeamColumn', 61028, 61028, 1028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301028, 69074.80355)
    ops.uniaxialMaterial('Elastic', 401028, 74498.42305)
    ops.section('Aggregator', 11028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401028, 'My', 301028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11028, 1028, 11028, 11028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 1)
    # Central joint node
    ops.node(1029, 14.6, 14.4, 2.95, '-mass', 12.347364933741078, 12.347364933741078, 12.347364933741078, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51029, 14.425, 14.4, 2.95)
    ops.element('elasticBeamColumn', 51029, 51029, 1029, 99999, 88888)
    ops.node(31029, 14.775, 14.4, 2.95)
    ops.element('elasticBeamColumn', 31029, 1029, 31029, 99999, 88888)
    ops.node(21029, 14.6, 14.4, 2.7)
    ops.element('elasticBeamColumn', 21029, 21029, 1029, 99999, 99999)
    ops.node(71029, 14.6, 14.4, 3.2)
    ops.element('elasticBeamColumn', 71029, 1029, 71029, 99999, 99999)
    ops.node(61029, 14.6, 14.225, 2.95)
    ops.element('elasticBeamColumn', 61029, 61029, 1029, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301029, 69074.80355)
    ops.uniaxialMaterial('Elastic', 401029, 74498.42305)
    ops.section('Aggregator', 11029, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401029, 'My', 301029, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11029, 1029, 11029, 11029, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 1)
    # Central joint node
    ops.node(1030, 18.45, 14.4, 2.95, '-mass', 14.150807849133537, 14.150807849133537, 14.150807849133537, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51030, 18.25, 14.4, 2.95)
    ops.element('elasticBeamColumn', 51030, 51030, 1030, 99999, 88888)
    ops.node(31030, 18.65, 14.4, 2.95)
    ops.element('elasticBeamColumn', 31030, 1030, 31030, 99999, 88888)
    ops.node(21030, 18.45, 14.4, 2.7)
    ops.element('elasticBeamColumn', 21030, 21030, 1030, 99999, 99999)
    ops.node(71030, 18.45, 14.4, 3.2)
    ops.element('elasticBeamColumn', 71030, 1030, 71030, 99999, 99999)
    ops.node(61030, 18.45, 14.2, 2.95)
    ops.element('elasticBeamColumn', 61030, 61030, 1030, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301030, 83668.3067)
    ops.uniaxialMaterial('Elastic', 401030, 90691.1797)
    ops.section('Aggregator', 11030, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401030, 'My', 301030, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11030, 1030, 11030, 11030, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 3, 1)
    # Central joint node
    ops.node(1031, 22.3, 14.4, 2.95, '-mass', 14.150807849133537, 14.150807849133537, 14.150807849133537, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51031, 22.1, 14.4, 2.95)
    ops.element('elasticBeamColumn', 51031, 51031, 1031, 99999, 88888)
    ops.node(31031, 22.5, 14.4, 2.95)
    ops.element('elasticBeamColumn', 31031, 1031, 31031, 99999, 88888)
    ops.node(21031, 22.3, 14.4, 2.7)
    ops.element('elasticBeamColumn', 21031, 21031, 1031, 99999, 99999)
    ops.node(71031, 22.3, 14.4, 3.2)
    ops.element('elasticBeamColumn', 71031, 1031, 71031, 99999, 99999)
    ops.node(61031, 22.3, 14.2, 2.95)
    ops.element('elasticBeamColumn', 61031, 61031, 1031, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301031, 83668.3067)
    ops.uniaxialMaterial('Elastic', 401031, 90691.1797)
    ops.section('Aggregator', 11031, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401031, 'My', 301031, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11031, 1031, 11031, 11031, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 3, 1)
    # Central joint node
    ops.node(1032, 26.15, 14.4, 2.95, '-mass', 9.15369138634047, 9.15369138634047, 9.15369138634047, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51032, 26.0, 14.4, 2.95)
    ops.element('elasticBeamColumn', 51032, 51032, 1032, 99999, 88888)
    ops.node(21032, 26.15, 14.4, 2.7)
    ops.element('elasticBeamColumn', 21032, 21032, 1032, 99999, 99999)
    ops.node(71032, 26.15, 14.4, 3.2)
    ops.element('elasticBeamColumn', 71032, 1032, 71032, 99999, 99999)
    ops.node(61032, 26.15, 14.25, 2.95)
    ops.element('elasticBeamColumn', 61032, 61032, 1032, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301032, 48743.5042)
    ops.uniaxialMaterial('Elastic', 401032, 37154.5799)
    ops.section('Aggregator', 11032, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401032, 'My', 301032, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11032, 1032, 11032, 11032, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 5.9, '-mass', 9.054455912334353, 9.054455912334353, 9.054455912334353, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.15, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.15, 5.9)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 42025.68045)
    ops.uniaxialMaterial('Elastic', 402001, 31938.11015)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 3.85, 0.0, 5.9, '-mass', 14.015486748216105, 14.015486748216105, 14.015486748216105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 3.65, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 4.05, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 3.85, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 3.85, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 3.85, 0.2, 5.9)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 72101.0554)
    ops.uniaxialMaterial('Elastic', 402002, 77465.1345)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 7.7, 0.0, 5.9, '-mass', 14.015486748216105, 14.015486748216105, 14.015486748216105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 7.5, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 7.9, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 7.7, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 7.7, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 7.7, 0.2, 5.9)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 72101.0554)
    ops.uniaxialMaterial('Elastic', 402003, 77465.1345)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 11.55, 0.0, 5.9, '-mass', 9.283202089704384, 9.283202089704384, 9.283202089704384, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 11.375, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(32004, 11.725, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32004, 2004, 32004, 99999, 88888)
    ops.node(22004, 11.55, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 11.55, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 11.55, 0.175, 5.9)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 69644.73545)
    ops.uniaxialMaterial('Elastic', 402004, 71254.2154)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    # Central joint node
    ops.node(2005, 14.6, 0.0, 5.9, '-mass', 9.283202089704382, 9.283202089704382, 9.283202089704382, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52005, 14.425, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52005, 52005, 2005, 99999, 88888)
    ops.node(32005, 14.775, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 14.6, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 14.6, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(42005, 14.6, 0.175, 5.9)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 69644.73545)
    ops.uniaxialMaterial('Elastic', 402005, 71254.2154)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    # Central joint node
    ops.node(2006, 18.45, 0.0, 5.9, '-mass', 14.015486748216105, 14.015486748216105, 14.015486748216105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 18.25, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 18.65, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 18.45, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 18.45, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(42006, 18.45, 0.2, 5.9)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 72101.0554)
    ops.uniaxialMaterial('Elastic', 402006, 77465.1345)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 0, 2)
    # Central joint node
    ops.node(2007, 22.3, 0.0, 5.9, '-mass', 14.015486748216105, 14.015486748216105, 14.015486748216105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 22.1, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 22.5, 0.0, 5.9)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 22.3, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 22.3, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(42007, 22.3, 0.2, 5.9)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 72101.0554)
    ops.uniaxialMaterial('Elastic', 402007, 77465.1345)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 0, 2)
    # Central joint node
    ops.node(2008, 26.15, 0.0, 5.9, '-mass', 9.054455912334351, 9.054455912334351, 9.054455912334351, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 26.0, 0.0, 5.9)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 26.15, 0.0, 5.65)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 26.15, 0.0, 6.15)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(42008, 26.15, 0.15, 5.9)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 42025.68045)
    ops.uniaxialMaterial('Elastic', 402008, 31938.11015)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2009, 0.0, 4.8, 5.9, '-mass', 14.99795361875637, 14.99795361875637, 14.99795361875637, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.2, 4.8, 5.9)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 4.8, 5.65)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 4.8, 6.15)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 4.6, 5.9)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 5.0, 5.9)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 101683.4924)
    ops.uniaxialMaterial('Elastic', 402009, 55990.5134)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2010, 3.85, 4.8, 5.9, '-mass', 21.105387359836904, 21.105387359836904, 21.105387359836904, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 3.625, 4.8, 5.9)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 4.075, 4.8, 5.9)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 3.85, 4.8, 5.65)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 3.85, 4.8, 6.15)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 3.85, 4.575, 5.9)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 3.85, 5.025, 5.9)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 137425.406)
    ops.uniaxialMaterial('Elastic', 402010, 106549.17235)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2011, 7.7, 4.8, 5.9, '-mass', 21.105387359836904, 21.105387359836904, 21.105387359836904, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 7.475, 4.8, 5.9)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 7.925, 4.8, 5.9)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 7.7, 4.8, 5.65)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 7.7, 4.8, 6.15)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 7.7, 4.575, 5.9)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 7.7, 5.025, 5.9)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 137425.406)
    ops.uniaxialMaterial('Elastic', 402011, 106549.17235)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2012, 11.55, 4.8, 5.9, '-mass', 19.668742354740058, 19.668742354740058, 19.668742354740058, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 11.325, 4.8, 5.9)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(32012, 11.775, 4.8, 5.9)
    ops.element('elasticBeamColumn', 32012, 2012, 32012, 99999, 88888)
    ops.node(22012, 11.55, 4.8, 5.65)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 11.55, 4.8, 6.15)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 11.55, 4.575, 5.9)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 11.55, 5.025, 5.9)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 133361.3257)
    ops.uniaxialMaterial('Elastic', 402012, 103398.19465)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    # Central joint node
    ops.node(2013, 14.6, 4.8, 5.9, '-mass', 19.668742354740058, 19.668742354740058, 19.668742354740058, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52013, 14.375, 4.8, 5.9)
    ops.element('elasticBeamColumn', 52013, 52013, 2013, 99999, 88888)
    ops.node(32013, 14.825, 4.8, 5.9)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 14.6, 4.8, 5.65)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 14.6, 4.8, 6.15)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 14.6, 4.575, 5.9)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 14.6, 5.025, 5.9)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302013, 133361.3257)
    ops.uniaxialMaterial('Elastic', 402013, 103398.19465)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    # Central joint node
    ops.node(2014, 18.45, 4.8, 5.9, '-mass', 21.105387359836904, 21.105387359836904, 21.105387359836904, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 18.225, 4.8, 5.9)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 18.675, 4.8, 5.9)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 18.45, 4.8, 5.65)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 18.45, 4.8, 6.15)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 18.45, 4.575, 5.9)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 18.45, 5.025, 5.9)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302014, 137425.406)
    ops.uniaxialMaterial('Elastic', 402014, 106549.17235)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 1, 2)
    # Central joint node
    ops.node(2015, 22.3, 4.8, 5.9, '-mass', 21.105387359836904, 21.105387359836904, 21.105387359836904, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 22.075, 4.8, 5.9)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 22.525, 4.8, 5.9)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 22.3, 4.8, 5.65)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 22.3, 4.8, 6.15)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 22.3, 4.575, 5.9)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 22.3, 5.025, 5.9)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302015, 137425.406)
    ops.uniaxialMaterial('Elastic', 402015, 106549.17235)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 1, 2)
    # Central joint node
    ops.node(2016, 26.15, 4.8, 5.9, '-mass', 14.99795361875637, 14.99795361875637, 14.99795361875637, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 25.95, 4.8, 5.9)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 26.15, 4.8, 5.65)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 26.15, 4.8, 6.15)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 26.15, 4.6, 5.9)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 26.15, 5.0, 5.9)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302016, 101683.4924)
    ops.uniaxialMaterial('Elastic', 402016, 55990.5134)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2017, 0.0, 9.6, 5.9, '-mass', 14.856669215086646, 14.856669215086646, 14.856669215086646, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32017, 0.2, 9.6, 5.9)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 0.0, 9.6, 5.65)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 0.0, 9.6, 6.15)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 0.0, 9.4, 5.9)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 0.0, 9.8, 5.9)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302017, 101399.67245)
    ops.uniaxialMaterial('Elastic', 402017, 47759.5363)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2018, 3.85, 9.6, 5.9, '-mass', 20.822818552497452, 20.822818552497452, 20.822818552497452, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 3.625, 9.6, 5.9)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(32018, 4.075, 9.6, 5.9)
    ops.element('elasticBeamColumn', 32018, 2018, 32018, 99999, 88888)
    ops.node(22018, 3.85, 9.6, 5.65)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 3.85, 9.6, 6.15)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 3.85, 9.375, 5.9)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 3.85, 9.825, 5.9)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302018, 133008.6822)
    ops.uniaxialMaterial('Elastic', 402018, 91509.49525)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2019, 7.7, 9.6, 5.9, '-mass', 20.822818552497452, 20.822818552497452, 20.822818552497452, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52019, 7.475, 9.6, 5.9)
    ops.element('elasticBeamColumn', 52019, 52019, 2019, 99999, 88888)
    ops.node(32019, 7.925, 9.6, 5.9)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 7.7, 9.6, 5.65)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 7.7, 9.6, 6.15)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 7.7, 9.375, 5.9)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    ops.node(42019, 7.7, 9.825, 5.9)
    ops.element('elasticBeamColumn', 42019, 2019, 42019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302019, 133008.6822)
    ops.uniaxialMaterial('Elastic', 402019, 91509.49525)
    ops.section('Aggregator', 12019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402019, 'My', 302019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12019, 2019, 12019, 12019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2020, 11.55, 9.6, 5.9, '-mass', 18.262772680937818, 18.262772680937818, 18.262772680937818, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 11.35, 9.6, 5.9)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(32020, 11.75, 9.6, 5.9)
    ops.element('elasticBeamColumn', 32020, 2020, 32020, 99999, 88888)
    ops.node(22020, 11.55, 9.6, 5.65)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 11.55, 9.6, 6.15)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 11.55, 9.4, 5.9)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    ops.node(42020, 11.55, 9.8, 5.9)
    ops.element('elasticBeamColumn', 42020, 2020, 42020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302020, 114783.2764)
    ops.uniaxialMaterial('Elastic', 402020, 76687.19555)
    ops.section('Aggregator', 12020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402020, 'My', 302020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12020, 2020, 12020, 12020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    # Central joint node
    ops.node(2021, 14.6, 9.6, 5.9, '-mass', 18.262772680937818, 18.262772680937818, 18.262772680937818, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52021, 14.4, 9.6, 5.9)
    ops.element('elasticBeamColumn', 52021, 52021, 2021, 99999, 88888)
    ops.node(32021, 14.8, 9.6, 5.9)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 14.6, 9.6, 5.65)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 14.6, 9.6, 6.15)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 14.6, 9.4, 5.9)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    ops.node(42021, 14.6, 9.8, 5.9)
    ops.element('elasticBeamColumn', 42021, 2021, 42021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302021, 114783.2764)
    ops.uniaxialMaterial('Elastic', 402021, 76687.19555)
    ops.section('Aggregator', 12021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402021, 'My', 302021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12021, 2021, 12021, 12021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    # Central joint node
    ops.node(2022, 18.45, 9.6, 5.9, '-mass', 20.822818552497456, 20.822818552497456, 20.822818552497456, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 18.225, 9.6, 5.9)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 18.675, 9.6, 5.9)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 18.45, 9.6, 5.65)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 18.45, 9.6, 6.15)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 18.45, 9.375, 5.9)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    ops.node(42022, 18.45, 9.825, 5.9)
    ops.element('elasticBeamColumn', 42022, 2022, 42022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302022, 133008.6822)
    ops.uniaxialMaterial('Elastic', 402022, 91509.49525)
    ops.section('Aggregator', 12022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402022, 'My', 302022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12022, 2022, 12022, 12022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 2, 2)
    # Central joint node
    ops.node(2023, 22.3, 9.6, 5.9, '-mass', 20.822818552497452, 20.822818552497452, 20.822818552497452, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 22.075, 9.6, 5.9)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 22.525, 9.6, 5.9)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 22.3, 9.6, 5.65)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 22.3, 9.6, 6.15)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 22.3, 9.375, 5.9)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    ops.node(42023, 22.3, 9.825, 5.9)
    ops.element('elasticBeamColumn', 42023, 2023, 42023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302023, 133008.6822)
    ops.uniaxialMaterial('Elastic', 402023, 91509.49525)
    ops.section('Aggregator', 12023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402023, 'My', 302023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12023, 2023, 12023, 12023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 2, 2)
    # Central joint node
    ops.node(2024, 26.15, 9.6, 5.9, '-mass', 14.856669215086644, 14.856669215086644, 14.856669215086644, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 25.95, 9.6, 5.9)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 26.15, 9.6, 5.65)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 26.15, 9.6, 6.15)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 26.15, 9.4, 5.9)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    ops.node(42024, 26.15, 9.8, 5.9)
    ops.element('elasticBeamColumn', 42024, 2024, 42024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302024, 101399.67245)
    ops.uniaxialMaterial('Elastic', 402024, 47759.5363)
    ops.section('Aggregator', 12024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402024, 'My', 302024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12024, 2024, 12024, 12024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2025, 0.0, 14.4, 5.9, '-mass', 9.054455912334355, 9.054455912334355, 9.054455912334355, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32025, 0.15, 14.4, 5.9)
    ops.element('elasticBeamColumn', 32025, 2025, 32025, 99999, 88888)
    ops.node(22025, 0.0, 14.4, 5.65)
    ops.element('elasticBeamColumn', 22025, 22025, 2025, 99999, 99999)
    ops.node(72025, 0.0, 14.4, 6.15)
    ops.element('elasticBeamColumn', 72025, 2025, 72025, 99999, 99999)
    ops.node(62025, 0.0, 14.25, 5.9)
    ops.element('elasticBeamColumn', 62025, 62025, 2025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302025, 42025.68045)
    ops.uniaxialMaterial('Elastic', 402025, 31938.11015)
    ops.section('Aggregator', 12025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402025, 'My', 302025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12025, 2025, 12025, 12025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2026, 3.85, 14.4, 5.9, '-mass', 14.015486748216105, 14.015486748216105, 14.015486748216105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52026, 3.65, 14.4, 5.9)
    ops.element('elasticBeamColumn', 52026, 52026, 2026, 99999, 88888)
    ops.node(32026, 4.05, 14.4, 5.9)
    ops.element('elasticBeamColumn', 32026, 2026, 32026, 99999, 88888)
    ops.node(22026, 3.85, 14.4, 5.65)
    ops.element('elasticBeamColumn', 22026, 22026, 2026, 99999, 99999)
    ops.node(72026, 3.85, 14.4, 6.15)
    ops.element('elasticBeamColumn', 72026, 2026, 72026, 99999, 99999)
    ops.node(62026, 3.85, 14.2, 5.9)
    ops.element('elasticBeamColumn', 62026, 62026, 2026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302026, 72101.0554)
    ops.uniaxialMaterial('Elastic', 402026, 77465.1345)
    ops.section('Aggregator', 12026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402026, 'My', 302026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12026, 2026, 12026, 12026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2027, 7.7, 14.4, 5.9, '-mass', 14.015486748216105, 14.015486748216105, 14.015486748216105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52027, 7.5, 14.4, 5.9)
    ops.element('elasticBeamColumn', 52027, 52027, 2027, 99999, 88888)
    ops.node(32027, 7.9, 14.4, 5.9)
    ops.element('elasticBeamColumn', 32027, 2027, 32027, 99999, 88888)
    ops.node(22027, 7.7, 14.4, 5.65)
    ops.element('elasticBeamColumn', 22027, 22027, 2027, 99999, 99999)
    ops.node(72027, 7.7, 14.4, 6.15)
    ops.element('elasticBeamColumn', 72027, 2027, 72027, 99999, 99999)
    ops.node(62027, 7.7, 14.2, 5.9)
    ops.element('elasticBeamColumn', 62027, 62027, 2027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302027, 72101.0554)
    ops.uniaxialMaterial('Elastic', 402027, 77465.1345)
    ops.section('Aggregator', 12027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402027, 'My', 302027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12027, 2027, 12027, 12027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2028, 11.55, 14.4, 5.9, '-mass', 12.130851172273191, 12.130851172273191, 12.130851172273191, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52028, 11.375, 14.4, 5.9)
    ops.element('elasticBeamColumn', 52028, 52028, 2028, 99999, 88888)
    ops.node(32028, 11.725, 14.4, 5.9)
    ops.element('elasticBeamColumn', 32028, 2028, 32028, 99999, 88888)
    ops.node(22028, 11.55, 14.4, 5.65)
    ops.element('elasticBeamColumn', 22028, 22028, 2028, 99999, 99999)
    ops.node(72028, 11.55, 14.4, 6.15)
    ops.element('elasticBeamColumn', 72028, 2028, 72028, 99999, 99999)
    ops.node(62028, 11.55, 14.225, 5.9)
    ops.element('elasticBeamColumn', 62028, 62028, 2028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302028, 59468.53285)
    ops.uniaxialMaterial('Elastic', 402028, 63500.15155)
    ops.section('Aggregator', 12028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402028, 'My', 302028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12028, 2028, 12028, 12028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 2)
    # Central joint node
    ops.node(2029, 14.6, 14.4, 5.9, '-mass', 12.13085117227319, 12.13085117227319, 12.13085117227319, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52029, 14.425, 14.4, 5.9)
    ops.element('elasticBeamColumn', 52029, 52029, 2029, 99999, 88888)
    ops.node(32029, 14.775, 14.4, 5.9)
    ops.element('elasticBeamColumn', 32029, 2029, 32029, 99999, 88888)
    ops.node(22029, 14.6, 14.4, 5.65)
    ops.element('elasticBeamColumn', 22029, 22029, 2029, 99999, 99999)
    ops.node(72029, 14.6, 14.4, 6.15)
    ops.element('elasticBeamColumn', 72029, 2029, 72029, 99999, 99999)
    ops.node(62029, 14.6, 14.225, 5.9)
    ops.element('elasticBeamColumn', 62029, 62029, 2029, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302029, 59468.53285)
    ops.uniaxialMaterial('Elastic', 402029, 63500.15155)
    ops.section('Aggregator', 12029, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402029, 'My', 302029, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12029, 2029, 12029, 12029, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 2)
    # Central joint node
    ops.node(2030, 18.45, 14.4, 5.9, '-mass', 14.015486748216105, 14.015486748216105, 14.015486748216105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52030, 18.25, 14.4, 5.9)
    ops.element('elasticBeamColumn', 52030, 52030, 2030, 99999, 88888)
    ops.node(32030, 18.65, 14.4, 5.9)
    ops.element('elasticBeamColumn', 32030, 2030, 32030, 99999, 88888)
    ops.node(22030, 18.45, 14.4, 5.65)
    ops.element('elasticBeamColumn', 22030, 22030, 2030, 99999, 99999)
    ops.node(72030, 18.45, 14.4, 6.15)
    ops.element('elasticBeamColumn', 72030, 2030, 72030, 99999, 99999)
    ops.node(62030, 18.45, 14.2, 5.9)
    ops.element('elasticBeamColumn', 62030, 62030, 2030, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302030, 72101.0554)
    ops.uniaxialMaterial('Elastic', 402030, 77465.1345)
    ops.section('Aggregator', 12030, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402030, 'My', 302030, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12030, 2030, 12030, 12030, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 3, 2)
    # Central joint node
    ops.node(2031, 22.3, 14.4, 5.9, '-mass', 14.015486748216105, 14.015486748216105, 14.015486748216105, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52031, 22.1, 14.4, 5.9)
    ops.element('elasticBeamColumn', 52031, 52031, 2031, 99999, 88888)
    ops.node(32031, 22.5, 14.4, 5.9)
    ops.element('elasticBeamColumn', 32031, 2031, 32031, 99999, 88888)
    ops.node(22031, 22.3, 14.4, 5.65)
    ops.element('elasticBeamColumn', 22031, 22031, 2031, 99999, 99999)
    ops.node(72031, 22.3, 14.4, 6.15)
    ops.element('elasticBeamColumn', 72031, 2031, 72031, 99999, 99999)
    ops.node(62031, 22.3, 14.2, 5.9)
    ops.element('elasticBeamColumn', 62031, 62031, 2031, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302031, 72101.0554)
    ops.uniaxialMaterial('Elastic', 402031, 77465.1345)
    ops.section('Aggregator', 12031, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402031, 'My', 302031, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12031, 2031, 12031, 12031, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 3, 2)
    # Central joint node
    ops.node(2032, 26.15, 14.4, 5.9, '-mass', 9.054455912334353, 9.054455912334353, 9.054455912334353, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52032, 26.0, 14.4, 5.9)
    ops.element('elasticBeamColumn', 52032, 52032, 2032, 99999, 88888)
    ops.node(22032, 26.15, 14.4, 5.65)
    ops.element('elasticBeamColumn', 22032, 22032, 2032, 99999, 99999)
    ops.node(72032, 26.15, 14.4, 6.15)
    ops.element('elasticBeamColumn', 72032, 2032, 72032, 99999, 99999)
    ops.node(62032, 26.15, 14.25, 5.9)
    ops.element('elasticBeamColumn', 62032, 62032, 2032, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302032, 42025.68045)
    ops.uniaxialMaterial('Elastic', 402032, 31938.11015)
    ops.section('Aggregator', 12032, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402032, 'My', 302032, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12032, 2032, 12032, 12032, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 8.85, '-mass', 8.908125637104995, 8.908125637104995, 8.908125637104995, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 8.85)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 8.6)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 9.1)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 8.85)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 28111.24135)
    ops.uniaxialMaterial('Elastic', 403001, 18074.1374)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 3.85, 0.0, 8.85, '-mass', 13.785976044852191, 13.785976044852191, 13.785976044852191, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 3.675, 0.0, 8.85)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 4.025, 0.0, 8.85)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 3.85, 0.0, 8.6)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 3.85, 0.0, 9.1)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 3.85, 0.175, 8.85)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 50678.7256)
    ops.uniaxialMaterial('Elastic', 403002, 46059.7432)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 7.7, 0.0, 8.85, '-mass', 13.785976044852191, 13.785976044852191, 13.785976044852191, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 7.525, 0.0, 8.85)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 7.875, 0.0, 8.85)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 7.7, 0.0, 8.6)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 7.7, 0.0, 9.1)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 7.7, 0.175, 8.85)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 50678.7256)
    ops.uniaxialMaterial('Elastic', 403003, 46059.7432)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 11.55, 0.0, 8.85, '-mass', 9.090541539245667, 9.090541539245667, 9.090541539245667, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 11.425, 0.0, 8.85)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(33004, 11.675, 0.0, 8.85)
    ops.element('elasticBeamColumn', 33004, 3004, 33004, 99999, 88888)
    ops.node(23004, 11.55, 0.0, 8.6)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 11.55, 0.0, 9.1)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 11.55, 0.125, 8.85)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 38727.00925)
    ops.uniaxialMaterial('Elastic', 403004, 35798.38105)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    # Central joint node
    ops.node(3005, 14.6, 0.0, 8.85, '-mass', 9.090541539245667, 9.090541539245667, 9.090541539245667, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53005, 14.475, 0.0, 8.85)
    ops.element('elasticBeamColumn', 53005, 53005, 3005, 99999, 88888)
    ops.node(33005, 14.725, 0.0, 8.85)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 14.6, 0.0, 8.6)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 14.6, 0.0, 9.1)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(43005, 14.6, 0.125, 8.85)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 38727.00925)
    ops.uniaxialMaterial('Elastic', 403005, 35798.38105)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    # Central joint node
    ops.node(3006, 18.45, 0.0, 8.85, '-mass', 13.785976044852191, 13.785976044852191, 13.785976044852191, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 18.275, 0.0, 8.85)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 18.625, 0.0, 8.85)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 18.45, 0.0, 8.6)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 18.45, 0.0, 9.1)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(43006, 18.45, 0.175, 8.85)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 50678.7256)
    ops.uniaxialMaterial('Elastic', 403006, 46059.7432)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 0, 3)
    # Central joint node
    ops.node(3007, 22.3, 0.0, 8.85, '-mass', 13.785976044852188, 13.785976044852188, 13.785976044852188, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 22.125, 0.0, 8.85)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 22.475, 0.0, 8.85)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 22.3, 0.0, 8.6)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 22.3, 0.0, 9.1)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(43007, 22.3, 0.175, 8.85)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 50678.7256)
    ops.uniaxialMaterial('Elastic', 403007, 46059.7432)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 0, 3)
    # Central joint node
    ops.node(3008, 26.15, 0.0, 8.85, '-mass', 8.908125637104993, 8.908125637104993, 8.908125637104993, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 26.025, 0.0, 8.85)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 26.15, 0.0, 8.6)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 26.15, 0.0, 9.1)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(43008, 26.15, 0.125, 8.85)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 28111.24135)
    ops.uniaxialMaterial('Elastic', 403008, 18074.1374)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3009, 0.0, 4.8, 8.85, '-mass', 14.768442915392452, 14.768442915392452, 14.768442915392452, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.175, 4.8, 8.85)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 4.8, 8.6)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 4.8, 9.1)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 4.625, 8.85)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 4.975, 8.85)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 70037.08695)
    ops.uniaxialMaterial('Elastic', 403009, 39119.5154)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3010, 3.85, 4.8, 8.85, '-mass', 20.628323139653418, 20.628323139653418, 20.628323139653418, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 3.675, 4.8, 8.85)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 4.025, 4.8, 8.85)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 3.85, 4.8, 8.6)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 3.85, 4.8, 9.1)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 3.85, 4.625, 8.85)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 3.85, 4.975, 8.85)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 84769.77815)
    ops.uniaxialMaterial('Elastic', 403010, 65724.01685)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3011, 7.7, 4.8, 8.85, '-mass', 20.628323139653418, 20.628323139653418, 20.628323139653418, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 7.525, 4.8, 8.85)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 7.875, 4.8, 8.85)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 7.7, 4.8, 8.6)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 7.7, 4.8, 9.1)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 7.7, 4.625, 8.85)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 7.7, 4.975, 8.85)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 84769.77815)
    ops.uniaxialMaterial('Elastic', 403011, 65724.01685)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3012, 11.55, 4.8, 8.85, '-mass', 19.21125, 19.21125, 19.21125, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 11.375, 4.8, 8.85)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(33012, 11.725, 4.8, 8.85)
    ops.element('elasticBeamColumn', 33012, 3012, 33012, 99999, 88888)
    ops.node(23012, 11.55, 4.8, 8.6)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 11.55, 4.8, 9.1)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 11.55, 4.625, 8.85)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 11.55, 4.975, 8.85)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 82892.15535)
    ops.uniaxialMaterial('Elastic', 403012, 64268.25145)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    # Central joint node
    ops.node(3013, 14.6, 4.8, 8.85, '-mass', 19.211249999999996, 19.211249999999996, 19.211249999999996, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53013, 14.425, 4.8, 8.85)
    ops.element('elasticBeamColumn', 53013, 53013, 3013, 99999, 88888)
    ops.node(33013, 14.775, 4.8, 8.85)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 14.6, 4.8, 8.6)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 14.6, 4.8, 9.1)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 14.6, 4.625, 8.85)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 14.6, 4.975, 8.85)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303013, 82892.15535)
    ops.uniaxialMaterial('Elastic', 403013, 64268.25145)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    # Central joint node
    ops.node(3014, 18.45, 4.8, 8.85, '-mass', 20.628323139653418, 20.628323139653418, 20.628323139653418, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 18.275, 4.8, 8.85)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 18.625, 4.8, 8.85)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 18.45, 4.8, 8.6)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 18.45, 4.8, 9.1)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 18.45, 4.625, 8.85)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 18.45, 4.975, 8.85)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303014, 84769.77815)
    ops.uniaxialMaterial('Elastic', 403014, 65724.01685)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 1, 3)
    # Central joint node
    ops.node(3015, 22.3, 4.8, 8.85, '-mass', 20.628323139653418, 20.628323139653418, 20.628323139653418, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 22.125, 4.8, 8.85)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 22.475, 4.8, 8.85)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 22.3, 4.8, 8.6)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 22.3, 4.8, 9.1)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 22.3, 4.625, 8.85)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 22.3, 4.975, 8.85)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303015, 84769.77815)
    ops.uniaxialMaterial('Elastic', 403015, 65724.01685)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 1, 3)
    # Central joint node
    ops.node(3016, 26.15, 4.8, 8.85, '-mass', 14.768442915392452, 14.768442915392452, 14.768442915392452, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 25.975, 4.8, 8.85)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 26.15, 4.8, 8.6)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 26.15, 4.8, 9.1)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 26.15, 4.625, 8.85)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 26.15, 4.975, 8.85)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303016, 70037.08695)
    ops.uniaxialMaterial('Elastic', 403016, 39119.5154)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3017, 0.0, 9.6, 8.85, '-mass', 14.674253312945972, 14.674253312945972, 14.674253312945972, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33017, 0.175, 9.6, 8.85)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 0.0, 9.6, 8.6)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 0.0, 9.6, 9.1)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 0.0, 9.425, 8.85)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 0.0, 9.775, 8.85)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303017, 69845.8886)
    ops.uniaxialMaterial('Elastic', 403017, 27852.28455)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3018, 3.85, 9.6, 8.85, '-mass', 20.43994393476045, 20.43994393476045, 20.43994393476045, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 3.675, 9.6, 8.85)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(33018, 4.025, 9.6, 8.85)
    ops.element('elasticBeamColumn', 33018, 3018, 33018, 99999, 88888)
    ops.node(23018, 3.85, 9.6, 8.6)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 3.85, 9.6, 9.1)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 3.85, 9.425, 8.85)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 3.85, 9.775, 8.85)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303018, 84495.897)
    ops.uniaxialMaterial('Elastic', 403018, 47663.5518)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3019, 7.7, 9.6, 8.85, '-mass', 20.439943934760453, 20.439943934760453, 20.439943934760453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53019, 7.525, 9.6, 8.85)
    ops.element('elasticBeamColumn', 53019, 53019, 3019, 99999, 88888)
    ops.node(33019, 7.875, 9.6, 8.85)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 7.7, 9.6, 8.6)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 7.7, 9.6, 9.1)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 7.7, 9.425, 8.85)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    ops.node(43019, 7.7, 9.775, 8.85)
    ops.element('elasticBeamColumn', 43019, 3019, 43019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303019, 84495.897)
    ops.uniaxialMaterial('Elastic', 403019, 47663.5518)
    ops.section('Aggregator', 13019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403019, 'My', 303019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13019, 3019, 13019, 13019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3020, 11.55, 9.6, 8.85, '-mass', 18.043047910295613, 18.043047910295613, 18.043047910295613, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 11.375, 9.6, 8.85)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(33020, 11.725, 9.6, 8.85)
    ops.element('elasticBeamColumn', 33020, 3020, 33020, 99999, 88888)
    ops.node(23020, 11.55, 9.6, 8.6)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 11.55, 9.6, 9.1)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 11.55, 9.425, 8.85)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    ops.node(43020, 11.55, 9.775, 8.85)
    ops.element('elasticBeamColumn', 43020, 3020, 43020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303020, 79881.2963)
    ops.uniaxialMaterial('Elastic', 403020, 45060.48745)
    ops.section('Aggregator', 13020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403020, 'My', 303020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13020, 3020, 13020, 13020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    # Central joint node
    ops.node(3021, 14.6, 9.6, 8.85, '-mass', 18.043047910295613, 18.043047910295613, 18.043047910295613, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53021, 14.425, 9.6, 8.85)
    ops.element('elasticBeamColumn', 53021, 53021, 3021, 99999, 88888)
    ops.node(33021, 14.775, 9.6, 8.85)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 14.6, 9.6, 8.6)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 14.6, 9.6, 9.1)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 14.6, 9.425, 8.85)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    ops.node(43021, 14.6, 9.775, 8.85)
    ops.element('elasticBeamColumn', 43021, 3021, 43021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303021, 79881.2963)
    ops.uniaxialMaterial('Elastic', 403021, 45060.48745)
    ops.section('Aggregator', 13021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403021, 'My', 303021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13021, 3021, 13021, 13021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    # Central joint node
    ops.node(3022, 18.45, 9.6, 8.85, '-mass', 20.439943934760453, 20.439943934760453, 20.439943934760453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 18.275, 9.6, 8.85)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 18.625, 9.6, 8.85)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 18.45, 9.6, 8.6)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 18.45, 9.6, 9.1)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 18.45, 9.425, 8.85)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    ops.node(43022, 18.45, 9.775, 8.85)
    ops.element('elasticBeamColumn', 43022, 3022, 43022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303022, 84495.897)
    ops.uniaxialMaterial('Elastic', 403022, 47663.5518)
    ops.section('Aggregator', 13022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403022, 'My', 303022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13022, 3022, 13022, 13022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 2, 3)
    # Central joint node
    ops.node(3023, 22.3, 9.6, 8.85, '-mass', 20.43994393476045, 20.43994393476045, 20.43994393476045, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 22.125, 9.6, 8.85)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 22.475, 9.6, 8.85)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 22.3, 9.6, 8.6)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 22.3, 9.6, 9.1)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 22.3, 9.425, 8.85)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    ops.node(43023, 22.3, 9.775, 8.85)
    ops.element('elasticBeamColumn', 43023, 3023, 43023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303023, 84495.897)
    ops.uniaxialMaterial('Elastic', 403023, 47663.5518)
    ops.section('Aggregator', 13023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403023, 'My', 303023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13023, 3023, 13023, 13023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 2, 3)
    # Central joint node
    ops.node(3024, 26.15, 9.6, 8.85, '-mass', 14.674253312945972, 14.674253312945972, 14.674253312945972, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 25.975, 9.6, 8.85)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 26.15, 9.6, 8.6)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 26.15, 9.6, 9.1)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 26.15, 9.425, 8.85)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    ops.node(43024, 26.15, 9.775, 8.85)
    ops.element('elasticBeamColumn', 43024, 3024, 43024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303024, 69845.8886)
    ops.uniaxialMaterial('Elastic', 403024, 27852.28455)
    ops.section('Aggregator', 13024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403024, 'My', 303024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13024, 3024, 13024, 13024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3025, 0.0, 14.4, 8.85, '-mass', 8.908125637104996, 8.908125637104996, 8.908125637104996, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33025, 0.125, 14.4, 8.85)
    ops.element('elasticBeamColumn', 33025, 3025, 33025, 99999, 88888)
    ops.node(23025, 0.0, 14.4, 8.6)
    ops.element('elasticBeamColumn', 23025, 23025, 3025, 99999, 99999)
    ops.node(73025, 0.0, 14.4, 9.1)
    ops.element('elasticBeamColumn', 73025, 3025, 73025, 99999, 99999)
    ops.node(63025, 0.0, 14.275, 8.85)
    ops.element('elasticBeamColumn', 63025, 63025, 3025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303025, 28111.24135)
    ops.uniaxialMaterial('Elastic', 403025, 18074.1374)
    ops.section('Aggregator', 13025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403025, 'My', 303025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13025, 3025, 13025, 13025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3026, 3.85, 14.4, 8.85, '-mass', 13.785976044852191, 13.785976044852191, 13.785976044852191, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53026, 3.675, 14.4, 8.85)
    ops.element('elasticBeamColumn', 53026, 53026, 3026, 99999, 88888)
    ops.node(33026, 4.025, 14.4, 8.85)
    ops.element('elasticBeamColumn', 33026, 3026, 33026, 99999, 88888)
    ops.node(23026, 3.85, 14.4, 8.6)
    ops.element('elasticBeamColumn', 23026, 23026, 3026, 99999, 99999)
    ops.node(73026, 3.85, 14.4, 9.1)
    ops.element('elasticBeamColumn', 73026, 3026, 73026, 99999, 99999)
    ops.node(63026, 3.85, 14.225, 8.85)
    ops.element('elasticBeamColumn', 63026, 63026, 3026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303026, 50678.7256)
    ops.uniaxialMaterial('Elastic', 403026, 46059.7432)
    ops.section('Aggregator', 13026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403026, 'My', 303026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13026, 3026, 13026, 13026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3027, 7.7, 14.4, 8.85, '-mass', 13.785976044852191, 13.785976044852191, 13.785976044852191, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53027, 7.525, 14.4, 8.85)
    ops.element('elasticBeamColumn', 53027, 53027, 3027, 99999, 88888)
    ops.node(33027, 7.875, 14.4, 8.85)
    ops.element('elasticBeamColumn', 33027, 3027, 33027, 99999, 88888)
    ops.node(23027, 7.7, 14.4, 8.6)
    ops.element('elasticBeamColumn', 23027, 23027, 3027, 99999, 99999)
    ops.node(73027, 7.7, 14.4, 9.1)
    ops.element('elasticBeamColumn', 73027, 3027, 73027, 99999, 99999)
    ops.node(63027, 7.7, 14.225, 8.85)
    ops.element('elasticBeamColumn', 63027, 63027, 3027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303027, 50678.7256)
    ops.uniaxialMaterial('Elastic', 403027, 46059.7432)
    ops.section('Aggregator', 13027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403027, 'My', 303027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13027, 3027, 13027, 13027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3028, 11.55, 14.4, 8.85, '-mass', 11.82993374108053, 11.82993374108053, 11.82993374108053, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53028, 11.425, 14.4, 8.85)
    ops.element('elasticBeamColumn', 53028, 53028, 3028, 99999, 88888)
    ops.node(33028, 11.675, 14.4, 8.85)
    ops.element('elasticBeamColumn', 33028, 3028, 33028, 99999, 88888)
    ops.node(23028, 11.55, 14.4, 8.6)
    ops.element('elasticBeamColumn', 23028, 23028, 3028, 99999, 99999)
    ops.node(73028, 11.55, 14.4, 9.1)
    ops.element('elasticBeamColumn', 73028, 3028, 73028, 99999, 99999)
    ops.node(63028, 11.55, 14.275, 8.85)
    ops.element('elasticBeamColumn', 63028, 63028, 3028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303028, 33972.81825)
    ops.uniaxialMaterial('Elastic', 403028, 33515.01265)
    ops.section('Aggregator', 13028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403028, 'My', 303028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13028, 3028, 13028, 13028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 3)
    # Central joint node
    ops.node(3029, 14.6, 14.4, 8.85, '-mass', 11.82993374108053, 11.82993374108053, 11.82993374108053, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53029, 14.475, 14.4, 8.85)
    ops.element('elasticBeamColumn', 53029, 53029, 3029, 99999, 88888)
    ops.node(33029, 14.725, 14.4, 8.85)
    ops.element('elasticBeamColumn', 33029, 3029, 33029, 99999, 88888)
    ops.node(23029, 14.6, 14.4, 8.6)
    ops.element('elasticBeamColumn', 23029, 23029, 3029, 99999, 99999)
    ops.node(73029, 14.6, 14.4, 9.1)
    ops.element('elasticBeamColumn', 73029, 3029, 73029, 99999, 99999)
    ops.node(63029, 14.6, 14.275, 8.85)
    ops.element('elasticBeamColumn', 63029, 63029, 3029, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303029, 33972.81825)
    ops.uniaxialMaterial('Elastic', 403029, 33515.01265)
    ops.section('Aggregator', 13029, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403029, 'My', 303029, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13029, 3029, 13029, 13029, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 3)
    # Central joint node
    ops.node(3030, 18.45, 14.4, 8.85, '-mass', 13.785976044852193, 13.785976044852193, 13.785976044852193, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53030, 18.275, 14.4, 8.85)
    ops.element('elasticBeamColumn', 53030, 53030, 3030, 99999, 88888)
    ops.node(33030, 18.625, 14.4, 8.85)
    ops.element('elasticBeamColumn', 33030, 3030, 33030, 99999, 88888)
    ops.node(23030, 18.45, 14.4, 8.6)
    ops.element('elasticBeamColumn', 23030, 23030, 3030, 99999, 99999)
    ops.node(73030, 18.45, 14.4, 9.1)
    ops.element('elasticBeamColumn', 73030, 3030, 73030, 99999, 99999)
    ops.node(63030, 18.45, 14.225, 8.85)
    ops.element('elasticBeamColumn', 63030, 63030, 3030, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303030, 50678.7256)
    ops.uniaxialMaterial('Elastic', 403030, 46059.7432)
    ops.section('Aggregator', 13030, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403030, 'My', 303030, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13030, 3030, 13030, 13030, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 3, 3)
    # Central joint node
    ops.node(3031, 22.3, 14.4, 8.85, '-mass', 13.78597604485219, 13.78597604485219, 13.78597604485219, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53031, 22.125, 14.4, 8.85)
    ops.element('elasticBeamColumn', 53031, 53031, 3031, 99999, 88888)
    ops.node(33031, 22.475, 14.4, 8.85)
    ops.element('elasticBeamColumn', 33031, 3031, 33031, 99999, 88888)
    ops.node(23031, 22.3, 14.4, 8.6)
    ops.element('elasticBeamColumn', 23031, 23031, 3031, 99999, 99999)
    ops.node(73031, 22.3, 14.4, 9.1)
    ops.element('elasticBeamColumn', 73031, 3031, 73031, 99999, 99999)
    ops.node(63031, 22.3, 14.225, 8.85)
    ops.element('elasticBeamColumn', 63031, 63031, 3031, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303031, 50678.7256)
    ops.uniaxialMaterial('Elastic', 403031, 46059.7432)
    ops.section('Aggregator', 13031, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403031, 'My', 303031, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13031, 3031, 13031, 13031, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 3, 3)
    # Central joint node
    ops.node(3032, 26.15, 14.4, 8.85, '-mass', 8.908125637104995, 8.908125637104995, 8.908125637104995, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53032, 26.025, 14.4, 8.85)
    ops.element('elasticBeamColumn', 53032, 53032, 3032, 99999, 88888)
    ops.node(23032, 26.15, 14.4, 8.6)
    ops.element('elasticBeamColumn', 23032, 23032, 3032, 99999, 99999)
    ops.node(73032, 26.15, 14.4, 9.1)
    ops.element('elasticBeamColumn', 73032, 3032, 73032, 99999, 99999)
    ops.node(63032, 26.15, 14.275, 8.85)
    ops.element('elasticBeamColumn', 63032, 63032, 3032, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303032, 28111.24135)
    ops.uniaxialMaterial('Elastic', 403032, 18074.1374)
    ops.section('Aggregator', 13032, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403032, 'My', 303032, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13032, 3032, 13032, 13032, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 11.8, '-mass', 4.833323139653414, 4.833323139653414, 4.833323139653414, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 11.8)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 11.6)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 11.8)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 21952.74415)
    ops.uniaxialMaterial('Elastic', 404001, 15695.43675)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 3.85, 0.0, 11.8, '-mass', 9.378725790010192, 9.378725790010192, 9.378725790010192, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 3.675, 0.0, 11.8)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 4.025, 0.0, 11.8)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 3.85, 0.0, 11.575)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 3.85, 0.175, 11.8)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 46438.6701)
    ops.uniaxialMaterial('Elastic', 404002, 29396.47115)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 7.7, 0.0, 11.8, '-mass', 9.378725790010192, 9.378725790010192, 9.378725790010192, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 7.525, 0.0, 11.8)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 7.875, 0.0, 11.8)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 7.7, 0.0, 11.575)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 7.7, 0.175, 11.8)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 46438.6701)
    ops.uniaxialMaterial('Elastic', 404003, 29396.47115)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 11.55, 0.0, 11.8, '-mass', 5.135234454638125, 5.135234454638125, 5.135234454638125, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 11.425, 0.0, 11.8)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(34004, 11.675, 0.0, 11.8)
    ops.element('elasticBeamColumn', 34004, 4004, 34004, 99999, 88888)
    ops.node(24004, 11.55, 0.0, 11.575)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 11.55, 0.125, 11.8)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 25788.9389)
    ops.uniaxialMaterial('Elastic', 404004, 16031.73285)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    # Central joint node
    ops.node(4005, 14.6, 0.0, 11.8, '-mass', 5.135234454638125, 5.135234454638125, 5.135234454638125, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54005, 14.475, 0.0, 11.8)
    ops.element('elasticBeamColumn', 54005, 54005, 4005, 99999, 88888)
    ops.node(34005, 14.725, 0.0, 11.8)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 14.6, 0.0, 11.575)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(44005, 14.6, 0.125, 11.8)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 25788.9389)
    ops.uniaxialMaterial('Elastic', 404005, 16031.73285)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    # Central joint node
    ops.node(4006, 18.45, 0.0, 11.8, '-mass', 9.378725790010192, 9.378725790010192, 9.378725790010192, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 18.275, 0.0, 11.8)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 18.625, 0.0, 11.8)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 18.45, 0.0, 11.575)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(44006, 18.45, 0.175, 11.8)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 46438.6701)
    ops.uniaxialMaterial('Elastic', 404006, 29396.47115)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 0, 4)
    # Central joint node
    ops.node(4007, 22.3, 0.0, 11.8, '-mass', 9.378725790010192, 9.378725790010192, 9.378725790010192, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 22.125, 0.0, 11.8)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 22.475, 0.0, 11.8)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 22.3, 0.0, 11.575)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(44007, 22.3, 0.175, 11.8)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 46438.6701)
    ops.uniaxialMaterial('Elastic', 404007, 29396.47115)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 0, 4)
    # Central joint node
    ops.node(4008, 26.15, 0.0, 11.8, '-mass', 4.833323139653413, 4.833323139653413, 4.833323139653413, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 26.025, 0.0, 11.8)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 26.15, 0.0, 11.6)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(44008, 26.15, 0.125, 11.8)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 21952.74415)
    ops.uniaxialMaterial('Elastic', 404008, 15695.43675)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4009, 0.0, 4.8, 11.8, '-mass', 9.469245667686033, 9.469245667686033, 9.469245667686033, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.175, 4.8, 11.8)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 4.8, 11.6)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 4.625, 11.8)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 4.975, 11.8)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 40729.84445)
    ops.uniaxialMaterial('Elastic', 404009, 40729.84445)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4010, 3.85, 4.8, 11.8, '-mass', 17.938644240570845, 17.938644240570845, 17.938644240570845, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 3.675, 4.8, 11.8)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 4.025, 4.8, 11.8)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 3.85, 4.8, 11.575)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 3.85, 4.625, 11.8)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 3.85, 4.975, 11.8)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 57093.03905)
    ops.uniaxialMaterial('Elastic', 404010, 50063.3251)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4011, 7.7, 4.8, 11.8, '-mass', 17.938644240570845, 17.938644240570845, 17.938644240570845, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 7.525, 4.8, 11.8)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 7.875, 4.8, 11.8)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 7.7, 4.8, 11.575)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 7.7, 4.625, 11.8)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 7.7, 4.975, 11.8)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 57093.03905)
    ops.uniaxialMaterial('Elastic', 404011, 50063.3251)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4012, 11.55, 4.8, 11.8, '-mass', 15.336077981651375, 15.336077981651375, 15.336077981651375, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 11.375, 4.8, 11.8)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(34012, 11.725, 4.8, 11.8)
    ops.element('elasticBeamColumn', 34012, 4012, 34012, 99999, 88888)
    ops.node(24012, 11.55, 4.8, 11.575)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 11.55, 4.625, 11.8)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 11.55, 4.975, 11.8)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 58134.52095)
    ops.uniaxialMaterial('Elastic', 404012, 50990.51625)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    # Central joint node
    ops.node(4013, 14.6, 4.8, 11.8, '-mass', 15.336077981651373, 15.336077981651373, 15.336077981651373, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54013, 14.425, 4.8, 11.8)
    ops.element('elasticBeamColumn', 54013, 54013, 4013, 99999, 88888)
    ops.node(34013, 14.775, 4.8, 11.8)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 14.6, 4.8, 11.575)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 14.6, 4.625, 11.8)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 14.6, 4.975, 11.8)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304013, 58134.52095)
    ops.uniaxialMaterial('Elastic', 404013, 50990.51625)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    # Central joint node
    ops.node(4014, 18.45, 4.8, 11.8, '-mass', 17.938644240570845, 17.938644240570845, 17.938644240570845, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 18.275, 4.8, 11.8)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 18.625, 4.8, 11.8)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 18.45, 4.8, 11.575)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 18.45, 4.625, 11.8)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 18.45, 4.975, 11.8)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304014, 57093.03905)
    ops.uniaxialMaterial('Elastic', 404014, 50063.3251)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 1, 4)
    # Central joint node
    ops.node(4015, 22.3, 4.8, 11.8, '-mass', 17.938644240570845, 17.938644240570845, 17.938644240570845, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 22.125, 4.8, 11.8)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 22.475, 4.8, 11.8)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 22.3, 4.8, 11.575)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 22.3, 4.625, 11.8)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 22.3, 4.975, 11.8)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304015, 57093.03905)
    ops.uniaxialMaterial('Elastic', 404015, 50063.3251)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 1, 4)
    # Central joint node
    ops.node(4016, 26.15, 4.8, 11.8, '-mass', 9.469245667686032, 9.469245667686032, 9.469245667686032, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 25.975, 4.8, 11.8)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 26.15, 4.8, 11.6)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 26.15, 4.625, 11.8)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 26.15, 4.975, 11.8)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304016, 40729.84445)
    ops.uniaxialMaterial('Elastic', 404016, 40729.84445)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4017, 0.0, 9.6, 11.8, '-mass', 9.37505606523955, 9.37505606523955, 9.37505606523955, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 0.175, 9.6, 11.8)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 0.0, 9.6, 11.6)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 0.0, 9.425, 11.8)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 0.0, 9.775, 11.8)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304017, 40567.5476)
    ops.uniaxialMaterial('Elastic', 404017, 29391.69845)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4018, 3.85, 9.6, 11.8, '-mass', 17.75026503567788, 17.75026503567788, 17.75026503567788, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 3.675, 9.6, 11.8)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(34018, 4.025, 9.6, 11.8)
    ops.element('elasticBeamColumn', 34018, 4018, 34018, 99999, 88888)
    ops.node(24018, 3.85, 9.6, 11.575)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 3.85, 9.425, 11.8)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 3.85, 9.775, 11.8)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304018, 56842.33695)
    ops.uniaxialMaterial('Elastic', 404018, 36369.2379)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4019, 7.7, 9.6, 11.8, '-mass', 17.75026503567788, 17.75026503567788, 17.75026503567788, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54019, 7.525, 9.6, 11.8)
    ops.element('elasticBeamColumn', 54019, 54019, 4019, 99999, 88888)
    ops.node(34019, 7.875, 9.6, 11.8)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 7.7, 9.6, 11.575)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 7.7, 9.425, 11.8)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    ops.node(44019, 7.7, 9.775, 11.8)
    ops.element('elasticBeamColumn', 44019, 4019, 44019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304019, 56842.33695)
    ops.uniaxialMaterial('Elastic', 404019, 36369.2379)
    ops.section('Aggregator', 14019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404019, 'My', 304019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14019, 4019, 14019, 14019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4020, 11.55, 9.6, 11.8, '-mass', 15.503827726809375, 15.503827726809375, 15.503827726809375, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 11.375, 9.6, 11.8)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(34020, 11.725, 9.6, 11.8)
    ops.element('elasticBeamColumn', 34020, 4020, 34020, 99999, 88888)
    ops.node(24020, 11.55, 9.6, 11.575)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 11.55, 9.425, 11.8)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    ops.node(44020, 11.55, 9.775, 11.8)
    ops.element('elasticBeamColumn', 44020, 4020, 44020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304020, 53750.88305)
    ops.uniaxialMaterial('Elastic', 404020, 34298.9812)
    ops.section('Aggregator', 14020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404020, 'My', 304020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14020, 4020, 14020, 14020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    # Central joint node
    ops.node(4021, 14.6, 9.6, 11.8, '-mass', 15.503827726809375, 15.503827726809375, 15.503827726809375, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54021, 14.425, 9.6, 11.8)
    ops.element('elasticBeamColumn', 54021, 54021, 4021, 99999, 88888)
    ops.node(34021, 14.775, 9.6, 11.8)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 14.6, 9.6, 11.575)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 14.6, 9.425, 11.8)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    ops.node(44021, 14.6, 9.775, 11.8)
    ops.element('elasticBeamColumn', 44021, 4021, 44021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304021, 53750.88305)
    ops.uniaxialMaterial('Elastic', 404021, 34298.9812)
    ops.section('Aggregator', 14021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404021, 'My', 304021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14021, 4021, 14021, 14021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    # Central joint node
    ops.node(4022, 18.45, 9.6, 11.8, '-mass', 17.75026503567788, 17.75026503567788, 17.75026503567788, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 18.275, 9.6, 11.8)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 18.625, 9.6, 11.8)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 18.45, 9.6, 11.575)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 18.45, 9.425, 11.8)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    ops.node(44022, 18.45, 9.775, 11.8)
    ops.element('elasticBeamColumn', 44022, 4022, 44022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304022, 56842.33695)
    ops.uniaxialMaterial('Elastic', 404022, 36369.2379)
    ops.section('Aggregator', 14022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404022, 'My', 304022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14022, 4022, 14022, 14022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 2, 4)
    # Central joint node
    ops.node(4023, 22.3, 9.6, 11.8, '-mass', 17.75026503567788, 17.75026503567788, 17.75026503567788, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 22.125, 9.6, 11.8)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 22.475, 9.6, 11.8)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 22.3, 9.6, 11.575)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 22.3, 9.425, 11.8)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    ops.node(44023, 22.3, 9.775, 11.8)
    ops.element('elasticBeamColumn', 44023, 4023, 44023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304023, 56842.33695)
    ops.uniaxialMaterial('Elastic', 404023, 36369.2379)
    ops.section('Aggregator', 14023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404023, 'My', 304023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14023, 4023, 14023, 14023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 2, 4)
    # Central joint node
    ops.node(4024, 26.15, 9.6, 11.8, '-mass', 9.37505606523955, 9.37505606523955, 9.37505606523955, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 25.975, 9.6, 11.8)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 26.15, 9.6, 11.6)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 26.15, 9.425, 11.8)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    ops.node(44024, 26.15, 9.775, 11.8)
    ops.element('elasticBeamColumn', 44024, 4024, 44024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304024, 40567.5476)
    ops.uniaxialMaterial('Elastic', 404024, 29391.69845)
    ops.section('Aggregator', 14024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404024, 'My', 304024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14024, 4024, 14024, 14024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4025, 0.0, 14.4, 11.8, '-mass', 4.833323139653415, 4.833323139653415, 4.833323139653415, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 0.125, 14.4, 11.8)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 0.0, 14.4, 11.6)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(64025, 0.0, 14.275, 11.8)
    ops.element('elasticBeamColumn', 64025, 64025, 4025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304025, 21952.74415)
    ops.uniaxialMaterial('Elastic', 404025, 15695.43675)
    ops.section('Aggregator', 14025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404025, 'My', 304025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14025, 4025, 14025, 14025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4026, 3.85, 14.4, 11.8, '-mass', 9.378725790010195, 9.378725790010195, 9.378725790010195, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 3.675, 14.4, 11.8)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(34026, 4.025, 14.4, 11.8)
    ops.element('elasticBeamColumn', 34026, 4026, 34026, 99999, 88888)
    ops.node(24026, 3.85, 14.4, 11.575)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(64026, 3.85, 14.225, 11.8)
    ops.element('elasticBeamColumn', 64026, 64026, 4026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304026, 46438.6701)
    ops.uniaxialMaterial('Elastic', 404026, 29396.47115)
    ops.section('Aggregator', 14026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404026, 'My', 304026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14026, 4026, 14026, 14026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4027, 7.7, 14.4, 11.8, '-mass', 9.378725790010195, 9.378725790010195, 9.378725790010195, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54027, 7.525, 14.4, 11.8)
    ops.element('elasticBeamColumn', 54027, 54027, 4027, 99999, 88888)
    ops.node(34027, 7.875, 14.4, 11.8)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 7.7, 14.4, 11.575)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(64027, 7.7, 14.225, 11.8)
    ops.element('elasticBeamColumn', 64027, 64027, 4027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304027, 46438.6701)
    ops.uniaxialMaterial('Elastic', 404027, 29396.47115)
    ops.section('Aggregator', 14027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404027, 'My', 304027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14027, 4027, 14027, 14027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4028, 11.55, 14.4, 11.8, '-mass', 8.009635575942916, 8.009635575942916, 8.009635575942916, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 11.425, 14.4, 11.8)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(34028, 11.675, 14.4, 11.8)
    ops.element('elasticBeamColumn', 34028, 4028, 34028, 99999, 88888)
    ops.node(24028, 11.55, 14.4, 11.575)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(64028, 11.55, 14.275, 11.8)
    ops.element('elasticBeamColumn', 64028, 64028, 4028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304028, 30657.81075)
    ops.uniaxialMaterial('Elastic', 404028, 19310.00865)
    ops.section('Aggregator', 14028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404028, 'My', 304028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14028, 4028, 14028, 14028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 4)
    # Central joint node
    ops.node(4029, 14.6, 14.4, 11.8, '-mass', 8.009635575942916, 8.009635575942916, 8.009635575942916, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54029, 14.475, 14.4, 11.8)
    ops.element('elasticBeamColumn', 54029, 54029, 4029, 99999, 88888)
    ops.node(34029, 14.725, 14.4, 11.8)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 14.6, 14.4, 11.575)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(64029, 14.6, 14.275, 11.8)
    ops.element('elasticBeamColumn', 64029, 64029, 4029, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304029, 30657.81075)
    ops.uniaxialMaterial('Elastic', 404029, 19310.00865)
    ops.section('Aggregator', 14029, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404029, 'My', 304029, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14029, 4029, 14029, 14029, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 4)
    # Central joint node
    ops.node(4030, 18.45, 14.4, 11.8, '-mass', 9.378725790010195, 9.378725790010195, 9.378725790010195, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 18.275, 14.4, 11.8)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(34030, 18.625, 14.4, 11.8)
    ops.element('elasticBeamColumn', 34030, 4030, 34030, 99999, 88888)
    ops.node(24030, 18.45, 14.4, 11.575)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(64030, 18.45, 14.225, 11.8)
    ops.element('elasticBeamColumn', 64030, 64030, 4030, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304030, 46438.6701)
    ops.uniaxialMaterial('Elastic', 404030, 29396.47115)
    ops.section('Aggregator', 14030, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404030, 'My', 304030, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14030, 4030, 14030, 14030, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (6, 3, 4)
    # Central joint node
    ops.node(4031, 22.3, 14.4, 11.8, '-mass', 9.378725790010193, 9.378725790010193, 9.378725790010193, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54031, 22.125, 14.4, 11.8)
    ops.element('elasticBeamColumn', 54031, 54031, 4031, 99999, 88888)
    ops.node(34031, 22.475, 14.4, 11.8)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 22.3, 14.4, 11.575)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(64031, 22.3, 14.225, 11.8)
    ops.element('elasticBeamColumn', 64031, 64031, 4031, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304031, 46438.6701)
    ops.uniaxialMaterial('Elastic', 404031, 29396.47115)
    ops.section('Aggregator', 14031, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404031, 'My', 304031, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14031, 4031, 14031, 14031, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (7, 3, 4)
    # Central joint node
    ops.node(4032, 26.15, 14.4, 11.8, '-mass', 4.833323139653414, 4.833323139653414, 4.833323139653414, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 26.025, 14.4, 11.8)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 26.15, 14.4, 11.6)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(64032, 26.15, 14.275, 11.8)
    ops.element('elasticBeamColumn', 64032, 64032, 4032, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304032, 21952.74415)
    ops.uniaxialMaterial('Elastic', 404032, 15695.43675)
    ops.section('Aggregator', 14032, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404032, 'My', 304032, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14032, 4032, 14032, 14032, '-orient', 0, 0, 1, 0, 1, 0)
