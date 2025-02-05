import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.65)
    ops.node(11002, 7.3, 0.0, 2.65)
    ops.node(11003, 14.6, 0.0, 2.65)
    ops.node(11004, 17.65, 0.0, 2.65)
    ops.node(11005, 24.95, 0.0, 2.65)
    ops.node(11006, 32.25, 0.0, 2.65)
    ops.node(11007, 0.0, 3.65, 2.65)
    ops.node(11008, 7.3, 3.65, 2.65)
    ops.node(11009, 14.6, 3.65, 2.65)
    ops.node(11010, 17.65, 3.65, 2.65)
    ops.node(11011, 24.95, 3.65, 2.65)
    ops.node(11012, 32.25, 3.65, 2.65)
    ops.node(11013, 0.0, 7.3, 2.65)
    ops.node(11014, 7.3, 7.3, 2.65)
    ops.node(11015, 14.6, 7.3, 2.65)
    ops.node(11016, 17.65, 7.3, 2.65)
    ops.node(11017, 24.95, 7.3, 2.65)
    ops.node(11018, 32.25, 7.3, 2.65)
    # Retained floor node
    ops.node(91000, 16.125, 3.68891121, 2.65)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.3)
    ops.node(12002, 7.3, 0.0, 5.3)
    ops.node(12003, 14.6, 0.0, 5.3)
    ops.node(12004, 17.65, 0.0, 5.3)
    ops.node(12005, 24.95, 0.0, 5.3)
    ops.node(12006, 32.25, 0.0, 5.3)
    ops.node(12007, 0.0, 3.65, 5.3)
    ops.node(12008, 7.3, 3.65, 5.3)
    ops.node(12009, 14.6, 3.65, 5.3)
    ops.node(12010, 17.65, 3.65, 5.3)
    ops.node(12011, 24.95, 3.65, 5.3)
    ops.node(12012, 32.25, 3.65, 5.3)
    ops.node(12013, 0.0, 7.3, 5.3)
    ops.node(12014, 7.3, 7.3, 5.3)
    ops.node(12015, 14.6, 7.3, 5.3)
    ops.node(12016, 17.65, 7.3, 5.3)
    ops.node(12017, 24.95, 7.3, 5.3)
    ops.node(12018, 32.25, 7.3, 5.3)
    # Retained floor node
    ops.node(92000, 16.125, 3.6859189, 5.3)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 7.95)
    ops.node(13002, 7.3, 0.0, 7.95)
    ops.node(13003, 14.6, 0.0, 7.95)
    ops.node(13004, 17.65, 0.0, 7.95)
    ops.node(13005, 24.95, 0.0, 7.95)
    ops.node(13006, 32.25, 0.0, 7.95)
    ops.node(13007, 0.0, 3.65, 7.95)
    ops.node(13008, 7.3, 3.65, 7.95)
    ops.node(13009, 14.6, 3.65, 7.95)
    ops.node(13010, 17.65, 3.65, 7.95)
    ops.node(13011, 24.95, 3.65, 7.95)
    ops.node(13012, 32.25, 3.65, 7.95)
    ops.node(13013, 0.0, 7.3, 7.95)
    ops.node(13014, 7.3, 7.3, 7.95)
    ops.node(13015, 14.6, 7.3, 7.95)
    ops.node(13016, 17.65, 7.3, 7.95)
    ops.node(13017, 24.95, 7.3, 7.95)
    ops.node(13018, 32.25, 7.3, 7.95)
    # Retained floor node
    ops.node(93000, 16.125, 3.683111, 7.95)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 10.6)
    ops.node(14002, 7.3, 0.0, 10.6)
    ops.node(14003, 14.6, 0.0, 10.6)
    ops.node(14004, 17.65, 0.0, 10.6)
    ops.node(14005, 24.95, 0.0, 10.6)
    ops.node(14006, 32.25, 0.0, 10.6)
    ops.node(14007, 0.0, 3.65, 10.6)
    ops.node(14008, 7.3, 3.65, 10.6)
    ops.node(14009, 14.6, 3.65, 10.6)
    ops.node(14010, 17.65, 3.65, 10.6)
    ops.node(14011, 24.95, 3.65, 10.6)
    ops.node(14012, 32.25, 3.65, 10.6)
    ops.node(14013, 0.0, 7.3, 10.6)
    ops.node(14014, 7.3, 7.3, 10.6)
    ops.node(14015, 14.6, 7.3, 10.6)
    ops.node(14016, 17.65, 7.3, 10.6)
    ops.node(14017, 24.95, 7.3, 10.6)
    ops.node(14018, 32.25, 7.3, 10.6)
    # Retained floor node
    ops.node(94000, 16.125, 3.70430411, 10.6)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
