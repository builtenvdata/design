import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 4052
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.10321100917431195, 0.10321100917431195, 0.10321100917431195, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 5
    # Fixed node
    ops.node(5, 0.0, 5.7, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 0.0, 5.7, 0.0, '-mass', 0.33027522935779824, 0.33027522935779824, 0.33027522935779824, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 0.0, 11.4, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 0.0, 11.4, 0.0, '-mass', 0.33027522935779824, 0.33027522935779824, 0.33027522935779824, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 0.0, 17.1, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 0.0, 17.1, 0.0, '-mass', 0.33027522935779824, 0.33027522935779824, 0.33027522935779824, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 17
    # Fixed node
    ops.node(17, 0.0, 22.8, 0.0)
    ops.fix(17, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70017, 0.0, 22.8, 0.0, '-mass', 0.2064220183486239, 0.2064220183486239, 0.2064220183486239, 0.0, 0.0, 0.0)
    ops.equalDOF(17, 70017, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4054
    # Fixed node
    ops.node(2, 2.9, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 2.9, 0.0, 0.0, '-mass', 0.19816513761467888, 0.19816513761467888, 0.19816513761467888, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 2.9, 5.7, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 2.9, 5.7, 0.0, '-mass', 0.5944954128440367, 0.5944954128440367, 0.5944954128440367, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 2.9, 11.4, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 2.9, 11.4, 0.0, '-mass', 0.544954128440367, 0.544954128440367, 0.544954128440367, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 2.9, 17.1, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 2.9, 17.1, 0.0, '-mass', 0.544954128440367, 0.544954128440367, 0.544954128440367, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 18
    # Fixed node
    ops.node(18, 2.9, 22.8, 0.0)
    ops.fix(18, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70018, 2.9, 22.8, 0.0, '-mass', 0.39633027522935776, 0.39633027522935776, 0.39633027522935776, 0.0, 0.0, 0.0)
    ops.equalDOF(18, 70018, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 3
    # Fixed node
    ops.node(3, 6.6, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 6.6, 0.0, 0.0, '-mass', 0.44587155963302755, 0.44587155963302755, 0.44587155963302755, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 6.6, 5.7, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 6.6, 5.7, 0.0, '-mass', 0.6440366972477064, 0.6440366972477064, 0.6440366972477064, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 6.6, 11.4, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 6.6, 11.4, 0.0, '-mass', 0.6440366972477064, 0.6440366972477064, 0.6440366972477064, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 6.6, 17.1, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 6.6, 17.1, 0.0, '-mass', 0.6440366972477064, 0.6440366972477064, 0.6440366972477064, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 19
    # Fixed node
    ops.node(19, 6.6, 22.8, 0.0)
    ops.fix(19, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70019, 6.6, 22.8, 0.0, '-mass', 0.5201834862385322, 0.5201834862385322, 0.5201834862385322, 0.0, 0.0, 0.0)
    ops.equalDOF(19, 70019, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4
    # Fixed node
    ops.node(4, 10.3, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 10.3, 0.0, 0.0, '-mass', 0.24770642201834858, 0.24770642201834858, 0.24770642201834858, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 10.3, 5.7, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 10.3, 5.7, 0.0, '-mass', 0.4128440366972478, 0.4128440366972478, 0.4128440366972478, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 10.3, 11.4, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 10.3, 11.4, 0.0, '-mass', 0.4128440366972478, 0.4128440366972478, 0.4128440366972478, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 10.3, 17.1, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 10.3, 17.1, 0.0, '-mass', 0.4128440366972478, 0.4128440366972478, 0.4128440366972478, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 20
    # Fixed node
    ops.node(20, 10.3, 22.8, 0.0)
    ops.fix(20, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70020, 10.3, 22.8, 0.0, '-mass', 0.24770642201834858, 0.24770642201834858, 0.24770642201834858, 0.0, 0.0, 0.0)
    ops.equalDOF(20, 70020, 1, 2, 3, 4, 5, 6)
