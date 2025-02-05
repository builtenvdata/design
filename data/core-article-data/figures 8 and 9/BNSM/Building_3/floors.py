import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (nodes & diaphrams).
    """
    # Floor no. 1
    # Constrained floor nodes
    ops.node(11001, 0.0, 0.0, 3.2)
    ops.node(11002, 7.4, 0.0, 3.2)
    ops.node(11003, 14.8, 0.0, 3.2)
    ops.node(11004, 17.8, 0.0, 3.2)
    ops.node(11005, 25.2, 0.0, 3.2)
    ops.node(11006, 32.6, 0.0, 3.2)
    ops.node(11007, 0.0, 3.5, 3.2)
    ops.node(11008, 7.4, 3.5, 3.2)
    ops.node(11009, 14.8, 3.5, 3.2)
    ops.node(11010, 17.8, 3.5, 3.2)
    ops.node(11011, 25.2, 3.5, 3.2)
    ops.node(11012, 32.6, 3.5, 3.2)
    ops.node(11013, 0.0, 7.0, 3.2)
    ops.node(11014, 7.4, 7.0, 3.2)
    ops.node(11015, 14.8, 7.0, 3.2)
    ops.node(11016, 17.8, 7.0, 3.2)
    ops.node(11017, 25.2, 7.0, 3.2)
    ops.node(11018, 32.6, 7.0, 3.2)
    ops.node(11019, 0.0, 10.5, 3.2)
    ops.node(11020, 7.4, 10.5, 3.2)
    ops.node(11021, 14.8, 10.5, 3.2)
    ops.node(11022, 17.8, 10.5, 3.2)
    ops.node(11023, 25.2, 10.5, 3.2)
    ops.node(11024, 32.6, 10.5, 3.2)
    # Retained floor node
    ops.node(91000, 16.3, 5.28277371, 3.2)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 91000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11011, 11012, 11013, 11014, 11015, 11016, 11017, 11018, 11019, 11020, 11021, 11022, 11023, 11024)
    # Fix the floating dofs of the retained node
    ops.fix(91000, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Constrained floor nodes
    ops.node(12001, 0.0, 0.0, 6.4)
    ops.node(12002, 7.4, 0.0, 6.4)
    ops.node(12003, 14.8, 0.0, 6.4)
    ops.node(12004, 17.8, 0.0, 6.4)
    ops.node(12005, 25.2, 0.0, 6.4)
    ops.node(12006, 32.6, 0.0, 6.4)
    ops.node(12007, 0.0, 3.5, 6.4)
    ops.node(12008, 7.4, 3.5, 6.4)
    ops.node(12009, 14.8, 3.5, 6.4)
    ops.node(12010, 17.8, 3.5, 6.4)
    ops.node(12011, 25.2, 3.5, 6.4)
    ops.node(12012, 32.6, 3.5, 6.4)
    ops.node(12013, 0.0, 7.0, 6.4)
    ops.node(12014, 7.4, 7.0, 6.4)
    ops.node(12015, 14.8, 7.0, 6.4)
    ops.node(12016, 17.8, 7.0, 6.4)
    ops.node(12017, 25.2, 7.0, 6.4)
    ops.node(12018, 32.6, 7.0, 6.4)
    ops.node(12019, 0.0, 10.5, 6.4)
    ops.node(12020, 7.4, 10.5, 6.4)
    ops.node(12021, 14.8, 10.5, 6.4)
    ops.node(12022, 17.8, 10.5, 6.4)
    ops.node(12023, 25.2, 10.5, 6.4)
    ops.node(12024, 32.6, 10.5, 6.4)
    # Retained floor node
    ops.node(92000, 16.3, 5.27989405, 6.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 92000, 12001, 12002, 12003, 12004, 12005, 12006, 12007, 12008, 12009, 12010, 12011, 12012, 12013, 12014, 12015, 12016, 12017, 12018, 12019, 12020, 12021, 12022, 12023, 12024)
    # Fix the floating dofs of the retained node
    ops.fix(92000, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Constrained floor nodes
    ops.node(13001, 0.0, 0.0, 9.6)
    ops.node(13002, 7.4, 0.0, 9.6)
    ops.node(13003, 14.8, 0.0, 9.6)
    ops.node(13004, 17.8, 0.0, 9.6)
    ops.node(13005, 25.2, 0.0, 9.6)
    ops.node(13006, 32.6, 0.0, 9.6)
    ops.node(13007, 0.0, 3.5, 9.6)
    ops.node(13008, 7.4, 3.5, 9.6)
    ops.node(13009, 14.8, 3.5, 9.6)
    ops.node(13010, 17.8, 3.5, 9.6)
    ops.node(13011, 25.2, 3.5, 9.6)
    ops.node(13012, 32.6, 3.5, 9.6)
    ops.node(13013, 0.0, 7.0, 9.6)
    ops.node(13014, 7.4, 7.0, 9.6)
    ops.node(13015, 14.8, 7.0, 9.6)
    ops.node(13016, 17.8, 7.0, 9.6)
    ops.node(13017, 25.2, 7.0, 9.6)
    ops.node(13018, 32.6, 7.0, 9.6)
    ops.node(13019, 0.0, 10.5, 9.6)
    ops.node(13020, 7.4, 10.5, 9.6)
    ops.node(13021, 14.8, 10.5, 9.6)
    ops.node(13022, 17.8, 10.5, 9.6)
    ops.node(13023, 25.2, 10.5, 9.6)
    ops.node(13024, 32.6, 10.5, 9.6)
    # Retained floor node
    ops.node(93000, 16.3, 5.27696945, 9.6)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 93000, 13001, 13002, 13003, 13004, 13005, 13006, 13007, 13008, 13009, 13010, 13011, 13012, 13013, 13014, 13015, 13016, 13017, 13018, 13019, 13020, 13021, 13022, 13023, 13024)
    # Fix the floating dofs of the retained node
    ops.fix(93000, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Constrained floor nodes
    ops.node(14001, 0.0, 0.0, 12.8)
    ops.node(14002, 7.4, 0.0, 12.8)
    ops.node(14003, 14.8, 0.0, 12.8)
    ops.node(14004, 17.8, 0.0, 12.8)
    ops.node(14005, 25.2, 0.0, 12.8)
    ops.node(14006, 32.6, 0.0, 12.8)
    ops.node(14007, 0.0, 3.5, 12.8)
    ops.node(14008, 7.4, 3.5, 12.8)
    ops.node(14009, 14.8, 3.5, 12.8)
    ops.node(14010, 17.8, 3.5, 12.8)
    ops.node(14011, 25.2, 3.5, 12.8)
    ops.node(14012, 32.6, 3.5, 12.8)
    ops.node(14013, 0.0, 7.0, 12.8)
    ops.node(14014, 7.4, 7.0, 12.8)
    ops.node(14015, 14.8, 7.0, 12.8)
    ops.node(14016, 17.8, 7.0, 12.8)
    ops.node(14017, 25.2, 7.0, 12.8)
    ops.node(14018, 32.6, 7.0, 12.8)
    ops.node(14019, 0.0, 10.5, 12.8)
    ops.node(14020, 7.4, 10.5, 12.8)
    ops.node(14021, 14.8, 10.5, 12.8)
    ops.node(14022, 17.8, 10.5, 12.8)
    ops.node(14023, 25.2, 10.5, 12.8)
    ops.node(14024, 32.6, 10.5, 12.8)
    # Retained floor node
    ops.node(94000, 16.3, 5.30229973, 12.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 94000, 14001, 14002, 14003, 14004, 14005, 14006, 14007, 14008, 14009, 14010, 14011, 14012, 14013, 14014, 14015, 14016, 14017, 14018, 14019, 14020, 14021, 14022, 14023, 14024)
    # Fix the floating dofs of the retained node
    ops.fix(94000, 0, 0, 1, 1, 1, 0)
