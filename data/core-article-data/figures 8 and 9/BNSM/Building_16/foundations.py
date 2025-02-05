import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 4063
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.12041284403669723, 0.12041284403669723, 0.12041284403669723, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 5
    # Fixed node
    ops.node(5, 0.0, 4.4, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 0.0, 4.4, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 0.0, 8.8, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 0.0, 8.8, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 0.0, 13.2, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 0.0, 13.2, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 0.0, 17.6, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 0.0, 17.6, 0.0, '-mass', 0.3853211009174312, 0.3853211009174312, 0.3853211009174312, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 21
    # Fixed node
    ops.node(21, 0.0, 22.0, 0.0)
    ops.fix(21, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70021, 0.0, 22.0, 0.0, '-mass', 0.24082568807339447, 0.24082568807339447, 0.24082568807339447, 0.0, 0.0, 0.0)
    ops.equalDOF(21, 70021, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4065
    # Fixed node
    ops.node(2, 3.1, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 3.1, 0.0, 0.0, '-mass', 0.3371559633027522, 0.3371559633027522, 0.3371559633027522, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 3.1, 4.4, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 3.1, 4.4, 0.0, '-mass', 0.8766055045871558, 0.8766055045871558, 0.8766055045871558, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 3.1, 8.8, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 3.1, 8.8, 0.0, '-mass', 0.8766055045871558, 0.8766055045871558, 0.8766055045871558, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 3.1, 13.2, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 3.1, 13.2, 0.0, '-mass', 0.8766055045871558, 0.8766055045871558, 0.8766055045871558, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 3.1, 17.6, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 3.1, 17.6, 0.0, '-mass', 0.8766055045871558, 0.8766055045871558, 0.8766055045871558, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 22
    # Fixed node
    ops.node(22, 3.1, 22.0, 0.0)
    ops.fix(22, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70022, 3.1, 22.0, 0.0, '-mass', 0.6068807339449541, 0.6068807339449541, 0.6068807339449541, 0.0, 0.0, 0.0)
    ops.equalDOF(22, 70022, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3
    # Fixed node
    ops.node(3, 7.35, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 7.35, 0.0, 0.0, '-mass', 0.741743119266055, 0.741743119266055, 0.741743119266055, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 7.35, 4.4, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 7.35, 4.4, 0.0, '-mass', 1.1559633027522938, 1.1559633027522938, 1.1559633027522938, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 7.35, 8.8, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 7.35, 8.8, 0.0, '-mass', 1.1559633027522938, 1.1559633027522938, 1.1559633027522938, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 7.35, 13.2, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 7.35, 13.2, 0.0, '-mass', 1.1559633027522938, 1.1559633027522938, 1.1559633027522938, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 19
    # Fixed node
    ops.node(19, 7.35, 17.6, 0.0)
    ops.fix(19, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70019, 7.35, 17.6, 0.0, '-mass', 1.1559633027522938, 1.1559633027522938, 1.1559633027522938, 0.0, 0.0, 0.0)
    ops.equalDOF(19, 70019, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 23
    # Fixed node
    ops.node(23, 7.35, 22.0, 0.0)
    ops.fix(23, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70023, 7.35, 22.0, 0.0, '-mass', 0.8477064220183487, 0.8477064220183487, 0.8477064220183487, 0.0, 0.0, 0.0)
    ops.equalDOF(23, 70023, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4
    # Fixed node
    ops.node(4, 11.6, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 11.6, 0.0, 0.0, '-mass', 0.4045871559633027, 0.4045871559633027, 0.4045871559633027, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 11.6, 4.4, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 11.6, 4.4, 0.0, '-mass', 0.6357798165137615, 0.6357798165137615, 0.6357798165137615, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 11.6, 8.8, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 11.6, 8.8, 0.0, '-mass', 0.6357798165137615, 0.6357798165137615, 0.6357798165137615, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 11.6, 13.2, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 11.6, 13.2, 0.0, '-mass', 0.6357798165137615, 0.6357798165137615, 0.6357798165137615, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 20
    # Fixed node
    ops.node(20, 11.6, 17.6, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 11.6, 17.6, 0.0, '-mass', 0.6357798165137615, 0.6357798165137615, 0.6357798165137615, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 24
    # Fixed node
    ops.node(24, 11.6, 22.0, 0.0)
    ops.fix(24, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70024, 11.6, 22.0, 0.0, '-mass', 0.4045871559633027, 0.4045871559633027, 0.4045871559633027, 0.0, 0.0, 0.0)
    ops.equalDOF(24, 70024, 1, 2, 3, 4, 5, 6)
