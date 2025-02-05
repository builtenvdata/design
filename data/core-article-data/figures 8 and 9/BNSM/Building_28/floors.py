import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.1)
    ops.node(11002, 4.25, 0.0, 3.1)
    ops.node(11003, 8.5, 0.0, 3.1)
    ops.node(11004, 11.35, 0.0, 3.1)
    ops.node(11005, 15.6, 0.0, 3.1)
    ops.node(11006, 19.85, 0.0, 3.1)
    ops.node(11007, 0.0, 5.5, 3.1)
    ops.node(11008, 4.25, 5.5, 3.1)
    ops.node(11009, 8.5, 5.5, 3.1)
    ops.node(11010, 11.35, 5.5, 3.1)
    ops.node(11011, 15.6, 5.5, 3.1)
    ops.node(11012, 19.85, 5.5, 3.1)
    ops.node(11013, 0.0, 11.0, 3.1)
    ops.node(11014, 4.25, 11.0, 3.1)
    ops.node(11015, 8.5, 11.0, 3.1)
    ops.node(11016, 11.35, 11.0, 3.1)
    ops.node(11017, 15.6, 11.0, 3.1)
    ops.node(11018, 19.85, 11.0, 3.1)
    # Retained floor node
    ops.node(91000, 9.925, 5.56098624, 3.1)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.2)
    ops.node(12002, 4.25, 0.0, 6.2)
    ops.node(12003, 8.5, 0.0, 6.2)
    ops.node(12004, 11.35, 0.0, 6.2)
    ops.node(12005, 15.6, 0.0, 6.2)
    ops.node(12006, 19.85, 0.0, 6.2)
    ops.node(12007, 0.0, 5.5, 6.2)
    ops.node(12008, 4.25, 5.5, 6.2)
    ops.node(12009, 8.5, 5.5, 6.2)
    ops.node(12010, 11.35, 5.5, 6.2)
    ops.node(12011, 15.6, 5.5, 6.2)
    ops.node(12012, 19.85, 5.5, 6.2)
    ops.node(12013, 0.0, 11.0, 6.2)
    ops.node(12014, 4.25, 11.0, 6.2)
    ops.node(12015, 8.5, 11.0, 6.2)
    ops.node(12016, 11.35, 11.0, 6.2)
    ops.node(12017, 15.6, 11.0, 6.2)
    ops.node(12018, 19.85, 11.0, 6.2)
    # Retained floor node
    ops.node(92000, 9.925, 5.56263303, 6.2)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.3)
    ops.node(13002, 4.25, 0.0, 9.3)
    ops.node(13003, 8.5, 0.0, 9.3)
    ops.node(13004, 11.35, 0.0, 9.3)
    ops.node(13005, 15.6, 0.0, 9.3)
    ops.node(13006, 19.85, 0.0, 9.3)
    ops.node(13007, 0.0, 5.5, 9.3)
    ops.node(13008, 4.25, 5.5, 9.3)
    ops.node(13009, 8.5, 5.5, 9.3)
    ops.node(13010, 11.35, 5.5, 9.3)
    ops.node(13011, 15.6, 5.5, 9.3)
    ops.node(13012, 19.85, 5.5, 9.3)
    ops.node(13013, 0.0, 11.0, 9.3)
    ops.node(13014, 4.25, 11.0, 9.3)
    ops.node(13015, 8.5, 11.0, 9.3)
    ops.node(13016, 11.35, 11.0, 9.3)
    ops.node(13017, 15.6, 11.0, 9.3)
    ops.node(13018, 19.85, 11.0, 9.3)
    # Retained floor node
    ops.node(93000, 9.925, 5.56406895, 9.3)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.4)
    ops.node(14002, 4.25, 0.0, 12.4)
    ops.node(14003, 8.5, 0.0, 12.4)
    ops.node(14004, 11.35, 0.0, 12.4)
    ops.node(14005, 15.6, 0.0, 12.4)
    ops.node(14006, 19.85, 0.0, 12.4)
    ops.node(14007, 0.0, 5.5, 12.4)
    ops.node(14008, 4.25, 5.5, 12.4)
    ops.node(14009, 8.5, 5.5, 12.4)
    ops.node(14010, 11.35, 5.5, 12.4)
    ops.node(14011, 15.6, 5.5, 12.4)
    ops.node(14012, 19.85, 5.5, 12.4)
    ops.node(14013, 0.0, 11.0, 12.4)
    ops.node(14014, 4.25, 11.0, 12.4)
    ops.node(14015, 8.5, 11.0, 12.4)
    ops.node(14016, 11.35, 11.0, 12.4)
    ops.node(14017, 15.6, 11.0, 12.4)
    ops.node(14018, 19.85, 11.0, 12.4)
    # Retained floor node
    ops.node(94000, 9.925, 5.64067679, 12.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
