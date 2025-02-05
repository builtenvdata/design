import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.0)
    ops.node(11002, 6.7, 0.0, 3.0)
    ops.node(11003, 9.55, 0.0, 3.0)
    ops.node(11004, 16.25, 0.0, 3.0)
    ops.node(11005, 0.0, 3.95, 3.0)
    ops.node(11006, 6.7, 3.95, 3.0)
    ops.node(11007, 9.55, 3.95, 3.0)
    ops.node(11008, 16.25, 3.95, 3.0)
    ops.node(11009, 0.0, 7.9, 3.0)
    ops.node(11010, 6.7, 7.9, 3.0)
    ops.node(11011, 9.55, 7.9, 3.0)
    ops.node(11012, 16.25, 7.9, 3.0)
    # Retained floor node
    ops.node(91000, 8.125, 4.04996355, 3.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.0)
    ops.node(12002, 6.7, 0.0, 6.0)
    ops.node(12003, 9.55, 0.0, 6.0)
    ops.node(12004, 16.25, 0.0, 6.0)
    ops.node(12005, 0.0, 3.95, 6.0)
    ops.node(12006, 6.7, 3.95, 6.0)
    ops.node(12007, 9.55, 3.95, 6.0)
    ops.node(12008, 16.25, 3.95, 6.0)
    ops.node(12009, 0.0, 7.9, 6.0)
    ops.node(12010, 6.7, 7.9, 6.0)
    ops.node(12011, 9.55, 7.9, 6.0)
    ops.node(12012, 16.25, 7.9, 6.0)
    # Retained floor node
    ops.node(92000, 8.125, 4.04576737, 6.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.0)
    ops.node(13002, 6.7, 0.0, 9.0)
    ops.node(13003, 9.55, 0.0, 9.0)
    ops.node(13004, 16.25, 0.0, 9.0)
    ops.node(13005, 0.0, 3.95, 9.0)
    ops.node(13006, 6.7, 3.95, 9.0)
    ops.node(13007, 9.55, 3.95, 9.0)
    ops.node(13008, 16.25, 3.95, 9.0)
    ops.node(13009, 0.0, 7.9, 9.0)
    ops.node(13010, 6.7, 7.9, 9.0)
    ops.node(13011, 9.55, 7.9, 9.0)
    ops.node(13012, 16.25, 7.9, 9.0)
    # Retained floor node
    ops.node(93000, 8.125, 4.04244787, 9.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.0)
    ops.node(14002, 6.7, 0.0, 12.0)
    ops.node(14003, 9.55, 0.0, 12.0)
    ops.node(14004, 16.25, 0.0, 12.0)
    ops.node(14005, 0.0, 3.95, 12.0)
    ops.node(14006, 6.7, 3.95, 12.0)
    ops.node(14007, 9.55, 3.95, 12.0)
    ops.node(14008, 16.25, 3.95, 12.0)
    ops.node(14009, 0.0, 7.9, 12.0)
    ops.node(14010, 6.7, 7.9, 12.0)
    ops.node(14011, 9.55, 7.9, 12.0)
    ops.node(14012, 16.25, 7.9, 12.0)
    # Retained floor node
    ops.node(94000, 8.125, 4.07981795, 12.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
