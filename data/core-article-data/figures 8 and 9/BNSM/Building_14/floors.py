import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.05)
    ops.node(11002, 3.0, 0.0, 3.05)
    ops.node(11003, 7.65, 0.0, 3.05)
    ops.node(11004, 12.3, 0.0, 3.05)
    ops.node(11005, 0.0, 5.2, 3.05)
    ops.node(11006, 3.0, 5.2, 3.05)
    ops.node(11007, 7.65, 5.2, 3.05)
    ops.node(11008, 12.3, 5.2, 3.05)
    ops.node(11009, 0.0, 10.4, 3.05)
    ops.node(11010, 3.0, 10.4, 3.05)
    ops.node(11011, 7.65, 10.4, 3.05)
    ops.node(11012, 12.3, 10.4, 3.05)
    ops.node(11013, 0.0, 15.6, 3.05)
    ops.node(11014, 3.0, 15.6, 3.05)
    ops.node(11015, 7.65, 15.6, 3.05)
    ops.node(11016, 12.3, 15.6, 3.05)
    # Retained floor node
    ops.node(91000, 6.41173966, 8.04338318, 3.05)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.8)
    ops.node(12002, 3.0, 0.0, 5.8)
    ops.node(12003, 7.65, 0.0, 5.8)
    ops.node(12004, 12.3, 0.0, 5.8)
    ops.node(12005, 0.0, 5.2, 5.8)
    ops.node(12006, 3.0, 5.2, 5.8)
    ops.node(12007, 7.65, 5.2, 5.8)
    ops.node(12008, 12.3, 5.2, 5.8)
    ops.node(12009, 0.0, 10.4, 5.8)
    ops.node(12010, 3.0, 10.4, 5.8)
    ops.node(12011, 7.65, 10.4, 5.8)
    ops.node(12012, 12.3, 10.4, 5.8)
    ops.node(12013, 0.0, 15.6, 5.8)
    ops.node(12014, 3.0, 15.6, 5.8)
    ops.node(12015, 7.65, 15.6, 5.8)
    ops.node(12016, 12.3, 15.6, 5.8)
    # Retained floor node
    ops.node(92000, 6.41031499, 8.02177992, 5.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.55)
    ops.node(13002, 3.0, 0.0, 8.55)
    ops.node(13003, 7.65, 0.0, 8.55)
    ops.node(13004, 12.3, 0.0, 8.55)
    ops.node(13005, 0.0, 5.2, 8.55)
    ops.node(13006, 3.0, 5.2, 8.55)
    ops.node(13007, 7.65, 5.2, 8.55)
    ops.node(13008, 12.3, 5.2, 8.55)
    ops.node(13009, 0.0, 10.4, 8.55)
    ops.node(13010, 3.0, 10.4, 8.55)
    ops.node(13011, 7.65, 10.4, 8.55)
    ops.node(13012, 12.3, 10.4, 8.55)
    ops.node(13013, 0.0, 15.6, 8.55)
    ops.node(13014, 3.0, 15.6, 8.55)
    ops.node(13015, 7.65, 15.6, 8.55)
    ops.node(13016, 12.3, 15.6, 8.55)
    # Retained floor node
    ops.node(93000, 6.4087787, 8.02370191, 8.55)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.3)
    ops.node(14002, 3.0, 0.0, 11.3)
    ops.node(14003, 7.65, 0.0, 11.3)
    ops.node(14004, 12.3, 0.0, 11.3)
    ops.node(14005, 0.0, 5.2, 11.3)
    ops.node(14006, 3.0, 5.2, 11.3)
    ops.node(14007, 7.65, 5.2, 11.3)
    ops.node(14008, 12.3, 5.2, 11.3)
    ops.node(14009, 0.0, 10.4, 11.3)
    ops.node(14010, 3.0, 10.4, 11.3)
    ops.node(14011, 7.65, 10.4, 11.3)
    ops.node(14012, 12.3, 10.4, 11.3)
    ops.node(14013, 0.0, 15.6, 11.3)
    ops.node(14014, 3.0, 15.6, 11.3)
    ops.node(14015, 7.65, 15.6, 11.3)
    ops.node(14016, 12.3, 15.6, 11.3)
    # Retained floor node
    ops.node(94000, 6.48451149, 8.06479647, 11.3)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
