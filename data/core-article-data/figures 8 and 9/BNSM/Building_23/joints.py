import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 0.5)
    # Central joint node
    ops.node(4029, 0.0, 0.0, 1.85, '-mass', 3.2467826197757397, 3.2467826197757397, 3.2467826197757397, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34029, 0.125, 0.0, 1.85)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 0.0, 0.0, 1.65)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(74029, 0.0, 0.0, 2.05)
    ops.element('elasticBeamColumn', 74029, 4029, 74029, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 0.5)
    # Central joint node
    ops.node(4030, 2.95, 0.0, 1.85, '-mass', 3.5183422528032624, 3.5183422528032624, 3.5183422528032624, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 2.775, 0.0, 1.85)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(24030, 2.95, 0.0, 1.65)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(74030, 2.95, 0.0, 2.05)
    ops.element('elasticBeamColumn', 74030, 4030, 74030, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 1.5)
    # Central joint node
    ops.node(4031, 0.0, 0.0, 5.25, '-mass', 3.0926541794087665, 3.0926541794087665, 3.0926541794087665, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34031, 0.125, 0.0, 5.25)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 0.0, 0.0, 5.075)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(74031, 0.0, 0.0, 5.425)
    ops.element('elasticBeamColumn', 74031, 4031, 74031, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    # Central joint node
    ops.node(4032, 2.95, 0.0, 5.25, '-mass', 3.3201771151885833, 3.3201771151885833, 3.3201771151885833, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 2.775, 0.0, 5.25)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 2.95, 0.0, 5.075)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(74032, 2.95, 0.0, 5.425)
    ops.element('elasticBeamColumn', 74032, 4032, 74032, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 2.5)
    # Central joint node
    ops.node(4033, 0.0, 0.0, 8.35, '-mass', 3.0926541794087665, 3.0926541794087665, 3.0926541794087665, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34033, 0.125, 0.0, 8.35)
    ops.element('elasticBeamColumn', 34033, 4033, 34033, 99999, 88888)
    ops.node(24033, 0.0, 0.0, 8.175)
    ops.element('elasticBeamColumn', 24033, 24033, 4033, 99999, 99999)
    ops.node(74033, 0.0, 0.0, 8.525)
    ops.element('elasticBeamColumn', 74033, 4033, 74033, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    # Central joint node
    ops.node(4034, 2.95, 0.0, 8.35, '-mass', 3.0926541794087665, 3.0926541794087665, 3.0926541794087665, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54034, 2.825, 0.0, 8.35)
    ops.element('elasticBeamColumn', 54034, 54034, 4034, 99999, 88888)
    ops.node(24034, 2.95, 0.0, 8.175)
    ops.element('elasticBeamColumn', 24034, 24034, 4034, 99999, 99999)
    ops.node(74034, 2.95, 0.0, 8.525)
    ops.element('elasticBeamColumn', 74034, 4034, 74034, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 3.5)
    # Central joint node
    ops.node(4035, 0.0, 0.0, 11.45, '-mass', 3.0926541794087665, 3.0926541794087665, 3.0926541794087665, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34035, 0.125, 0.0, 11.45)
    ops.element('elasticBeamColumn', 34035, 4035, 34035, 99999, 88888)
    ops.node(24035, 0.0, 0.0, 11.275)
    ops.element('elasticBeamColumn', 24035, 24035, 4035, 99999, 99999)
    ops.node(74035, 0.0, 0.0, 11.625)
    ops.element('elasticBeamColumn', 74035, 4035, 74035, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 3.5)
    # Central joint node
    ops.node(4036, 2.95, 0.0, 11.45, '-mass', 3.0926541794087665, 3.0926541794087665, 3.0926541794087665, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54036, 2.825, 0.0, 11.45)
    ops.element('elasticBeamColumn', 54036, 54036, 4036, 99999, 88888)
    ops.node(24036, 2.95, 0.0, 11.275)
    ops.element('elasticBeamColumn', 24036, 24036, 4036, 99999, 99999)
    ops.node(74036, 2.95, 0.0, 11.625)
    ops.element('elasticBeamColumn', 74036, 4036, 74036, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.7, '-mass', 2.9023955147808356, 2.9023955147808356, 2.9023955147808356, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.125, 0.0, 3.7)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 3.45)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.95)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.125, 3.7)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 36110.44375)
    ops.uniaxialMaterial('Elastic', 401001, 37940.10695)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 2.95, 0.0, 3.7, '-mass', 9.198652956811042, 9.198652956811042, 9.198652956811042, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 2.775, 0.0, 3.7)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 3.125, 0.0, 3.7)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 2.95, 0.0, 3.45)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 2.95, 0.0, 3.95)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 2.95, 0.175, 3.7)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 55719.8957)
    ops.uniaxialMaterial('Elastic', 401002, 104855.30235)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 8.3, 0.0, 3.7, '-mass', 13.658264119534415, 13.658264119534415, 13.658264119534415, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 8.125, 0.0, 3.7)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 8.475, 0.0, 3.7)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 8.3, 0.0, 3.45)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 8.3, 0.0, 3.95)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 8.3, 0.175, 3.7)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 52207.05025)
    ops.uniaxialMaterial('Elastic', 401003, 94780.2376)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 13.65, 0.0, 3.7, '-mass', 8.79253674885997, 8.79253674885997, 8.79253674885997, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 13.5, 0.0, 3.7)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 13.65, 0.0, 3.45)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 13.65, 0.0, 3.95)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 13.65, 0.15, 3.7)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 34899.09875)
    ops.uniaxialMaterial('Elastic', 401004, 45754.4832)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 4.25, 3.7, '-mass', 9.296682512134613, 9.296682512134613, 9.296682512134613, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.15, 4.25, 3.7)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 4.25, 3.4)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 4.25, 4.0)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 4.1, 3.7)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 4.4, 3.7)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 61310.79015)
    ops.uniaxialMaterial('Elastic', 401005, 63287.2733)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 2.95, 4.25, 3.7, '-mass', 15.541287100578304, 15.541287100578304, 15.541287100578304, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 2.775, 4.25, 3.7)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 3.125, 4.25, 3.7)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 2.95, 4.25, 3.4)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 2.95, 4.25, 4.0)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 2.95, 4.075, 3.7)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 2.95, 4.425, 3.7)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 80524.7422)
    ops.uniaxialMaterial('Elastic', 401006, 128272.7722)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 8.3, 4.25, 3.7, '-mass', 17.403786139170766, 17.403786139170766, 17.403786139170766, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 8.1, 4.25, 3.7)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 8.5, 4.25, 3.7)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 8.3, 4.25, 3.4)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 8.3, 4.25, 4.0)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 8.3, 4.05, 3.7)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 8.3, 4.45, 3.7)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 97851.96655)
    ops.uniaxialMaterial('Elastic', 401007, 155874.36445)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 13.65, 4.25, 3.7, '-mass', 12.503931805569069, 12.503931805569069, 12.503931805569069, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 13.475, 4.25, 3.7)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 13.65, 4.25, 3.4)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 13.65, 4.25, 4.0)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 13.65, 4.075, 3.7)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 13.65, 4.425, 3.7)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 71711.4758)
    ops.uniaxialMaterial('Elastic', 401008, 83456.406)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 8.5, 3.7, '-mass', 8.839249326002152, 8.839249326002152, 8.839249326002152, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.15, 8.5, 3.7)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 8.5, 3.4)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 8.5, 4.0)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 8.35, 3.7)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 8.65, 3.7)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 56186.04835)
    ops.uniaxialMaterial('Elastic', 401009, 58458.0901)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 2.95, 8.5, 3.7, '-mass', 13.567544026576321, 13.567544026576321, 13.567544026576321, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 2.775, 8.5, 3.7)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 3.125, 8.5, 3.7)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 2.95, 8.5, 3.4)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 2.95, 8.5, 4.0)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 2.95, 8.325, 3.7)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 2.95, 8.675, 3.7)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 75134.25465)
    ops.uniaxialMaterial('Elastic', 401010, 119685.93585)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 8.3, 8.5, 3.7, '-mass', 17.403786139170766, 17.403786139170766, 17.403786139170766, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 8.1, 8.5, 3.7)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 8.5, 8.5, 3.7)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 8.3, 8.5, 3.4)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 8.3, 8.5, 4.0)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 8.3, 8.3, 3.7)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 8.3, 8.7, 3.7)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 97851.96655)
    ops.uniaxialMaterial('Elastic', 401011, 155874.36445)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 13.65, 8.5, 3.7, '-mass', 12.503931805569069, 12.503931805569069, 12.503931805569069, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 13.475, 8.5, 3.7)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 13.65, 8.5, 3.4)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 13.65, 8.5, 4.0)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 13.65, 8.325, 3.7)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 13.65, 8.675, 3.7)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 71711.4758)
    ops.uniaxialMaterial('Elastic', 401012, 83456.406)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1013, 0.0, 12.75, 3.7, '-mass', 8.839249326002152, 8.839249326002152, 8.839249326002152, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.15, 12.75, 3.7)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 12.75, 3.4)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 12.75, 4.0)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 12.6, 3.7)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 12.9, 3.7)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301013, 56186.04835)
    ops.uniaxialMaterial('Elastic', 401013, 58458.0901)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1014, 2.95, 12.75, 3.7, '-mass', 13.567544026576321, 13.567544026576321, 13.567544026576321, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 2.775, 12.75, 3.7)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 3.125, 12.75, 3.7)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 2.95, 12.75, 3.4)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 2.95, 12.75, 4.0)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 2.95, 12.575, 3.7)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 2.95, 12.925, 3.7)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301014, 75134.25465)
    ops.uniaxialMaterial('Elastic', 401014, 119685.93585)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1015, 8.3, 12.75, 3.7, '-mass', 17.403786139170766, 17.403786139170766, 17.403786139170766, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 8.1, 12.75, 3.7)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 8.5, 12.75, 3.7)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 8.3, 12.75, 3.4)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 8.3, 12.75, 4.0)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 8.3, 12.55, 3.7)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 8.3, 12.95, 3.7)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301015, 97851.96655)
    ops.uniaxialMaterial('Elastic', 401015, 155874.36445)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1016, 13.65, 12.75, 3.7, '-mass', 12.503931805569069, 12.503931805569069, 12.503931805569069, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 13.475, 12.75, 3.7)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 13.65, 12.75, 3.4)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 13.65, 12.75, 4.0)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 13.65, 12.575, 3.7)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 13.65, 12.925, 3.7)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301016, 71711.4758)
    ops.uniaxialMaterial('Elastic', 401016, 83456.406)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 1)
    # Central joint node
    ops.node(1017, 0.0, 17.0, 3.7, '-mass', 8.839249326002152, 8.839249326002152, 8.839249326002152, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31017, 0.15, 17.0, 3.7)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 0.0, 17.0, 3.4)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 0.0, 17.0, 4.0)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 0.0, 16.85, 3.7)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 0.0, 17.15, 3.7)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301017, 56186.04835)
    ops.uniaxialMaterial('Elastic', 401017, 58458.0901)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 1)
    # Central joint node
    ops.node(1018, 2.95, 17.0, 3.7, '-mass', 13.567544026576321, 13.567544026576321, 13.567544026576321, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 2.775, 17.0, 3.7)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(31018, 3.125, 17.0, 3.7)
    ops.element('elasticBeamColumn', 31018, 1018, 31018, 99999, 88888)
    ops.node(21018, 2.95, 17.0, 3.4)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 2.95, 17.0, 4.0)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 2.95, 16.825, 3.7)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 2.95, 17.175, 3.7)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301018, 75134.25465)
    ops.uniaxialMaterial('Elastic', 401018, 119685.93585)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 1)
    # Central joint node
    ops.node(1019, 8.3, 17.0, 3.7, '-mass', 17.403786139170766, 17.403786139170766, 17.403786139170766, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51019, 8.1, 17.0, 3.7)
    ops.element('elasticBeamColumn', 51019, 51019, 1019, 99999, 88888)
    ops.node(31019, 8.5, 17.0, 3.7)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 8.3, 17.0, 3.4)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 8.3, 17.0, 4.0)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 8.3, 16.8, 3.7)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    ops.node(41019, 8.3, 17.2, 3.7)
    ops.element('elasticBeamColumn', 41019, 1019, 41019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301019, 97851.96655)
    ops.uniaxialMaterial('Elastic', 401019, 155874.36445)
    ops.section('Aggregator', 11019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401019, 'My', 301019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11019, 1019, 11019, 11019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 1)
    # Central joint node
    ops.node(1020, 13.65, 17.0, 3.7, '-mass', 12.503931805569069, 12.503931805569069, 12.503931805569069, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 13.475, 17.0, 3.7)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(21020, 13.65, 17.0, 3.4)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 13.65, 17.0, 4.0)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 13.65, 16.825, 3.7)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    ops.node(41020, 13.65, 17.175, 3.7)
    ops.element('elasticBeamColumn', 41020, 1020, 41020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301020, 71711.4758)
    ops.uniaxialMaterial('Elastic', 401020, 83456.406)
    ops.section('Aggregator', 11020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401020, 'My', 301020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11020, 1020, 11020, 11020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 1)
    # Central joint node
    ops.node(1021, 0.0, 21.25, 3.7, '-mass', 8.839249326002152, 8.839249326002152, 8.839249326002152, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31021, 0.15, 21.25, 3.7)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 0.0, 21.25, 3.4)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 0.0, 21.25, 4.0)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 0.0, 21.1, 3.7)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    ops.node(41021, 0.0, 21.4, 3.7)
    ops.element('elasticBeamColumn', 41021, 1021, 41021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301021, 56186.04835)
    ops.uniaxialMaterial('Elastic', 401021, 58458.0901)
    ops.section('Aggregator', 11021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401021, 'My', 301021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11021, 1021, 11021, 11021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 1)
    # Central joint node
    ops.node(1022, 2.95, 21.25, 3.7, '-mass', 13.567544026576321, 13.567544026576321, 13.567544026576321, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 2.775, 21.25, 3.7)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 3.125, 21.25, 3.7)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 2.95, 21.25, 3.4)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 2.95, 21.25, 4.0)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 2.95, 21.075, 3.7)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    ops.node(41022, 2.95, 21.425, 3.7)
    ops.element('elasticBeamColumn', 41022, 1022, 41022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301022, 75134.25465)
    ops.uniaxialMaterial('Elastic', 401022, 119685.93585)
    ops.section('Aggregator', 11022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401022, 'My', 301022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11022, 1022, 11022, 11022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 1)
    # Central joint node
    ops.node(1023, 8.3, 21.25, 3.7, '-mass', 17.403786139170766, 17.403786139170766, 17.403786139170766, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 8.1, 21.25, 3.7)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 8.5, 21.25, 3.7)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 8.3, 21.25, 3.4)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 8.3, 21.25, 4.0)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 8.3, 21.05, 3.7)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    ops.node(41023, 8.3, 21.45, 3.7)
    ops.element('elasticBeamColumn', 41023, 1023, 41023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301023, 97851.96655)
    ops.uniaxialMaterial('Elastic', 401023, 155874.36445)
    ops.section('Aggregator', 11023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401023, 'My', 301023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11023, 1023, 11023, 11023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 1)
    # Central joint node
    ops.node(1024, 13.65, 21.25, 3.7, '-mass', 12.503931805569069, 12.503931805569069, 12.503931805569069, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 13.475, 21.25, 3.7)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 13.65, 21.25, 3.4)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 13.65, 21.25, 4.0)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 13.65, 21.075, 3.7)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    ops.node(41024, 13.65, 21.425, 3.7)
    ops.element('elasticBeamColumn', 41024, 1024, 41024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301024, 71711.4758)
    ops.uniaxialMaterial('Elastic', 401024, 83456.406)
    ops.section('Aggregator', 11024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401024, 'My', 301024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11024, 1024, 11024, 11024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 1)
    # Central joint node
    ops.node(1025, 0.0, 25.5, 3.7, '-mass', 5.83420162528446, 5.83420162528446, 5.83420162528446, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31025, 0.125, 25.5, 3.7)
    ops.element('elasticBeamColumn', 31025, 1025, 31025, 99999, 88888)
    ops.node(21025, 0.0, 25.5, 3.45)
    ops.element('elasticBeamColumn', 21025, 21025, 1025, 99999, 99999)
    ops.node(71025, 0.0, 25.5, 3.95)
    ops.element('elasticBeamColumn', 71025, 1025, 71025, 99999, 99999)
    ops.node(61025, 0.0, 25.375, 3.7)
    ops.element('elasticBeamColumn', 61025, 61025, 1025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301025, 30022.14165)
    ops.uniaxialMaterial('Elastic', 401025, 30922.76365)
    ops.section('Aggregator', 11025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401025, 'My', 301025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11025, 1025, 11025, 11025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 1)
    # Central joint node
    ops.node(1026, 2.95, 25.5, 3.7, '-mass', 10.593354072411508, 10.593354072411508, 10.593354072411508, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51026, 2.8, 25.5, 3.7)
    ops.element('elasticBeamColumn', 51026, 51026, 1026, 99999, 88888)
    ops.node(31026, 3.1, 25.5, 3.7)
    ops.element('elasticBeamColumn', 31026, 1026, 31026, 99999, 88888)
    ops.node(21026, 2.95, 25.5, 3.45)
    ops.element('elasticBeamColumn', 21026, 21026, 1026, 99999, 99999)
    ops.node(71026, 2.95, 25.5, 3.95)
    ops.element('elasticBeamColumn', 71026, 1026, 71026, 99999, 99999)
    ops.node(61026, 2.95, 25.35, 3.7)
    ops.element('elasticBeamColumn', 61026, 61026, 1026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301026, 39705.5206)
    ops.uniaxialMaterial('Elastic', 401026, 71522.5916)
    ops.section('Aggregator', 11026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401026, 'My', 301026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11026, 1026, 11026, 11026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 1)
    # Central joint node
    ops.node(1027, 8.3, 25.5, 3.7, '-mass', 13.658264119534415, 13.658264119534415, 13.658264119534415, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51027, 8.125, 25.5, 3.7)
    ops.element('elasticBeamColumn', 51027, 51027, 1027, 99999, 88888)
    ops.node(31027, 8.475, 25.5, 3.7)
    ops.element('elasticBeamColumn', 31027, 1027, 31027, 99999, 88888)
    ops.node(21027, 8.3, 25.5, 3.45)
    ops.element('elasticBeamColumn', 21027, 21027, 1027, 99999, 99999)
    ops.node(71027, 8.3, 25.5, 3.95)
    ops.element('elasticBeamColumn', 71027, 1027, 71027, 99999, 99999)
    ops.node(61027, 8.3, 25.325, 3.7)
    ops.element('elasticBeamColumn', 61027, 61027, 1027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301027, 52207.05025)
    ops.uniaxialMaterial('Elastic', 401027, 94780.2376)
    ops.section('Aggregator', 11027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401027, 'My', 301027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11027, 1027, 11027, 11027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 1)
    # Central joint node
    ops.node(1028, 13.65, 25.5, 3.7, '-mass', 8.79253674885997, 8.79253674885997, 8.79253674885997, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51028, 13.5, 25.5, 3.7)
    ops.element('elasticBeamColumn', 51028, 51028, 1028, 99999, 88888)
    ops.node(21028, 13.65, 25.5, 3.45)
    ops.element('elasticBeamColumn', 21028, 21028, 1028, 99999, 99999)
    ops.node(71028, 13.65, 25.5, 3.95)
    ops.element('elasticBeamColumn', 71028, 1028, 71028, 99999, 99999)
    ops.node(61028, 13.65, 25.35, 3.7)
    ops.element('elasticBeamColumn', 61028, 61028, 1028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301028, 34899.09875)
    ops.uniaxialMaterial('Elastic', 401028, 45754.4832)
    ops.section('Aggregator', 11028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401028, 'My', 301028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11028, 1028, 11028, 11028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 6.8, '-mass', 2.8144750254842, 2.8144750254842, 2.8144750254842, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.125, 0.0, 6.8)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 6.55)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 7.05)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.125, 6.8)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 26211.59565)
    ops.uniaxialMaterial('Elastic', 402001, 32492.79305)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 2.95, 0.0, 6.8, '-mass', 8.935961825312571, 8.935961825312571, 8.935961825312571, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 2.775, 0.0, 6.8)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 3.125, 0.0, 6.8)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 2.95, 0.0, 6.55)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 2.95, 0.0, 7.05)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 2.95, 0.175, 6.8)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 47474.46605)
    ops.uniaxialMaterial('Elastic', 402002, 88587.25275)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 8.3, 0.0, 6.8, '-mass', 13.23685739170567, 13.23685739170567, 13.23685739170567, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 8.125, 0.0, 6.8)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 8.475, 0.0, 6.8)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 8.3, 0.0, 6.55)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 8.3, 0.0, 7.05)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 8.3, 0.175, 6.8)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 32075.5845)
    ops.uniaxialMaterial('Elastic', 402003, 80600.70615)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 13.65, 0.0, 6.8, '-mass', 8.570212589838563, 8.570212589838563, 8.570212589838563, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 13.5, 0.0, 6.8)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 13.65, 0.0, 6.55)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 13.65, 0.0, 7.05)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 13.65, 0.15, 6.8)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 25551.9714)
    ops.uniaxialMaterial('Elastic', 402004, 39388.24)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 4.25, 6.8, '-mass', 8.996376701737061, 8.996376701737061, 8.996376701737061, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.15, 4.25, 6.8)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 4.25, 6.5)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 4.25, 7.1)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 4.1, 6.8)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 4.4, 6.8)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 46164.41585)
    ops.uniaxialMaterial('Elastic', 402005, 55176.2024)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 2.95, 4.25, 6.8, '-mass', 15.015904837581363, 15.015904837581363, 15.015904837581363, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 2.775, 4.25, 6.8)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 3.125, 4.25, 6.8)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 2.95, 4.25, 6.5)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 2.95, 4.25, 7.1)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 2.95, 4.075, 6.8)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 2.95, 4.425, 6.8)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 69204.19655)
    ops.uniaxialMaterial('Elastic', 402006, 110239.5847)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 8.3, 4.25, 6.8, '-mass', 16.936202041311436, 16.936202041311436, 16.936202041311436, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 8.1, 4.25, 6.8)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 8.5, 4.25, 6.8)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 8.3, 4.25, 6.5)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 8.3, 4.25, 7.1)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 8.3, 4.05, 6.8)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 8.3, 4.45, 6.8)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 61120.31185)
    ops.uniaxialMaterial('Elastic', 402007, 133604.2318)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 13.65, 4.25, 6.8, '-mass', 12.082525077740327, 12.082525077740327, 12.082525077740327, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 13.475, 4.25, 6.8)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 13.65, 4.25, 6.5)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 13.65, 4.25, 7.1)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 13.65, 4.075, 6.8)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 13.65, 4.425, 6.8)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 52648.94895)
    ops.uniaxialMaterial('Elastic', 402008, 71965.4524)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 8.5, 6.8, '-mass', 8.5389435156046, 8.5389435156046, 8.5389435156046, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.15, 8.5, 6.8)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 8.5, 6.5)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 8.5, 7.1)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 8.35, 6.8)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 8.65, 6.8)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 41782.49295)
    ops.uniaxialMaterial('Elastic', 402009, 50460.2844)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 2.95, 8.5, 6.8, '-mass', 13.042161763579383, 13.042161763579383, 13.042161763579383, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 2.775, 8.5, 6.8)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 3.125, 8.5, 6.8)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 2.95, 8.5, 6.5)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 2.95, 8.5, 7.1)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 2.95, 8.325, 6.8)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 2.95, 8.675, 6.8)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 64281.81215)
    ops.uniaxialMaterial('Elastic', 402010, 102398.41845)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 8.3, 8.5, 6.8, '-mass', 16.936202041311436, 16.936202041311436, 16.936202041311436, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 8.1, 8.5, 6.8)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 8.5, 8.5, 6.8)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 8.3, 8.5, 6.5)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 8.3, 8.5, 7.1)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 8.3, 8.3, 6.8)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 8.3, 8.7, 6.8)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 61120.31185)
    ops.uniaxialMaterial('Elastic', 402011, 133604.2318)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 13.65, 8.5, 6.8, '-mass', 12.082525077740327, 12.082525077740327, 12.082525077740327, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 13.475, 8.5, 6.8)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 13.65, 8.5, 6.5)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 13.65, 8.5, 7.1)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 13.65, 8.325, 6.8)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 13.65, 8.675, 6.8)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 52648.94895)
    ops.uniaxialMaterial('Elastic', 402012, 71965.4524)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2013, 0.0, 12.75, 6.8, '-mass', 8.5389435156046, 8.5389435156046, 8.5389435156046, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.15, 12.75, 6.8)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 12.75, 6.5)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 12.75, 7.1)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 12.6, 6.8)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 12.9, 6.8)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302013, 41782.49295)
    ops.uniaxialMaterial('Elastic', 402013, 50460.2844)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2014, 2.95, 12.75, 6.8, '-mass', 13.042161763579383, 13.042161763579383, 13.042161763579383, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 2.775, 12.75, 6.8)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 3.125, 12.75, 6.8)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 2.95, 12.75, 6.5)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 2.95, 12.75, 7.1)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 2.95, 12.575, 6.8)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 2.95, 12.925, 6.8)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302014, 64281.81215)
    ops.uniaxialMaterial('Elastic', 402014, 102398.41845)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2015, 8.3, 12.75, 6.8, '-mass', 16.936202041311436, 16.936202041311436, 16.936202041311436, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 8.1, 12.75, 6.8)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 8.5, 12.75, 6.8)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 8.3, 12.75, 6.5)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 8.3, 12.75, 7.1)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 8.3, 12.55, 6.8)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 8.3, 12.95, 6.8)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302015, 61120.31185)
    ops.uniaxialMaterial('Elastic', 402015, 133604.2318)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2016, 13.65, 12.75, 6.8, '-mass', 12.082525077740327, 12.082525077740327, 12.082525077740327, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 13.475, 12.75, 6.8)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 13.65, 12.75, 6.5)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 13.65, 12.75, 7.1)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 13.65, 12.575, 6.8)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 13.65, 12.925, 6.8)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302016, 52648.94895)
    ops.uniaxialMaterial('Elastic', 402016, 71965.4524)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 2)
    # Central joint node
    ops.node(2017, 0.0, 17.0, 6.8, '-mass', 8.5389435156046, 8.5389435156046, 8.5389435156046, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32017, 0.15, 17.0, 6.8)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 0.0, 17.0, 6.5)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 0.0, 17.0, 7.1)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 0.0, 16.85, 6.8)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 0.0, 17.15, 6.8)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302017, 41782.49295)
    ops.uniaxialMaterial('Elastic', 402017, 50460.2844)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 2)
    # Central joint node
    ops.node(2018, 2.95, 17.0, 6.8, '-mass', 13.042161763579383, 13.042161763579383, 13.042161763579383, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 2.775, 17.0, 6.8)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(32018, 3.125, 17.0, 6.8)
    ops.element('elasticBeamColumn', 32018, 2018, 32018, 99999, 88888)
    ops.node(22018, 2.95, 17.0, 6.5)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 2.95, 17.0, 7.1)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 2.95, 16.825, 6.8)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 2.95, 17.175, 6.8)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302018, 64281.81215)
    ops.uniaxialMaterial('Elastic', 402018, 102398.41845)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 2)
    # Central joint node
    ops.node(2019, 8.3, 17.0, 6.8, '-mass', 16.936202041311436, 16.936202041311436, 16.936202041311436, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52019, 8.1, 17.0, 6.8)
    ops.element('elasticBeamColumn', 52019, 52019, 2019, 99999, 88888)
    ops.node(32019, 8.5, 17.0, 6.8)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 8.3, 17.0, 6.5)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 8.3, 17.0, 7.1)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 8.3, 16.8, 6.8)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    ops.node(42019, 8.3, 17.2, 6.8)
    ops.element('elasticBeamColumn', 42019, 2019, 42019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302019, 61120.31185)
    ops.uniaxialMaterial('Elastic', 402019, 133604.2318)
    ops.section('Aggregator', 12019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402019, 'My', 302019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12019, 2019, 12019, 12019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 2)
    # Central joint node
    ops.node(2020, 13.65, 17.0, 6.8, '-mass', 12.082525077740327, 12.082525077740327, 12.082525077740327, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 13.475, 17.0, 6.8)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(22020, 13.65, 17.0, 6.5)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 13.65, 17.0, 7.1)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 13.65, 16.825, 6.8)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    ops.node(42020, 13.65, 17.175, 6.8)
    ops.element('elasticBeamColumn', 42020, 2020, 42020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302020, 52648.94895)
    ops.uniaxialMaterial('Elastic', 402020, 71965.4524)
    ops.section('Aggregator', 12020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402020, 'My', 302020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12020, 2020, 12020, 12020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 2)
    # Central joint node
    ops.node(2021, 0.0, 21.25, 6.8, '-mass', 8.5389435156046, 8.5389435156046, 8.5389435156046, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32021, 0.15, 21.25, 6.8)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 0.0, 21.25, 6.5)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 0.0, 21.25, 7.1)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 0.0, 21.1, 6.8)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    ops.node(42021, 0.0, 21.4, 6.8)
    ops.element('elasticBeamColumn', 42021, 2021, 42021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302021, 41782.49295)
    ops.uniaxialMaterial('Elastic', 402021, 50460.2844)
    ops.section('Aggregator', 12021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402021, 'My', 302021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12021, 2021, 12021, 12021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 2)
    # Central joint node
    ops.node(2022, 2.95, 21.25, 6.8, '-mass', 13.042161763579383, 13.042161763579383, 13.042161763579383, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 2.775, 21.25, 6.8)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 3.125, 21.25, 6.8)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 2.95, 21.25, 6.5)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 2.95, 21.25, 7.1)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 2.95, 21.075, 6.8)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    ops.node(42022, 2.95, 21.425, 6.8)
    ops.element('elasticBeamColumn', 42022, 2022, 42022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302022, 64281.81215)
    ops.uniaxialMaterial('Elastic', 402022, 102398.41845)
    ops.section('Aggregator', 12022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402022, 'My', 302022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12022, 2022, 12022, 12022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 2)
    # Central joint node
    ops.node(2023, 8.3, 21.25, 6.8, '-mass', 16.936202041311436, 16.936202041311436, 16.936202041311436, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 8.1, 21.25, 6.8)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 8.5, 21.25, 6.8)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 8.3, 21.25, 6.5)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 8.3, 21.25, 7.1)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 8.3, 21.05, 6.8)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    ops.node(42023, 8.3, 21.45, 6.8)
    ops.element('elasticBeamColumn', 42023, 2023, 42023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302023, 61120.31185)
    ops.uniaxialMaterial('Elastic', 402023, 133604.2318)
    ops.section('Aggregator', 12023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402023, 'My', 302023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12023, 2023, 12023, 12023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 2)
    # Central joint node
    ops.node(2024, 13.65, 21.25, 6.8, '-mass', 12.082525077740327, 12.082525077740327, 12.082525077740327, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 13.475, 21.25, 6.8)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 13.65, 21.25, 6.5)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 13.65, 21.25, 7.1)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 13.65, 21.075, 6.8)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    ops.node(42024, 13.65, 21.425, 6.8)
    ops.element('elasticBeamColumn', 42024, 2024, 42024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302024, 52648.94895)
    ops.uniaxialMaterial('Elastic', 402024, 71965.4524)
    ops.section('Aggregator', 12024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402024, 'My', 302024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12024, 2024, 12024, 12024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 2)
    # Central joint node
    ops.node(2025, 0.0, 25.5, 6.8, '-mass', 5.72334535617131, 5.72334535617131, 5.72334535617131, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32025, 0.125, 25.5, 6.8)
    ops.element('elasticBeamColumn', 32025, 2025, 32025, 99999, 88888)
    ops.node(22025, 0.0, 25.5, 6.55)
    ops.element('elasticBeamColumn', 22025, 22025, 2025, 99999, 99999)
    ops.node(72025, 0.0, 25.5, 7.05)
    ops.element('elasticBeamColumn', 72025, 2025, 72025, 99999, 99999)
    ops.node(62025, 0.0, 25.375, 6.8)
    ops.element('elasticBeamColumn', 62025, 62025, 2025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302025, 22383.8533)
    ops.uniaxialMaterial('Elastic', 402025, 26706.84105)
    ops.section('Aggregator', 12025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402025, 'My', 302025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12025, 2025, 12025, 12025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 2)
    # Central joint node
    ops.node(2026, 2.95, 25.5, 6.8, '-mass', 10.319042145806005, 10.319042145806005, 10.319042145806005, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52026, 2.8, 25.5, 6.8)
    ops.element('elasticBeamColumn', 52026, 52026, 2026, 99999, 88888)
    ops.node(32026, 3.1, 25.5, 6.8)
    ops.element('elasticBeamColumn', 32026, 2026, 32026, 99999, 88888)
    ops.node(22026, 2.95, 25.5, 6.55)
    ops.element('elasticBeamColumn', 22026, 22026, 2026, 99999, 99999)
    ops.node(72026, 2.95, 25.5, 7.05)
    ops.element('elasticBeamColumn', 72026, 2026, 72026, 99999, 99999)
    ops.node(62026, 2.95, 25.35, 6.8)
    ops.element('elasticBeamColumn', 62026, 62026, 2026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302026, 34069.66445)
    ops.uniaxialMaterial('Elastic', 402026, 60809.1458)
    ops.section('Aggregator', 12026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402026, 'My', 302026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12026, 2026, 12026, 12026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 2)
    # Central joint node
    ops.node(2027, 8.3, 25.5, 6.8, '-mass', 13.23685739170567, 13.23685739170567, 13.23685739170567, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52027, 8.125, 25.5, 6.8)
    ops.element('elasticBeamColumn', 52027, 52027, 2027, 99999, 88888)
    ops.node(32027, 8.475, 25.5, 6.8)
    ops.element('elasticBeamColumn', 32027, 2027, 32027, 99999, 88888)
    ops.node(22027, 8.3, 25.5, 6.55)
    ops.element('elasticBeamColumn', 22027, 22027, 2027, 99999, 99999)
    ops.node(72027, 8.3, 25.5, 7.05)
    ops.element('elasticBeamColumn', 72027, 2027, 72027, 99999, 99999)
    ops.node(62027, 8.3, 25.325, 6.8)
    ops.element('elasticBeamColumn', 62027, 62027, 2027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302027, 32075.5845)
    ops.uniaxialMaterial('Elastic', 402027, 80600.70615)
    ops.section('Aggregator', 12027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402027, 'My', 302027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12027, 2027, 12027, 12027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 2)
    # Central joint node
    ops.node(2028, 13.65, 25.5, 6.8, '-mass', 8.570212589838563, 8.570212589838563, 8.570212589838563, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52028, 13.5, 25.5, 6.8)
    ops.element('elasticBeamColumn', 52028, 52028, 2028, 99999, 88888)
    ops.node(22028, 13.65, 25.5, 6.55)
    ops.element('elasticBeamColumn', 22028, 22028, 2028, 99999, 99999)
    ops.node(72028, 13.65, 25.5, 7.05)
    ops.element('elasticBeamColumn', 72028, 2028, 72028, 99999, 99999)
    ops.node(62028, 13.65, 25.35, 6.8)
    ops.element('elasticBeamColumn', 62028, 62028, 2028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302028, 25551.9714)
    ops.uniaxialMaterial('Elastic', 402028, 39388.24)
    ops.section('Aggregator', 12028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402028, 'My', 302028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12028, 2028, 12028, 12028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 9.9, '-mass', 2.8144750254842, 2.8144750254842, 2.8144750254842, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 9.9)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 9.65)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 10.15)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 9.9)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 20101.1017)
    ops.uniaxialMaterial('Elastic', 403001, 25029.60855)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 2.95, 0.0, 9.9, '-mass', 8.770212589838565, 8.770212589838565, 8.770212589838565, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 2.825, 0.0, 9.9)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 3.075, 0.0, 9.9)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 2.95, 0.0, 9.65)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 2.95, 0.0, 10.15)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 2.95, 0.125, 9.9)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 24287.9631)
    ops.uniaxialMaterial('Elastic', 403002, 47835.72165)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 8.3, 0.0, 9.9, '-mass', 13.009334455925853, 13.009334455925853, 13.009334455925853, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 8.175, 0.0, 9.9)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 8.425, 0.0, 9.9)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 8.3, 0.0, 9.65)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 8.3, 0.0, 10.15)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 8.3, 0.125, 9.9)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 20003.3198)
    ops.uniaxialMaterial('Elastic', 403003, 44883.41415)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 13.65, 0.0, 9.9, '-mass', 8.413943476688715, 8.413943476688715, 8.413943476688715, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 13.525, 0.0, 9.9)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 13.65, 0.0, 9.65)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 13.65, 0.0, 10.15)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 13.65, 0.125, 9.9)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 15606.14635)
    ops.uniaxialMaterial('Elastic', 403004, 26332.8072)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 4.25, 9.9, '-mass', 8.89209535617131, 8.89209535617131, 8.89209535617131, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.125, 4.25, 9.9)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 4.25, 9.6)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 4.25, 10.2)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 4.125, 9.9)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 4.375, 9.9)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 33919.72295)
    ops.uniaxialMaterial('Elastic', 403005, 37920.66765)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 2.95, 4.25, 9.9, '-mass', 14.684406366633354, 14.684406366633354, 14.684406366633354, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 2.825, 4.25, 9.9)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 3.075, 4.25, 9.9)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 2.95, 4.25, 9.6)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 2.95, 4.25, 10.2)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 2.95, 4.125, 9.9)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 2.95, 4.375, 9.9)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 37413.45415)
    ops.uniaxialMaterial('Elastic', 403006, 62967.90015)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 8.3, 4.25, 9.9, '-mass', 16.794000206449052, 16.794000206449052, 16.794000206449052, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 8.125, 4.25, 9.9)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 8.475, 4.25, 9.9)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 8.3, 4.25, 9.6)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 8.3, 4.25, 10.2)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 8.3, 4.075, 9.9)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 8.3, 4.425, 9.9)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 42695.276)
    ops.uniaxialMaterial('Elastic', 403007, 93328.5413)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 13.65, 4.25, 9.9, '-mass', 11.751026606792315, 11.751026606792315, 11.751026606792315, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 13.525, 4.25, 9.9)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 13.65, 4.25, 9.6)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 13.65, 4.25, 10.2)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 13.65, 4.125, 9.9)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 13.65, 4.375, 9.9)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 27260.85425)
    ops.uniaxialMaterial('Elastic', 403008, 41347.51735)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 8.5, 9.9, '-mass', 8.43466217003885, 8.43466217003885, 8.43466217003885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.125, 8.5, 9.9)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 8.5, 9.6)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 8.5, 10.2)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 8.375, 9.9)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 8.625, 9.9)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 29887.13115)
    ops.uniaxialMaterial('Elastic', 403009, 33958.3007)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 2.95, 8.5, 9.9, '-mass', 12.710663292631372, 12.710663292631372, 12.710663292631372, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 2.825, 8.5, 9.9)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 3.075, 8.5, 9.9)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 2.95, 8.5, 9.6)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 2.95, 8.5, 10.2)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 2.95, 8.375, 9.9)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 2.95, 8.625, 9.9)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 34401.161)
    ops.uniaxialMaterial('Elastic', 403010, 57878.46005)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 8.3, 8.5, 9.9, '-mass', 16.794000206449052, 16.794000206449052, 16.794000206449052, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 8.125, 8.5, 9.9)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 8.475, 8.5, 9.9)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 8.3, 8.5, 9.6)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 8.3, 8.5, 10.2)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 8.3, 8.325, 9.9)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 8.3, 8.675, 9.9)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 42695.276)
    ops.uniaxialMaterial('Elastic', 403011, 93328.5413)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 13.65, 8.5, 9.9, '-mass', 11.751026606792315, 11.751026606792315, 11.751026606792315, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 13.525, 8.5, 9.9)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 13.65, 8.5, 9.6)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 13.65, 8.5, 10.2)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 13.65, 8.375, 9.9)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 13.65, 8.625, 9.9)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 27260.85425)
    ops.uniaxialMaterial('Elastic', 403012, 41347.51735)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3013, 0.0, 12.75, 9.9, '-mass', 8.43466217003885, 8.43466217003885, 8.43466217003885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 12.75, 9.9)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 12.75, 9.6)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 12.75, 10.2)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 12.625, 9.9)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 12.875, 9.9)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303013, 29887.13115)
    ops.uniaxialMaterial('Elastic', 403013, 33958.3007)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3014, 2.95, 12.75, 9.9, '-mass', 12.710663292631372, 12.710663292631372, 12.710663292631372, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 2.825, 12.75, 9.9)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 3.075, 12.75, 9.9)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 2.95, 12.75, 9.6)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 2.95, 12.75, 10.2)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 2.95, 12.625, 9.9)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 2.95, 12.875, 9.9)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303014, 34401.161)
    ops.uniaxialMaterial('Elastic', 403014, 57878.46005)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3015, 8.3, 12.75, 9.9, '-mass', 16.794000206449052, 16.794000206449052, 16.794000206449052, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 8.125, 12.75, 9.9)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 8.475, 12.75, 9.9)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 8.3, 12.75, 9.6)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 8.3, 12.75, 10.2)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 8.3, 12.575, 9.9)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 8.3, 12.925, 9.9)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303015, 42695.276)
    ops.uniaxialMaterial('Elastic', 403015, 93328.5413)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3016, 13.65, 12.75, 9.9, '-mass', 11.751026606792315, 11.751026606792315, 11.751026606792315, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 13.525, 12.75, 9.9)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 13.65, 12.75, 9.6)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 13.65, 12.75, 10.2)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 13.65, 12.625, 9.9)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 13.65, 12.875, 9.9)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303016, 27260.85425)
    ops.uniaxialMaterial('Elastic', 403016, 41347.51735)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 3)
    # Central joint node
    ops.node(3017, 0.0, 17.0, 9.9, '-mass', 8.43466217003885, 8.43466217003885, 8.43466217003885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33017, 0.125, 17.0, 9.9)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 0.0, 17.0, 9.6)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 0.0, 17.0, 10.2)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 0.0, 16.875, 9.9)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 0.0, 17.125, 9.9)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303017, 29887.13115)
    ops.uniaxialMaterial('Elastic', 403017, 33958.3007)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 3)
    # Central joint node
    ops.node(3018, 2.95, 17.0, 9.9, '-mass', 12.710663292631372, 12.710663292631372, 12.710663292631372, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 2.825, 17.0, 9.9)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(33018, 3.075, 17.0, 9.9)
    ops.element('elasticBeamColumn', 33018, 3018, 33018, 99999, 88888)
    ops.node(23018, 2.95, 17.0, 9.6)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 2.95, 17.0, 10.2)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 2.95, 16.875, 9.9)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 2.95, 17.125, 9.9)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303018, 34401.161)
    ops.uniaxialMaterial('Elastic', 403018, 57878.46005)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 3)
    # Central joint node
    ops.node(3019, 8.3, 17.0, 9.9, '-mass', 16.794000206449052, 16.794000206449052, 16.794000206449052, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53019, 8.125, 17.0, 9.9)
    ops.element('elasticBeamColumn', 53019, 53019, 3019, 99999, 88888)
    ops.node(33019, 8.475, 17.0, 9.9)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 8.3, 17.0, 9.6)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 8.3, 17.0, 10.2)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 8.3, 16.825, 9.9)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    ops.node(43019, 8.3, 17.175, 9.9)
    ops.element('elasticBeamColumn', 43019, 3019, 43019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303019, 42695.276)
    ops.uniaxialMaterial('Elastic', 403019, 93328.5413)
    ops.section('Aggregator', 13019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403019, 'My', 303019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13019, 3019, 13019, 13019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 3)
    # Central joint node
    ops.node(3020, 13.65, 17.0, 9.9, '-mass', 11.751026606792315, 11.751026606792315, 11.751026606792315, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 13.525, 17.0, 9.9)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(23020, 13.65, 17.0, 9.6)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 13.65, 17.0, 10.2)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 13.65, 16.875, 9.9)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    ops.node(43020, 13.65, 17.125, 9.9)
    ops.element('elasticBeamColumn', 43020, 3020, 43020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303020, 27260.85425)
    ops.uniaxialMaterial('Elastic', 403020, 41347.51735)
    ops.section('Aggregator', 13020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403020, 'My', 303020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13020, 3020, 13020, 13020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 3)
    # Central joint node
    ops.node(3021, 0.0, 21.25, 9.9, '-mass', 8.43466217003885, 8.43466217003885, 8.43466217003885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33021, 0.125, 21.25, 9.9)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 0.0, 21.25, 9.6)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 0.0, 21.25, 10.2)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 0.0, 21.125, 9.9)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    ops.node(43021, 0.0, 21.375, 9.9)
    ops.element('elasticBeamColumn', 43021, 3021, 43021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303021, 29887.13115)
    ops.uniaxialMaterial('Elastic', 403021, 33958.3007)
    ops.section('Aggregator', 13021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403021, 'My', 303021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13021, 3021, 13021, 13021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 3)
    # Central joint node
    ops.node(3022, 2.95, 21.25, 9.9, '-mass', 12.710663292631372, 12.710663292631372, 12.710663292631372, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 2.825, 21.25, 9.9)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 3.075, 21.25, 9.9)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 2.95, 21.25, 9.6)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 2.95, 21.25, 10.2)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 2.95, 21.125, 9.9)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    ops.node(43022, 2.95, 21.375, 9.9)
    ops.element('elasticBeamColumn', 43022, 3022, 43022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303022, 34401.161)
    ops.uniaxialMaterial('Elastic', 403022, 57878.46005)
    ops.section('Aggregator', 13022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403022, 'My', 303022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13022, 3022, 13022, 13022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 3)
    # Central joint node
    ops.node(3023, 8.3, 21.25, 9.9, '-mass', 16.794000206449052, 16.794000206449052, 16.794000206449052, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 8.125, 21.25, 9.9)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 8.475, 21.25, 9.9)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 8.3, 21.25, 9.6)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 8.3, 21.25, 10.2)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 8.3, 21.075, 9.9)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    ops.node(43023, 8.3, 21.425, 9.9)
    ops.element('elasticBeamColumn', 43023, 3023, 43023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303023, 42695.276)
    ops.uniaxialMaterial('Elastic', 403023, 93328.5413)
    ops.section('Aggregator', 13023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403023, 'My', 303023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13023, 3023, 13023, 13023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 3)
    # Central joint node
    ops.node(3024, 13.65, 21.25, 9.9, '-mass', 11.751026606792315, 11.751026606792315, 11.751026606792315, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 13.525, 21.25, 9.9)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 13.65, 21.25, 9.6)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 13.65, 21.25, 10.2)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 13.65, 21.125, 9.9)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    ops.node(43024, 13.65, 21.375, 9.9)
    ops.element('elasticBeamColumn', 43024, 3024, 43024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303024, 27260.85425)
    ops.uniaxialMaterial('Elastic', 403024, 41347.51735)
    ops.section('Aggregator', 13024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403024, 'My', 303024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13024, 3024, 13024, 13024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 3)
    # Central joint node
    ops.node(3025, 0.0, 25.5, 9.9, '-mass', 5.72334535617131, 5.72334535617131, 5.72334535617131, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33025, 0.125, 25.5, 9.9)
    ops.element('elasticBeamColumn', 33025, 3025, 33025, 99999, 88888)
    ops.node(23025, 0.0, 25.5, 9.65)
    ops.element('elasticBeamColumn', 23025, 23025, 3025, 99999, 99999)
    ops.node(73025, 0.0, 25.5, 10.15)
    ops.element('elasticBeamColumn', 73025, 3025, 73025, 99999, 99999)
    ops.node(63025, 0.0, 25.375, 9.9)
    ops.element('elasticBeamColumn', 63025, 63025, 3025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303025, 18081.71275)
    ops.uniaxialMaterial('Elastic', 403025, 21652.02295)
    ops.section('Aggregator', 13025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403025, 'My', 303025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13025, 3025, 13025, 13025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 3)
    # Central joint node
    ops.node(3026, 2.95, 25.5, 9.9, '-mass', 10.162773032656157, 10.162773032656157, 10.162773032656157, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53026, 2.825, 25.5, 9.9)
    ops.element('elasticBeamColumn', 53026, 53026, 3026, 99999, 88888)
    ops.node(33026, 3.075, 25.5, 9.9)
    ops.element('elasticBeamColumn', 33026, 3026, 33026, 99999, 88888)
    ops.node(23026, 2.95, 25.5, 9.65)
    ops.element('elasticBeamColumn', 23026, 23026, 3026, 99999, 99999)
    ops.node(73026, 2.95, 25.5, 10.15)
    ops.element('elasticBeamColumn', 73026, 3026, 73026, 99999, 99999)
    ops.node(63026, 2.95, 25.375, 9.9)
    ops.element('elasticBeamColumn', 63026, 63026, 3026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303026, 21365.5587)
    ops.uniaxialMaterial('Elastic', 403026, 39684.82075)
    ops.section('Aggregator', 13026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403026, 'My', 303026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13026, 3026, 13026, 13026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 3)
    # Central joint node
    ops.node(3027, 8.3, 25.5, 9.9, '-mass', 13.009334455925853, 13.009334455925853, 13.009334455925853, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53027, 8.175, 25.5, 9.9)
    ops.element('elasticBeamColumn', 53027, 53027, 3027, 99999, 88888)
    ops.node(33027, 8.425, 25.5, 9.9)
    ops.element('elasticBeamColumn', 33027, 3027, 33027, 99999, 88888)
    ops.node(23027, 8.3, 25.5, 9.65)
    ops.element('elasticBeamColumn', 23027, 23027, 3027, 99999, 99999)
    ops.node(73027, 8.3, 25.5, 10.15)
    ops.element('elasticBeamColumn', 73027, 3027, 73027, 99999, 99999)
    ops.node(63027, 8.3, 25.375, 9.9)
    ops.element('elasticBeamColumn', 63027, 63027, 3027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303027, 20003.3198)
    ops.uniaxialMaterial('Elastic', 403027, 44883.41415)
    ops.section('Aggregator', 13027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403027, 'My', 303027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13027, 3027, 13027, 13027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 3)
    # Central joint node
    ops.node(3028, 13.65, 25.5, 9.9, '-mass', 8.413943476688715, 8.413943476688715, 8.413943476688715, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53028, 13.525, 25.5, 9.9)
    ops.element('elasticBeamColumn', 53028, 53028, 3028, 99999, 88888)
    ops.node(23028, 13.65, 25.5, 9.65)
    ops.element('elasticBeamColumn', 23028, 23028, 3028, 99999, 99999)
    ops.node(73028, 13.65, 25.5, 10.15)
    ops.element('elasticBeamColumn', 73028, 3028, 73028, 99999, 99999)
    ops.node(63028, 13.65, 25.375, 9.9)
    ops.element('elasticBeamColumn', 63028, 63028, 3028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303028, 15606.14635)
    ops.uniaxialMaterial('Elastic', 403028, 26332.8072)
    ops.section('Aggregator', 13028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403028, 'My', 303028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13028, 3028, 13028, 13028, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 13.0, '-mass', 0.791284403669725, 0.791284403669725, 0.791284403669725, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 13.0)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 12.8)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 13.0)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 8618.42015)
    ops.uniaxialMaterial('Elastic', 404001, 12669.556)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 2.95, 0.0, 13.0, '-mass', 4.319333384945598, 4.319333384945598, 4.319333384945598, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 2.825, 0.0, 13.0)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 3.075, 0.0, 13.0)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 2.95, 0.0, 12.8)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 2.95, 0.125, 13.0)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 14968.2525)
    ops.uniaxialMaterial('Elastic', 404002, 20991.3252)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 8.3, 0.0, 13.0, '-mass', 7.605027626160307, 7.605027626160307, 7.605027626160307, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 8.175, 0.0, 13.0)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 8.425, 0.0, 13.0)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 8.3, 0.0, 12.8)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 8.3, 0.125, 13.0)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 18896.5466)
    ops.uniaxialMaterial('Elastic', 404003, 26193.23205)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 13.65, 0.0, 13.0, '-mass', 4.076978644884434, 4.076978644884434, 4.076978644884434, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 13.525, 0.0, 13.0)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 13.65, 0.0, 12.8)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 13.65, 0.125, 13.0)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 14689.3824)
    ops.uniaxialMaterial('Elastic', 404004, 20622.87195)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 4.25, 13.0, '-mass', 4.906608607955204, 4.906608607955204, 4.906608607955204, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.125, 4.25, 13.0)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 4.25, 12.75)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 4.125, 13.0)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 4.375, 13.0)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 21238.55295)
    ops.uniaxialMaterial('Elastic', 404005, 34387.68365)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 2.95, 4.25, 13.0, '-mass', 11.635489445124687, 11.635489445124687, 11.635489445124687, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 2.825, 4.25, 13.0)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 3.075, 4.25, 13.0)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 2.95, 4.25, 12.75)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 2.95, 4.125, 13.0)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 2.95, 4.375, 13.0)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 26044.6411)
    ops.uniaxialMaterial('Elastic', 404006, 41661.00505)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 8.3, 4.25, 13.0, '-mass', 14.546140879231926, 14.546140879231926, 14.546140879231926, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 8.125, 4.25, 13.0)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 8.475, 4.25, 13.0)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 8.3, 4.25, 12.75)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 8.3, 4.075, 13.0)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 8.3, 4.425, 13.0)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 33385.724)
    ops.uniaxialMaterial('Elastic', 404007, 59086.53925)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 13.65, 4.25, 13.0, '-mass', 7.58973710628263, 7.58973710628263, 7.58973710628263, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 13.525, 4.25, 13.0)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 13.65, 4.25, 12.75)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 13.65, 4.125, 13.0)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 13.65, 4.375, 13.0)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 20984.67205)
    ops.uniaxialMaterial('Elastic', 404008, 34004.025)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 8.5, 13.0, '-mass', 4.257470528856382, 4.257470528856382, 4.257470528856382, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.125, 8.5, 13.0)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 8.5, 12.75)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 8.375, 13.0)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 8.625, 13.0)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 16694.3812)
    ops.uniaxialMaterial('Elastic', 404009, 27534.42545)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 2.95, 8.5, 13.0, '-mass', 10.986351366025865, 10.986351366025865, 10.986351366025865, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 2.825, 8.5, 13.0)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 3.075, 8.5, 13.0)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 2.95, 8.5, 12.75)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 2.95, 8.375, 13.0)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 2.95, 8.625, 13.0)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 23100.87145)
    ops.uniaxialMaterial('Elastic', 404010, 37203.91065)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 8.3, 8.5, 13.0, '-mass', 14.546140879231926, 14.546140879231926, 14.546140879231926, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 8.125, 8.5, 13.0)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 8.475, 8.5, 13.0)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 8.3, 8.5, 12.75)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 8.3, 8.325, 13.0)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 8.3, 8.675, 13.0)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 33385.724)
    ops.uniaxialMaterial('Elastic', 404011, 59086.53925)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 13.65, 8.5, 13.0, '-mass', 7.58973710628263, 7.58973710628263, 7.58973710628263, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 13.525, 8.5, 13.0)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 13.65, 8.5, 12.75)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 13.65, 8.375, 13.0)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 13.65, 8.625, 13.0)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 20984.67205)
    ops.uniaxialMaterial('Elastic', 404012, 34004.025)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4013, 0.0, 12.75, 13.0, '-mass', 4.257470528856382, 4.257470528856382, 4.257470528856382, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 12.75, 13.0)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 12.75, 12.75)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 12.625, 13.0)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 12.875, 13.0)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304013, 16694.3812)
    ops.uniaxialMaterial('Elastic', 404013, 27534.42545)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4014, 2.95, 12.75, 13.0, '-mass', 10.986351366025865, 10.986351366025865, 10.986351366025865, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 2.825, 12.75, 13.0)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 3.075, 12.75, 13.0)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 2.95, 12.75, 12.75)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 2.95, 12.625, 13.0)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 2.95, 12.875, 13.0)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304014, 23100.87145)
    ops.uniaxialMaterial('Elastic', 404014, 37203.91065)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4015, 8.3, 12.75, 13.0, '-mass', 14.546140879231926, 14.546140879231926, 14.546140879231926, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 8.125, 12.75, 13.0)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 8.475, 12.75, 13.0)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 8.3, 12.75, 12.75)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 8.3, 12.575, 13.0)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 8.3, 12.925, 13.0)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304015, 33385.724)
    ops.uniaxialMaterial('Elastic', 404015, 59086.53925)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4016, 13.65, 12.75, 13.0, '-mass', 7.58973710628263, 7.58973710628263, 7.58973710628263, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 13.525, 12.75, 13.0)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 13.65, 12.75, 12.75)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 13.65, 12.625, 13.0)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 13.65, 12.875, 13.0)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304016, 20984.67205)
    ops.uniaxialMaterial('Elastic', 404016, 34004.025)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 4)
    # Central joint node
    ops.node(4017, 0.0, 17.0, 13.0, '-mass', 4.257470528856382, 4.257470528856382, 4.257470528856382, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 0.125, 17.0, 13.0)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 0.0, 17.0, 12.75)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 0.0, 16.875, 13.0)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 0.0, 17.125, 13.0)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304017, 16694.3812)
    ops.uniaxialMaterial('Elastic', 404017, 27534.42545)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 4)
    # Central joint node
    ops.node(4018, 2.95, 17.0, 13.0, '-mass', 10.986351366025865, 10.986351366025865, 10.986351366025865, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 2.825, 17.0, 13.0)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(34018, 3.075, 17.0, 13.0)
    ops.element('elasticBeamColumn', 34018, 4018, 34018, 99999, 88888)
    ops.node(24018, 2.95, 17.0, 12.75)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 2.95, 16.875, 13.0)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 2.95, 17.125, 13.0)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304018, 23100.87145)
    ops.uniaxialMaterial('Elastic', 404018, 37203.91065)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 4)
    # Central joint node
    ops.node(4019, 8.3, 17.0, 13.0, '-mass', 14.546140879231926, 14.546140879231926, 14.546140879231926, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54019, 8.125, 17.0, 13.0)
    ops.element('elasticBeamColumn', 54019, 54019, 4019, 99999, 88888)
    ops.node(34019, 8.475, 17.0, 13.0)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 8.3, 17.0, 12.75)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 8.3, 16.825, 13.0)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    ops.node(44019, 8.3, 17.175, 13.0)
    ops.element('elasticBeamColumn', 44019, 4019, 44019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304019, 33385.724)
    ops.uniaxialMaterial('Elastic', 404019, 59086.53925)
    ops.section('Aggregator', 14019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404019, 'My', 304019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14019, 4019, 14019, 14019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 4)
    # Central joint node
    ops.node(4020, 13.65, 17.0, 13.0, '-mass', 7.58973710628263, 7.58973710628263, 7.58973710628263, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 13.525, 17.0, 13.0)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 13.65, 17.0, 12.75)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 13.65, 16.875, 13.0)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    ops.node(44020, 13.65, 17.125, 13.0)
    ops.element('elasticBeamColumn', 44020, 4020, 44020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304020, 20984.67205)
    ops.uniaxialMaterial('Elastic', 404020, 34004.025)
    ops.section('Aggregator', 14020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404020, 'My', 304020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14020, 4020, 14020, 14020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 4)
    # Central joint node
    ops.node(4021, 0.0, 21.25, 13.0, '-mass', 4.257470528856382, 4.257470528856382, 4.257470528856382, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 0.125, 21.25, 13.0)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 0.0, 21.25, 12.75)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 0.0, 21.125, 13.0)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    ops.node(44021, 0.0, 21.375, 13.0)
    ops.element('elasticBeamColumn', 44021, 4021, 44021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304021, 16694.3812)
    ops.uniaxialMaterial('Elastic', 404021, 27534.42545)
    ops.section('Aggregator', 14021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404021, 'My', 304021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14021, 4021, 14021, 14021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 4)
    # Central joint node
    ops.node(4022, 2.95, 21.25, 13.0, '-mass', 10.986351366025865, 10.986351366025865, 10.986351366025865, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 2.825, 21.25, 13.0)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 3.075, 21.25, 13.0)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 2.95, 21.25, 12.75)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 2.95, 21.125, 13.0)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    ops.node(44022, 2.95, 21.375, 13.0)
    ops.element('elasticBeamColumn', 44022, 4022, 44022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304022, 23100.87145)
    ops.uniaxialMaterial('Elastic', 404022, 37203.91065)
    ops.section('Aggregator', 14022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404022, 'My', 304022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14022, 4022, 14022, 14022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 4)
    # Central joint node
    ops.node(4023, 8.3, 21.25, 13.0, '-mass', 14.546140879231926, 14.546140879231926, 14.546140879231926, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 8.125, 21.25, 13.0)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 8.475, 21.25, 13.0)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 8.3, 21.25, 12.75)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 8.3, 21.075, 13.0)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    ops.node(44023, 8.3, 21.425, 13.0)
    ops.element('elasticBeamColumn', 44023, 4023, 44023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304023, 33385.724)
    ops.uniaxialMaterial('Elastic', 404023, 59086.53925)
    ops.section('Aggregator', 14023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404023, 'My', 304023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14023, 4023, 14023, 14023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 4)
    # Central joint node
    ops.node(4024, 13.65, 21.25, 13.0, '-mass', 7.58973710628263, 7.58973710628263, 7.58973710628263, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 13.525, 21.25, 13.0)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 13.65, 21.25, 12.75)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 13.65, 21.125, 13.0)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    ops.node(44024, 13.65, 21.375, 13.0)
    ops.element('elasticBeamColumn', 44024, 4024, 44024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304024, 20984.67205)
    ops.uniaxialMaterial('Elastic', 404024, 34004.025)
    ops.section('Aggregator', 14024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404024, 'My', 304024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14024, 4024, 14024, 14024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 6, 4)
    # Central joint node
    ops.node(4025, 0.0, 25.5, 13.0, '-mass', 2.3374508607584663, 2.3374508607584663, 2.3374508607584663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 0.125, 25.5, 13.0)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 0.0, 25.5, 12.8)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(64025, 0.0, 25.375, 13.0)
    ops.element('elasticBeamColumn', 64025, 64025, 4025, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304025, 11983.88425)
    ops.uniaxialMaterial('Elastic', 404025, 17057.84635)
    ops.section('Aggregator', 14025, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404025, 'My', 304025, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14025, 4025, 14025, 14025, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 6, 4)
    # Central joint node
    ops.node(4026, 2.95, 25.5, 13.0, '-mass', 5.865499842034339, 5.865499842034339, 5.865499842034339, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 2.825, 25.5, 13.0)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(34026, 3.075, 25.5, 13.0)
    ops.element('elasticBeamColumn', 34026, 4026, 34026, 99999, 88888)
    ops.node(24026, 2.95, 25.5, 12.8)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(64026, 2.95, 25.375, 13.0)
    ops.element('elasticBeamColumn', 64026, 64026, 4026, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304026, 16970.44255)
    ops.uniaxialMaterial('Elastic', 404026, 23640.33435)
    ops.section('Aggregator', 14026, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404026, 'My', 304026, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14026, 4026, 14026, 14026, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 6, 4)
    # Central joint node
    ops.node(4027, 8.3, 25.5, 13.0, '-mass', 7.605027626160307, 7.605027626160307, 7.605027626160307, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54027, 8.175, 25.5, 13.0)
    ops.element('elasticBeamColumn', 54027, 54027, 4027, 99999, 88888)
    ops.node(34027, 8.425, 25.5, 13.0)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 8.3, 25.5, 12.8)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(64027, 8.3, 25.375, 13.0)
    ops.element('elasticBeamColumn', 64027, 64027, 4027, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304027, 18896.5466)
    ops.uniaxialMaterial('Elastic', 404027, 26193.23205)
    ops.section('Aggregator', 14027, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404027, 'My', 304027, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14027, 4027, 14027, 14027, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 6, 4)
    # Central joint node
    ops.node(4028, 13.65, 25.5, 13.0, '-mass', 4.076978644884434, 4.076978644884434, 4.076978644884434, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 13.525, 25.5, 13.0)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 13.65, 25.5, 12.8)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(64028, 13.65, 25.375, 13.0)
    ops.element('elasticBeamColumn', 64028, 64028, 4028, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304028, 14689.3824)
    ops.uniaxialMaterial('Elastic', 404028, 20622.87195)
    ops.section('Aggregator', 14028, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404028, 'My', 304028, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14028, 4028, 14028, 14028, '-orient', 0, 0, 1, 0, 1, 0)
