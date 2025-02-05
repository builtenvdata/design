import openseespy.opensees as ops


def add_foundations() -> None:
    """Add foundation components to ops domain (nodes and constraints).
    """
    # Foundation or support under the column 1
    # Fixed node
    ops.node(1, 0.0, 0.0, 0.0)
    ops.fix(1, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.41957186544342495, 0.41957186544342495, 0.41957186544342495, 0.0, 0.0, 0.0)
    ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 5
    # Fixed node
    ops.node(5, 0.0, 4.4, 0.0)
    ops.fix(5, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70005, 0.0, 4.4, 0.0, '-mass', 0.6935779816513762, 0.6935779816513762, 0.6935779816513762, 0.0, 0.0, 0.0)
    ops.equalDOF(5, 70005, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 9
    # Fixed node
    ops.node(9, 0.0, 8.8, 0.0)
    ops.fix(9, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70009, 0.0, 8.8, 0.0, '-mass', 0.6935779816513762, 0.6935779816513762, 0.6935779816513762, 0.0, 0.0, 0.0)
    ops.equalDOF(9, 70009, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 13
    # Fixed node
    ops.node(13, 0.0, 13.2, 0.0)
    ops.fix(13, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70013, 0.0, 13.2, 0.0, '-mass', 0.41957186544342495, 0.41957186544342495, 0.41957186544342495, 0.0, 0.0, 0.0)
    ops.equalDOF(13, 70013, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4041
    # Fixed node
    ops.node(2, 5.05, 0.0, 0.0)
    ops.fix(2, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70002, 5.05, 0.0, 0.0, '-mass', 0.27400611620795107, 0.27400611620795107, 0.27400611620795107, 0.0, 0.0, 0.0)
    ops.equalDOF(2, 70002, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 6
    # Fixed node
    ops.node(6, 5.05, 4.4, 0.0)
    ops.fix(6, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70006, 5.05, 4.4, 0.0, '-mass', 0.8562691131498469, 0.8562691131498469, 0.8562691131498469, 0.0, 0.0, 0.0)
    ops.equalDOF(6, 70006, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 10
    # Fixed node
    ops.node(10, 5.05, 8.8, 0.0)
    ops.fix(10, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70010, 5.05, 8.8, 0.0, '-mass', 0.8562691131498469, 0.8562691131498469, 0.8562691131498469, 0.0, 0.0, 0.0)
    ops.equalDOF(10, 70010, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 14
    # Fixed node
    ops.node(14, 5.05, 13.2, 0.0)
    ops.fix(14, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70014, 5.05, 13.2, 0.0, '-mass', 0.5480122324159021, 0.5480122324159021, 0.5480122324159021, 0.0, 0.0, 0.0)
    ops.equalDOF(14, 70014, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4043
    # Fixed node
    ops.node(3, 7.95, 0.0, 0.0)
    ops.fix(3, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70003, 7.95, 0.0, 0.0, '-mass', 0.27400611620795107, 0.27400611620795107, 0.27400611620795107, 0.0, 0.0, 0.0)
    ops.equalDOF(3, 70003, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 7
    # Fixed node
    ops.node(7, 7.95, 4.4, 0.0)
    ops.fix(7, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70007, 7.95, 4.4, 0.0, '-mass', 0.8562691131498469, 0.8562691131498469, 0.8562691131498469, 0.0, 0.0, 0.0)
    ops.equalDOF(7, 70007, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 11
    # Fixed node
    ops.node(11, 7.95, 8.8, 0.0)
    ops.fix(11, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70011, 7.95, 8.8, 0.0, '-mass', 0.8562691131498469, 0.8562691131498469, 0.8562691131498469, 0.0, 0.0, 0.0)
    ops.equalDOF(11, 70011, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 15
    # Fixed node
    ops.node(15, 7.95, 13.2, 0.0)
    ops.fix(15, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70015, 7.95, 13.2, 0.0, '-mass', 0.5480122324159021, 0.5480122324159021, 0.5480122324159021, 0.0, 0.0, 0.0)
    ops.equalDOF(15, 70015, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 4
    # Fixed node
    ops.node(4, 13.0, 0.0, 0.0)
    ops.fix(4, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70004, 13.0, 0.0, 0.0, '-mass', 0.41957186544342495, 0.41957186544342495, 0.41957186544342495, 0.0, 0.0, 0.0)
    ops.equalDOF(4, 70004, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 8
    # Fixed node
    ops.node(8, 13.0, 4.4, 0.0)
    ops.fix(8, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70008, 13.0, 4.4, 0.0, '-mass', 0.6935779816513762, 0.6935779816513762, 0.6935779816513762, 0.0, 0.0, 0.0)
    ops.equalDOF(8, 70008, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 12
    # Fixed node
    ops.node(12, 13.0, 8.8, 0.0)
    ops.fix(12, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70012, 13.0, 8.8, 0.0, '-mass', 0.6935779816513762, 0.6935779816513762, 0.6935779816513762, 0.0, 0.0, 0.0)
    ops.equalDOF(12, 70012, 1, 2, 3, 4, 5, 6)

    # Foundation or support under the column 16
    # Fixed node
    ops.node(16, 13.0, 13.2, 0.0)
    ops.fix(16, 1, 1, 1, 1, 1, 1)
    # Foundation node
    ops.node(70016, 13.0, 13.2, 0.0, '-mass', 0.41957186544342495, 0.41957186544342495, 0.41957186544342495, 0.0, 0.0, 0.0)
    ops.equalDOF(16, 70016, 1, 2, 3, 4, 5, 6)
