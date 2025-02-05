import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.65)
    ops.node(11002, 5.8, 0.0, 3.65)
    ops.node(11003, 11.6, 0.0, 3.65)
    ops.node(11004, 17.4, 0.0, 3.65)
    ops.node(11005, 20.2, 0.0, 3.65)
    ops.node(11006, 26.0, 0.0, 3.65)
    ops.node(11007, 31.8, 0.0, 3.65)
    ops.node(11008, 37.6, 0.0, 3.65)
    ops.node(11009, 0.0, 4.75, 3.65)
    ops.node(11010, 5.8, 4.75, 3.65)
    ops.node(11011, 11.6, 4.75, 3.65)
    ops.node(11012, 17.4, 4.75, 3.65)
    ops.node(11013, 20.2, 4.75, 3.65)
    ops.node(11014, 26.0, 4.75, 3.65)
    ops.node(11015, 31.8, 4.75, 3.65)
    ops.node(11016, 37.6, 4.75, 3.65)
    ops.node(11017, 0.0, 9.5, 3.65)
    ops.node(11018, 5.8, 9.5, 3.65)
    ops.node(11019, 11.6, 9.5, 3.65)
    ops.node(11020, 17.4, 9.5, 3.65)
    ops.node(11021, 20.2, 9.5, 3.65)
    ops.node(11022, 26.0, 9.5, 3.65)
    ops.node(11023, 31.8, 9.5, 3.65)
    ops.node(11024, 37.6, 9.5, 3.65)
    # Retained floor node
    ops.node(91000, 18.8, 4.78023141, 3.65)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.45)
    ops.node(12002, 5.8, 0.0, 6.45)
    ops.node(12003, 11.6, 0.0, 6.45)
    ops.node(12004, 17.4, 0.0, 6.45)
    ops.node(12005, 20.2, 0.0, 6.45)
    ops.node(12006, 26.0, 0.0, 6.45)
    ops.node(12007, 31.8, 0.0, 6.45)
    ops.node(12008, 37.6, 0.0, 6.45)
    ops.node(12009, 0.0, 4.75, 6.45)
    ops.node(12010, 5.8, 4.75, 6.45)
    ops.node(12011, 11.6, 4.75, 6.45)
    ops.node(12012, 17.4, 4.75, 6.45)
    ops.node(12013, 20.2, 4.75, 6.45)
    ops.node(12014, 26.0, 4.75, 6.45)
    ops.node(12015, 31.8, 4.75, 6.45)
    ops.node(12016, 37.6, 4.75, 6.45)
    ops.node(12017, 0.0, 9.5, 6.45)
    ops.node(12018, 5.8, 9.5, 6.45)
    ops.node(12019, 11.6, 9.5, 6.45)
    ops.node(12020, 17.4, 9.5, 6.45)
    ops.node(12021, 20.2, 9.5, 6.45)
    ops.node(12022, 26.0, 9.5, 6.45)
    ops.node(12023, 31.8, 9.5, 6.45)
    ops.node(12024, 37.6, 9.5, 6.45)
    # Retained floor node
    ops.node(92000, 18.8, 4.7808191, 6.45)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.25)
    ops.node(13002, 5.8, 0.0, 9.25)
    ops.node(13003, 11.6, 0.0, 9.25)
    ops.node(13004, 17.4, 0.0, 9.25)
    ops.node(13005, 20.2, 0.0, 9.25)
    ops.node(13006, 26.0, 0.0, 9.25)
    ops.node(13007, 31.8, 0.0, 9.25)
    ops.node(13008, 37.6, 0.0, 9.25)
    ops.node(13009, 0.0, 4.75, 9.25)
    ops.node(13010, 5.8, 4.75, 9.25)
    ops.node(13011, 11.6, 4.75, 9.25)
    ops.node(13012, 17.4, 4.75, 9.25)
    ops.node(13013, 20.2, 4.75, 9.25)
    ops.node(13014, 26.0, 4.75, 9.25)
    ops.node(13015, 31.8, 4.75, 9.25)
    ops.node(13016, 37.6, 4.75, 9.25)
    ops.node(13017, 0.0, 9.5, 9.25)
    ops.node(13018, 5.8, 9.5, 9.25)
    ops.node(13019, 11.6, 9.5, 9.25)
    ops.node(13020, 17.4, 9.5, 9.25)
    ops.node(13021, 20.2, 9.5, 9.25)
    ops.node(13022, 26.0, 9.5, 9.25)
    ops.node(13023, 31.8, 9.5, 9.25)
    ops.node(13024, 37.6, 9.5, 9.25)
    # Retained floor node
    ops.node(93000, 18.8, 4.78193607, 9.25)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.05)
    ops.node(14002, 5.8, 0.0, 12.05)
    ops.node(14003, 11.6, 0.0, 12.05)
    ops.node(14004, 17.4, 0.0, 12.05)
    ops.node(14005, 20.2, 0.0, 12.05)
    ops.node(14006, 26.0, 0.0, 12.05)
    ops.node(14007, 31.8, 0.0, 12.05)
    ops.node(14008, 37.6, 0.0, 12.05)
    ops.node(14009, 0.0, 4.75, 12.05)
    ops.node(14010, 5.8, 4.75, 12.05)
    ops.node(14011, 11.6, 4.75, 12.05)
    ops.node(14012, 17.4, 4.75, 12.05)
    ops.node(14013, 20.2, 4.75, 12.05)
    ops.node(14014, 26.0, 4.75, 12.05)
    ops.node(14015, 31.8, 4.75, 12.05)
    ops.node(14016, 37.6, 4.75, 12.05)
    ops.node(14017, 0.0, 9.5, 12.05)
    ops.node(14018, 5.8, 9.5, 12.05)
    ops.node(14019, 11.6, 9.5, 12.05)
    ops.node(14020, 17.4, 9.5, 12.05)
    ops.node(14021, 20.2, 9.5, 12.05)
    ops.node(14022, 26.0, 9.5, 12.05)
    ops.node(14023, 31.8, 9.5, 12.05)
    ops.node(14024, 37.6, 9.5, 12.05)
    # Retained floor node
    ops.node(94000, 18.8, 4.81211635, 12.05)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
