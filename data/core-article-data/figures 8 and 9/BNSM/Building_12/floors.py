import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.05)
    ops.node(11002, 3.9, 0.0, 3.05)
    ops.node(11003, 7.8, 0.0, 3.05)
    ops.node(11004, 10.8, 0.0, 3.05)
    ops.node(11005, 14.7, 0.0, 3.05)
    ops.node(11006, 18.6, 0.0, 3.05)
    ops.node(11007, 0.0, 5.35, 3.05)
    ops.node(11008, 3.9, 5.35, 3.05)
    ops.node(11009, 7.8, 5.35, 3.05)
    ops.node(11010, 10.8, 5.35, 3.05)
    ops.node(11011, 14.7, 5.35, 3.05)
    ops.node(11012, 18.6, 5.35, 3.05)
    ops.node(11013, 0.0, 10.7, 3.05)
    ops.node(11014, 3.9, 10.7, 3.05)
    ops.node(11015, 7.8, 10.7, 3.05)
    ops.node(11016, 10.8, 10.7, 3.05)
    ops.node(11017, 14.7, 10.7, 3.05)
    ops.node(11018, 18.6, 10.7, 3.05)
    # Retained floor node
    ops.node(91000, 9.3, 5.47211453, 3.05)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.1)
    ops.node(12002, 3.9, 0.0, 6.1)
    ops.node(12003, 7.8, 0.0, 6.1)
    ops.node(12004, 10.8, 0.0, 6.1)
    ops.node(12005, 14.7, 0.0, 6.1)
    ops.node(12006, 18.6, 0.0, 6.1)
    ops.node(12007, 0.0, 5.35, 6.1)
    ops.node(12008, 3.9, 5.35, 6.1)
    ops.node(12009, 7.8, 5.35, 6.1)
    ops.node(12010, 10.8, 5.35, 6.1)
    ops.node(12011, 14.7, 5.35, 6.1)
    ops.node(12012, 18.6, 5.35, 6.1)
    ops.node(12013, 0.0, 10.7, 6.1)
    ops.node(12014, 3.9, 10.7, 6.1)
    ops.node(12015, 7.8, 10.7, 6.1)
    ops.node(12016, 10.8, 10.7, 6.1)
    ops.node(12017, 14.7, 10.7, 6.1)
    ops.node(12018, 18.6, 10.7, 6.1)
    # Retained floor node
    ops.node(92000, 9.3, 5.46944874, 6.1)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.15)
    ops.node(13002, 3.9, 0.0, 9.15)
    ops.node(13003, 7.8, 0.0, 9.15)
    ops.node(13004, 10.8, 0.0, 9.15)
    ops.node(13005, 14.7, 0.0, 9.15)
    ops.node(13006, 18.6, 0.0, 9.15)
    ops.node(13007, 0.0, 5.35, 9.15)
    ops.node(13008, 3.9, 5.35, 9.15)
    ops.node(13009, 7.8, 5.35, 9.15)
    ops.node(13010, 10.8, 5.35, 9.15)
    ops.node(13011, 14.7, 5.35, 9.15)
    ops.node(13012, 18.6, 5.35, 9.15)
    ops.node(13013, 0.0, 10.7, 9.15)
    ops.node(13014, 3.9, 10.7, 9.15)
    ops.node(13015, 7.8, 10.7, 9.15)
    ops.node(13016, 10.8, 10.7, 9.15)
    ops.node(13017, 14.7, 10.7, 9.15)
    ops.node(13018, 18.6, 10.7, 9.15)
    # Retained floor node
    ops.node(93000, 9.3, 5.46690443, 9.15)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.2)
    ops.node(14002, 3.9, 0.0, 12.2)
    ops.node(14003, 7.8, 0.0, 12.2)
    ops.node(14004, 10.8, 0.0, 12.2)
    ops.node(14005, 14.7, 0.0, 12.2)
    ops.node(14006, 18.6, 0.0, 12.2)
    ops.node(14007, 0.0, 5.35, 12.2)
    ops.node(14008, 3.9, 5.35, 12.2)
    ops.node(14009, 7.8, 5.35, 12.2)
    ops.node(14010, 10.8, 5.35, 12.2)
    ops.node(14011, 14.7, 5.35, 12.2)
    ops.node(14012, 18.6, 5.35, 12.2)
    ops.node(14013, 0.0, 10.7, 12.2)
    ops.node(14014, 3.9, 10.7, 12.2)
    ops.node(14015, 7.8, 10.7, 12.2)
    ops.node(14016, 10.8, 10.7, 12.2)
    ops.node(14017, 14.7, 10.7, 12.2)
    ops.node(14018, 18.6, 10.7, 12.2)
    # Retained floor node
    ops.node(94000, 9.3, 5.53055968, 12.2)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
