import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 2.9)
    ops.node(11002, 5.3, 0.0, 2.9)
    ops.node(11003, 10.6, 0.0, 2.9)
    ops.node(11004, 13.45, 0.0, 2.9)
    ops.node(11005, 18.75, 0.0, 2.9)
    ops.node(11006, 24.05, 0.0, 2.9)
    ops.node(11007, 0.0, 4.25, 2.9)
    ops.node(11008, 5.3, 4.25, 2.9)
    ops.node(11009, 10.6, 4.25, 2.9)
    ops.node(11010, 13.45, 4.25, 2.9)
    ops.node(11011, 18.75, 4.25, 2.9)
    ops.node(11012, 24.05, 4.25, 2.9)
    ops.node(11013, 0.0, 8.5, 2.9)
    ops.node(11014, 5.3, 8.5, 2.9)
    ops.node(11015, 10.6, 8.5, 2.9)
    ops.node(11016, 13.45, 8.5, 2.9)
    ops.node(11017, 18.75, 8.5, 2.9)
    ops.node(11018, 24.05, 8.5, 2.9)
    ops.node(11019, 0.0, 12.75, 2.9)
    ops.node(11020, 5.3, 12.75, 2.9)
    ops.node(11021, 10.6, 12.75, 2.9)
    ops.node(11022, 13.45, 12.75, 2.9)
    ops.node(11023, 18.75, 12.75, 2.9)
    ops.node(11024, 24.05, 12.75, 2.9)
    # Retained floor node
    ops.node(91000, 12.025, 6.39824803, 2.9)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 5.8)
    ops.node(12002, 5.3, 0.0, 5.8)
    ops.node(12003, 10.6, 0.0, 5.8)
    ops.node(12004, 13.45, 0.0, 5.8)
    ops.node(12005, 18.75, 0.0, 5.8)
    ops.node(12006, 24.05, 0.0, 5.8)
    ops.node(12007, 0.0, 4.25, 5.8)
    ops.node(12008, 5.3, 4.25, 5.8)
    ops.node(12009, 10.6, 4.25, 5.8)
    ops.node(12010, 13.45, 4.25, 5.8)
    ops.node(12011, 18.75, 4.25, 5.8)
    ops.node(12012, 24.05, 4.25, 5.8)
    ops.node(12013, 0.0, 8.5, 5.8)
    ops.node(12014, 5.3, 8.5, 5.8)
    ops.node(12015, 10.6, 8.5, 5.8)
    ops.node(12016, 13.45, 8.5, 5.8)
    ops.node(12017, 18.75, 8.5, 5.8)
    ops.node(12018, 24.05, 8.5, 5.8)
    ops.node(12019, 0.0, 12.75, 5.8)
    ops.node(12020, 5.3, 12.75, 5.8)
    ops.node(12021, 10.6, 12.75, 5.8)
    ops.node(12022, 13.45, 12.75, 5.8)
    ops.node(12023, 18.75, 12.75, 5.8)
    ops.node(12024, 24.05, 12.75, 5.8)
    # Retained floor node
    ops.node(92000, 12.025, 6.39663192, 5.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 8.7)
    ops.node(13002, 5.3, 0.0, 8.7)
    ops.node(13003, 10.6, 0.0, 8.7)
    ops.node(13004, 13.45, 0.0, 8.7)
    ops.node(13005, 18.75, 0.0, 8.7)
    ops.node(13006, 24.05, 0.0, 8.7)
    ops.node(13007, 0.0, 4.25, 8.7)
    ops.node(13008, 5.3, 4.25, 8.7)
    ops.node(13009, 10.6, 4.25, 8.7)
    ops.node(13010, 13.45, 4.25, 8.7)
    ops.node(13011, 18.75, 4.25, 8.7)
    ops.node(13012, 24.05, 4.25, 8.7)
    ops.node(13013, 0.0, 8.5, 8.7)
    ops.node(13014, 5.3, 8.5, 8.7)
    ops.node(13015, 10.6, 8.5, 8.7)
    ops.node(13016, 13.45, 8.5, 8.7)
    ops.node(13017, 18.75, 8.5, 8.7)
    ops.node(13018, 24.05, 8.5, 8.7)
    ops.node(13019, 0.0, 12.75, 8.7)
    ops.node(13020, 5.3, 12.75, 8.7)
    ops.node(13021, 10.6, 12.75, 8.7)
    ops.node(13022, 13.45, 12.75, 8.7)
    ops.node(13023, 18.75, 12.75, 8.7)
    ops.node(13024, 24.05, 12.75, 8.7)
    # Retained floor node
    ops.node(93000, 12.025, 6.39532778, 8.7)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 11.6)
    ops.node(14002, 5.3, 0.0, 11.6)
    ops.node(14003, 10.6, 0.0, 11.6)
    ops.node(14004, 13.45, 0.0, 11.6)
    ops.node(14005, 18.75, 0.0, 11.6)
    ops.node(14006, 24.05, 0.0, 11.6)
    ops.node(14007, 0.0, 4.25, 11.6)
    ops.node(14008, 5.3, 4.25, 11.6)
    ops.node(14009, 10.6, 4.25, 11.6)
    ops.node(14010, 13.45, 4.25, 11.6)
    ops.node(14011, 18.75, 4.25, 11.6)
    ops.node(14012, 24.05, 4.25, 11.6)
    ops.node(14013, 0.0, 8.5, 11.6)
    ops.node(14014, 5.3, 8.5, 11.6)
    ops.node(14015, 10.6, 8.5, 11.6)
    ops.node(14016, 13.45, 8.5, 11.6)
    ops.node(14017, 18.75, 8.5, 11.6)
    ops.node(14018, 24.05, 8.5, 11.6)
    ops.node(14019, 0.0, 12.75, 11.6)
    ops.node(14020, 5.3, 12.75, 11.6)
    ops.node(14021, 10.6, 12.75, 11.6)
    ops.node(14022, 13.45, 12.75, 11.6)
    ops.node(14023, 18.75, 12.75, 11.6)
    ops.node(14024, 24.05, 12.75, 11.6)
    # Retained floor node
    ops.node(94000, 12.025, 6.44773361, 11.6)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
