import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.3)
    ops.node(11002, 5.45, 0.0, 2.3)
    ops.node(11003, 8.35, 0.0, 2.3)
    ops.node(11004, 13.8, 0.0, 2.3)
    ops.node(11005, 0.0, 4.45, 2.3)
    ops.node(11006, 5.45, 4.45, 2.3)
    ops.node(11007, 8.35, 4.45, 2.3)
    ops.node(11008, 13.8, 4.45, 2.3)
    ops.node(11009, 0.0, 8.9, 2.3)
    ops.node(11010, 5.45, 8.9, 2.3)
    ops.node(11011, 8.35, 8.9, 2.3)
    ops.node(11012, 13.8, 8.9, 2.3)
    ops.node(11013, 0.0, 13.35, 2.3)
    ops.node(11014, 5.45, 13.35, 2.3)
    ops.node(11015, 8.35, 13.35, 2.3)
    ops.node(11016, 13.8, 13.35, 2.3)
    # Retained floor node
    ops.node(91000, 6.9, 6.71629763, 2.3)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 4.6)
    ops.node(12002, 5.45, 0.0, 4.6)
    ops.node(12003, 8.35, 0.0, 4.6)
    ops.node(12004, 13.8, 0.0, 4.6)
    ops.node(12005, 0.0, 4.45, 4.6)
    ops.node(12006, 5.45, 4.45, 4.6)
    ops.node(12007, 8.35, 4.45, 4.6)
    ops.node(12008, 13.8, 4.45, 4.6)
    ops.node(12009, 0.0, 8.9, 4.6)
    ops.node(12010, 5.45, 8.9, 4.6)
    ops.node(12011, 8.35, 8.9, 4.6)
    ops.node(12012, 13.8, 8.9, 4.6)
    ops.node(12013, 0.0, 13.35, 4.6)
    ops.node(12014, 5.45, 13.35, 4.6)
    ops.node(12015, 8.35, 13.35, 4.6)
    ops.node(12016, 13.8, 13.35, 4.6)
    # Retained floor node
    ops.node(92000, 6.9, 6.71466734, 4.6)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 6.9)
    ops.node(13002, 5.45, 0.0, 6.9)
    ops.node(13003, 8.35, 0.0, 6.9)
    ops.node(13004, 13.8, 0.0, 6.9)
    ops.node(13005, 0.0, 4.45, 6.9)
    ops.node(13006, 5.45, 4.45, 6.9)
    ops.node(13007, 8.35, 4.45, 6.9)
    ops.node(13008, 13.8, 4.45, 6.9)
    ops.node(13009, 0.0, 8.9, 6.9)
    ops.node(13010, 5.45, 8.9, 6.9)
    ops.node(13011, 8.35, 8.9, 6.9)
    ops.node(13012, 13.8, 8.9, 6.9)
    ops.node(13013, 0.0, 13.35, 6.9)
    ops.node(13014, 5.45, 13.35, 6.9)
    ops.node(13015, 8.35, 13.35, 6.9)
    ops.node(13016, 13.8, 13.35, 6.9)
    # Retained floor node
    ops.node(93000, 6.9, 6.71299944, 6.9)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 9.2)
    ops.node(14002, 5.45, 0.0, 9.2)
    ops.node(14003, 8.35, 0.0, 9.2)
    ops.node(14004, 13.8, 0.0, 9.2)
    ops.node(14005, 0.0, 4.45, 9.2)
    ops.node(14006, 5.45, 4.45, 9.2)
    ops.node(14007, 8.35, 4.45, 9.2)
    ops.node(14008, 13.8, 4.45, 9.2)
    ops.node(14009, 0.0, 8.9, 9.2)
    ops.node(14010, 5.45, 8.9, 9.2)
    ops.node(14011, 8.35, 8.9, 9.2)
    ops.node(14012, 13.8, 8.9, 9.2)
    ops.node(14013, 0.0, 13.35, 9.2)
    ops.node(14014, 5.45, 13.35, 9.2)
    ops.node(14015, 8.35, 13.35, 9.2)
    ops.node(14016, 13.8, 13.35, 9.2)
    # Retained floor node
    ops.node(94000, 6.9, 6.81538259, 9.2)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
