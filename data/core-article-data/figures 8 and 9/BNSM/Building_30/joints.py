import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(4025, 7.7, 0.0, 1.25, '-mass', 4.400229357798166, 4.400229357798166, 4.400229357798166, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 7.875, 0.0, 1.25)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 7.7, 0.0, 1.0)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 7.7, 0.0, 1.5)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 0.5)
    # Central joint node
    ops.node(4026, 10.65, 0.0, 1.25, '-mass', 4.400229357798166, 4.400229357798166, 4.400229357798166, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 10.475, 0.0, 1.25)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 10.65, 0.0, 1.0)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 10.65, 0.0, 1.5)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(4027, 7.7, 0.0, 3.75, '-mass', 4.65282874617737, 4.65282874617737, 4.65282874617737, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34027, 7.875, 0.0, 3.75)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 7.7, 0.0, 3.425)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(74027, 7.7, 0.0, 4.075)
    ops.element('elasticBeamColumn', 74027, 4027, 74027, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    # Central joint node
    ops.node(4028, 10.65, 0.0, 3.75, '-mass', 4.65282874617737, 4.65282874617737, 4.65282874617737, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 10.475, 0.0, 3.75)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 10.65, 0.0, 3.425)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(74028, 10.65, 0.0, 4.075)
    ops.element('elasticBeamColumn', 74028, 4028, 74028, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(4029, 7.7, 0.0, 6.25, '-mass', 4.284021406727828, 4.284021406727828, 4.284021406727828, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34029, 7.825, 0.0, 6.25)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 7.7, 0.0, 6.0)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(74029, 7.7, 0.0, 6.5)
    ops.element('elasticBeamColumn', 74029, 4029, 74029, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    # Central joint node
    ops.node(4030, 10.65, 0.0, 6.25, '-mass', 4.284021406727828, 4.284021406727828, 4.284021406727828, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 10.525, 0.0, 6.25)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(24030, 10.65, 0.0, 6.0)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(74030, 10.65, 0.0, 6.5)
    ops.element('elasticBeamColumn', 74030, 4030, 74030, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(4031, 7.7, 0.0, 8.75, '-mass', 4.103593272171254, 4.103593272171254, 4.103593272171254, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34031, 7.825, 0.0, 8.75)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 7.7, 0.0, 8.55)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(74031, 7.7, 0.0, 8.95)
    ops.element('elasticBeamColumn', 74031, 4031, 74031, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    # Central joint node
    ops.node(4032, 10.65, 0.0, 8.75, '-mass', 4.103593272171254, 4.103593272171254, 4.103593272171254, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 10.525, 0.0, 8.75)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 10.65, 0.0, 8.55)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(74032, 10.65, 0.0, 8.95)
    ops.element('elasticBeamColumn', 74032, 4032, 74032, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 2.5, '-mass', 8.684146756719663, 8.684146756719663, 8.684146756719663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.125, 0.0, 2.5)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.2)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 2.8)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.175, 2.5)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11001, 1001, 11001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 3.85, 0.0, 2.5, '-mass', 12.750760383979589, 12.750760383979589, 12.750760383979589, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 3.675, 0.0, 2.5)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 4.025, 0.0, 2.5)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 3.85, 0.0, 2.275)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 3.85, 0.0, 2.725)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 3.85, 0.25, 2.5)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11002, 1002, 11002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 7.7, 0.0, 2.5, '-mass', 9.69974308699489, 9.69974308699489, 9.69974308699489, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 7.525, 0.0, 2.5)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 7.875, 0.0, 2.5)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 7.7, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 7.7, 0.0, 2.7)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 7.7, 0.275, 2.5)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11003, 1003, 11003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 10.65, 0.0, 2.5, '-mass', 9.69974308699489, 9.69974308699489, 9.69974308699489, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 10.475, 0.0, 2.5)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(31004, 10.825, 0.0, 2.5)
    ops.element('elasticBeamColumn', 31004, 1004, 31004, 99999, 88888)
    ops.node(21004, 10.65, 0.0, 2.3)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 10.65, 0.0, 2.7)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 10.65, 0.275, 2.5)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11004, 1004, 11004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    # Central joint node
    ops.node(1005, 14.5, 0.0, 2.5, '-mass', 12.75076038397959, 12.75076038397959, 12.75076038397959, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51005, 14.325, 0.0, 2.5)
    ops.element('elasticBeamColumn', 51005, 51005, 1005, 99999, 88888)
    ops.node(31005, 14.675, 0.0, 2.5)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 14.5, 0.0, 2.275)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 14.5, 0.0, 2.725)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(41005, 14.5, 0.25, 2.5)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11005, 1005, 11005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    # Central joint node
    ops.node(1006, 18.35, 0.0, 2.5, '-mass', 8.684146756719663, 8.684146756719663, 8.684146756719663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 18.225, 0.0, 2.5)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(21006, 18.35, 0.0, 2.2)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 18.35, 0.0, 2.8)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(41006, 18.35, 0.175, 2.5)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11006, 1006, 11006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1007, 0.0, 5.8, 2.5, '-mass', 14.536387295294578, 14.536387295294578, 14.536387295294578, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31007, 0.275, 5.8, 2.5)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 0.0, 5.8, 2.2)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 0.0, 5.8, 2.8)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 0.0, 5.65, 2.5)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 0.0, 5.95, 2.5)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11007, 1007, 11007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1008, 3.85, 5.8, 2.5, '-mass', 19.210797016684975, 19.210797016684975, 19.210797016684975, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 3.525, 5.8, 2.5)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(31008, 4.175, 5.8, 2.5)
    ops.element('elasticBeamColumn', 31008, 1008, 31008, 99999, 88888)
    ops.node(21008, 3.85, 5.8, 2.275)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 3.85, 5.8, 2.725)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 3.85, 5.625, 2.5)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 3.85, 5.975, 2.5)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11008, 1008, 11008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1009, 7.7, 5.8, 2.5, '-mass', 19.906671916639784, 19.906671916639784, 19.906671916639784, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51009, 7.35, 5.8, 2.5)
    ops.element('elasticBeamColumn', 51009, 51009, 1009, 99999, 88888)
    ops.node(31009, 8.05, 5.8, 2.5)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 7.7, 5.8, 2.275)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 7.7, 5.8, 2.725)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 7.7, 5.625, 2.5)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 7.7, 5.975, 2.5)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11009, 1009, 11009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1010, 10.65, 5.8, 2.5, '-mass', 19.906671916639784, 19.906671916639784, 19.906671916639784, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 10.3, 5.8, 2.5)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 11.0, 5.8, 2.5)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 10.65, 5.8, 2.275)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 10.65, 5.8, 2.725)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 10.65, 5.625, 2.5)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 10.65, 5.975, 2.5)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11010, 1010, 11010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    # Central joint node
    ops.node(1011, 14.5, 5.8, 2.5, '-mass', 19.210797016684975, 19.210797016684975, 19.210797016684975, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 14.175, 5.8, 2.5)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 14.825, 5.8, 2.5)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 14.5, 5.8, 2.275)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 14.5, 5.8, 2.725)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 14.5, 5.625, 2.5)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 14.5, 5.975, 2.5)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11011, 1011, 11011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    # Central joint node
    ops.node(1012, 18.35, 5.8, 2.5, '-mass', 14.536387295294578, 14.536387295294578, 14.536387295294578, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 18.075, 5.8, 2.5)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 18.35, 5.8, 2.2)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 18.35, 5.8, 2.8)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 18.35, 5.65, 2.5)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 18.35, 5.95, 2.5)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11012, 1012, 11012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1013, 0.0, 11.6, 2.5, '-mass', 14.183176286120265, 14.183176286120265, 14.183176286120265, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.275, 11.6, 2.5)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 11.6, 2.2)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 11.6, 2.8)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 11.45, 2.5)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 11.75, 2.5)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11013, 1013, 11013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1014, 3.85, 11.6, 2.5, '-mass', 18.50437499833635, 18.50437499833635, 18.50437499833635, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 3.525, 11.6, 2.5)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 4.175, 11.6, 2.5)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 3.85, 11.6, 2.275)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 3.85, 11.6, 2.725)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 3.85, 11.425, 2.5)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 3.85, 11.775, 2.5)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11014, 1014, 11014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1015, 7.7, 11.6, 2.5, '-mass', 16.191686405467152, 16.191686405467152, 16.191686405467152, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 7.4, 11.6, 2.5)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 8.0, 11.6, 2.5)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 7.7, 11.6, 2.3)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 7.7, 11.6, 2.7)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 7.7, 11.45, 2.5)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 7.7, 11.75, 2.5)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11015, 1015, 11015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1016, 10.65, 11.6, 2.5, '-mass', 16.191686405467152, 16.191686405467152, 16.191686405467152, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 10.35, 11.6, 2.5)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(31016, 10.95, 11.6, 2.5)
    ops.element('elasticBeamColumn', 31016, 1016, 31016, 99999, 88888)
    ops.node(21016, 10.65, 11.6, 2.3)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 10.65, 11.6, 2.7)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 10.65, 11.45, 2.5)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 10.65, 11.75, 2.5)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11016, 1016, 11016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    # Central joint node
    ops.node(1017, 14.5, 11.6, 2.5, '-mass', 18.50437499833635, 18.50437499833635, 18.50437499833635, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51017, 14.175, 11.6, 2.5)
    ops.element('elasticBeamColumn', 51017, 51017, 1017, 99999, 88888)
    ops.node(31017, 14.825, 11.6, 2.5)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 14.5, 11.6, 2.275)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 14.5, 11.6, 2.725)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 14.5, 11.425, 2.5)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 14.5, 11.775, 2.5)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11017, 1017, 11017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    # Central joint node
    ops.node(1018, 18.35, 11.6, 2.5, '-mass', 14.183176286120265, 14.183176286120265, 14.183176286120265, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 18.075, 11.6, 2.5)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(21018, 18.35, 11.6, 2.2)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 18.35, 11.6, 2.8)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 18.35, 11.45, 2.5)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 18.35, 11.75, 2.5)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11018, 1018, 11018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1019, 0.0, 17.4, 2.5, '-mass', 8.932464799533117, 8.932464799533117, 8.932464799533117, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31019, 0.15, 17.4, 2.5)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 0.0, 17.4, 2.2)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 0.0, 17.4, 2.8)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 0.0, 17.225, 2.5)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11019, 1019, 11019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1020, 3.85, 17.4, 2.5, '-mass', 13.033329191319039, 13.033329191319039, 13.033329191319039, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 3.675, 17.4, 2.5)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(31020, 4.025, 17.4, 2.5)
    ops.element('elasticBeamColumn', 31020, 1020, 31020, 99999, 88888)
    ops.node(21020, 3.85, 17.4, 2.275)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 3.85, 17.4, 2.725)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 3.85, 17.15, 2.5)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11020, 1020, 11020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1021, 7.7, 17.4, 2.5, '-mass', 11.517046056963956, 11.517046056963956, 11.517046056963956, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51021, 7.525, 17.4, 2.5)
    ops.element('elasticBeamColumn', 51021, 51021, 1021, 99999, 88888)
    ops.node(31021, 7.875, 17.4, 2.5)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 7.7, 17.4, 2.3)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 7.7, 17.4, 2.7)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 7.7, 17.175, 2.5)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11021, 1021, 11021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1022, 10.65, 17.4, 2.5, '-mass', 11.517046056963954, 11.517046056963954, 11.517046056963954, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 10.475, 17.4, 2.5)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 10.825, 17.4, 2.5)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 10.65, 17.4, 2.3)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 10.65, 17.4, 2.7)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 10.65, 17.175, 2.5)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11022, 1022, 11022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 1)
    # Central joint node
    ops.node(1023, 14.5, 17.4, 2.5, '-mass', 13.033329191319039, 13.033329191319039, 13.033329191319039, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 14.325, 17.4, 2.5)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 14.675, 17.4, 2.5)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 14.5, 17.4, 2.275)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 14.5, 17.4, 2.725)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 14.5, 17.15, 2.5)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11023, 1023, 11023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 1)
    # Central joint node
    ops.node(1024, 18.35, 17.4, 2.5, '-mass', 8.932464799533117, 8.932464799533117, 8.932464799533117, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 18.2, 17.4, 2.5)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 18.35, 17.4, 2.2)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 18.35, 17.4, 2.8)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 18.35, 17.225, 2.5)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11024, 1024, 11024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 5.0, '-mass', 8.607694157331284, 8.607694157331284, 8.607694157331284, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.125, 0.0, 5.0)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 4.7)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 5.3)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.175, 5.0)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12001, 2001, 12001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 3.85, 0.0, 5.0, '-mass', 12.521402585814451, 12.521402585814451, 12.521402585814451, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 3.675, 0.0, 5.0)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 4.025, 0.0, 5.0)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 3.85, 0.0, 4.775)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 3.85, 0.0, 5.225)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 3.85, 0.25, 5.0)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12002, 2002, 12002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 7.7, 0.0, 5.0, '-mass', 9.596532077820578, 9.596532077820578, 9.596532077820578, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 7.525, 0.0, 5.0)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 7.875, 0.0, 5.0)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 7.7, 0.0, 4.8)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 7.7, 0.0, 5.2)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 7.7, 0.275, 5.0)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12003, 2003, 12003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 10.65, 0.0, 5.0, '-mass', 9.596532077820578, 9.596532077820578, 9.596532077820578, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 10.475, 0.0, 5.0)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(32004, 10.825, 0.0, 5.0)
    ops.element('elasticBeamColumn', 32004, 2004, 32004, 99999, 88888)
    ops.node(22004, 10.65, 0.0, 4.8)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 10.65, 0.0, 5.2)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 10.65, 0.275, 5.0)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12004, 2004, 12004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    # Central joint node
    ops.node(2005, 14.5, 0.0, 5.0, '-mass', 12.521402585814453, 12.521402585814453, 12.521402585814453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52005, 14.325, 0.0, 5.0)
    ops.element('elasticBeamColumn', 52005, 52005, 2005, 99999, 88888)
    ops.node(32005, 14.675, 0.0, 5.0)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 14.5, 0.0, 4.775)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 14.5, 0.0, 5.225)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(42005, 14.5, 0.25, 5.0)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12005, 2005, 12005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    # Central joint node
    ops.node(2006, 18.35, 0.0, 5.0, '-mass', 8.607694157331284, 8.607694157331284, 8.607694157331284, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 18.225, 0.0, 5.0)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(22006, 18.35, 0.0, 4.7)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 18.35, 0.0, 5.3)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(42006, 18.35, 0.175, 5.0)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12006, 2006, 12006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2007, 0.0, 5.8, 5.0, '-mass', 14.343420934438306, 14.343420934438306, 14.343420934438306, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32007, 0.275, 5.8, 5.0)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 0.0, 5.8, 4.7)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 0.0, 5.8, 5.3)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 0.0, 5.65, 5.0)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 0.0, 5.95, 5.0)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12007, 2007, 12007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2008, 3.85, 5.8, 5.0, '-mass', 18.79428325521708, 18.79428325521708, 18.79428325521708, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 3.525, 5.8, 5.0)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(32008, 4.175, 5.8, 5.0)
    ops.element('elasticBeamColumn', 32008, 2008, 32008, 99999, 88888)
    ops.node(22008, 3.85, 5.8, 4.775)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 3.85, 5.8, 5.225)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 3.85, 5.625, 5.0)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 3.85, 5.975, 5.0)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12008, 2008, 12008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2009, 7.7, 5.8, 5.0, '-mass', 19.491381396762108, 19.491381396762108, 19.491381396762108, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52009, 7.35, 5.8, 5.0)
    ops.element('elasticBeamColumn', 52009, 52009, 2009, 99999, 88888)
    ops.node(32009, 8.05, 5.8, 5.0)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 7.7, 5.8, 4.8)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 7.7, 5.8, 5.2)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 7.7, 5.625, 5.0)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 7.7, 5.975, 5.0)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12009, 2009, 12009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2010, 10.65, 5.8, 5.0, '-mass', 19.491381396762108, 19.491381396762108, 19.491381396762108, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 10.3, 5.8, 5.0)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 11.0, 5.8, 5.0)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 10.65, 5.8, 4.8)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 10.65, 5.8, 5.2)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 10.65, 5.625, 5.0)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 10.65, 5.975, 5.0)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12010, 2010, 12010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    # Central joint node
    ops.node(2011, 14.5, 5.8, 5.0, '-mass', 18.79428325521708, 18.79428325521708, 18.79428325521708, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 14.175, 5.8, 5.0)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 14.825, 5.8, 5.0)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 14.5, 5.8, 4.775)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 14.5, 5.8, 5.225)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 14.5, 5.625, 5.0)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 14.5, 5.975, 5.0)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12011, 2011, 12011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    # Central joint node
    ops.node(2012, 18.35, 5.8, 5.0, '-mass', 14.343420934438306, 14.343420934438306, 14.343420934438306, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 18.075, 5.8, 5.0)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 18.35, 5.8, 4.7)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 18.35, 5.8, 5.3)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 18.35, 5.65, 5.0)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 18.35, 5.95, 5.0)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12012, 2012, 12012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2013, 0.0, 11.6, 5.0, '-mass', 14.060852127098858, 14.060852127098858, 14.060852127098858, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.275, 11.6, 5.0)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 11.6, 4.7)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 11.6, 5.3)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 11.45, 5.0)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 11.75, 5.0)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12013, 2013, 12013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2014, 3.85, 11.6, 5.0, '-mass', 18.22914564053818, 18.22914564053818, 18.22914564053818, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 3.525, 11.6, 5.0)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 4.175, 11.6, 5.0)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 3.85, 11.6, 4.775)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 3.85, 11.6, 5.225)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 3.85, 11.425, 5.0)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 3.85, 11.775, 5.0)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12014, 2014, 12014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2015, 7.7, 11.6, 5.0, '-mass', 16.023490686812718, 16.023490686812718, 16.023490686812718, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 7.4, 11.6, 5.0)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 8.0, 11.6, 5.0)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 7.7, 11.6, 4.8)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 7.7, 11.6, 5.2)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 7.7, 11.45, 5.0)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 7.7, 11.75, 5.0)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12015, 2015, 12015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2016, 10.65, 11.6, 5.0, '-mass', 16.023490686812718, 16.023490686812718, 16.023490686812718, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 10.35, 11.6, 5.0)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(32016, 10.95, 11.6, 5.0)
    ops.element('elasticBeamColumn', 32016, 2016, 32016, 99999, 88888)
    ops.node(22016, 10.65, 11.6, 4.8)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 10.65, 11.6, 5.2)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 10.65, 11.45, 5.0)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 10.65, 11.75, 5.0)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12016, 2016, 12016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    # Central joint node
    ops.node(2017, 14.5, 11.6, 5.0, '-mass', 18.22914564053818, 18.22914564053818, 18.22914564053818, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52017, 14.175, 11.6, 5.0)
    ops.element('elasticBeamColumn', 52017, 52017, 2017, 99999, 88888)
    ops.node(32017, 14.825, 11.6, 5.0)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 14.5, 11.6, 4.775)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 14.5, 11.6, 5.225)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 14.5, 11.425, 5.0)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 14.5, 11.775, 5.0)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12017, 2017, 12017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    # Central joint node
    ops.node(2018, 18.35, 11.6, 5.0, '-mass', 14.060852127098858, 14.060852127098858, 14.060852127098858, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 18.075, 11.6, 5.0)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(22018, 18.35, 11.6, 4.7)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 18.35, 11.6, 5.3)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 18.35, 11.45, 5.0)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 18.35, 11.75, 5.0)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12018, 2018, 12018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2019, 0.0, 17.4, 5.0, '-mass', 8.70830577812639, 8.70830577812639, 8.70830577812639, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32019, 0.15, 17.4, 5.0)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 0.0, 17.4, 4.7)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 0.0, 17.4, 5.3)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 0.0, 17.225, 5.0)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12019, 2019, 12019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2020, 3.85, 17.4, 5.0, '-mass', 12.615592188260935, 12.615592188260935, 12.615592188260935, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 3.675, 17.4, 5.0)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(32020, 4.025, 17.4, 5.0)
    ops.element('elasticBeamColumn', 32020, 2020, 32020, 99999, 88888)
    ops.node(22020, 3.85, 17.4, 4.775)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 3.85, 17.4, 5.225)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 3.85, 17.15, 5.0)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12020, 2020, 12020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2021, 7.7, 17.4, 5.0, '-mass', 11.136617922407378, 11.136617922407378, 11.136617922407378, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52021, 7.525, 17.4, 5.0)
    ops.element('elasticBeamColumn', 52021, 52021, 2021, 99999, 88888)
    ops.node(32021, 7.875, 17.4, 5.0)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 7.7, 17.4, 4.8)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 7.7, 17.4, 5.2)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 7.7, 17.175, 5.0)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12021, 2021, 12021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2022, 10.65, 17.4, 5.0, '-mass', 11.136617922407378, 11.136617922407378, 11.136617922407378, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 10.475, 17.4, 5.0)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 10.825, 17.4, 5.0)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 10.65, 17.4, 4.8)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 10.65, 17.4, 5.2)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 10.65, 17.175, 5.0)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12022, 2022, 12022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 2)
    # Central joint node
    ops.node(2023, 14.5, 17.4, 5.0, '-mass', 12.615592188260935, 12.615592188260935, 12.615592188260935, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 14.325, 17.4, 5.0)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 14.675, 17.4, 5.0)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 14.5, 17.4, 4.775)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 14.5, 17.4, 5.225)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 14.5, 17.15, 5.0)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12023, 2023, 12023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 2)
    # Central joint node
    ops.node(2024, 18.35, 17.4, 5.0, '-mass', 8.70830577812639, 8.70830577812639, 8.70830577812639, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 18.2, 17.4, 5.0)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 18.35, 17.4, 4.7)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 18.35, 17.4, 5.3)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 18.35, 17.225, 5.0)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12024, 2024, 12024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 7.5, '-mass', 8.484146756719664, 8.484146756719664, 8.484146756719664, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 7.5)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 7.2)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 7.8)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 7.5)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13001, 3001, 13001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 3.85, 0.0, 7.5, '-mass', 12.197855185202831, 12.197855185202831, 12.197855185202831, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 3.725, 0.0, 7.5)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 3.975, 0.0, 7.5)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 3.85, 0.0, 7.275)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 3.85, 0.0, 7.725)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 3.85, 0.2, 7.5)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13002, 3002, 13002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 7.7, 0.0, 7.5, '-mass', 9.410140640511711, 9.410140640511711, 9.410140640511711, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 7.575, 0.0, 7.5)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 7.825, 0.0, 7.5)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 7.7, 0.0, 7.3)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 7.7, 0.0, 7.7)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 7.7, 0.25, 7.5)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13003, 3003, 13003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 10.65, 0.0, 7.5, '-mass', 9.410140640511711, 9.410140640511711, 9.410140640511711, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 10.525, 0.0, 7.5)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(33004, 10.775, 0.0, 7.5)
    ops.element('elasticBeamColumn', 33004, 3004, 33004, 99999, 88888)
    ops.node(23004, 10.65, 0.0, 7.3)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 10.65, 0.0, 7.7)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 10.65, 0.25, 7.5)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13004, 3004, 13004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    # Central joint node
    ops.node(3005, 14.5, 0.0, 7.5, '-mass', 12.197855185202831, 12.197855185202831, 12.197855185202831, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53005, 14.375, 0.0, 7.5)
    ops.element('elasticBeamColumn', 53005, 53005, 3005, 99999, 88888)
    ops.node(33005, 14.625, 0.0, 7.5)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 14.5, 0.0, 7.275)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 14.5, 0.0, 7.725)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(43005, 14.5, 0.2, 7.5)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13005, 3005, 13005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    # Central joint node
    ops.node(3006, 18.35, 0.0, 7.5, '-mass', 8.484146756719664, 8.484146756719664, 8.484146756719664, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 18.225, 0.0, 7.5)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(23006, 18.35, 0.0, 7.2)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 18.35, 0.0, 7.8)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(43006, 18.35, 0.125, 7.5)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13006, 3006, 13006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3007, 0.0, 5.8, 7.5, '-mass', 14.2210967754169, 14.2210967754169, 14.2210967754169, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33007, 0.25, 5.8, 7.5)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 0.0, 5.8, 7.2)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 0.0, 5.8, 7.8)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 0.0, 5.675, 7.5)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 0.0, 5.925, 7.5)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13007, 3007, 13007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3008, 3.85, 5.8, 7.5, '-mass', 18.519053897418914, 18.519053897418914, 18.519053897418914, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 3.575, 5.8, 7.5)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(33008, 4.125, 5.8, 7.5)
    ops.element('elasticBeamColumn', 33008, 3008, 33008, 99999, 88888)
    ops.node(23008, 3.85, 5.8, 7.275)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 3.85, 5.8, 7.725)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 3.85, 5.675, 7.5)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 3.85, 5.925, 7.5)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13008, 3008, 13008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3009, 7.7, 5.8, 7.5, '-mass', 19.200861519086267, 19.200861519086267, 19.200861519086267, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53009, 7.4, 5.8, 7.5)
    ops.element('elasticBeamColumn', 53009, 53009, 3009, 99999, 88888)
    ops.node(33009, 8.0, 5.8, 7.5)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 7.7, 5.8, 7.3)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 7.7, 5.8, 7.7)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 7.7, 5.675, 7.5)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 7.7, 5.925, 7.5)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13009, 3009, 13009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3010, 10.65, 5.8, 7.5, '-mass', 19.200861519086267, 19.200861519086267, 19.200861519086267, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 10.35, 5.8, 7.5)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 10.95, 5.8, 7.5)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 10.65, 5.8, 7.3)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 10.65, 5.8, 7.7)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 10.65, 5.675, 7.5)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 10.65, 5.925, 7.5)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13010, 3010, 13010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    # Central joint node
    ops.node(3011, 14.5, 5.8, 7.5, '-mass', 18.519053897418914, 18.519053897418914, 18.519053897418914, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 14.225, 5.8, 7.5)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 14.775, 5.8, 7.5)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 14.5, 5.8, 7.275)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 14.5, 5.8, 7.725)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 14.5, 5.675, 7.5)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 14.5, 5.925, 7.5)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13011, 3011, 13011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    # Central joint node
    ops.node(3012, 18.35, 5.8, 7.5, '-mass', 14.2210967754169, 14.2210967754169, 14.2210967754169, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 18.1, 5.8, 7.5)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 18.35, 5.8, 7.2)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 18.35, 5.8, 7.8)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 18.35, 5.675, 7.5)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 18.35, 5.925, 7.5)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13012, 3012, 13012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3013, 0.0, 11.6, 7.5, '-mass', 13.938527968077452, 13.938527968077452, 13.938527968077452, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.25, 11.6, 7.5)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 11.6, 7.2)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 11.6, 7.8)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 11.475, 7.5)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 11.725, 7.5)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13013, 3013, 13013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3014, 3.85, 11.6, 7.5, '-mass', 17.953916282740014, 17.953916282740014, 17.953916282740014, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 3.575, 11.6, 7.5)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 4.125, 11.6, 7.5)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 3.85, 11.6, 7.275)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 3.85, 11.6, 7.725)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 3.85, 11.475, 7.5)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 3.85, 11.725, 7.5)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13014, 3014, 13014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3015, 7.7, 11.6, 7.5, '-mass', 15.855294968158287, 15.855294968158287, 15.855294968158287, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 7.45, 11.6, 7.5)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 7.95, 11.6, 7.5)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 7.7, 11.6, 7.3)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 7.7, 11.6, 7.7)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 7.7, 11.475, 7.5)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 7.7, 11.725, 7.5)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13015, 3015, 13015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3016, 10.65, 11.6, 7.5, '-mass', 15.855294968158287, 15.855294968158287, 15.855294968158287, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 10.4, 11.6, 7.5)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(33016, 10.9, 11.6, 7.5)
    ops.element('elasticBeamColumn', 33016, 3016, 33016, 99999, 88888)
    ops.node(23016, 10.65, 11.6, 7.3)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 10.65, 11.6, 7.7)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 10.65, 11.475, 7.5)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 10.65, 11.725, 7.5)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13016, 3016, 13016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    # Central joint node
    ops.node(3017, 14.5, 11.6, 7.5, '-mass', 17.953916282740014, 17.953916282740014, 17.953916282740014, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53017, 14.225, 11.6, 7.5)
    ops.element('elasticBeamColumn', 53017, 53017, 3017, 99999, 88888)
    ops.node(33017, 14.775, 11.6, 7.5)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 14.5, 11.6, 7.275)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 14.5, 11.6, 7.725)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 14.5, 11.475, 7.5)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 14.5, 11.725, 7.5)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13017, 3017, 13017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    # Central joint node
    ops.node(3018, 18.35, 11.6, 7.5, '-mass', 13.938527968077452, 13.938527968077452, 13.938527968077452, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 18.1, 11.6, 7.5)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(23018, 18.35, 11.6, 7.2)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 18.35, 11.6, 7.8)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 18.35, 11.475, 7.5)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 18.35, 11.725, 7.5)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13018, 3018, 13018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3019, 0.0, 17.4, 7.5, '-mass', 8.484146756719662, 8.484146756719662, 8.484146756719662, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33019, 0.125, 17.4, 7.5)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 0.0, 17.4, 7.2)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 0.0, 17.4, 7.8)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 0.0, 17.275, 7.5)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13019, 3019, 13019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3020, 3.85, 17.4, 7.5, '-mass', 12.19785518520283, 12.19785518520283, 12.19785518520283, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 3.725, 17.4, 7.5)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(33020, 3.975, 17.4, 7.5)
    ops.element('elasticBeamColumn', 33020, 3020, 33020, 99999, 88888)
    ops.node(23020, 3.85, 17.4, 7.275)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 3.85, 17.4, 7.725)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 3.85, 17.2, 7.5)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13020, 3020, 13020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3021, 7.7, 17.4, 7.5, '-mass', 10.756189787850804, 10.756189787850804, 10.756189787850804, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53021, 7.575, 17.4, 7.5)
    ops.element('elasticBeamColumn', 53021, 53021, 3021, 99999, 88888)
    ops.node(33021, 7.825, 17.4, 7.5)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 7.7, 17.4, 7.3)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 7.7, 17.4, 7.7)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 7.7, 17.225, 7.5)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13021, 3021, 13021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3022, 10.65, 17.4, 7.5, '-mass', 10.756189787850804, 10.756189787850804, 10.756189787850804, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 10.525, 17.4, 7.5)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 10.775, 17.4, 7.5)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 10.65, 17.4, 7.3)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 10.65, 17.4, 7.7)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 10.65, 17.225, 7.5)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13022, 3022, 13022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 3)
    # Central joint node
    ops.node(3023, 14.5, 17.4, 7.5, '-mass', 12.19785518520283, 12.19785518520283, 12.19785518520283, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 14.375, 17.4, 7.5)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 14.625, 17.4, 7.5)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 14.5, 17.4, 7.275)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 14.5, 17.4, 7.725)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 14.5, 17.2, 7.5)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13023, 3023, 13023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 3)
    # Central joint node
    ops.node(3024, 18.35, 17.4, 7.5, '-mass', 8.484146756719662, 8.484146756719662, 8.484146756719662, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 18.225, 17.4, 7.5)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 18.35, 17.4, 7.2)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 18.35, 17.4, 7.8)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 18.35, 17.275, 7.5)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13024, 3024, 13024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 10.0, '-mass', 4.029763474354728, 4.029763474354728, 4.029763474354728, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 10.0)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 9.775)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 10.0)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14001, 4001, 14001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 3.85, 0.0, 10.0, '-mass', 8.373288416599365, 8.373288416599365, 8.373288416599365, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 3.725, 0.0, 10.0)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 3.975, 0.0, 10.0)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 3.85, 0.0, 9.825)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 3.85, 0.2, 10.0)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14002, 4002, 14002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 7.7, 0.0, 10.0, '-mass', 5.186338397902128, 5.186338397902128, 5.186338397902128, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 7.575, 0.0, 10.0)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 7.825, 0.0, 10.0)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 7.7, 0.0, 9.825)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 7.7, 0.25, 10.0)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14003, 4003, 14003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 10.65, 0.0, 10.0, '-mass', 5.186338397902128, 5.186338397902128, 5.186338397902128, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 10.525, 0.0, 10.0)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(34004, 10.775, 0.0, 10.0)
    ops.element('elasticBeamColumn', 34004, 4004, 34004, 99999, 88888)
    ops.node(24004, 10.65, 0.0, 9.825)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 10.65, 0.25, 10.0)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14004, 4004, 14004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    # Central joint node
    ops.node(4005, 14.5, 0.0, 10.0, '-mass', 8.373288416599365, 8.373288416599365, 8.373288416599365, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54005, 14.375, 0.0, 10.0)
    ops.element('elasticBeamColumn', 54005, 54005, 4005, 99999, 88888)
    ops.node(34005, 14.625, 0.0, 10.0)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 14.5, 0.0, 9.825)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(44005, 14.5, 0.2, 10.0)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14005, 4005, 14005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    # Central joint node
    ops.node(4006, 18.35, 0.0, 10.0, '-mass', 4.029763474354729, 4.029763474354729, 4.029763474354729, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 18.225, 0.0, 10.0)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(24006, 18.35, 0.0, 9.775)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(44006, 18.35, 0.125, 10.0)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14006, 4006, 14006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4007, 0.0, 5.8, 10.0, '-mass', 8.059526948709456, 8.059526948709456, 8.059526948709456, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34007, 0.25, 5.8, 10.0)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 0.0, 5.8, 9.775)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 0.0, 5.675, 10.0)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 0.0, 5.925, 10.0)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14007, 4007, 14007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4008, 3.85, 5.8, 10.0, '-mass', 16.55544533472778, 16.55544533472778, 16.55544533472778, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 3.575, 5.8, 10.0)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(34008, 4.125, 5.8, 10.0)
    ops.element('elasticBeamColumn', 34008, 4008, 34008, 99999, 88888)
    ops.node(24008, 3.85, 5.8, 9.8)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 3.85, 5.675, 10.0)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 3.85, 5.925, 10.0)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14008, 4008, 14008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4009, 7.7, 5.8, 10.0, '-mass', 15.23169740083958, 15.23169740083958, 15.23169740083958, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54009, 7.4, 5.8, 10.0)
    ops.element('elasticBeamColumn', 54009, 54009, 4009, 99999, 88888)
    ops.node(34009, 8.0, 5.8, 10.0)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 7.7, 5.8, 9.8)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 7.7, 5.675, 10.0)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 7.7, 5.925, 10.0)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14009, 4009, 14009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4010, 10.65, 5.8, 10.0, '-mass', 15.23169740083958, 15.23169740083958, 15.23169740083958, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 10.35, 5.8, 10.0)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 10.95, 5.8, 10.0)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 10.65, 5.8, 9.8)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 10.65, 5.675, 10.0)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 10.65, 5.925, 10.0)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14010, 4010, 14010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    # Central joint node
    ops.node(4011, 14.5, 5.8, 10.0, '-mass', 16.55544533472778, 16.55544533472778, 16.55544533472778, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 14.225, 5.8, 10.0)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 14.775, 5.8, 10.0)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 14.5, 5.8, 9.8)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 14.5, 5.675, 10.0)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 14.5, 5.925, 10.0)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14011, 4011, 14011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    # Central joint node
    ops.node(4012, 18.35, 5.8, 10.0, '-mass', 8.059526948709458, 8.059526948709458, 8.059526948709458, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 18.1, 5.8, 10.0)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 18.35, 5.8, 9.775)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 18.35, 5.675, 10.0)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 18.35, 5.925, 10.0)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14012, 4012, 14012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4013, 0.0, 11.6, 10.0, '-mass', 7.776958141370007, 7.776958141370007, 7.776958141370007, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.25, 11.6, 10.0)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 11.6, 9.775)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 11.475, 10.0)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 11.725, 10.0)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14013, 4013, 14013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4014, 3.85, 11.6, 10.0, '-mass', 15.990307720048882, 15.990307720048882, 15.990307720048882, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 3.575, 11.6, 10.0)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 4.125, 11.6, 10.0)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 3.85, 11.6, 9.825)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 3.85, 11.475, 10.0)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 3.85, 11.725, 10.0)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14014, 4014, 14014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4015, 7.7, 11.6, 10.0, '-mass', 13.77027967763841, 13.77027967763841, 13.77027967763841, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 7.45, 11.6, 10.0)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 7.95, 11.6, 10.0)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 7.7, 11.6, 9.825)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 7.7, 11.475, 10.0)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 7.7, 11.725, 10.0)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14015, 4015, 14015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4016, 10.65, 11.6, 10.0, '-mass', 13.77027967763841, 13.77027967763841, 13.77027967763841, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 10.4, 11.6, 10.0)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(34016, 10.9, 11.6, 10.0)
    ops.element('elasticBeamColumn', 34016, 4016, 34016, 99999, 88888)
    ops.node(24016, 10.65, 11.6, 9.825)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 10.65, 11.475, 10.0)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 10.65, 11.725, 10.0)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14016, 4016, 14016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    # Central joint node
    ops.node(4017, 14.5, 11.6, 10.0, '-mass', 15.990307720048882, 15.990307720048882, 15.990307720048882, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54017, 14.225, 11.6, 10.0)
    ops.element('elasticBeamColumn', 54017, 54017, 4017, 99999, 88888)
    ops.node(34017, 14.775, 11.6, 10.0)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 14.5, 11.6, 9.825)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 14.5, 11.475, 10.0)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 14.5, 11.725, 10.0)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14017, 4017, 14017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    # Central joint node
    ops.node(4018, 18.35, 11.6, 10.0, '-mass', 7.776958141370007, 7.776958141370007, 7.776958141370007, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 18.1, 11.6, 10.0)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 18.35, 11.6, 9.775)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 18.35, 11.475, 10.0)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 18.35, 11.725, 10.0)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14018, 4018, 14018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4019, 0.0, 17.4, 10.0, '-mass', 4.029763474354728, 4.029763474354728, 4.029763474354728, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 0.125, 17.4, 10.0)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 0.0, 17.4, 9.775)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 0.0, 17.275, 10.0)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14019, 4019, 14019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4020, 3.85, 17.4, 10.0, '-mass', 8.373288416599364, 8.373288416599364, 8.373288416599364, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 3.725, 17.4, 10.0)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(34020, 3.975, 17.4, 10.0)
    ops.element('elasticBeamColumn', 34020, 4020, 34020, 99999, 88888)
    ops.node(24020, 3.85, 17.4, 9.825)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 3.85, 17.2, 10.0)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14020, 4020, 14020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4021, 7.7, 17.4, 10.0, '-mass', 7.211133722611254, 7.211133722611254, 7.211133722611254, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54021, 7.575, 17.4, 10.0)
    ops.element('elasticBeamColumn', 54021, 54021, 4021, 99999, 88888)
    ops.node(34021, 7.825, 17.4, 10.0)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 7.7, 17.4, 9.825)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 7.7, 17.225, 10.0)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14021, 4021, 14021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4022, 10.65, 17.4, 10.0, '-mass', 7.211133722611254, 7.211133722611254, 7.211133722611254, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 10.525, 17.4, 10.0)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 10.775, 17.4, 10.0)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 10.65, 17.4, 9.825)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 10.65, 17.225, 10.0)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14022, 4022, 14022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 4)
    # Central joint node
    ops.node(4023, 14.5, 17.4, 10.0, '-mass', 8.373288416599364, 8.373288416599364, 8.373288416599364, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 14.375, 17.4, 10.0)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 14.625, 17.4, 10.0)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 14.5, 17.4, 9.825)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 14.5, 17.2, 10.0)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14023, 4023, 14023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 4)
    # Central joint node
    ops.node(4024, 18.35, 17.4, 10.0, '-mass', 4.029763474354729, 4.029763474354729, 4.029763474354729, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 18.225, 17.4, 10.0)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 18.35, 17.4, 9.775)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 18.35, 17.275, 10.0)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14024, 4024, 14024, 99999, '-orient', 0, 0, 1, 0, 1, 0)
