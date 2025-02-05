import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (1, 1, 0.5)
    # Central joint node
    ops.node(4017, 7.45, 3.5, 1.3, '-mass', 2.7595183486238533, 2.7595183486238533, 2.7595183486238533, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 7.625, 3.5, 1.3)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 7.45, 3.5, 1.15)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(74017, 7.45, 3.5, 1.45)
    ops.element('elasticBeamColumn', 74017, 4017, 74017, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 1, 0.5)
    # Central joint node
    ops.node(4018, 10.3, 3.5, 1.3, '-mass', 2.7595183486238533, 2.7595183486238533, 2.7595183486238533, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 10.125, 3.5, 1.3)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 10.3, 3.5, 1.15)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(74018, 10.3, 3.5, 1.45)
    ops.element('elasticBeamColumn', 74018, 4018, 74018, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 1, 1.5)
    # Central joint node
    ops.node(4019, 7.45, 3.5, 3.9, '-mass', 2.7595183486238533, 2.7595183486238533, 2.7595183486238533, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 7.625, 3.5, 3.9)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 7.45, 3.5, 3.75)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(74019, 7.45, 3.5, 4.05)
    ops.element('elasticBeamColumn', 74019, 4019, 74019, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 1, 1.5)
    # Central joint node
    ops.node(4020, 10.3, 3.5, 3.9, '-mass', 2.7595183486238533, 2.7595183486238533, 2.7595183486238533, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 10.125, 3.5, 3.9)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 10.3, 3.5, 3.75)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(74020, 10.3, 3.5, 4.05)
    ops.element('elasticBeamColumn', 74020, 4020, 74020, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 1, 2.5)
    # Central joint node
    ops.node(4021, 7.45, 3.5, 6.5, '-mass', 2.568692660550459, 2.568692660550459, 2.568692660550459, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 7.575, 3.5, 6.5)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 7.45, 3.5, 6.35)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(74021, 7.45, 3.5, 6.65)
    ops.element('elasticBeamColumn', 74021, 4021, 74021, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 1, 2.5)
    # Central joint node
    ops.node(4022, 10.3, 3.5, 6.5, '-mass', 2.568692660550459, 2.568692660550459, 2.568692660550459, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 10.175, 3.5, 6.5)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(24022, 10.3, 3.5, 6.35)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(74022, 10.3, 3.5, 6.65)
    ops.element('elasticBeamColumn', 74022, 4022, 74022, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 1, 3.5)
    # Central joint node
    ops.node(4023, 7.45, 3.5, 9.1, '-mass', 2.568692660550459, 2.568692660550459, 2.568692660550459, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34023, 7.575, 3.5, 9.1)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 7.45, 3.5, 8.95)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(74023, 7.45, 3.5, 9.25)
    ops.element('elasticBeamColumn', 74023, 4023, 74023, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 1, 3.5)
    # Central joint node
    ops.node(4024, 10.3, 3.5, 9.1, '-mass', 2.568692660550459, 2.568692660550459, 2.568692660550459, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 10.175, 3.5, 9.1)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 10.3, 3.5, 8.95)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(74024, 10.3, 3.5, 9.25)
    ops.element('elasticBeamColumn', 74024, 4024, 74024, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 2.6, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.125, 0.0, 2.6)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 2.9)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.125, 2.6)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 26235.39605)
    ops.uniaxialMaterial('Elastic', 401001, 55996.2503)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 7.45, 0.0, 2.6, '-mass', 11.72737003058104, 11.72737003058104, 11.72737003058104, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 7.3, 0.0, 2.6)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 7.6, 0.0, 2.6)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 7.45, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 7.45, 0.0, 2.9)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 7.45, 0.15, 2.6)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 38017.26555)
    ops.uniaxialMaterial('Elastic', 401002, 100666.01895)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 10.3, 0.0, 2.6, '-mass', 11.72737003058104, 11.72737003058104, 11.72737003058104, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 10.15, 0.0, 2.6)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 10.45, 0.0, 2.6)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 10.3, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 10.3, 0.0, 2.9)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 10.3, 0.15, 2.6)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 38017.26555)
    ops.uniaxialMaterial('Elastic', 401003, 100666.01895)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 17.75, 0.0, 2.6, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 17.625, 0.0, 2.6)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 17.75, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 17.75, 0.0, 2.9)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 17.75, 0.125, 2.6)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 26235.39605)
    ops.uniaxialMaterial('Elastic', 401004, 55996.2503)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 3.5, 2.6, '-mass', 12.780377166156981, 12.780377166156981, 12.780377166156981, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.15, 3.5, 2.6)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 3.5, 2.3)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 3.5, 2.9)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 3.35, 2.6)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 3.65, 2.6)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 53990.59615)
    ops.uniaxialMaterial('Elastic', 401005, 81493.80885)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 7.45, 3.5, 2.6, '-mass', 13.437538226299695, 13.437538226299695, 13.437538226299695, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 7.275, 3.5, 2.6)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 7.625, 3.5, 2.6)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 7.45, 3.5, 2.3)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 7.45, 3.5, 2.9)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 7.45, 3.325, 2.6)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 7.45, 3.675, 2.6)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 84286.38905)
    ops.uniaxialMaterial('Elastic', 401006, 180436.1835)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 10.3, 3.5, 2.6, '-mass', 13.437538226299692, 13.437538226299692, 13.437538226299692, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 10.125, 3.5, 2.6)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 10.475, 3.5, 2.6)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 10.3, 3.5, 2.3)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 10.3, 3.5, 2.9)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 10.3, 3.325, 2.6)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 10.3, 3.675, 2.6)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 84286.38905)
    ops.uniaxialMaterial('Elastic', 401007, 180436.1835)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 17.75, 3.5, 2.6, '-mass', 12.78037716615698, 12.78037716615698, 12.78037716615698, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 17.6, 3.5, 2.6)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 17.75, 3.5, 2.3)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 17.75, 3.5, 2.9)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 17.75, 3.35, 2.6)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 17.75, 3.65, 2.6)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 53990.59615)
    ops.uniaxialMaterial('Elastic', 401008, 81493.80885)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 7.0, 2.6, '-mass', 12.780377166156981, 12.780377166156981, 12.780377166156981, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.15, 7.0, 2.6)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 7.0, 2.3)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 7.0, 2.9)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 6.85, 2.6)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 7.15, 2.6)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 54085.25565)
    ops.uniaxialMaterial('Elastic', 401009, 81625.9272)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 7.45, 7.0, 2.6, '-mass', 15.272744648318042, 15.272744648318042, 15.272744648318042, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 7.3, 7.0, 2.6)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 7.6, 7.0, 2.6)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 7.45, 7.0, 2.3)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 7.45, 7.0, 2.9)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 7.45, 6.85, 2.6)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 7.45, 7.15, 2.6)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 68894.922)
    ops.uniaxialMaterial('Elastic', 401010, 119678.89815)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 10.3, 7.0, 2.6, '-mass', 15.27274464831804, 15.27274464831804, 15.27274464831804, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 10.15, 7.0, 2.6)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 10.45, 7.0, 2.6)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 10.3, 7.0, 2.3)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 10.3, 7.0, 2.9)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 10.3, 6.85, 2.6)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 10.3, 7.15, 2.6)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 68894.922)
    ops.uniaxialMaterial('Elastic', 401011, 119678.89815)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 17.75, 7.0, 2.6, '-mass', 12.78037716615698, 12.78037716615698, 12.78037716615698, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 17.6, 7.0, 2.6)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 17.75, 7.0, 2.3)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 17.75, 7.0, 2.9)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 17.75, 6.85, 2.6)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 17.75, 7.15, 2.6)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 54085.25565)
    ops.uniaxialMaterial('Elastic', 401012, 81625.9272)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1013, 0.0, 10.5, 2.6, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.125, 10.5, 2.6)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 10.5, 2.3)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 10.5, 2.9)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 10.375, 2.6)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301013, 26235.39605)
    ops.uniaxialMaterial('Elastic', 401013, 55996.2503)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1014, 7.45, 10.5, 2.6, '-mass', 11.72737003058104, 11.72737003058104, 11.72737003058104, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 7.3, 10.5, 2.6)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 7.6, 10.5, 2.6)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 7.45, 10.5, 2.3)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 7.45, 10.5, 2.9)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 7.45, 10.35, 2.6)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301014, 38017.26555)
    ops.uniaxialMaterial('Elastic', 401014, 100666.01895)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1015, 10.3, 10.5, 2.6, '-mass', 11.72737003058104, 11.72737003058104, 11.72737003058104, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 10.15, 10.5, 2.6)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 10.45, 10.5, 2.6)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 10.3, 10.5, 2.3)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 10.3, 10.5, 2.9)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 10.3, 10.35, 2.6)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301015, 38017.26555)
    ops.uniaxialMaterial('Elastic', 401015, 100666.01895)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1016, 17.75, 10.5, 2.6, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 17.625, 10.5, 2.6)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 17.75, 10.5, 2.3)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 17.75, 10.5, 2.9)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 17.75, 10.375, 2.6)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301016, 26235.39605)
    ops.uniaxialMaterial('Elastic', 401016, 55996.2503)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 5.2, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.125, 0.0, 5.2)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 4.9)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 5.5)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.125, 5.2)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 22521.22595)
    ops.uniaxialMaterial('Elastic', 402001, 48463.8064)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 7.45, 0.0, 5.2, '-mass', 11.59709480122324, 11.59709480122324, 11.59709480122324, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 7.3, 0.0, 5.2)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 7.6, 0.0, 5.2)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 7.45, 0.0, 4.9)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 7.45, 0.0, 5.5)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 7.45, 0.15, 5.2)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 27235.03855)
    ops.uniaxialMaterial('Elastic', 402002, 85743.18055)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 10.3, 0.0, 5.2, '-mass', 11.59709480122324, 11.59709480122324, 11.59709480122324, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 10.15, 0.0, 5.2)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 10.45, 0.0, 5.2)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 10.3, 0.0, 4.9)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 10.3, 0.0, 5.5)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 10.3, 0.15, 5.2)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 27235.03855)
    ops.uniaxialMaterial('Elastic', 402003, 85743.18055)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 17.75, 0.0, 5.2, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 17.625, 0.0, 5.2)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 17.75, 0.0, 4.9)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 17.75, 0.0, 5.5)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 17.75, 0.125, 5.2)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 22521.22595)
    ops.uniaxialMaterial('Elastic', 402004, 48463.8064)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 3.5, 5.2, '-mass', 12.692915392456674, 12.692915392456674, 12.692915392456674, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.15, 3.5, 5.2)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 3.5, 4.9)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 3.5, 5.5)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 3.35, 5.2)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 3.65, 5.2)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 46126.51335)
    ops.uniaxialMaterial('Elastic', 402005, 70513.79845)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 7.45, 3.5, 5.2, '-mass', 13.256498470948012, 13.256498470948012, 13.256498470948012, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 7.275, 3.5, 5.2)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 7.625, 3.5, 5.2)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 7.45, 3.5, 4.9)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 7.45, 3.5, 5.5)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 7.45, 3.325, 5.2)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 7.45, 3.675, 5.2)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 59319.4555)
    ops.uniaxialMaterial('Elastic', 402006, 154055.6867)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 10.3, 3.5, 5.2, '-mass', 13.256498470948008, 13.256498470948008, 13.256498470948008, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 10.125, 3.5, 5.2)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 10.475, 3.5, 5.2)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 10.3, 3.5, 4.9)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 10.3, 3.5, 5.5)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 10.3, 3.325, 5.2)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 10.3, 3.675, 5.2)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 59319.4555)
    ops.uniaxialMaterial('Elastic', 402007, 154055.6867)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 17.75, 3.5, 5.2, '-mass', 12.692915392456673, 12.692915392456673, 12.692915392456673, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 17.6, 3.5, 5.2)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 17.75, 3.5, 4.9)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 17.75, 3.5, 5.5)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 17.75, 3.35, 5.2)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 17.75, 3.65, 5.2)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 46126.51335)
    ops.uniaxialMaterial('Elastic', 402008, 70513.79845)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 7.0, 5.2, '-mass', 12.780377166156981, 12.780377166156981, 12.780377166156981, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.15, 7.0, 5.2)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 7.0, 4.9)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 7.0, 5.5)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 6.85, 5.2)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 7.15, 5.2)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 46237.27545)
    ops.uniaxialMaterial('Elastic', 402009, 70668.5102)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 7.45, 7.0, 5.2, '-mass', 15.09965596330275, 15.09965596330275, 15.09965596330275, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 7.3, 7.0, 5.2)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 7.6, 7.0, 5.2)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 7.45, 7.0, 4.9)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 7.45, 7.0, 5.5)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 7.45, 6.85, 5.2)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 7.45, 7.15, 5.2)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 49954.52775)
    ops.uniaxialMaterial('Elastic', 402010, 102967.8721)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 10.3, 7.0, 5.2, '-mass', 15.099655963302748, 15.099655963302748, 15.099655963302748, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 10.15, 7.0, 5.2)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 10.45, 7.0, 5.2)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 10.3, 7.0, 4.9)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 10.3, 7.0, 5.5)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 10.3, 6.85, 5.2)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 10.3, 7.15, 5.2)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 49954.52775)
    ops.uniaxialMaterial('Elastic', 402011, 102967.8721)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 17.75, 7.0, 5.2, '-mass', 12.78037716615698, 12.78037716615698, 12.78037716615698, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 17.6, 7.0, 5.2)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 17.75, 7.0, 4.9)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 17.75, 7.0, 5.5)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 17.75, 6.85, 5.2)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 17.75, 7.15, 5.2)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 46237.27545)
    ops.uniaxialMaterial('Elastic', 402012, 70668.5102)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2013, 0.0, 10.5, 5.2, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.125, 10.5, 5.2)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 10.5, 4.9)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 10.5, 5.5)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 10.375, 5.2)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302013, 22521.22595)
    ops.uniaxialMaterial('Elastic', 402013, 48463.8064)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2014, 7.45, 10.5, 5.2, '-mass', 11.59709480122324, 11.59709480122324, 11.59709480122324, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 7.3, 10.5, 5.2)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 7.6, 10.5, 5.2)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 7.45, 10.5, 4.9)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 7.45, 10.5, 5.5)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 7.45, 10.35, 5.2)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302014, 27235.03855)
    ops.uniaxialMaterial('Elastic', 402014, 85743.18055)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2015, 10.3, 10.5, 5.2, '-mass', 11.59709480122324, 11.59709480122324, 11.59709480122324, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 10.15, 10.5, 5.2)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 10.45, 10.5, 5.2)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 10.3, 10.5, 4.9)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 10.3, 10.5, 5.5)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 10.3, 10.35, 5.2)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302015, 27235.03855)
    ops.uniaxialMaterial('Elastic', 402015, 85743.18055)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2016, 17.75, 10.5, 5.2, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 17.625, 10.5, 5.2)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 17.75, 10.5, 4.9)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 17.75, 10.5, 5.5)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 17.75, 10.375, 5.2)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302016, 22521.22595)
    ops.uniaxialMaterial('Elastic', 402016, 48463.8064)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 7.8, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 7.8)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 7.5)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 8.1)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 7.8)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 17993.3801)
    ops.uniaxialMaterial('Elastic', 403001, 39298.1479)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 7.45, 0.0, 7.8, '-mass', 11.509633027522934, 11.509633027522934, 11.509633027522934, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 7.325, 0.0, 7.8)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 7.575, 0.0, 7.8)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 7.45, 0.0, 7.5)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 7.45, 0.0, 8.1)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 7.45, 0.125, 7.8)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 19932.3132)
    ops.uniaxialMaterial('Elastic', 403002, 55999.2725)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 10.3, 0.0, 7.8, '-mass', 11.509633027522934, 11.509633027522934, 11.509633027522934, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 10.175, 0.0, 7.8)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 10.425, 0.0, 7.8)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 10.3, 0.0, 7.5)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 10.3, 0.0, 8.1)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 10.3, 0.125, 7.8)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 19932.3132)
    ops.uniaxialMaterial('Elastic', 403003, 55999.2725)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 17.75, 0.0, 7.8, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 17.625, 0.0, 7.8)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 17.75, 0.0, 7.5)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 17.75, 0.0, 8.1)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 17.75, 0.125, 7.8)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 17993.3801)
    ops.uniaxialMaterial('Elastic', 403004, 39298.1479)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 3.5, 7.8, '-mass', 12.605453618756368, 12.605453618756368, 12.605453618756368, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.125, 3.5, 7.8)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 3.5, 7.5)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 3.5, 8.1)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 3.375, 7.8)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 3.625, 7.8)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 33306.22485)
    ops.uniaxialMaterial('Elastic', 403005, 47572.09835)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 7.45, 3.5, 7.8, '-mass', 13.161085626911314, 13.161085626911314, 13.161085626911314, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 7.325, 3.5, 7.8)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 7.575, 3.5, 7.8)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 7.45, 3.5, 7.5)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 7.45, 3.5, 8.1)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 7.45, 3.375, 7.8)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 7.45, 3.625, 7.8)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 39245.48725)
    ops.uniaxialMaterial('Elastic', 403006, 85760.3519)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 10.3, 3.5, 7.8, '-mass', 13.16108562691131, 13.16108562691131, 13.16108562691131, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 10.175, 3.5, 7.8)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 10.425, 3.5, 7.8)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 10.3, 3.5, 7.5)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 10.3, 3.5, 8.1)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 10.3, 3.375, 7.8)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 10.3, 3.625, 7.8)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 39245.48725)
    ops.uniaxialMaterial('Elastic', 403007, 85760.3519)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 17.75, 3.5, 7.8, '-mass', 12.605453618756366, 12.605453618756366, 12.605453618756366, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 17.625, 3.5, 7.8)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 17.75, 3.5, 7.5)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 17.75, 3.5, 8.1)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 17.75, 3.375, 7.8)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 17.75, 3.625, 7.8)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 33306.22485)
    ops.uniaxialMaterial('Elastic', 403008, 47572.09835)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 7.0, 7.8, '-mass', 12.780377166156981, 12.780377166156981, 12.780377166156981, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.15, 7.0, 7.8)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 7.0, 7.5)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 7.0, 8.1)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 6.85, 7.8)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 7.15, 7.8)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 36749.9171)
    ops.uniaxialMaterial('Elastic', 403009, 57406.9904)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 7.45, 7.0, 7.8, '-mass', 15.012194189602443, 15.012194189602443, 15.012194189602443, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 7.325, 7.0, 7.8)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 7.575, 7.0, 7.8)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 7.45, 7.0, 7.5)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 7.45, 7.0, 8.1)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 7.45, 6.875, 7.8)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 7.45, 7.125, 7.8)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 36697.9013)
    ops.uniaxialMaterial('Elastic', 403010, 68880.4981)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 10.3, 7.0, 7.8, '-mass', 15.012194189602441, 15.012194189602441, 15.012194189602441, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 10.175, 7.0, 7.8)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 10.425, 7.0, 7.8)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 10.3, 7.0, 7.5)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 10.3, 7.0, 8.1)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 10.3, 6.875, 7.8)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 10.3, 7.125, 7.8)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 36697.9013)
    ops.uniaxialMaterial('Elastic', 403011, 68880.4981)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 17.75, 7.0, 7.8, '-mass', 12.78037716615698, 12.78037716615698, 12.78037716615698, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 17.6, 7.0, 7.8)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 17.75, 7.0, 7.5)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 17.75, 7.0, 8.1)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 17.75, 6.85, 7.8)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 17.75, 7.15, 7.8)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 36749.9171)
    ops.uniaxialMaterial('Elastic', 403012, 57406.9904)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3013, 0.0, 10.5, 7.8, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 10.5, 7.8)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 10.5, 7.5)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 10.5, 8.1)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 10.375, 7.8)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303013, 17993.3801)
    ops.uniaxialMaterial('Elastic', 403013, 39298.1479)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3014, 7.45, 10.5, 7.8, '-mass', 11.509633027522934, 11.509633027522934, 11.509633027522934, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 7.325, 10.5, 7.8)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 7.575, 10.5, 7.8)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 7.45, 10.5, 7.5)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 7.45, 10.5, 8.1)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 7.45, 10.375, 7.8)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303014, 19932.3132)
    ops.uniaxialMaterial('Elastic', 403014, 55999.2725)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3015, 10.3, 10.5, 7.8, '-mass', 11.509633027522934, 11.509633027522934, 11.509633027522934, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 10.175, 10.5, 7.8)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 10.425, 10.5, 7.8)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 10.3, 10.5, 7.5)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 10.3, 10.5, 8.1)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 10.3, 10.375, 7.8)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303015, 19932.3132)
    ops.uniaxialMaterial('Elastic', 403015, 55999.2725)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3016, 17.75, 10.5, 7.8, '-mass', 9.842991845056062, 9.842991845056062, 9.842991845056062, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 17.625, 10.5, 7.8)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 17.75, 10.5, 7.5)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 17.75, 10.5, 8.1)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 17.75, 10.375, 7.8)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303016, 17993.3801)
    ops.uniaxialMaterial('Elastic', 403016, 39298.1479)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 10.4, '-mass', 4.837563710499491, 4.837563710499491, 4.837563710499491, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 10.4)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 10.15)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 10.4)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 16663.0955)
    ops.uniaxialMaterial('Elastic', 404001, 30683.4174)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 7.45, 0.0, 10.4, '-mass', 6.39184505606524, 6.39184505606524, 6.39184505606524, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 7.325, 0.0, 10.4)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 7.575, 0.0, 10.4)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 7.45, 0.0, 10.15)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 7.45, 0.125, 10.4)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 18626.89725)
    ops.uniaxialMaterial('Elastic', 404002, 33899.58945)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 10.3, 0.0, 10.4, '-mass', 6.391845056065239, 6.391845056065239, 6.391845056065239, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 10.175, 0.0, 10.4)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 10.425, 0.0, 10.4)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 10.3, 0.0, 10.15)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 10.3, 0.125, 10.4)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 18626.89725)
    ops.uniaxialMaterial('Elastic', 404003, 33899.58945)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 17.75, 0.0, 10.4, '-mass', 4.83756371049949, 4.83756371049949, 4.83756371049949, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 17.625, 0.0, 10.4)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 17.75, 0.0, 10.15)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 17.75, 0.125, 10.4)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 16663.0955)
    ops.uniaxialMaterial('Elastic', 404004, 30683.4174)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 3.5, 10.4, '-mass', 8.701732925586134, 8.701732925586134, 8.701732925586134, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.125, 3.5, 10.4)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 3.5, 10.125)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 3.375, 10.4)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 3.625, 10.4)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 23527.0298)
    ops.uniaxialMaterial('Elastic', 404005, 42697.04175)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 7.45, 3.5, 10.4, '-mass', 10.296075433231394, 10.296075433231394, 10.296075433231394, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 7.325, 3.5, 10.4)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 7.575, 3.5, 10.4)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 7.45, 3.5, 10.125)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 7.45, 3.375, 10.4)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 7.45, 3.625, 10.4)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 23751.9281)
    ops.uniaxialMaterial('Elastic', 404006, 43069.5718)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 10.3, 3.5, 10.4, '-mass', 10.296075433231394, 10.296075433231394, 10.296075433231394, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 10.175, 3.5, 10.4)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 10.425, 3.5, 10.4)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 10.3, 3.5, 10.125)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 10.3, 3.375, 10.4)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 10.3, 3.625, 10.4)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 23751.9281)
    ops.uniaxialMaterial('Elastic', 404007, 43069.5718)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 17.75, 3.5, 10.4, '-mass', 8.701732925586134, 8.701732925586134, 8.701732925586134, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 17.625, 3.5, 10.4)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 17.75, 3.5, 10.125)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 17.75, 3.375, 10.4)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 17.75, 3.625, 10.4)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 23527.0298)
    ops.uniaxialMaterial('Elastic', 404008, 42697.04175)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 7.0, 10.4, '-mass', 8.78919469928644, 8.78919469928644, 8.78919469928644, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.15, 7.0, 10.4)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 7.0, 10.125)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 6.85, 10.4)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 7.15, 10.4)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 25734.61045)
    ops.uniaxialMaterial('Elastic', 404009, 51825.134)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 7.45, 7.0, 10.4, '-mass', 12.047795616717632, 12.047795616717632, 12.047795616717632, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 7.325, 7.0, 10.4)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 7.575, 7.0, 10.4)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 7.45, 7.0, 10.125)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 7.45, 6.875, 10.4)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 7.45, 7.125, 10.4)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 27397.10955)
    ops.uniaxialMaterial('Elastic', 404010, 49117.2363)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 10.3, 7.0, 10.4, '-mass', 12.047795616717632, 12.047795616717632, 12.047795616717632, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 10.175, 7.0, 10.4)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 10.425, 7.0, 10.4)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 10.3, 7.0, 10.125)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 10.3, 6.875, 10.4)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 10.3, 7.125, 10.4)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 27397.10955)
    ops.uniaxialMaterial('Elastic', 404011, 49117.2363)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 17.75, 7.0, 10.4, '-mass', 8.78919469928644, 8.78919469928644, 8.78919469928644, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 17.6, 7.0, 10.4)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 17.75, 7.0, 10.125)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 17.75, 6.85, 10.4)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 17.75, 7.15, 10.4)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 25734.61045)
    ops.uniaxialMaterial('Elastic', 404012, 51825.134)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4013, 0.0, 10.5, 10.4, '-mass', 4.837563710499491, 4.837563710499491, 4.837563710499491, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 10.5, 10.4)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 10.5, 10.15)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 10.375, 10.4)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304013, 16663.0955)
    ops.uniaxialMaterial('Elastic', 404013, 30683.4174)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4014, 7.45, 10.5, 10.4, '-mass', 6.39184505606524, 6.39184505606524, 6.39184505606524, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 7.325, 10.5, 10.4)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 7.575, 10.5, 10.4)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 7.45, 10.5, 10.15)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 7.45, 10.375, 10.4)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304014, 18626.89725)
    ops.uniaxialMaterial('Elastic', 404014, 33899.58945)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4015, 10.3, 10.5, 10.4, '-mass', 6.391845056065239, 6.391845056065239, 6.391845056065239, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 10.175, 10.5, 10.4)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 10.425, 10.5, 10.4)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 10.3, 10.5, 10.15)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 10.3, 10.375, 10.4)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304015, 18626.89725)
    ops.uniaxialMaterial('Elastic', 404015, 33899.58945)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4016, 17.75, 10.5, 10.4, '-mass', 4.83756371049949, 4.83756371049949, 4.83756371049949, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 17.625, 10.5, 10.4)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 17.75, 10.5, 10.15)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 17.75, 10.375, 10.4)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304016, 16663.0955)
    ops.uniaxialMaterial('Elastic', 404016, 30683.4174)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)
