import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(4019, 8.5, 0.0, 1.55, '-mass', 4.005237003058102, 4.005237003058102, 4.005237003058102, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 8.675, 0.0, 1.55)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 8.5, 0.0, 1.3)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(74019, 8.5, 0.0, 1.8)
    ops.element('elasticBeamColumn', 74019, 4019, 74019, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 0.5)
    # Central joint node
    ops.node(4020, 11.35, 0.0, 1.55, '-mass', 4.005237003058102, 4.005237003058102, 4.005237003058102, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 11.175, 0.0, 1.55)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 11.35, 0.0, 1.3)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(74020, 11.35, 0.0, 1.8)
    ops.element('elasticBeamColumn', 74020, 4020, 74020, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(4021, 8.5, 0.0, 4.65, '-mass', 4.005237003058102, 4.005237003058102, 4.005237003058102, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 8.675, 0.0, 4.65)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 8.5, 0.0, 4.4)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(74021, 8.5, 0.0, 4.9)
    ops.element('elasticBeamColumn', 74021, 4021, 74021, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    # Central joint node
    ops.node(4022, 11.35, 0.0, 4.65, '-mass', 4.005237003058102, 4.005237003058102, 4.005237003058102, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 11.175, 0.0, 4.65)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(24022, 11.35, 0.0, 4.4)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(74022, 11.35, 0.0, 4.9)
    ops.element('elasticBeamColumn', 74022, 4022, 74022, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(4023, 8.5, 0.0, 7.75, '-mass', 3.620833333333332, 3.620833333333332, 3.620833333333332, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34023, 8.625, 0.0, 7.75)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 8.5, 0.0, 7.55)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(74023, 8.5, 0.0, 7.95)
    ops.element('elasticBeamColumn', 74023, 4023, 74023, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    # Central joint node
    ops.node(4024, 11.35, 0.0, 7.75, '-mass', 3.620833333333332, 3.620833333333332, 3.620833333333332, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 11.225, 0.0, 7.75)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 11.35, 0.0, 7.55)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(74024, 11.35, 0.0, 7.95)
    ops.element('elasticBeamColumn', 74024, 4024, 74024, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(4025, 8.5, 0.0, 10.85, '-mass', 3.620833333333332, 3.620833333333332, 3.620833333333332, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 8.625, 0.0, 10.85)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 8.5, 0.0, 10.65)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 8.5, 0.0, 11.05)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    # Central joint node
    ops.node(4026, 11.35, 0.0, 10.85, '-mass', 3.620833333333332, 3.620833333333332, 3.620833333333332, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 11.225, 0.0, 10.85)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 11.35, 0.0, 10.65)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 11.35, 0.0, 11.05)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.1, '-mass', 8.94676746567473, 8.94676746567473, 8.94676746567473, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.15, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.825)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.375)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.15, 3.1)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11001, 1001, 11001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 4.25, 0.0, 3.1, '-mass', 13.061934523602261, 13.061934523602261, 13.061934523602261, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 4.075, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 4.425, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 4.25, 0.0, 2.9)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 4.25, 0.0, 3.3)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 4.25, 0.175, 3.1)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11002, 1002, 11002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 8.5, 0.0, 3.1, '-mass', 9.510987649160969, 9.510987649160969, 9.510987649160969, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 8.325, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 8.675, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 8.5, 0.0, 2.925)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 8.5, 0.0, 3.275)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 8.5, 0.175, 3.1)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11003, 1003, 11003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 11.35, 0.0, 3.1, '-mass', 9.510987649160969, 9.510987649160969, 9.510987649160969, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 11.175, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(31004, 11.525, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31004, 1004, 31004, 99999, 88888)
    ops.node(21004, 11.35, 0.0, 2.925)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 11.35, 0.0, 3.275)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 11.35, 0.175, 3.1)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11004, 1004, 11004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    # Central joint node
    ops.node(1005, 15.6, 0.0, 3.1, '-mass', 13.061934523602261, 13.061934523602261, 13.061934523602261, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51005, 15.425, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51005, 51005, 1005, 99999, 88888)
    ops.node(31005, 15.775, 0.0, 3.1)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 15.6, 0.0, 2.9)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 15.6, 0.0, 3.3)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(41005, 15.6, 0.175, 3.1)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11005, 1005, 11005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    # Central joint node
    ops.node(1006, 19.85, 0.0, 3.1, '-mass', 8.94676746567473, 8.94676746567473, 8.94676746567473, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 19.7, 0.0, 3.1)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(21006, 19.85, 0.0, 2.825)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 19.85, 0.0, 3.375)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(41006, 19.85, 0.15, 3.1)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11006, 1006, 11006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1007, 0.0, 5.5, 3.1, '-mass', 14.398835644907052, 14.398835644907052, 14.398835644907052, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31007, 0.175, 5.5, 3.1)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 0.0, 5.5, 2.825)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 0.0, 5.5, 3.375)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 0.0, 5.325, 3.1)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 0.0, 5.675, 3.1)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11007, 1007, 11007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1008, 4.25, 5.5, 3.1, '-mass', 19.36199341009953, 19.36199341009953, 19.36199341009953, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 4.05, 5.5, 3.1)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(31008, 4.45, 5.5, 3.1)
    ops.element('elasticBeamColumn', 31008, 1008, 31008, 99999, 88888)
    ops.node(21008, 4.25, 5.5, 2.875)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 4.25, 5.5, 3.325)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 4.25, 5.3, 3.1)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 4.25, 5.7, 3.1)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11008, 1008, 11008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1009, 8.5, 5.5, 3.1, '-mass', 18.889188046095622, 18.889188046095622, 18.889188046095622, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51009, 8.3, 5.5, 3.1)
    ops.element('elasticBeamColumn', 51009, 51009, 1009, 99999, 88888)
    ops.node(31009, 8.7, 5.5, 3.1)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 8.5, 5.5, 2.875)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 8.5, 5.5, 3.325)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 8.5, 5.3, 3.1)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 8.5, 5.7, 3.1)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11009, 1009, 11009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1010, 11.35, 5.5, 3.1, '-mass', 18.889188046095622, 18.889188046095622, 18.889188046095622, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 11.15, 5.5, 3.1)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 11.55, 5.5, 3.1)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 11.35, 5.5, 2.875)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 11.35, 5.5, 3.325)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 11.35, 5.3, 3.1)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 11.35, 5.7, 3.1)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11010, 1010, 11010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    # Central joint node
    ops.node(1011, 15.6, 5.5, 3.1, '-mass', 19.36199341009953, 19.36199341009953, 19.36199341009953, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 15.4, 5.5, 3.1)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 15.8, 5.5, 3.1)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 15.6, 5.5, 2.875)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 15.6, 5.5, 3.325)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 15.6, 5.3, 3.1)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 15.6, 5.7, 3.1)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11011, 1011, 11011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    # Central joint node
    ops.node(1012, 19.85, 5.5, 3.1, '-mass', 14.398835644907052, 14.398835644907052, 14.398835644907052, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 19.675, 5.5, 3.1)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 19.85, 5.5, 2.825)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 19.85, 5.5, 3.375)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 19.85, 5.325, 3.1)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 19.85, 5.675, 3.1)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11012, 1012, 11012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1013, 0.0, 11.0, 3.1, '-mass', 8.94676746567473, 8.94676746567473, 8.94676746567473, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.15, 11.0, 3.1)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 11.0, 2.825)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 11.0, 3.375)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 10.85, 3.1)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11013, 1013, 11013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1014, 4.25, 11.0, 3.1, '-mass', 13.061934523602261, 13.061934523602261, 13.061934523602261, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 4.075, 11.0, 3.1)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 4.425, 11.0, 3.1)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 4.25, 11.0, 2.9)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 4.25, 11.0, 3.3)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 4.25, 10.825, 3.1)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11014, 1014, 11014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1015, 8.5, 11.0, 3.1, '-mass', 10.8081825579948, 10.8081825579948, 10.8081825579948, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 8.35, 11.0, 3.1)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 8.65, 11.0, 3.1)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 8.5, 11.0, 2.925)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 8.5, 11.0, 3.275)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 8.5, 10.85, 3.1)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11015, 1015, 11015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1016, 11.35, 11.0, 3.1, '-mass', 10.8081825579948, 10.8081825579948, 10.8081825579948, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 11.2, 11.0, 3.1)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(31016, 11.5, 11.0, 3.1)
    ops.element('elasticBeamColumn', 31016, 1016, 31016, 99999, 88888)
    ops.node(21016, 11.35, 11.0, 2.925)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 11.35, 11.0, 3.275)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 11.35, 10.85, 3.1)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11016, 1016, 11016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    # Central joint node
    ops.node(1017, 15.6, 11.0, 3.1, '-mass', 13.061934523602261, 13.061934523602261, 13.061934523602261, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51017, 15.425, 11.0, 3.1)
    ops.element('elasticBeamColumn', 51017, 51017, 1017, 99999, 88888)
    ops.node(31017, 15.775, 11.0, 3.1)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 15.6, 11.0, 2.9)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 15.6, 11.0, 3.3)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 15.6, 10.825, 3.1)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11017, 1017, 11017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    # Central joint node
    ops.node(1018, 19.85, 11.0, 3.1, '-mass', 8.94676746567473, 8.94676746567473, 8.94676746567473, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 19.7, 11.0, 3.1)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(21018, 19.85, 11.0, 2.825)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 19.85, 11.0, 3.375)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 19.85, 10.85, 3.1)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11018, 1018, 11018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 6.2, '-mass', 8.790498352524883, 8.790498352524883, 8.790498352524883, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.15, 0.0, 6.2)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 5.925)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.475)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.15, 6.2)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12001, 2001, 12001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 4.25, 0.0, 6.2, '-mass', 12.73043605265425, 12.73043605265425, 12.73043605265425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 4.075, 0.0, 6.2)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 4.425, 0.0, 6.2)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 4.25, 0.0, 6.0)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 4.25, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 4.25, 0.175, 6.2)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12002, 2002, 12002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 8.5, 0.0, 6.2, '-mass', 9.310376028365862, 9.310376028365862, 9.310376028365862, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 8.325, 0.0, 6.2)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 8.675, 0.0, 6.2)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 8.5, 0.0, 6.025)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 8.5, 0.0, 6.375)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 8.5, 0.175, 6.2)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12003, 2003, 12003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 11.35, 0.0, 6.2, '-mass', 9.310376028365862, 9.310376028365862, 9.310376028365862, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 11.175, 0.0, 6.2)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(32004, 11.525, 0.0, 6.2)
    ops.element('elasticBeamColumn', 32004, 2004, 32004, 99999, 88888)
    ops.node(22004, 11.35, 0.0, 6.025)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 11.35, 0.0, 6.375)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 11.35, 0.175, 6.2)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12004, 2004, 12004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    # Central joint node
    ops.node(2005, 15.6, 0.0, 6.2, '-mass', 12.73043605265425, 12.73043605265425, 12.73043605265425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52005, 15.425, 0.0, 6.2)
    ops.element('elasticBeamColumn', 52005, 52005, 2005, 99999, 88888)
    ops.node(32005, 15.775, 0.0, 6.2)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 15.6, 0.0, 6.0)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 15.6, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(42005, 15.6, 0.175, 6.2)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12005, 2005, 12005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    # Central joint node
    ops.node(2006, 19.85, 0.0, 6.2, '-mass', 8.790498352524885, 8.790498352524885, 8.790498352524885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 19.7, 0.0, 6.2)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(22006, 19.85, 0.0, 5.925)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 19.85, 0.0, 6.475)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(42006, 19.85, 0.15, 6.2)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12006, 2006, 12006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2007, 0.0, 5.5, 6.2, '-mass', 14.093331057751092, 14.093331057751092, 14.093331057751092, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32007, 0.175, 5.5, 6.2)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 0.0, 5.5, 5.925)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 0.0, 5.5, 6.475)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 0.0, 5.325, 6.2)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 0.0, 5.675, 6.2)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12007, 2007, 12007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2008, 4.25, 5.5, 6.2, '-mass', 19.063828272484848, 19.063828272484848, 19.063828272484848, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 4.05, 5.5, 6.2)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(32008, 4.45, 5.5, 6.2)
    ops.element('elasticBeamColumn', 32008, 2008, 32008, 99999, 88888)
    ops.node(22008, 4.25, 5.5, 6.0)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 4.25, 5.5, 6.4)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 4.25, 5.3, 6.2)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 4.25, 5.7, 6.2)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12008, 2008, 12008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2009, 8.5, 5.5, 6.2, '-mass', 18.61671098187544, 18.61671098187544, 18.61671098187544, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52009, 8.3, 5.5, 6.2)
    ops.element('elasticBeamColumn', 52009, 52009, 2009, 99999, 88888)
    ops.node(32009, 8.7, 5.5, 6.2)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 8.5, 5.5, 6.0)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 8.5, 5.5, 6.4)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 8.5, 5.3, 6.2)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 8.5, 5.7, 6.2)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12009, 2009, 12009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2010, 11.35, 5.5, 6.2, '-mass', 18.61671098187544, 18.61671098187544, 18.61671098187544, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 11.15, 5.5, 6.2)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 11.55, 5.5, 6.2)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 11.35, 5.5, 6.0)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 11.35, 5.5, 6.4)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 11.35, 5.3, 6.2)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 11.35, 5.7, 6.2)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12010, 2010, 12010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    # Central joint node
    ops.node(2011, 15.6, 5.5, 6.2, '-mass', 19.063828272484848, 19.063828272484848, 19.063828272484848, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 15.4, 5.5, 6.2)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 15.8, 5.5, 6.2)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 15.6, 5.5, 6.0)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 15.6, 5.5, 6.4)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 15.6, 5.3, 6.2)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 15.6, 5.7, 6.2)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12011, 2011, 12011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    # Central joint node
    ops.node(2012, 19.85, 5.5, 6.2, '-mass', 14.093331057751092, 14.093331057751092, 14.093331057751092, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 19.675, 5.5, 6.2)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 19.85, 5.5, 5.925)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 19.85, 5.5, 6.475)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 19.85, 5.325, 6.2)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 19.85, 5.675, 6.2)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12012, 2012, 12012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2013, 0.0, 11.0, 6.2, '-mass', 8.790498352524883, 8.790498352524883, 8.790498352524883, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.15, 11.0, 6.2)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 11.0, 5.925)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 11.0, 6.475)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 10.85, 6.2)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12013, 2013, 12013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2014, 4.25, 11.0, 6.2, '-mass', 12.73043605265425, 12.73043605265425, 12.73043605265425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 4.075, 11.0, 6.2)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 4.425, 11.0, 6.2)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 4.25, 11.0, 6.0)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 4.25, 11.0, 6.4)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 4.25, 10.825, 6.2)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12014, 2014, 12014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2015, 8.5, 11.0, 6.2, '-mass', 10.61705105952385, 10.61705105952385, 10.61705105952385, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 8.35, 11.0, 6.2)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 8.65, 11.0, 6.2)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 8.5, 11.0, 6.025)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 8.5, 11.0, 6.375)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 8.5, 10.85, 6.2)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12015, 2015, 12015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2016, 11.35, 11.0, 6.2, '-mass', 10.61705105952385, 10.61705105952385, 10.61705105952385, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 11.2, 11.0, 6.2)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(32016, 11.5, 11.0, 6.2)
    ops.element('elasticBeamColumn', 32016, 2016, 32016, 99999, 88888)
    ops.node(22016, 11.35, 11.0, 6.025)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 11.35, 11.0, 6.375)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 11.35, 10.85, 6.2)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12016, 2016, 12016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    # Central joint node
    ops.node(2017, 15.6, 11.0, 6.2, '-mass', 12.73043605265425, 12.73043605265425, 12.73043605265425, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52017, 15.425, 11.0, 6.2)
    ops.element('elasticBeamColumn', 52017, 52017, 2017, 99999, 88888)
    ops.node(32017, 15.775, 11.0, 6.2)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 15.6, 11.0, 6.0)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 15.6, 11.0, 6.4)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 15.6, 10.825, 6.2)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12017, 2017, 12017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    # Central joint node
    ops.node(2018, 19.85, 11.0, 6.2, '-mass', 8.790498352524885, 8.790498352524885, 8.790498352524885, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 19.7, 11.0, 6.2)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(22018, 19.85, 11.0, 5.925)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 19.85, 11.0, 6.475)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 19.85, 10.85, 6.2)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12018, 2018, 12018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 9.3, '-mass', 8.686217006959133, 8.686217006959133, 8.686217006959133, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 9.3)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 9.025)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 9.575)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13001, 3001, 13001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 4.25, 0.0, 9.3, '-mass', 12.502913116874435, 12.502913116874435, 12.502913116874435, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 4.125, 0.0, 9.3)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 4.375, 0.0, 9.3)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 4.25, 0.0, 9.1)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 4.25, 0.0, 9.5)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 4.25, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13002, 3002, 13002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 8.5, 0.0, 9.3, '-mass', 9.196614560475954, 9.196614560475954, 9.196614560475954, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 8.375, 0.0, 9.3)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 8.625, 0.0, 9.3)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 8.5, 0.0, 9.125)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 8.5, 0.0, 9.475)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 8.5, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13003, 3003, 13003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 11.35, 0.0, 9.3, '-mass', 9.196614560475954, 9.196614560475954, 9.196614560475954, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 11.225, 0.0, 9.3)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(33004, 11.475, 0.0, 9.3)
    ops.element('elasticBeamColumn', 33004, 3004, 33004, 99999, 88888)
    ops.node(23004, 11.35, 0.0, 9.125)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 11.35, 0.0, 9.475)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 11.35, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13004, 3004, 13004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    # Central joint node
    ops.node(3005, 15.6, 0.0, 9.3, '-mass', 12.502913116874435, 12.502913116874435, 12.502913116874435, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53005, 15.475, 0.0, 9.3)
    ops.element('elasticBeamColumn', 53005, 53005, 3005, 99999, 88888)
    ops.node(33005, 15.725, 0.0, 9.3)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 15.6, 0.0, 9.1)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 15.6, 0.0, 9.5)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(43005, 15.6, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13005, 3005, 13005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    # Central joint node
    ops.node(3006, 19.85, 0.0, 9.3, '-mass', 8.686217006959136, 8.686217006959136, 8.686217006959136, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 19.725, 0.0, 9.3)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(23006, 19.85, 0.0, 9.025)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 19.85, 0.0, 9.575)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(43006, 19.85, 0.125, 9.3)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13006, 3006, 13006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3007, 0.0, 5.5, 9.3, '-mass', 13.787826470595128, 13.787826470595128, 13.787826470595128, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33007, 0.125, 5.5, 9.3)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 0.0, 5.5, 9.025)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 0.0, 5.5, 9.575)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 0.0, 5.375, 9.3)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 0.0, 5.625, 9.3)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13007, 3007, 13007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3008, 4.25, 5.5, 9.3, '-mass', 18.765663134870174, 18.765663134870174, 18.765663134870174, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 4.075, 5.5, 9.3)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(33008, 4.425, 5.5, 9.3)
    ops.element('elasticBeamColumn', 33008, 3008, 33008, 99999, 88888)
    ops.node(23008, 4.25, 5.5, 9.1)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 4.25, 5.5, 9.5)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 4.25, 5.325, 9.3)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 4.25, 5.675, 9.3)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13008, 3008, 13008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3009, 8.5, 5.5, 9.3, '-mass', 18.34423391765526, 18.34423391765526, 18.34423391765526, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53009, 8.325, 5.5, 9.3)
    ops.element('elasticBeamColumn', 53009, 53009, 3009, 99999, 88888)
    ops.node(33009, 8.675, 5.5, 9.3)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 8.5, 5.5, 9.125)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 8.5, 5.5, 9.475)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 8.5, 5.325, 9.3)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 8.5, 5.675, 9.3)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13009, 3009, 13009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3010, 11.35, 5.5, 9.3, '-mass', 18.34423391765526, 18.34423391765526, 18.34423391765526, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 11.175, 5.5, 9.3)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 11.525, 5.5, 9.3)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 11.35, 5.5, 9.125)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 11.35, 5.5, 9.475)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 11.35, 5.325, 9.3)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 11.35, 5.675, 9.3)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13010, 3010, 13010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    # Central joint node
    ops.node(3011, 15.6, 5.5, 9.3, '-mass', 18.765663134870174, 18.765663134870174, 18.765663134870174, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 15.425, 5.5, 9.3)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 15.775, 5.5, 9.3)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 15.6, 5.5, 9.1)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 15.6, 5.5, 9.5)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 15.6, 5.325, 9.3)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 15.6, 5.675, 9.3)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13011, 3011, 13011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    # Central joint node
    ops.node(3012, 19.85, 5.5, 9.3, '-mass', 13.787826470595128, 13.787826470595128, 13.787826470595128, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 19.725, 5.5, 9.3)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 19.85, 5.5, 9.025)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 19.85, 5.5, 9.575)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 19.85, 5.375, 9.3)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 19.85, 5.625, 9.3)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13012, 3012, 13012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3013, 0.0, 11.0, 9.3, '-mass', 8.686217006959133, 8.686217006959133, 8.686217006959133, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 11.0, 9.3)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 11.0, 9.025)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 11.0, 9.575)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 10.875, 9.3)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13013, 3013, 13013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3014, 4.25, 11.0, 9.3, '-mass', 12.502913116874435, 12.502913116874435, 12.502913116874435, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 4.125, 11.0, 9.3)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 4.375, 11.0, 9.3)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 4.25, 11.0, 9.1)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 4.25, 11.0, 9.5)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 4.25, 10.875, 9.3)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13014, 3014, 13014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3015, 8.5, 11.0, 9.3, '-mass', 10.512769713958102, 10.512769713958102, 10.512769713958102, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 8.375, 11.0, 9.3)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 8.625, 11.0, 9.3)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 8.5, 11.0, 9.125)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 8.5, 11.0, 9.475)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 8.5, 10.875, 9.3)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13015, 3015, 13015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3016, 11.35, 11.0, 9.3, '-mass', 10.512769713958102, 10.512769713958102, 10.512769713958102, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 11.225, 11.0, 9.3)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(33016, 11.475, 11.0, 9.3)
    ops.element('elasticBeamColumn', 33016, 3016, 33016, 99999, 88888)
    ops.node(23016, 11.35, 11.0, 9.125)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 11.35, 11.0, 9.475)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 11.35, 10.875, 9.3)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13016, 3016, 13016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    # Central joint node
    ops.node(3017, 15.6, 11.0, 9.3, '-mass', 12.502913116874435, 12.502913116874435, 12.502913116874435, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53017, 15.475, 11.0, 9.3)
    ops.element('elasticBeamColumn', 53017, 53017, 3017, 99999, 88888)
    ops.node(33017, 15.725, 11.0, 9.3)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 15.6, 11.0, 9.1)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 15.6, 11.0, 9.5)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 15.6, 10.875, 9.3)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13017, 3017, 13017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    # Central joint node
    ops.node(3018, 19.85, 11.0, 9.3, '-mass', 8.686217006959136, 8.686217006959136, 8.686217006959136, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 19.725, 11.0, 9.3)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(23018, 19.85, 11.0, 9.025)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 19.85, 11.0, 9.575)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 19.85, 10.875, 9.3)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13018, 3018, 13018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 12.4, '-mass', 4.175895906041702, 4.175895906041702, 4.175895906041702, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 12.4)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 12.2)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 12.4)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14001, 4001, 14001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 4.25, 0.0, 12.4, '-mass', 8.1820670414412, 8.1820670414412, 8.1820670414412, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 4.125, 0.0, 12.4)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 4.375, 0.0, 12.4)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 4.25, 0.0, 12.225)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 4.25, 0.125, 12.4)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14002, 4002, 14002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 8.5, 0.0, 12.4, '-mass', 4.7711558448796225, 4.7711558448796225, 4.7711558448796225, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 8.375, 0.0, 12.4)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 8.625, 0.0, 12.4)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 8.5, 0.0, 12.225)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 8.5, 0.125, 12.4)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14003, 4003, 14003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 11.35, 0.0, 12.4, '-mass', 4.7711558448796225, 4.7711558448796225, 4.7711558448796225, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 11.225, 0.0, 12.4)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(34004, 11.475, 0.0, 12.4)
    ops.element('elasticBeamColumn', 34004, 4004, 34004, 99999, 88888)
    ops.node(24004, 11.35, 0.0, 12.225)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 11.35, 0.125, 12.4)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14004, 4004, 14004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    # Central joint node
    ops.node(4005, 15.6, 0.0, 12.4, '-mass', 8.1820670414412, 8.1820670414412, 8.1820670414412, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54005, 15.475, 0.0, 12.4)
    ops.element('elasticBeamColumn', 54005, 54005, 4005, 99999, 88888)
    ops.node(34005, 15.725, 0.0, 12.4)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 15.6, 0.0, 12.225)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(44005, 15.6, 0.125, 12.4)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14005, 4005, 14005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    # Central joint node
    ops.node(4006, 19.85, 0.0, 12.4, '-mass', 4.175895906041702, 4.175895906041702, 4.175895906041702, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 19.725, 0.0, 12.4)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(24006, 19.85, 0.0, 12.2)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(44006, 19.85, 0.125, 12.4)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14006, 4006, 14006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4007, 0.0, 5.5, 12.4, '-mass', 8.03680710260328, 8.03680710260328, 8.03680710260328, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34007, 0.125, 5.5, 12.4)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 0.0, 5.5, 12.2)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 0.0, 5.375, 12.4)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 0.0, 5.625, 12.4)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14007, 4007, 14007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4008, 4.25, 5.5, 12.4, '-mass', 16.19869065780595, 16.19869065780595, 16.19869065780595, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 4.075, 5.5, 12.4)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(34008, 4.425, 5.5, 12.4)
    ops.element('elasticBeamColumn', 34008, 4008, 34008, 99999, 88888)
    ops.node(24008, 4.25, 5.5, 12.225)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 4.25, 5.325, 12.4)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 4.25, 5.675, 12.4)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14008, 4008, 14008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4009, 8.5, 5.5, 12.4, '-mass', 14.021017811640984, 14.021017811640984, 14.021017811640984, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54009, 8.325, 5.5, 12.4)
    ops.element('elasticBeamColumn', 54009, 54009, 4009, 99999, 88888)
    ops.node(34009, 8.675, 5.5, 12.4)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 8.5, 5.5, 12.225)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 8.5, 5.325, 12.4)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 8.5, 5.675, 12.4)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14009, 4009, 14009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4010, 11.35, 5.5, 12.4, '-mass', 14.021017811640984, 14.021017811640984, 14.021017811640984, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 11.175, 5.5, 12.4)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 11.525, 5.5, 12.4)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 11.35, 5.5, 12.225)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 11.35, 5.325, 12.4)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 11.35, 5.675, 12.4)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14010, 4010, 14010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    # Central joint node
    ops.node(4011, 15.6, 5.5, 12.4, '-mass', 16.19869065780595, 16.19869065780595, 16.19869065780595, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 15.425, 5.5, 12.4)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 15.775, 5.5, 12.4)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 15.6, 5.5, 12.225)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 15.6, 5.325, 12.4)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 15.6, 5.675, 12.4)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14011, 4011, 14011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    # Central joint node
    ops.node(4012, 19.85, 5.5, 12.4, '-mass', 8.03680710260328, 8.03680710260328, 8.03680710260328, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 19.725, 5.5, 12.4)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 19.85, 5.5, 12.2)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 19.85, 5.375, 12.4)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 19.85, 5.625, 12.4)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14012, 4012, 14012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4013, 0.0, 11.0, 12.4, '-mass', 4.175895906041702, 4.175895906041702, 4.175895906041702, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 11.0, 12.4)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 11.0, 12.2)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 10.875, 12.4)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14013, 4013, 14013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4014, 4.25, 11.0, 12.4, '-mass', 8.1820670414412, 8.1820670414412, 8.1820670414412, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 4.125, 11.0, 12.4)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 4.375, 11.0, 12.4)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 4.25, 11.0, 12.225)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 4.25, 10.875, 12.4)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14014, 4014, 14014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4015, 8.5, 11.0, 12.4, '-mass', 6.674594382663504, 6.674594382663504, 6.674594382663504, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 8.375, 11.0, 12.4)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 8.625, 11.0, 12.4)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 8.5, 11.0, 12.225)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 8.5, 10.875, 12.4)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14015, 4015, 14015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4016, 11.35, 11.0, 12.4, '-mass', 6.674594382663504, 6.674594382663504, 6.674594382663504, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 11.225, 11.0, 12.4)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(34016, 11.475, 11.0, 12.4)
    ops.element('elasticBeamColumn', 34016, 4016, 34016, 99999, 88888)
    ops.node(24016, 11.35, 11.0, 12.225)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 11.35, 10.875, 12.4)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14016, 4016, 14016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    # Central joint node
    ops.node(4017, 15.6, 11.0, 12.4, '-mass', 8.1820670414412, 8.1820670414412, 8.1820670414412, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54017, 15.475, 11.0, 12.4)
    ops.element('elasticBeamColumn', 54017, 54017, 4017, 99999, 88888)
    ops.node(34017, 15.725, 11.0, 12.4)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 15.6, 11.0, 12.225)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 15.6, 10.875, 12.4)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14017, 4017, 14017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    # Central joint node
    ops.node(4018, 19.85, 11.0, 12.4, '-mass', 4.175895906041702, 4.175895906041702, 4.175895906041702, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 19.725, 11.0, 12.4)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 19.85, 11.0, 12.2)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 19.85, 10.875, 12.4)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14018, 4018, 14018, 99999, '-orient', 0, 0, 1, 0, 1, 0)
