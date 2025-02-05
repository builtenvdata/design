import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 1
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.3247706422018349, 0.3247706422018349, 0.3247706422018349, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 0.0, 4.8, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 0.0, 4.8, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 0.0, 9.6, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 0.0, 9.6, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 25
    # Fixed node
    ops.node(25, 0.0, 14.4, 0.0)
    ops.fix(25, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70025, 0.0, 14.4, 0.0, '-mass', 0.3247706422018349, 0.3247706422018349, 0.3247706422018349, 0.0, 0.0, 0.0)
    ops.equalDOF(25, 70025, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 2
    # Fixed node
    ops.node(2, 3.85, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 3.85, 0.0, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 3.85, 4.8, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 3.85, 4.8, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 3.85, 9.6, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 3.85, 9.6, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 26
    # Fixed node
    ops.node(26, 3.85, 14.4, 0.0)
    ops.fix(26, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70026, 3.85, 14.4, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(26, 70026, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3
    # Fixed node
    ops.node(3, 7.7, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 7.7, 0.0, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 7.7, 4.8, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 7.7, 4.8, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 19
    # Fixed node
    ops.node(19, 7.7, 9.6, 0.0)
    ops.fix(19, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70019, 7.7, 9.6, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(19, 70019, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 27
    # Fixed node
    ops.node(27, 7.7, 14.4, 0.0)
    ops.fix(27, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70027, 7.7, 14.4, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(27, 70027, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4085
    # Fixed node
    ops.node(4, 11.55, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 11.55, 0.0, 0.0, '-mass', 0.2210244648318042, 0.2210244648318042, 0.2210244648318042, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 11.55, 4.8, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 11.55, 4.8, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 20
    # Fixed node
    ops.node(20, 11.55, 9.6, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 11.55, 9.6, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 28
    # Fixed node
    ops.node(28, 11.55, 14.4, 0.0)
    ops.fix(28, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70028, 11.55, 14.4, 0.0, '-mass', 0.4420489296636084, 0.4420489296636084, 0.4420489296636084, 0.0, 0.0, 0.0)
    ops.equalDOF(28, 70028, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4087
    # Fixed node
    ops.node(5, 14.6, 0.0, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 14.6, 0.0, 0.0, '-mass', 0.2210244648318042, 0.2210244648318042, 0.2210244648318042, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 14.6, 4.8, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 14.6, 4.8, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 21
    # Fixed node
    ops.node(21, 14.6, 9.6, 0.0)
    ops.fix(21, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70021, 14.6, 9.6, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(21, 70021, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 29
    # Fixed node
    ops.node(29, 14.6, 14.4, 0.0)
    ops.fix(29, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70029, 14.6, 14.4, 0.0, '-mass', 0.4420489296636084, 0.4420489296636084, 0.4420489296636084, 0.0, 0.0, 0.0)
    ops.equalDOF(29, 70029, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 18.45, 0.0, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 18.45, 0.0, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 18.45, 4.8, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 18.45, 4.8, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 22
    # Fixed node
    ops.node(22, 18.45, 9.6, 0.0)
    ops.fix(22, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70022, 18.45, 9.6, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(22, 70022, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 30
    # Fixed node
    ops.node(30, 18.45, 14.4, 0.0)
    ops.fix(30, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70030, 18.45, 14.4, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(30, 70030, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 22.3, 0.0, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 22.3, 0.0, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 22.3, 4.8, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 22.3, 4.8, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 23
    # Fixed node
    ops.node(23, 22.3, 9.6, 0.0)
    ops.fix(23, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70023, 22.3, 9.6, 0.0, '-mass', 0.7307339449541285, 0.7307339449541285, 0.7307339449541285, 0.0, 0.0, 0.0)
    ops.equalDOF(23, 70023, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 31
    # Fixed node
    ops.node(31, 22.3, 14.4, 0.0)
    ops.fix(31, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70031, 22.3, 14.4, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(31, 70031, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 26.15, 0.0, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 26.15, 0.0, 0.0, '-mass', 0.3247706422018349, 0.3247706422018349, 0.3247706422018349, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 26.15, 4.8, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 26.15, 4.8, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 24
    # Fixed node
    ops.node(24, 26.15, 9.6, 0.0)
    ops.fix(24, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70024, 26.15, 9.6, 0.0, '-mass', 0.5773700305810399, 0.5773700305810399, 0.5773700305810399, 0.0, 0.0, 0.0)
    ops.equalDOF(24, 70024, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 32
    # Fixed node
    ops.node(32, 26.15, 14.4, 0.0)
    ops.fix(32, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70032, 26.15, 14.4, 0.0, '-mass', 0.3247706422018349, 0.3247706422018349, 0.3247706422018349, 0.0, 0.0, 0.0)
    ops.equalDOF(32, 70032, 1, 2, 3, 4, 5, 6)
