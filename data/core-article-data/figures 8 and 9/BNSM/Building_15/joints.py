import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (1, 0, 0.5)
    # Central joint node
    ops.node(4013, 5.8, 0.0, 1.775, '-mass', 3.6955848623853216, 3.6955848623853216, 3.6955848623853216, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 6.025, 0.0, 1.775)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 5.8, 0.0, 1.575)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(74013, 5.8, 0.0, 1.975)
    ops.element('elasticBeamColumn', 74013, 4013, 74013, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(4014, 8.65, 0.0, 1.775, '-mass', 3.6955848623853216, 3.6955848623853216, 3.6955848623853216, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 8.425, 0.0, 1.775)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(24014, 8.65, 0.0, 1.575)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(74014, 8.65, 0.0, 1.975)
    ops.element('elasticBeamColumn', 74014, 4014, 74014, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    # Central joint node
    ops.node(4015, 5.8, 0.0, 4.825, '-mass', 3.34329128440367, 3.34329128440367, 3.34329128440367, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34015, 6.025, 0.0, 4.825)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 5.8, 0.0, 4.65)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(74015, 5.8, 0.0, 5.0)
    ops.element('elasticBeamColumn', 74015, 4015, 74015, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(4016, 8.65, 0.0, 4.825, '-mass', 3.34329128440367, 3.34329128440367, 3.34329128440367, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 8.425, 0.0, 4.825)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 8.65, 0.0, 4.65)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(74016, 8.65, 0.0, 5.0)
    ops.element('elasticBeamColumn', 74016, 4016, 74016, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    # Central joint node
    ops.node(4017, 5.8, 0.0, 7.375, '-mass', 3.0937500000000004, 3.0937500000000004, 3.0937500000000004, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 5.975, 0.0, 7.375)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 5.8, 0.0, 7.2)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(74017, 5.8, 0.0, 7.55)
    ops.element('elasticBeamColumn', 74017, 4017, 74017, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(4018, 8.65, 0.0, 7.375, '-mass', 3.0937500000000004, 3.0937500000000004, 3.0937500000000004, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 8.475, 0.0, 7.375)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 8.65, 0.0, 7.2)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(74018, 8.65, 0.0, 7.55)
    ops.element('elasticBeamColumn', 74018, 4018, 74018, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 3.5)
    # Central joint node
    ops.node(4019, 5.8, 0.0, 9.925, '-mass', 3.0937500000000004, 3.0937500000000004, 3.0937500000000004, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 5.975, 0.0, 9.925)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 5.8, 0.0, 9.75)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(74019, 5.8, 0.0, 10.1)
    ops.element('elasticBeamColumn', 74019, 4019, 74019, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(4020, 8.65, 0.0, 9.925, '-mass', 3.0937500000000004, 3.0937500000000004, 3.0937500000000004, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 8.475, 0.0, 9.925)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 8.65, 0.0, 9.75)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(74020, 8.65, 0.0, 10.1)
    ops.element('elasticBeamColumn', 74020, 4020, 74020, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.55, '-mass', 12.808699031600408, 12.808699031600408, 12.808699031600408, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.2, 0.0, 3.55)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 3.25)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.85)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.2, 3.55)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301001, 64160.63755)
    ops.uniaxialMaterial('Elastic', 401001, 92474.2516)
    ops.section('Aggregator', 11001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401001, 'My', 301001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11001, 1001, 11001, 11001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 5.8, 0.0, 3.55, '-mass', 13.292796890927624, 13.292796890927624, 13.292796890927624, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 5.575, 0.0, 3.55)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 6.025, 0.0, 3.55)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 5.8, 0.0, 3.25)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 5.8, 0.0, 3.85)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 5.8, 0.225, 3.55)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301002, 115439.998)
    ops.uniaxialMaterial('Elastic', 401002, 214692.50695)
    ops.section('Aggregator', 11002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401002, 'My', 301002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11002, 1002, 11002, 11002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 8.65, 0.0, 3.55, '-mass', 13.292796890927622, 13.292796890927622, 13.292796890927622, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 8.425, 0.0, 3.55)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 8.875, 0.0, 3.55)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 8.65, 0.0, 3.25)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 8.65, 0.0, 3.85)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 8.65, 0.225, 3.55)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301003, 115439.998)
    ops.uniaxialMaterial('Elastic', 401003, 214692.50695)
    ops.section('Aggregator', 11003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401003, 'My', 301003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11003, 1003, 11003, 11003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 14.45, 0.0, 3.55, '-mass', 12.808699031600407, 12.808699031600407, 12.808699031600407, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 14.25, 0.0, 3.55)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 14.45, 0.0, 3.25)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 14.45, 0.0, 3.85)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 14.45, 0.2, 3.55)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301004, 64160.63755)
    ops.uniaxialMaterial('Elastic', 401004, 92474.2516)
    ops.section('Aggregator', 11004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401004, 'My', 301004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11004, 1004, 11004, 11004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 4.15, 3.55, '-mass', 19.7148496432212, 19.7148496432212, 19.7148496432212, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.25, 4.15, 3.55)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 4.15, 3.2)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 4.15, 3.9)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 3.9, 3.55)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 4.4, 3.55)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301005, 147176.07345)
    ops.uniaxialMaterial('Elastic', 401005, 182059.48765)
    ops.section('Aggregator', 11005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401005, 'My', 301005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11005, 1005, 11005, 11005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 5.8, 4.15, 3.55, '-mass', 23.924928644240573, 23.924928644240573, 23.924928644240573, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 5.55, 4.15, 3.55)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 6.05, 4.15, 3.55)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 5.8, 4.15, 3.2)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 5.8, 4.15, 3.9)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 5.8, 3.9, 3.55)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 5.8, 4.4, 3.55)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301006, 179381.31935)
    ops.uniaxialMaterial('Elastic', 401006, 271650.07665)
    ops.section('Aggregator', 11006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401006, 'My', 301006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11006, 1006, 11006, 11006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 8.65, 4.15, 3.55, '-mass', 23.92492864424057, 23.92492864424057, 23.92492864424057, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 8.4, 4.15, 3.55)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 8.9, 4.15, 3.55)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 8.65, 4.15, 3.2)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 8.65, 4.15, 3.9)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 8.65, 3.9, 3.55)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 8.65, 4.4, 3.55)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301007, 179381.31935)
    ops.uniaxialMaterial('Elastic', 401007, 271650.07665)
    ops.section('Aggregator', 11007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401007, 'My', 301007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11007, 1007, 11007, 11007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 14.45, 4.15, 3.55, '-mass', 19.7148496432212, 19.7148496432212, 19.7148496432212, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 14.2, 4.15, 3.55)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 14.45, 4.15, 3.2)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 14.45, 4.15, 3.9)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 14.45, 3.9, 3.55)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 14.45, 4.4, 3.55)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301008, 147176.07345)
    ops.uniaxialMaterial('Elastic', 401008, 182059.48765)
    ops.section('Aggregator', 11008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401008, 'My', 301008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11008, 1008, 11008, 11008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 8.3, 3.55, '-mass', 12.808699031600408, 12.808699031600408, 12.808699031600408, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.2, 8.3, 3.55)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 8.3, 3.25)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 8.3, 3.85)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 8.1, 3.55)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301009, 64160.63755)
    ops.uniaxialMaterial('Elastic', 401009, 92474.2516)
    ops.section('Aggregator', 11009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401009, 'My', 301009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11009, 1009, 11009, 11009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 5.8, 8.3, 3.55, '-mass', 15.764018858307852, 15.764018858307852, 15.764018858307852, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 5.6, 8.3, 3.55)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 6.0, 8.3, 3.55)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 5.8, 8.3, 3.25)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 5.8, 8.3, 3.85)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 5.8, 8.1, 3.55)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301010, 83428.4692)
    ops.uniaxialMaterial('Elastic', 401010, 146039.59415)
    ops.section('Aggregator', 11010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401010, 'My', 301010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11010, 1010, 11010, 11010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 8.65, 8.3, 3.55, '-mass', 15.76401885830785, 15.76401885830785, 15.76401885830785, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 8.45, 8.3, 3.55)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 8.85, 8.3, 3.55)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 8.65, 8.3, 3.25)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 8.65, 8.3, 3.85)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 8.65, 8.1, 3.55)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301011, 83428.4692)
    ops.uniaxialMaterial('Elastic', 401011, 146039.59415)
    ops.section('Aggregator', 11011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401011, 'My', 301011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11011, 1011, 11011, 11011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 14.45, 8.3, 3.55, '-mass', 12.808699031600407, 12.808699031600407, 12.808699031600407, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 14.25, 8.3, 3.55)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 14.45, 8.3, 3.25)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 14.45, 8.3, 3.85)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 14.45, 8.1, 3.55)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 301012, 64160.63755)
    ops.uniaxialMaterial('Elastic', 401012, 92474.2516)
    ops.section('Aggregator', 11012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 401012, 'My', 301012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 11012, 1012, 11012, 11012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 6.1, '-mass', 12.432552242609582, 12.432552242609582, 12.432552242609582, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.2, 0.0, 6.1)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 5.8)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.2, 6.1)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302001, 47648.0487)
    ops.uniaxialMaterial('Elastic', 402001, 79623.644)
    ops.section('Aggregator', 12001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402001, 'My', 302001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12001, 2001, 12001, 12001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 5.8, 0.0, 6.1, '-mass', 12.85380606523955, 12.85380606523955, 12.85380606523955, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 5.575, 0.0, 6.1)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 6.025, 0.0, 6.1)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 5.8, 0.0, 5.8)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 5.8, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 5.8, 0.225, 6.1)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302002, 84235.00535)
    ops.uniaxialMaterial('Elastic', 402002, 181961.31025)
    ops.section('Aggregator', 12002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402002, 'My', 302002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12002, 2002, 12002, 12002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 8.65, 0.0, 6.1, '-mass', 12.853806065239548, 12.853806065239548, 12.853806065239548, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 8.425, 0.0, 6.1)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 8.875, 0.0, 6.1)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 8.65, 0.0, 5.8)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 8.65, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 8.65, 0.225, 6.1)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302003, 84235.00535)
    ops.uniaxialMaterial('Elastic', 402003, 181961.31025)
    ops.section('Aggregator', 12003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402003, 'My', 302003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12003, 2003, 12003, 12003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 14.45, 0.0, 6.1, '-mass', 12.43255224260958, 12.43255224260958, 12.43255224260958, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 14.25, 0.0, 6.1)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 14.45, 0.0, 5.8)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 14.45, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 14.45, 0.2, 6.1)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302004, 47648.0487)
    ops.uniaxialMaterial('Elastic', 402004, 79623.644)
    ops.section('Aggregator', 12004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402004, 'My', 302004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12004, 2004, 12004, 12004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 4.15, 6.1, '-mass', 19.001393985728846, 19.001393985728846, 19.001393985728846, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.25, 4.15, 6.1)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 4.15, 5.75)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 4.15, 6.45)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 3.9, 6.1)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 4.4, 6.1)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302005, 109544.5206)
    ops.uniaxialMaterial('Elastic', 402005, 156897.69095)
    ops.section('Aggregator', 12005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402005, 'My', 302005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12005, 2005, 12005, 12005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 5.8, 4.15, 6.1, '-mass', 22.957650356778796, 22.957650356778796, 22.957650356778796, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 5.55, 4.15, 6.1)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 6.05, 4.15, 6.1)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 5.8, 4.15, 5.75)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 5.8, 4.15, 6.45)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 5.8, 3.9, 6.1)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 5.8, 4.4, 6.1)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302006, 135981.63595)
    ops.uniaxialMaterial('Elastic', 402006, 233127.703)
    ops.section('Aggregator', 12006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402006, 'My', 302006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12006, 2006, 12006, 12006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 8.65, 4.15, 6.1, '-mass', 22.957650356778792, 22.957650356778792, 22.957650356778792, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 8.4, 4.15, 6.1)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 8.9, 4.15, 6.1)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 8.65, 4.15, 5.75)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 8.65, 4.15, 6.45)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 8.65, 3.9, 6.1)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 8.65, 4.4, 6.1)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302007, 135981.63595)
    ops.uniaxialMaterial('Elastic', 402007, 233127.703)
    ops.section('Aggregator', 12007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402007, 'My', 302007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12007, 2007, 12007, 12007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 14.45, 4.15, 6.1, '-mass', 19.001393985728843, 19.001393985728843, 19.001393985728843, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 14.2, 4.15, 6.1)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 14.45, 4.15, 5.75)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 14.45, 4.15, 6.45)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 14.45, 3.9, 6.1)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 14.45, 4.4, 6.1)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302008, 109544.5206)
    ops.uniaxialMaterial('Elastic', 402008, 156897.69095)
    ops.section('Aggregator', 12008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402008, 'My', 302008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12008, 2008, 12008, 12008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 8.3, 6.1, '-mass', 12.432552242609582, 12.432552242609582, 12.432552242609582, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.2, 8.3, 6.1)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 8.3, 5.8)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 8.3, 6.4)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 8.1, 6.1)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302009, 47648.0487)
    ops.uniaxialMaterial('Elastic', 402009, 79623.644)
    ops.section('Aggregator', 12009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402009, 'My', 302009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12009, 2009, 12009, 12009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 5.8, 8.3, 6.1, '-mass', 15.260960754332315, 15.260960754332315, 15.260960754332315, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 5.6, 8.3, 6.1)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 6.0, 8.3, 6.1)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 5.8, 8.3, 5.8)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 5.8, 8.3, 6.4)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 5.8, 8.1, 6.1)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302010, 62809.12225)
    ops.uniaxialMaterial('Elastic', 402010, 124285.2741)
    ops.section('Aggregator', 12010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402010, 'My', 302010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12010, 2010, 12010, 12010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 8.65, 8.3, 6.1, '-mass', 15.260960754332315, 15.260960754332315, 15.260960754332315, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 8.45, 8.3, 6.1)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 8.85, 8.3, 6.1)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 8.65, 8.3, 5.8)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 8.65, 8.3, 6.4)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 8.65, 8.1, 6.1)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302011, 62809.12225)
    ops.uniaxialMaterial('Elastic', 402011, 124285.2741)
    ops.section('Aggregator', 12011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402011, 'My', 302011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12011, 2011, 12011, 12011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 14.45, 8.3, 6.1, '-mass', 12.43255224260958, 12.43255224260958, 12.43255224260958, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 14.25, 8.3, 6.1)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 14.45, 8.3, 5.8)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 14.45, 8.3, 6.4)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 14.45, 8.1, 6.1)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 302012, 47648.0487)
    ops.uniaxialMaterial('Elastic', 402012, 79623.644)
    ops.section('Aggregator', 12012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 402012, 'My', 302012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 12012, 2012, 12012, 12012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 8.65, '-mass', 12.214050713557592, 12.214050713557592, 12.214050713557592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.175, 0.0, 8.65)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 8.35)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 8.95)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.175, 8.65)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303001, 33269.7877)
    ops.uniaxialMaterial('Elastic', 403001, 56091.293)
    ops.section('Aggregator', 13001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403001, 'My', 303001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13001, 3001, 13001, 13001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 5.8, 0.0, 8.65, '-mass', 12.66557976554536, 12.66557976554536, 12.66557976554536, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 5.625, 0.0, 8.65)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 5.975, 0.0, 8.65)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 5.8, 0.0, 8.35)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 5.8, 0.0, 8.95)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 5.8, 0.175, 8.65)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303002, 43242.46205)
    ops.uniaxialMaterial('Elastic', 403002, 108688.5551)
    ops.section('Aggregator', 13002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403002, 'My', 303002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13002, 3002, 13002, 13002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 8.65, 0.0, 8.65, '-mass', 12.665579765545358, 12.665579765545358, 12.665579765545358, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 8.475, 0.0, 8.65)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 8.825, 0.0, 8.65)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 8.65, 0.0, 8.35)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 8.65, 0.0, 8.95)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 8.65, 0.175, 8.65)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303003, 43242.46205)
    ops.uniaxialMaterial('Elastic', 403003, 108688.5551)
    ops.section('Aggregator', 13003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403003, 'My', 303003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13003, 3003, 13003, 13003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 14.45, 0.0, 8.65, '-mass', 12.214050713557592, 12.214050713557592, 12.214050713557592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 14.275, 0.0, 8.65)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 14.45, 0.0, 8.35)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 14.45, 0.0, 8.95)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 14.45, 0.175, 8.65)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303004, 33269.7877)
    ops.uniaxialMaterial('Elastic', 403004, 56091.293)
    ops.section('Aggregator', 13004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403004, 'My', 303004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13004, 3004, 13004, 13004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 4.15, 8.65, '-mass', 18.51760193679918, 18.51760193679918, 18.51760193679918, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.2, 4.15, 8.65)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 4.15, 8.3)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 4.15, 9.0)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 3.95, 8.65)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 4.35, 8.65)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303005, 69021.41645)
    ops.uniaxialMaterial('Elastic', 403005, 101161.79975)
    ops.section('Aggregator', 13005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403005, 'My', 303005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13005, 3005, 13005, 13005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 5.8, 4.15, 8.65, '-mass', 22.550005096839957, 22.550005096839957, 22.550005096839957, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 5.6, 4.15, 8.65)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 6.0, 4.15, 8.65)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 5.8, 4.15, 8.3)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 5.8, 4.15, 9.0)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 5.8, 3.95, 8.65)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 5.8, 4.35, 8.65)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303006, 75951.3743)
    ops.uniaxialMaterial('Elastic', 403006, 149202.5106)
    ops.section('Aggregator', 13006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403006, 'My', 303006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13006, 3006, 13006, 13006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 8.65, 4.15, 8.65, '-mass', 22.550005096839957, 22.550005096839957, 22.550005096839957, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 8.45, 4.15, 8.65)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 8.85, 4.15, 8.65)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 8.65, 4.15, 8.3)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 8.65, 4.15, 9.0)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 8.65, 3.95, 8.65)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 8.65, 4.35, 8.65)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303007, 75951.3743)
    ops.uniaxialMaterial('Elastic', 403007, 149202.5106)
    ops.section('Aggregator', 13007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403007, 'My', 303007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13007, 3007, 13007, 13007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 14.45, 4.15, 8.65, '-mass', 18.517601936799178, 18.517601936799178, 18.517601936799178, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 14.25, 4.15, 8.65)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 14.45, 4.15, 8.3)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 14.45, 4.15, 9.0)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 14.45, 3.95, 8.65)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 14.45, 4.35, 8.65)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303008, 69021.41645)
    ops.uniaxialMaterial('Elastic', 403008, 101161.79975)
    ops.section('Aggregator', 13008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403008, 'My', 303008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13008, 3008, 13008, 13008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 8.3, 8.65, '-mass', 12.214050713557592, 12.214050713557592, 12.214050713557592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.175, 8.3, 8.65)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 8.3, 8.35)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 8.3, 8.95)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 8.125, 8.65)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303009, 33269.7877)
    ops.uniaxialMaterial('Elastic', 403009, 56091.293)
    ops.section('Aggregator', 13009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403009, 'My', 303009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13009, 3009, 13009, 13009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 5.8, 8.3, 8.65, '-mass', 15.08053261977574, 15.08053261977574, 15.08053261977574, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 5.625, 8.3, 8.65)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 5.975, 8.3, 8.65)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 5.8, 8.3, 8.35)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 5.8, 8.3, 8.95)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 5.8, 8.125, 8.65)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303010, 38022.9522)
    ops.uniaxialMaterial('Elastic', 403010, 85654.7526)
    ops.section('Aggregator', 13010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403010, 'My', 303010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13010, 3010, 13010, 13010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 8.65, 8.3, 8.65, '-mass', 15.080532619775738, 15.080532619775738, 15.080532619775738, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 8.475, 8.3, 8.65)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 8.825, 8.3, 8.65)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 8.65, 8.3, 8.35)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 8.65, 8.3, 8.95)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 8.65, 8.125, 8.65)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303011, 38022.9522)
    ops.uniaxialMaterial('Elastic', 403011, 85654.7526)
    ops.section('Aggregator', 13011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403011, 'My', 303011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13011, 3011, 13011, 13011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 14.45, 8.3, 8.65, '-mass', 12.214050713557592, 12.214050713557592, 12.214050713557592, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 14.275, 8.3, 8.65)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 14.45, 8.3, 8.35)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 14.45, 8.3, 8.95)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 14.45, 8.125, 8.65)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 303012, 33269.7877)
    ops.uniaxialMaterial('Elastic', 403012, 56091.293)
    ops.section('Aggregator', 13012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 403012, 'My', 303012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 13012, 3012, 13012, 13012, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 11.2, '-mass', 6.972989296636086, 6.972989296636086, 6.972989296636086, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.175, 0.0, 11.2)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 10.95)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.175, 11.2)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304001, 24500.4085)
    ops.uniaxialMaterial('Elastic', 404001, 44026.9964)
    ops.section('Aggregator', 14001, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404001, 'My', 304001, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14001, 4001, 14001, 14001, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 5.8, 0.0, 11.2, '-mass', 7.319243119266055, 7.319243119266055, 7.319243119266055, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 5.625, 0.0, 11.2)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 5.975, 0.0, 11.2)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 5.8, 0.0, 10.95)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 5.8, 0.175, 11.2)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304002, 34451.868)
    ops.uniaxialMaterial('Elastic', 404002, 44682.7524)
    ops.section('Aggregator', 14002, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404002, 'My', 304002, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14002, 4002, 14002, 14002, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 8.65, 0.0, 11.2, '-mass', 7.319243119266054, 7.319243119266054, 7.319243119266054, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 8.475, 0.0, 11.2)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 8.825, 0.0, 11.2)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 8.65, 0.0, 10.95)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 8.65, 0.175, 11.2)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304003, 34451.868)
    ops.uniaxialMaterial('Elastic', 404003, 44682.7524)
    ops.section('Aggregator', 14003, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404003, 'My', 304003, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14003, 4003, 14003, 14003, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 14.45, 0.0, 11.2, '-mass', 6.972989296636085, 6.972989296636085, 6.972989296636085, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 14.275, 0.0, 11.2)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 14.45, 0.0, 10.95)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 14.45, 0.175, 11.2)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304004, 24500.4085)
    ops.uniaxialMaterial('Elastic', 404004, 44026.9964)
    ops.section('Aggregator', 14004, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404004, 'My', 304004, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14004, 4004, 14004, 14004, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 4.15, 11.2, '-mass', 13.397048929663606, 13.397048929663606, 13.397048929663606, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.2, 4.15, 11.2)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 4.15, 10.9)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 3.95, 11.2)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 4.35, 11.2)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304005, 37113.2615)
    ops.uniaxialMaterial('Elastic', 404005, 80645.58255)
    ops.section('Aggregator', 14005, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404005, 'My', 304005, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14005, 4005, 14005, 14005, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 5.8, 4.15, 11.2, '-mass', 18.48846712538226, 18.48846712538226, 18.48846712538226, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 5.6, 4.15, 11.2)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 6.0, 4.15, 11.2)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 5.8, 4.15, 10.9)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 5.8, 3.95, 11.2)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 5.8, 4.35, 11.2)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304006, 58308.06335)
    ops.uniaxialMaterial('Elastic', 404006, 91720.4797)
    ops.section('Aggregator', 14006, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404006, 'My', 304006, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14006, 4006, 14006, 14006, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 8.65, 4.15, 11.2, '-mass', 18.48846712538226, 18.48846712538226, 18.48846712538226, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 8.45, 4.15, 11.2)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 8.85, 4.15, 11.2)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 8.65, 4.15, 10.9)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 8.65, 3.95, 11.2)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 8.65, 4.35, 11.2)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304007, 58308.06335)
    ops.uniaxialMaterial('Elastic', 404007, 91720.4797)
    ops.section('Aggregator', 14007, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404007, 'My', 304007, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14007, 4007, 14007, 14007, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 14.45, 4.15, 11.2, '-mass', 13.397048929663605, 13.397048929663605, 13.397048929663605, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 14.25, 4.15, 11.2)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 14.45, 4.15, 10.9)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 14.45, 3.95, 11.2)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 14.45, 4.35, 11.2)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304008, 37113.2615)
    ops.uniaxialMaterial('Elastic', 404008, 80645.58255)
    ops.section('Aggregator', 14008, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404008, 'My', 304008, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14008, 4008, 14008, 14008, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 8.3, 11.2, '-mass', 6.972989296636086, 6.972989296636086, 6.972989296636086, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.175, 8.3, 11.2)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 8.3, 10.95)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 8.125, 11.2)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304009, 24500.4085)
    ops.uniaxialMaterial('Elastic', 404009, 44026.9964)
    ops.section('Aggregator', 14009, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404009, 'My', 304009, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14009, 4009, 14009, 14009, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 5.8, 8.3, 11.2, '-mass', 9.707354740061163, 9.707354740061163, 9.707354740061163, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 5.625, 8.3, 11.2)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 5.975, 8.3, 11.2)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 5.8, 8.3, 10.95)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 5.8, 8.125, 11.2)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304010, 38692.34235)
    ops.uniaxialMaterial('Elastic', 404010, 49954.9801)
    ops.section('Aggregator', 14010, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404010, 'My', 304010, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14010, 4010, 14010, 14010, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 8.65, 8.3, 11.2, '-mass', 9.707354740061161, 9.707354740061161, 9.707354740061161, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 8.475, 8.3, 11.2)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 8.825, 8.3, 11.2)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 8.65, 8.3, 10.95)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 8.65, 8.125, 11.2)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304011, 38692.34235)
    ops.uniaxialMaterial('Elastic', 404011, 49954.9801)
    ops.section('Aggregator', 14011, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404011, 'My', 304011, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14011, 4011, 14011, 14011, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 14.45, 8.3, 11.2, '-mass', 6.972989296636085, 6.972989296636085, 6.972989296636085, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 14.275, 8.3, 11.2)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 14.45, 8.3, 10.95)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 14.45, 8.125, 11.2)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    # Joint flexibility element: Elastic
    ops.uniaxialMaterial('Elastic', 304012, 24500.4085)
    ops.uniaxialMaterial('Elastic', 404012, 44026.9964)
    ops.section('Aggregator', 14012, 99999, 'P', 99999, 'Vy', 99999, 'Vz', 404012, 'My', 304012, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 14012, 4012, 14012, 14012, '-orient', 0, 0, 1, 0, 1, 0)
