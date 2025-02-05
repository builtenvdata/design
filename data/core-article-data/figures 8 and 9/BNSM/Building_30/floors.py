import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.5)
    ops.node(11002, 3.85, 0.0, 2.5)
    ops.node(11003, 7.7, 0.0, 2.5)
    ops.node(11004, 10.65, 0.0, 2.5)
    ops.node(11005, 14.5, 0.0, 2.5)
    ops.node(11006, 18.35, 0.0, 2.5)
    ops.node(11007, 0.0, 5.8, 2.5)
    ops.node(11008, 3.85, 5.8, 2.5)
    ops.node(11009, 7.7, 5.8, 2.5)
    ops.node(11010, 10.65, 5.8, 2.5)
    ops.node(11011, 14.5, 5.8, 2.5)
    ops.node(11012, 18.35, 5.8, 2.5)
    ops.node(11013, 0.0, 11.6, 2.5)
    ops.node(11014, 3.85, 11.6, 2.5)
    ops.node(11015, 7.7, 11.6, 2.5)
    ops.node(11016, 10.65, 11.6, 2.5)
    ops.node(11017, 14.5, 11.6, 2.5)
    ops.node(11018, 18.35, 11.6, 2.5)
    ops.node(11019, 0.0, 17.4, 2.5)
    ops.node(11020, 3.85, 17.4, 2.5)
    ops.node(11021, 7.7, 17.4, 2.5)
    ops.node(11022, 10.65, 17.4, 2.5)
    ops.node(11023, 14.5, 17.4, 2.5)
    ops.node(11024, 18.35, 17.4, 2.5)
    # Retained floor node
    ops.node(91000, 9.175, 8.7393828, 2.5)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.0)
    ops.node(12002, 3.85, 0.0, 5.0)
    ops.node(12003, 7.7, 0.0, 5.0)
    ops.node(12004, 10.65, 0.0, 5.0)
    ops.node(12005, 14.5, 0.0, 5.0)
    ops.node(12006, 18.35, 0.0, 5.0)
    ops.node(12007, 0.0, 5.8, 5.0)
    ops.node(12008, 3.85, 5.8, 5.0)
    ops.node(12009, 7.7, 5.8, 5.0)
    ops.node(12010, 10.65, 5.8, 5.0)
    ops.node(12011, 14.5, 5.8, 5.0)
    ops.node(12012, 18.35, 5.8, 5.0)
    ops.node(12013, 0.0, 11.6, 5.0)
    ops.node(12014, 3.85, 11.6, 5.0)
    ops.node(12015, 7.7, 11.6, 5.0)
    ops.node(12016, 10.65, 11.6, 5.0)
    ops.node(12017, 14.5, 11.6, 5.0)
    ops.node(12018, 18.35, 11.6, 5.0)
    ops.node(12019, 0.0, 17.4, 5.0)
    ops.node(12020, 3.85, 17.4, 5.0)
    ops.node(12021, 7.7, 17.4, 5.0)
    ops.node(12022, 10.65, 17.4, 5.0)
    ops.node(12023, 14.5, 17.4, 5.0)
    ops.node(12024, 18.35, 17.4, 5.0)
    # Retained floor node
    ops.node(92000, 9.175, 8.71570893, 5.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 7.5)
    ops.node(13002, 3.85, 0.0, 7.5)
    ops.node(13003, 7.7, 0.0, 7.5)
    ops.node(13004, 10.65, 0.0, 7.5)
    ops.node(13005, 14.5, 0.0, 7.5)
    ops.node(13006, 18.35, 0.0, 7.5)
    ops.node(13007, 0.0, 5.8, 7.5)
    ops.node(13008, 3.85, 5.8, 7.5)
    ops.node(13009, 7.7, 5.8, 7.5)
    ops.node(13010, 10.65, 5.8, 7.5)
    ops.node(13011, 14.5, 5.8, 7.5)
    ops.node(13012, 18.35, 5.8, 7.5)
    ops.node(13013, 0.0, 11.6, 7.5)
    ops.node(13014, 3.85, 11.6, 7.5)
    ops.node(13015, 7.7, 11.6, 7.5)
    ops.node(13016, 10.65, 11.6, 7.5)
    ops.node(13017, 14.5, 11.6, 7.5)
    ops.node(13018, 18.35, 11.6, 7.5)
    ops.node(13019, 0.0, 17.4, 7.5)
    ops.node(13020, 3.85, 17.4, 7.5)
    ops.node(13021, 7.7, 17.4, 7.5)
    ops.node(13022, 10.65, 17.4, 7.5)
    ops.node(13023, 14.5, 17.4, 7.5)
    ops.node(13024, 18.35, 17.4, 7.5)
    # Retained floor node
    ops.node(93000, 9.175, 8.69720961, 7.5)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 10.0)
    ops.node(14002, 3.85, 0.0, 10.0)
    ops.node(14003, 7.7, 0.0, 10.0)
    ops.node(14004, 10.65, 0.0, 10.0)
    ops.node(14005, 14.5, 0.0, 10.0)
    ops.node(14006, 18.35, 0.0, 10.0)
    ops.node(14007, 0.0, 5.8, 10.0)
    ops.node(14008, 3.85, 5.8, 10.0)
    ops.node(14009, 7.7, 5.8, 10.0)
    ops.node(14010, 10.65, 5.8, 10.0)
    ops.node(14011, 14.5, 5.8, 10.0)
    ops.node(14012, 18.35, 5.8, 10.0)
    ops.node(14013, 0.0, 11.6, 10.0)
    ops.node(14014, 3.85, 11.6, 10.0)
    ops.node(14015, 7.7, 11.6, 10.0)
    ops.node(14016, 10.65, 11.6, 10.0)
    ops.node(14017, 14.5, 11.6, 10.0)
    ops.node(14018, 18.35, 11.6, 10.0)
    ops.node(14019, 0.0, 17.4, 10.0)
    ops.node(14020, 3.85, 17.4, 10.0)
    ops.node(14021, 7.7, 17.4, 10.0)
    ops.node(14022, 10.65, 17.4, 10.0)
    ops.node(14023, 14.5, 17.4, 10.0)
    ops.node(14024, 18.35, 17.4, 10.0)
    # Retained floor node
    ops.node(94000, 9.175, 8.79529165, 10.0)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
