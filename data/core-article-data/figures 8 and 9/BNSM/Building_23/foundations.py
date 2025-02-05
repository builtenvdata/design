import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 4074
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.14143730886850153, 0.14143730886850153, 0.14143730886850153, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 5
    # Fixed node
    ops.node(5, 0.0, 4.25, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 0.0, 4.25, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 0.0, 8.5, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 0.0, 8.5, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 0.0, 12.75, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 0.0, 12.75, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 0.0, 17.0, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 0.0, 17.0, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 21
    # Fixed node
    ops.node(21, 0.0, 21.25, 0.0)
    ops.fix(21, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70021, 0.0, 21.25, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(21, 70021, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 25
    # Fixed node
    ops.node(25, 0.0, 25.5, 0.0)
    ops.fix(25, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70025, 0.0, 25.5, 0.0, '-mass', 0.28287461773700306, 0.28287461773700306, 0.28287461773700306, 0.0, 0.0, 0.0)
    ops.equalDOF(25, 70025, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4076
    # Fixed node
    ops.node(2, 2.95, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 2.95, 0.0, 0.0, '-mass', 0.27721712538226295, 0.27721712538226295, 0.27721712538226295, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 2.95, 4.25, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 2.95, 4.25, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 2.95, 8.5, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 2.95, 8.5, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 2.95, 12.75, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 2.95, 12.75, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 2.95, 17.0, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 2.95, 17.0, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 22
    # Fixed node
    ops.node(22, 2.95, 21.25, 0.0)
    ops.fix(22, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70022, 2.95, 21.25, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(22, 70022, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 26
    # Fixed node
    ops.node(26, 2.95, 25.5, 0.0)
    ops.fix(26, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70026, 2.95, 25.5, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(26, 70026, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3
    # Fixed node
    ops.node(3, 8.3, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 8.3, 0.0, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 8.3, 4.25, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 8.3, 4.25, 0.0, '-mass', 0.7241590214067279, 0.7241590214067279, 0.7241590214067279, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 8.3, 8.5, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 8.3, 8.5, 0.0, '-mass', 0.7241590214067279, 0.7241590214067279, 0.7241590214067279, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 8.3, 12.75, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 8.3, 12.75, 0.0, '-mass', 0.7241590214067279, 0.7241590214067279, 0.7241590214067279, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 19
    # Fixed node
    ops.node(19, 8.3, 17.0, 0.0)
    ops.fix(19, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70019, 8.3, 17.0, 0.0, '-mass', 0.7241590214067279, 0.7241590214067279, 0.7241590214067279, 0.0, 0.0, 0.0)
    ops.equalDOF(19, 70019, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 23
    # Fixed node
    ops.node(23, 8.3, 21.25, 0.0)
    ops.fix(23, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70023, 8.3, 21.25, 0.0, '-mass', 0.7241590214067279, 0.7241590214067279, 0.7241590214067279, 0.0, 0.0, 0.0)
    ops.equalDOF(23, 70023, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 27
    # Fixed node
    ops.node(27, 8.3, 25.5, 0.0)
    ops.fix(27, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70027, 8.3, 25.5, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(27, 70027, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4
    # Fixed node
    ops.node(4, 13.65, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 13.65, 0.0, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 13.65, 4.25, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 13.65, 4.25, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 13.65, 8.5, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 13.65, 8.5, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 13.65, 12.75, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 13.65, 12.75, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 20
    # Fixed node
    ops.node(20, 13.65, 17.0, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 13.65, 17.0, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 24
    # Fixed node
    ops.node(24, 13.65, 21.25, 0.0)
    ops.fix(24, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70024, 13.65, 21.25, 0.0, '-mass', 0.5544342507645259, 0.5544342507645259, 0.5544342507645259, 0.0, 0.0, 0.0)
    ops.equalDOF(24, 70024, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 28
    # Fixed node
    ops.node(28, 13.65, 25.5, 0.0)
    ops.fix(28, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70028, 13.65, 25.5, 0.0, '-mass', 0.4073394495412844, 0.4073394495412844, 0.4073394495412844, 0.0, 0.0, 0.0)
    ops.equalDOF(28, 70028, 1, 2, 3, 4, 5, 6)
