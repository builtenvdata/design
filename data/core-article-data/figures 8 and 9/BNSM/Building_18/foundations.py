import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 1
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.2675840978593272, 0.2675840978593272, 0.2675840978593272, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 0.0, 4.6, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 0.0, 4.6, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 0.0, 9.2, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 0.0, 9.2, 0.0, '-mass', 0.2675840978593272, 0.2675840978593272, 0.2675840978593272, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 2
    # Fixed node
    ops.node(2, 4.95, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 4.95, 0.0, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 4.95, 4.6, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 4.95, 4.6, 0.0, '-mass', 0.5244648318042813, 0.5244648318042813, 0.5244648318042813, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 4.95, 9.2, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 4.95, 9.2, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4046
    # Fixed node
    ops.node(3, 9.9, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 9.9, 0.0, 0.0, '-mass', 0.1926605504587156, 0.1926605504587156, 0.1926605504587156, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 9.9, 4.6, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 9.9, 4.6, 0.0, '-mass', 0.5244648318042813, 0.5244648318042813, 0.5244648318042813, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 9.9, 9.2, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 9.9, 9.2, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4048
    # Fixed node
    ops.node(4, 12.9, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 12.9, 0.0, 0.0, '-mass', 0.1926605504587156, 0.1926605504587156, 0.1926605504587156, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 12.9, 4.6, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 12.9, 4.6, 0.0, '-mass', 0.5244648318042813, 0.5244648318042813, 0.5244648318042813, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 12.9, 9.2, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 12.9, 9.2, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 5
    # Fixed node
    ops.node(5, 17.85, 0.0, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 17.85, 0.0, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 17.85, 4.6, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 17.85, 4.6, 0.0, '-mass', 0.5244648318042813, 0.5244648318042813, 0.5244648318042813, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 17.85, 9.2, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 17.85, 9.2, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 22.8, 0.0, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 22.8, 0.0, 0.0, '-mass', 0.2675840978593272, 0.2675840978593272, 0.2675840978593272, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 22.8, 4.6, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 22.8, 4.6, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 22.8, 9.2, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 22.8, 9.2, 0.0, '-mass', 0.2675840978593272, 0.2675840978593272, 0.2675840978593272, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)
