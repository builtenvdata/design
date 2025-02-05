import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain (nodes and rigid offsets)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (2, 0, 0.5)
    # Central joint node
    ops.node(4025, 10.6, 0.0, 1.45, '-mass', 3.4842316513761458, 3.4842316513761458, 3.4842316513761458, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34025, 10.775, 0.0, 1.45)
    ops.element('elasticBeamColumn', 34025, 4025, 34025, 99999, 88888)
    ops.node(24025, 10.6, 0.0, 1.25)
    ops.element('elasticBeamColumn', 24025, 24025, 4025, 99999, 99999)
    ops.node(74025, 10.6, 0.0, 1.65)
    ops.element('elasticBeamColumn', 74025, 4025, 74025, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 0.5)
    # Central joint node
    ops.node(4026, 13.45, 0.0, 1.45, '-mass', 3.4842316513761458, 3.4842316513761458, 3.4842316513761458, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54026, 13.275, 0.0, 1.45)
    ops.element('elasticBeamColumn', 54026, 54026, 4026, 99999, 88888)
    ops.node(24026, 13.45, 0.0, 1.25)
    ops.element('elasticBeamColumn', 24026, 24026, 4026, 99999, 99999)
    ops.node(74026, 13.45, 0.0, 1.65)
    ops.element('elasticBeamColumn', 74026, 4026, 74026, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    # Central joint node
    ops.node(4027, 10.6, 0.0, 4.35, '-mass', 3.4842316513761458, 3.4842316513761458, 3.4842316513761458, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34027, 10.775, 0.0, 4.35)
    ops.element('elasticBeamColumn', 34027, 4027, 34027, 99999, 88888)
    ops.node(24027, 10.6, 0.0, 4.15)
    ops.element('elasticBeamColumn', 24027, 24027, 4027, 99999, 99999)
    ops.node(74027, 10.6, 0.0, 4.55)
    ops.element('elasticBeamColumn', 74027, 4027, 74027, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    # Central joint node
    ops.node(4028, 13.45, 0.0, 4.35, '-mass', 3.4842316513761458, 3.4842316513761458, 3.4842316513761458, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54028, 13.275, 0.0, 4.35)
    ops.element('elasticBeamColumn', 54028, 54028, 4028, 99999, 88888)
    ops.node(24028, 13.45, 0.0, 4.15)
    ops.element('elasticBeamColumn', 24028, 24028, 4028, 99999, 99999)
    ops.node(74028, 13.45, 0.0, 4.55)
    ops.element('elasticBeamColumn', 74028, 4028, 74028, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    # Central joint node
    ops.node(4029, 10.6, 0.0, 7.25, '-mass', 3.1484518348623842, 3.1484518348623842, 3.1484518348623842, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34029, 10.725, 0.0, 7.25)
    ops.element('elasticBeamColumn', 34029, 4029, 34029, 99999, 88888)
    ops.node(24029, 10.6, 0.0, 7.05)
    ops.element('elasticBeamColumn', 24029, 24029, 4029, 99999, 99999)
    ops.node(74029, 10.6, 0.0, 7.45)
    ops.element('elasticBeamColumn', 74029, 4029, 74029, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    # Central joint node
    ops.node(4030, 13.45, 0.0, 7.25, '-mass', 3.1484518348623842, 3.1484518348623842, 3.1484518348623842, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54030, 13.325, 0.0, 7.25)
    ops.element('elasticBeamColumn', 54030, 54030, 4030, 99999, 88888)
    ops.node(24030, 13.45, 0.0, 7.05)
    ops.element('elasticBeamColumn', 24030, 24030, 4030, 99999, 99999)
    ops.node(74030, 13.45, 0.0, 7.45)
    ops.element('elasticBeamColumn', 74030, 4030, 74030, 99999, 99999)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    # Central joint node
    ops.node(4031, 10.6, 0.0, 10.15, '-mass', 3.1484518348623842, 3.1484518348623842, 3.1484518348623842, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34031, 10.725, 0.0, 10.15)
    ops.element('elasticBeamColumn', 34031, 4031, 34031, 99999, 88888)
    ops.node(24031, 10.6, 0.0, 9.95)
    ops.element('elasticBeamColumn', 24031, 24031, 4031, 99999, 99999)
    ops.node(74031, 10.6, 0.0, 10.35)
    ops.element('elasticBeamColumn', 74031, 4031, 74031, 99999, 99999)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    # Central joint node
    ops.node(4032, 13.45, 0.0, 10.15, '-mass', 3.1484518348623842, 3.1484518348623842, 3.1484518348623842, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54032, 13.325, 0.0, 10.15)
    ops.element('elasticBeamColumn', 54032, 54032, 4032, 99999, 88888)
    ops.node(24032, 13.45, 0.0, 9.95)
    ops.element('elasticBeamColumn', 24032, 24032, 4032, 99999, 99999)
    ops.node(74032, 13.45, 0.0, 10.35)
    ops.element('elasticBeamColumn', 74032, 4032, 74032, 99999, 99999)

    # -------------------------------------------------
    # Add floor joints to ops domain (nodes, joint offsets and flexibility)
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    # Central joint node
    ops.node(1001, 0.0, 0.0, 2.9, '-mass', 8.938781963540471, 8.938781963540471, 8.938781963540471, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31001, 0.125, 0.0, 2.9)
    ops.element('elasticBeamColumn', 31001, 1001, 31001, 99999, 88888)
    ops.node(21001, 0.0, 0.0, 2.625)
    ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)
    ops.node(71001, 0.0, 0.0, 3.175)
    ops.element('elasticBeamColumn', 71001, 1001, 71001, 99999, 99999)
    ops.node(41001, 0.0, 0.175, 2.9)
    ops.element('elasticBeamColumn', 41001, 1001, 41001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11001, 1001, 11001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    # Central joint node
    ops.node(1002, 5.3, 0.0, 2.9, '-mass', 13.98133558865077, 13.98133558865077, 13.98133558865077, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51002, 5.125, 0.0, 2.9)
    ops.element('elasticBeamColumn', 51002, 51002, 1002, 99999, 88888)
    ops.node(31002, 5.475, 0.0, 2.9)
    ops.element('elasticBeamColumn', 31002, 1002, 31002, 99999, 88888)
    ops.node(21002, 5.3, 0.0, 2.625)
    ops.element('elasticBeamColumn', 21002, 21002, 1002, 99999, 99999)
    ops.node(71002, 5.3, 0.0, 3.175)
    ops.element('elasticBeamColumn', 71002, 1002, 71002, 99999, 99999)
    ops.node(41002, 5.3, 0.275, 2.9)
    ops.element('elasticBeamColumn', 41002, 1002, 41002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11002, 1002, 11002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    # Central joint node
    ops.node(1003, 10.6, 0.0, 2.9, '-mass', 9.514011321338637, 9.514011321338637, 9.514011321338637, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51003, 10.425, 0.0, 2.9)
    ops.element('elasticBeamColumn', 51003, 51003, 1003, 99999, 88888)
    ops.node(31003, 10.775, 0.0, 2.9)
    ops.element('elasticBeamColumn', 31003, 1003, 31003, 99999, 88888)
    ops.node(21003, 10.6, 0.0, 2.625)
    ops.element('elasticBeamColumn', 21003, 21003, 1003, 99999, 99999)
    ops.node(71003, 10.6, 0.0, 3.175)
    ops.element('elasticBeamColumn', 71003, 1003, 71003, 99999, 99999)
    ops.node(41003, 10.6, 0.25, 2.9)
    ops.element('elasticBeamColumn', 41003, 1003, 41003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11003, 1003, 11003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    # Central joint node
    ops.node(1004, 13.45, 0.0, 2.9, '-mass', 9.51401132133864, 9.51401132133864, 9.51401132133864, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51004, 13.275, 0.0, 2.9)
    ops.element('elasticBeamColumn', 51004, 51004, 1004, 99999, 88888)
    ops.node(31004, 13.625, 0.0, 2.9)
    ops.element('elasticBeamColumn', 31004, 1004, 31004, 99999, 88888)
    ops.node(21004, 13.45, 0.0, 2.625)
    ops.element('elasticBeamColumn', 21004, 21004, 1004, 99999, 99999)
    ops.node(71004, 13.45, 0.0, 3.175)
    ops.element('elasticBeamColumn', 71004, 1004, 71004, 99999, 99999)
    ops.node(41004, 13.45, 0.25, 2.9)
    ops.element('elasticBeamColumn', 41004, 1004, 41004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11004, 1004, 11004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    # Central joint node
    ops.node(1005, 18.75, 0.0, 2.9, '-mass', 13.981335588650772, 13.981335588650772, 13.981335588650772, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51005, 18.575, 0.0, 2.9)
    ops.element('elasticBeamColumn', 51005, 51005, 1005, 99999, 88888)
    ops.node(31005, 18.925, 0.0, 2.9)
    ops.element('elasticBeamColumn', 31005, 1005, 31005, 99999, 88888)
    ops.node(21005, 18.75, 0.0, 2.625)
    ops.element('elasticBeamColumn', 21005, 21005, 1005, 99999, 99999)
    ops.node(71005, 18.75, 0.0, 3.175)
    ops.element('elasticBeamColumn', 71005, 1005, 71005, 99999, 99999)
    ops.node(41005, 18.75, 0.275, 2.9)
    ops.element('elasticBeamColumn', 41005, 1005, 41005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11005, 1005, 11005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    # Central joint node
    ops.node(1006, 24.05, 0.0, 2.9, '-mass', 8.938781963540475, 8.938781963540475, 8.938781963540475, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51006, 23.925, 0.0, 2.9)
    ops.element('elasticBeamColumn', 51006, 51006, 1006, 99999, 88888)
    ops.node(21006, 24.05, 0.0, 2.625)
    ops.element('elasticBeamColumn', 21006, 21006, 1006, 99999, 99999)
    ops.node(71006, 24.05, 0.0, 3.175)
    ops.element('elasticBeamColumn', 71006, 1006, 71006, 99999, 99999)
    ops.node(41006, 24.05, 0.175, 2.9)
    ops.element('elasticBeamColumn', 41006, 1006, 41006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11006, 1006, 11006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    # Central joint node
    ops.node(1007, 0.0, 4.25, 2.9, '-mass', 13.896320298130892, 13.896320298130892, 13.896320298130892, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31007, 0.275, 4.25, 2.9)
    ops.element('elasticBeamColumn', 31007, 1007, 31007, 99999, 88888)
    ops.node(21007, 0.0, 4.25, 2.65)
    ops.element('elasticBeamColumn', 21007, 21007, 1007, 99999, 99999)
    ops.node(71007, 0.0, 4.25, 3.15)
    ops.element('elasticBeamColumn', 71007, 1007, 71007, 99999, 99999)
    ops.node(61007, 0.0, 4.05, 2.9)
    ops.element('elasticBeamColumn', 61007, 61007, 1007, 99999, 77777)
    ops.node(41007, 0.0, 4.45, 2.9)
    ops.element('elasticBeamColumn', 41007, 1007, 41007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11007, 1007, 11007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    # Central joint node
    ops.node(1008, 5.3, 4.25, 2.9, '-mass', 18.865015723682784, 18.865015723682784, 18.865015723682784, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51008, 4.95, 4.25, 2.9)
    ops.element('elasticBeamColumn', 51008, 51008, 1008, 99999, 88888)
    ops.node(31008, 5.65, 4.25, 2.9)
    ops.element('elasticBeamColumn', 31008, 1008, 31008, 99999, 88888)
    ops.node(21008, 5.3, 4.25, 2.65)
    ops.element('elasticBeamColumn', 21008, 21008, 1008, 99999, 99999)
    ops.node(71008, 5.3, 4.25, 3.15)
    ops.element('elasticBeamColumn', 71008, 1008, 71008, 99999, 99999)
    ops.node(61008, 5.3, 4.025, 2.9)
    ops.element('elasticBeamColumn', 61008, 61008, 1008, 99999, 77777)
    ops.node(41008, 5.3, 4.475, 2.9)
    ops.element('elasticBeamColumn', 41008, 1008, 41008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11008, 1008, 11008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    # Central joint node
    ops.node(1009, 10.6, 4.25, 2.9, '-mass', 16.96434490171822, 16.96434490171822, 16.96434490171822, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51009, 10.3, 4.25, 2.9)
    ops.element('elasticBeamColumn', 51009, 51009, 1009, 99999, 88888)
    ops.node(31009, 10.9, 4.25, 2.9)
    ops.element('elasticBeamColumn', 31009, 1009, 31009, 99999, 88888)
    ops.node(21009, 10.6, 4.25, 2.65)
    ops.element('elasticBeamColumn', 21009, 21009, 1009, 99999, 99999)
    ops.node(71009, 10.6, 4.25, 3.15)
    ops.element('elasticBeamColumn', 71009, 1009, 71009, 99999, 99999)
    ops.node(61009, 10.6, 4.05, 2.9)
    ops.element('elasticBeamColumn', 61009, 61009, 1009, 99999, 77777)
    ops.node(41009, 10.6, 4.45, 2.9)
    ops.element('elasticBeamColumn', 41009, 1009, 41009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11009, 1009, 11009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    # Central joint node
    ops.node(1010, 13.45, 4.25, 2.9, '-mass', 16.964344901718224, 16.964344901718224, 16.964344901718224, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51010, 13.15, 4.25, 2.9)
    ops.element('elasticBeamColumn', 51010, 51010, 1010, 99999, 88888)
    ops.node(31010, 13.75, 4.25, 2.9)
    ops.element('elasticBeamColumn', 31010, 1010, 31010, 99999, 88888)
    ops.node(21010, 13.45, 4.25, 2.65)
    ops.element('elasticBeamColumn', 21010, 21010, 1010, 99999, 99999)
    ops.node(71010, 13.45, 4.25, 3.15)
    ops.element('elasticBeamColumn', 71010, 1010, 71010, 99999, 99999)
    ops.node(61010, 13.45, 4.05, 2.9)
    ops.element('elasticBeamColumn', 61010, 61010, 1010, 99999, 77777)
    ops.node(41010, 13.45, 4.45, 2.9)
    ops.element('elasticBeamColumn', 41010, 1010, 41010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11010, 1010, 11010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    # Central joint node
    ops.node(1011, 18.75, 4.25, 2.9, '-mass', 18.865015723682788, 18.865015723682788, 18.865015723682788, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51011, 18.4, 4.25, 2.9)
    ops.element('elasticBeamColumn', 51011, 51011, 1011, 99999, 88888)
    ops.node(31011, 19.1, 4.25, 2.9)
    ops.element('elasticBeamColumn', 31011, 1011, 31011, 99999, 88888)
    ops.node(21011, 18.75, 4.25, 2.65)
    ops.element('elasticBeamColumn', 21011, 21011, 1011, 99999, 99999)
    ops.node(71011, 18.75, 4.25, 3.15)
    ops.element('elasticBeamColumn', 71011, 1011, 71011, 99999, 99999)
    ops.node(61011, 18.75, 4.025, 2.9)
    ops.element('elasticBeamColumn', 61011, 61011, 1011, 99999, 77777)
    ops.node(41011, 18.75, 4.475, 2.9)
    ops.element('elasticBeamColumn', 41011, 1011, 41011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11011, 1011, 11011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    # Central joint node
    ops.node(1012, 24.05, 4.25, 2.9, '-mass', 13.896320298130892, 13.896320298130892, 13.896320298130892, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51012, 23.775, 4.25, 2.9)
    ops.element('elasticBeamColumn', 51012, 51012, 1012, 99999, 88888)
    ops.node(21012, 24.05, 4.25, 2.65)
    ops.element('elasticBeamColumn', 21012, 21012, 1012, 99999, 99999)
    ops.node(71012, 24.05, 4.25, 3.15)
    ops.element('elasticBeamColumn', 71012, 1012, 71012, 99999, 99999)
    ops.node(61012, 24.05, 4.05, 2.9)
    ops.element('elasticBeamColumn', 61012, 61012, 1012, 99999, 77777)
    ops.node(41012, 24.05, 4.45, 2.9)
    ops.element('elasticBeamColumn', 41012, 1012, 41012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11012, 1012, 11012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    # Central joint node
    ops.node(1013, 0.0, 8.5, 2.9, '-mass', 13.896320298130892, 13.896320298130892, 13.896320298130892, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31013, 0.275, 8.5, 2.9)
    ops.element('elasticBeamColumn', 31013, 1013, 31013, 99999, 88888)
    ops.node(21013, 0.0, 8.5, 2.65)
    ops.element('elasticBeamColumn', 21013, 21013, 1013, 99999, 99999)
    ops.node(71013, 0.0, 8.5, 3.15)
    ops.element('elasticBeamColumn', 71013, 1013, 71013, 99999, 99999)
    ops.node(61013, 0.0, 8.3, 2.9)
    ops.element('elasticBeamColumn', 61013, 61013, 1013, 99999, 77777)
    ops.node(41013, 0.0, 8.7, 2.9)
    ops.element('elasticBeamColumn', 41013, 1013, 41013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11013, 1013, 11013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    # Central joint node
    ops.node(1014, 5.3, 8.5, 2.9, '-mass', 18.865015723682784, 18.865015723682784, 18.865015723682784, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51014, 4.95, 8.5, 2.9)
    ops.element('elasticBeamColumn', 51014, 51014, 1014, 99999, 88888)
    ops.node(31014, 5.65, 8.5, 2.9)
    ops.element('elasticBeamColumn', 31014, 1014, 31014, 99999, 88888)
    ops.node(21014, 5.3, 8.5, 2.65)
    ops.element('elasticBeamColumn', 21014, 21014, 1014, 99999, 99999)
    ops.node(71014, 5.3, 8.5, 3.15)
    ops.element('elasticBeamColumn', 71014, 1014, 71014, 99999, 99999)
    ops.node(61014, 5.3, 8.275, 2.9)
    ops.element('elasticBeamColumn', 61014, 61014, 1014, 99999, 77777)
    ops.node(41014, 5.3, 8.725, 2.9)
    ops.element('elasticBeamColumn', 41014, 1014, 41014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11014, 1014, 11014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    # Central joint node
    ops.node(1015, 10.6, 8.5, 2.9, '-mass', 14.544945957904945, 14.544945957904945, 14.544945957904945, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51015, 10.35, 8.5, 2.9)
    ops.element('elasticBeamColumn', 51015, 51015, 1015, 99999, 88888)
    ops.node(31015, 10.85, 8.5, 2.9)
    ops.element('elasticBeamColumn', 31015, 1015, 31015, 99999, 88888)
    ops.node(21015, 10.6, 8.5, 2.65)
    ops.element('elasticBeamColumn', 21015, 21015, 1015, 99999, 99999)
    ops.node(71015, 10.6, 8.5, 3.15)
    ops.element('elasticBeamColumn', 71015, 1015, 71015, 99999, 99999)
    ops.node(61015, 10.6, 8.325, 2.9)
    ops.element('elasticBeamColumn', 61015, 61015, 1015, 99999, 77777)
    ops.node(41015, 10.6, 8.675, 2.9)
    ops.element('elasticBeamColumn', 41015, 1015, 41015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11015, 1015, 11015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    # Central joint node
    ops.node(1016, 13.45, 8.5, 2.9, '-mass', 14.544945957904947, 14.544945957904947, 14.544945957904947, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51016, 13.2, 8.5, 2.9)
    ops.element('elasticBeamColumn', 51016, 51016, 1016, 99999, 88888)
    ops.node(31016, 13.7, 8.5, 2.9)
    ops.element('elasticBeamColumn', 31016, 1016, 31016, 99999, 88888)
    ops.node(21016, 13.45, 8.5, 2.65)
    ops.element('elasticBeamColumn', 21016, 21016, 1016, 99999, 99999)
    ops.node(71016, 13.45, 8.5, 3.15)
    ops.element('elasticBeamColumn', 71016, 1016, 71016, 99999, 99999)
    ops.node(61016, 13.45, 8.325, 2.9)
    ops.element('elasticBeamColumn', 61016, 61016, 1016, 99999, 77777)
    ops.node(41016, 13.45, 8.675, 2.9)
    ops.element('elasticBeamColumn', 41016, 1016, 41016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11016, 1016, 11016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    # Central joint node
    ops.node(1017, 18.75, 8.5, 2.9, '-mass', 18.865015723682788, 18.865015723682788, 18.865015723682788, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51017, 18.4, 8.5, 2.9)
    ops.element('elasticBeamColumn', 51017, 51017, 1017, 99999, 88888)
    ops.node(31017, 19.1, 8.5, 2.9)
    ops.element('elasticBeamColumn', 31017, 1017, 31017, 99999, 88888)
    ops.node(21017, 18.75, 8.5, 2.65)
    ops.element('elasticBeamColumn', 21017, 21017, 1017, 99999, 99999)
    ops.node(71017, 18.75, 8.5, 3.15)
    ops.element('elasticBeamColumn', 71017, 1017, 71017, 99999, 99999)
    ops.node(61017, 18.75, 8.275, 2.9)
    ops.element('elasticBeamColumn', 61017, 61017, 1017, 99999, 77777)
    ops.node(41017, 18.75, 8.725, 2.9)
    ops.element('elasticBeamColumn', 41017, 1017, 41017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11017, 1017, 11017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    # Central joint node
    ops.node(1018, 24.05, 8.5, 2.9, '-mass', 13.896320298130892, 13.896320298130892, 13.896320298130892, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51018, 23.775, 8.5, 2.9)
    ops.element('elasticBeamColumn', 51018, 51018, 1018, 99999, 88888)
    ops.node(21018, 24.05, 8.5, 2.65)
    ops.element('elasticBeamColumn', 21018, 21018, 1018, 99999, 99999)
    ops.node(71018, 24.05, 8.5, 3.15)
    ops.element('elasticBeamColumn', 71018, 1018, 71018, 99999, 99999)
    ops.node(61018, 24.05, 8.3, 2.9)
    ops.element('elasticBeamColumn', 61018, 61018, 1018, 99999, 77777)
    ops.node(41018, 24.05, 8.7, 2.9)
    ops.element('elasticBeamColumn', 41018, 1018, 41018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11018, 1018, 11018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    # Central joint node
    ops.node(1019, 0.0, 12.75, 2.9, '-mass', 8.938781963540471, 8.938781963540471, 8.938781963540471, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(31019, 0.125, 12.75, 2.9)
    ops.element('elasticBeamColumn', 31019, 1019, 31019, 99999, 88888)
    ops.node(21019, 0.0, 12.75, 2.625)
    ops.element('elasticBeamColumn', 21019, 21019, 1019, 99999, 99999)
    ops.node(71019, 0.0, 12.75, 3.175)
    ops.element('elasticBeamColumn', 71019, 1019, 71019, 99999, 99999)
    ops.node(61019, 0.0, 12.575, 2.9)
    ops.element('elasticBeamColumn', 61019, 61019, 1019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11019, 1019, 11019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    # Central joint node
    ops.node(1020, 5.3, 12.75, 2.9, '-mass', 13.98133558865077, 13.98133558865077, 13.98133558865077, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51020, 5.125, 12.75, 2.9)
    ops.element('elasticBeamColumn', 51020, 51020, 1020, 99999, 88888)
    ops.node(31020, 5.475, 12.75, 2.9)
    ops.element('elasticBeamColumn', 31020, 1020, 31020, 99999, 88888)
    ops.node(21020, 5.3, 12.75, 2.625)
    ops.element('elasticBeamColumn', 21020, 21020, 1020, 99999, 99999)
    ops.node(71020, 5.3, 12.75, 3.175)
    ops.element('elasticBeamColumn', 71020, 1020, 71020, 99999, 99999)
    ops.node(61020, 5.3, 12.475, 2.9)
    ops.element('elasticBeamColumn', 61020, 61020, 1020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11020, 1020, 11020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    # Central joint node
    ops.node(1021, 10.6, 12.75, 2.9, '-mass', 10.915999992204256, 10.915999992204256, 10.915999992204256, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51021, 10.45, 12.75, 2.9)
    ops.element('elasticBeamColumn', 51021, 51021, 1021, 99999, 88888)
    ops.node(31021, 10.75, 12.75, 2.9)
    ops.element('elasticBeamColumn', 31021, 1021, 31021, 99999, 88888)
    ops.node(21021, 10.6, 12.75, 2.625)
    ops.element('elasticBeamColumn', 21021, 21021, 1021, 99999, 99999)
    ops.node(71021, 10.6, 12.75, 3.175)
    ops.element('elasticBeamColumn', 71021, 1021, 71021, 99999, 99999)
    ops.node(61021, 10.6, 12.525, 2.9)
    ops.element('elasticBeamColumn', 61021, 61021, 1021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11021, 1021, 11021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    # Central joint node
    ops.node(1022, 13.45, 12.75, 2.9, '-mass', 10.915999992204258, 10.915999992204258, 10.915999992204258, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51022, 13.3, 12.75, 2.9)
    ops.element('elasticBeamColumn', 51022, 51022, 1022, 99999, 88888)
    ops.node(31022, 13.6, 12.75, 2.9)
    ops.element('elasticBeamColumn', 31022, 1022, 31022, 99999, 88888)
    ops.node(21022, 13.45, 12.75, 2.625)
    ops.element('elasticBeamColumn', 21022, 21022, 1022, 99999, 99999)
    ops.node(71022, 13.45, 12.75, 3.175)
    ops.element('elasticBeamColumn', 71022, 1022, 71022, 99999, 99999)
    ops.node(61022, 13.45, 12.525, 2.9)
    ops.element('elasticBeamColumn', 61022, 61022, 1022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11022, 1022, 11022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 1)
    # Central joint node
    ops.node(1023, 18.75, 12.75, 2.9, '-mass', 13.981335588650772, 13.981335588650772, 13.981335588650772, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51023, 18.575, 12.75, 2.9)
    ops.element('elasticBeamColumn', 51023, 51023, 1023, 99999, 88888)
    ops.node(31023, 18.925, 12.75, 2.9)
    ops.element('elasticBeamColumn', 31023, 1023, 31023, 99999, 88888)
    ops.node(21023, 18.75, 12.75, 2.625)
    ops.element('elasticBeamColumn', 21023, 21023, 1023, 99999, 99999)
    ops.node(71023, 18.75, 12.75, 3.175)
    ops.element('elasticBeamColumn', 71023, 1023, 71023, 99999, 99999)
    ops.node(61023, 18.75, 12.475, 2.9)
    ops.element('elasticBeamColumn', 61023, 61023, 1023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11023, 1023, 11023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 1)
    # Central joint node
    ops.node(1024, 24.05, 12.75, 2.9, '-mass', 8.938781963540475, 8.938781963540475, 8.938781963540475, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(51024, 23.925, 12.75, 2.9)
    ops.element('elasticBeamColumn', 51024, 51024, 1024, 99999, 88888)
    ops.node(21024, 24.05, 12.75, 2.625)
    ops.element('elasticBeamColumn', 21024, 21024, 1024, 99999, 99999)
    ops.node(71024, 24.05, 12.75, 3.175)
    ops.element('elasticBeamColumn', 71024, 1024, 71024, 99999, 99999)
    ops.node(61024, 24.05, 12.575, 2.9)
    ops.element('elasticBeamColumn', 61024, 61024, 1024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 11024, 1024, 11024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    # Central joint node
    ops.node(2001, 0.0, 0.0, 5.8, '-mass', 8.980066367210195, 8.980066367210195, 8.980066367210195, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32001, 0.125, 0.0, 5.8)
    ops.element('elasticBeamColumn', 32001, 2001, 32001, 99999, 88888)
    ops.node(22001, 0.0, 0.0, 5.525)
    ops.element('elasticBeamColumn', 22001, 22001, 2001, 99999, 99999)
    ops.node(72001, 0.0, 0.0, 6.075)
    ops.element('elasticBeamColumn', 72001, 2001, 72001, 99999, 99999)
    ops.node(42001, 0.0, 0.175, 5.8)
    ops.element('elasticBeamColumn', 42001, 2001, 42001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12001, 2001, 12001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    # Central joint node
    ops.node(2002, 5.3, 0.0, 5.8, '-mass', 13.741886047366366, 13.741886047366366, 13.741886047366366, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52002, 5.125, 0.0, 5.8)
    ops.element('elasticBeamColumn', 52002, 52002, 2002, 99999, 88888)
    ops.node(32002, 5.475, 0.0, 5.8)
    ops.element('elasticBeamColumn', 32002, 2002, 32002, 99999, 88888)
    ops.node(22002, 5.3, 0.0, 5.525)
    ops.element('elasticBeamColumn', 22002, 22002, 2002, 99999, 99999)
    ops.node(72002, 5.3, 0.0, 6.075)
    ops.element('elasticBeamColumn', 72002, 2002, 72002, 99999, 99999)
    ops.node(42002, 5.3, 0.275, 5.8)
    ops.element('elasticBeamColumn', 42002, 2002, 42002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12002, 2002, 12002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    # Central joint node
    ops.node(2003, 10.6, 0.0, 5.8, '-mass', 9.380983798402857, 9.380983798402857, 9.380983798402857, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52003, 10.425, 0.0, 5.8)
    ops.element('elasticBeamColumn', 52003, 52003, 2003, 99999, 88888)
    ops.node(32003, 10.775, 0.0, 5.8)
    ops.element('elasticBeamColumn', 32003, 2003, 32003, 99999, 88888)
    ops.node(22003, 10.6, 0.0, 5.525)
    ops.element('elasticBeamColumn', 22003, 22003, 2003, 99999, 99999)
    ops.node(72003, 10.6, 0.0, 6.075)
    ops.element('elasticBeamColumn', 72003, 2003, 72003, 99999, 99999)
    ops.node(42003, 10.6, 0.25, 5.8)
    ops.element('elasticBeamColumn', 42003, 2003, 42003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12003, 2003, 12003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    # Central joint node
    ops.node(2004, 13.45, 0.0, 5.8, '-mass', 9.380983798402859, 9.380983798402859, 9.380983798402859, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52004, 13.275, 0.0, 5.8)
    ops.element('elasticBeamColumn', 52004, 52004, 2004, 99999, 88888)
    ops.node(32004, 13.625, 0.0, 5.8)
    ops.element('elasticBeamColumn', 32004, 2004, 32004, 99999, 88888)
    ops.node(22004, 13.45, 0.0, 5.525)
    ops.element('elasticBeamColumn', 22004, 22004, 2004, 99999, 99999)
    ops.node(72004, 13.45, 0.0, 6.075)
    ops.element('elasticBeamColumn', 72004, 2004, 72004, 99999, 99999)
    ops.node(42004, 13.45, 0.25, 5.8)
    ops.element('elasticBeamColumn', 42004, 2004, 42004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12004, 2004, 12004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    # Central joint node
    ops.node(2005, 18.75, 0.0, 5.8, '-mass', 13.74188604736637, 13.74188604736637, 13.74188604736637, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52005, 18.575, 0.0, 5.8)
    ops.element('elasticBeamColumn', 52005, 52005, 2005, 99999, 88888)
    ops.node(32005, 18.925, 0.0, 5.8)
    ops.element('elasticBeamColumn', 32005, 2005, 32005, 99999, 88888)
    ops.node(22005, 18.75, 0.0, 5.525)
    ops.element('elasticBeamColumn', 22005, 22005, 2005, 99999, 99999)
    ops.node(72005, 18.75, 0.0, 6.075)
    ops.element('elasticBeamColumn', 72005, 2005, 72005, 99999, 99999)
    ops.node(42005, 18.75, 0.275, 5.8)
    ops.element('elasticBeamColumn', 42005, 2005, 42005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12005, 2005, 12005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    # Central joint node
    ops.node(2006, 24.05, 0.0, 5.8, '-mass', 8.980066367210199, 8.980066367210199, 8.980066367210199, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52006, 23.925, 0.0, 5.8)
    ops.element('elasticBeamColumn', 52006, 52006, 2006, 99999, 88888)
    ops.node(22006, 24.05, 0.0, 5.525)
    ops.element('elasticBeamColumn', 22006, 22006, 2006, 99999, 99999)
    ops.node(72006, 24.05, 0.0, 6.075)
    ops.element('elasticBeamColumn', 72006, 2006, 72006, 99999, 99999)
    ops.node(42006, 24.05, 0.175, 5.8)
    ops.element('elasticBeamColumn', 42006, 2006, 42006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12006, 2006, 12006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    # Central joint node
    ops.node(2007, 0.0, 4.25, 5.8, '-mass', 13.996626108528446, 13.996626108528446, 13.996626108528446, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32007, 0.275, 4.25, 5.8)
    ops.element('elasticBeamColumn', 32007, 2007, 32007, 99999, 88888)
    ops.node(22007, 0.0, 4.25, 5.55)
    ops.element('elasticBeamColumn', 22007, 22007, 2007, 99999, 99999)
    ops.node(72007, 0.0, 4.25, 6.05)
    ops.element('elasticBeamColumn', 72007, 2007, 72007, 99999, 99999)
    ops.node(62007, 0.0, 4.05, 5.8)
    ops.element('elasticBeamColumn', 62007, 62007, 2007, 99999, 77777)
    ops.node(42007, 0.0, 4.45, 5.8)
    ops.element('elasticBeamColumn', 42007, 2007, 42007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12007, 2007, 12007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    # Central joint node
    ops.node(2008, 5.3, 4.25, 5.8, '-mass', 18.4925386594626, 18.4925386594626, 18.4925386594626, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52008, 4.95, 4.25, 5.8)
    ops.element('elasticBeamColumn', 52008, 52008, 2008, 99999, 88888)
    ops.node(32008, 5.65, 4.25, 5.8)
    ops.element('elasticBeamColumn', 32008, 2008, 32008, 99999, 88888)
    ops.node(22008, 5.3, 4.25, 5.55)
    ops.element('elasticBeamColumn', 22008, 22008, 2008, 99999, 99999)
    ops.node(72008, 5.3, 4.25, 6.05)
    ops.element('elasticBeamColumn', 72008, 2008, 72008, 99999, 99999)
    ops.node(62008, 5.3, 4.025, 5.8)
    ops.element('elasticBeamColumn', 62008, 62008, 2008, 99999, 77777)
    ops.node(42008, 5.3, 4.475, 5.8)
    ops.element('elasticBeamColumn', 42008, 2008, 42008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12008, 2008, 12008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    # Central joint node
    ops.node(2009, 10.6, 4.25, 5.8, '-mass', 16.73376386196287, 16.73376386196287, 16.73376386196287, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52009, 10.3, 4.25, 5.8)
    ops.element('elasticBeamColumn', 52009, 52009, 2009, 99999, 88888)
    ops.node(32009, 10.9, 4.25, 5.8)
    ops.element('elasticBeamColumn', 32009, 2009, 32009, 99999, 88888)
    ops.node(22009, 10.6, 4.25, 5.55)
    ops.element('elasticBeamColumn', 22009, 22009, 2009, 99999, 99999)
    ops.node(72009, 10.6, 4.25, 6.05)
    ops.element('elasticBeamColumn', 72009, 2009, 72009, 99999, 99999)
    ops.node(62009, 10.6, 4.05, 5.8)
    ops.element('elasticBeamColumn', 62009, 62009, 2009, 99999, 77777)
    ops.node(42009, 10.6, 4.45, 5.8)
    ops.element('elasticBeamColumn', 42009, 2009, 42009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12009, 2009, 12009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    # Central joint node
    ops.node(2010, 13.45, 4.25, 5.8, '-mass', 16.73376386196287, 16.73376386196287, 16.73376386196287, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52010, 13.15, 4.25, 5.8)
    ops.element('elasticBeamColumn', 52010, 52010, 2010, 99999, 88888)
    ops.node(32010, 13.75, 4.25, 5.8)
    ops.element('elasticBeamColumn', 32010, 2010, 32010, 99999, 88888)
    ops.node(22010, 13.45, 4.25, 5.55)
    ops.element('elasticBeamColumn', 22010, 22010, 2010, 99999, 99999)
    ops.node(72010, 13.45, 4.25, 6.05)
    ops.element('elasticBeamColumn', 72010, 2010, 72010, 99999, 99999)
    ops.node(62010, 13.45, 4.05, 5.8)
    ops.element('elasticBeamColumn', 62010, 62010, 2010, 99999, 77777)
    ops.node(42010, 13.45, 4.45, 5.8)
    ops.element('elasticBeamColumn', 42010, 2010, 42010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12010, 2010, 12010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    # Central joint node
    ops.node(2011, 18.75, 4.25, 5.8, '-mass', 18.492538659462603, 18.492538659462603, 18.492538659462603, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52011, 18.4, 4.25, 5.8)
    ops.element('elasticBeamColumn', 52011, 52011, 2011, 99999, 88888)
    ops.node(32011, 19.1, 4.25, 5.8)
    ops.element('elasticBeamColumn', 32011, 2011, 32011, 99999, 88888)
    ops.node(22011, 18.75, 4.25, 5.55)
    ops.element('elasticBeamColumn', 22011, 22011, 2011, 99999, 99999)
    ops.node(72011, 18.75, 4.25, 6.05)
    ops.element('elasticBeamColumn', 72011, 2011, 72011, 99999, 99999)
    ops.node(62011, 18.75, 4.025, 5.8)
    ops.element('elasticBeamColumn', 62011, 62011, 2011, 99999, 77777)
    ops.node(42011, 18.75, 4.475, 5.8)
    ops.element('elasticBeamColumn', 42011, 2011, 42011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12011, 2011, 12011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    # Central joint node
    ops.node(2012, 24.05, 4.25, 5.8, '-mass', 13.996626108528446, 13.996626108528446, 13.996626108528446, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52012, 23.775, 4.25, 5.8)
    ops.element('elasticBeamColumn', 52012, 52012, 2012, 99999, 88888)
    ops.node(22012, 24.05, 4.25, 5.55)
    ops.element('elasticBeamColumn', 22012, 22012, 2012, 99999, 99999)
    ops.node(72012, 24.05, 4.25, 6.05)
    ops.element('elasticBeamColumn', 72012, 2012, 72012, 99999, 99999)
    ops.node(62012, 24.05, 4.05, 5.8)
    ops.element('elasticBeamColumn', 62012, 62012, 2012, 99999, 77777)
    ops.node(42012, 24.05, 4.45, 5.8)
    ops.element('elasticBeamColumn', 42012, 2012, 42012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12012, 2012, 12012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    # Central joint node
    ops.node(2013, 0.0, 8.5, 5.8, '-mass', 13.996626108528446, 13.996626108528446, 13.996626108528446, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32013, 0.275, 8.5, 5.8)
    ops.element('elasticBeamColumn', 32013, 2013, 32013, 99999, 88888)
    ops.node(22013, 0.0, 8.5, 5.55)
    ops.element('elasticBeamColumn', 22013, 22013, 2013, 99999, 99999)
    ops.node(72013, 0.0, 8.5, 6.05)
    ops.element('elasticBeamColumn', 72013, 2013, 72013, 99999, 99999)
    ops.node(62013, 0.0, 8.3, 5.8)
    ops.element('elasticBeamColumn', 62013, 62013, 2013, 99999, 77777)
    ops.node(42013, 0.0, 8.7, 5.8)
    ops.element('elasticBeamColumn', 42013, 2013, 42013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12013, 2013, 12013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    # Central joint node
    ops.node(2014, 5.3, 8.5, 5.8, '-mass', 18.4925386594626, 18.4925386594626, 18.4925386594626, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52014, 4.95, 8.5, 5.8)
    ops.element('elasticBeamColumn', 52014, 52014, 2014, 99999, 88888)
    ops.node(32014, 5.65, 8.5, 5.8)
    ops.element('elasticBeamColumn', 32014, 2014, 32014, 99999, 88888)
    ops.node(22014, 5.3, 8.5, 5.55)
    ops.element('elasticBeamColumn', 22014, 22014, 2014, 99999, 99999)
    ops.node(72014, 5.3, 8.5, 6.05)
    ops.element('elasticBeamColumn', 72014, 2014, 72014, 99999, 99999)
    ops.node(62014, 5.3, 8.275, 5.8)
    ops.element('elasticBeamColumn', 62014, 62014, 2014, 99999, 77777)
    ops.node(42014, 5.3, 8.725, 5.8)
    ops.element('elasticBeamColumn', 42014, 2014, 42014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12014, 2014, 12014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    # Central joint node
    ops.node(2015, 10.6, 8.5, 5.8, '-mass', 14.278890912033384, 14.278890912033384, 14.278890912033384, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52015, 10.35, 8.5, 5.8)
    ops.element('elasticBeamColumn', 52015, 52015, 2015, 99999, 88888)
    ops.node(32015, 10.85, 8.5, 5.8)
    ops.element('elasticBeamColumn', 32015, 2015, 32015, 99999, 88888)
    ops.node(22015, 10.6, 8.5, 5.55)
    ops.element('elasticBeamColumn', 22015, 22015, 2015, 99999, 99999)
    ops.node(72015, 10.6, 8.5, 6.05)
    ops.element('elasticBeamColumn', 72015, 2015, 72015, 99999, 99999)
    ops.node(62015, 10.6, 8.325, 5.8)
    ops.element('elasticBeamColumn', 62015, 62015, 2015, 99999, 77777)
    ops.node(42015, 10.6, 8.675, 5.8)
    ops.element('elasticBeamColumn', 42015, 2015, 42015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12015, 2015, 12015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    # Central joint node
    ops.node(2016, 13.45, 8.5, 5.8, '-mass', 14.278890912033386, 14.278890912033386, 14.278890912033386, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52016, 13.2, 8.5, 5.8)
    ops.element('elasticBeamColumn', 52016, 52016, 2016, 99999, 88888)
    ops.node(32016, 13.7, 8.5, 5.8)
    ops.element('elasticBeamColumn', 32016, 2016, 32016, 99999, 88888)
    ops.node(22016, 13.45, 8.5, 5.55)
    ops.element('elasticBeamColumn', 22016, 22016, 2016, 99999, 99999)
    ops.node(72016, 13.45, 8.5, 6.05)
    ops.element('elasticBeamColumn', 72016, 2016, 72016, 99999, 99999)
    ops.node(62016, 13.45, 8.325, 5.8)
    ops.element('elasticBeamColumn', 62016, 62016, 2016, 99999, 77777)
    ops.node(42016, 13.45, 8.675, 5.8)
    ops.element('elasticBeamColumn', 42016, 2016, 42016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12016, 2016, 12016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    # Central joint node
    ops.node(2017, 18.75, 8.5, 5.8, '-mass', 18.492538659462603, 18.492538659462603, 18.492538659462603, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52017, 18.4, 8.5, 5.8)
    ops.element('elasticBeamColumn', 52017, 52017, 2017, 99999, 88888)
    ops.node(32017, 19.1, 8.5, 5.8)
    ops.element('elasticBeamColumn', 32017, 2017, 32017, 99999, 88888)
    ops.node(22017, 18.75, 8.5, 5.55)
    ops.element('elasticBeamColumn', 22017, 22017, 2017, 99999, 99999)
    ops.node(72017, 18.75, 8.5, 6.05)
    ops.element('elasticBeamColumn', 72017, 2017, 72017, 99999, 99999)
    ops.node(62017, 18.75, 8.275, 5.8)
    ops.element('elasticBeamColumn', 62017, 62017, 2017, 99999, 77777)
    ops.node(42017, 18.75, 8.725, 5.8)
    ops.element('elasticBeamColumn', 42017, 2017, 42017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12017, 2017, 12017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    # Central joint node
    ops.node(2018, 24.05, 8.5, 5.8, '-mass', 13.996626108528446, 13.996626108528446, 13.996626108528446, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52018, 23.775, 8.5, 5.8)
    ops.element('elasticBeamColumn', 52018, 52018, 2018, 99999, 88888)
    ops.node(22018, 24.05, 8.5, 5.55)
    ops.element('elasticBeamColumn', 22018, 22018, 2018, 99999, 99999)
    ops.node(72018, 24.05, 8.5, 6.05)
    ops.element('elasticBeamColumn', 72018, 2018, 72018, 99999, 99999)
    ops.node(62018, 24.05, 8.3, 5.8)
    ops.element('elasticBeamColumn', 62018, 62018, 2018, 99999, 77777)
    ops.node(42018, 24.05, 8.7, 5.8)
    ops.element('elasticBeamColumn', 42018, 2018, 42018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12018, 2018, 12018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    # Central joint node
    ops.node(2019, 0.0, 12.75, 5.8, '-mass', 8.980066367210195, 8.980066367210195, 8.980066367210195, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(32019, 0.125, 12.75, 5.8)
    ops.element('elasticBeamColumn', 32019, 2019, 32019, 99999, 88888)
    ops.node(22019, 0.0, 12.75, 5.525)
    ops.element('elasticBeamColumn', 22019, 22019, 2019, 99999, 99999)
    ops.node(72019, 0.0, 12.75, 6.075)
    ops.element('elasticBeamColumn', 72019, 2019, 72019, 99999, 99999)
    ops.node(62019, 0.0, 12.575, 5.8)
    ops.element('elasticBeamColumn', 62019, 62019, 2019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12019, 2019, 12019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    # Central joint node
    ops.node(2020, 5.3, 12.75, 5.8, '-mass', 13.741886047366366, 13.741886047366366, 13.741886047366366, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52020, 5.125, 12.75, 5.8)
    ops.element('elasticBeamColumn', 52020, 52020, 2020, 99999, 88888)
    ops.node(32020, 5.475, 12.75, 5.8)
    ops.element('elasticBeamColumn', 32020, 2020, 32020, 99999, 88888)
    ops.node(22020, 5.3, 12.75, 5.525)
    ops.element('elasticBeamColumn', 22020, 22020, 2020, 99999, 99999)
    ops.node(72020, 5.3, 12.75, 6.075)
    ops.element('elasticBeamColumn', 72020, 2020, 72020, 99999, 99999)
    ops.node(62020, 5.3, 12.475, 5.8)
    ops.element('elasticBeamColumn', 62020, 62020, 2020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12020, 2020, 12020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    # Central joint node
    ops.node(2021, 10.6, 12.75, 5.8, '-mass', 10.747498463152269, 10.747498463152269, 10.747498463152269, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52021, 10.45, 12.75, 5.8)
    ops.element('elasticBeamColumn', 52021, 52021, 2021, 99999, 88888)
    ops.node(32021, 10.75, 12.75, 5.8)
    ops.element('elasticBeamColumn', 32021, 2021, 32021, 99999, 88888)
    ops.node(22021, 10.6, 12.75, 5.525)
    ops.element('elasticBeamColumn', 22021, 22021, 2021, 99999, 99999)
    ops.node(72021, 10.6, 12.75, 6.075)
    ops.element('elasticBeamColumn', 72021, 2021, 72021, 99999, 99999)
    ops.node(62021, 10.6, 12.525, 5.8)
    ops.element('elasticBeamColumn', 62021, 62021, 2021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12021, 2021, 12021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    # Central joint node
    ops.node(2022, 13.45, 12.75, 5.8, '-mass', 10.74749846315227, 10.74749846315227, 10.74749846315227, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52022, 13.3, 12.75, 5.8)
    ops.element('elasticBeamColumn', 52022, 52022, 2022, 99999, 88888)
    ops.node(32022, 13.6, 12.75, 5.8)
    ops.element('elasticBeamColumn', 32022, 2022, 32022, 99999, 88888)
    ops.node(22022, 13.45, 12.75, 5.525)
    ops.element('elasticBeamColumn', 22022, 22022, 2022, 99999, 99999)
    ops.node(72022, 13.45, 12.75, 6.075)
    ops.element('elasticBeamColumn', 72022, 2022, 72022, 99999, 99999)
    ops.node(62022, 13.45, 12.525, 5.8)
    ops.element('elasticBeamColumn', 62022, 62022, 2022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12022, 2022, 12022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 2)
    # Central joint node
    ops.node(2023, 18.75, 12.75, 5.8, '-mass', 13.74188604736637, 13.74188604736637, 13.74188604736637, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52023, 18.575, 12.75, 5.8)
    ops.element('elasticBeamColumn', 52023, 52023, 2023, 99999, 88888)
    ops.node(32023, 18.925, 12.75, 5.8)
    ops.element('elasticBeamColumn', 32023, 2023, 32023, 99999, 88888)
    ops.node(22023, 18.75, 12.75, 5.525)
    ops.element('elasticBeamColumn', 22023, 22023, 2023, 99999, 99999)
    ops.node(72023, 18.75, 12.75, 6.075)
    ops.element('elasticBeamColumn', 72023, 2023, 72023, 99999, 99999)
    ops.node(62023, 18.75, 12.475, 5.8)
    ops.element('elasticBeamColumn', 62023, 62023, 2023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12023, 2023, 12023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 2)
    # Central joint node
    ops.node(2024, 24.05, 12.75, 5.8, '-mass', 8.980066367210199, 8.980066367210199, 8.980066367210199, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(52024, 23.925, 12.75, 5.8)
    ops.element('elasticBeamColumn', 52024, 52024, 2024, 99999, 88888)
    ops.node(22024, 24.05, 12.75, 5.525)
    ops.element('elasticBeamColumn', 22024, 22024, 2024, 99999, 99999)
    ops.node(72024, 24.05, 12.75, 6.075)
    ops.element('elasticBeamColumn', 72024, 2024, 72024, 99999, 99999)
    ops.node(62024, 24.05, 12.575, 5.8)
    ops.element('elasticBeamColumn', 62024, 62024, 2024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 12024, 2024, 12024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    # Central joint node
    ops.node(3001, 0.0, 0.0, 8.7, '-mass', 8.631442513999186, 8.631442513999186, 8.631442513999186, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33001, 0.125, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33001, 3001, 33001, 99999, 88888)
    ops.node(23001, 0.0, 0.0, 8.425)
    ops.element('elasticBeamColumn', 23001, 23001, 3001, 99999, 99999)
    ops.node(73001, 0.0, 0.0, 8.975)
    ops.element('elasticBeamColumn', 73001, 3001, 73001, 99999, 99999)
    ops.node(43001, 0.0, 0.125, 8.7)
    ops.element('elasticBeamColumn', 43001, 3001, 43001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13001, 3001, 13001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    # Central joint node
    ops.node(3002, 5.3, 0.0, 8.7, '-mass', 13.502436506081963, 13.502436506081963, 13.502436506081963, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53002, 5.175, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53002, 53002, 3002, 99999, 88888)
    ops.node(33002, 5.425, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33002, 3002, 33002, 99999, 88888)
    ops.node(23002, 5.3, 0.0, 8.425)
    ops.element('elasticBeamColumn', 23002, 23002, 3002, 99999, 99999)
    ops.node(73002, 5.3, 0.0, 8.975)
    ops.element('elasticBeamColumn', 73002, 3002, 73002, 99999, 99999)
    ops.node(43002, 5.3, 0.25, 8.7)
    ops.element('elasticBeamColumn', 43002, 3002, 43002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13002, 3002, 13002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    # Central joint node
    ops.node(3003, 10.6, 0.0, 8.7, '-mass', 9.182971565986954, 9.182971565986954, 9.182971565986954, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53003, 10.475, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53003, 53003, 3003, 99999, 88888)
    ops.node(33003, 10.725, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33003, 3003, 33003, 99999, 88888)
    ops.node(23003, 10.6, 0.0, 8.425)
    ops.element('elasticBeamColumn', 23003, 23003, 3003, 99999, 99999)
    ops.node(73003, 10.6, 0.0, 8.975)
    ops.element('elasticBeamColumn', 73003, 3003, 73003, 99999, 99999)
    ops.node(43003, 10.6, 0.2, 8.7)
    ops.element('elasticBeamColumn', 43003, 3003, 43003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13003, 3003, 13003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    # Central joint node
    ops.node(3004, 13.45, 0.0, 8.7, '-mass', 9.182971565986957, 9.182971565986957, 9.182971565986957, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53004, 13.325, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53004, 53004, 3004, 99999, 88888)
    ops.node(33004, 13.575, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33004, 3004, 33004, 99999, 88888)
    ops.node(23004, 13.45, 0.0, 8.425)
    ops.element('elasticBeamColumn', 23004, 23004, 3004, 99999, 99999)
    ops.node(73004, 13.45, 0.0, 8.975)
    ops.element('elasticBeamColumn', 73004, 3004, 73004, 99999, 99999)
    ops.node(43004, 13.45, 0.2, 8.7)
    ops.element('elasticBeamColumn', 43004, 3004, 43004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13004, 3004, 13004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    # Central joint node
    ops.node(3005, 18.75, 0.0, 8.7, '-mass', 13.502436506081967, 13.502436506081967, 13.502436506081967, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53005, 18.625, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53005, 53005, 3005, 99999, 88888)
    ops.node(33005, 18.875, 0.0, 8.7)
    ops.element('elasticBeamColumn', 33005, 3005, 33005, 99999, 88888)
    ops.node(23005, 18.75, 0.0, 8.425)
    ops.element('elasticBeamColumn', 23005, 23005, 3005, 99999, 99999)
    ops.node(73005, 18.75, 0.0, 8.975)
    ops.element('elasticBeamColumn', 73005, 3005, 73005, 99999, 99999)
    ops.node(43005, 18.75, 0.25, 8.7)
    ops.element('elasticBeamColumn', 43005, 3005, 43005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13005, 3005, 13005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    # Central joint node
    ops.node(3006, 24.05, 0.0, 8.7, '-mass', 8.63144251399919, 8.63144251399919, 8.63144251399919, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53006, 23.925, 0.0, 8.7)
    ops.element('elasticBeamColumn', 53006, 53006, 3006, 99999, 88888)
    ops.node(23006, 24.05, 0.0, 8.425)
    ops.element('elasticBeamColumn', 23006, 23006, 3006, 99999, 99999)
    ops.node(73006, 24.05, 0.0, 8.975)
    ops.element('elasticBeamColumn', 73006, 3006, 73006, 99999, 99999)
    ops.node(43006, 24.05, 0.125, 8.7)
    ops.element('elasticBeamColumn', 43006, 3006, 43006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13006, 3006, 13006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    # Central joint node
    ops.node(3007, 0.0, 4.25, 8.7, '-mass', 13.31711540516453, 13.31711540516453, 13.31711540516453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33007, 0.25, 4.25, 8.7)
    ops.element('elasticBeamColumn', 33007, 3007, 33007, 99999, 88888)
    ops.node(23007, 0.0, 4.25, 8.45)
    ops.element('elasticBeamColumn', 23007, 23007, 3007, 99999, 99999)
    ops.node(73007, 0.0, 4.25, 8.95)
    ops.element('elasticBeamColumn', 73007, 3007, 73007, 99999, 99999)
    ops.node(63007, 0.0, 4.075, 8.7)
    ops.element('elasticBeamColumn', 63007, 63007, 3007, 99999, 77777)
    ops.node(43007, 0.0, 4.425, 8.7)
    ops.element('elasticBeamColumn', 43007, 3007, 43007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13007, 3007, 13007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    # Central joint node
    ops.node(3008, 5.3, 4.25, 8.7, '-mass', 18.12006159524242, 18.12006159524242, 18.12006159524242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53008, 5.0, 4.25, 8.7)
    ops.element('elasticBeamColumn', 53008, 53008, 3008, 99999, 88888)
    ops.node(33008, 5.6, 4.25, 8.7)
    ops.element('elasticBeamColumn', 33008, 3008, 33008, 99999, 88888)
    ops.node(23008, 5.3, 4.25, 8.45)
    ops.element('elasticBeamColumn', 23008, 23008, 3008, 99999, 99999)
    ops.node(73008, 5.3, 4.25, 8.95)
    ops.element('elasticBeamColumn', 73008, 3008, 73008, 99999, 99999)
    ops.node(63008, 5.3, 4.075, 8.7)
    ops.element('elasticBeamColumn', 63008, 63008, 3008, 99999, 77777)
    ops.node(43008, 5.3, 4.425, 8.7)
    ops.element('elasticBeamColumn', 43008, 3008, 43008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13008, 3008, 13008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    # Central joint node
    ops.node(3009, 10.6, 4.25, 8.7, '-mass', 16.373213403247274, 16.373213403247274, 16.373213403247274, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53009, 10.35, 4.25, 8.7)
    ops.element('elasticBeamColumn', 53009, 53009, 3009, 99999, 88888)
    ops.node(33009, 10.85, 4.25, 8.7)
    ops.element('elasticBeamColumn', 33009, 3009, 33009, 99999, 88888)
    ops.node(23009, 10.6, 4.25, 8.45)
    ops.element('elasticBeamColumn', 23009, 23009, 3009, 99999, 99999)
    ops.node(73009, 10.6, 4.25, 8.95)
    ops.element('elasticBeamColumn', 73009, 3009, 73009, 99999, 99999)
    ops.node(63009, 10.6, 4.075, 8.7)
    ops.element('elasticBeamColumn', 63009, 63009, 3009, 99999, 77777)
    ops.node(43009, 10.6, 4.425, 8.7)
    ops.element('elasticBeamColumn', 43009, 3009, 43009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13009, 3009, 13009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    # Central joint node
    ops.node(3010, 13.45, 4.25, 8.7, '-mass', 16.373213403247274, 16.373213403247274, 16.373213403247274, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53010, 13.2, 4.25, 8.7)
    ops.element('elasticBeamColumn', 53010, 53010, 3010, 99999, 88888)
    ops.node(33010, 13.7, 4.25, 8.7)
    ops.element('elasticBeamColumn', 33010, 3010, 33010, 99999, 88888)
    ops.node(23010, 13.45, 4.25, 8.45)
    ops.element('elasticBeamColumn', 23010, 23010, 3010, 99999, 99999)
    ops.node(73010, 13.45, 4.25, 8.95)
    ops.element('elasticBeamColumn', 73010, 3010, 73010, 99999, 99999)
    ops.node(63010, 13.45, 4.075, 8.7)
    ops.element('elasticBeamColumn', 63010, 63010, 3010, 99999, 77777)
    ops.node(43010, 13.45, 4.425, 8.7)
    ops.element('elasticBeamColumn', 43010, 3010, 43010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13010, 3010, 13010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    # Central joint node
    ops.node(3011, 18.75, 4.25, 8.7, '-mass', 18.12006159524242, 18.12006159524242, 18.12006159524242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53011, 18.45, 4.25, 8.7)
    ops.element('elasticBeamColumn', 53011, 53011, 3011, 99999, 88888)
    ops.node(33011, 19.05, 4.25, 8.7)
    ops.element('elasticBeamColumn', 33011, 3011, 33011, 99999, 88888)
    ops.node(23011, 18.75, 4.25, 8.45)
    ops.element('elasticBeamColumn', 23011, 23011, 3011, 99999, 99999)
    ops.node(73011, 18.75, 4.25, 8.95)
    ops.element('elasticBeamColumn', 73011, 3011, 73011, 99999, 99999)
    ops.node(63011, 18.75, 4.075, 8.7)
    ops.element('elasticBeamColumn', 63011, 63011, 3011, 99999, 77777)
    ops.node(43011, 18.75, 4.425, 8.7)
    ops.element('elasticBeamColumn', 43011, 3011, 43011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13011, 3011, 13011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    # Central joint node
    ops.node(3012, 24.05, 4.25, 8.7, '-mass', 13.31711540516453, 13.31711540516453, 13.31711540516453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53012, 23.8, 4.25, 8.7)
    ops.element('elasticBeamColumn', 53012, 53012, 3012, 99999, 88888)
    ops.node(23012, 24.05, 4.25, 8.45)
    ops.element('elasticBeamColumn', 23012, 23012, 3012, 99999, 99999)
    ops.node(73012, 24.05, 4.25, 8.95)
    ops.element('elasticBeamColumn', 73012, 3012, 73012, 99999, 99999)
    ops.node(63012, 24.05, 4.075, 8.7)
    ops.element('elasticBeamColumn', 63012, 63012, 3012, 99999, 77777)
    ops.node(43012, 24.05, 4.425, 8.7)
    ops.element('elasticBeamColumn', 43012, 3012, 43012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13012, 3012, 13012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    # Central joint node
    ops.node(3013, 0.0, 8.5, 8.7, '-mass', 13.31711540516453, 13.31711540516453, 13.31711540516453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33013, 0.25, 8.5, 8.7)
    ops.element('elasticBeamColumn', 33013, 3013, 33013, 99999, 88888)
    ops.node(23013, 0.0, 8.5, 8.45)
    ops.element('elasticBeamColumn', 23013, 23013, 3013, 99999, 99999)
    ops.node(73013, 0.0, 8.5, 8.95)
    ops.element('elasticBeamColumn', 73013, 3013, 73013, 99999, 99999)
    ops.node(63013, 0.0, 8.325, 8.7)
    ops.element('elasticBeamColumn', 63013, 63013, 3013, 99999, 77777)
    ops.node(43013, 0.0, 8.675, 8.7)
    ops.element('elasticBeamColumn', 43013, 3013, 43013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13013, 3013, 13013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    # Central joint node
    ops.node(3014, 5.3, 8.5, 8.7, '-mass', 18.12006159524242, 18.12006159524242, 18.12006159524242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53014, 5.0, 8.5, 8.7)
    ops.element('elasticBeamColumn', 53014, 53014, 3014, 99999, 88888)
    ops.node(33014, 5.6, 8.5, 8.7)
    ops.element('elasticBeamColumn', 33014, 3014, 33014, 99999, 88888)
    ops.node(23014, 5.3, 8.5, 8.45)
    ops.element('elasticBeamColumn', 23014, 23014, 3014, 99999, 99999)
    ops.node(73014, 5.3, 8.5, 8.95)
    ops.element('elasticBeamColumn', 73014, 3014, 73014, 99999, 99999)
    ops.node(63014, 5.3, 8.325, 8.7)
    ops.element('elasticBeamColumn', 63014, 63014, 3014, 99999, 77777)
    ops.node(43014, 5.3, 8.675, 8.7)
    ops.element('elasticBeamColumn', 43014, 3014, 43014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13014, 3014, 13014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    # Central joint node
    ops.node(3015, 10.6, 8.5, 8.7, '-mass', 13.88286644720158, 13.88286644720158, 13.88286644720158, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53015, 10.4, 8.5, 8.7)
    ops.element('elasticBeamColumn', 53015, 53015, 3015, 99999, 88888)
    ops.node(33015, 10.8, 8.5, 8.7)
    ops.element('elasticBeamColumn', 33015, 3015, 33015, 99999, 88888)
    ops.node(23015, 10.6, 8.5, 8.45)
    ops.element('elasticBeamColumn', 23015, 23015, 3015, 99999, 99999)
    ops.node(73015, 10.6, 8.5, 8.95)
    ops.element('elasticBeamColumn', 73015, 3015, 73015, 99999, 99999)
    ops.node(63015, 10.6, 8.375, 8.7)
    ops.element('elasticBeamColumn', 63015, 63015, 3015, 99999, 77777)
    ops.node(43015, 10.6, 8.625, 8.7)
    ops.element('elasticBeamColumn', 43015, 3015, 43015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13015, 3015, 13015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    # Central joint node
    ops.node(3016, 13.45, 8.5, 8.7, '-mass', 13.882866447201582, 13.882866447201582, 13.882866447201582, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53016, 13.25, 8.5, 8.7)
    ops.element('elasticBeamColumn', 53016, 53016, 3016, 99999, 88888)
    ops.node(33016, 13.65, 8.5, 8.7)
    ops.element('elasticBeamColumn', 33016, 3016, 33016, 99999, 88888)
    ops.node(23016, 13.45, 8.5, 8.45)
    ops.element('elasticBeamColumn', 23016, 23016, 3016, 99999, 99999)
    ops.node(73016, 13.45, 8.5, 8.95)
    ops.element('elasticBeamColumn', 73016, 3016, 73016, 99999, 99999)
    ops.node(63016, 13.45, 8.375, 8.7)
    ops.element('elasticBeamColumn', 63016, 63016, 3016, 99999, 77777)
    ops.node(43016, 13.45, 8.625, 8.7)
    ops.element('elasticBeamColumn', 43016, 3016, 43016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13016, 3016, 13016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    # Central joint node
    ops.node(3017, 18.75, 8.5, 8.7, '-mass', 18.12006159524242, 18.12006159524242, 18.12006159524242, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53017, 18.45, 8.5, 8.7)
    ops.element('elasticBeamColumn', 53017, 53017, 3017, 99999, 88888)
    ops.node(33017, 19.05, 8.5, 8.7)
    ops.element('elasticBeamColumn', 33017, 3017, 33017, 99999, 88888)
    ops.node(23017, 18.75, 8.5, 8.45)
    ops.element('elasticBeamColumn', 23017, 23017, 3017, 99999, 99999)
    ops.node(73017, 18.75, 8.5, 8.95)
    ops.element('elasticBeamColumn', 73017, 3017, 73017, 99999, 99999)
    ops.node(63017, 18.75, 8.325, 8.7)
    ops.element('elasticBeamColumn', 63017, 63017, 3017, 99999, 77777)
    ops.node(43017, 18.75, 8.675, 8.7)
    ops.element('elasticBeamColumn', 43017, 3017, 43017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13017, 3017, 13017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    # Central joint node
    ops.node(3018, 24.05, 8.5, 8.7, '-mass', 13.31711540516453, 13.31711540516453, 13.31711540516453, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53018, 23.8, 8.5, 8.7)
    ops.element('elasticBeamColumn', 53018, 53018, 3018, 99999, 88888)
    ops.node(23018, 24.05, 8.5, 8.45)
    ops.element('elasticBeamColumn', 23018, 23018, 3018, 99999, 99999)
    ops.node(73018, 24.05, 8.5, 8.95)
    ops.element('elasticBeamColumn', 73018, 3018, 73018, 99999, 99999)
    ops.node(63018, 24.05, 8.325, 8.7)
    ops.element('elasticBeamColumn', 63018, 63018, 3018, 99999, 77777)
    ops.node(43018, 24.05, 8.675, 8.7)
    ops.element('elasticBeamColumn', 43018, 3018, 43018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13018, 3018, 13018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    # Central joint node
    ops.node(3019, 0.0, 12.75, 8.7, '-mass', 8.631442513999186, 8.631442513999186, 8.631442513999186, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(33019, 0.125, 12.75, 8.7)
    ops.element('elasticBeamColumn', 33019, 3019, 33019, 99999, 88888)
    ops.node(23019, 0.0, 12.75, 8.425)
    ops.element('elasticBeamColumn', 23019, 23019, 3019, 99999, 99999)
    ops.node(73019, 0.0, 12.75, 8.975)
    ops.element('elasticBeamColumn', 73019, 3019, 73019, 99999, 99999)
    ops.node(63019, 0.0, 12.625, 8.7)
    ops.element('elasticBeamColumn', 63019, 63019, 3019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13019, 3019, 13019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    # Central joint node
    ops.node(3020, 5.3, 12.75, 8.7, '-mass', 13.502436506081963, 13.502436506081963, 13.502436506081963, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53020, 5.175, 12.75, 8.7)
    ops.element('elasticBeamColumn', 53020, 53020, 3020, 99999, 88888)
    ops.node(33020, 5.425, 12.75, 8.7)
    ops.element('elasticBeamColumn', 33020, 3020, 33020, 99999, 88888)
    ops.node(23020, 5.3, 12.75, 8.425)
    ops.element('elasticBeamColumn', 23020, 23020, 3020, 99999, 99999)
    ops.node(73020, 5.3, 12.75, 8.975)
    ops.element('elasticBeamColumn', 73020, 3020, 73020, 99999, 99999)
    ops.node(63020, 5.3, 12.5, 8.7)
    ops.element('elasticBeamColumn', 63020, 63020, 3020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13020, 3020, 13020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    # Central joint node
    ops.node(3021, 10.6, 12.75, 8.7, '-mass', 10.51401222462016, 10.51401222462016, 10.51401222462016, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53021, 10.475, 12.75, 8.7)
    ops.element('elasticBeamColumn', 53021, 53021, 3021, 99999, 88888)
    ops.node(33021, 10.725, 12.75, 8.7)
    ops.element('elasticBeamColumn', 33021, 3021, 33021, 99999, 88888)
    ops.node(23021, 10.6, 12.75, 8.425)
    ops.element('elasticBeamColumn', 23021, 23021, 3021, 99999, 99999)
    ops.node(73021, 10.6, 12.75, 8.975)
    ops.element('elasticBeamColumn', 73021, 3021, 73021, 99999, 99999)
    ops.node(63021, 10.6, 12.575, 8.7)
    ops.element('elasticBeamColumn', 63021, 63021, 3021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13021, 3021, 13021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    # Central joint node
    ops.node(3022, 13.45, 12.75, 8.7, '-mass', 10.514012224620162, 10.514012224620162, 10.514012224620162, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53022, 13.325, 12.75, 8.7)
    ops.element('elasticBeamColumn', 53022, 53022, 3022, 99999, 88888)
    ops.node(33022, 13.575, 12.75, 8.7)
    ops.element('elasticBeamColumn', 33022, 3022, 33022, 99999, 88888)
    ops.node(23022, 13.45, 12.75, 8.425)
    ops.element('elasticBeamColumn', 23022, 23022, 3022, 99999, 99999)
    ops.node(73022, 13.45, 12.75, 8.975)
    ops.element('elasticBeamColumn', 73022, 3022, 73022, 99999, 99999)
    ops.node(63022, 13.45, 12.575, 8.7)
    ops.element('elasticBeamColumn', 63022, 63022, 3022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13022, 3022, 13022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 3)
    # Central joint node
    ops.node(3023, 18.75, 12.75, 8.7, '-mass', 13.502436506081967, 13.502436506081967, 13.502436506081967, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53023, 18.625, 12.75, 8.7)
    ops.element('elasticBeamColumn', 53023, 53023, 3023, 99999, 88888)
    ops.node(33023, 18.875, 12.75, 8.7)
    ops.element('elasticBeamColumn', 33023, 3023, 33023, 99999, 88888)
    ops.node(23023, 18.75, 12.75, 8.425)
    ops.element('elasticBeamColumn', 23023, 23023, 3023, 99999, 99999)
    ops.node(73023, 18.75, 12.75, 8.975)
    ops.element('elasticBeamColumn', 73023, 3023, 73023, 99999, 99999)
    ops.node(63023, 18.75, 12.5, 8.7)
    ops.element('elasticBeamColumn', 63023, 63023, 3023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13023, 3023, 13023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 3)
    # Central joint node
    ops.node(3024, 24.05, 12.75, 8.7, '-mass', 8.63144251399919, 8.63144251399919, 8.63144251399919, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(53024, 23.925, 12.75, 8.7)
    ops.element('elasticBeamColumn', 53024, 53024, 3024, 99999, 88888)
    ops.node(23024, 24.05, 12.75, 8.425)
    ops.element('elasticBeamColumn', 23024, 23024, 3024, 99999, 99999)
    ops.node(73024, 24.05, 12.75, 8.975)
    ops.element('elasticBeamColumn', 73024, 3024, 73024, 99999, 99999)
    ops.node(63024, 24.05, 12.625, 8.7)
    ops.element('elasticBeamColumn', 63024, 63024, 3024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 13024, 3024, 13024, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    # Central joint node
    ops.node(4001, 0.0, 0.0, 11.6, '-mass', 4.109755459972684, 4.109755459972684, 4.109755459972684, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34001, 0.125, 0.0, 11.6)
    ops.element('elasticBeamColumn', 34001, 4001, 34001, 99999, 88888)
    ops.node(24001, 0.0, 0.0, 11.375)
    ops.element('elasticBeamColumn', 24001, 24001, 4001, 99999, 99999)
    ops.node(44001, 0.0, 0.125, 11.6)
    ops.element('elasticBeamColumn', 44001, 4001, 44001, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14001, 4001, 14001, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    # Central joint node
    ops.node(4002, 5.3, 0.0, 11.6, '-mass', 7.907584314440781, 7.907584314440781, 7.907584314440781, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54002, 5.175, 0.0, 11.6)
    ops.element('elasticBeamColumn', 54002, 54002, 4002, 99999, 88888)
    ops.node(34002, 5.425, 0.0, 11.6)
    ops.element('elasticBeamColumn', 34002, 4002, 34002, 99999, 88888)
    ops.node(24002, 5.3, 0.0, 11.375)
    ops.element('elasticBeamColumn', 24002, 24002, 4002, 99999, 99999)
    ops.node(44002, 5.3, 0.25, 11.6)
    ops.element('elasticBeamColumn', 44002, 4002, 44002, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14002, 4002, 14002, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    # Central joint node
    ops.node(4003, 10.6, 0.0, 11.6, '-mass', 4.613578089942103, 4.613578089942103, 4.613578089942103, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54003, 10.475, 0.0, 11.6)
    ops.element('elasticBeamColumn', 54003, 54003, 4003, 99999, 88888)
    ops.node(34003, 10.725, 0.0, 11.6)
    ops.element('elasticBeamColumn', 34003, 4003, 34003, 99999, 88888)
    ops.node(24003, 10.6, 0.0, 11.375)
    ops.element('elasticBeamColumn', 24003, 24003, 4003, 99999, 99999)
    ops.node(44003, 10.6, 0.2, 11.6)
    ops.element('elasticBeamColumn', 44003, 4003, 44003, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14003, 4003, 14003, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    # Central joint node
    ops.node(4004, 13.45, 0.0, 11.6, '-mass', 4.613578089942103, 4.613578089942103, 4.613578089942103, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54004, 13.325, 0.0, 11.6)
    ops.element('elasticBeamColumn', 54004, 54004, 4004, 99999, 88888)
    ops.node(34004, 13.575, 0.0, 11.6)
    ops.element('elasticBeamColumn', 34004, 4004, 34004, 99999, 88888)
    ops.node(24004, 13.45, 0.0, 11.375)
    ops.element('elasticBeamColumn', 24004, 24004, 4004, 99999, 99999)
    ops.node(44004, 13.45, 0.2, 11.6)
    ops.element('elasticBeamColumn', 44004, 4004, 44004, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14004, 4004, 14004, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    # Central joint node
    ops.node(4005, 18.75, 0.0, 11.6, '-mass', 7.907584314440782, 7.907584314440782, 7.907584314440782, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54005, 18.625, 0.0, 11.6)
    ops.element('elasticBeamColumn', 54005, 54005, 4005, 99999, 88888)
    ops.node(34005, 18.875, 0.0, 11.6)
    ops.element('elasticBeamColumn', 34005, 4005, 34005, 99999, 88888)
    ops.node(24005, 18.75, 0.0, 11.375)
    ops.element('elasticBeamColumn', 24005, 24005, 4005, 99999, 99999)
    ops.node(44005, 18.75, 0.25, 11.6)
    ops.element('elasticBeamColumn', 44005, 4005, 44005, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14005, 4005, 14005, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    # Central joint node
    ops.node(4006, 24.05, 0.0, 11.6, '-mass', 4.109755459972685, 4.109755459972685, 4.109755459972685, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54006, 23.925, 0.0, 11.6)
    ops.element('elasticBeamColumn', 54006, 54006, 4006, 99999, 88888)
    ops.node(24006, 24.05, 0.0, 11.375)
    ops.element('elasticBeamColumn', 24006, 24006, 4006, 99999, 99999)
    ops.node(44006, 24.05, 0.125, 11.6)
    ops.element('elasticBeamColumn', 44006, 4006, 44006, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14006, 4006, 14006, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    # Central joint node
    ops.node(4007, 0.0, 4.25, 11.6, '-mass', 8.25100939089338, 8.25100939089338, 8.25100939089338, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34007, 0.25, 4.25, 11.6)
    ops.element('elasticBeamColumn', 34007, 4007, 34007, 99999, 88888)
    ops.node(24007, 0.0, 4.25, 11.375)
    ops.element('elasticBeamColumn', 24007, 24007, 4007, 99999, 99999)
    ops.node(64007, 0.0, 4.075, 11.6)
    ops.element('elasticBeamColumn', 64007, 64007, 4007, 99999, 77777)
    ops.node(44007, 0.0, 4.425, 11.6)
    ops.element('elasticBeamColumn', 44007, 4007, 44007, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14007, 4007, 14007, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    # Central joint node
    ops.node(4008, 5.3, 4.25, 11.6, '-mass', 15.381529485150674, 15.381529485150674, 15.381529485150674, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54008, 5.0, 4.25, 11.6)
    ops.element('elasticBeamColumn', 54008, 54008, 4008, 99999, 88888)
    ops.node(34008, 5.6, 4.25, 11.6)
    ops.element('elasticBeamColumn', 34008, 4008, 34008, 99999, 88888)
    ops.node(24008, 5.3, 4.25, 11.375)
    ops.element('elasticBeamColumn', 24008, 24008, 4008, 99999, 99999)
    ops.node(64008, 5.3, 4.075, 11.6)
    ops.element('elasticBeamColumn', 64008, 64008, 4008, 99999, 77777)
    ops.node(44008, 5.3, 4.425, 11.6)
    ops.element('elasticBeamColumn', 44008, 4008, 44008, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14008, 4008, 14008, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    # Central joint node
    ops.node(4009, 10.6, 4.25, 11.6, '-mass', 12.654571711096409, 12.654571711096409, 12.654571711096409, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54009, 10.35, 4.25, 11.6)
    ops.element('elasticBeamColumn', 54009, 54009, 4009, 99999, 88888)
    ops.node(34009, 10.85, 4.25, 11.6)
    ops.element('elasticBeamColumn', 34009, 4009, 34009, 99999, 88888)
    ops.node(24009, 10.6, 4.25, 11.375)
    ops.element('elasticBeamColumn', 24009, 24009, 4009, 99999, 99999)
    ops.node(64009, 10.6, 4.075, 11.6)
    ops.element('elasticBeamColumn', 64009, 64009, 4009, 99999, 77777)
    ops.node(44009, 10.6, 4.425, 11.6)
    ops.element('elasticBeamColumn', 44009, 4009, 44009, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14009, 4009, 14009, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    # Central joint node
    ops.node(4010, 13.45, 4.25, 11.6, '-mass', 12.654571711096409, 12.654571711096409, 12.654571711096409, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54010, 13.2, 4.25, 11.6)
    ops.element('elasticBeamColumn', 54010, 54010, 4010, 99999, 88888)
    ops.node(34010, 13.7, 4.25, 11.6)
    ops.element('elasticBeamColumn', 34010, 4010, 34010, 99999, 88888)
    ops.node(24010, 13.45, 4.25, 11.375)
    ops.element('elasticBeamColumn', 24010, 24010, 4010, 99999, 99999)
    ops.node(64010, 13.45, 4.075, 11.6)
    ops.element('elasticBeamColumn', 64010, 64010, 4010, 99999, 77777)
    ops.node(44010, 13.45, 4.425, 11.6)
    ops.element('elasticBeamColumn', 44010, 4010, 44010, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14010, 4010, 14010, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    # Central joint node
    ops.node(4011, 18.75, 4.25, 11.6, '-mass', 15.381529485150677, 15.381529485150677, 15.381529485150677, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54011, 18.45, 4.25, 11.6)
    ops.element('elasticBeamColumn', 54011, 54011, 4011, 99999, 88888)
    ops.node(34011, 19.05, 4.25, 11.6)
    ops.element('elasticBeamColumn', 34011, 4011, 34011, 99999, 88888)
    ops.node(24011, 18.75, 4.25, 11.375)
    ops.element('elasticBeamColumn', 24011, 24011, 4011, 99999, 99999)
    ops.node(64011, 18.75, 4.075, 11.6)
    ops.element('elasticBeamColumn', 64011, 64011, 4011, 99999, 77777)
    ops.node(44011, 18.75, 4.425, 11.6)
    ops.element('elasticBeamColumn', 44011, 4011, 44011, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14011, 4011, 14011, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    # Central joint node
    ops.node(4012, 24.05, 4.25, 11.6, '-mass', 8.251009390893383, 8.251009390893383, 8.251009390893383, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54012, 23.8, 4.25, 11.6)
    ops.element('elasticBeamColumn', 54012, 54012, 4012, 99999, 88888)
    ops.node(24012, 24.05, 4.25, 11.375)
    ops.element('elasticBeamColumn', 24012, 24012, 4012, 99999, 99999)
    ops.node(64012, 24.05, 4.075, 11.6)
    ops.element('elasticBeamColumn', 64012, 64012, 4012, 99999, 77777)
    ops.node(44012, 24.05, 4.425, 11.6)
    ops.element('elasticBeamColumn', 44012, 4012, 44012, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14012, 4012, 14012, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    # Central joint node
    ops.node(4013, 0.0, 8.5, 11.6, '-mass', 8.25100939089338, 8.25100939089338, 8.25100939089338, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34013, 0.25, 8.5, 11.6)
    ops.element('elasticBeamColumn', 34013, 4013, 34013, 99999, 88888)
    ops.node(24013, 0.0, 8.5, 11.375)
    ops.element('elasticBeamColumn', 24013, 24013, 4013, 99999, 99999)
    ops.node(64013, 0.0, 8.325, 11.6)
    ops.element('elasticBeamColumn', 64013, 64013, 4013, 99999, 77777)
    ops.node(44013, 0.0, 8.675, 11.6)
    ops.element('elasticBeamColumn', 44013, 4013, 44013, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14013, 4013, 14013, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    # Central joint node
    ops.node(4014, 5.3, 8.5, 11.6, '-mass', 15.381529485150674, 15.381529485150674, 15.381529485150674, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54014, 5.0, 8.5, 11.6)
    ops.element('elasticBeamColumn', 54014, 54014, 4014, 99999, 88888)
    ops.node(34014, 5.6, 8.5, 11.6)
    ops.element('elasticBeamColumn', 34014, 4014, 34014, 99999, 88888)
    ops.node(24014, 5.3, 8.5, 11.375)
    ops.element('elasticBeamColumn', 24014, 24014, 4014, 99999, 99999)
    ops.node(64014, 5.3, 8.325, 11.6)
    ops.element('elasticBeamColumn', 64014, 64014, 4014, 99999, 77777)
    ops.node(44014, 5.3, 8.675, 11.6)
    ops.element('elasticBeamColumn', 44014, 4014, 44014, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14014, 4014, 14014, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    # Central joint node
    ops.node(4015, 10.6, 8.5, 11.6, '-mass', 11.761383266773445, 11.761383266773445, 11.761383266773445, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54015, 10.4, 8.5, 11.6)
    ops.element('elasticBeamColumn', 54015, 54015, 4015, 99999, 88888)
    ops.node(34015, 10.8, 8.5, 11.6)
    ops.element('elasticBeamColumn', 34015, 4015, 34015, 99999, 88888)
    ops.node(24015, 10.6, 8.5, 11.375)
    ops.element('elasticBeamColumn', 24015, 24015, 4015, 99999, 99999)
    ops.node(64015, 10.6, 8.375, 11.6)
    ops.element('elasticBeamColumn', 64015, 64015, 4015, 99999, 77777)
    ops.node(44015, 10.6, 8.625, 11.6)
    ops.element('elasticBeamColumn', 44015, 4015, 44015, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14015, 4015, 14015, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    # Central joint node
    ops.node(4016, 13.45, 8.5, 11.6, '-mass', 11.761383266773446, 11.761383266773446, 11.761383266773446, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54016, 13.25, 8.5, 11.6)
    ops.element('elasticBeamColumn', 54016, 54016, 4016, 99999, 88888)
    ops.node(34016, 13.65, 8.5, 11.6)
    ops.element('elasticBeamColumn', 34016, 4016, 34016, 99999, 88888)
    ops.node(24016, 13.45, 8.5, 11.375)
    ops.element('elasticBeamColumn', 24016, 24016, 4016, 99999, 99999)
    ops.node(64016, 13.45, 8.375, 11.6)
    ops.element('elasticBeamColumn', 64016, 64016, 4016, 99999, 77777)
    ops.node(44016, 13.45, 8.625, 11.6)
    ops.element('elasticBeamColumn', 44016, 4016, 44016, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14016, 4016, 14016, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    # Central joint node
    ops.node(4017, 18.75, 8.5, 11.6, '-mass', 15.381529485150677, 15.381529485150677, 15.381529485150677, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54017, 18.45, 8.5, 11.6)
    ops.element('elasticBeamColumn', 54017, 54017, 4017, 99999, 88888)
    ops.node(34017, 19.05, 8.5, 11.6)
    ops.element('elasticBeamColumn', 34017, 4017, 34017, 99999, 88888)
    ops.node(24017, 18.75, 8.5, 11.375)
    ops.element('elasticBeamColumn', 24017, 24017, 4017, 99999, 99999)
    ops.node(64017, 18.75, 8.325, 11.6)
    ops.element('elasticBeamColumn', 64017, 64017, 4017, 99999, 77777)
    ops.node(44017, 18.75, 8.675, 11.6)
    ops.element('elasticBeamColumn', 44017, 4017, 44017, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14017, 4017, 14017, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    # Central joint node
    ops.node(4018, 24.05, 8.5, 11.6, '-mass', 8.251009390893383, 8.251009390893383, 8.251009390893383, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54018, 23.8, 8.5, 11.6)
    ops.element('elasticBeamColumn', 54018, 54018, 4018, 99999, 88888)
    ops.node(24018, 24.05, 8.5, 11.375)
    ops.element('elasticBeamColumn', 24018, 24018, 4018, 99999, 99999)
    ops.node(64018, 24.05, 8.325, 11.6)
    ops.element('elasticBeamColumn', 64018, 64018, 4018, 99999, 77777)
    ops.node(44018, 24.05, 8.675, 11.6)
    ops.element('elasticBeamColumn', 44018, 4018, 44018, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14018, 4018, 14018, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    # Central joint node
    ops.node(4019, 0.0, 12.75, 11.6, '-mass', 4.109755459972684, 4.109755459972684, 4.109755459972684, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(34019, 0.125, 12.75, 11.6)
    ops.element('elasticBeamColumn', 34019, 4019, 34019, 99999, 88888)
    ops.node(24019, 0.0, 12.75, 11.375)
    ops.element('elasticBeamColumn', 24019, 24019, 4019, 99999, 99999)
    ops.node(64019, 0.0, 12.625, 11.6)
    ops.element('elasticBeamColumn', 64019, 64019, 4019, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14019, 4019, 14019, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    # Central joint node
    ops.node(4020, 5.3, 12.75, 11.6, '-mass', 7.907584314440781, 7.907584314440781, 7.907584314440781, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54020, 5.175, 12.75, 11.6)
    ops.element('elasticBeamColumn', 54020, 54020, 4020, 99999, 88888)
    ops.node(34020, 5.425, 12.75, 11.6)
    ops.element('elasticBeamColumn', 34020, 4020, 34020, 99999, 88888)
    ops.node(24020, 5.3, 12.75, 11.375)
    ops.element('elasticBeamColumn', 24020, 24020, 4020, 99999, 99999)
    ops.node(64020, 5.3, 12.5, 11.6)
    ops.element('elasticBeamColumn', 64020, 64020, 4020, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14020, 4020, 14020, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    # Central joint node
    ops.node(4021, 10.6, 12.75, 11.6, '-mass', 6.125875119625256, 6.125875119625256, 6.125875119625256, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54021, 10.475, 12.75, 11.6)
    ops.element('elasticBeamColumn', 54021, 54021, 4021, 99999, 88888)
    ops.node(34021, 10.725, 12.75, 11.6)
    ops.element('elasticBeamColumn', 34021, 4021, 34021, 99999, 88888)
    ops.node(24021, 10.6, 12.75, 11.375)
    ops.element('elasticBeamColumn', 24021, 24021, 4021, 99999, 99999)
    ops.node(64021, 10.6, 12.575, 11.6)
    ops.element('elasticBeamColumn', 64021, 64021, 4021, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14021, 4021, 14021, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    # Central joint node
    ops.node(4022, 13.45, 12.75, 11.6, '-mass', 6.125875119625256, 6.125875119625256, 6.125875119625256, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54022, 13.325, 12.75, 11.6)
    ops.element('elasticBeamColumn', 54022, 54022, 4022, 99999, 88888)
    ops.node(34022, 13.575, 12.75, 11.6)
    ops.element('elasticBeamColumn', 34022, 4022, 34022, 99999, 88888)
    ops.node(24022, 13.45, 12.75, 11.375)
    ops.element('elasticBeamColumn', 24022, 24022, 4022, 99999, 99999)
    ops.node(64022, 13.45, 12.575, 11.6)
    ops.element('elasticBeamColumn', 64022, 64022, 4022, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14022, 4022, 14022, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (4, 3, 4)
    # Central joint node
    ops.node(4023, 18.75, 12.75, 11.6, '-mass', 7.907584314440782, 7.907584314440782, 7.907584314440782, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54023, 18.625, 12.75, 11.6)
    ops.element('elasticBeamColumn', 54023, 54023, 4023, 99999, 88888)
    ops.node(34023, 18.875, 12.75, 11.6)
    ops.element('elasticBeamColumn', 34023, 4023, 34023, 99999, 88888)
    ops.node(24023, 18.75, 12.75, 11.375)
    ops.element('elasticBeamColumn', 24023, 24023, 4023, 99999, 99999)
    ops.node(64023, 18.75, 12.5, 11.6)
    ops.element('elasticBeamColumn', 64023, 64023, 4023, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14023, 4023, 14023, 99999, '-orient', 0, 0, 1, 0, 1, 0)

    # Joint grid ids (x, y, z): (5, 3, 4)
    # Central joint node
    ops.node(4024, 24.05, 12.75, 11.6, '-mass', 4.109755459972685, 4.109755459972685, 4.109755459972685, 0.0, 0.0, 0.0)
    # Rigid-joint offset elements
    ops.node(54024, 23.925, 12.75, 11.6)
    ops.element('elasticBeamColumn', 54024, 54024, 4024, 99999, 88888)
    ops.node(24024, 24.05, 12.75, 11.375)
    ops.element('elasticBeamColumn', 24024, 24024, 4024, 99999, 99999)
    ops.node(64024, 24.05, 12.625, 11.6)
    ops.element('elasticBeamColumn', 64024, 64024, 4024, 99999, 77777)
    # Joint flexibility element: Rigid
    ops.element('zeroLengthSection', 14024, 4024, 14024, 99999, '-orient', 0, 0, 1, 0, 1, 0)
