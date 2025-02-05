import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 1
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.39067278287461765, 0.39067278287461765, 0.39067278287461765, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 0.0, 4.75, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 0.0, 4.75, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 0.0, 9.5, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 0.0, 9.5, 0.0, '-mass', 0.39067278287461765, 0.39067278287461765, 0.39067278287461765, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 2
    # Fixed node
    ops.node(2, 5.8, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 5.8, 0.0, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 5.8, 4.75, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 5.8, 4.75, 0.0, '-mass', 1.5626911314984706, 1.5626911314984706, 1.5626911314984706, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 5.8, 9.5, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 5.8, 9.5, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3
    # Fixed node
    ops.node(3, 11.6, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 11.6, 0.0, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 11.6, 4.75, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 11.6, 4.75, 0.0, '-mass', 1.5626911314984706, 1.5626911314984706, 1.5626911314984706, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 19
    # Fixed node
    ops.node(19, 11.6, 9.5, 0.0)
    ops.fix(19, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70019, 11.6, 9.5, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(19, 70019, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4062
    # Fixed node
    ops.node(4, 17.4, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 17.4, 0.0, 0.0, '-mass', 0.39067278287461765, 0.39067278287461765, 0.39067278287461765, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 17.4, 4.75, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 17.4, 4.75, 0.0, '-mass', 1.0715596330275228, 1.0715596330275228, 1.0715596330275228, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 20
    # Fixed node
    ops.node(20, 17.4, 9.5, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 17.4, 9.5, 0.0, '-mass', 0.5357798165137614, 0.5357798165137614, 0.5357798165137614, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4064
    # Fixed node
    ops.node(5, 20.2, 0.0, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 20.2, 0.0, 0.0, '-mass', 0.39067278287461765, 0.39067278287461765, 0.39067278287461765, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 20.2, 4.75, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 20.2, 4.75, 0.0, '-mass', 1.0715596330275228, 1.0715596330275228, 1.0715596330275228, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 21
    # Fixed node
    ops.node(21, 20.2, 9.5, 0.0)
    ops.fix(21, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70021, 20.2, 9.5, 0.0, '-mass', 0.5357798165137614, 0.5357798165137614, 0.5357798165137614, 0.0, 0.0, 0.0)
    ops.equalDOF(21, 70021, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 26.0, 0.0, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 26.0, 0.0, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 26.0, 4.75, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 26.0, 4.75, 0.0, '-mass', 1.5626911314984706, 1.5626911314984706, 1.5626911314984706, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 22
    # Fixed node
    ops.node(22, 26.0, 9.5, 0.0)
    ops.fix(22, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70022, 26.0, 9.5, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(22, 70022, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 31.8, 0.0, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 31.8, 0.0, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 31.8, 4.75, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 31.8, 4.75, 0.0, '-mass', 1.5626911314984706, 1.5626911314984706, 1.5626911314984706, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 23
    # Fixed node
    ops.node(23, 31.8, 9.5, 0.0)
    ops.fix(23, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70023, 31.8, 9.5, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(23, 70023, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 37.6, 0.0, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 37.6, 0.0, 0.0, '-mass', 0.39067278287461765, 0.39067278287461765, 0.39067278287461765, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 37.6, 4.75, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 37.6, 4.75, 0.0, '-mass', 0.8594801223241589, 0.8594801223241589, 0.8594801223241589, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 24
    # Fixed node
    ops.node(24, 37.6, 9.5, 0.0)
    ops.fix(24, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70024, 37.6, 9.5, 0.0, '-mass', 0.39067278287461765, 0.39067278287461765, 0.39067278287461765, 0.0, 0.0, 0.0)
    ops.equalDOF(24, 70024, 1, 2, 3, 4, 5, 6)
