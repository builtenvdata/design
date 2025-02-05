import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(4025, 14.8, 0.0, 1.6, '-mass', 3.166819571865443, 3.166819571865443, 3.166819571865443, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 14.975, 0.0, 1.6)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 14.8, 0.0, 1.375)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 14.8, 0.0, 1.825)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 0.5)
    # Central joint node
    ops.node(4026, 17.8, 0.0, 1.6, '-mass', 3.166819571865443, 3.166819571865443, 3.166819571865443, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 17.625, 0.0, 1.6)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 17.8, 0.0, 1.375)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 17.8, 0.0, 1.825)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(4027, 14.8, 0.0, 4.8, '-mass', 3.010856269113149, 3.010856269113149, 3.010856269113149, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34027, 14.975, 0.0, 4.8)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 14.8, 0.0, 4.625)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(74027, 14.8, 0.0, 4.975)
    ops.element('elasticBeamColumn', 74027, 4027, 74027, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    # Central joint node
    ops.node(4028, 17.8, 0.0, 4.8, '-mass', 3.010856269113149, 3.010856269113149, 3.010856269113149, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 17.625, 0.0, 4.8)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 17.8, 0.0, 4.625)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(74028, 17.8, 0.0, 4.975)
    ops.element('elasticBeamColumn', 74028, 4028, 74028, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(4029, 14.8, 0.0, 8.0, '-mass', 2.775993883792048, 2.775993883792048, 2.775993883792048, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34029, 14.925, 0.0, 8.0)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 14.8, 0.0, 7.825)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(74029, 14.8, 0.0, 8.175)
    ops.element('elasticBeamColumn', 74029, 4029, 74029, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    # Central joint node
    ops.node(4030, 17.8, 0.0, 8.0, '-mass', 2.775993883792048, 2.775993883792048, 2.775993883792048, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 17.675, 0.0, 8.0)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(24030, 17.8, 0.0, 7.825)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(74030, 17.8, 0.0, 8.175)
    ops.element('elasticBeamColumn', 74030, 4030, 74030, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(4031, 14.8, 0.0, 11.2, '-mass', 2.7759938837920486, 2.7759938837920486, 2.7759938837920486, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34031, 14.925, 0.0, 11.2)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 14.8, 0.0, 11.025)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(74031, 14.8, 0.0, 11.375)
    ops.element('elasticBeamColumn', 74031, 4031, 74031, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    # Central joint node
    ops.node(4032, 17.8, 0.0, 11.2, '-mass', 2.7759938837920486, 2.7759938837920486, 2.7759938837920486, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 17.675, 0.0, 11.2)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 17.8, 0.0, 11.025)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(74032, 17.8, 0.0, 11.375)
    ops.element('elasticBeamColumn', 74032, 4032, 74032, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.2, '-mass', 10.438857940043885, 10.438857940043885, 10.438857940043885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.15, 0.0, 3.2)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.9)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.5)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.15, 3.2)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 40713.2761)
    ops.uniaxialMaterial('Elastic', 401001, 61568.2552)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 7.4, 0.0, 3.2, '-mass', 17.84907163951692, 17.84907163951692, 17.84907163951692, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 7.2, 0.0, 3.2)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 7.6, 0.0, 3.2)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 7.4, 0.0, 2.9)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 7.4, 0.0, 3.5)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 7.4, 0.2, 3.2)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 75915.97445)
    ops.uniaxialMaterial('Elastic', 401002, 149101.35435)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 14.8, 0.0, 3.2, '-mass', 10.984423689279359, 10.984423689279359, 10.984423689279359, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 14.625, 0.0, 3.2)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 14.975, 0.0, 3.2)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 14.8, 0.0, 2.9)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 14.8, 0.0, 3.5)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 14.8, 0.175, 3.2)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 57431.9961)
    ops.uniaxialMaterial('Elastic', 401003, 138997.55275)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 17.8, 0.0, 3.2, '-mass', 10.984423689279357, 10.984423689279357, 10.984423689279357, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 17.625, 0.0, 3.2)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(31004, 17.975, 0.0, 3.2)
    ops.element('elasticBeamColumn', 31004, 1004, 31004, 99999, 88888)
    ops.node(21004, 17.8, 0.0, 2.9)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 17.8, 0.0, 3.5)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 17.8, 0.175, 3.2)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 57431.9961)
    ops.uniaxialMaterial('Elastic', 401004, 138997.55275)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    # Central joint node
    ops.node(1005, 25.2, 0.0, 3.2, '-mass', 17.84907163951692, 17.84907163951692, 17.84907163951692, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51005, 25.0, 0.0, 3.2)
    ops.element('elasticBeamColumn', 51005, 51005, 1005, 99999, 88888)
    ops.node(31005, 25.4, 0.0, 3.2)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 25.2, 0.0, 2.9)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 25.2, 0.0, 3.5)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(41005, 25.2, 0.2, 3.2)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 75915.97445)
    ops.uniaxialMaterial('Elastic', 401005, 149101.35435)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    # Central joint node
    ops.node(1006, 32.6, 0.0, 3.2, '-mass', 10.438857940043885, 10.438857940043885, 10.438857940043885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 32.45, 0.0, 3.2)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(21006, 32.6, 0.0, 2.9)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 32.6, 0.0, 3.5)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(41006, 32.6, 0.15, 3.2)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 40713.2761)
    ops.uniaxialMaterial('Elastic', 401006, 61568.2552)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1007, 0.0, 3.5, 3.2, '-mass', 13.404729131871662, 13.404729131871662, 13.404729131871662, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31007, 0.175, 3.5, 3.2)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 0.0, 3.5, 2.875)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 0.0, 3.5, 3.525)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 0.0, 3.325, 3.2)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 0.0, 3.675, 3.2)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 74927.004)
    ops.uniaxialMaterial('Elastic', 401007, 96007.81725)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1008, 7.4, 3.5, 3.2, '-mass', 20.39987620461998, 20.39987620461998, 20.39987620461998, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 7.2, 3.5, 3.2)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(31008, 7.6, 3.5, 3.2)
    ops.element('elasticBeamColumn', 31008, 1008, 31008, 99999, 88888)
    ops.node(21008, 7.4, 3.5, 2.875)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 7.4, 3.5, 3.525)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 7.4, 3.3, 3.2)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 7.4, 3.7, 3.2)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 119573.6563)
    ops.uniaxialMaterial('Elastic', 401008, 183183.2733)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1009, 14.8, 3.5, 3.2, '-mass', 16.086364406780277, 16.086364406780277, 16.086364406780277, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51009, 14.625, 3.5, 3.2)
    ops.element('elasticBeamColumn', 51009, 51009, 1009, 99999, 88888)
    ops.node(31009, 14.975, 3.5, 3.2)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 14.8, 3.5, 2.875)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 14.8, 3.5, 3.525)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 14.8, 3.325, 3.2)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 14.8, 3.675, 3.2)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 81212.53265)
    ops.uniaxialMaterial('Elastic', 401009, 141966.25075)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1010, 17.8, 3.5, 3.2, '-mass', 16.086364406780273, 16.086364406780273, 16.086364406780273, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 17.625, 3.5, 3.2)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 17.975, 3.5, 3.2)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 17.8, 3.5, 2.875)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 17.8, 3.5, 3.525)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 17.8, 3.325, 3.2)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 17.8, 3.675, 3.2)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 81212.53265)
    ops.uniaxialMaterial('Elastic', 401010, 141966.25075)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    # Central joint node
    ops.node(1011, 25.2, 3.5, 3.2, '-mass', 20.39987620461998, 20.39987620461998, 20.39987620461998, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 25.0, 3.5, 3.2)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 25.4, 3.5, 3.2)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 25.2, 3.5, 2.875)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 25.2, 3.5, 3.525)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 25.2, 3.3, 3.2)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 25.2, 3.7, 3.2)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 119573.6563)
    ops.uniaxialMaterial('Elastic', 401011, 183183.2733)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    # Central joint node
    ops.node(1012, 32.6, 3.5, 3.2, '-mass', 13.404729131871665, 13.404729131871665, 13.404729131871665, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 32.425, 3.5, 3.2)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 32.6, 3.5, 2.875)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 32.6, 3.5, 3.525)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 32.6, 3.325, 3.2)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 32.6, 3.675, 3.2)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 74927.004)
    ops.uniaxialMaterial('Elastic', 401012, 96007.81725)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1013, 0.0, 7.0, 3.2, '-mass', 13.404729131871662, 13.404729131871662, 13.404729131871662, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.175, 7.0, 3.2)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 7.0, 2.875)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 7.0, 3.525)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 6.825, 3.2)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 7.175, 3.2)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301013, 74927.004)
    ops.uniaxialMaterial('Elastic', 401013, 96007.81725)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1014, 7.4, 7.0, 3.2, '-mass', 20.39987620461998, 20.39987620461998, 20.39987620461998, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 7.2, 7.0, 3.2)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 7.6, 7.0, 3.2)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 7.4, 7.0, 2.875)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 7.4, 7.0, 3.525)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 7.4, 6.8, 3.2)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 7.4, 7.2, 3.2)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301014, 119573.6563)
    ops.uniaxialMaterial('Elastic', 401014, 183183.2733)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1015, 14.8, 7.0, 3.2, '-mass', 14.454544024196537, 14.454544024196537, 14.454544024196537, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 14.625, 7.0, 3.2)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 14.975, 7.0, 3.2)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 14.8, 7.0, 2.875)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 14.8, 7.0, 3.525)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 14.8, 6.825, 3.2)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 14.8, 7.175, 3.2)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301015, 76824.41695)
    ops.uniaxialMaterial('Elastic', 401015, 134295.46015)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1016, 17.8, 7.0, 3.2, '-mass', 14.454544024196533, 14.454544024196533, 14.454544024196533, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 17.625, 7.0, 3.2)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(31016, 17.975, 7.0, 3.2)
    ops.element('elasticBeamColumn', 31016, 1016, 31016, 99999, 88888)
    ops.node(21016, 17.8, 7.0, 2.875)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 17.8, 7.0, 3.525)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 17.8, 6.825, 3.2)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 17.8, 7.175, 3.2)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301016, 76824.41695)
    ops.uniaxialMaterial('Elastic', 401016, 134295.46015)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    # Central joint node
    ops.node(1017, 25.2, 7.0, 3.2, '-mass', 20.39987620461998, 20.39987620461998, 20.39987620461998, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51017, 25.0, 7.0, 3.2)
    ops.element('elasticBeamColumn', 51017, 51017, 1017, 99999, 88888)
    ops.node(31017, 25.4, 7.0, 3.2)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 25.2, 7.0, 2.875)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 25.2, 7.0, 3.525)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 25.2, 6.8, 3.2)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 25.2, 7.2, 3.2)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301017, 119573.6563)
    ops.uniaxialMaterial('Elastic', 401017, 183183.2733)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    # Central joint node
    ops.node(1018, 32.6, 7.0, 3.2, '-mass', 13.404729131871665, 13.404729131871665, 13.404729131871665, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 32.425, 7.0, 3.2)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(21018, 32.6, 7.0, 2.875)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 32.6, 7.0, 3.525)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 32.6, 6.825, 3.2)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 32.6, 7.175, 3.2)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301018, 74927.004)
    ops.uniaxialMaterial('Elastic', 401018, 96007.81725)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1019, 0.0, 10.5, 3.2, '-mass', 10.438857940043885, 10.438857940043885, 10.438857940043885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31019, 0.15, 10.5, 3.2)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 0.0, 10.5, 2.9)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 0.0, 10.5, 3.5)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 0.0, 10.35, 3.2)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301019, 40713.2761)
    ops.uniaxialMaterial('Elastic', 401019, 61568.2552)
    ops.section('Aggregator', 11019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401019, 'My', 301019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11019, 1019, 11019, 11019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1020, 7.4, 10.5, 3.2, '-mass', 17.84907163951692, 17.84907163951692, 17.84907163951692, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 7.2, 10.5, 3.2)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(31020, 7.6, 10.5, 3.2)
    ops.element('elasticBeamColumn', 31020, 1020, 31020, 99999, 88888)
    ops.node(21020, 7.4, 10.5, 2.9)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 7.4, 10.5, 3.5)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 7.4, 10.3, 3.2)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301020, 75915.97445)
    ops.uniaxialMaterial('Elastic', 401020, 149101.35435)
    ops.section('Aggregator', 11020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401020, 'My', 301020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11020, 1020, 11020, 11020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1021, 14.8, 10.5, 3.2, '-mass', 12.641747037582467, 12.641747037582467, 12.641747037582467, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51021, 14.625, 10.5, 3.2)
    ops.element('elasticBeamColumn', 51021, 51021, 1021, 99999, 88888)
    ops.node(31021, 14.975, 10.5, 3.2)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 14.8, 10.5, 2.9)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 14.8, 10.5, 3.5)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 14.8, 10.325, 3.2)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301021, 48917.2854)
    ops.uniaxialMaterial('Elastic', 401021, 109311.2892)
    ops.section('Aggregator', 11021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401021, 'My', 301021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11021, 1021, 11021, 11021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1022, 17.8, 10.5, 3.2, '-mass', 12.641747037582466, 12.641747037582466, 12.641747037582466, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 17.625, 10.5, 3.2)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 17.975, 10.5, 3.2)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 17.8, 10.5, 2.9)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 17.8, 10.5, 3.5)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 17.8, 10.325, 3.2)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301022, 48917.2854)
    ops.uniaxialMaterial('Elastic', 401022, 109311.2892)
    ops.section('Aggregator', 11022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401022, 'My', 301022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11022, 1022, 11022, 11022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 1)
    # Central joint node
    ops.node(1023, 25.2, 10.5, 3.2, '-mass', 17.84907163951692, 17.84907163951692, 17.84907163951692, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 25.0, 10.5, 3.2)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 25.4, 10.5, 3.2)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 25.2, 10.5, 2.9)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 25.2, 10.5, 3.5)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 25.2, 10.3, 3.2)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301023, 75915.97445)
    ops.uniaxialMaterial('Elastic', 401023, 149101.35435)
    ops.section('Aggregator', 11023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401023, 'My', 301023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11023, 1023, 11023, 11023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 1)
    # Central joint node
    ops.node(1024, 32.6, 10.5, 3.2, '-mass', 10.438857940043885, 10.438857940043885, 10.438857940043885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 32.45, 10.5, 3.2)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 32.6, 10.5, 2.9)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 32.6, 10.5, 3.5)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 32.6, 10.35, 3.2)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301024, 40713.2761)
    ops.uniaxialMaterial('Elastic', 401024, 61568.2552)
    ops.section('Aggregator', 11024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401024, 'My', 301024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11024, 1024, 11024, 11024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 6.4, '-mass', 10.245585768790061, 10.245585768790061, 10.245585768790061, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.15, 0.0, 6.4)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 6.1)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.7)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.15, 6.4)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 34953.8887)
    ops.uniaxialMaterial('Elastic', 402001, 53108.3079)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 7.4, 0.0, 6.4, '-mass', 17.64876582911937, 17.64876582911937, 17.64876582911937, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 7.2, 0.0, 6.4)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 7.6, 0.0, 6.4)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 7.4, 0.0, 6.1)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 7.4, 0.0, 6.7)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 7.4, 0.2, 6.4)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 56652.7213)
    ops.uniaxialMaterial('Elastic', 402002, 126919.95075)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 14.8, 0.0, 6.4, '-mass', 10.781365585303822, 10.781365585303822, 10.781365585303822, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 14.625, 0.0, 6.4)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 14.975, 0.0, 6.4)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 14.8, 0.0, 6.1)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 14.8, 0.0, 6.7)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 14.8, 0.175, 6.4)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 48973.3302)
    ops.uniaxialMaterial('Elastic', 402003, 117564.9859)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 17.8, 0.0, 6.4, '-mass', 10.78136558530382, 10.78136558530382, 10.78136558530382, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 17.625, 0.0, 6.4)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(32004, 17.975, 0.0, 6.4)
    ops.element('elasticBeamColumn', 32004, 2004, 32004, 99999, 88888)
    ops.node(22004, 17.8, 0.0, 6.1)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 17.8, 0.0, 6.7)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 17.8, 0.175, 6.4)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 48973.3302)
    ops.uniaxialMaterial('Elastic', 402004, 117564.9859)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    # Central joint node
    ops.node(2005, 25.2, 0.0, 6.4, '-mass', 17.64876582911937, 17.64876582911937, 17.64876582911937, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52005, 25.0, 0.0, 6.4)
    ops.element('elasticBeamColumn', 52005, 52005, 2005, 99999, 88888)
    ops.node(32005, 25.4, 0.0, 6.4)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 25.2, 0.0, 6.1)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 25.2, 0.0, 6.7)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(42005, 25.2, 0.2, 6.4)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 56652.7213)
    ops.uniaxialMaterial('Elastic', 402005, 126919.95075)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    # Central joint node
    ops.node(2006, 32.6, 0.0, 6.4, '-mass', 10.245585768790063, 10.245585768790063, 10.245585768790063, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 32.45, 0.0, 6.4)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(22006, 32.6, 0.0, 6.1)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 32.6, 0.0, 6.7)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(42006, 32.6, 0.15, 6.4)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 34953.8887)
    ops.uniaxialMaterial('Elastic', 402006, 53108.3079)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2007, 0.0, 3.5, 6.4, '-mass', 12.99861292392059, 12.99861292392059, 12.99861292392059, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32007, 0.175, 3.5, 6.4)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 0.0, 3.5, 6.075)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 0.0, 3.5, 6.725)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 0.0, 3.325, 6.4)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 0.0, 3.675, 6.4)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 63846.33745)
    ops.uniaxialMaterial('Elastic', 402007, 82916.51265)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2008, 7.4, 3.5, 6.4, '-mass', 20.146053574650562, 20.146053574650562, 20.146053574650562, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 7.2, 3.5, 6.4)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(32008, 7.6, 3.5, 6.4)
    ops.element('elasticBeamColumn', 32008, 2008, 32008, 99999, 88888)
    ops.node(22008, 7.4, 3.5, 6.075)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 7.4, 3.5, 6.725)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 7.4, 3.3, 6.4)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 7.4, 3.7, 6.4)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 89832.6544)
    ops.uniaxialMaterial('Elastic', 402008, 157034.9394)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2009, 14.8, 3.5, 6.4, '-mass', 15.680248198829203, 15.680248198829203, 15.680248198829203, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52009, 14.625, 3.5, 6.4)
    ops.element('elasticBeamColumn', 52009, 52009, 2009, 99999, 88888)
    ops.node(32009, 14.975, 3.5, 6.4)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 14.8, 3.5, 6.075)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 14.8, 3.5, 6.725)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 14.8, 3.325, 6.4)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 14.8, 3.675, 6.4)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 69801.7861)
    ops.uniaxialMaterial('Elastic', 402009, 122019.3182)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2010, 17.8, 3.5, 6.4, '-mass', 15.680248198829199, 15.680248198829199, 15.680248198829199, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 17.625, 3.5, 6.4)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 17.975, 3.5, 6.4)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 17.8, 3.5, 6.075)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 17.8, 3.5, 6.725)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 17.8, 3.325, 6.4)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 17.8, 3.675, 6.4)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 69801.7861)
    ops.uniaxialMaterial('Elastic', 402010, 122019.3182)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    # Central joint node
    ops.node(2011, 25.2, 3.5, 6.4, '-mass', 20.146053574650562, 20.146053574650562, 20.146053574650562, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 25.0, 3.5, 6.4)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 25.4, 3.5, 6.4)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 25.2, 3.5, 6.075)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 25.2, 3.5, 6.725)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 25.2, 3.3, 6.4)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 25.2, 3.7, 6.4)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 89832.6544)
    ops.uniaxialMaterial('Elastic', 402011, 157034.9394)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    # Central joint node
    ops.node(2012, 32.6, 3.5, 6.4, '-mass', 12.998612923920593, 12.998612923920593, 12.998612923920593, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 32.425, 3.5, 6.4)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 32.6, 3.5, 6.075)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 32.6, 3.5, 6.725)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 32.6, 3.325, 6.4)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 32.6, 3.675, 6.4)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 63846.33745)
    ops.uniaxialMaterial('Elastic', 402012, 82916.51265)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2013, 0.0, 7.0, 6.4, '-mass', 12.99861292392059, 12.99861292392059, 12.99861292392059, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.175, 7.0, 6.4)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 7.0, 6.075)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 7.0, 6.725)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 6.825, 6.4)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 7.175, 6.4)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302013, 63846.33745)
    ops.uniaxialMaterial('Elastic', 402013, 82916.51265)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2014, 7.4, 7.0, 6.4, '-mass', 20.146053574650562, 20.146053574650562, 20.146053574650562, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 7.2, 7.0, 6.4)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 7.6, 7.0, 6.4)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 7.4, 7.0, 6.075)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 7.4, 7.0, 6.725)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 7.4, 6.8, 6.4)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 7.4, 7.2, 6.4)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302014, 89832.6544)
    ops.uniaxialMaterial('Elastic', 402014, 157034.9394)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2015, 14.8, 7.0, 6.4, '-mass', 14.048427816245464, 14.048427816245464, 14.048427816245464, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 14.625, 7.0, 6.4)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 14.975, 7.0, 6.4)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 14.8, 7.0, 6.075)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 14.8, 7.0, 6.725)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 14.8, 6.825, 6.4)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 14.8, 7.175, 6.4)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302015, 65793.84005)
    ops.uniaxialMaterial('Elastic', 402015, 115013.0957)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2016, 17.8, 7.0, 6.4, '-mass', 14.04842781624546, 14.04842781624546, 14.04842781624546, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 17.625, 7.0, 6.4)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(32016, 17.975, 7.0, 6.4)
    ops.element('elasticBeamColumn', 32016, 2016, 32016, 99999, 88888)
    ops.node(22016, 17.8, 7.0, 6.075)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 17.8, 7.0, 6.725)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 17.8, 6.825, 6.4)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 17.8, 7.175, 6.4)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302016, 65793.84005)
    ops.uniaxialMaterial('Elastic', 402016, 115013.0957)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    # Central joint node
    ops.node(2017, 25.2, 7.0, 6.4, '-mass', 20.146053574650562, 20.146053574650562, 20.146053574650562, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52017, 25.0, 7.0, 6.4)
    ops.element('elasticBeamColumn', 52017, 52017, 2017, 99999, 88888)
    ops.node(32017, 25.4, 7.0, 6.4)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 25.2, 7.0, 6.075)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 25.2, 7.0, 6.725)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 25.2, 6.8, 6.4)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 25.2, 7.2, 6.4)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302017, 89832.6544)
    ops.uniaxialMaterial('Elastic', 402017, 157034.9394)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    # Central joint node
    ops.node(2018, 32.6, 7.0, 6.4, '-mass', 12.998612923920593, 12.998612923920593, 12.998612923920593, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 32.425, 7.0, 6.4)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(22018, 32.6, 7.0, 6.075)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 32.6, 7.0, 6.725)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 32.6, 6.825, 6.4)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 32.6, 7.175, 6.4)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302018, 63846.33745)
    ops.uniaxialMaterial('Elastic', 402018, 82916.51265)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2019, 0.0, 10.5, 6.4, '-mass', 10.245585768790061, 10.245585768790061, 10.245585768790061, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32019, 0.15, 10.5, 6.4)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 0.0, 10.5, 6.1)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 0.0, 10.5, 6.7)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 0.0, 10.35, 6.4)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302019, 34953.8887)
    ops.uniaxialMaterial('Elastic', 402019, 53108.3079)
    ops.section('Aggregator', 12019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402019, 'My', 302019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12019, 2019, 12019, 12019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2020, 7.4, 10.5, 6.4, '-mass', 17.64876582911937, 17.64876582911937, 17.64876582911937, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 7.2, 10.5, 6.4)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(32020, 7.6, 10.5, 6.4)
    ops.element('elasticBeamColumn', 32020, 2020, 32020, 99999, 88888)
    ops.node(22020, 7.4, 10.5, 6.1)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 7.4, 10.5, 6.7)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 7.4, 10.3, 6.4)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302020, 56652.7213)
    ops.uniaxialMaterial('Elastic', 402020, 126919.95075)
    ops.section('Aggregator', 12020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402020, 'My', 302020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12020, 2020, 12020, 12020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2021, 14.8, 10.5, 6.4, '-mass', 12.32125774094638, 12.32125774094638, 12.32125774094638, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52021, 14.625, 10.5, 6.4)
    ops.element('elasticBeamColumn', 52021, 52021, 2021, 99999, 88888)
    ops.node(32021, 14.975, 10.5, 6.4)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 14.8, 10.5, 6.1)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 14.8, 10.5, 6.7)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 14.8, 10.325, 6.4)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302021, 41935.70855)
    ops.uniaxialMaterial('Elastic', 402021, 92952.3854)
    ops.section('Aggregator', 12021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402021, 'My', 302021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12021, 2021, 12021, 12021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2022, 17.8, 10.5, 6.4, '-mass', 12.321257740946379, 12.321257740946379, 12.321257740946379, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 17.625, 10.5, 6.4)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 17.975, 10.5, 6.4)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 17.8, 10.5, 6.1)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 17.8, 10.5, 6.7)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 17.8, 10.325, 6.4)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302022, 41935.70855)
    ops.uniaxialMaterial('Elastic', 402022, 92952.3854)
    ops.section('Aggregator', 12022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402022, 'My', 302022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12022, 2022, 12022, 12022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 2)
    # Central joint node
    ops.node(2023, 25.2, 10.5, 6.4, '-mass', 17.64876582911937, 17.64876582911937, 17.64876582911937, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 25.0, 10.5, 6.4)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 25.4, 10.5, 6.4)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 25.2, 10.5, 6.1)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 25.2, 10.5, 6.7)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 25.2, 10.3, 6.4)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302023, 56652.7213)
    ops.uniaxialMaterial('Elastic', 402023, 126919.95075)
    ops.section('Aggregator', 12023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402023, 'My', 302023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12023, 2023, 12023, 12023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 2)
    # Central joint node
    ops.node(2024, 32.6, 10.5, 6.4, '-mass', 10.245585768790063, 10.245585768790063, 10.245585768790063, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 32.45, 10.5, 6.4)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 32.6, 10.5, 6.1)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 32.6, 10.5, 6.7)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 32.6, 10.35, 6.4)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302024, 34953.8887)
    ops.uniaxialMaterial('Elastic', 402024, 53108.3079)
    ops.section('Aggregator', 12024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402024, 'My', 302024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12024, 2024, 12024, 12024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 9.6, '-mass', 10.052313597536239, 10.052313597536239, 10.052313597536239, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 9.6)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 9.3)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 9.9)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 9.6)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 18222.4929)
    ops.uniaxialMaterial('Elastic', 403001, 35593.90625)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 7.4, 0.0, 9.6, '-mass', 17.373536471321206, 17.373536471321206, 17.373536471321206, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 7.225, 0.0, 9.6)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 7.575, 0.0, 9.6)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 7.4, 0.0, 9.3)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 7.4, 0.0, 9.9)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 7.4, 0.175, 9.6)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 33675.0615)
    ops.uniaxialMaterial('Elastic', 403002, 87004.6919)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 14.8, 0.0, 9.6, '-mass', 10.578307481328288, 10.578307481328288, 10.578307481328288, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 14.675, 0.0, 9.6)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 14.925, 0.0, 9.6)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 14.8, 0.0, 9.3)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 14.8, 0.0, 9.9)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 14.8, 0.125, 9.6)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 22506.9799)
    ops.uniaxialMaterial('Elastic', 403003, 63823.83375)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 17.8, 0.0, 9.6, '-mass', 10.578307481328286, 10.578307481328286, 10.578307481328286, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 17.675, 0.0, 9.6)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(33004, 17.925, 0.0, 9.6)
    ops.element('elasticBeamColumn', 33004, 3004, 33004, 99999, 88888)
    ops.node(23004, 17.8, 0.0, 9.3)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 17.8, 0.0, 9.9)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 17.8, 0.125, 9.6)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 22506.9799)
    ops.uniaxialMaterial('Elastic', 403004, 63823.83375)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    # Central joint node
    ops.node(3005, 25.2, 0.0, 9.6, '-mass', 17.373536471321206, 17.373536471321206, 17.373536471321206, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53005, 25.025, 0.0, 9.6)
    ops.element('elasticBeamColumn', 53005, 53005, 3005, 99999, 88888)
    ops.node(33005, 25.375, 0.0, 9.6)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 25.2, 0.0, 9.3)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 25.2, 0.0, 9.9)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(43005, 25.2, 0.175, 9.6)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 33675.0615)
    ops.uniaxialMaterial('Elastic', 403005, 87004.6919)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    # Central joint node
    ops.node(3006, 32.6, 0.0, 9.6, '-mass', 10.052313597536239, 10.052313597536239, 10.052313597536239, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 32.475, 0.0, 9.6)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(23006, 32.6, 0.0, 9.3)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 32.6, 0.0, 9.9)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(43006, 32.6, 0.125, 9.6)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 18222.4929)
    ops.uniaxialMaterial('Elastic', 403006, 35593.90625)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3007, 0.0, 3.5, 9.6, '-mass', 12.59249671596952, 12.59249671596952, 12.59249671596952, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33007, 0.125, 3.5, 9.6)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 0.0, 3.5, 9.275)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 0.0, 3.5, 9.925)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 0.0, 3.375, 9.6)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 0.0, 3.625, 9.6)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 30944.792)
    ops.uniaxialMaterial('Elastic', 403007, 47753.4327)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3008, 7.4, 3.5, 9.6, '-mass', 19.74238384987992, 19.74238384987992, 19.74238384987992, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 7.225, 3.5, 9.6)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(33008, 7.575, 3.5, 9.6)
    ops.element('elasticBeamColumn', 33008, 3008, 33008, 99999, 88888)
    ops.node(23008, 7.4, 3.5, 9.275)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 7.4, 3.5, 9.925)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 7.4, 3.325, 9.6)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 7.4, 3.675, 9.6)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 54038.6704)
    ops.uniaxialMaterial('Elastic', 403008, 109479.2364)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3009, 14.8, 3.5, 9.6, '-mass', 15.274131990878134, 15.274131990878134, 15.274131990878134, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53009, 14.675, 3.5, 9.6)
    ops.element('elasticBeamColumn', 53009, 53009, 3009, 99999, 88888)
    ops.node(33009, 14.925, 3.5, 9.6)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 14.8, 3.5, 9.275)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 14.8, 3.5, 9.925)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 14.8, 3.375, 9.6)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 14.8, 3.625, 9.6)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 34479.99875)
    ops.uniaxialMaterial('Elastic', 403009, 69581.26095)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3010, 17.8, 3.5, 9.6, '-mass', 15.27413199087813, 15.27413199087813, 15.27413199087813, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 17.675, 3.5, 9.6)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 17.925, 3.5, 9.6)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 17.8, 3.5, 9.275)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 17.8, 3.5, 9.925)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 17.8, 3.375, 9.6)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 17.8, 3.625, 9.6)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 34479.99875)
    ops.uniaxialMaterial('Elastic', 403010, 69581.26095)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    # Central joint node
    ops.node(3011, 25.2, 3.5, 9.6, '-mass', 19.74238384987992, 19.74238384987992, 19.74238384987992, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 25.025, 3.5, 9.6)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 25.375, 3.5, 9.6)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 25.2, 3.5, 9.275)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 25.2, 3.5, 9.925)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 25.2, 3.325, 9.6)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 25.2, 3.675, 9.6)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 54038.6704)
    ops.uniaxialMaterial('Elastic', 403011, 109479.2364)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    # Central joint node
    ops.node(3012, 32.6, 3.5, 9.6, '-mass', 12.592496715969524, 12.592496715969524, 12.592496715969524, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 32.475, 3.5, 9.6)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 32.6, 3.5, 9.275)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 32.6, 3.5, 9.925)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 32.6, 3.375, 9.6)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 32.6, 3.625, 9.6)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 30944.792)
    ops.uniaxialMaterial('Elastic', 403012, 47753.4327)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3013, 0.0, 7.0, 9.6, '-mass', 12.59249671596952, 12.59249671596952, 12.59249671596952, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 7.0, 9.6)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 7.0, 9.275)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 7.0, 9.925)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 6.875, 9.6)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 7.125, 9.6)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303013, 30944.792)
    ops.uniaxialMaterial('Elastic', 403013, 47753.4327)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3014, 7.4, 7.0, 9.6, '-mass', 19.74238384987992, 19.74238384987992, 19.74238384987992, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 7.225, 7.0, 9.6)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 7.575, 7.0, 9.6)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 7.4, 7.0, 9.275)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 7.4, 7.0, 9.925)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 7.4, 6.825, 9.6)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 7.4, 7.175, 9.6)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303014, 54038.6704)
    ops.uniaxialMaterial('Elastic', 403014, 109479.2364)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3015, 14.8, 7.0, 9.6, '-mass', 13.642311608294396, 13.642311608294396, 13.642311608294396, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 14.675, 7.0, 9.6)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 14.925, 7.0, 9.6)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 14.8, 7.0, 9.275)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 14.8, 7.0, 9.925)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 14.8, 6.875, 9.6)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 14.8, 7.125, 9.6)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303015, 32238.7223)
    ops.uniaxialMaterial('Elastic', 403015, 65024.2645)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3016, 17.8, 7.0, 9.6, '-mass', 13.642311608294392, 13.642311608294392, 13.642311608294392, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 17.675, 7.0, 9.6)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(33016, 17.925, 7.0, 9.6)
    ops.element('elasticBeamColumn', 33016, 3016, 33016, 99999, 88888)
    ops.node(23016, 17.8, 7.0, 9.275)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 17.8, 7.0, 9.925)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 17.8, 6.875, 9.6)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 17.8, 7.125, 9.6)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303016, 32238.7223)
    ops.uniaxialMaterial('Elastic', 403016, 65024.2645)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    # Central joint node
    ops.node(3017, 25.2, 7.0, 9.6, '-mass', 19.74238384987992, 19.74238384987992, 19.74238384987992, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53017, 25.025, 7.0, 9.6)
    ops.element('elasticBeamColumn', 53017, 53017, 3017, 99999, 88888)
    ops.node(33017, 25.375, 7.0, 9.6)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 25.2, 7.0, 9.275)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 25.2, 7.0, 9.925)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 25.2, 6.825, 9.6)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 25.2, 7.175, 9.6)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303017, 54038.6704)
    ops.uniaxialMaterial('Elastic', 403017, 109479.2364)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    # Central joint node
    ops.node(3018, 32.6, 7.0, 9.6, '-mass', 12.592496715969524, 12.592496715969524, 12.592496715969524, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 32.475, 7.0, 9.6)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(23018, 32.6, 7.0, 9.275)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 32.6, 7.0, 9.925)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 32.6, 6.875, 9.6)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 32.6, 7.125, 9.6)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303018, 30944.792)
    ops.uniaxialMaterial('Elastic', 403018, 47753.4327)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3019, 0.0, 10.5, 9.6, '-mass', 10.052313597536239, 10.052313597536239, 10.052313597536239, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33019, 0.125, 10.5, 9.6)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 0.0, 10.5, 9.3)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 0.0, 10.5, 9.9)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 0.0, 10.375, 9.6)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303019, 18222.4929)
    ops.uniaxialMaterial('Elastic', 403019, 35593.90625)
    ops.section('Aggregator', 13019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403019, 'My', 303019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13019, 3019, 13019, 13019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3020, 7.4, 10.5, 9.6, '-mass', 17.373536471321206, 17.373536471321206, 17.373536471321206, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 7.225, 10.5, 9.6)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(33020, 7.575, 10.5, 9.6)
    ops.element('elasticBeamColumn', 33020, 3020, 33020, 99999, 88888)
    ops.node(23020, 7.4, 10.5, 9.3)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 7.4, 10.5, 9.9)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 7.4, 10.325, 9.6)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303020, 33675.0615)
    ops.uniaxialMaterial('Elastic', 403020, 87004.6919)
    ops.section('Aggregator', 13020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403020, 'My', 303020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13020, 3020, 13020, 13020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3021, 14.8, 10.5, 9.6, '-mass', 12.000768444310296, 12.000768444310296, 12.000768444310296, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53021, 14.675, 10.5, 9.6)
    ops.element('elasticBeamColumn', 53021, 53021, 3021, 99999, 88888)
    ops.node(33021, 14.925, 10.5, 9.6)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 14.8, 10.5, 9.3)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 14.8, 10.5, 9.9)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 14.8, 10.375, 9.6)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303021, 20350.1183)
    ops.uniaxialMaterial('Elastic', 403021, 51557.5078)
    ops.section('Aggregator', 13021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403021, 'My', 303021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13021, 3021, 13021, 13021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3022, 17.8, 10.5, 9.6, '-mass', 12.000768444310294, 12.000768444310294, 12.000768444310294, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 17.675, 10.5, 9.6)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 17.925, 10.5, 9.6)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 17.8, 10.5, 9.3)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 17.8, 10.5, 9.9)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 17.8, 10.375, 9.6)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303022, 20350.1183)
    ops.uniaxialMaterial('Elastic', 403022, 51557.5078)
    ops.section('Aggregator', 13022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403022, 'My', 303022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13022, 3022, 13022, 13022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 3)
    # Central joint node
    ops.node(3023, 25.2, 10.5, 9.6, '-mass', 17.373536471321206, 17.373536471321206, 17.373536471321206, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 25.025, 10.5, 9.6)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 25.375, 10.5, 9.6)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 25.2, 10.5, 9.3)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 25.2, 10.5, 9.9)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 25.2, 10.325, 9.6)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303023, 33675.0615)
    ops.uniaxialMaterial('Elastic', 403023, 87004.6919)
    ops.section('Aggregator', 13023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403023, 'My', 303023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13023, 3023, 13023, 13023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 3)
    # Central joint node
    ops.node(3024, 32.6, 10.5, 9.6, '-mass', 10.052313597536239, 10.052313597536239, 10.052313597536239, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 32.475, 10.5, 9.6)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 32.6, 10.5, 9.3)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 32.6, 10.5, 9.9)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 32.6, 10.375, 9.6)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303024, 18222.4929)
    ops.uniaxialMaterial('Elastic', 403024, 35593.90625)
    ops.section('Aggregator', 13024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403024, 'My', 303024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13024, 3024, 13024, 13024, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 12.8, '-mass', 4.7533329655280845, 4.7533329655280845, 4.7533329655280845, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 12.8)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 12.55)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 12.8)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 15600.29345)
    ops.uniaxialMaterial('Elastic', 404001, 28617.48155)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 7.4, 0.0, 12.8, '-mass', 9.239999264389501, 9.239999264389501, 9.239999264389501, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 7.225, 0.0, 12.8)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 7.575, 0.0, 12.8)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 7.4, 0.0, 12.55)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 7.4, 0.175, 12.8)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 29231.79375)
    ops.uniaxialMaterial('Elastic', 404002, 52220.74405)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 14.8, 0.0, 12.8, '-mass', 5.0897244028369535, 5.0897244028369535, 5.0897244028369535, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 14.675, 0.0, 12.8)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 14.925, 0.0, 12.8)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 14.8, 0.0, 12.55)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 14.8, 0.125, 12.8)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 15978.42665)
    ops.uniaxialMaterial('Elastic', 404003, 29236.5356)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 17.8, 0.0, 12.8, '-mass', 5.089724402836953, 5.089724402836953, 5.089724402836953, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 17.675, 0.0, 12.8)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(34004, 17.925, 0.0, 12.8)
    ops.element('elasticBeamColumn', 34004, 4004, 34004, 99999, 88888)
    ops.node(24004, 17.8, 0.0, 12.55)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 17.8, 0.125, 12.8)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 15978.42665)
    ops.uniaxialMaterial('Elastic', 404004, 29236.5356)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    # Central joint node
    ops.node(4005, 25.2, 0.0, 12.8, '-mass', 9.239999264389501, 9.239999264389501, 9.239999264389501, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54005, 25.025, 0.0, 12.8)
    ops.element('elasticBeamColumn', 54005, 54005, 4005, 99999, 88888)
    ops.node(34005, 25.375, 0.0, 12.8)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 25.2, 0.0, 12.55)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(44005, 25.2, 0.175, 12.8)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 29231.79375)
    ops.uniaxialMaterial('Elastic', 404005, 52220.74405)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    # Central joint node
    ops.node(4006, 32.6, 0.0, 12.8, '-mass', 4.753332965528085, 4.753332965528085, 4.753332965528085, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 32.475, 0.0, 12.8)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(24006, 32.6, 0.0, 12.55)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(44006, 32.6, 0.125, 12.8)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 15600.29345)
    ops.uniaxialMaterial('Elastic', 404006, 28617.48155)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4007, 0.0, 3.5, 12.8, '-mass', 8.628378469282467, 8.628378469282467, 8.628378469282467, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34007, 0.125, 3.5, 12.8)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 0.0, 3.5, 12.5)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 0.0, 3.375, 12.8)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 0.0, 3.625, 12.8)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 22135.15025)
    ops.uniaxialMaterial('Elastic', 404007, 44471.5055)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4008, 7.4, 3.5, 12.8, '-mass', 16.733209537953314, 16.733209537953314, 16.733209537953314, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 7.225, 3.5, 12.8)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(34008, 7.575, 3.5, 12.8)
    ops.element('elasticBeamColumn', 34008, 4008, 34008, 99999, 88888)
    ops.node(24008, 7.4, 3.5, 12.5)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 7.4, 3.325, 12.8)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 7.4, 3.675, 12.8)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 35466.717)
    ops.uniaxialMaterial('Elastic', 404008, 77166.31635)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4009, 14.8, 3.5, 12.8, '-mass', 12.223877148880176, 12.223877148880176, 12.223877148880176, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54009, 14.675, 3.5, 12.8)
    ops.element('elasticBeamColumn', 54009, 54009, 4009, 99999, 88888)
    ops.node(34009, 14.925, 3.5, 12.8)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 14.8, 3.5, 12.5)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 14.8, 3.375, 12.8)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 14.8, 3.625, 12.8)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 26137.60095)
    ops.uniaxialMaterial('Elastic', 404009, 51698.46575)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4010, 17.8, 3.5, 12.8, '-mass', 12.223877148880172, 12.223877148880172, 12.223877148880172, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 17.675, 3.5, 12.8)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 17.925, 3.5, 12.8)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 17.8, 3.5, 12.5)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 17.8, 3.375, 12.8)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 17.8, 3.625, 12.8)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 26137.60095)
    ops.uniaxialMaterial('Elastic', 404010, 51698.46575)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    # Central joint node
    ops.node(4011, 25.2, 3.5, 12.8, '-mass', 16.733209537953314, 16.733209537953314, 16.733209537953314, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 25.025, 3.5, 12.8)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 25.375, 3.5, 12.8)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 25.2, 3.5, 12.5)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 25.2, 3.325, 12.8)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 25.2, 3.675, 12.8)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 35466.717)
    ops.uniaxialMaterial('Elastic', 404011, 77166.31635)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    # Central joint node
    ops.node(4012, 32.6, 3.5, 12.8, '-mass', 8.628378469282469, 8.628378469282469, 8.628378469282469, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 32.475, 3.5, 12.8)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 32.6, 3.5, 12.5)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 32.6, 3.375, 12.8)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 32.6, 3.625, 12.8)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 22135.15025)
    ops.uniaxialMaterial('Elastic', 404012, 44471.5055)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4013, 0.0, 7.0, 12.8, '-mass', 8.628378469282467, 8.628378469282467, 8.628378469282467, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 7.0, 12.8)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 7.0, 12.5)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 6.875, 12.8)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 7.125, 12.8)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304013, 22135.15025)
    ops.uniaxialMaterial('Elastic', 404013, 44471.5055)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4014, 7.4, 7.0, 12.8, '-mass', 16.733209537953314, 16.733209537953314, 16.733209537953314, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 7.225, 7.0, 12.8)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 7.575, 7.0, 12.8)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 7.4, 7.0, 12.5)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 7.4, 6.825, 12.8)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 7.4, 7.175, 12.8)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304014, 35466.717)
    ops.uniaxialMaterial('Elastic', 404014, 77166.31635)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4015, 14.8, 7.0, 12.8, '-mass', 11.680232097591032, 11.680232097591032, 11.680232097591032, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 14.675, 7.0, 12.8)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 14.925, 7.0, 12.8)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 14.8, 7.0, 12.5)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 14.8, 6.875, 12.8)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 14.8, 7.125, 12.8)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304015, 23710.64095)
    ops.uniaxialMaterial('Elastic', 404015, 47312.7223)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4016, 17.8, 7.0, 12.8, '-mass', 11.68023209759103, 11.68023209759103, 11.68023209759103, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 17.675, 7.0, 12.8)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(34016, 17.925, 7.0, 12.8)
    ops.element('elasticBeamColumn', 34016, 4016, 34016, 99999, 88888)
    ops.node(24016, 17.8, 7.0, 12.5)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 17.8, 6.875, 12.8)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 17.8, 7.125, 12.8)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304016, 23710.64095)
    ops.uniaxialMaterial('Elastic', 404016, 47312.7223)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    # Central joint node
    ops.node(4017, 25.2, 7.0, 12.8, '-mass', 16.733209537953314, 16.733209537953314, 16.733209537953314, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54017, 25.025, 7.0, 12.8)
    ops.element('elasticBeamColumn', 54017, 54017, 4017, 99999, 88888)
    ops.node(34017, 25.375, 7.0, 12.8)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 25.2, 7.0, 12.5)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 25.2, 6.825, 12.8)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 25.2, 7.175, 12.8)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304017, 35466.717)
    ops.uniaxialMaterial('Elastic', 404017, 77166.31635)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    # Central joint node
    ops.node(4018, 32.6, 7.0, 12.8, '-mass', 8.628378469282469, 8.628378469282469, 8.628378469282469, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 32.475, 7.0, 12.8)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 32.6, 7.0, 12.5)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 32.6, 6.875, 12.8)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 32.6, 7.125, 12.8)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304018, 22135.15025)
    ops.uniaxialMaterial('Elastic', 404018, 44471.5055)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4019, 0.0, 10.5, 12.8, '-mass', 4.7533329655280845, 4.7533329655280845, 4.7533329655280845, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 0.125, 10.5, 12.8)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 0.0, 10.5, 12.55)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 0.0, 10.375, 12.8)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304019, 15600.29345)
    ops.uniaxialMaterial('Elastic', 404019, 28617.48155)
    ops.section('Aggregator', 14019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404019, 'My', 304019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14019, 4019, 14019, 14019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4020, 7.4, 10.5, 12.8, '-mass', 9.239999264389501, 9.239999264389501, 9.239999264389501, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 7.225, 10.5, 12.8)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(34020, 7.575, 10.5, 12.8)
    ops.element('elasticBeamColumn', 34020, 4020, 34020, 99999, 88888)
    ops.node(24020, 7.4, 10.5, 12.55)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 7.4, 10.325, 12.8)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304020, 29231.79375)
    ops.uniaxialMaterial('Elastic', 404020, 52220.74405)
    ops.section('Aggregator', 14020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404020, 'My', 304020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14020, 4020, 14020, 14020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4021, 14.8, 10.5, 12.8, '-mass', 6.407700146654843, 6.407700146654843, 6.407700146654843, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54021, 14.675, 10.5, 12.8)
    ops.element('elasticBeamColumn', 54021, 54021, 4021, 99999, 88888)
    ops.node(34021, 14.925, 10.5, 12.8)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 14.8, 10.5, 12.55)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 14.8, 10.375, 12.8)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304021, 17599.17865)
    ops.uniaxialMaterial('Elastic', 404021, 31895.9074)
    ops.section('Aggregator', 14021, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404021, 'My', 304021, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14021, 4021, 14021, 14021, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4022, 17.8, 10.5, 12.8, '-mass', 6.407700146654843, 6.407700146654843, 6.407700146654843, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 17.675, 10.5, 12.8)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 17.925, 10.5, 12.8)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 17.8, 10.5, 12.55)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 17.8, 10.375, 12.8)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304022, 17599.17865)
    ops.uniaxialMaterial('Elastic', 404022, 31895.9074)
    ops.section('Aggregator', 14022, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404022, 'My', 304022, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14022, 4022, 14022, 14022, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 4)
    # Central joint node
    ops.node(4023, 25.2, 10.5, 12.8, '-mass', 9.239999264389501, 9.239999264389501, 9.239999264389501, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 25.025, 10.5, 12.8)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 25.375, 10.5, 12.8)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 25.2, 10.5, 12.55)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 25.2, 10.325, 12.8)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304023, 29231.79375)
    ops.uniaxialMaterial('Elastic', 404023, 52220.74405)
    ops.section('Aggregator', 14023, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404023, 'My', 304023, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14023, 4023, 14023, 14023, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 4)
    # Central joint node
    ops.node(4024, 32.6, 10.5, 12.8, '-mass', 4.753332965528085, 4.753332965528085, 4.753332965528085, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 32.475, 10.5, 12.8)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 32.6, 10.5, 12.55)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 32.6, 10.375, 12.8)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304024, 15600.29345)
    ops.uniaxialMaterial('Elastic', 404024, 28617.48155)
    ops.section('Aggregator', 14024, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404024, 'My', 304024, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14024, 4024, 14024, 14024, '-orient', 0, 0, 1, 0, 1, 0)
