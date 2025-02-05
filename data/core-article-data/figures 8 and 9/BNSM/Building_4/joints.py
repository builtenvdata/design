import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 0.5)
    # Central joint node
    ops.node(4029, 0.0, 0.0, 1.85, '-mass', 3.923579255861367, 3.923579255861367, 3.923579255861367, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34029, 0.15, 0.0, 1.85)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 0.0, 0.0, 1.6)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(74029, 0.0, 0.0, 2.1)
    ops.element('elasticBeamColumn', 74029, 4029, 74029, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 0.5)
    # Central joint node
    ops.node(4030, 2.95, 0.0, 1.85, '-mass', 4.8061480632008164, 4.8061480632008164, 4.8061480632008164, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 2.725, 0.0, 1.85)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(24030, 2.95, 0.0, 1.6)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(74030, 2.95, 0.0, 2.1)
    ops.element('elasticBeamColumn', 74030, 4030, 74030, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 1.5)
    # Central joint node
    ops.node(4031, 0.0, 0.0, 5.125, '-mass', 3.755383537206932, 3.755383537206932, 3.755383537206932, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34031, 0.15, 0.0, 5.125)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 0.0, 0.0, 4.875)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(74031, 0.0, 0.0, 5.375)
    ops.element('elasticBeamColumn', 74031, 4031, 74031, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    # Central joint node
    ops.node(4032, 2.95, 0.0, 5.125, '-mass', 4.4352000509684, 4.4352000509684, 4.4352000509684, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 2.725, 0.0, 5.125)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 2.95, 0.0, 4.875)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(74032, 2.95, 0.0, 5.375)
    ops.element('elasticBeamColumn', 74032, 4032, 74032, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 2.5)
    # Central joint node
    ops.node(4033, 0.0, 0.0, 7.975, '-mass', 3.621591488277268, 3.621591488277268, 3.621591488277268, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34033, 0.125, 0.0, 7.975)
    ops.element('elasticBeamColumn', 34033, 4033, 34033, 99999, 88888)
    ops.node(24033, 0.0, 0.0, 7.775)
    ops.element('elasticBeamColumn', 24033, 24033, 4033, 99999, 99999)
    ops.node(74033, 0.0, 0.0, 8.175)
    ops.element('elasticBeamColumn', 74033, 4033, 74033, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    # Central joint node
    ops.node(4034, 2.95, 0.0, 7.975, '-mass', 4.013793323139653, 4.013793323139653, 4.013793323139653, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54034, 2.775, 0.0, 7.975)
    ops.element('elasticBeamColumn', 54034, 54034, 4034, 99999, 88888)
    ops.node(24034, 2.95, 0.0, 7.775)
    ops.element('elasticBeamColumn', 24034, 24034, 4034, 99999, 99999)
    ops.node(74034, 2.95, 0.0, 8.175)
    ops.element('elasticBeamColumn', 74034, 4034, 74034, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 3.5)
    # Central joint node
    ops.node(4035, 0.0, 0.0, 10.825, '-mass', 3.549420234454639, 3.549420234454639, 3.549420234454639, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34035, 0.125, 0.0, 10.825)
    ops.element('elasticBeamColumn', 34035, 4035, 34035, 99999, 88888)
    ops.node(24035, 0.0, 0.0, 10.625)
    ops.element('elasticBeamColumn', 24035, 24035, 4035, 99999, 99999)
    ops.node(74035, 0.0, 0.0, 11.025)
    ops.element('elasticBeamColumn', 74035, 4035, 74035, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 3.5)
    # Central joint node
    ops.node(4036, 2.95, 0.0, 10.825, '-mass', 3.941622069317024, 3.941622069317024, 3.941622069317024, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54036, 2.775, 0.0, 10.825)
    ops.element('elasticBeamColumn', 54036, 54036, 4036, 99999, 88888)
    ops.node(24036, 2.95, 0.0, 10.625)
    ops.element('elasticBeamColumn', 24036, 24036, 4036, 99999, 99999)
    ops.node(74036, 2.95, 0.0, 11.025)
    ops.element('elasticBeamColumn', 74036, 4036, 74036, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.7, '-mass', 3.4666156982670744, 3.4666156982670744, 3.4666156982670744, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.15, 0.0, 3.7)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 3.45)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.95)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.125, 3.7)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 46698.7917)
    ops.uniaxialMaterial('Elastic', 401001, 45854.8389)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 2.95, 0.0, 3.7, '-mass', 13.244081294597349, 13.244081294597349, 13.244081294597349, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 2.725, 0.0, 3.7)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 3.175, 0.0, 3.7)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 2.95, 0.0, 3.425)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 2.95, 0.0, 3.975)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 2.95, 0.3, 3.7)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 156528.1621)
    ops.uniaxialMaterial('Elastic', 401002, 179980.0248)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 7.7, 0.0, 3.7, '-mass', 21.332301223241583, 21.332301223241583, 21.332301223241583, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 7.45, 0.0, 3.7)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 7.95, 0.0, 3.7)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 7.7, 0.0, 3.425)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 7.7, 0.0, 3.975)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 7.7, 0.35, 3.7)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 162464.6136)
    ops.uniaxialMaterial('Elastic', 401003, 182455.95955)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 12.45, 0.0, 3.7, '-mass', 12.788576707441385, 12.788576707441385, 12.788576707441385, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 12.275, 0.0, 3.7)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 12.45, 0.0, 3.45)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 12.45, 0.0, 3.95)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 12.45, 0.225, 3.7)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 73699.4572)
    ops.uniaxialMaterial('Elastic', 401004, 75073.99255)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 5.15, 3.7, '-mass', 12.436034658511723, 12.436034658511723, 12.436034658511723, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.225, 5.15, 3.7)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 5.15, 3.45)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 5.15, 3.95)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 5.025, 3.7)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 5.275, 3.7)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 84689.23255)
    ops.uniaxialMaterial('Elastic', 401005, 65651.5617)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 2.95, 5.15, 3.7, '-mass', 25.667214576962284, 25.667214576962284, 25.667214576962284, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 2.525, 5.15, 3.7)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 3.375, 5.15, 3.7)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 2.95, 5.15, 3.425)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 2.95, 5.15, 3.975)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 2.95, 4.975, 3.7)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 2.95, 5.325, 3.7)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 164951.51505)
    ops.uniaxialMaterial('Elastic', 401006, 209894.84035)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 7.7, 5.15, 3.7, '-mass', 31.84910805300713, 31.84910805300713, 31.84910805300713, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 7.2, 5.15, 3.7)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 8.2, 5.15, 3.7)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 7.7, 5.15, 3.425)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 7.7, 5.15, 3.975)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 7.7, 4.925, 3.7)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 7.7, 5.375, 3.7)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 218028.46225)
    ops.uniaxialMaterial('Elastic', 401007, 285194.08205)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 12.45, 5.15, 3.7, '-mass', 20.449834352701323, 20.449834352701323, 20.449834352701323, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 12.075, 5.15, 3.7)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 12.45, 5.15, 3.45)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 12.45, 5.15, 3.95)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 12.45, 5.0, 3.7)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 12.45, 5.3, 3.7)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 118980.0175)
    ops.uniaxialMaterial('Elastic', 401008, 113719.64045)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 10.3, 3.7, '-mass', 13.3368374108053, 13.3368374108053, 13.3368374108053, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.25, 10.3, 3.7)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 10.3, 3.45)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 10.3, 3.95)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 10.175, 3.7)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 10.425, 3.7)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 85134.91065)
    ops.uniaxialMaterial('Elastic', 401009, 69400.045)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 2.95, 10.3, 3.7, '-mass', 24.49023955147808, 24.49023955147808, 24.49023955147808, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 2.55, 10.3, 3.7)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 3.35, 10.3, 3.7)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 2.95, 10.3, 3.425)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 2.95, 10.3, 3.975)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 2.95, 10.125, 3.7)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 2.95, 10.475, 3.7)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 162191.1985)
    ops.uniaxialMaterial('Elastic', 401010, 200109.20455)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 7.7, 10.3, 3.7, '-mass', 31.84910805300713, 31.84910805300713, 31.84910805300713, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 7.2, 10.3, 3.7)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 8.2, 10.3, 3.7)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 7.7, 10.3, 3.425)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 7.7, 10.3, 3.975)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 7.7, 10.075, 3.7)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 7.7, 10.525, 3.7)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 218028.46225)
    ops.uniaxialMaterial('Elastic', 401011, 285194.08205)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 12.45, 10.3, 3.7, '-mass', 20.44983435270132, 20.44983435270132, 20.44983435270132, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 12.075, 10.3, 3.7)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 12.45, 10.3, 3.45)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 12.45, 10.3, 3.95)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 12.45, 10.15, 3.7)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 12.45, 10.45, 3.7)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 118980.0175)
    ops.uniaxialMaterial('Elastic', 401012, 113719.64045)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1013, 0.0, 15.45, 3.7, '-mass', 13.336837410805302, 13.336837410805302, 13.336837410805302, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.25, 15.45, 3.7)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 15.45, 3.45)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 15.45, 3.95)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 15.325, 3.7)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 15.575, 3.7)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301013, 85134.91065)
    ops.uniaxialMaterial('Elastic', 401013, 69400.045)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1014, 2.95, 15.45, 3.7, '-mass', 24.49023955147808, 24.49023955147808, 24.49023955147808, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 2.55, 15.45, 3.7)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 3.35, 15.45, 3.7)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 2.95, 15.45, 3.425)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 2.95, 15.45, 3.975)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 2.95, 15.275, 3.7)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 2.95, 15.625, 3.7)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301014, 162191.1985)
    ops.uniaxialMaterial('Elastic', 401014, 200109.20455)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1015, 7.7, 15.45, 3.7, '-mass', 31.84910805300713, 31.84910805300713, 31.84910805300713, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 7.2, 15.45, 3.7)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 8.2, 15.45, 3.7)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 7.7, 15.45, 3.425)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 7.7, 15.45, 3.975)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 7.7, 15.225, 3.7)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 7.7, 15.675, 3.7)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301015, 218028.46225)
    ops.uniaxialMaterial('Elastic', 401015, 285194.08205)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1016, 12.45, 15.45, 3.7, '-mass', 20.449834352701323, 20.449834352701323, 20.449834352701323, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 12.075, 15.45, 3.7)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 12.45, 15.45, 3.45)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 12.45, 15.45, 3.95)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 12.45, 15.3, 3.7)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 12.45, 15.6, 3.7)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301016, 118980.0175)
    ops.uniaxialMaterial('Elastic', 401016, 113719.64045)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 1)
    # Central joint node
    ops.node(1017, 0.0, 20.6, 3.7, '-mass', 13.336837410805302, 13.336837410805302, 13.336837410805302, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31017, 0.25, 20.6, 3.7)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 0.0, 20.6, 3.45)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 0.0, 20.6, 3.95)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 0.0, 20.475, 3.7)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 0.0, 20.725, 3.7)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301017, 85134.91065)
    ops.uniaxialMaterial('Elastic', 401017, 69400.045)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 1)
    # Central joint node
    ops.node(1018, 2.95, 20.6, 3.7, '-mass', 24.490239551478084, 24.490239551478084, 24.490239551478084, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 2.55, 20.6, 3.7)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(31018, 3.35, 20.6, 3.7)
    ops.element('elasticBeamColumn', 31018, 1018, 31018, 99999, 88888)
    ops.node(21018, 2.95, 20.6, 3.425)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 2.95, 20.6, 3.975)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 2.95, 20.425, 3.7)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 2.95, 20.775, 3.7)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301018, 162191.1985)
    ops.uniaxialMaterial('Elastic', 401018, 200109.20455)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 1)
    # Central joint node
    ops.node(1019, 7.7, 20.6, 3.7, '-mass', 31.84910805300713, 31.84910805300713, 31.84910805300713, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51019, 7.2, 20.6, 3.7)
    ops.element('elasticBeamColumn', 51019, 51019, 1019, 99999, 88888)
    ops.node(31019, 8.2, 20.6, 3.7)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 7.7, 20.6, 3.425)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 7.7, 20.6, 3.975)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 7.7, 20.375, 3.7)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    ops.node(41019, 7.7, 20.825, 3.7)
    ops.element('elasticBeamColumn', 41019, 1019, 41019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301019, 218028.46225)
    ops.uniaxialMaterial('Elastic', 401019, 285194.08205)
    ops.section('Aggregator', 11019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401019, 'My', 301019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11019, 1019, 11019, 11019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 1)
    # Central joint node
    ops.node(1020, 12.45, 20.6, 3.7, '-mass', 20.449834352701323, 20.449834352701323, 20.449834352701323, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 12.075, 20.6, 3.7)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(21020, 12.45, 20.6, 3.45)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 12.45, 20.6, 3.95)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 12.45, 20.45, 3.7)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    ops.node(41020, 12.45, 20.75, 3.7)
    ops.element('elasticBeamColumn', 41020, 1020, 41020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301020, 118980.0175)
    ops.uniaxialMaterial('Elastic', 401020, 113719.64045)
    ops.section('Aggregator', 11020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401020, 'My', 301020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11020, 1020, 11020, 11020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 1)
    # Central joint node
    ops.node(1021, 0.0, 25.75, 3.7, '-mass', 13.336837410805298, 13.336837410805298, 13.336837410805298, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31021, 0.25, 25.75, 3.7)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 0.0, 25.75, 3.45)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 0.0, 25.75, 3.95)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 0.0, 25.625, 3.7)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    ops.node(41021, 0.0, 25.875, 3.7)
    ops.element('elasticBeamColumn', 41021, 1021, 41021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301021, 85160.13435)
    ops.uniaxialMaterial('Elastic', 401021, 69419.73165)
    ops.section('Aggregator', 11021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401021, 'My', 301021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11021, 1021, 11021, 11021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 1)
    # Central joint node
    ops.node(1022, 2.95, 25.75, 3.7, '-mass', 24.490239551478076, 24.490239551478076, 24.490239551478076, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 2.55, 25.75, 3.7)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 3.35, 25.75, 3.7)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 2.95, 25.75, 3.425)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 2.95, 25.75, 3.975)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 2.95, 25.575, 3.7)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    ops.node(41022, 2.95, 25.925, 3.7)
    ops.element('elasticBeamColumn', 41022, 1022, 41022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301022, 162249.24465)
    ops.uniaxialMaterial('Elastic', 401022, 200179.98965)
    ops.section('Aggregator', 11022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401022, 'My', 301022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11022, 1022, 11022, 11022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 1)
    # Central joint node
    ops.node(1023, 7.7, 25.75, 3.7, '-mass', 31.84910805300712, 31.84910805300712, 31.84910805300712, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 7.2, 25.75, 3.7)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 8.2, 25.75, 3.7)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 7.7, 25.75, 3.425)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 7.7, 25.75, 3.975)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 7.7, 25.525, 3.7)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    ops.node(41023, 7.7, 25.975, 3.7)
    ops.element('elasticBeamColumn', 41023, 1023, 41023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301023, 218105.0168)
    ops.uniaxialMaterial('Elastic', 401023, 285292.56425)
    ops.section('Aggregator', 11023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401023, 'My', 301023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11023, 1023, 11023, 11023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 1)
    # Central joint node
    ops.node(1024, 12.45, 25.75, 3.7, '-mass', 20.44983435270132, 20.44983435270132, 20.44983435270132, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 12.075, 25.75, 3.7)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 12.45, 25.75, 3.45)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 12.45, 25.75, 3.95)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 12.45, 25.6, 3.7)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    ops.node(41024, 12.45, 25.9, 3.7)
    ops.element('elasticBeamColumn', 41024, 1024, 41024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301024, 119017.2156)
    ops.uniaxialMaterial('Elastic', 401024, 113754.01635)
    ops.section('Aggregator', 11024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401024, 'My', 301024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11024, 1024, 11024, 11024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 1)
    # Central joint node
    ops.node(1025, 0.0, 30.9, 3.7, '-mass', 8.311130224260957, 8.311130224260957, 8.311130224260957, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31025, 0.15, 30.9, 3.7)
    ops.element('elasticBeamColumn', 31025, 1025, 31025, 99999, 88888)
    ops.node(21025, 0.0, 30.9, 3.425)
    ops.element('elasticBeamColumn', 21025, 21025, 1025, 99999, 99999)
    ops.node(71025, 0.0, 30.9, 3.975)
    ops.element('elasticBeamColumn', 71025, 1025, 71025, 99999, 99999)
    ops.node(61025, 0.0, 30.75, 3.7)
    ops.element('elasticBeamColumn', 61025, 61025, 1025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301025, 46169.76415)
    ops.uniaxialMaterial('Elastic', 401025, 52112.5447)
    ops.section('Aggregator', 11025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401025, 'My', 301025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11025, 1025, 11025, 11025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 1)
    # Central joint node
    ops.node(1026, 2.95, 30.9, 3.7, '-mass', 16.999350152905194, 16.999350152905194, 16.999350152905194, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51026, 2.725, 30.9, 3.7)
    ops.element('elasticBeamColumn', 51026, 51026, 1026, 99999, 88888)
    ops.node(31026, 3.175, 30.9, 3.7)
    ops.element('elasticBeamColumn', 31026, 1026, 31026, 99999, 88888)
    ops.node(21026, 2.95, 30.9, 3.425)
    ops.element('elasticBeamColumn', 21026, 21026, 1026, 99999, 99999)
    ops.node(71026, 2.95, 30.9, 3.975)
    ops.element('elasticBeamColumn', 71026, 1026, 71026, 99999, 99999)
    ops.node(61026, 2.95, 30.6, 3.7)
    ops.element('elasticBeamColumn', 61026, 61026, 1026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301026, 129027.57965)
    ops.uniaxialMaterial('Elastic', 401026, 170034.9655)
    ops.section('Aggregator', 11026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401026, 'My', 301026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11026, 1026, 11026, 11026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 1)
    # Central joint node
    ops.node(1027, 7.7, 30.9, 3.7, '-mass', 21.506613149847087, 21.506613149847087, 21.506613149847087, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51027, 7.45, 30.9, 3.7)
    ops.element('elasticBeamColumn', 51027, 51027, 1027, 99999, 88888)
    ops.node(31027, 7.95, 30.9, 3.7)
    ops.element('elasticBeamColumn', 31027, 1027, 31027, 99999, 88888)
    ops.node(21027, 7.7, 30.9, 3.425)
    ops.element('elasticBeamColumn', 21027, 21027, 1027, 99999, 99999)
    ops.node(71027, 7.7, 30.9, 3.975)
    ops.element('elasticBeamColumn', 71027, 1027, 71027, 99999, 99999)
    ops.node(61027, 7.7, 30.55, 3.7)
    ops.element('elasticBeamColumn', 61027, 61027, 1027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301027, 162673.73325)
    ops.uniaxialMaterial('Elastic', 401027, 204355.49745)
    ops.section('Aggregator', 11027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401027, 'My', 301027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11027, 1027, 11027, 11027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 1)
    # Central joint node
    ops.node(1028, 12.45, 30.9, 3.7, '-mass', 12.875732670744137, 12.875732670744137, 12.875732670744137, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51028, 12.275, 30.9, 3.7)
    ops.element('elasticBeamColumn', 51028, 51028, 1028, 99999, 88888)
    ops.node(21028, 12.45, 30.9, 3.425)
    ops.element('elasticBeamColumn', 21028, 21028, 1028, 99999, 99999)
    ops.node(71028, 12.45, 30.9, 3.975)
    ops.element('elasticBeamColumn', 71028, 1028, 71028, 99999, 99999)
    ops.node(61028, 12.45, 30.675, 3.7)
    ops.element('elasticBeamColumn', 61028, 61028, 1028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301028, 73783.4549)
    ops.uniaxialMaterial('Elastic', 401028, 84766.5297)
    ops.section('Aggregator', 11028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401028, 'My', 301028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11028, 1028, 11028, 11028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 6.55, '-mass', 3.270514780835882, 3.270514780835882, 3.270514780835882, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.15, 0.0, 6.55)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 6.3)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.8)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.125, 6.55)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 39842.1313)
    ops.uniaxialMaterial('Elastic', 402001, 33378.57395)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 2.95, 0.0, 6.55, '-mass', 12.584906982670745, 12.584906982670745, 12.584906982670745, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 2.725, 0.0, 6.55)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 3.175, 0.0, 6.55)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 2.95, 0.0, 6.275)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 2.95, 0.0, 6.825)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 2.95, 0.3, 6.55)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 133517.8581)
    ops.uniaxialMaterial('Elastic', 402002, 131852.6964)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 7.7, 0.0, 6.55, '-mass', 20.14912079510703, 20.14912079510703, 20.14912079510703, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 7.45, 0.0, 6.55)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 7.95, 0.0, 6.55)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 7.7, 0.0, 6.275)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 7.7, 0.0, 6.825)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 7.7, 0.35, 6.55)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 139392.71505)
    ops.uniaxialMaterial('Elastic', 402003, 137675.8181)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 12.45, 0.0, 6.55, '-mass', 12.162888634046888, 12.162888634046888, 12.162888634046888, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 12.275, 0.0, 6.55)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 12.45, 0.0, 6.3)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 12.45, 0.0, 6.8)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 12.45, 0.225, 6.55)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 63202.2214)
    ops.uniaxialMaterial('Elastic', 402004, 56629.6334)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 5.15, 6.55, '-mass', 12.141692150866465, 12.141692150866465, 12.141692150866465, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.225, 5.15, 6.55)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 5.15, 6.3)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 5.15, 6.8)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 5.025, 6.55)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 5.275, 6.55)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 72666.64715)
    ops.uniaxialMaterial('Elastic', 402005, 43416.6881)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 2.95, 5.15, 6.55, '-mass', 24.73892711518858, 24.73892711518858, 24.73892711518858, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 2.525, 5.15, 6.55)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 3.375, 5.15, 6.55)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 2.95, 5.15, 6.275)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 2.95, 5.15, 6.825)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 2.95, 4.975, 6.55)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 2.95, 5.325, 6.55)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 141505.9026)
    ops.uniaxialMaterial('Elastic', 402006, 139747.30925)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 7.7, 5.15, 6.55, '-mass', 30.620056065239545, 30.620056065239545, 30.620056065239545, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 7.2, 5.15, 6.55)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 8.2, 5.15, 6.55)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 7.7, 5.15, 6.275)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 7.7, 5.15, 6.825)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 7.7, 4.925, 6.55)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 7.7, 5.375, 6.55)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 186661.90175)
    ops.uniaxialMaterial('Elastic', 402007, 189636.87685)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 12.45, 5.15, 6.55, '-mass', 19.852739551478084, 19.852739551478084, 19.852739551478084, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 12.075, 5.15, 6.55)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 12.45, 5.15, 6.3)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 12.45, 5.15, 6.8)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 12.45, 5.0, 6.55)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 12.45, 5.3, 6.55)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 101358.4712)
    ops.uniaxialMaterial('Elastic', 402008, 74831.15045)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 10.3, 6.55, '-mass', 13.029497961264015, 13.029497961264015, 13.029497961264015, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.25, 10.3, 6.55)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 10.3, 6.3)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 10.3, 6.8)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 10.175, 6.55)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 10.425, 6.55)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 72275.99945)
    ops.uniaxialMaterial('Elastic', 402009, 45444.69585)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 2.95, 10.3, 6.55, '-mass', 23.64115698267074, 23.64115698267074, 23.64115698267074, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 2.55, 10.3, 6.55)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 3.35, 10.3, 6.55)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 2.95, 10.3, 6.275)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 2.95, 10.3, 6.825)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 2.95, 10.125, 6.55)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 2.95, 10.475, 6.55)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 138670.56125)
    ops.uniaxialMaterial('Elastic', 402010, 132765.5534)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 7.7, 10.3, 6.55, '-mass', 30.620056065239545, 30.620056065239545, 30.620056065239545, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 7.2, 10.3, 6.55)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 8.2, 10.3, 6.55)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 7.7, 10.3, 6.275)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 7.7, 10.3, 6.825)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 7.7, 10.075, 6.55)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 7.7, 10.525, 6.55)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 186661.90175)
    ops.uniaxialMaterial('Elastic', 402011, 189636.87685)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 12.45, 10.3, 6.55, '-mass', 19.852739551478084, 19.852739551478084, 19.852739551478084, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 12.075, 10.3, 6.55)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 12.45, 10.3, 6.3)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 12.45, 10.3, 6.8)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 12.45, 10.15, 6.55)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 12.45, 10.45, 6.55)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 101358.4712)
    ops.uniaxialMaterial('Elastic', 402012, 74831.15045)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2013, 0.0, 15.45, 6.55, '-mass', 13.029497961264017, 13.029497961264017, 13.029497961264017, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.25, 15.45, 6.55)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 15.45, 6.3)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 15.45, 6.8)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 15.325, 6.55)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 15.575, 6.55)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302013, 72275.99945)
    ops.uniaxialMaterial('Elastic', 402013, 45444.69585)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2014, 2.95, 15.45, 6.55, '-mass', 23.64115698267074, 23.64115698267074, 23.64115698267074, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 2.55, 15.45, 6.55)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 3.35, 15.45, 6.55)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 2.95, 15.45, 6.275)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 2.95, 15.45, 6.825)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 2.95, 15.275, 6.55)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 2.95, 15.625, 6.55)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302014, 138670.56125)
    ops.uniaxialMaterial('Elastic', 402014, 132765.5534)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2015, 7.7, 15.45, 6.55, '-mass', 30.620056065239545, 30.620056065239545, 30.620056065239545, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 7.2, 15.45, 6.55)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 8.2, 15.45, 6.55)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 7.7, 15.45, 6.275)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 7.7, 15.45, 6.825)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 7.7, 15.225, 6.55)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 7.7, 15.675, 6.55)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302015, 186661.90175)
    ops.uniaxialMaterial('Elastic', 402015, 189636.87685)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2016, 12.45, 15.45, 6.55, '-mass', 19.852739551478084, 19.852739551478084, 19.852739551478084, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 12.075, 15.45, 6.55)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 12.45, 15.45, 6.3)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 12.45, 15.45, 6.8)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 12.45, 15.3, 6.55)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 12.45, 15.6, 6.55)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302016, 101358.4712)
    ops.uniaxialMaterial('Elastic', 402016, 74831.15045)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 2)
    # Central joint node
    ops.node(2017, 0.0, 20.6, 6.55, '-mass', 13.029497961264017, 13.029497961264017, 13.029497961264017, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32017, 0.25, 20.6, 6.55)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 0.0, 20.6, 6.3)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 0.0, 20.6, 6.8)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 0.0, 20.475, 6.55)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 0.0, 20.725, 6.55)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302017, 72275.99945)
    ops.uniaxialMaterial('Elastic', 402017, 45444.69585)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 2)
    # Central joint node
    ops.node(2018, 2.95, 20.6, 6.55, '-mass', 23.64115698267074, 23.64115698267074, 23.64115698267074, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 2.55, 20.6, 6.55)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(32018, 3.35, 20.6, 6.55)
    ops.element('elasticBeamColumn', 32018, 2018, 32018, 99999, 88888)
    ops.node(22018, 2.95, 20.6, 6.275)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 2.95, 20.6, 6.825)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 2.95, 20.425, 6.55)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 2.95, 20.775, 6.55)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302018, 138670.56125)
    ops.uniaxialMaterial('Elastic', 402018, 132765.5534)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 2)
    # Central joint node
    ops.node(2019, 7.7, 20.6, 6.55, '-mass', 30.620056065239545, 30.620056065239545, 30.620056065239545, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52019, 7.2, 20.6, 6.55)
    ops.element('elasticBeamColumn', 52019, 52019, 2019, 99999, 88888)
    ops.node(32019, 8.2, 20.6, 6.55)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 7.7, 20.6, 6.275)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 7.7, 20.6, 6.825)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 7.7, 20.375, 6.55)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    ops.node(42019, 7.7, 20.825, 6.55)
    ops.element('elasticBeamColumn', 42019, 2019, 42019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302019, 186661.90175)
    ops.uniaxialMaterial('Elastic', 402019, 189636.87685)
    ops.section('Aggregator', 12019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402019, 'My', 302019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12019, 2019, 12019, 12019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 2)
    # Central joint node
    ops.node(2020, 12.45, 20.6, 6.55, '-mass', 19.852739551478084, 19.852739551478084, 19.852739551478084, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 12.075, 20.6, 6.55)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(22020, 12.45, 20.6, 6.3)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 12.45, 20.6, 6.8)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 12.45, 20.45, 6.55)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    ops.node(42020, 12.45, 20.75, 6.55)
    ops.element('elasticBeamColumn', 42020, 2020, 42020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302020, 101358.4712)
    ops.uniaxialMaterial('Elastic', 402020, 74831.15045)
    ops.section('Aggregator', 12020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402020, 'My', 302020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12020, 2020, 12020, 12020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 2)
    # Central joint node
    ops.node(2021, 0.0, 25.75, 6.55, '-mass', 13.074604994903158, 13.074604994903158, 13.074604994903158, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32021, 0.25, 25.75, 6.55)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 0.0, 25.75, 6.3)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 0.0, 25.75, 6.8)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 0.0, 25.625, 6.55)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    ops.node(42021, 0.0, 25.875, 6.55)
    ops.element('elasticBeamColumn', 42021, 2021, 42021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302021, 72305.7091)
    ops.uniaxialMaterial('Elastic', 402021, 52275.91235)
    ops.section('Aggregator', 12021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402021, 'My', 302021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12021, 2021, 12021, 12021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 2)
    # Central joint node
    ops.node(2022, 2.95, 25.75, 6.55, '-mass', 23.75889398572884, 23.75889398572884, 23.75889398572884, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 2.55, 25.75, 6.55)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 3.35, 25.75, 6.55)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 2.95, 25.75, 6.275)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 2.95, 25.75, 6.825)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 2.95, 25.575, 6.55)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    ops.node(42022, 2.95, 25.925, 6.55)
    ops.element('elasticBeamColumn', 42022, 2022, 42022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302022, 138738.4484)
    ops.uniaxialMaterial('Elastic', 402022, 151868.153)
    ops.section('Aggregator', 12022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402022, 'My', 302022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12022, 2022, 12022, 12022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 2)
    # Central joint node
    ops.node(2023, 7.7, 25.75, 6.55, '-mass', 30.765316004077462, 30.765316004077462, 30.765316004077462, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 7.2, 25.75, 6.55)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 8.2, 25.75, 6.55)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 7.7, 25.75, 6.275)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 7.7, 25.75, 6.825)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 7.7, 25.525, 6.55)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    ops.node(42023, 7.7, 25.975, 6.55)
    ops.element('elasticBeamColumn', 42023, 2023, 42023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302023, 186751.3148)
    ops.uniaxialMaterial('Elastic', 402023, 216919.3105)
    ops.section('Aggregator', 12023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402023, 'My', 302023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12023, 2023, 12023, 12023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 2)
    # Central joint node
    ops.node(2024, 12.45, 25.75, 6.55, '-mass', 19.92536952089704, 19.92536952089704, 19.92536952089704, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 12.075, 25.75, 6.55)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 12.45, 25.75, 6.3)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 12.45, 25.75, 6.8)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 12.45, 25.6, 6.55)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    ops.node(42024, 12.45, 25.9, 6.55)
    ops.element('elasticBeamColumn', 42024, 2024, 42024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302024, 101402.13375)
    ops.uniaxialMaterial('Elastic', 402024, 85944.33955)
    ops.section('Aggregator', 12024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402024, 'My', 302024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12024, 2024, 12024, 12024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 2)
    # Central joint node
    ops.node(2025, 0.0, 30.9, 6.55, '-mass', 7.977338175331293, 7.977338175331293, 7.977338175331293, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32025, 0.15, 30.9, 6.55)
    ops.element('elasticBeamColumn', 32025, 2025, 32025, 99999, 88888)
    ops.node(22025, 0.0, 30.9, 6.3)
    ops.element('elasticBeamColumn', 22025, 22025, 2025, 99999, 99999)
    ops.node(72025, 0.0, 30.9, 6.8)
    ops.element('elasticBeamColumn', 72025, 2025, 72025, 99999, 99999)
    ops.node(62025, 0.0, 30.75, 6.55)
    ops.element('elasticBeamColumn', 62025, 62025, 2025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302025, 39650.86775)
    ops.uniaxialMaterial('Elastic', 402025, 39650.86775)
    ops.section('Aggregator', 12025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402025, 'My', 302025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12025, 2025, 12025, 12025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 2)
    # Central joint node
    ops.node(2026, 2.95, 30.9, 6.55, '-mass', 16.010665137614673, 16.010665137614673, 16.010665137614673, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52026, 2.725, 30.9, 6.55)
    ops.element('elasticBeamColumn', 52026, 52026, 2026, 99999, 88888)
    ops.node(32026, 3.175, 30.9, 6.55)
    ops.element('elasticBeamColumn', 32026, 2026, 32026, 99999, 88888)
    ops.node(22026, 2.95, 30.9, 6.275)
    ops.element('elasticBeamColumn', 22026, 22026, 2026, 99999, 99999)
    ops.node(72026, 2.95, 30.9, 6.825)
    ops.element('elasticBeamColumn', 72026, 2026, 72026, 99999, 99999)
    ops.node(62026, 2.95, 30.6, 6.55)
    ops.element('elasticBeamColumn', 62026, 62026, 2026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302026, 110630.2696)
    ops.uniaxialMaterial('Elastic', 402026, 129364.3218)
    ops.section('Aggregator', 12026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402026, 'My', 302026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12026, 2026, 12026, 12026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 2)
    # Central joint node
    ops.node(2027, 7.7, 30.9, 6.55, '-mass', 20.294380733944948, 20.294380733944948, 20.294380733944948, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52027, 7.45, 30.9, 6.55)
    ops.element('elasticBeamColumn', 52027, 52027, 2027, 99999, 88888)
    ops.node(32027, 7.95, 30.9, 6.55)
    ops.element('elasticBeamColumn', 32027, 2027, 32027, 99999, 88888)
    ops.node(22027, 7.7, 30.9, 6.275)
    ops.element('elasticBeamColumn', 22027, 22027, 2027, 99999, 99999)
    ops.node(72027, 7.7, 30.9, 6.825)
    ops.element('elasticBeamColumn', 72027, 2027, 72027, 99999, 99999)
    ops.node(62027, 7.7, 30.55, 6.55)
    ops.element('elasticBeamColumn', 62027, 62027, 2027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302027, 139504.4726)
    ops.uniaxialMaterial('Elastic', 402027, 155637.4523)
    ops.section('Aggregator', 12027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402027, 'My', 302027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12027, 2027, 12027, 12027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 2)
    # Central joint node
    ops.node(2028, 12.45, 30.9, 6.55, '-mass', 12.235518603465849, 12.235518603465849, 12.235518603465849, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52028, 12.275, 30.9, 6.55)
    ops.element('elasticBeamColumn', 52028, 52028, 2028, 99999, 88888)
    ops.node(22028, 12.45, 30.9, 6.3)
    ops.element('elasticBeamColumn', 22028, 22028, 2028, 99999, 99999)
    ops.node(72028, 12.45, 30.9, 6.8)
    ops.element('elasticBeamColumn', 72028, 2028, 72028, 99999, 99999)
    ops.node(62028, 12.45, 30.675, 6.55)
    ops.element('elasticBeamColumn', 62028, 62028, 2028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302028, 63247.2374)
    ops.uniaxialMaterial('Elastic', 402028, 64638.56925)
    ops.section('Aggregator', 12028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402028, 'My', 302028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12028, 2028, 12028, 12028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 9.4, '-mass', 3.2036187563710503, 3.2036187563710503, 3.2036187563710503, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 9.4)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 9.15)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 9.65)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 9.4)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 27417.15595)
    ops.uniaxialMaterial('Elastic', 403001, 19668.19785)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 2.95, 0.0, 9.4, '-mass', 12.301573649337412, 12.301573649337412, 12.301573649337412, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 2.775, 0.0, 9.4)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 3.125, 0.0, 9.4)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 2.95, 0.0, 9.125)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 2.95, 0.0, 9.675)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 2.95, 0.25, 9.4)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 83728.10365)
    ops.uniaxialMaterial('Elastic', 403002, 72657.15405)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 7.7, 0.0, 9.4, '-mass', 19.620374617737, 19.620374617737, 19.620374617737, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 7.5, 0.0, 9.4)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 7.9, 0.0, 9.4)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 7.7, 0.0, 9.125)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 7.7, 0.0, 9.675)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 7.7, 0.3, 9.4)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 92225.17995)
    ops.uniaxialMaterial('Elastic', 403003, 81125.22795)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 12.45, 0.0, 9.4, '-mass', 11.846221967380222, 11.846221967380222, 11.846221967380222, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 12.325, 0.0, 9.4)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 12.45, 0.0, 9.15)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 12.45, 0.0, 9.65)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 12.45, 0.175, 9.4)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 37429.16215)
    ops.uniaxialMaterial('Elastic', 403004, 29309.93175)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 5.15, 9.4, '-mass', 12.054536187563713, 12.054536187563713, 12.054536187563713, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.175, 5.15, 9.4)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 5.15, 9.15)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 5.15, 9.65)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 5.025, 9.4)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 5.275, 9.4)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 56389.74505)
    ops.uniaxialMaterial('Elastic', 403005, 31263.28965)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 2.95, 5.15, 9.4, '-mass', 24.35544087665647, 24.35544087665647, 24.35544087665647, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 2.575, 5.15, 9.4)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 3.325, 5.15, 9.4)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 2.95, 5.15, 9.125)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 2.95, 5.15, 9.675)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 2.95, 5.025, 9.4)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 2.95, 5.275, 9.4)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 89947.3527)
    ops.uniaxialMaterial('Elastic', 403006, 97622.10975)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 7.7, 5.15, 9.4, '-mass', 30.149413863404682, 30.149413863404682, 30.149413863404682, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 7.25, 5.15, 9.4)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 8.15, 5.15, 9.4)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 7.7, 5.15, 9.125)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 7.7, 5.15, 9.675)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 7.7, 4.975, 9.4)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 7.7, 5.325, 9.4)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 124270.19125)
    ops.uniaxialMaterial('Elastic', 403007, 126770.39555)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 12.45, 5.15, 9.4, '-mass', 19.634849643221198, 19.634849643221198, 19.634849643221198, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 12.125, 5.15, 9.4)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 12.45, 5.15, 9.15)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 12.45, 5.15, 9.65)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 12.45, 5.025, 9.4)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 12.45, 5.275, 9.4)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 70780.027)
    ops.uniaxialMaterial('Elastic', 403008, 55729.4981)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 10.3, 9.4, '-mass', 12.942341997961263, 12.942341997961263, 12.942341997961263, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.2, 10.3, 9.4)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 10.3, 9.15)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 10.3, 9.65)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 10.175, 9.4)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 10.425, 9.4)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 56809.50055)
    ops.uniaxialMaterial('Elastic', 403009, 32425.9372)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 2.95, 10.3, 9.4, '-mass', 23.318679918450556, 23.318679918450556, 23.318679918450556, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 2.575, 10.3, 9.4)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 3.325, 10.3, 9.4)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 2.95, 10.3, 9.125)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 2.95, 10.3, 9.675)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 2.95, 10.175, 9.4)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 2.95, 10.425, 9.4)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 87492.7446)
    ops.uniaxialMaterial('Elastic', 403010, 95021.54345)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 7.7, 10.3, 9.4, '-mass', 30.149413863404682, 30.149413863404682, 30.149413863404682, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 7.25, 10.3, 9.4)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 8.15, 10.3, 9.4)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 7.7, 10.3, 9.125)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 7.7, 10.3, 9.675)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 7.7, 10.125, 9.4)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 7.7, 10.475, 9.4)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 124270.19125)
    ops.uniaxialMaterial('Elastic', 403011, 126770.39555)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 12.45, 10.3, 9.4, '-mass', 19.634849643221198, 19.634849643221198, 19.634849643221198, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 12.125, 10.3, 9.4)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 12.45, 10.3, 9.15)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 12.45, 10.3, 9.65)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 12.45, 10.175, 9.4)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 12.45, 10.425, 9.4)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 70780.027)
    ops.uniaxialMaterial('Elastic', 403012, 55729.4981)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3013, 0.0, 15.45, 9.4, '-mass', 12.942341997961265, 12.942341997961265, 12.942341997961265, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.2, 15.45, 9.4)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 15.45, 9.15)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 15.45, 9.65)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 15.325, 9.4)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 15.575, 9.4)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303013, 56809.50055)
    ops.uniaxialMaterial('Elastic', 403013, 32425.9372)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3014, 2.95, 15.45, 9.4, '-mass', 23.318679918450556, 23.318679918450556, 23.318679918450556, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 2.575, 15.45, 9.4)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 3.325, 15.45, 9.4)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 2.95, 15.45, 9.125)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 2.95, 15.45, 9.675)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 2.95, 15.325, 9.4)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 2.95, 15.575, 9.4)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303014, 87492.7446)
    ops.uniaxialMaterial('Elastic', 403014, 95021.54345)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3015, 7.7, 15.45, 9.4, '-mass', 30.149413863404682, 30.149413863404682, 30.149413863404682, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 7.25, 15.45, 9.4)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 8.15, 15.45, 9.4)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 7.7, 15.45, 9.125)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 7.7, 15.45, 9.675)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 7.7, 15.275, 9.4)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 7.7, 15.625, 9.4)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303015, 124270.19125)
    ops.uniaxialMaterial('Elastic', 403015, 126770.39555)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3016, 12.45, 15.45, 9.4, '-mass', 19.634849643221198, 19.634849643221198, 19.634849643221198, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 12.125, 15.45, 9.4)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 12.45, 15.45, 9.15)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 12.45, 15.45, 9.65)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 12.45, 15.325, 9.4)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 12.45, 15.575, 9.4)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303016, 70780.027)
    ops.uniaxialMaterial('Elastic', 403016, 55729.4981)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 3)
    # Central joint node
    ops.node(3017, 0.0, 20.6, 9.4, '-mass', 12.942341997961265, 12.942341997961265, 12.942341997961265, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33017, 0.2, 20.6, 9.4)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 0.0, 20.6, 9.15)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 0.0, 20.6, 9.65)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 0.0, 20.475, 9.4)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 0.0, 20.725, 9.4)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303017, 56809.50055)
    ops.uniaxialMaterial('Elastic', 403017, 32425.9372)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 3)
    # Central joint node
    ops.node(3018, 2.95, 20.6, 9.4, '-mass', 23.318679918450556, 23.318679918450556, 23.318679918450556, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 2.575, 20.6, 9.4)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(33018, 3.325, 20.6, 9.4)
    ops.element('elasticBeamColumn', 33018, 3018, 33018, 99999, 88888)
    ops.node(23018, 2.95, 20.6, 9.125)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 2.95, 20.6, 9.675)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 2.95, 20.475, 9.4)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 2.95, 20.725, 9.4)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303018, 87492.7446)
    ops.uniaxialMaterial('Elastic', 403018, 95021.54345)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 3)
    # Central joint node
    ops.node(3019, 7.7, 20.6, 9.4, '-mass', 30.149413863404682, 30.149413863404682, 30.149413863404682, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53019, 7.25, 20.6, 9.4)
    ops.element('elasticBeamColumn', 53019, 53019, 3019, 99999, 88888)
    ops.node(33019, 8.15, 20.6, 9.4)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 7.7, 20.6, 9.125)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 7.7, 20.6, 9.675)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 7.7, 20.425, 9.4)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    ops.node(43019, 7.7, 20.775, 9.4)
    ops.element('elasticBeamColumn', 43019, 3019, 43019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303019, 124270.19125)
    ops.uniaxialMaterial('Elastic', 403019, 126770.39555)
    ops.section('Aggregator', 13019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403019, 'My', 303019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13019, 3019, 13019, 13019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 3)
    # Central joint node
    ops.node(3020, 12.45, 20.6, 9.4, '-mass', 19.634849643221198, 19.634849643221198, 19.634849643221198, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 12.125, 20.6, 9.4)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(23020, 12.45, 20.6, 9.15)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 12.45, 20.6, 9.65)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 12.45, 20.475, 9.4)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    ops.node(43020, 12.45, 20.725, 9.4)
    ops.element('elasticBeamColumn', 43020, 3020, 43020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303020, 70780.027)
    ops.uniaxialMaterial('Elastic', 403020, 55729.4981)
    ops.section('Aggregator', 13020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403020, 'My', 303020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13020, 3020, 13020, 13020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 3)
    # Central joint node
    ops.node(3021, 0.0, 25.75, 9.4, '-mass', 12.942341997961261, 12.942341997961261, 12.942341997961261, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33021, 0.2, 25.75, 9.4)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 0.0, 25.75, 9.15)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 0.0, 25.75, 9.65)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 0.0, 25.625, 9.4)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    ops.node(43021, 0.0, 25.875, 9.4)
    ops.element('elasticBeamColumn', 43021, 3021, 43021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303021, 56809.50055)
    ops.uniaxialMaterial('Elastic', 403021, 32425.9372)
    ops.section('Aggregator', 13021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403021, 'My', 303021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13021, 3021, 13021, 13021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 3)
    # Central joint node
    ops.node(3022, 2.95, 25.75, 9.4, '-mass', 23.318679918450552, 23.318679918450552, 23.318679918450552, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 2.575, 25.75, 9.4)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 3.325, 25.75, 9.4)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 2.95, 25.75, 9.125)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 2.95, 25.75, 9.675)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 2.95, 25.625, 9.4)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    ops.node(43022, 2.95, 25.875, 9.4)
    ops.element('elasticBeamColumn', 43022, 3022, 43022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303022, 87492.7446)
    ops.uniaxialMaterial('Elastic', 403022, 95021.54345)
    ops.section('Aggregator', 13022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403022, 'My', 303022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13022, 3022, 13022, 13022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 3)
    # Central joint node
    ops.node(3023, 7.7, 25.75, 9.4, '-mass', 30.149413863404675, 30.149413863404675, 30.149413863404675, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 7.25, 25.75, 9.4)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 8.15, 25.75, 9.4)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 7.7, 25.75, 9.125)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 7.7, 25.75, 9.675)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 7.7, 25.575, 9.4)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    ops.node(43023, 7.7, 25.925, 9.4)
    ops.element('elasticBeamColumn', 43023, 3023, 43023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303023, 124270.19125)
    ops.uniaxialMaterial('Elastic', 403023, 126770.39555)
    ops.section('Aggregator', 13023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403023, 'My', 303023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13023, 3023, 13023, 13023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 3)
    # Central joint node
    ops.node(3024, 12.45, 25.75, 9.4, '-mass', 19.63484964322119, 19.63484964322119, 19.63484964322119, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 12.125, 25.75, 9.4)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 12.45, 25.75, 9.15)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 12.45, 25.75, 9.65)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 12.45, 25.625, 9.4)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    ops.node(43024, 12.45, 25.875, 9.4)
    ops.element('elasticBeamColumn', 43024, 3024, 43024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303024, 70780.027)
    ops.uniaxialMaterial('Elastic', 403024, 55729.4981)
    ops.section('Aggregator', 13024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403024, 'My', 303024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13024, 3024, 13024, 13024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 3)
    # Central joint node
    ops.node(3025, 0.0, 30.9, 9.4, '-mass', 7.791252548419978, 7.791252548419978, 7.791252548419978, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33025, 0.125, 30.9, 9.4)
    ops.element('elasticBeamColumn', 33025, 3025, 33025, 99999, 88888)
    ops.node(23025, 0.0, 30.9, 9.15)
    ops.element('elasticBeamColumn', 23025, 23025, 3025, 99999, 99999)
    ops.node(73025, 0.0, 30.9, 9.65)
    ops.element('elasticBeamColumn', 73025, 3025, 73025, 99999, 99999)
    ops.node(63025, 0.0, 30.775, 9.4)
    ops.element('elasticBeamColumn', 63025, 63025, 3025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303025, 26451.9075)
    ops.uniaxialMaterial('Elastic', 403025, 19925.913)
    ops.section('Aggregator', 13025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403025, 'My', 303025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13025, 3025, 13025, 13025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 3)
    # Central joint node
    ops.node(3026, 2.95, 30.9, 9.4, '-mass', 15.44399847094801, 15.44399847094801, 15.44399847094801, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53026, 2.775, 30.9, 9.4)
    ops.element('elasticBeamColumn', 53026, 53026, 3026, 99999, 88888)
    ops.node(33026, 3.125, 30.9, 9.4)
    ops.element('elasticBeamColumn', 33026, 3026, 33026, 99999, 88888)
    ops.node(23026, 2.95, 30.9, 9.125)
    ops.element('elasticBeamColumn', 23026, 23026, 3026, 99999, 99999)
    ops.node(73026, 2.95, 30.9, 9.675)
    ops.element('elasticBeamColumn', 73026, 3026, 73026, 99999, 99999)
    ops.node(63026, 2.95, 30.65, 9.4)
    ops.element('elasticBeamColumn', 63026, 63026, 3026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303026, 70975.0344)
    ops.uniaxialMaterial('Elastic', 403026, 66071.8611)
    ops.section('Aggregator', 13026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403026, 'My', 303026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13026, 3026, 13026, 13026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 3)
    # Central joint node
    ops.node(3027, 7.7, 30.9, 9.4, '-mass', 19.620374617736996, 19.620374617736996, 19.620374617736996, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53027, 7.5, 30.9, 9.4)
    ops.element('elasticBeamColumn', 53027, 53027, 3027, 99999, 88888)
    ops.node(33027, 7.9, 30.9, 9.4)
    ops.element('elasticBeamColumn', 33027, 3027, 33027, 99999, 88888)
    ops.node(23027, 7.7, 30.9, 9.125)
    ops.element('elasticBeamColumn', 23027, 23027, 3027, 99999, 99999)
    ops.node(73027, 7.7, 30.9, 9.675)
    ops.element('elasticBeamColumn', 73027, 3027, 73027, 99999, 99999)
    ops.node(63027, 7.7, 30.6, 9.4)
    ops.element('elasticBeamColumn', 63027, 63027, 3027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303027, 92225.17995)
    ops.uniaxialMaterial('Elastic', 403027, 81125.22795)
    ops.section('Aggregator', 13027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403027, 'My', 303027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13027, 3027, 13027, 13027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 3)
    # Central joint node
    ops.node(3028, 12.45, 30.9, 9.4, '-mass', 11.846221967380222, 11.846221967380222, 11.846221967380222, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53028, 12.325, 30.9, 9.4)
    ops.element('elasticBeamColumn', 53028, 53028, 3028, 99999, 88888)
    ops.node(23028, 12.45, 30.9, 9.15)
    ops.element('elasticBeamColumn', 23028, 23028, 3028, 99999, 99999)
    ops.node(73028, 12.45, 30.9, 9.65)
    ops.element('elasticBeamColumn', 73028, 3028, 73028, 99999, 99999)
    ops.node(63028, 12.45, 30.725, 9.4)
    ops.element('elasticBeamColumn', 63028, 63028, 3028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303028, 37429.16215)
    ops.uniaxialMaterial('Elastic', 403028, 29309.93175)
    ops.section('Aggregator', 13028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403028, 'My', 303028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13028, 3028, 13028, 13028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 12.25, '-mass', 0.8294342507645261, 0.8294342507645261, 0.8294342507645261, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 12.25)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 12.05)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 12.25)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 12788.73195)
    ops.uniaxialMaterial('Elastic', 404001, 8710.788)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 2.95, 0.0, 12.25, '-mass', 7.260079001019369, 7.260079001019369, 7.260079001019369, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 2.775, 0.0, 12.25)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 3.125, 0.0, 12.25)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 2.95, 0.0, 12.0)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 2.95, 0.25, 12.25)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 55839.5218)
    ops.uniaxialMaterial('Elastic', 404002, 29663.93515)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 7.7, 0.0, 12.25, '-mass', 13.683766564729867, 13.683766564729867, 13.683766564729867, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 7.5, 0.0, 12.25)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 7.9, 0.0, 12.25)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 7.7, 0.0, 12.0)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 7.7, 0.3, 12.25)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 84840.6648)
    ops.uniaxialMaterial('Elastic', 404003, 45252.1282)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 12.45, 0.0, 12.25, '-mass', 6.886072884811416, 6.886072884811416, 6.886072884811416, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 12.325, 0.0, 12.25)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 12.45, 0.0, 12.05)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 12.45, 0.175, 12.25)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 29296.10465)
    ops.uniaxialMaterial('Elastic', 404004, 22122.24195)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 5.15, 12.25, '-mass', 7.037455402650358, 7.037455402650358, 7.037455402650358, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.175, 5.15, 12.25)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 5.15, 12.05)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 5.025, 12.25)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 5.275, 12.25)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 34969.19105)
    ops.uniaxialMaterial('Elastic', 404005, 34944.81925)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 2.95, 5.15, 12.25, '-mass', 19.62275101936799, 19.62275101936799, 19.62275101936799, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 2.575, 5.15, 12.25)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 3.325, 5.15, 12.25)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 2.95, 5.15, 12.0)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 2.95, 5.025, 12.25)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 2.95, 5.275, 12.25)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 59104.252)
    ops.uniaxialMaterial('Elastic', 404006, 66948.91985)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 7.7, 5.15, 12.25, '-mass', 26.32747196738022, 26.32747196738022, 26.32747196738022, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 7.25, 5.15, 12.25)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 8.15, 5.15, 12.25)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 7.7, 5.15, 12.0)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 7.7, 4.975, 12.25)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 7.7, 5.325, 12.25)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 79014.90605)
    ops.uniaxialMaterial('Elastic', 404007, 93805.95175)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 12.45, 5.15, 12.25, '-mass', 13.496151885830782, 13.496151885830782, 13.496151885830782, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 12.125, 5.15, 12.25)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 12.45, 5.15, 12.05)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 12.45, 5.025, 12.25)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 12.45, 5.275, 12.25)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 38789.07365)
    ops.uniaxialMaterial('Elastic', 404008, 52278.5016)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 10.3, 12.25, '-mass', 7.48361365953109, 7.48361365953109, 7.48361365953109, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.2, 10.3, 12.25)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 10.3, 12.05)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 10.175, 12.25)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 10.425, 12.25)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 30531.85575)
    ops.uniaxialMaterial('Elastic', 404009, 32247.38965)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 2.95, 10.3, 12.25, '-mass', 20.025331294597347, 20.025331294597347, 20.025331294597347, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 2.575, 10.3, 12.25)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 3.325, 10.3, 12.25)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 2.95, 10.3, 12.0)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 2.95, 10.175, 12.25)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 2.95, 10.425, 12.25)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 55670.22995)
    ops.uniaxialMaterial('Elastic', 404010, 62795.33975)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 7.7, 10.3, 12.25, '-mass', 26.32747196738022, 26.32747196738022, 26.32747196738022, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 7.25, 10.3, 12.25)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 8.15, 10.3, 12.25)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 7.7, 10.3, 12.0)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 7.7, 10.125, 12.25)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 7.7, 10.475, 12.25)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 79014.90605)
    ops.uniaxialMaterial('Elastic', 404011, 93805.95175)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 12.45, 10.3, 12.25, '-mass', 13.496151885830782, 13.496151885830782, 13.496151885830782, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 12.125, 10.3, 12.25)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 12.45, 10.3, 12.05)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 12.45, 10.175, 12.25)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 12.45, 10.425, 12.25)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 38789.07365)
    ops.uniaxialMaterial('Elastic', 404012, 52278.5016)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4013, 0.0, 15.45, 12.25, '-mass', 7.483613659531091, 7.483613659531091, 7.483613659531091, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.2, 15.45, 12.25)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 15.45, 12.05)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 15.325, 12.25)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 15.575, 12.25)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304013, 30531.85575)
    ops.uniaxialMaterial('Elastic', 404013, 32247.38965)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4014, 2.95, 15.45, 12.25, '-mass', 20.025331294597347, 20.025331294597347, 20.025331294597347, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 2.575, 15.45, 12.25)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 3.325, 15.45, 12.25)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 2.95, 15.45, 12.0)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 2.95, 15.325, 12.25)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 2.95, 15.575, 12.25)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304014, 55670.22995)
    ops.uniaxialMaterial('Elastic', 404014, 62795.33975)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4015, 7.7, 15.45, 12.25, '-mass', 26.32747196738022, 26.32747196738022, 26.32747196738022, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 7.25, 15.45, 12.25)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 8.15, 15.45, 12.25)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 7.7, 15.45, 12.0)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 7.7, 15.275, 12.25)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 7.7, 15.625, 12.25)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304015, 79014.90605)
    ops.uniaxialMaterial('Elastic', 404015, 93805.95175)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4016, 12.45, 15.45, 12.25, '-mass', 13.496151885830782, 13.496151885830782, 13.496151885830782, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 12.125, 15.45, 12.25)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 12.45, 15.45, 12.05)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 12.45, 15.325, 12.25)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 12.45, 15.575, 12.25)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304016, 38789.07365)
    ops.uniaxialMaterial('Elastic', 404016, 52278.5016)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 4)
    # Central joint node
    ops.node(4017, 0.0, 20.6, 12.25, '-mass', 7.483613659531091, 7.483613659531091, 7.483613659531091, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 0.2, 20.6, 12.25)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 0.0, 20.6, 12.05)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 0.0, 20.475, 12.25)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 0.0, 20.725, 12.25)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304017, 30531.85575)
    ops.uniaxialMaterial('Elastic', 404017, 32247.38965)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 4)
    # Central joint node
    ops.node(4018, 2.95, 20.6, 12.25, '-mass', 20.025331294597347, 20.025331294597347, 20.025331294597347, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 2.575, 20.6, 12.25)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(34018, 3.325, 20.6, 12.25)
    ops.element('elasticBeamColumn', 34018, 4018, 34018, 99999, 88888)
    ops.node(24018, 2.95, 20.6, 12.0)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 2.95, 20.475, 12.25)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 2.95, 20.725, 12.25)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304018, 55670.22995)
    ops.uniaxialMaterial('Elastic', 404018, 62795.33975)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 4)
    # Central joint node
    ops.node(4019, 7.7, 20.6, 12.25, '-mass', 26.32747196738022, 26.32747196738022, 26.32747196738022, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54019, 7.25, 20.6, 12.25)
    ops.element('elasticBeamColumn', 54019, 54019, 4019, 99999, 88888)
    ops.node(34019, 8.15, 20.6, 12.25)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 7.7, 20.6, 12.0)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 7.7, 20.425, 12.25)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    ops.node(44019, 7.7, 20.775, 12.25)
    ops.element('elasticBeamColumn', 44019, 4019, 44019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304019, 79014.90605)
    ops.uniaxialMaterial('Elastic', 404019, 93805.95175)
    ops.section('Aggregator', 14019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404019, 'My', 304019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14019, 4019, 14019, 14019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 4)
    # Central joint node
    ops.node(4020, 12.45, 20.6, 12.25, '-mass', 13.496151885830782, 13.496151885830782, 13.496151885830782, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 12.125, 20.6, 12.25)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 12.45, 20.6, 12.05)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 12.45, 20.475, 12.25)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    ops.node(44020, 12.45, 20.725, 12.25)
    ops.element('elasticBeamColumn', 44020, 4020, 44020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304020, 38789.07365)
    ops.uniaxialMaterial('Elastic', 404020, 52278.5016)
    ops.section('Aggregator', 14020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404020, 'My', 304020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14020, 4020, 14020, 14020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 4)
    # Central joint node
    ops.node(4021, 0.0, 25.75, 12.25, '-mass', 7.483613659531089, 7.483613659531089, 7.483613659531089, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 0.2, 25.75, 12.25)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 0.0, 25.75, 12.05)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 0.0, 25.625, 12.25)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    ops.node(44021, 0.0, 25.875, 12.25)
    ops.element('elasticBeamColumn', 44021, 4021, 44021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304021, 30531.85575)
    ops.uniaxialMaterial('Elastic', 404021, 32247.38965)
    ops.section('Aggregator', 14021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404021, 'My', 304021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14021, 4021, 14021, 14021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 4)
    # Central joint node
    ops.node(4022, 2.95, 25.75, 12.25, '-mass', 20.025331294597343, 20.025331294597343, 20.025331294597343, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 2.575, 25.75, 12.25)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 3.325, 25.75, 12.25)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 2.95, 25.75, 12.0)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 2.95, 25.625, 12.25)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    ops.node(44022, 2.95, 25.875, 12.25)
    ops.element('elasticBeamColumn', 44022, 4022, 44022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304022, 55670.22995)
    ops.uniaxialMaterial('Elastic', 404022, 62795.33975)
    ops.section('Aggregator', 14022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404022, 'My', 304022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14022, 4022, 14022, 14022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 4)
    # Central joint node
    ops.node(4023, 7.7, 25.75, 12.25, '-mass', 26.327471967380212, 26.327471967380212, 26.327471967380212, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 7.25, 25.75, 12.25)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 8.15, 25.75, 12.25)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 7.7, 25.75, 12.0)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 7.7, 25.575, 12.25)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    ops.node(44023, 7.7, 25.925, 12.25)
    ops.element('elasticBeamColumn', 44023, 4023, 44023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304023, 79014.90605)
    ops.uniaxialMaterial('Elastic', 404023, 93805.95175)
    ops.section('Aggregator', 14023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404023, 'My', 304023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14023, 4023, 14023, 14023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 4)
    # Central joint node
    ops.node(4024, 12.45, 25.75, 12.25, '-mass', 13.496151885830779, 13.496151885830779, 13.496151885830779, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 12.125, 25.75, 12.25)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 12.45, 25.75, 12.05)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 12.45, 25.625, 12.25)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    ops.node(44024, 12.45, 25.875, 12.25)
    ops.element('elasticBeamColumn', 44024, 4024, 44024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304024, 38789.07365)
    ops.uniaxialMaterial('Elastic', 404024, 52278.5016)
    ops.section('Aggregator', 14024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404024, 'My', 304024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14024, 4024, 14024, 14024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 4)
    # Central joint node
    ops.node(4025, 0.0, 30.9, 12.25, '-mass', 3.857556065239551, 3.857556065239551, 3.857556065239551, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 0.125, 30.9, 12.25)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 0.0, 30.9, 12.05)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(64025, 0.0, 30.775, 12.25)
    ops.element('elasticBeamColumn', 64025, 64025, 4025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304025, 20203.1895)
    ops.uniaxialMaterial('Elastic', 404025, 14371.60045)
    ops.section('Aggregator', 14025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404025, 'My', 304025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14025, 4025, 14025, 14025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 4)
    # Central joint node
    ops.node(4026, 2.95, 30.9, 12.25, '-mass', 10.484301732925585, 10.484301732925585, 10.484301732925585, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 2.775, 30.9, 12.25)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(34026, 3.125, 30.9, 12.25)
    ops.element('elasticBeamColumn', 34026, 4026, 34026, 99999, 88888)
    ops.node(24026, 2.95, 30.9, 12.0)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(64026, 2.95, 30.65, 12.25)
    ops.element('elasticBeamColumn', 64026, 64026, 4026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304026, 64544.3377)
    ops.uniaxialMaterial('Elastic', 404026, 34530.70435)
    ops.section('Aggregator', 14026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404026, 'My', 304026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14026, 4026, 14026, 14026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 4)
    # Central joint node
    ops.node(4027, 7.7, 30.9, 12.25, '-mass', 13.683766564729863, 13.683766564729863, 13.683766564729863, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54027, 7.5, 30.9, 12.25)
    ops.element('elasticBeamColumn', 54027, 54027, 4027, 99999, 88888)
    ops.node(34027, 7.9, 30.9, 12.25)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 7.7, 30.9, 12.0)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(64027, 7.7, 30.6, 12.25)
    ops.element('elasticBeamColumn', 64027, 64027, 4027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304027, 84840.6648)
    ops.uniaxialMaterial('Elastic', 404027, 45252.1282)
    ops.section('Aggregator', 14027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404027, 'My', 304027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14027, 4027, 14027, 14027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 4)
    # Central joint node
    ops.node(4028, 12.45, 30.9, 12.25, '-mass', 6.886072884811414, 6.886072884811414, 6.886072884811414, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 12.325, 30.9, 12.25)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 12.45, 30.9, 12.05)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(64028, 12.45, 30.725, 12.25)
    ops.element('elasticBeamColumn', 64028, 64028, 4028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304028, 29296.10465)
    ops.uniaxialMaterial('Elastic', 404028, 22122.24195)
    ops.section('Aggregator', 14028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404028, 'My', 304028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14028, 4028, 14028, 14028, '-orient', 0, 0, 1, 0, 1, 0)
