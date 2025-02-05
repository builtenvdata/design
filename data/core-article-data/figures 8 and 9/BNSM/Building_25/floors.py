import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.6)
    ops.node(11002, 7.45, 0.0, 2.6)
    ops.node(11003, 10.3, 0.0, 2.6)
    ops.node(11004, 17.75, 0.0, 2.6)
    ops.node(11005, 0.0, 3.5, 2.6)
    ops.node(11006, 7.45, 3.5, 2.6)
    ops.node(11007, 10.3, 3.5, 2.6)
    ops.node(11008, 17.75, 3.5, 2.6)
    ops.node(11009, 0.0, 7.0, 2.6)
    ops.node(11010, 7.45, 7.0, 2.6)
    ops.node(11011, 10.3, 7.0, 2.6)
    ops.node(11012, 17.75, 7.0, 2.6)
    ops.node(11013, 0.0, 10.5, 2.6)
    ops.node(11014, 7.45, 10.5, 2.6)
    ops.node(11015, 10.3, 10.5, 2.6)
    ops.node(11016, 17.75, 10.5, 2.6)
    # Retained floor node
    ops.node(91000, 8.875, 5.28296944, 2.6)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.2)
    ops.node(12002, 7.45, 0.0, 5.2)
    ops.node(12003, 10.3, 0.0, 5.2)
    ops.node(12004, 17.75, 0.0, 5.2)
    ops.node(12005, 0.0, 3.5, 5.2)
    ops.node(12006, 7.45, 3.5, 5.2)
    ops.node(12007, 10.3, 3.5, 5.2)
    ops.node(12008, 17.75, 3.5, 5.2)
    ops.node(12009, 0.0, 7.0, 5.2)
    ops.node(12010, 7.45, 7.0, 5.2)
    ops.node(12011, 10.3, 7.0, 5.2)
    ops.node(12012, 17.75, 7.0, 5.2)
    ops.node(12013, 0.0, 10.5, 5.2)
    ops.node(12014, 7.45, 10.5, 5.2)
    ops.node(12015, 10.3, 10.5, 5.2)
    ops.node(12016, 17.75, 10.5, 5.2)
    # Retained floor node
    ops.node(92000, 8.875, 5.28493534, 5.2)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 7.8)
    ops.node(13002, 7.45, 0.0, 7.8)
    ops.node(13003, 10.3, 0.0, 7.8)
    ops.node(13004, 17.75, 0.0, 7.8)
    ops.node(13005, 0.0, 3.5, 7.8)
    ops.node(13006, 7.45, 3.5, 7.8)
    ops.node(13007, 10.3, 3.5, 7.8)
    ops.node(13008, 17.75, 3.5, 7.8)
    ops.node(13009, 0.0, 7.0, 7.8)
    ops.node(13010, 7.45, 7.0, 7.8)
    ops.node(13011, 10.3, 7.0, 7.8)
    ops.node(13012, 17.75, 7.0, 7.8)
    ops.node(13013, 0.0, 10.5, 7.8)
    ops.node(13014, 7.45, 10.5, 7.8)
    ops.node(13015, 10.3, 10.5, 7.8)
    ops.node(13016, 17.75, 10.5, 7.8)
    # Retained floor node
    ops.node(93000, 8.875, 5.28683145, 7.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 10.4)
    ops.node(14002, 7.45, 0.0, 10.4)
    ops.node(14003, 10.3, 0.0, 10.4)
    ops.node(14004, 17.75, 0.0, 10.4)
    ops.node(14005, 0.0, 3.5, 10.4)
    ops.node(14006, 7.45, 3.5, 10.4)
    ops.node(14007, 10.3, 3.5, 10.4)
    ops.node(14008, 17.75, 3.5, 10.4)
    ops.node(14009, 0.0, 7.0, 10.4)
    ops.node(14010, 7.45, 7.0, 10.4)
    ops.node(14011, 10.3, 7.0, 10.4)
    ops.node(14012, 17.75, 7.0, 10.4)
    ops.node(14013, 0.0, 10.5, 10.4)
    ops.node(14014, 7.45, 10.5, 10.4)
    ops.node(14015, 10.3, 10.5, 10.4)
    ops.node(14016, 17.75, 10.5, 10.4)
    # Retained floor node
    ops.node(94000, 8.875, 5.30166771, 10.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
