import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 4074
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.16972477064220182, 0.16972477064220182, 0.16972477064220182, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 5
    # Fixed node
    ops.node(5, 0.0, 5.15, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 0.0, 5.15, 0.0, '-mass', 0.5091743119266056, 0.5091743119266056, 0.5091743119266056, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 0.0, 10.3, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 0.0, 10.3, 0.0, '-mass', 0.5657492354740061, 0.5657492354740061, 0.5657492354740061, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 0.0, 15.45, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 0.0, 15.45, 0.0, '-mass', 0.5657492354740061, 0.5657492354740061, 0.5657492354740061, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 0.0, 20.6, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 0.0, 20.6, 0.0, '-mass', 0.5657492354740061, 0.5657492354740061, 0.5657492354740061, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 21
    # Fixed node
    ops.node(21, 0.0, 25.75, 0.0)
    ops.fix(21, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70021, 0.0, 25.75, 0.0, '-mass', 0.5657492354740061, 0.5657492354740061, 0.5657492354740061, 0.0, 0.0, 0.0)
    ops.equalDOF(21, 70021, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 25
    # Fixed node
    ops.node(25, 0.0, 30.9, 0.0)
    ops.fix(25, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70025, 0.0, 30.9, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(25, 70025, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4076
    # Fixed node
    ops.node(2, 2.95, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 2.95, 0.0, 0.0, '-mass', 0.6110091743119267, 0.6110091743119267, 0.6110091743119267, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 2.95, 5.15, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 2.95, 5.15, 0.0, '-mass', 1.3464831804281345, 1.3464831804281345, 1.3464831804281345, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 2.95, 10.3, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 2.95, 10.3, 0.0, '-mass', 1.2672782874617734, 1.2672782874617734, 1.2672782874617734, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 2.95, 15.45, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 2.95, 15.45, 0.0, '-mass', 1.2672782874617734, 1.2672782874617734, 1.2672782874617734, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 2.95, 20.6, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 2.95, 20.6, 0.0, '-mass', 1.2672782874617734, 1.2672782874617734, 1.2672782874617734, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 22
    # Fixed node
    ops.node(22, 2.95, 25.75, 0.0)
    ops.fix(22, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70022, 2.95, 25.75, 0.0, '-mass', 1.2672782874617734, 1.2672782874617734, 1.2672782874617734, 0.0, 0.0, 0.0)
    ops.equalDOF(22, 70022, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 26
    # Fixed node
    ops.node(26, 2.95, 30.9, 0.0)
    ops.fix(26, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70026, 2.95, 30.9, 0.0, '-mass', 1.2220183486238534, 1.2220183486238534, 1.2220183486238534, 0.0, 0.0, 0.0)
    ops.equalDOF(26, 70026, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3
    # Fixed node
    ops.node(3, 7.7, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 7.7, 0.0, 0.0, '-mass', 1.5840978593272168, 1.5840978593272168, 1.5840978593272168, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 7.7, 5.15, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 7.7, 5.15, 0.0, '-mass', 2.0366972477064222, 2.0366972477064222, 2.0366972477064222, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 7.7, 10.3, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 7.7, 10.3, 0.0, '-mass', 2.0366972477064222, 2.0366972477064222, 2.0366972477064222, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 7.7, 15.45, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 7.7, 15.45, 0.0, '-mass', 2.0366972477064222, 2.0366972477064222, 2.0366972477064222, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 19
    # Fixed node
    ops.node(19, 7.7, 20.6, 0.0)
    ops.fix(19, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70019, 7.7, 20.6, 0.0, '-mass', 2.0366972477064222, 2.0366972477064222, 2.0366972477064222, 0.0, 0.0, 0.0)
    ops.equalDOF(19, 70019, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 23
    # Fixed node
    ops.node(23, 7.7, 25.75, 0.0)
    ops.fix(23, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70023, 7.7, 25.75, 0.0, '-mass', 2.0366972477064222, 2.0366972477064222, 2.0366972477064222, 0.0, 0.0, 0.0)
    ops.equalDOF(23, 70023, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 27
    # Fixed node
    ops.node(27, 7.7, 30.9, 0.0)
    ops.fix(27, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70027, 7.7, 30.9, 0.0, '-mass', 1.5840978593272168, 1.5840978593272168, 1.5840978593272168, 0.0, 0.0, 0.0)
    ops.equalDOF(27, 70027, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4
    # Fixed node
    ops.node(4, 12.45, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 12.45, 0.0, 0.0, '-mass', 0.7128440366972478, 0.7128440366972478, 0.7128440366972478, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 12.45, 5.15, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 12.45, 5.15, 0.0, '-mass', 1.018348623853211, 1.018348623853211, 1.018348623853211, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 12.45, 10.3, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 12.45, 10.3, 0.0, '-mass', 1.018348623853211, 1.018348623853211, 1.018348623853211, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 12.45, 15.45, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 12.45, 15.45, 0.0, '-mass', 1.018348623853211, 1.018348623853211, 1.018348623853211, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 20
    # Fixed node
    ops.node(20, 12.45, 20.6, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 12.45, 20.6, 0.0, '-mass', 1.018348623853211, 1.018348623853211, 1.018348623853211, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 24
    # Fixed node
    ops.node(24, 12.45, 25.75, 0.0)
    ops.fix(24, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70024, 12.45, 25.75, 0.0, '-mass', 1.018348623853211, 1.018348623853211, 1.018348623853211, 0.0, 0.0, 0.0)
    ops.equalDOF(24, 70024, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 28
    # Fixed node
    ops.node(28, 12.45, 30.9, 0.0)
    ops.fix(28, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70028, 12.45, 30.9, 0.0, '-mass', 0.7128440366972478, 0.7128440366972478, 0.7128440366972478, 0.0, 0.0, 0.0)
    ops.equalDOF(28, 70028, 1, 2, 3, 4, 5, 6)
