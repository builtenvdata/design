import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.7)
    ops.node(11002, 2.9, 0.0, 2.7)
    ops.node(11003, 6.6, 0.0, 2.7)
    ops.node(11004, 10.3, 0.0, 2.7)
    ops.node(11005, 0.0, 5.7, 2.7)
    ops.node(11006, 2.9, 5.7, 2.7)
    ops.node(11007, 6.6, 5.7, 2.7)
    ops.node(11008, 10.3, 5.7, 2.7)
    ops.node(11009, 0.0, 11.4, 2.7)
    ops.node(11010, 2.9, 11.4, 2.7)
    ops.node(11011, 6.6, 11.4, 2.7)
    ops.node(11012, 10.3, 11.4, 2.7)
    ops.node(11013, 0.0, 17.1, 2.7)
    ops.node(11014, 2.9, 17.1, 2.7)
    ops.node(11015, 6.6, 17.1, 2.7)
    ops.node(11016, 10.3, 17.1, 2.7)
    ops.node(11017, 0.0, 22.8, 2.7)
    ops.node(11018, 2.9, 22.8, 2.7)
    ops.node(11019, 6.6, 22.8, 2.7)
    ops.node(11020, 10.3, 22.8, 2.7)
    # Retained floor node
    ops.node(91000, 5.27435734, 11.71244241, 2.7)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.4)
    ops.node(12002, 2.9, 0.0, 5.4)
    ops.node(12003, 6.6, 0.0, 5.4)
    ops.node(12004, 10.3, 0.0, 5.4)
    ops.node(12005, 0.0, 5.7, 5.4)
    ops.node(12006, 2.9, 5.7, 5.4)
    ops.node(12007, 6.6, 5.7, 5.4)
    ops.node(12008, 10.3, 5.7, 5.4)
    ops.node(12009, 0.0, 11.4, 5.4)
    ops.node(12010, 2.9, 11.4, 5.4)
    ops.node(12011, 6.6, 11.4, 5.4)
    ops.node(12012, 10.3, 11.4, 5.4)
    ops.node(12013, 0.0, 17.1, 5.4)
    ops.node(12014, 2.9, 17.1, 5.4)
    ops.node(12015, 6.6, 17.1, 5.4)
    ops.node(12016, 10.3, 17.1, 5.4)
    ops.node(12017, 0.0, 22.8, 5.4)
    ops.node(12018, 2.9, 22.8, 5.4)
    ops.node(12019, 6.6, 22.8, 5.4)
    ops.node(12020, 10.3, 22.8, 5.4)
    # Retained floor node
    ops.node(92000, 5.2721826, 11.69354411, 5.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.1)
    ops.node(13002, 2.9, 0.0, 8.1)
    ops.node(13003, 6.6, 0.0, 8.1)
    ops.node(13004, 10.3, 0.0, 8.1)
    ops.node(13005, 0.0, 5.7, 8.1)
    ops.node(13006, 2.9, 5.7, 8.1)
    ops.node(13007, 6.6, 5.7, 8.1)
    ops.node(13008, 10.3, 5.7, 8.1)
    ops.node(13009, 0.0, 11.4, 8.1)
    ops.node(13010, 2.9, 11.4, 8.1)
    ops.node(13011, 6.6, 11.4, 8.1)
    ops.node(13012, 10.3, 11.4, 8.1)
    ops.node(13013, 0.0, 17.1, 8.1)
    ops.node(13014, 2.9, 17.1, 8.1)
    ops.node(13015, 6.6, 17.1, 8.1)
    ops.node(13016, 10.3, 17.1, 8.1)
    ops.node(13017, 0.0, 22.8, 8.1)
    ops.node(13018, 2.9, 22.8, 8.1)
    ops.node(13019, 6.6, 22.8, 8.1)
    ops.node(13020, 10.3, 22.8, 8.1)
    # Retained floor node
    ops.node(93000, 5.26976619, 11.68308551, 8.1)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 10.8)
    ops.node(14002, 2.9, 0.0, 10.8)
    ops.node(14003, 6.6, 0.0, 10.8)
    ops.node(14004, 10.3, 0.0, 10.8)
    ops.node(14005, 0.0, 5.7, 10.8)
    ops.node(14006, 2.9, 5.7, 10.8)
    ops.node(14007, 6.6, 5.7, 10.8)
    ops.node(14008, 10.3, 5.7, 10.8)
    ops.node(14009, 0.0, 11.4, 10.8)
    ops.node(14010, 2.9, 11.4, 10.8)
    ops.node(14011, 6.6, 11.4, 10.8)
    ops.node(14012, 10.3, 11.4, 10.8)
    ops.node(14013, 0.0, 17.1, 10.8)
    ops.node(14014, 2.9, 17.1, 10.8)
    ops.node(14015, 6.6, 17.1, 10.8)
    ops.node(14016, 10.3, 17.1, 10.8)
    ops.node(14017, 0.0, 22.8, 10.8)
    ops.node(14018, 2.9, 22.8, 10.8)
    ops.node(14019, 6.6, 22.8, 10.8)
    ops.node(14020, 10.3, 22.8, 10.8)
    # Retained floor node
    ops.node(94000, 5.30609694, 11.76442266, 10.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
