import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 0.5)
    # Central joint node
    ops.node(4021, 0.0, 0.0, 1.575, '-mass', 3.079020132517839, 3.079020132517839, 3.079020132517839, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 0.125, 0.0, 1.575)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 0.0, 0.0, 1.375)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(74021, 0.0, 0.0, 1.775)
    ops.element('elasticBeamColumn', 74021, 4021, 74021, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 0.5)
    # Central joint node
    ops.node(4022, 3.05, 0.0, 1.575, '-mass', 3.618469673802242, 3.618469673802242, 3.618469673802242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 2.825, 0.0, 1.575)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(24022, 3.05, 0.0, 1.375)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(74022, 3.05, 0.0, 1.775)
    ops.element('elasticBeamColumn', 74022, 4022, 74022, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 1.5)
    # Central joint node
    ops.node(4023, 0.0, 0.0, 4.725, '-mass', 3.079020132517839, 3.079020132517839, 3.079020132517839, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34023, 0.125, 0.0, 4.725)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 0.0, 0.0, 4.525)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(74023, 0.0, 0.0, 4.925)
    ops.element('elasticBeamColumn', 74023, 4023, 74023, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    # Central joint node
    ops.node(4024, 3.05, 0.0, 4.725, '-mass', 3.618469673802242, 3.618469673802242, 3.618469673802242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 2.825, 0.0, 4.725)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 3.05, 0.0, 4.525)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(74024, 3.05, 0.0, 4.925)
    ops.element('elasticBeamColumn', 74024, 4024, 74024, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 2.5)
    # Central joint node
    ops.node(4025, 0.0, 0.0, 7.875, '-mass', 3.079020132517839, 3.079020132517839, 3.079020132517839, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 0.125, 0.0, 7.875)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 0.0, 0.0, 7.675)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 0.0, 0.0, 8.075)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    # Central joint node
    ops.node(4026, 3.05, 0.0, 7.875, '-mass', 3.3102127930682967, 3.3102127930682967, 3.3102127930682967, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 2.875, 0.0, 7.875)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 3.05, 0.0, 7.675)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 3.05, 0.0, 8.075)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 3.5)
    # Central joint node
    ops.node(4027, 0.0, 0.0, 11.025, '-mass', 3.079020132517839, 3.079020132517839, 3.079020132517839, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34027, 0.125, 0.0, 11.025)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 0.0, 0.0, 10.825)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(74027, 0.0, 0.0, 11.225)
    ops.element('elasticBeamColumn', 74027, 4027, 74027, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 3.5)
    # Central joint node
    ops.node(4028, 3.05, 0.0, 11.025, '-mass', 3.310212793068297, 3.310212793068297, 3.310212793068297, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 2.875, 0.0, 11.025)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 3.05, 0.0, 10.825)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(74028, 3.05, 0.0, 11.225)
    ops.element('elasticBeamColumn', 74028, 4028, 74028, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.15, '-mass', 2.977166156982671, 2.977166156982671, 2.977166156982671, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.125, 0.0, 3.15)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.85)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.45)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.125, 3.15)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 37001.0368)
    ops.uniaxialMaterial('Elastic', 401001, 46907.62815)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 3.05, 0.0, 3.15, '-mass', 13.063798419979612, 13.063798419979612, 13.063798419979612, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 2.825, 0.0, 3.15)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 3.275, 0.0, 3.15)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 3.05, 0.0, 2.85)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 3.05, 0.0, 3.45)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 3.05, 0.225, 3.15)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 105923.1152)
    ops.uniaxialMaterial('Elastic', 401002, 191930.4933)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 9.0, 0.0, 3.15, '-mass', 21.26256116207951, 21.26256116207951, 21.26256116207951, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 8.75, 0.0, 3.15)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 9.25, 0.0, 3.15)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 9.0, 0.0, 2.85)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 9.0, 0.0, 3.45)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 9.0, 0.25, 3.15)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 115712.4847)
    ops.uniaxialMaterial('Elastic', 401003, 202666.0218)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 14.95, 0.0, 3.15, '-mass', 12.323278542303772, 12.323278542303772, 12.323278542303772, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 14.775, 0.0, 3.15)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 14.95, 0.0, 2.85)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 14.95, 0.0, 3.45)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 14.95, 0.175, 3.15)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 60784.53115)
    ops.uniaxialMaterial('Elastic', 401004, 76219.58255)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 3.95, 3.15, '-mass', 10.236990316004078, 10.236990316004078, 10.236990316004078, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.175, 3.95, 3.15)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 3.95, 2.8)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 3.95, 3.5)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 3.775, 3.15)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 4.125, 3.15)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 72064.1733)
    ops.uniaxialMaterial('Elastic', 401005, 89767.91125)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 3.05, 3.95, 3.15, '-mass', 23.385280326197755, 23.385280326197755, 23.385280326197755, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 2.8, 3.95, 3.15)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 3.3, 3.95, 3.15)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 3.05, 3.95, 2.8)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 3.05, 3.95, 3.5)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 3.05, 3.7, 3.15)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 3.05, 4.2, 3.15)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 172021.78025)
    ops.uniaxialMaterial('Elastic', 401006, 255934.84375)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 9.0, 3.95, 3.15, '-mass', 29.96436799184505, 29.96436799184505, 29.96436799184505, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 8.725, 3.95, 3.15)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 9.275, 3.95, 3.15)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 9.0, 3.95, 2.8)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 9.0, 3.95, 3.5)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 9.0, 3.675, 3.15)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 9.0, 4.225, 3.15)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 215884.32595)
    ops.uniaxialMaterial('Elastic', 401007, 313669.0677)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 14.95, 3.95, 3.15, '-mass', 18.79966615698267, 18.79966615698267, 18.79966615698267, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 14.725, 3.95, 3.15)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 14.95, 3.95, 2.8)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 14.95, 3.95, 3.5)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 14.95, 3.725, 3.15)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 14.95, 4.175, 3.15)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 142185.25065)
    ops.uniaxialMaterial('Elastic', 401008, 152992.14675)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 7.9, 3.15, '-mass', 10.718896534148827, 10.718896534148827, 10.718896534148827, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.175, 7.9, 3.15)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 7.9, 2.8)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 7.9, 3.5)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 7.725, 3.15)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 8.075, 3.15)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 71574.35455)
    ops.uniaxialMaterial('Elastic', 401009, 89212.9876)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 3.05, 7.9, 3.15, '-mass', 22.457910295616717, 22.457910295616717, 22.457910295616717, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 2.8, 7.9, 3.15)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 3.3, 7.9, 3.15)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 3.05, 7.9, 2.8)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 3.05, 7.9, 3.5)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 3.05, 7.65, 3.15)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 3.05, 8.15, 3.15)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 169068.15725)
    ops.uniaxialMaterial('Elastic', 401010, 251540.4291)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 9.0, 7.9, 3.15, '-mass', 29.96436799184505, 29.96436799184505, 29.96436799184505, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 8.725, 7.9, 3.15)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 9.275, 7.9, 3.15)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 9.0, 7.9, 2.8)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 9.0, 7.9, 3.5)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 9.0, 7.625, 3.15)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 9.0, 8.175, 3.15)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 215884.32595)
    ops.uniaxialMaterial('Elastic', 401011, 313669.0677)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 14.95, 7.9, 3.15, '-mass', 18.79966615698267, 18.79966615698267, 18.79966615698267, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 14.725, 7.9, 3.15)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 14.95, 7.9, 2.8)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 14.95, 7.9, 3.5)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 14.95, 7.675, 3.15)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 14.95, 8.125, 3.15)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 142185.25065)
    ops.uniaxialMaterial('Elastic', 401012, 152992.14675)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1013, 0.0, 11.85, 3.15, '-mass', 10.71889653414883, 10.71889653414883, 10.71889653414883, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.175, 11.85, 3.15)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 11.85, 2.8)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 11.85, 3.5)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 11.675, 3.15)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 12.025, 3.15)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301013, 71574.35455)
    ops.uniaxialMaterial('Elastic', 401013, 89212.9876)
    ops.section('Aggregator', 11013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401013, 'My', 301013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11013, 1013, 11013, 11013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1014, 3.05, 11.85, 3.15, '-mass', 22.457910295616717, 22.457910295616717, 22.457910295616717, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 2.8, 11.85, 3.15)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 3.3, 11.85, 3.15)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 3.05, 11.85, 2.8)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 3.05, 11.85, 3.5)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 3.05, 11.6, 3.15)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 3.05, 12.1, 3.15)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301014, 169068.15725)
    ops.uniaxialMaterial('Elastic', 401014, 251540.4291)
    ops.section('Aggregator', 11014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401014, 'My', 301014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11014, 1014, 11014, 11014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1015, 9.0, 11.85, 3.15, '-mass', 29.96436799184505, 29.96436799184505, 29.96436799184505, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 8.725, 11.85, 3.15)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 9.275, 11.85, 3.15)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 9.0, 11.85, 2.8)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 9.0, 11.85, 3.5)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 9.0, 11.575, 3.15)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 9.0, 12.125, 3.15)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301015, 215884.32595)
    ops.uniaxialMaterial('Elastic', 401015, 313669.0677)
    ops.section('Aggregator', 11015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401015, 'My', 301015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11015, 1015, 11015, 11015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1016, 14.95, 11.85, 3.15, '-mass', 18.79966615698267, 18.79966615698267, 18.79966615698267, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 14.725, 11.85, 3.15)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 14.95, 11.85, 2.8)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 14.95, 11.85, 3.5)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 14.95, 11.625, 3.15)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 14.95, 12.075, 3.15)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301016, 142185.25065)
    ops.uniaxialMaterial('Elastic', 401016, 152992.14675)
    ops.section('Aggregator', 11016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401016, 'My', 301016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11016, 1016, 11016, 11016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 1)
    # Central joint node
    ops.node(1017, 0.0, 15.8, 3.15, '-mass', 6.995635830784914, 6.995635830784914, 6.995635830784914, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31017, 0.15, 15.8, 3.15)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 0.0, 15.8, 2.85)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 0.0, 15.8, 3.45)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 0.0, 15.65, 3.15)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301017, 37529.97575)
    ops.uniaxialMaterial('Elastic', 401017, 49453.60705)
    ops.section('Aggregator', 11017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401017, 'My', 301017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11017, 1017, 11017, 11017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 1)
    # Central joint node
    ops.node(1018, 3.05, 15.8, 3.15, '-mass', 15.672991845056064, 15.672991845056064, 15.672991845056064, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 2.85, 15.8, 3.15)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(31018, 3.25, 15.8, 3.15)
    ops.element('elasticBeamColumn', 31018, 1018, 31018, 99999, 88888)
    ops.node(21018, 3.05, 15.8, 2.85)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 3.05, 15.8, 3.45)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 3.05, 15.6, 3.15)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301018, 80282.45415)
    ops.uniaxialMaterial('Elastic', 401018, 139314.76305)
    ops.section('Aggregator', 11018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401018, 'My', 301018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11018, 1018, 11018, 11018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 1)
    # Central joint node
    ops.node(1019, 9.0, 15.8, 3.15, '-mass', 21.26256116207951, 21.26256116207951, 21.26256116207951, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51019, 8.75, 15.8, 3.15)
    ops.element('elasticBeamColumn', 51019, 51019, 1019, 99999, 88888)
    ops.node(31019, 9.25, 15.8, 3.15)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 9.0, 15.8, 2.85)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 9.0, 15.8, 3.45)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 9.0, 15.55, 3.15)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301019, 115712.4847)
    ops.uniaxialMaterial('Elastic', 401019, 202666.0218)
    ops.section('Aggregator', 11019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401019, 'My', 301019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11019, 1019, 11019, 11019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 1)
    # Central joint node
    ops.node(1020, 14.95, 15.8, 3.15, '-mass', 12.323278542303772, 12.323278542303772, 12.323278542303772, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 14.775, 15.8, 3.15)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(21020, 14.95, 15.8, 2.85)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 14.95, 15.8, 3.45)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 14.95, 15.625, 3.15)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301020, 60784.53115)
    ops.uniaxialMaterial('Elastic', 401020, 76219.58255)
    ops.section('Aggregator', 11020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401020, 'My', 301020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11020, 1020, 11020, 11020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 6.3, '-mass', 2.977166156982671, 2.977166156982671, 2.977166156982671, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.125, 0.0, 6.3)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 6.0)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.6)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.125, 6.3)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 31759.72475)
    ops.uniaxialMaterial('Elastic', 402001, 40338.4876)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 3.05, 0.0, 6.3, '-mass', 12.788874872579001, 12.788874872579001, 12.788874872579001, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 2.825, 0.0, 6.3)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 3.275, 0.0, 6.3)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 3.05, 0.0, 6.0)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 3.05, 0.0, 6.6)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 3.05, 0.225, 6.3)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 90537.87235)
    ops.uniaxialMaterial('Elastic', 402002, 162708.8553)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 9.0, 0.0, 6.3, '-mass', 20.855374617737002, 20.855374617737002, 20.855374617737002, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 8.75, 0.0, 6.3)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 9.25, 0.0, 6.3)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 9.0, 0.0, 6.0)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 9.0, 0.0, 6.6)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 9.0, 0.25, 6.3)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 87590.3646)
    ops.uniaxialMaterial('Elastic', 402003, 172872.75725)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 14.95, 0.0, 6.3, '-mass', 12.031688328236493, 12.031688328236493, 12.031688328236493, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 14.775, 0.0, 6.3)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 14.95, 0.0, 6.0)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 14.95, 0.0, 6.6)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 14.95, 0.175, 6.3)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 45929.2676)
    ops.uniaxialMaterial('Elastic', 402004, 65636.65565)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 3.95, 6.3, '-mass', 10.00579765545362, 10.00579765545362, 10.00579765545362, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.175, 3.95, 6.3)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 3.95, 5.95)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 3.95, 6.65)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 3.775, 6.3)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 4.125, 6.3)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 61956.8031)
    ops.uniaxialMaterial('Elastic', 402005, 78315.2801)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 3.05, 3.95, 6.3, '-mass', 22.79690112130479, 22.79690112130479, 22.79690112130479, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 2.8, 3.95, 6.3)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 3.3, 3.95, 6.3)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 3.05, 3.95, 5.95)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 3.05, 3.95, 6.65)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 3.05, 3.7, 6.3)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 3.05, 4.2, 6.3)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 147849.00735)
    ops.uniaxialMaterial('Elastic', 402006, 219970.47435)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 9.0, 3.95, 6.3, '-mass', 29.64127930682976, 29.64127930682976, 29.64127930682976, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 8.725, 3.95, 6.3)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 9.275, 3.95, 6.3)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 9.0, 3.95, 5.95)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 9.0, 3.95, 6.65)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 9.0, 3.675, 6.3)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 9.0, 4.225, 6.3)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 164316.2516)
    ops.uniaxialMaterial('Elastic', 402007, 269141.1168)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 14.95, 3.95, 6.3, '-mass', 18.370614169215084, 18.370614169215084, 18.370614169215084, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 14.725, 3.95, 6.3)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 14.95, 3.95, 5.95)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 14.95, 3.95, 6.65)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 14.95, 3.725, 6.3)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 14.95, 4.175, 6.3)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 107594.9652)
    ops.uniaxialMaterial('Elastic', 402008, 131974.66535)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 7.9, 6.3, '-mass', 10.487703873598369, 10.487703873598369, 10.487703873598369, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.175, 7.9, 6.3)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 7.9, 5.95)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 7.9, 6.65)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 7.725, 6.3)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 8.075, 6.3)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 60900.348)
    ops.uniaxialMaterial('Elastic', 402009, 77117.95345)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 3.05, 7.9, 6.3, '-mass', 21.86953109072375, 21.86953109072375, 21.86953109072375, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 2.8, 7.9, 6.3)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 3.3, 7.9, 6.3)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 3.05, 7.9, 5.95)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 3.05, 7.9, 6.65)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 3.05, 7.65, 6.3)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 3.05, 8.15, 6.3)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 144866.55535)
    ops.uniaxialMaterial('Elastic', 402010, 215533.1677)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 9.0, 7.9, 6.3, '-mass', 29.64127930682976, 29.64127930682976, 29.64127930682976, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 8.725, 7.9, 6.3)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 9.275, 7.9, 6.3)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 9.0, 7.9, 5.95)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 9.0, 7.9, 6.65)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 9.0, 7.625, 6.3)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 9.0, 8.175, 6.3)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 164316.2516)
    ops.uniaxialMaterial('Elastic', 402011, 269141.1168)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 14.95, 7.9, 6.3, '-mass', 18.37061416921508, 18.37061416921508, 18.37061416921508, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 14.725, 7.9, 6.3)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 14.95, 7.9, 5.95)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 14.95, 7.9, 6.65)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 14.95, 7.675, 6.3)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 14.95, 8.125, 6.3)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 107594.9652)
    ops.uniaxialMaterial('Elastic', 402012, 131974.66535)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2013, 0.0, 11.85, 6.3, '-mass', 10.48770387359837, 10.48770387359837, 10.48770387359837, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.175, 11.85, 6.3)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 11.85, 5.95)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 11.85, 6.65)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 11.675, 6.3)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 12.025, 6.3)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302013, 60900.348)
    ops.uniaxialMaterial('Elastic', 402013, 77117.95345)
    ops.section('Aggregator', 12013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402013, 'My', 302013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12013, 2013, 12013, 12013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2014, 3.05, 11.85, 6.3, '-mass', 21.86953109072375, 21.86953109072375, 21.86953109072375, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 2.8, 11.85, 6.3)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 3.3, 11.85, 6.3)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 3.05, 11.85, 5.95)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 3.05, 11.85, 6.65)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 3.05, 11.6, 6.3)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 3.05, 12.1, 6.3)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302014, 144866.55535)
    ops.uniaxialMaterial('Elastic', 402014, 215533.1677)
    ops.section('Aggregator', 12014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402014, 'My', 302014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12014, 2014, 12014, 12014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2015, 9.0, 11.85, 6.3, '-mass', 29.641279306829762, 29.641279306829762, 29.641279306829762, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 8.725, 11.85, 6.3)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 9.275, 11.85, 6.3)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 9.0, 11.85, 5.95)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 9.0, 11.85, 6.65)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 9.0, 11.575, 6.3)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 9.0, 12.125, 6.3)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302015, 164316.2516)
    ops.uniaxialMaterial('Elastic', 402015, 269141.1168)
    ops.section('Aggregator', 12015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402015, 'My', 302015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12015, 2015, 12015, 12015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2016, 14.95, 11.85, 6.3, '-mass', 18.370614169215084, 18.370614169215084, 18.370614169215084, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 14.725, 11.85, 6.3)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 14.95, 11.85, 5.95)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 14.95, 11.85, 6.65)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 14.95, 11.625, 6.3)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 14.95, 12.075, 6.3)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302016, 107594.9652)
    ops.uniaxialMaterial('Elastic', 402016, 131974.66535)
    ops.section('Aggregator', 12016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402016, 'My', 302016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12016, 2016, 12016, 12016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 2)
    # Central joint node
    ops.node(2017, 0.0, 15.8, 6.3, '-mass', 6.88967252803262, 6.88967252803262, 6.88967252803262, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32017, 0.15, 15.8, 6.3)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 0.0, 15.8, 6.0)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 0.0, 15.8, 6.6)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 0.0, 15.65, 6.3)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302017, 32354.45415)
    ops.uniaxialMaterial('Elastic', 402017, 42782.48485)
    ops.section('Aggregator', 12017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402017, 'My', 302017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12017, 2017, 12017, 12017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 2)
    # Central joint node
    ops.node(2018, 3.05, 15.8, 6.3, '-mass', 15.407701325178389, 15.407701325178389, 15.407701325178389, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 2.85, 15.8, 6.3)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(32018, 3.25, 15.8, 6.3)
    ops.element('elasticBeamColumn', 32018, 2018, 32018, 99999, 88888)
    ops.node(22018, 3.05, 15.8, 6.0)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 3.05, 15.8, 6.6)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 3.05, 15.6, 6.3)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302018, 68991.4027)
    ops.uniaxialMaterial('Elastic', 402018, 118711.168)
    ops.section('Aggregator', 12018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402018, 'My', 302018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12018, 2018, 12018, 12018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 2)
    # Central joint node
    ops.node(2019, 9.0, 15.8, 6.3, '-mass', 20.855374617737002, 20.855374617737002, 20.855374617737002, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52019, 8.75, 15.8, 6.3)
    ops.element('elasticBeamColumn', 52019, 52019, 2019, 99999, 88888)
    ops.node(32019, 9.25, 15.8, 6.3)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 9.0, 15.8, 6.0)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 9.0, 15.8, 6.6)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 9.0, 15.55, 6.3)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302019, 87590.3646)
    ops.uniaxialMaterial('Elastic', 402019, 172872.75725)
    ops.section('Aggregator', 12019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402019, 'My', 302019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12019, 2019, 12019, 12019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 2)
    # Central joint node
    ops.node(2020, 14.95, 15.8, 6.3, '-mass', 12.031688328236493, 12.031688328236493, 12.031688328236493, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 14.775, 15.8, 6.3)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(22020, 14.95, 15.8, 6.0)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 14.95, 15.8, 6.6)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 14.95, 15.625, 6.3)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302020, 45929.2676)
    ops.uniaxialMaterial('Elastic', 402020, 65636.65565)
    ops.section('Aggregator', 12020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402020, 'My', 302020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12020, 2020, 12020, 12020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 9.45, '-mass', 2.9167686034658513, 2.9167686034658513, 2.9167686034658513, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 9.45)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 9.15)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 9.75)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 9.45)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 20693.08885)
    ops.uniaxialMaterial('Elastic', 403001, 31276.665)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 3.05, 0.0, 9.45, '-mass', 12.513951325178388, 12.513951325178388, 12.513951325178388, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 2.875, 0.0, 9.45)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 3.225, 0.0, 9.45)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 3.05, 0.0, 9.15)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 3.05, 0.0, 9.75)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 3.05, 0.175, 9.45)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 40471.38235)
    ops.uniaxialMaterial('Elastic', 403002, 96930.8598)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 9.0, 0.0, 9.45, '-mass', 20.448188073394494, 20.448188073394494, 20.448188073394494, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 8.8, 0.0, 9.45)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 9.2, 0.0, 9.45)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 9.0, 0.0, 9.15)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 9.0, 0.0, 9.75)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 9.0, 0.2, 9.45)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 48474.77945)
    ops.uniaxialMaterial('Elastic', 403003, 108438.48525)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 14.95, 0.0, 9.45, '-mass', 11.643462028542304, 11.643462028542304, 11.643462028542304, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 14.825, 0.0, 9.45)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 14.95, 0.0, 9.15)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 14.95, 0.0, 9.75)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 14.95, 0.125, 9.45)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 27212.5704)
    ops.uniaxialMaterial('Elastic', 403004, 37513.887)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 3.95, 9.45, '-mass', 9.65380988786952, 9.65380988786952, 9.65380988786952, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.125, 3.95, 9.45)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 3.95, 9.1)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 3.95, 9.8)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 3.825, 9.45)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 4.075, 9.45)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 36654.60555)
    ops.uniaxialMaterial('Elastic', 403005, 45913.4048)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 3.05, 3.95, 9.45, '-mass', 22.20852191641182, 22.20852191641182, 22.20852191641182, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 2.85, 3.95, 9.45)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 3.25, 3.95, 9.45)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 3.05, 3.95, 9.1)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 3.05, 3.95, 9.8)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 3.05, 3.75, 9.45)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 3.05, 4.15, 9.45)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 73418.0387)
    ops.uniaxialMaterial('Elastic', 403006, 140568.68385)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 9.0, 3.95, 9.45, '-mass', 29.318190621814473, 29.318190621814473, 29.318190621814473, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 8.75, 3.95, 9.45)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 9.25, 3.95, 9.45)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 9.0, 3.95, 9.1)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 9.0, 3.95, 9.8)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 9.0, 3.7, 9.45)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 9.0, 4.2, 9.45)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 104567.2977)
    ops.uniaxialMaterial('Elastic', 403007, 200208.1188)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 14.95, 3.95, 9.45, '-mass', 17.748290010193678, 17.748290010193678, 17.748290010193678, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 14.775, 3.95, 9.45)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 14.95, 3.95, 9.1)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 14.95, 3.95, 9.8)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 14.95, 3.775, 9.45)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 14.95, 4.125, 9.45)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 57583.0371)
    ops.uniaxialMaterial('Elastic', 403008, 82583.0133)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 7.9, 9.45, '-mass', 10.13571610601427, 10.13571610601427, 10.13571610601427, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.125, 7.9, 9.45)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 7.9, 9.1)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 7.9, 9.8)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 7.775, 9.45)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 8.025, 9.45)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 35210.83835)
    ops.uniaxialMaterial('Elastic', 403009, 44336.15825)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 3.05, 7.9, 9.45, '-mass', 21.28115188583078, 21.28115188583078, 21.28115188583078, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 2.85, 7.9, 9.45)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 3.25, 7.9, 9.45)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 3.05, 7.9, 9.1)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 3.05, 7.9, 9.8)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 3.05, 7.7, 9.45)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 3.05, 8.1, 9.45)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 71447.7693)
    ops.uniaxialMaterial('Elastic', 403010, 136796.33885)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 9.0, 7.9, 9.45, '-mass', 29.318190621814473, 29.318190621814473, 29.318190621814473, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 8.75, 7.9, 9.45)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 9.25, 7.9, 9.45)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 9.0, 7.9, 9.1)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 9.0, 7.9, 9.8)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 9.0, 7.65, 9.45)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 9.0, 8.15, 9.45)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 104567.2977)
    ops.uniaxialMaterial('Elastic', 403011, 200208.1188)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 14.95, 7.9, 9.45, '-mass', 17.748290010193678, 17.748290010193678, 17.748290010193678, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 14.775, 7.9, 9.45)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 14.95, 7.9, 9.1)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 14.95, 7.9, 9.8)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 14.95, 7.725, 9.45)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 14.95, 8.075, 9.45)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 57583.0371)
    ops.uniaxialMaterial('Elastic', 403012, 82583.0133)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3013, 0.0, 11.85, 9.45, '-mass', 10.135716106014272, 10.135716106014272, 10.135716106014272, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 11.85, 9.45)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 11.85, 9.1)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 11.85, 9.8)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 11.725, 9.45)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 11.975, 9.45)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303013, 35210.83835)
    ops.uniaxialMaterial('Elastic', 403013, 44336.15825)
    ops.section('Aggregator', 13013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403013, 'My', 303013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13013, 3013, 13013, 13013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3014, 3.05, 11.85, 9.45, '-mass', 21.28115188583078, 21.28115188583078, 21.28115188583078, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 2.85, 11.85, 9.45)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 3.25, 11.85, 9.45)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 3.05, 11.85, 9.1)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 3.05, 11.85, 9.8)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 3.05, 11.65, 9.45)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 3.05, 12.05, 9.45)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303014, 71447.7693)
    ops.uniaxialMaterial('Elastic', 403014, 136796.33885)
    ops.section('Aggregator', 13014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403014, 'My', 303014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13014, 3014, 13014, 13014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3015, 9.0, 11.85, 9.45, '-mass', 29.318190621814473, 29.318190621814473, 29.318190621814473, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 8.75, 11.85, 9.45)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 9.25, 11.85, 9.45)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 9.0, 11.85, 9.1)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 9.0, 11.85, 9.8)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 9.0, 11.6, 9.45)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 9.0, 12.1, 9.45)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303015, 104567.2977)
    ops.uniaxialMaterial('Elastic', 403015, 200208.1188)
    ops.section('Aggregator', 13015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403015, 'My', 303015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13015, 3015, 13015, 13015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3016, 14.95, 11.85, 9.45, '-mass', 17.748290010193678, 17.748290010193678, 17.748290010193678, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 14.775, 11.85, 9.45)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 14.95, 11.85, 9.1)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 14.95, 11.85, 9.8)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 14.95, 11.675, 9.45)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 14.95, 12.025, 9.45)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303016, 57583.0371)
    ops.uniaxialMaterial('Elastic', 403016, 82583.0133)
    ops.section('Aggregator', 13016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403016, 'My', 303016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13016, 3016, 13016, 13016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 3)
    # Central joint node
    ops.node(3017, 0.0, 15.8, 9.45, '-mass', 6.723311671763508, 6.723311671763508, 6.723311671763508, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33017, 0.125, 15.8, 9.45)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 0.0, 15.8, 9.15)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 0.0, 15.8, 9.75)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 0.0, 15.675, 9.45)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303017, 20695.26775)
    ops.uniaxialMaterial('Elastic', 403017, 28758.82135)
    ops.section('Aggregator', 13017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403017, 'My', 303017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13017, 3017, 13017, 13017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 3)
    # Central joint node
    ops.node(3018, 3.05, 15.8, 9.45, '-mass', 15.142410805300713, 15.142410805300713, 15.142410805300713, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 2.875, 15.8, 9.45)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(33018, 3.225, 15.8, 9.45)
    ops.element('elasticBeamColumn', 33018, 3018, 33018, 99999, 88888)
    ops.node(23018, 3.05, 15.8, 9.15)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 3.05, 15.8, 9.75)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 3.05, 15.625, 9.45)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303018, 36863.47625)
    ops.uniaxialMaterial('Elastic', 403018, 81664.68335)
    ops.section('Aggregator', 13018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403018, 'My', 303018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13018, 3018, 13018, 13018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 3)
    # Central joint node
    ops.node(3019, 9.0, 15.8, 9.45, '-mass', 20.448188073394494, 20.448188073394494, 20.448188073394494, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53019, 8.8, 15.8, 9.45)
    ops.element('elasticBeamColumn', 53019, 53019, 3019, 99999, 88888)
    ops.node(33019, 9.2, 15.8, 9.45)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 9.0, 15.8, 9.15)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 9.0, 15.8, 9.75)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 9.0, 15.6, 9.45)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303019, 48474.77945)
    ops.uniaxialMaterial('Elastic', 403019, 108438.48525)
    ops.section('Aggregator', 13019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403019, 'My', 303019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13019, 3019, 13019, 13019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 3)
    # Central joint node
    ops.node(3020, 14.95, 15.8, 9.45, '-mass', 11.643462028542304, 11.643462028542304, 11.643462028542304, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 14.825, 15.8, 9.45)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(23020, 14.95, 15.8, 9.15)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 14.95, 15.8, 9.75)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 14.95, 15.675, 9.45)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303020, 27212.5704)
    ops.uniaxialMaterial('Elastic', 403020, 37513.887)
    ops.section('Aggregator', 13020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403020, 'My', 303020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13020, 3020, 13020, 13020, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 12.6, '-mass', 0.8766819571865441, 0.8766819571865441, 0.8766819571865441, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 12.6)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 12.35)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 12.6)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 8208.2374)
    ops.uniaxialMaterial('Elastic', 404001, 16373.2267)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 3.05, 0.0, 12.6, '-mass', 7.06565239551478, 7.06565239551478, 7.06565239551478, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 2.875, 0.0, 12.6)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 3.225, 0.0, 12.6)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 3.05, 0.0, 12.35)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 3.05, 0.175, 12.6)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 29201.74275)
    ops.uniaxialMaterial('Elastic', 404002, 44129.78015)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 9.0, 0.0, 12.6, '-mass', 12.956534148827727, 12.956534148827727, 12.956534148827727, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 8.8, 0.0, 12.6)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 9.2, 0.0, 12.6)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 9.0, 0.0, 12.35)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 9.0, 0.2, 12.6)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 36631.5256)
    ops.uniaxialMaterial('Elastic', 404003, 64580.58075)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 14.95, 0.0, 12.6, '-mass', 6.555790010193679, 6.555790010193679, 6.555790010193679, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 14.825, 0.0, 12.6)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 14.95, 0.0, 12.35)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 14.95, 0.125, 12.6)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 16740.72305)
    ops.uniaxialMaterial('Elastic', 404004, 30196.8748)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 3.95, 12.6, '-mass', 5.780001274209989, 5.780001274209989, 5.780001274209989, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.125, 3.95, 12.6)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 3.95, 12.3)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 3.825, 12.6)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 4.075, 12.6)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 22747.1075)
    ops.uniaxialMaterial('Elastic', 404005, 41639.9154)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 3.05, 3.95, 12.6, '-mass', 18.011306065239552, 18.011306065239552, 18.011306065239552, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 2.85, 3.95, 12.6)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 3.25, 3.95, 12.6)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 3.05, 3.95, 12.3)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 3.05, 3.75, 12.6)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 3.05, 4.15, 12.6)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 50037.6831)
    ops.uniaxialMaterial('Elastic', 404006, 91078.24645)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 9.0, 3.95, 12.6, '-mass', 25.061080530071358, 25.061080530071358, 25.061080530071358, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 8.75, 3.95, 12.6)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 9.25, 3.95, 12.6)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 9.0, 3.95, 12.3)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 9.0, 3.7, 12.6)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 9.0, 4.2, 12.6)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 58183.06885)
    ops.uniaxialMaterial('Elastic', 404007, 116798.76685)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 14.95, 3.95, 12.6, '-mass', 12.810815494393477, 12.810815494393477, 12.810815494393477, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 14.775, 3.95, 12.6)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 14.95, 3.95, 12.3)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 14.95, 3.775, 12.6)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 14.95, 4.125, 12.6)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 31669.11825)
    ops.uniaxialMaterial('Elastic', 404008, 68971.87145)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 7.9, 12.6, '-mass', 5.9646024464831795, 5.9646024464831795, 5.9646024464831795, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.125, 7.9, 12.6)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 7.9, 12.3)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 7.775, 12.6)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 8.025, 12.6)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 19629.9994)
    ops.uniaxialMaterial('Elastic', 404009, 36420.708)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 3.05, 7.9, 12.6, '-mass', 18.19590723751274, 18.19590723751274, 18.19590723751274, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 2.85, 7.9, 12.6)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 3.25, 7.9, 12.6)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 3.05, 7.9, 12.3)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 3.05, 7.7, 12.6)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 3.05, 8.1, 12.6)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 47229.2575)
    ops.uniaxialMaterial('Elastic', 404010, 86298.64075)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 9.0, 7.9, 12.6, '-mass', 25.061080530071358, 25.061080530071358, 25.061080530071358, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 8.75, 7.9, 12.6)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 9.25, 7.9, 12.6)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 9.0, 7.9, 12.3)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 9.0, 7.65, 12.6)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 9.0, 8.15, 12.6)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 58183.06885)
    ops.uniaxialMaterial('Elastic', 404011, 116798.76685)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 14.95, 7.9, 12.6, '-mass', 12.810815494393477, 12.810815494393477, 12.810815494393477, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 14.775, 7.9, 12.6)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 14.95, 7.9, 12.3)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 14.95, 7.725, 12.6)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 14.95, 8.075, 12.6)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 31669.11825)
    ops.uniaxialMaterial('Elastic', 404012, 68971.87145)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4013, 0.0, 11.85, 12.6, '-mass', 5.96460244648318, 5.96460244648318, 5.96460244648318, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 11.85, 12.6)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 11.85, 12.3)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 11.725, 12.6)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 11.975, 12.6)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304013, 19629.9994)
    ops.uniaxialMaterial('Elastic', 404013, 36420.708)
    ops.section('Aggregator', 14013, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404013, 'My', 304013, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14013, 4013, 14013, 14013, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4014, 3.05, 11.85, 12.6, '-mass', 18.195907237512742, 18.195907237512742, 18.195907237512742, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 2.85, 11.85, 12.6)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 3.25, 11.85, 12.6)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 3.05, 11.85, 12.3)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 3.05, 11.65, 12.6)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 3.05, 12.05, 12.6)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304014, 47229.2575)
    ops.uniaxialMaterial('Elastic', 404014, 86298.64075)
    ops.section('Aggregator', 14014, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404014, 'My', 304014, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14014, 4014, 14014, 14014, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4015, 9.0, 11.85, 12.6, '-mass', 25.061080530071358, 25.061080530071358, 25.061080530071358, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 8.75, 11.85, 12.6)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 9.25, 11.85, 12.6)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 9.0, 11.85, 12.3)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 9.0, 11.6, 12.6)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 9.0, 12.1, 12.6)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304015, 58183.06885)
    ops.uniaxialMaterial('Elastic', 404015, 116798.76685)
    ops.section('Aggregator', 14015, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404015, 'My', 304015, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14015, 4015, 14015, 14015, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4016, 14.95, 11.85, 12.6, '-mass', 12.810815494393477, 12.810815494393477, 12.810815494393477, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 14.775, 11.85, 12.6)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 14.95, 11.85, 12.3)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 14.95, 11.675, 12.6)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 14.95, 12.025, 12.6)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304016, 31669.11825)
    ops.uniaxialMaterial('Elastic', 404016, 68971.87145)
    ops.section('Aggregator', 14016, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404016, 'My', 304016, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14016, 4016, 14016, 14016, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 4)
    # Central joint node
    ops.node(4017, 0.0, 15.8, 12.6, '-mass', 3.1773318042813457, 3.1773318042813457, 3.1773318042813457, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 0.125, 15.8, 12.6)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 0.0, 15.8, 12.35)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 0.0, 15.675, 12.6)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304017, 12551.43045)
    ops.uniaxialMaterial('Elastic', 404017, 23334.14295)
    ops.section('Aggregator', 14017, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404017, 'My', 304017, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14017, 4017, 14017, 14017, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 4)
    # Central joint node
    ops.node(4018, 3.05, 15.8, 12.6, '-mass', 9.48189857288481, 9.48189857288481, 9.48189857288481, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 2.875, 15.8, 12.6)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(34018, 3.225, 15.8, 12.6)
    ops.element('elasticBeamColumn', 34018, 4018, 34018, 99999, 88888)
    ops.node(24018, 3.05, 15.8, 12.35)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 3.05, 15.625, 12.6)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304018, 33031.658)
    ops.uniaxialMaterial('Elastic', 404018, 49558.5484)
    ops.section('Aggregator', 14018, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404018, 'My', 304018, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14018, 4018, 14018, 14018, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 4)
    # Central joint node
    ops.node(4019, 9.0, 15.8, 12.6, '-mass', 12.956534148827727, 12.956534148827727, 12.956534148827727, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54019, 8.8, 15.8, 12.6)
    ops.element('elasticBeamColumn', 54019, 54019, 4019, 99999, 88888)
    ops.node(34019, 9.2, 15.8, 12.6)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 9.0, 15.8, 12.35)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 9.0, 15.6, 12.6)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304019, 36631.5256)
    ops.uniaxialMaterial('Elastic', 404019, 64580.58075)
    ops.section('Aggregator', 14019, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404019, 'My', 304019, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14019, 4019, 14019, 14019, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 4)
    # Central joint node
    ops.node(4020, 14.95, 15.8, 12.6, '-mass', 6.55579001019368, 6.55579001019368, 6.55579001019368, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 14.825, 15.8, 12.6)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 14.95, 15.8, 12.35)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 14.95, 15.675, 12.6)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304020, 16740.72305)
    ops.uniaxialMaterial('Elastic', 404020, 30196.8748)
    ops.section('Aggregator', 14020, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404020, 'My', 304020, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14020, 4020, 14020, 14020, '-orient', 0, 0, 1, 0, 1, 0)
