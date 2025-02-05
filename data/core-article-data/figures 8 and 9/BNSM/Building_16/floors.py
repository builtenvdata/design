import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.15)
    ops.node(11002, 3.1, 0.0, 3.15)
    ops.node(11003, 7.35, 0.0, 3.15)
    ops.node(11004, 11.6, 0.0, 3.15)
    ops.node(11005, 0.0, 4.4, 3.15)
    ops.node(11006, 3.1, 4.4, 3.15)
    ops.node(11007, 7.35, 4.4, 3.15)
    ops.node(11008, 11.6, 4.4, 3.15)
    ops.node(11009, 0.0, 8.8, 3.15)
    ops.node(11010, 3.1, 8.8, 3.15)
    ops.node(11011, 7.35, 8.8, 3.15)
    ops.node(11012, 11.6, 8.8, 3.15)
    ops.node(11013, 0.0, 13.2, 3.15)
    ops.node(11014, 3.1, 13.2, 3.15)
    ops.node(11015, 7.35, 13.2, 3.15)
    ops.node(11016, 11.6, 13.2, 3.15)
    ops.node(11017, 0.0, 17.6, 3.15)
    ops.node(11018, 3.1, 17.6, 3.15)
    ops.node(11019, 7.35, 17.6, 3.15)
    ops.node(11020, 11.6, 17.6, 3.15)
    ops.node(11021, 0.0, 22.0, 3.15)
    ops.node(11022, 3.1, 22.0, 3.15)
    ops.node(11023, 7.35, 22.0, 3.15)
    ops.node(11024, 11.6, 22.0, 3.15)
    # Retained floor node
    ops.node(91000, 5.97126733, 11.23863427, 3.15)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.3)
    ops.node(12002, 3.1, 0.0, 6.3)
    ops.node(12003, 7.35, 0.0, 6.3)
    ops.node(12004, 11.6, 0.0, 6.3)
    ops.node(12005, 0.0, 4.4, 6.3)
    ops.node(12006, 3.1, 4.4, 6.3)
    ops.node(12007, 7.35, 4.4, 6.3)
    ops.node(12008, 11.6, 4.4, 6.3)
    ops.node(12009, 0.0, 8.8, 6.3)
    ops.node(12010, 3.1, 8.8, 6.3)
    ops.node(12011, 7.35, 8.8, 6.3)
    ops.node(12012, 11.6, 8.8, 6.3)
    ops.node(12013, 0.0, 13.2, 6.3)
    ops.node(12014, 3.1, 13.2, 6.3)
    ops.node(12015, 7.35, 13.2, 6.3)
    ops.node(12016, 11.6, 13.2, 6.3)
    ops.node(12017, 0.0, 17.6, 6.3)
    ops.node(12018, 3.1, 17.6, 6.3)
    ops.node(12019, 7.35, 17.6, 6.3)
    ops.node(12020, 11.6, 17.6, 6.3)
    ops.node(12021, 0.0, 22.0, 6.3)
    ops.node(12022, 3.1, 22.0, 6.3)
    ops.node(12023, 7.35, 22.0, 6.3)
    ops.node(12024, 11.6, 22.0, 6.3)
    # Retained floor node
    ops.node(92000, 5.96943726, 11.2426504, 6.3)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.45)
    ops.node(13002, 3.1, 0.0, 9.45)
    ops.node(13003, 7.35, 0.0, 9.45)
    ops.node(13004, 11.6, 0.0, 9.45)
    ops.node(13005, 0.0, 4.4, 9.45)
    ops.node(13006, 3.1, 4.4, 9.45)
    ops.node(13007, 7.35, 4.4, 9.45)
    ops.node(13008, 11.6, 4.4, 9.45)
    ops.node(13009, 0.0, 8.8, 9.45)
    ops.node(13010, 3.1, 8.8, 9.45)
    ops.node(13011, 7.35, 8.8, 9.45)
    ops.node(13012, 11.6, 8.8, 9.45)
    ops.node(13013, 0.0, 13.2, 9.45)
    ops.node(13014, 3.1, 13.2, 9.45)
    ops.node(13015, 7.35, 13.2, 9.45)
    ops.node(13016, 11.6, 13.2, 9.45)
    ops.node(13017, 0.0, 17.6, 9.45)
    ops.node(13018, 3.1, 17.6, 9.45)
    ops.node(13019, 7.35, 17.6, 9.45)
    ops.node(13020, 11.6, 17.6, 9.45)
    ops.node(13021, 0.0, 22.0, 9.45)
    ops.node(13022, 3.1, 22.0, 9.45)
    ops.node(13023, 7.35, 22.0, 9.45)
    ops.node(13024, 11.6, 22.0, 9.45)
    # Retained floor node
    ops.node(93000, 5.96720177, 11.22894681, 9.45)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.6)
    ops.node(14002, 3.1, 0.0, 12.6)
    ops.node(14003, 7.35, 0.0, 12.6)
    ops.node(14004, 11.6, 0.0, 12.6)
    ops.node(14005, 0.0, 4.4, 12.6)
    ops.node(14006, 3.1, 4.4, 12.6)
    ops.node(14007, 7.35, 4.4, 12.6)
    ops.node(14008, 11.6, 4.4, 12.6)
    ops.node(14009, 0.0, 8.8, 12.6)
    ops.node(14010, 3.1, 8.8, 12.6)
    ops.node(14011, 7.35, 8.8, 12.6)
    ops.node(14012, 11.6, 8.8, 12.6)
    ops.node(14013, 0.0, 13.2, 12.6)
    ops.node(14014, 3.1, 13.2, 12.6)
    ops.node(14015, 7.35, 13.2, 12.6)
    ops.node(14016, 11.6, 13.2, 12.6)
    ops.node(14017, 0.0, 17.6, 12.6)
    ops.node(14018, 3.1, 17.6, 12.6)
    ops.node(14019, 7.35, 17.6, 12.6)
    ops.node(14020, 11.6, 17.6, 12.6)
    ops.node(14021, 0.0, 22.0, 12.6)
    ops.node(14022, 3.1, 22.0, 12.6)
    ops.node(14023, 7.35, 22.0, 12.6)
    ops.node(14024, 11.6, 22.0, 12.6)
    # Retained floor node
    ops.node(94000, 5.99832988, 11.25844082, 12.6)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
