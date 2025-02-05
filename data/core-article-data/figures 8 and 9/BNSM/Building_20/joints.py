import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 0.5)
    # Central joint node
    ops.node(4025, 0.0, 0.0, 1.675, '-mass', 2.9307148318042815, 2.9307148318042815, 2.9307148318042815, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 0.125, 0.0, 1.675)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 0.0, 0.0, 1.475)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 0.0, 0.0, 1.875)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 0.5)
    # Central joint node
    ops.node(4026, 2.85, 0.0, 1.675, '-mass', 3.1765863914373087, 3.1765863914373087, 3.1765863914373087, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 2.675, 0.0, 1.675)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 2.85, 0.0, 1.475)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 2.85, 0.0, 1.875)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 1.5)
    # Central joint node
    ops.node(4027, 0.0, 0.0, 4.75, '-mass', 2.7840787461773697, 2.7840787461773697, 2.7840787461773697, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34027, 0.125, 0.0, 4.75)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 0.0, 0.0, 4.575)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(74027, 0.0, 0.0, 4.925)
    ops.element('elasticBeamColumn', 74027, 4027, 74027, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 1.5)
    # Central joint node
    ops.node(4028, 2.85, 0.0, 4.75, '-mass', 2.989583333333333, 2.989583333333333, 2.989583333333333, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 2.675, 0.0, 4.75)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 2.85, 0.0, 4.575)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(74028, 2.85, 0.0, 4.925)
    ops.element('elasticBeamColumn', 74028, 4028, 74028, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 2.5)
    # Central joint node
    ops.node(4029, 0.0, 0.0, 7.55, '-mass', 2.7840787461773697, 2.7840787461773697, 2.7840787461773697, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34029, 0.125, 0.0, 7.55)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 0.0, 0.0, 7.375)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(74029, 0.0, 0.0, 7.725)
    ops.element('elasticBeamColumn', 74029, 4029, 74029, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 2.5)
    # Central joint node
    ops.node(4030, 2.85, 0.0, 7.55, '-mass', 2.7840787461773697, 2.7840787461773697, 2.7840787461773697, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 2.725, 0.0, 7.55)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(24030, 2.85, 0.0, 7.375)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(74030, 2.85, 0.0, 7.725)
    ops.element('elasticBeamColumn', 74030, 4030, 74030, 99999, 99999)

    # Joint grid ids (x, y, z): (0, 0, 3.5)
    # Central joint node
    ops.node(4031, 0.0, 0.0, 10.35, '-mass', 2.7840787461773697, 2.7840787461773697, 2.7840787461773697, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34031, 0.125, 0.0, 10.35)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 0.0, 0.0, 10.175)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(74031, 0.0, 0.0, 10.525)
    ops.element('elasticBeamColumn', 74031, 4031, 74031, 99999, 99999)

    # Joint grid ids (x, y, z): (1, 0, 3.5)
    # Central joint node
    ops.node(4032, 2.85, 0.0, 10.35, '-mass', 2.7840787461773697, 2.7840787461773697, 2.7840787461773697, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 2.725, 0.0, 10.35)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 2.85, 0.0, 10.175)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(74032, 2.85, 0.0, 10.525)
    ops.element('elasticBeamColumn', 74032, 4032, 74032, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 3.35, '-mass', 2.6025739041794087, 2.6025739041794087, 2.6025739041794087, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.125, 0.0, 3.35)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 3.1)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.6)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.125, 3.35)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11001, 1001, 11001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 2.85, 0.0, 3.35, '-mass', 8.570912726670983, 8.570912726670983, 8.570912726670983, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 2.675, 0.0, 3.35)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 3.025, 0.0, 3.35)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 2.85, 0.0, 3.1)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 2.85, 0.0, 3.6)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 2.85, 0.175, 3.35)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11002, 1002, 11002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 8.15, 0.0, 3.35, '-mass', 12.595240336114642, 12.595240336114642, 12.595240336114642, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 7.975, 0.0, 3.35)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 8.325, 0.0, 3.35)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 8.15, 0.0, 3.1)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 8.15, 0.0, 3.6)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 8.15, 0.175, 3.35)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11003, 1003, 11003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 13.45, 0.0, 3.35, '-mass', 8.21716654930095, 8.21716654930095, 8.21716654930095, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 13.3, 0.0, 3.35)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(21004, 13.45, 0.0, 3.1)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 13.45, 0.0, 3.6)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 13.45, 0.15, 3.35)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11004, 1004, 11004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1005, 0.0, 3.85, 3.35, '-mass', 8.43765035055677, 8.43765035055677, 8.43765035055677, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31005, 0.15, 3.85, 3.35)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 0.0, 3.85, 3.15)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 0.0, 3.85, 3.55)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(61005, 0.0, 3.7, 3.35)
    ops.element('elasticBeamColumn', 61005, 61005, 1005, 99999, 77777)
    ops.node(41005, 0.0, 4.0, 3.35)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11005, 1005, 11005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1006, 2.85, 3.85, 3.35, '-mass', 14.623002817150516, 14.623002817150516, 14.623002817150516, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 2.675, 3.85, 3.35)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(31006, 3.025, 3.85, 3.35)
    ops.element('elasticBeamColumn', 31006, 1006, 31006, 99999, 88888)
    ops.node(21006, 2.85, 3.85, 3.15)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 2.85, 3.85, 3.55)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(61006, 2.85, 3.675, 3.35)
    ops.element('elasticBeamColumn', 61006, 61006, 1006, 99999, 77777)
    ops.node(41006, 2.85, 4.025, 3.35)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11006, 1006, 11006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1007, 8.15, 3.85, 3.35, '-mass', 15.927228888335298, 15.927228888335298, 15.927228888335298, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51007, 7.975, 3.85, 3.35)
    ops.element('elasticBeamColumn', 51007, 51007, 1007, 99999, 88888)
    ops.node(31007, 8.325, 3.85, 3.35)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 8.15, 3.85, 3.15)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 8.15, 3.85, 3.55)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 8.15, 3.675, 3.35)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 8.15, 4.025, 3.35)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11007, 1007, 11007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1008, 13.45, 3.85, 3.35, '-mass', 11.830918215829218, 11.830918215829218, 11.830918215829218, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 13.275, 3.85, 3.35)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(21008, 13.45, 3.85, 3.15)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 13.45, 3.85, 3.55)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 13.45, 3.675, 3.35)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 13.45, 4.025, 3.35)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11008, 1008, 11008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1009, 0.0, 7.7, 3.35, '-mass', 7.83043576737246, 7.83043576737246, 7.83043576737246, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31009, 0.125, 7.7, 3.35)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 0.0, 7.7, 3.15)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 0.0, 7.7, 3.55)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 0.0, 7.575, 3.35)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 0.0, 7.825, 3.35)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11009, 1009, 11009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1010, 2.85, 7.7, 3.35, '-mass', 12.849070598899948, 12.849070598899948, 12.849070598899948, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 2.675, 7.7, 3.35)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 3.025, 7.7, 3.35)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 2.85, 7.7, 3.15)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 2.85, 7.7, 3.55)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 2.85, 7.525, 3.35)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 2.85, 7.875, 3.35)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11010, 1010, 11010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1011, 8.15, 7.7, 3.35, '-mass', 15.927228888335298, 15.927228888335298, 15.927228888335298, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 7.975, 7.7, 3.35)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 8.325, 7.7, 3.35)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 8.15, 7.7, 3.15)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 8.15, 7.7, 3.55)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 8.15, 7.525, 3.35)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 8.15, 7.875, 3.35)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11011, 1011, 11011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1012, 13.45, 7.7, 3.35, '-mass', 11.830918215829218, 11.830918215829218, 11.830918215829218, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 13.275, 7.7, 3.35)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 13.45, 7.7, 3.15)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 13.45, 7.7, 3.55)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 13.45, 7.525, 3.35)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 13.45, 7.875, 3.35)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11012, 1012, 11012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1013, 0.0, 11.55, 3.35, '-mass', 7.83043576737246, 7.83043576737246, 7.83043576737246, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.125, 11.55, 3.35)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 11.55, 3.15)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 11.55, 3.55)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 11.425, 3.35)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 11.675, 3.35)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11013, 1013, 11013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1014, 2.85, 11.55, 3.35, '-mass', 12.849070598899948, 12.849070598899948, 12.849070598899948, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 2.675, 11.55, 3.35)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 3.025, 11.55, 3.35)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 2.85, 11.55, 3.15)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 2.85, 11.55, 3.55)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 2.85, 11.375, 3.35)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 2.85, 11.725, 3.35)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11014, 1014, 11014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1015, 8.15, 11.55, 3.35, '-mass', 15.927228888335298, 15.927228888335298, 15.927228888335298, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 7.975, 11.55, 3.35)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 8.325, 11.55, 3.35)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 8.15, 11.55, 3.15)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 8.15, 11.55, 3.55)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 8.15, 11.375, 3.35)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 8.15, 11.725, 3.35)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11015, 1015, 11015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1016, 13.45, 11.55, 3.35, '-mass', 11.830918215829216, 11.830918215829216, 11.830918215829216, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 13.275, 11.55, 3.35)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(21016, 13.45, 11.55, 3.15)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 13.45, 11.55, 3.55)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 13.45, 11.375, 3.35)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 13.45, 11.725, 3.35)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11016, 1016, 11016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 1)
    # Central joint node
    ops.node(1017, 0.0, 15.4, 3.35, '-mass', 7.830435767372459, 7.830435767372459, 7.830435767372459, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31017, 0.125, 15.4, 3.35)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 0.0, 15.4, 3.15)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 0.0, 15.4, 3.55)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 0.0, 15.275, 3.35)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 0.0, 15.525, 3.35)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11017, 1017, 11017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 1)
    # Central joint node
    ops.node(1018, 2.85, 15.4, 3.35, '-mass', 12.849070598899948, 12.849070598899948, 12.849070598899948, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 2.675, 15.4, 3.35)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(31018, 3.025, 15.4, 3.35)
    ops.element('elasticBeamColumn', 31018, 1018, 31018, 99999, 88888)
    ops.node(21018, 2.85, 15.4, 3.15)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 2.85, 15.4, 3.55)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 2.85, 15.225, 3.35)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 2.85, 15.575, 3.35)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11018, 1018, 11018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 1)
    # Central joint node
    ops.node(1019, 8.15, 15.4, 3.35, '-mass', 15.927228888335298, 15.927228888335298, 15.927228888335298, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51019, 7.975, 15.4, 3.35)
    ops.element('elasticBeamColumn', 51019, 51019, 1019, 99999, 88888)
    ops.node(31019, 8.325, 15.4, 3.35)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 8.15, 15.4, 3.15)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 8.15, 15.4, 3.55)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 8.15, 15.225, 3.35)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    ops.node(41019, 8.15, 15.575, 3.35)
    ops.element('elasticBeamColumn', 41019, 1019, 41019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11019, 1019, 11019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 1)
    # Central joint node
    ops.node(1020, 13.45, 15.4, 3.35, '-mass', 11.830918215829216, 11.830918215829216, 11.830918215829216, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 13.275, 15.4, 3.35)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(21020, 13.45, 15.4, 3.15)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 13.45, 15.4, 3.55)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 13.45, 15.225, 3.35)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    ops.node(41020, 13.45, 15.575, 3.35)
    ops.element('elasticBeamColumn', 41020, 1020, 41020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11020, 1020, 11020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 1)
    # Central joint node
    ops.node(1021, 0.0, 19.25, 3.35, '-mass', 5.271716354634242, 5.271716354634242, 5.271716354634242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31021, 0.125, 19.25, 3.35)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 0.0, 19.25, 3.1)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 0.0, 19.25, 3.6)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 0.0, 19.125, 3.35)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11021, 1021, 11021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 1)
    # Central joint node
    ops.node(1022, 2.85, 19.25, 3.35, '-mass', 9.84764946866506, 9.84764946866506, 9.84764946866506, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 2.7, 19.25, 3.35)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 3.0, 19.25, 3.35)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 2.85, 19.25, 3.1)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 2.85, 19.25, 3.6)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 2.85, 19.1, 3.35)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11022, 1022, 11022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 1)
    # Central joint node
    ops.node(1023, 8.15, 19.25, 3.35, '-mass', 12.595240336114642, 12.595240336114642, 12.595240336114642, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 7.975, 19.25, 3.35)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 8.325, 19.25, 3.35)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 8.15, 19.25, 3.1)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 8.15, 19.25, 3.6)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 8.15, 19.075, 3.35)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11023, 1023, 11023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 1)
    # Central joint node
    ops.node(1024, 13.45, 19.25, 3.35, '-mass', 8.21716654930095, 8.21716654930095, 8.21716654930095, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 13.3, 19.25, 3.35)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 13.45, 19.25, 3.1)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 13.45, 19.25, 3.6)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 13.45, 19.1, 3.35)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11024, 1024, 11024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 6.15, '-mass', 2.5815494393476044, 2.5815494393476044, 2.5815494393476044, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.125, 0.0, 6.15)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 5.9)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.125, 6.15)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12001, 2001, 12001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 2.85, 0.0, 6.15, '-mass', 8.379857680799422, 8.379857680799422, 8.379857680799422, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 2.675, 0.0, 6.15)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 3.025, 0.0, 6.15)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 2.85, 0.0, 5.9)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 2.85, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 2.85, 0.175, 6.15)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12002, 2002, 12002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 8.15, 0.0, 6.15, '-mass', 12.307319846818007, 12.307319846818007, 12.307319846818007, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 7.975, 0.0, 6.15)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 8.325, 0.0, 6.15)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 8.15, 0.0, 5.9)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 8.15, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 8.15, 0.175, 6.15)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12003, 2003, 12003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 13.45, 0.0, 6.15, '-mass', 7.968236885692387, 7.968236885692387, 7.968236885692387, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 13.3, 0.0, 6.15)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(22004, 13.45, 0.0, 5.9)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 13.45, 0.0, 6.4)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 13.45, 0.15, 6.15)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12004, 2004, 12004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2005, 0.0, 3.85, 6.15, '-mass', 8.28291028939469, 8.28291028939469, 8.28291028939469, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32005, 0.15, 3.85, 6.15)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 0.0, 3.85, 5.95)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 0.0, 3.85, 6.35)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(62005, 0.0, 3.7, 6.15)
    ops.element('elasticBeamColumn', 62005, 62005, 2005, 99999, 77777)
    ops.node(42005, 0.0, 4.0, 6.15)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12005, 2005, 12005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2006, 2.85, 3.85, 6.15, '-mass', 14.240892725407399, 14.240892725407399, 14.240892725407399, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 2.675, 3.85, 6.15)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(32006, 3.025, 3.85, 6.15)
    ops.element('elasticBeamColumn', 32006, 2006, 32006, 99999, 88888)
    ops.node(22006, 2.85, 3.85, 5.95)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 2.85, 3.85, 6.35)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(62006, 2.85, 3.675, 6.15)
    ops.element('elasticBeamColumn', 62006, 62006, 2006, 99999, 77777)
    ops.node(42006, 2.85, 4.025, 6.15)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12006, 2006, 12006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2007, 8.15, 3.85, 6.15, '-mass', 15.639308399038663, 15.639308399038663, 15.639308399038663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52007, 7.975, 3.85, 6.15)
    ops.element('elasticBeamColumn', 52007, 52007, 2007, 99999, 88888)
    ops.node(32007, 8.325, 3.85, 6.15)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 8.15, 3.85, 5.95)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 8.15, 3.85, 6.35)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 8.15, 3.675, 6.15)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 8.15, 4.025, 6.15)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12007, 2007, 12007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2008, 13.45, 3.85, 6.15, '-mass', 11.354618521639615, 11.354618521639615, 11.354618521639615, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 13.275, 3.85, 6.15)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(22008, 13.45, 3.85, 5.95)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 13.45, 3.85, 6.35)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 13.45, 3.675, 6.15)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 13.45, 4.025, 6.15)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12008, 2008, 12008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2009, 0.0, 7.7, 6.15, '-mass', 7.788386837708852, 7.788386837708852, 7.788386837708852, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32009, 0.125, 7.7, 6.15)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 0.0, 7.7, 5.95)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 0.0, 7.7, 6.35)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 0.0, 7.575, 6.15)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 0.0, 7.825, 6.15)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12009, 2009, 12009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2010, 2.85, 7.7, 6.15, '-mass', 12.466960507156829, 12.466960507156829, 12.466960507156829, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 2.675, 7.7, 6.15)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 3.025, 7.7, 6.15)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 2.85, 7.7, 5.95)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 2.85, 7.7, 6.35)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 2.85, 7.525, 6.15)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 2.85, 7.875, 6.15)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12010, 2010, 12010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2011, 8.15, 7.7, 6.15, '-mass', 15.639308399038663, 15.639308399038663, 15.639308399038663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 7.975, 7.7, 6.15)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 8.325, 7.7, 6.15)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 8.15, 7.7, 5.95)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 8.15, 7.7, 6.35)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 8.15, 7.525, 6.15)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 8.15, 7.875, 6.15)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12011, 2011, 12011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2012, 13.45, 7.7, 6.15, '-mass', 11.354618521639615, 11.354618521639615, 11.354618521639615, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 13.275, 7.7, 6.15)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 13.45, 7.7, 5.95)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 13.45, 7.7, 6.35)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 13.45, 7.525, 6.15)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 13.45, 7.875, 6.15)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12012, 2012, 12012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2013, 0.0, 11.55, 6.15, '-mass', 7.788386837708852, 7.788386837708852, 7.788386837708852, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.125, 11.55, 6.15)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 11.55, 5.95)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 11.55, 6.35)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 11.425, 6.15)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 11.675, 6.15)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12013, 2013, 12013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2014, 2.85, 11.55, 6.15, '-mass', 12.466960507156829, 12.466960507156829, 12.466960507156829, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 2.675, 11.55, 6.15)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 3.025, 11.55, 6.15)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 2.85, 11.55, 5.95)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 2.85, 11.55, 6.35)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 2.85, 11.375, 6.15)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 2.85, 11.725, 6.15)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12014, 2014, 12014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2015, 8.15, 11.55, 6.15, '-mass', 15.639308399038663, 15.639308399038663, 15.639308399038663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 7.975, 11.55, 6.15)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 8.325, 11.55, 6.15)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 8.15, 11.55, 5.95)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 8.15, 11.55, 6.35)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 8.15, 11.375, 6.15)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 8.15, 11.725, 6.15)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12015, 2015, 12015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2016, 13.45, 11.55, 6.15, '-mass', 11.354618521639615, 11.354618521639615, 11.354618521639615, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 13.275, 11.55, 6.15)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(22016, 13.45, 11.55, 5.95)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 13.45, 11.55, 6.35)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 13.45, 11.375, 6.15)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 13.45, 11.725, 6.15)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12016, 2016, 12016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 2)
    # Central joint node
    ops.node(2017, 0.0, 15.4, 6.15, '-mass', 7.788386837708851, 7.788386837708851, 7.788386837708851, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32017, 0.125, 15.4, 6.15)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 0.0, 15.4, 5.95)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 0.0, 15.4, 6.35)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 0.0, 15.275, 6.15)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 0.0, 15.525, 6.15)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12017, 2017, 12017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 2)
    # Central joint node
    ops.node(2018, 2.85, 15.4, 6.15, '-mass', 12.466960507156829, 12.466960507156829, 12.466960507156829, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 2.675, 15.4, 6.15)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(32018, 3.025, 15.4, 6.15)
    ops.element('elasticBeamColumn', 32018, 2018, 32018, 99999, 88888)
    ops.node(22018, 2.85, 15.4, 5.95)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 2.85, 15.4, 6.35)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 2.85, 15.225, 6.15)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 2.85, 15.575, 6.15)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12018, 2018, 12018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 2)
    # Central joint node
    ops.node(2019, 8.15, 15.4, 6.15, '-mass', 15.639308399038663, 15.639308399038663, 15.639308399038663, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52019, 7.975, 15.4, 6.15)
    ops.element('elasticBeamColumn', 52019, 52019, 2019, 99999, 88888)
    ops.node(32019, 8.325, 15.4, 6.15)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 8.15, 15.4, 5.95)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 8.15, 15.4, 6.35)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 8.15, 15.225, 6.15)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    ops.node(42019, 8.15, 15.575, 6.15)
    ops.element('elasticBeamColumn', 42019, 2019, 42019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12019, 2019, 12019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 2)
    # Central joint node
    ops.node(2020, 13.45, 15.4, 6.15, '-mass', 11.354618521639615, 11.354618521639615, 11.354618521639615, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 13.275, 15.4, 6.15)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(22020, 13.45, 15.4, 5.95)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 13.45, 15.4, 6.35)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 13.45, 15.225, 6.15)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    ops.node(42020, 13.45, 15.575, 6.15)
    ops.element('elasticBeamColumn', 42020, 2020, 42020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12020, 2020, 12020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 2)
    # Central joint node
    ops.node(2021, 0.0, 19.25, 6.15, '-mass', 5.229667424970633, 5.229667424970633, 5.229667424970633, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32021, 0.125, 19.25, 6.15)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 0.0, 19.25, 5.9)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 0.0, 19.25, 6.4)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 0.0, 19.125, 6.15)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12021, 2021, 12021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 2)
    # Central joint node
    ops.node(2022, 2.85, 19.25, 6.15, '-mass', 9.645814606279739, 9.645814606279739, 9.645814606279739, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 2.7, 19.25, 6.15)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 3.0, 19.25, 6.15)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 2.85, 19.25, 5.9)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 2.85, 19.25, 6.4)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 2.85, 19.1, 6.15)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12022, 2022, 12022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 2)
    # Central joint node
    ops.node(2023, 8.15, 19.25, 6.15, '-mass', 12.307319846818007, 12.307319846818007, 12.307319846818007, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 7.975, 19.25, 6.15)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 8.325, 19.25, 6.15)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 8.15, 19.25, 5.9)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 8.15, 19.25, 6.4)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 8.15, 19.075, 6.15)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12023, 2023, 12023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 2)
    # Central joint node
    ops.node(2024, 13.45, 19.25, 6.15, '-mass', 7.968236885692387, 7.968236885692387, 7.968236885692387, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 13.3, 19.25, 6.15)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 13.45, 19.25, 5.9)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 13.45, 19.25, 6.4)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 13.45, 19.1, 6.15)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12024, 2024, 12024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 8.95, '-mass', 2.487359836901121, 2.487359836901121, 2.487359836901121, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 8.95)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 8.7)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 9.2)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 8.95)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13001, 3001, 13001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 2.85, 0.0, 8.95, '-mass', 8.159368384163336, 8.159368384163336, 8.159368384163336, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 2.725, 0.0, 8.95)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 2.975, 0.0, 8.95)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 2.85, 0.0, 8.7)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 2.85, 0.0, 9.2)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 2.85, 0.125, 8.95)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13002, 3002, 13002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 8.15, 0.0, 8.95, '-mass', 12.101815259662045, 12.101815259662045, 12.101815259662045, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 8.025, 0.0, 8.95)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 8.275, 0.0, 8.95)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 8.15, 0.0, 8.7)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 8.15, 0.0, 9.2)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 8.15, 0.125, 8.95)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13003, 3003, 13003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 13.45, 0.0, 8.95, '-mass', 7.77985768079942, 7.77985768079942, 7.77985768079942, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 13.325, 0.0, 8.95)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(23004, 13.45, 0.0, 8.7)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 13.45, 0.0, 9.2)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 13.45, 0.125, 8.95)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13004, 3004, 13004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3005, 0.0, 3.85, 8.95, '-mass', 7.869607537101112, 7.869607537101112, 7.869607537101112, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33005, 0.125, 3.85, 8.95)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 0.0, 3.85, 8.725)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 0.0, 3.85, 9.175)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(63005, 0.0, 3.725, 8.95)
    ops.element('elasticBeamColumn', 63005, 63005, 3005, 99999, 77777)
    ops.node(43005, 0.0, 3.975, 8.95)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13005, 3005, 13005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3006, 2.85, 3.85, 8.95, '-mass', 13.426060921126052, 13.426060921126052, 13.426060921126052, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 2.725, 3.85, 8.95)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(33006, 2.975, 3.85, 8.95)
    ops.element('elasticBeamColumn', 33006, 3006, 33006, 99999, 88888)
    ops.node(23006, 2.85, 3.85, 8.725)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 2.85, 3.85, 9.175)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(63006, 2.85, 3.725, 8.95)
    ops.element('elasticBeamColumn', 63006, 63006, 3006, 99999, 77777)
    ops.node(43006, 2.85, 3.975, 8.95)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13006, 3006, 13006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3007, 8.15, 3.85, 8.95, '-mass', 14.947565279772608, 14.947565279772608, 14.947565279772608, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53007, 8.025, 3.85, 8.95)
    ops.element('elasticBeamColumn', 53007, 53007, 3007, 99999, 88888)
    ops.node(33007, 8.275, 3.85, 8.95)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 8.15, 3.85, 8.725)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 8.15, 3.85, 9.175)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 8.15, 3.725, 8.95)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 8.15, 3.975, 8.95)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13007, 3007, 13007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3008, 13.45, 3.85, 8.95, '-mass', 10.71761546353564, 10.71761546353564, 10.71761546353564, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 13.325, 3.85, 8.95)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(23008, 13.45, 3.85, 8.725)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 13.45, 3.85, 9.175)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 13.45, 3.725, 8.95)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 13.45, 3.975, 8.95)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13008, 3008, 13008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3009, 0.0, 7.7, 8.95, '-mass', 7.469273687861756, 7.469273687861756, 7.469273687861756, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33009, 0.125, 7.7, 8.95)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 0.0, 7.7, 8.725)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 0.0, 7.7, 9.175)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 0.0, 7.575, 8.95)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 0.0, 7.825, 8.95)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13009, 3009, 13009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3010, 2.85, 7.7, 8.95, '-mass', 11.652128702875482, 11.652128702875482, 11.652128702875482, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 2.725, 7.7, 8.95)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 2.975, 7.7, 8.95)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 2.85, 7.7, 8.725)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 2.85, 7.7, 9.175)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 2.85, 7.575, 8.95)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 2.85, 7.825, 8.95)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13010, 3010, 13010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3011, 8.15, 7.7, 8.95, '-mass', 14.947565279772608, 14.947565279772608, 14.947565279772608, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 8.025, 7.7, 8.95)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 8.275, 7.7, 8.95)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 8.15, 7.7, 8.725)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 8.15, 7.7, 9.175)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 8.15, 7.575, 8.95)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 8.15, 7.825, 8.95)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13011, 3011, 13011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3012, 13.45, 7.7, 8.95, '-mass', 10.71761546353564, 10.71761546353564, 10.71761546353564, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 13.325, 7.7, 8.95)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 13.45, 7.7, 8.725)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 13.45, 7.7, 9.175)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 13.45, 7.575, 8.95)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 13.45, 7.825, 8.95)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13012, 3012, 13012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3013, 0.0, 11.55, 8.95, '-mass', 7.469273687861756, 7.469273687861756, 7.469273687861756, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.125, 11.55, 8.95)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 11.55, 8.725)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 11.55, 9.175)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 11.425, 8.95)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 11.675, 8.95)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13013, 3013, 13013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3014, 2.85, 11.55, 8.95, '-mass', 11.652128702875482, 11.652128702875482, 11.652128702875482, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 2.725, 11.55, 8.95)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 2.975, 11.55, 8.95)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 2.85, 11.55, 8.725)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 2.85, 11.55, 9.175)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 2.85, 11.425, 8.95)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 2.85, 11.675, 8.95)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13014, 3014, 13014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3015, 8.15, 11.55, 8.95, '-mass', 14.947565279772608, 14.947565279772608, 14.947565279772608, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 8.025, 11.55, 8.95)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 8.275, 11.55, 8.95)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 8.15, 11.55, 8.725)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 8.15, 11.55, 9.175)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 8.15, 11.425, 8.95)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 8.15, 11.675, 8.95)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13015, 3015, 13015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3016, 13.45, 11.55, 8.95, '-mass', 10.71761546353564, 10.71761546353564, 10.71761546353564, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 13.325, 11.55, 8.95)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(23016, 13.45, 11.55, 8.725)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 13.45, 11.55, 9.175)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 13.45, 11.425, 8.95)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 13.45, 11.675, 8.95)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13016, 3016, 13016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 3)
    # Central joint node
    ops.node(3017, 0.0, 15.4, 8.95, '-mass', 7.4692736878617545, 7.4692736878617545, 7.4692736878617545, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33017, 0.125, 15.4, 8.95)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 0.0, 15.4, 8.725)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 0.0, 15.4, 9.175)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 0.0, 15.275, 8.95)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 0.0, 15.525, 8.95)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13017, 3017, 13017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 3)
    # Central joint node
    ops.node(3018, 2.85, 15.4, 8.95, '-mass', 11.652128702875482, 11.652128702875482, 11.652128702875482, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 2.725, 15.4, 8.95)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(33018, 2.975, 15.4, 8.95)
    ops.element('elasticBeamColumn', 33018, 3018, 33018, 99999, 88888)
    ops.node(23018, 2.85, 15.4, 8.725)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 2.85, 15.4, 9.175)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 2.85, 15.275, 8.95)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 2.85, 15.525, 8.95)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13018, 3018, 13018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 3)
    # Central joint node
    ops.node(3019, 8.15, 15.4, 8.95, '-mass', 14.947565279772608, 14.947565279772608, 14.947565279772608, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53019, 8.025, 15.4, 8.95)
    ops.element('elasticBeamColumn', 53019, 53019, 3019, 99999, 88888)
    ops.node(33019, 8.275, 15.4, 8.95)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 8.15, 15.4, 8.725)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 8.15, 15.4, 9.175)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 8.15, 15.275, 8.95)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    ops.node(43019, 8.15, 15.525, 8.95)
    ops.element('elasticBeamColumn', 43019, 3019, 43019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13019, 3019, 13019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 3)
    # Central joint node
    ops.node(3020, 13.45, 15.4, 8.95, '-mass', 10.71761546353564, 10.71761546353564, 10.71761546353564, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 13.325, 15.4, 8.95)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(23020, 13.45, 15.4, 8.725)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 13.45, 15.4, 9.175)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 13.45, 15.275, 8.95)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    ops.node(43020, 13.45, 15.525, 8.95)
    ops.element('elasticBeamColumn', 43020, 3020, 43020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13020, 3020, 13020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 3)
    # Central joint node
    ops.node(3021, 0.0, 19.25, 8.95, '-mass', 5.135477822524149, 5.135477822524149, 5.135477822524149, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33021, 0.125, 19.25, 8.95)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 0.0, 19.25, 8.7)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 0.0, 19.25, 9.2)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 0.0, 19.125, 8.95)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13021, 3021, 13021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 3)
    # Central joint node
    ops.node(3022, 2.85, 19.25, 8.95, '-mass', 9.433888000775152, 9.433888000775152, 9.433888000775152, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 2.725, 19.25, 8.95)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 2.975, 19.25, 8.95)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 2.85, 19.25, 8.7)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 2.85, 19.25, 9.2)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 2.85, 19.125, 8.95)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13022, 3022, 13022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 3)
    # Central joint node
    ops.node(3023, 8.15, 19.25, 8.95, '-mass', 12.101815259662045, 12.101815259662045, 12.101815259662045, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 8.025, 19.25, 8.95)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 8.275, 19.25, 8.95)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 8.15, 19.25, 8.7)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 8.15, 19.25, 9.2)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 8.15, 19.125, 8.95)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13023, 3023, 13023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 3)
    # Central joint node
    ops.node(3024, 13.45, 19.25, 8.95, '-mass', 7.77985768079942, 7.77985768079942, 7.77985768079942, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 13.325, 19.25, 8.95)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 13.45, 19.25, 8.7)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 13.45, 19.25, 9.2)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 13.45, 19.125, 8.95)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13024, 3024, 13024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 11.75, '-mass', 0.6685015290519878, 0.6685015290519878, 0.6685015290519878, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 11.75)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 11.55)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 11.75)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14001, 4001, 14001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 2.85, 0.0, 11.75, '-mass', 3.7543989652030905, 3.7543989652030905, 3.7543989652030905, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 2.725, 0.0, 11.75)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 2.975, 0.0, 11.75)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 2.85, 0.0, 11.55)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 2.85, 0.125, 11.75)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14002, 4002, 14002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 8.15, 0.0, 11.75, '-mass', 6.574241355482633, 6.574241355482633, 6.574241355482633, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 8.025, 0.0, 11.75)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 8.275, 0.0, 11.75)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 8.15, 0.0, 11.55)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 8.15, 0.125, 11.75)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14003, 4003, 14003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 13.45, 0.0, 11.75, '-mass', 3.535438720554772, 3.535438720554772, 3.535438720554772, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 13.325, 0.0, 11.75)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(24004, 13.45, 0.0, 11.55)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 13.45, 0.125, 11.75)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14004, 4004, 14004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4005, 0.0, 3.85, 11.75, '-mass', 4.404023948925781, 4.404023948925781, 4.404023948925781, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34005, 0.125, 3.85, 11.75)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 0.0, 3.85, 11.55)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(64005, 0.0, 3.725, 11.75)
    ops.element('elasticBeamColumn', 64005, 64005, 4005, 99999, 77777)
    ops.node(44005, 0.0, 3.975, 11.75)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14005, 4005, 14005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4006, 2.85, 3.85, 11.75, '-mass', 10.57581882122799, 10.57581882122799, 10.57581882122799, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 2.725, 3.85, 11.75)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(34006, 2.975, 3.85, 11.75)
    ops.element('elasticBeamColumn', 34006, 4006, 34006, 99999, 88888)
    ops.node(24006, 2.85, 3.85, 11.55)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(64006, 2.85, 3.725, 11.75)
    ops.element('elasticBeamColumn', 64006, 64006, 4006, 99999, 77777)
    ops.node(44006, 2.85, 3.975, 11.75)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14006, 4006, 14006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4007, 8.15, 3.85, 11.75, '-mass', 12.934415432677806, 12.934415432677806, 12.934415432677806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54007, 8.025, 3.85, 11.75)
    ops.element('elasticBeamColumn', 54007, 54007, 4007, 99999, 88888)
    ops.node(34007, 8.275, 3.85, 11.75)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 8.15, 3.85, 11.55)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 8.15, 3.725, 11.75)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 8.15, 3.975, 11.75)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14007, 4007, 14007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4008, 13.45, 3.85, 11.75, '-mass', 6.856810162822082, 6.856810162822082, 6.856810162822082, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 13.325, 3.85, 11.75)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(24008, 13.45, 3.85, 11.55)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 13.45, 3.725, 11.75)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 13.45, 3.975, 11.75)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14008, 4008, 14008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4009, 0.0, 7.7, 11.75, '-mass', 3.835914870328627, 3.835914870328627, 3.835914870328627, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34009, 0.125, 7.7, 11.75)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 0.0, 7.7, 11.55)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 0.0, 7.575, 11.75)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 0.0, 7.825, 11.75)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14009, 4009, 14009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4010, 2.85, 7.7, 11.75, '-mass', 10.007709742630835, 10.007709742630835, 10.007709742630835, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 2.725, 7.7, 11.75)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 2.975, 7.7, 11.75)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 2.85, 7.7, 11.55)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 2.85, 7.575, 11.75)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 2.85, 7.825, 11.75)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14010, 4010, 14010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4011, 8.15, 7.7, 11.75, '-mass', 12.934415432677806, 12.934415432677806, 12.934415432677806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 8.025, 7.7, 11.75)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 8.275, 7.7, 11.75)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 8.15, 7.7, 11.55)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 8.15, 7.575, 11.75)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 8.15, 7.825, 11.75)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14011, 4011, 14011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4012, 13.45, 7.7, 11.75, '-mass', 6.856810162822082, 6.856810162822082, 6.856810162822082, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 13.325, 7.7, 11.75)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 13.45, 7.7, 11.55)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 13.45, 7.575, 11.75)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 13.45, 7.825, 11.75)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14012, 4012, 14012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4013, 0.0, 11.55, 11.75, '-mass', 3.835914870328627, 3.835914870328627, 3.835914870328627, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.125, 11.55, 11.75)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 11.55, 11.55)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 11.425, 11.75)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 11.675, 11.75)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14013, 4013, 14013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4014, 2.85, 11.55, 11.75, '-mass', 10.007709742630833, 10.007709742630833, 10.007709742630833, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 2.725, 11.55, 11.75)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 2.975, 11.55, 11.75)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 2.85, 11.55, 11.55)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 2.85, 11.425, 11.75)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 2.85, 11.675, 11.75)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14014, 4014, 14014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4015, 8.15, 11.55, 11.75, '-mass', 12.934415432677806, 12.934415432677806, 12.934415432677806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 8.025, 11.55, 11.75)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 8.275, 11.55, 11.75)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 8.15, 11.55, 11.55)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 8.15, 11.425, 11.75)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 8.15, 11.675, 11.75)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14015, 4015, 14015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4016, 13.45, 11.55, 11.75, '-mass', 6.856810162822082, 6.856810162822082, 6.856810162822082, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 13.325, 11.55, 11.75)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(24016, 13.45, 11.55, 11.55)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 13.45, 11.425, 11.75)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 13.45, 11.675, 11.75)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14016, 4016, 14016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 4, 4)
    # Central joint node
    ops.node(4017, 0.0, 15.4, 11.75, '-mass', 3.835914870328627, 3.835914870328627, 3.835914870328627, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34017, 0.125, 15.4, 11.75)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 0.0, 15.4, 11.55)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 0.0, 15.275, 11.75)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 0.0, 15.525, 11.75)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14017, 4017, 14017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 4, 4)
    # Central joint node
    ops.node(4018, 2.85, 15.4, 11.75, '-mass', 10.007709742630833, 10.007709742630833, 10.007709742630833, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 2.725, 15.4, 11.75)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(34018, 2.975, 15.4, 11.75)
    ops.element('elasticBeamColumn', 34018, 4018, 34018, 99999, 88888)
    ops.node(24018, 2.85, 15.4, 11.55)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 2.85, 15.275, 11.75)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 2.85, 15.525, 11.75)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14018, 4018, 14018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 4, 4)
    # Central joint node
    ops.node(4019, 8.15, 15.4, 11.75, '-mass', 12.934415432677806, 12.934415432677806, 12.934415432677806, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54019, 8.025, 15.4, 11.75)
    ops.element('elasticBeamColumn', 54019, 54019, 4019, 99999, 88888)
    ops.node(34019, 8.275, 15.4, 11.75)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 8.15, 15.4, 11.55)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 8.15, 15.275, 11.75)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    ops.node(44019, 8.15, 15.525, 11.75)
    ops.element('elasticBeamColumn', 44019, 4019, 44019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14019, 4019, 14019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 4, 4)
    # Central joint node
    ops.node(4020, 13.45, 15.4, 11.75, '-mass', 6.856810162822082, 6.856810162822082, 6.856810162822082, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 13.325, 15.4, 11.75)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(24020, 13.45, 15.4, 11.55)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 13.45, 15.275, 11.75)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    ops.node(44020, 13.45, 15.525, 11.75)
    ops.element('elasticBeamColumn', 44020, 4020, 44020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14020, 4020, 14020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 5, 4)
    # Central joint node
    ops.node(4021, 0.0, 19.25, 11.75, '-mass', 2.024991074308044, 2.024991074308044, 2.024991074308044, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34021, 0.125, 19.25, 11.75)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 0.0, 19.25, 11.55)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 0.0, 19.125, 11.75)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14021, 4021, 14021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 5, 4)
    # Central joint node
    ops.node(4022, 2.85, 19.25, 11.75, '-mass', 5.110888510459147, 5.110888510459147, 5.110888510459147, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 2.725, 19.25, 11.75)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 2.975, 19.25, 11.75)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 2.85, 19.25, 11.55)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 2.85, 19.125, 11.75)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14022, 4022, 14022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 5, 4)
    # Central joint node
    ops.node(4023, 8.15, 19.25, 11.75, '-mass', 6.574241355482633, 6.574241355482633, 6.574241355482633, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 8.025, 19.25, 11.75)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 8.275, 19.25, 11.75)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 8.15, 19.25, 11.55)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 8.15, 19.125, 11.75)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14023, 4023, 14023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 5, 4)
    # Central joint node
    ops.node(4024, 13.45, 19.25, 11.75, '-mass', 3.535438720554772, 3.535438720554772, 3.535438720554772, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 13.325, 19.25, 11.75)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 13.45, 19.25, 11.55)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 13.45, 19.125, 11.75)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14024, 4024, 14024, 99999, '-orient', 0, 0, 1, 0, 1, 0)
