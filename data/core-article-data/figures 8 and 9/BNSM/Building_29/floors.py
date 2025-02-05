import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.5)
    ops.node(11002, 2.9, 0.0, 3.5)
    ops.node(11003, 7.9, 0.0, 3.5)
    ops.node(11004, 12.9, 0.0, 3.5)
    ops.node(11005, 0.0, 4.05, 3.5)
    ops.node(11006, 2.9, 4.05, 3.5)
    ops.node(11007, 7.9, 4.05, 3.5)
    ops.node(11008, 12.9, 4.05, 3.5)
    ops.node(11009, 0.0, 8.1, 3.5)
    ops.node(11010, 2.9, 8.1, 3.5)
    ops.node(11011, 7.9, 8.1, 3.5)
    ops.node(11012, 12.9, 8.1, 3.5)
    ops.node(11013, 0.0, 12.15, 3.5)
    ops.node(11014, 2.9, 12.15, 3.5)
    ops.node(11015, 7.9, 12.15, 3.5)
    ops.node(11016, 12.9, 12.15, 3.5)
    ops.node(11017, 0.0, 16.2, 3.5)
    ops.node(11018, 2.9, 16.2, 3.5)
    ops.node(11019, 7.9, 16.2, 3.5)
    ops.node(11020, 12.9, 16.2, 3.5)
    # Retained floor node
    ops.node(91000, 6.51432488, 8.22267178, 3.5)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.4)
    ops.node(12002, 2.9, 0.0, 6.4)
    ops.node(12003, 7.9, 0.0, 6.4)
    ops.node(12004, 12.9, 0.0, 6.4)
    ops.node(12005, 0.0, 4.05, 6.4)
    ops.node(12006, 2.9, 4.05, 6.4)
    ops.node(12007, 7.9, 4.05, 6.4)
    ops.node(12008, 12.9, 4.05, 6.4)
    ops.node(12009, 0.0, 8.1, 6.4)
    ops.node(12010, 2.9, 8.1, 6.4)
    ops.node(12011, 7.9, 8.1, 6.4)
    ops.node(12012, 12.9, 8.1, 6.4)
    ops.node(12013, 0.0, 12.15, 6.4)
    ops.node(12014, 2.9, 12.15, 6.4)
    ops.node(12015, 7.9, 12.15, 6.4)
    ops.node(12016, 12.9, 12.15, 6.4)
    ops.node(12017, 0.0, 16.2, 6.4)
    ops.node(12018, 2.9, 16.2, 6.4)
    ops.node(12019, 7.9, 16.2, 6.4)
    ops.node(12020, 12.9, 16.2, 6.4)
    # Retained floor node
    ops.node(92000, 6.51354126, 8.21929188, 6.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.3)
    ops.node(13002, 2.9, 0.0, 9.3)
    ops.node(13003, 7.9, 0.0, 9.3)
    ops.node(13004, 12.9, 0.0, 9.3)
    ops.node(13005, 0.0, 4.05, 9.3)
    ops.node(13006, 2.9, 4.05, 9.3)
    ops.node(13007, 7.9, 4.05, 9.3)
    ops.node(13008, 12.9, 4.05, 9.3)
    ops.node(13009, 0.0, 8.1, 9.3)
    ops.node(13010, 2.9, 8.1, 9.3)
    ops.node(13011, 7.9, 8.1, 9.3)
    ops.node(13012, 12.9, 8.1, 9.3)
    ops.node(13013, 0.0, 12.15, 9.3)
    ops.node(13014, 2.9, 12.15, 9.3)
    ops.node(13015, 7.9, 12.15, 9.3)
    ops.node(13016, 12.9, 12.15, 9.3)
    ops.node(13017, 0.0, 16.2, 9.3)
    ops.node(13018, 2.9, 16.2, 9.3)
    ops.node(13019, 7.9, 16.2, 9.3)
    ops.node(13020, 12.9, 16.2, 9.3)
    # Retained floor node
    ops.node(93000, 6.49501585, 8.2163063, 9.3)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.2)
    ops.node(14002, 2.9, 0.0, 12.2)
    ops.node(14003, 7.9, 0.0, 12.2)
    ops.node(14004, 12.9, 0.0, 12.2)
    ops.node(14005, 0.0, 4.05, 12.2)
    ops.node(14006, 2.9, 4.05, 12.2)
    ops.node(14007, 7.9, 4.05, 12.2)
    ops.node(14008, 12.9, 4.05, 12.2)
    ops.node(14009, 0.0, 8.1, 12.2)
    ops.node(14010, 2.9, 8.1, 12.2)
    ops.node(14011, 7.9, 8.1, 12.2)
    ops.node(14012, 12.9, 8.1, 12.2)
    ops.node(14013, 0.0, 12.15, 12.2)
    ops.node(14014, 2.9, 12.15, 12.2)
    ops.node(14015, 7.9, 12.15, 12.2)
    ops.node(14016, 12.9, 12.15, 12.2)
    ops.node(14017, 0.0, 16.2, 12.2)
    ops.node(14018, 2.9, 16.2, 12.2)
    ops.node(14019, 7.9, 16.2, 12.2)
    ops.node(14020, 12.9, 16.2, 12.2)
    # Retained floor node
    ops.node(94000, 6.5379261, 8.23798462, 12.2)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
