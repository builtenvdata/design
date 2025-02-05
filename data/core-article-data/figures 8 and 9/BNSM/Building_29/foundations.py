import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 4052
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.1337920489296636, 0.1337920489296636, 0.1337920489296636, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 5
    # Fixed node
    ops.node(5, 0.0, 4.05, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 0.0, 4.05, 0.0, '-mass', 0.32110091743119257, 0.32110091743119257, 0.32110091743119257, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 0.0, 8.1, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 0.0, 8.1, 0.0, '-mass', 0.32110091743119257, 0.32110091743119257, 0.32110091743119257, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 0.0, 12.15, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 0.0, 12.15, 0.0, '-mass', 0.32110091743119257, 0.32110091743119257, 0.32110091743119257, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 0.0, 16.2, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 0.0, 16.2, 0.0, '-mass', 0.2675840978593272, 0.2675840978593272, 0.2675840978593272, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4054
    # Fixed node
    ops.node(2, 2.9, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 2.9, 0.0, 0.0, '-mass', 0.2996941896024464, 0.2996941896024464, 0.2996941896024464, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 2.9, 4.05, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 2.9, 4.05, 0.0, '-mass', 0.6743119266055045, 0.6743119266055045, 0.6743119266055045, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 2.9, 8.1, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 2.9, 8.1, 0.0, '-mass', 0.5137614678899083, 0.5137614678899083, 0.5137614678899083, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 2.9, 12.15, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 2.9, 12.15, 0.0, '-mass', 0.5137614678899083, 0.5137614678899083, 0.5137614678899083, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 2.9, 16.2, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 2.9, 16.2, 0.0, '-mass', 0.4495412844036697, 0.4495412844036697, 0.4495412844036697, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3
    # Fixed node
    ops.node(3, 7.9, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 7.9, 0.0, 0.0, '-mass', 0.5137614678899083, 0.5137614678899083, 0.5137614678899083, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 7.9, 4.05, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 7.9, 4.05, 0.0, '-mass', 0.749235474006116, 0.749235474006116, 0.749235474006116, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 7.9, 8.1, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 7.9, 8.1, 0.0, '-mass', 0.749235474006116, 0.749235474006116, 0.749235474006116, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 7.9, 12.15, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 7.9, 12.15, 0.0, '-mass', 0.749235474006116, 0.749235474006116, 0.749235474006116, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 19
    # Fixed node
    ops.node(19, 7.9, 16.2, 0.0)
    ops.fix(19, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70019, 7.9, 16.2, 0.0, '-mass', 0.5993883792048929, 0.5993883792048929, 0.5993883792048929, 0.0, 0.0, 0.0)
    ops.equalDOF(19, 70019, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4
    # Fixed node
    ops.node(4, 12.9, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 12.9, 0.0, 0.0, '-mass', 0.32110091743119257, 0.32110091743119257, 0.32110091743119257, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 12.9, 4.05, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 12.9, 4.05, 0.0, '-mass', 0.5137614678899083, 0.5137614678899083, 0.5137614678899083, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 12.9, 8.1, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 12.9, 8.1, 0.0, '-mass', 0.5137614678899083, 0.5137614678899083, 0.5137614678899083, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 12.9, 12.15, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 12.9, 12.15, 0.0, '-mass', 0.5137614678899083, 0.5137614678899083, 0.5137614678899083, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 20
    # Fixed node
    ops.node(20, 12.9, 16.2, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 12.9, 16.2, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)
