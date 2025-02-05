import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.8)
    ops.node(11002, 5.05, 0.0, 2.8)
    ops.node(11003, 7.95, 0.0, 2.8)
    ops.node(11004, 13.0, 0.0, 2.8)
    ops.node(11005, 0.0, 4.4, 2.8)
    ops.node(11006, 5.05, 4.4, 2.8)
    ops.node(11007, 7.95, 4.4, 2.8)
    ops.node(11008, 13.0, 4.4, 2.8)
    ops.node(11009, 0.0, 8.8, 2.8)
    ops.node(11010, 5.05, 8.8, 2.8)
    ops.node(11011, 7.95, 8.8, 2.8)
    ops.node(11012, 13.0, 8.8, 2.8)
    ops.node(11013, 0.0, 13.2, 2.8)
    ops.node(11014, 5.05, 13.2, 2.8)
    ops.node(11015, 7.95, 13.2, 2.8)
    ops.node(11016, 13.0, 13.2, 2.8)
    # Retained floor node
    ops.node(91000, 6.5, 6.72461735, 2.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.6)
    ops.node(12002, 5.05, 0.0, 5.6)
    ops.node(12003, 7.95, 0.0, 5.6)
    ops.node(12004, 13.0, 0.0, 5.6)
    ops.node(12005, 0.0, 4.4, 5.6)
    ops.node(12006, 5.05, 4.4, 5.6)
    ops.node(12007, 7.95, 4.4, 5.6)
    ops.node(12008, 13.0, 4.4, 5.6)
    ops.node(12009, 0.0, 8.8, 5.6)
    ops.node(12010, 5.05, 8.8, 5.6)
    ops.node(12011, 7.95, 8.8, 5.6)
    ops.node(12012, 13.0, 8.8, 5.6)
    ops.node(12013, 0.0, 13.2, 5.6)
    ops.node(12014, 5.05, 13.2, 5.6)
    ops.node(12015, 7.95, 13.2, 5.6)
    ops.node(12016, 13.0, 13.2, 5.6)
    # Retained floor node
    ops.node(92000, 6.5, 6.72299806, 5.6)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.4)
    ops.node(13002, 5.05, 0.0, 8.4)
    ops.node(13003, 7.95, 0.0, 8.4)
    ops.node(13004, 13.0, 0.0, 8.4)
    ops.node(13005, 0.0, 4.4, 8.4)
    ops.node(13006, 5.05, 4.4, 8.4)
    ops.node(13007, 7.95, 4.4, 8.4)
    ops.node(13008, 13.0, 4.4, 8.4)
    ops.node(13009, 0.0, 8.8, 8.4)
    ops.node(13010, 5.05, 8.8, 8.4)
    ops.node(13011, 7.95, 8.8, 8.4)
    ops.node(13012, 13.0, 8.8, 8.4)
    ops.node(13013, 0.0, 13.2, 8.4)
    ops.node(13014, 5.05, 13.2, 8.4)
    ops.node(13015, 7.95, 13.2, 8.4)
    ops.node(13016, 13.0, 13.2, 8.4)
    # Retained floor node
    ops.node(93000, 6.5, 6.72172913, 8.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.2)
    ops.node(14002, 5.05, 0.0, 11.2)
    ops.node(14003, 7.95, 0.0, 11.2)
    ops.node(14004, 13.0, 0.0, 11.2)
    ops.node(14005, 0.0, 4.4, 11.2)
    ops.node(14006, 5.05, 4.4, 11.2)
    ops.node(14007, 7.95, 4.4, 11.2)
    ops.node(14008, 13.0, 4.4, 11.2)
    ops.node(14009, 0.0, 8.8, 11.2)
    ops.node(14010, 5.05, 8.8, 11.2)
    ops.node(14011, 7.95, 8.8, 11.2)
    ops.node(14012, 13.0, 8.8, 11.2)
    ops.node(14013, 0.0, 13.2, 11.2)
    ops.node(14014, 5.05, 13.2, 11.2)
    ops.node(14015, 7.95, 13.2, 11.2)
    ops.node(14016, 13.0, 13.2, 11.2)
    # Retained floor node
    ops.node(94000, 6.5, 6.80348847, 11.2)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
