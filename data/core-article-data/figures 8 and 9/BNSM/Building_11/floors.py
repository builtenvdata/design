import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.15)
    ops.node(11002, 3.05, 0.0, 3.15)
    ops.node(11003, 9.0, 0.0, 3.15)
    ops.node(11004, 14.95, 0.0, 3.15)
    ops.node(11005, 0.0, 3.95, 3.15)
    ops.node(11006, 3.05, 3.95, 3.15)
    ops.node(11007, 9.0, 3.95, 3.15)
    ops.node(11008, 14.95, 3.95, 3.15)
    ops.node(11009, 0.0, 7.9, 3.15)
    ops.node(11010, 3.05, 7.9, 3.15)
    ops.node(11011, 9.0, 7.9, 3.15)
    ops.node(11012, 14.95, 7.9, 3.15)
    ops.node(11013, 0.0, 11.85, 3.15)
    ops.node(11014, 3.05, 11.85, 3.15)
    ops.node(11015, 9.0, 11.85, 3.15)
    ops.node(11016, 14.95, 11.85, 3.15)
    ops.node(11017, 0.0, 15.8, 3.15)
    ops.node(11018, 3.05, 15.8, 3.15)
    ops.node(11019, 9.0, 15.8, 3.15)
    ops.node(11020, 14.95, 15.8, 3.15)
    # Retained floor node
    ops.node(91000, 7.66538789, 8.04368611, 3.15)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.3)
    ops.node(12002, 3.05, 0.0, 6.3)
    ops.node(12003, 9.0, 0.0, 6.3)
    ops.node(12004, 14.95, 0.0, 6.3)
    ops.node(12005, 0.0, 3.95, 6.3)
    ops.node(12006, 3.05, 3.95, 6.3)
    ops.node(12007, 9.0, 3.95, 6.3)
    ops.node(12008, 14.95, 3.95, 6.3)
    ops.node(12009, 0.0, 7.9, 6.3)
    ops.node(12010, 3.05, 7.9, 6.3)
    ops.node(12011, 9.0, 7.9, 6.3)
    ops.node(12012, 14.95, 7.9, 6.3)
    ops.node(12013, 0.0, 11.85, 6.3)
    ops.node(12014, 3.05, 11.85, 6.3)
    ops.node(12015, 9.0, 11.85, 6.3)
    ops.node(12016, 14.95, 11.85, 6.3)
    ops.node(12017, 0.0, 15.8, 6.3)
    ops.node(12018, 3.05, 15.8, 6.3)
    ops.node(12019, 9.0, 15.8, 6.3)
    ops.node(12020, 14.95, 15.8, 6.3)
    # Retained floor node
    ops.node(92000, 7.66759914, 8.04429454, 6.3)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.45)
    ops.node(13002, 3.05, 0.0, 9.45)
    ops.node(13003, 9.0, 0.0, 9.45)
    ops.node(13004, 14.95, 0.0, 9.45)
    ops.node(13005, 0.0, 3.95, 9.45)
    ops.node(13006, 3.05, 3.95, 9.45)
    ops.node(13007, 9.0, 3.95, 9.45)
    ops.node(13008, 14.95, 3.95, 9.45)
    ops.node(13009, 0.0, 7.9, 9.45)
    ops.node(13010, 3.05, 7.9, 9.45)
    ops.node(13011, 9.0, 7.9, 9.45)
    ops.node(13012, 14.95, 7.9, 9.45)
    ops.node(13013, 0.0, 11.85, 9.45)
    ops.node(13014, 3.05, 11.85, 9.45)
    ops.node(13015, 9.0, 11.85, 9.45)
    ops.node(13016, 14.95, 11.85, 9.45)
    ops.node(13017, 0.0, 15.8, 9.45)
    ops.node(13018, 3.05, 15.8, 9.45)
    ops.node(13019, 9.0, 15.8, 9.45)
    ops.node(13020, 14.95, 15.8, 9.45)
    # Retained floor node
    ops.node(93000, 7.66420109, 8.04546692, 9.45)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.6)
    ops.node(14002, 3.05, 0.0, 12.6)
    ops.node(14003, 9.0, 0.0, 12.6)
    ops.node(14004, 14.95, 0.0, 12.6)
    ops.node(14005, 0.0, 3.95, 12.6)
    ops.node(14006, 3.05, 3.95, 12.6)
    ops.node(14007, 9.0, 3.95, 12.6)
    ops.node(14008, 14.95, 3.95, 12.6)
    ops.node(14009, 0.0, 7.9, 12.6)
    ops.node(14010, 3.05, 7.9, 12.6)
    ops.node(14011, 9.0, 7.9, 12.6)
    ops.node(14012, 14.95, 7.9, 12.6)
    ops.node(14013, 0.0, 11.85, 12.6)
    ops.node(14014, 3.05, 11.85, 12.6)
    ops.node(14015, 9.0, 11.85, 12.6)
    ops.node(14016, 14.95, 11.85, 12.6)
    ops.node(14017, 0.0, 15.8, 12.6)
    ops.node(14018, 3.05, 15.8, 12.6)
    ops.node(14019, 9.0, 15.8, 12.6)
    ops.node(14020, 14.95, 15.8, 12.6)
    # Retained floor node
    ops.node(94000, 7.7310652, 8.0578201, 12.6)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
