import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.55)
    ops.node(11002, 5.8, 0.0, 3.55)
    ops.node(11003, 8.65, 0.0, 3.55)
    ops.node(11004, 14.45, 0.0, 3.55)
    ops.node(11005, 0.0, 4.15, 3.55)
    ops.node(11006, 5.8, 4.15, 3.55)
    ops.node(11007, 8.65, 4.15, 3.55)
    ops.node(11008, 14.45, 4.15, 3.55)
    ops.node(11009, 0.0, 8.3, 3.55)
    ops.node(11010, 5.8, 8.3, 3.55)
    ops.node(11011, 8.65, 8.3, 3.55)
    ops.node(11012, 14.45, 8.3, 3.55)
    # Retained floor node
    ops.node(91000, 7.225, 4.25431446, 3.55)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.1)
    ops.node(12002, 5.8, 0.0, 6.1)
    ops.node(12003, 8.65, 0.0, 6.1)
    ops.node(12004, 14.45, 0.0, 6.1)
    ops.node(12005, 0.0, 4.15, 6.1)
    ops.node(12006, 5.8, 4.15, 6.1)
    ops.node(12007, 8.65, 4.15, 6.1)
    ops.node(12008, 14.45, 4.15, 6.1)
    ops.node(12009, 0.0, 8.3, 6.1)
    ops.node(12010, 5.8, 8.3, 6.1)
    ops.node(12011, 8.65, 8.3, 6.1)
    ops.node(12012, 14.45, 8.3, 6.1)
    # Retained floor node
    ops.node(92000, 7.225, 4.25522231, 6.1)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.65)
    ops.node(13002, 5.8, 0.0, 8.65)
    ops.node(13003, 8.65, 0.0, 8.65)
    ops.node(13004, 14.45, 0.0, 8.65)
    ops.node(13005, 0.0, 4.15, 8.65)
    ops.node(13006, 5.8, 4.15, 8.65)
    ops.node(13007, 8.65, 4.15, 8.65)
    ops.node(13008, 14.45, 4.15, 8.65)
    ops.node(13009, 0.0, 8.3, 8.65)
    ops.node(13010, 5.8, 8.3, 8.65)
    ops.node(13011, 8.65, 8.3, 8.65)
    ops.node(13012, 14.45, 8.3, 8.65)
    # Retained floor node
    ops.node(93000, 7.225, 4.25748454, 8.65)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.2)
    ops.node(14002, 5.8, 0.0, 11.2)
    ops.node(14003, 8.65, 0.0, 11.2)
    ops.node(14004, 14.45, 0.0, 11.2)
    ops.node(14005, 0.0, 4.15, 11.2)
    ops.node(14006, 5.8, 4.15, 11.2)
    ops.node(14007, 8.65, 4.15, 11.2)
    ops.node(14008, 14.45, 4.15, 11.2)
    ops.node(14009, 0.0, 8.3, 11.2)
    ops.node(14010, 5.8, 8.3, 11.2)
    ops.node(14011, 8.65, 8.3, 11.2)
    ops.node(14012, 14.45, 8.3, 11.2)
    # Retained floor node
    ops.node(94000, 7.225, 4.30766726, 11.2)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
