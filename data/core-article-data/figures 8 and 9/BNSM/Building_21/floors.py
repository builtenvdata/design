import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.25)
    ops.node(11002, 4.45, 0.0, 3.25)
    ops.node(11003, 8.9, 0.0, 3.25)
    ops.node(11004, 13.35, 0.0, 3.25)
    ops.node(11005, 16.35, 0.0, 3.25)
    ops.node(11006, 20.8, 0.0, 3.25)
    ops.node(11007, 25.25, 0.0, 3.25)
    ops.node(11008, 29.7, 0.0, 3.25)
    ops.node(11009, 0.0, 5.15, 3.25)
    ops.node(11010, 4.45, 5.15, 3.25)
    ops.node(11011, 8.9, 5.15, 3.25)
    ops.node(11012, 13.35, 5.15, 3.25)
    ops.node(11013, 16.35, 5.15, 3.25)
    ops.node(11014, 20.8, 5.15, 3.25)
    ops.node(11015, 25.25, 5.15, 3.25)
    ops.node(11016, 29.7, 5.15, 3.25)
    ops.node(11017, 0.0, 10.3, 3.25)
    ops.node(11018, 4.45, 10.3, 3.25)
    ops.node(11019, 8.9, 10.3, 3.25)
    ops.node(11020, 13.35, 10.3, 3.25)
    ops.node(11021, 16.35, 10.3, 3.25)
    ops.node(11022, 20.8, 10.3, 3.25)
    ops.node(11023, 25.25, 10.3, 3.25)
    ops.node(11024, 29.7, 10.3, 3.25)
    # Retained floor node
    ops.node(91000, 14.85, 5.2242042, 3.25)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.95)
    ops.node(12002, 4.45, 0.0, 5.95)
    ops.node(12003, 8.9, 0.0, 5.95)
    ops.node(12004, 13.35, 0.0, 5.95)
    ops.node(12005, 16.35, 0.0, 5.95)
    ops.node(12006, 20.8, 0.0, 5.95)
    ops.node(12007, 25.25, 0.0, 5.95)
    ops.node(12008, 29.7, 0.0, 5.95)
    ops.node(12009, 0.0, 5.15, 5.95)
    ops.node(12010, 4.45, 5.15, 5.95)
    ops.node(12011, 8.9, 5.15, 5.95)
    ops.node(12012, 13.35, 5.15, 5.95)
    ops.node(12013, 16.35, 5.15, 5.95)
    ops.node(12014, 20.8, 5.15, 5.95)
    ops.node(12015, 25.25, 5.15, 5.95)
    ops.node(12016, 29.7, 5.15, 5.95)
    ops.node(12017, 0.0, 10.3, 5.95)
    ops.node(12018, 4.45, 10.3, 5.95)
    ops.node(12019, 8.9, 10.3, 5.95)
    ops.node(12020, 13.35, 10.3, 5.95)
    ops.node(12021, 16.35, 10.3, 5.95)
    ops.node(12022, 20.8, 10.3, 5.95)
    ops.node(12023, 25.25, 10.3, 5.95)
    ops.node(12024, 29.7, 10.3, 5.95)
    # Retained floor node
    ops.node(92000, 14.85, 5.22278319, 5.95)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.65)
    ops.node(13002, 4.45, 0.0, 8.65)
    ops.node(13003, 8.9, 0.0, 8.65)
    ops.node(13004, 13.35, 0.0, 8.65)
    ops.node(13005, 16.35, 0.0, 8.65)
    ops.node(13006, 20.8, 0.0, 8.65)
    ops.node(13007, 25.25, 0.0, 8.65)
    ops.node(13008, 29.7, 0.0, 8.65)
    ops.node(13009, 0.0, 5.15, 8.65)
    ops.node(13010, 4.45, 5.15, 8.65)
    ops.node(13011, 8.9, 5.15, 8.65)
    ops.node(13012, 13.35, 5.15, 8.65)
    ops.node(13013, 16.35, 5.15, 8.65)
    ops.node(13014, 20.8, 5.15, 8.65)
    ops.node(13015, 25.25, 5.15, 8.65)
    ops.node(13016, 29.7, 5.15, 8.65)
    ops.node(13017, 0.0, 10.3, 8.65)
    ops.node(13018, 4.45, 10.3, 8.65)
    ops.node(13019, 8.9, 10.3, 8.65)
    ops.node(13020, 13.35, 10.3, 8.65)
    ops.node(13021, 16.35, 10.3, 8.65)
    ops.node(13022, 20.8, 10.3, 8.65)
    ops.node(13023, 25.25, 10.3, 8.65)
    ops.node(13024, 29.7, 10.3, 8.65)
    # Retained floor node
    ops.node(93000, 14.85, 5.22231056, 8.65)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.35)
    ops.node(14002, 4.45, 0.0, 11.35)
    ops.node(14003, 8.9, 0.0, 11.35)
    ops.node(14004, 13.35, 0.0, 11.35)
    ops.node(14005, 16.35, 0.0, 11.35)
    ops.node(14006, 20.8, 0.0, 11.35)
    ops.node(14007, 25.25, 0.0, 11.35)
    ops.node(14008, 29.7, 0.0, 11.35)
    ops.node(14009, 0.0, 5.15, 11.35)
    ops.node(14010, 4.45, 5.15, 11.35)
    ops.node(14011, 8.9, 5.15, 11.35)
    ops.node(14012, 13.35, 5.15, 11.35)
    ops.node(14013, 16.35, 5.15, 11.35)
    ops.node(14014, 20.8, 5.15, 11.35)
    ops.node(14015, 25.25, 5.15, 11.35)
    ops.node(14016, 29.7, 5.15, 11.35)
    ops.node(14017, 0.0, 10.3, 11.35)
    ops.node(14018, 4.45, 10.3, 11.35)
    ops.node(14019, 8.9, 10.3, 11.35)
    ops.node(14020, 13.35, 10.3, 11.35)
    ops.node(14021, 16.35, 10.3, 11.35)
    ops.node(14022, 20.8, 10.3, 11.35)
    ops.node(14023, 25.25, 10.3, 11.35)
    ops.node(14024, 29.7, 10.3, 11.35)
    # Retained floor node
    ops.node(94000, 14.85, 5.25296167, 11.35)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
