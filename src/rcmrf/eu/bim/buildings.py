"""
Defines building layout
"""

import numpy as np
from scipy.interpolate import interp1d
from numpy.matlib import repmat

class General:
    
    def _pre_allocate(self, taxonomy):
        # 1) Pre-alocates all the variables coming from taxonomy (not to be edited)
        # TODO: change the variable names later to avoid this
        self.aux = 1
        self.nmodes = 6
        old_names = ['Layout', 'fsyd_EQ', 'fcd_EQ', 'Hground', 'Hupper', 'Columnorient', 'beamtype', 'slabtype', 'Beta', 'DesignClass', 'NStoreys']
        new_names = ['BuildingTYPE', 'fsydEQ', 'fcdEQ', 'hground', 'hstorey', 'ColumnType', 'BeamType', 'SlabType', 'ag', 'designlevel', 'nstoreys']
        for attribute, value in taxonomy.items():
            if attribute in old_names:
                setattr(self, new_names[old_names.index(attribute)], value)
            else:
                setattr(self, attribute, value)
        self.Ec = 9.5 * ((self.fck + 8) ** (1/3)) * 1000000
        self.G = self.Ec/(2 * (1 + 0.2))

        # Considered the different load combinations that may be applicable to 
        # CDH is from EUROCODE rest is from Portugal codes

        if self.designlevel == 'CDN':
            prcp = 2.0
            pservice = 2.0
            pconcrete = 24.0
            ppstair = pconcrete * self.Hstairs
            prcproof = 2.0
            pservice_stair = 1.5 * pservice
            # ...........................................................................
            ped = 1.00 * self.ppslab + 1.00 * prcp + 1.00 * pservice             
            ped_stair = 1.00 * ppstair + 1.00 * prcp + 1.00 * pservice_stair     
            ped_roof = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall = 1.00 * self.ppinfill
            # ...........................................................................
            ped_eq = 1.00 * self.ppslab + 1.00 * prcp
            ped_stair_eq = 1.00 * ppstair + 1.00 * prcp
            ped_roof_eq = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall_eq = 1.00 * self.ppinfill
            # ...........................................................................
            ped_eq_final = 1.00 * self.ppslab + 1.00 * prcp + 0.30 * pservice
            ped_stair_eq_final = 1.00 * ppstair + 1.00 * prcp + 0.30 * pservice_stair
            ped_roof_eq_final = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall_eq_final = 1.00 * self.ppinfill
            # ...........................................................................
            pCP = 1.00 * self.ppslab + 1.00 * prcp
            pCP_stair = 1.00 * ppstair + 1.00 * prcp
            pCP_roof = 1.00 * self.ppslab + 1.00 * prcproof
            pCP_wall = 1.00 * self.ppinfill

        elif self.designlevel == 'CDL':
            prcp = 2.0
            pservice = 2.0
            pconcrete = 24.0
            ppstair = pconcrete * self.Hstairs
            prcproof = 2.0
            pservice_stair = 1.5 * pservice
            # ...........................................................................
            ped = 1.50 * self.ppslab + 1.50 * prcp + 1.50 * pservice             
            ped_stair = 1.50 * ppstair + 1.50 * prcp + 1.50 * pservice_stair     
            ped_roof = 1.50 * self.ppslab + 1.50 * prcproof
            ped_wall = 1.50 * self.ppinfill
            # ...........................................................................
            ped_eq = 1.00 * self.ppslab + 1.00 * prcp + 1.00 * pservice             
            ped_stair_eq = 1.00 * ppstair + 1.00 * prcp + 1.00 * pservice_stair     
            ped_roof_eq = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall_eq = 1.00 * self.ppinfill
            # ...........................................................................
            ped_eq_final = 1.00 * self.ppslab + 1.00 * prcp + 0.30 * pservice
            ped_stair_eq_final = 1.00 * ppstair + 1.00 * prcp + 0.30 * pservice_stair
            ped_roof_eq_final = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall_eq_final = 1.00 * self.ppinfill
            # ...........................................................................
            pCP = 1.00 * self.ppslab + 1.00 * prcp
            pCP_stair = 1.00 * ppstair + 1.00 * prcp
            pCP_roof = 1.00 * self.ppslab + 1.00 * prcproof
            pCP_wall = 1.00 * self.ppinfill

        elif self.designlevel == 'CDM':
            prcp = 2.0
            pservice = 2.0
            pconcrete = 25.0
            ppstair = pconcrete * self.Hstairs
            prcproof = 2.0
            pservice_stair = 1.5 * pservice
            # ...........................................................................
            ped = 1.50 * self.ppslab + 1.50 * prcp + 1.50 * pservice             
            ped_stair = 1.50 * ppstair + 1.50 * prcp + 1.50 * pservice_stair     
            ped_roof = 1.50 * self.ppslab + 1.50 * prcproof
            ped_wall = 1.50 * self.ppinfill
            # ...........................................................................
            ped_eq = 1.00 * self.ppslab + 1.00 * prcp + 0.30 * pservice             
            ped_stair_eq = 1.00 * ppstair + 1.00 * prcp + 0.30 * pservice_stair     
            ped_roof_eq = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall_eq = 1.00 * self.ppinfill
            # ...........................................................................
            ped_eq_final = 1.00 * self.ppslab + 1.00 * prcp + 0.30 * pservice
            ped_stair_eq_final = 1.00 * ppstair + 1.00 * prcp + 0.30 * pservice_stair
            ped_roof_eq_final = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall_eq_final = 1.00 * self.ppinfill
            # ...........................................................................
            pCP = 1.00 * self.ppslab + 1.00 * prcp
            pCP_stair = 1.00 * ppstair + 1.00 * prcp
            pCP_roof = 1.00 * self.ppslab + 1.00 * prcproof
            pCP_wall = 1.00 * self.ppinfill

        elif self.designlevel == 'CDH':
            prcp = 2.0
            pservice = 2.0
            pconcrete = 25.0
            ppstair = pconcrete * self.Hstairs
            prcproof = 2.0
            pservice_stair = 1.5 * pservice
            # ...........................................................................
            ped = 1.35 * self.ppslab + 1.35 * prcp + 1.50 * pservice             
            ped_stair = 1.35 * ppstair + 1.35 * prcp + 1.50 * pservice_stair     
            ped_roof = 1.35 * self.ppslab + 1.35 * prcproof
            ped_wall = 1.35 * self.ppinfill
            # ...........................................................................
            ped_eq = 1.00 * self.ppslab + 1.00 * prcp + 0.30 * pservice             
            ped_stair_eq = 1.00 * ppstair + 1.00 * prcp + 0.30 * pservice_stair     
            ped_roof_eq = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall_eq = 1.00 * self.ppinfill
            # ...........................................................................
            ped_eq_final = 1.00 * self.ppslab + 1.00 * prcp + 0.30 * pservice
            ped_stair_eq_final = 1.00 * ppstair + 1.00 * prcp + 0.30 * pservice_stair
            ped_roof_eq_final = 1.00 * self.ppslab + 1.00 * prcproof
            ped_wall_eq_final = 1.00 * self.ppinfill
            # ...........................................................................
            pCP = 1.00 * self.ppslab + 1.00 * prcp
            pCP_stair = 1.00 * ppstair + 1.00 * prcp
            pCP_roof = 1.00 * self.ppslab + 1.00 * prcproof
            pCP_wall = 1.00 * self.ppinfill

        # 2) Pre-alocates all the loads: GENERAL (not to be edited)
        self.prcp = prcp
        self.pservice_all = pservice
        self.pconcrete = pconcrete
        self.ppstair = ppstair
        self.prcproof = prcproof
        self.pservice_stair = pservice_stair
        # ...........................................................................
        self.ped = ped     
        self.pedstair = ped_stair
        self.pedroof = ped_roof
        self.pedwall = ped_wall
        # ...........................................................................
        self.pedEQ = ped_eq            
        self.pedstairEQ = ped_stair_eq    
        self.pedroofEQ = ped_roof_eq
        self.pedwallEQ = ped_wall_eq
        # ...........................................................................
        self.pedEQfinal = ped_eq_final
        self.pedstairEQfinal = ped_stair_eq_final
        self.pedroofEQfinal = ped_roof_eq_final
        self.pedwallEQfinal = ped_wall_eq_final
        # ...........................................................................
        self.pCP = pCP
        self.pCPstair = pCP_stair
        self.pCProof = pCP_roof
        self.pCPwall = pCP_wall

        # 3) Pre-alocates some flags
        self.CvFLAGX = -100
        self.CvFLAGY = -100
        self.CvFLAGstair = -100
        self.CvFLAG = -100
        self.CpFLAG = -100
        self.CpM = -100
        self.designiteration = 1


class Column:
        
    def update_mechanical_properties(self):
        self.Area = self.HX * self.HY
        self.IX = (self.HY * self.HX ** 3)/12
        self.IY = (self.HX * self.HY ** 3)/12
        minH = np.minimum(self.HX, self.HY)
        maxH = np.maximum(self.HX, self.HY)
        self.J = (maxH * minH ** 3) * (1/3 - 0.21 * (minH / maxH) * (1 - (minH ** 4 / (12*maxH ** 4))))


class Beam:

    def update_mechanical_properties(self):
        self.Area = self.B * self.H
        self.IY = (self.H * self.B ** 3)/12
        self.IZ = (self.B * self.H ** 3)/12
        minHB = np.minimum(self.B, self.H)
        maxHB = np.maximum(self.B, self.H)
        self.J = (maxHB * minHB ** 3) * (1/3 - 0.21 * (minHB / maxHB) * (1 - (minHB ** 4 / (12*maxHB ** 4))))


def _get_alpha_load(a_over_l):
    """
    Computes loading coefficient used to distribute slab loads on beams

    References:
        d'Arga e Lima, J., Monteiro, V., Mun,. M. (1997) Betão Armado, Esforços Normais e de Flexão, 3rd Ed. 
        Laboratório Nacional de Engenharia Civil, Lisboa.

    Args:
        a_over_l (numpy.ndarray): ratios of short spans to longer spans

    Returns:
        numpy.ndarray: loading coefficient used to distribute slab loads on beams
    """
    a_over_l_ref = np.arange(0, 0.55, 0.05)
    alpha_ref = np.array([1.000, 0.9967, 0.9867, 0.97, 0.9467, 0.9167, 0.88, 0.8367, 0.7867, 0.73, 0.6667])
    alpha_load = np.zeros(len(a_over_l))
    alpha_load[a_over_l > 0.50] = 0.6667
    alpha_load[a_over_l <= 0.50] = interp1d(a_over_l_ref, alpha_ref)(a_over_l[a_over_l <= 0.50])

    return alpha_load


class LayoutManager:
    """Used to define attributes necessary for completing the design.
    """

    def __init__(self):
        """Initialise the main objects for the building

        Args:
            taxonomy (dict): building taxonomy information
        """
        self.general = General()
        self.beamX = Beam()
        self.beamY = Beam()
        self.beamStair = Beam()
        self.column = Column()


    def make_layout(self, taxonomy: dict):
        """
        Pre-allocates taxonomy variables.
        Defines beam and column nodes.
        """
        ## Pre-allocate variables
        self.general._pre_allocate(taxonomy)

        ## Perform layout-specific calculations
        # TODO try to make this a single function with several inputs (HOSSAM), discuss the potential inputs for the function
        # For now we run the associated layout method based on user input
        getattr(self, f"_{self.general.BuildingTYPE.lower()}")()

        ## Perform general calculations
        self.general.noderef = self.general.Reference.copy()  # always use copy, since the numpy arrays are mutable
        self.general.heightvector = np.array([self.general.hground] + [self.general.hstorey] * (self.general.nstoreys - 1))
        self.general.Zvector = np.append(0, np.cumsum(self.general.heightvector))
        self.general.Coords = repmat(self.general.Plan, self.general.nstoreys + 1, 1)
        aux = self.general.Plan.shape[0]
        Zcoords = np.zeros((self.general.Coords.shape[0],1))
        Name = np.zeros((self.general.Coords.shape[0],1))
        for i in range(len(self.general.Zvector)):
            Zcoords[i*aux:(i+1)*aux] = self.general.Zvector[i]
            Name[i*aux:(i+1)*aux] = i * 100 + self.general.Reference.reshape(-1,1)
        self.general.Coords = np.append(self.general.Coords, Zcoords, axis=1)
        Coords = np.append(Name, self.general.Coords, axis=1)
        CoordsExtra1 = np.zeros((self.general.heightvector.shape[0], 4))
        CoordsExtra2 = np.zeros((self.general.heightvector.shape[0], 4))
        for i in range(self.general.heightvector.shape[0]):
            CoordsExtra1[i,:] = np.array([20000+(i+1)*100+self.general.stair_node_left_mirror_1st_storey,
                                          self.general.stairXleft, self.general.stairY,
                                          np.sum(self.general.heightvector[:i]) + self.general.heightvector[i]/2])
            CoordsExtra2[i,:] = np.array([20000+(i+1)*100+self.general.stair_node_right_mirror_1st_storey,
                                          self.general.stairXright, self.general.stairY,
                                          np.sum(self.general.heightvector[:i]) + self.general.heightvector[i]/2])

        self.general.Coordsref = np.vstack((Coords, CoordsExtra1, CoordsExtra2))
        self.general.Coordsref = np.round(self.general.Coordsref, 10)
        self.general.CoordsExtra1 = np.round(CoordsExtra1, 10)
        self.general.CoordsExtra2 = np.round(CoordsExtra2, 10)

        self.beamX.Ainf3 = repmat(self.beamX.Ainf3, self.general.nstoreys, 1)
        self.beamX.alpha = repmat(self.beamX.alpha, self.general.nstoreys, 1)
        self.beamX.Astair3 = repmat(self.beamX.Astair3, self.general.nstoreys, 1)
        self.beamX.Ainf2 = repmat(self.beamX.Ainf2, self.general.nstoreys, 1)
        self.beamX.Astair2 = repmat(self.beamX.Astair2, self.general.nstoreys, 1)
        self.beamX.Ainf1 = repmat(self.beamX.Ainf1, self.general.nstoreys, 1)
        self.beamX.Astair1 = repmat(self.beamX.Astair1, self.general.nstoreys, 1)
        self.beamX.L = repmat(self.beamX.L, self.general.nstoreys, 1)
        self.beamX.name = self.beamX.beamXnameref[:self.general.nstoreys, :]
        self.beamX.elasnodei = self.beamX.elasXnodeiref[:self.general.nstoreys, :]
        self.beamX.elasnodej = self.beamX.elasXnodejref[:self.general.nstoreys, :]

        self.beamStair.Ainf3 = repmat(self.beamStair.Ainf3, self.general.nstoreys, 1)
        self.beamStair.Astair3 = repmat(self.beamStair.Astair3, self.general.nstoreys, 1)
        self.beamStair.Ainf2 = repmat(self.beamStair.Ainf2, self.general.nstoreys, 1)
        self.beamStair.Astair2 = repmat(self.beamStair.Astair2, self.general.nstoreys, 1)
        self.beamStair.Ainf1 = repmat(self.beamStair.Ainf1, self.general.nstoreys, 1)
        self.beamStair.Astair1 = repmat(self.beamStair.Astair1, self.general.nstoreys, 1)
        self.beamStair.L = repmat(self.beamStair.L, self.general.nstoreys, 1)
        self.beamStair.name = self.beamStair.beamStairnameref[:self.general.nstoreys, :]
        self.beamStair.elasnodei = self.beamStair.elasStairnodeiref[:self.general.nstoreys, :]
        self.beamStair.elasnodej = self.beamStair.elasStairnodejref[:self.general.nstoreys, :]

        self.beamY.Ainf3 = repmat(self.beamY.Ainf3, self.general.nstoreys, 1)
        self.beamY.alpha = repmat(self.beamY.alpha, self.general.nstoreys, 1)
        self.beamY.Astair3 = repmat(self.beamY.Astair3, self.general.nstoreys, 1)
        self.beamY.Ainf2 = repmat(self.beamY.Ainf2, self.general.nstoreys, 1)
        self.beamY.Astair2 = repmat(self.beamY.Astair2, self.general.nstoreys, 1)
        self.beamY.Ainf1 = repmat(self.beamY.Ainf1, self.general.nstoreys, 1)
        self.beamY.Astair1 = repmat(self.beamY.Astair1, self.general.nstoreys, 1)
        self.beamY.L = repmat(self.beamY.L, self.general.nstoreys, 1)
        self.beamY.name = self.beamY.beamYnameref[:self.general.nstoreys, :]
        self.beamY.elasnodei = self.beamY.elasYnodeiref[:self.general.nstoreys, :]
        self.beamY.elasnodej = self.beamY.elasYnodejref[:self.general.nstoreys, :]

        self.column.Ainfref = repmat(self.column.Ainfref, 8, 1)
        self.column.Aroofref = repmat(self.column.Aroofref, 8, 1)
        self.column.Astairref = repmat(self.column.Astairref, 8, 1)
        self.column.name = self.column.nameref[:self.general.nstoreys, :]
        self.column.elasnodei = self.column.elasCnodeiref[:self.general.nstoreys, :]
        self.column.elasnodej = self.column.elasCnodejref[:self.general.nstoreys, :]
        self.column.Ainf = self.column.Ainfref[:self.general.nstoreys, :]
        self.column.Astair = self.column.Astairref[:self.general.nstoreys, :]
        self.column.Aroof = self.column.Aroofref[:self.general.nstoreys, :]
        self.column.walllength = repmat(self.column.walllength, self.general.nstoreys, 1)
        aa = self.column.Lref * self.general.hstorey
        bb = self.column.Lref * self.general.hground
        aauxi = repmat(aa, self.general.nstoreys - 1, 1)
        self.column.L = np.vstack((bb, aauxi))
        aux = round(self.general.nstoreys/2 + 1e-8) # add 1e-8 because Python3.x rounds to the even values (https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior)
        self.column.positionfactor = np.vstack((repmat(self.column.positionfactor_ref[0,:], aux, 1),
                                                repmat(self.column.positionfactor_ref[1,:], self.general.nstoreys - aux, 1)))
        self.column.storeyfactor = np.ones((self.general.nstoreys, self.column.elasCnodeiref.shape[1]))
        self.column.storeyfactor = np.flip(np.arange(self.general.nstoreys)).reshape(-1,1) * self.column.storeyfactor
        self.column.rooffactor = np.ones((self.general.nstoreys, self.column.elasCnodeiref.shape[1]))

        # TODO: Indexing of Python and MATLAB is different. For now I apply modifications on indices here. Fix these later on.
        self.column.Colindex1 -= 1
        self.column.Colindex2 -= 1
        self.beamX.index -= 1
        self.beamY.index -= 1


    def _b01(self):
        """
        Building B01 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B01 - Needs to be changed for different buildings
        self.general.number_of_alignmentsX = 3
        self.general.number_of_alignmentsY = 4
        self.general.Reference = np.arange(1,13)

        # 2) Plan configuration (first incr all in X then in Y)
        self.general.Plan = np.array([[0, 0], [ax, 0], [ax + astair, 0], [ax + astair + ax, 0], 
                              [0, ay], [ax, ay], [ax + astair, ay], [ax + astair + ax, ay], 
                              [0, 2*ay], [ax, 2*ay], [ax + astair, 2*ay], [ax + astair + ax, 2*ay]])

        # 3) Column names including the two-sub-columns of the staircase
        self.column.nameref = np.array([[101, 102, 20102, 103, 20103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
                                        [201, 202, 20202, 203, 20203, 204, 205, 206, 207, 208, 209, 210, 211, 212],
                                        [301, 302, 20302, 303, 20303, 304, 305, 306, 307, 308, 309, 310, 311, 312],
                                        [401, 402, 20402, 403, 20403, 404, 405, 406, 407, 408, 409, 410, 411, 412],
                                        [501, 502, 20502, 503, 20503, 504, 505, 506, 507, 508, 509, 510, 511, 512],
                                        [601, 602, 20602, 603, 20603, 604, 605, 606, 607, 608, 609, 610, 611, 612],
                                        [701, 702, 20702, 703, 20703, 704, 705, 706, 707, 708, 709, 710, 711, 712],
                                        [801, 802, 20802, 803, 20803, 804, 805, 806, 807, 808, 809, 810, 811, 812]], dtype='int')

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        self.column.elasCnodeiref = np.array([[  1,   2, 20102,   3, 20103,   4,   5,   6,   7,   8,   9,  10,  11,  12], # 1102 is the half height node for the staircase beam
                                              [101, 102, 20202, 103, 20203, 104, 105, 106, 107, 108, 109, 110, 111, 112],
                                              [201, 202, 20302, 203, 20303, 204, 205, 206, 207, 208, 209, 210, 211, 212],
                                              [301, 302, 20402, 303, 20403, 304, 305, 306, 307, 308, 309, 310, 311, 312],
                                              [401, 402, 20502, 403, 20503, 404, 405, 406, 407, 408, 409, 410, 411, 412],
                                              [501, 502, 20602, 503, 20603, 504, 505, 506, 507, 508, 509, 510, 511, 512],
                                              [601, 602, 20702, 603, 20703, 604, 605, 606, 607, 608, 609, 610, 611, 612],
                                              [701, 702, 20802, 703, 20803, 704, 705, 706, 707, 708, 709, 710, 711, 712]], dtype='int')
        
        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        self.column.elasCnodejref = np.array([[101, 20102, 102, 20103, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112], # 1102 is the half height node for the staircase beam
                                              [201, 20202, 202, 20203, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212],
                                              [301, 20302, 302, 20303, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312],
                                              [401, 20402, 402, 20403, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412],
                                              [501, 20502, 502, 20503, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512],
                                              [601, 20602, 602, 20603, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612],
                                              [701, 20702, 702, 20703, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712],
                                              [801, 20802, 802, 20803, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812]], dtype='int') 

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        self.column.Ainfref = np.array([(ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay), 
                                        (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay),
                                        (ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................       
        self.column.Astairref = np.array([0, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0])
        # ...........................................................................
        self.column.Aroofref = np.array([(ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2),
                                         (ax/2)*(ay/2), (ax/2)*(ay), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2),
                                         (ax/2)*(ay), (ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................        
        self.column.positionfactor_ref = np.array([[1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.3], # bottom storeys 1.3 for periferic and 1.1 for central
                                                   [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.5]]) # top storeys 1.5 for periferic and 1.3 for central
        # ...........................................................................
        self.column.Colindex1 = np.array([1, 6, 7, 10, 11, 14], dtype='int')
        self.column.Colindex2 = np.array([2, 3, 4, 5, 8, 9, 12, 13], dtype='int')
        self.column.Lref = np.array([1, 0.50, 0.50, 0.50, 0.50, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        # ...........................................................................
        self.column.walllength = np.array([ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, 0, ay/2, ay/2, 0, ax/2+ay/2, ax/2+astair/2, ax/2+astair/2, ax/2+ay/2])
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 2
        self.general.stair_node_right_mirror_1st_storey = 3
        self.general.stairXleft = ax
        self.general.stairXright = ax + astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([2, 2, 2, 3, 3, 3, 4, 4, 4], dtype='int') # to define the different continuous beams
        self.beamY.index = np.array([2, 3, 4, 5, 2, 3, 4, 5], dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50110)  # beamX names
        self.beamY.auxvY = np.arange(50151, 50159)  # beamY names
        self.beamStair.auxvStair = 51102  # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([101, 102, 103, 105, 106, 107, 109, 110, 111], dtype='int')
        self.beamY.auxvY1 = np.array([101, 102, 103, 104, 105, 106, 107, 108], dtype='int')
        self.beamStair.auxvStair1 = 20102
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                            300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                            600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                            300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                            600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 4
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        self.beamX.Ainf1 = np.array([(ax)*(ay/2), 0, (ax)*(ay/2), (ax)*(ay), (astair)*(ay/2), (ax)*(ay), (ax)*(ay/2), (astair)*(ay/2), (ax)*(ay/2)])
        self.beamX.Astair1 = np.array([0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0])
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamY.Ainf1 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        self.beamY.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0])

        # Case slaborient = 2 - Unloading in Y beams
        self.beamX.Ainf2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamX.Astair2 = np.array([0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0])
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        self.beamY.Ainf2 = np.array([(ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax/2)*(ay)])
        self.beamY.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        
        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay:
            a1 = (ax-2*ay/2)*(ay/2) + 2*(ay/2)*(ay/2)/2 # influence area for beam no. 1 along -x
            a2 = 0
            a3 = a1
            a4 = 2*a1
            a5 = (astair)*(astair/2)/2
            a6 = a4
            a7 = a1
            a8 = a5
            a9 = a7
            self.beamX.Ainf3 = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])
            self.beamX.a_over_l = np.array([(ay/2)/ax, 0, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            a11 = (ay)*(ay/2)/2
            a12 = (ay)*(ay/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamY.Ainf3 = np.array([a11, a11, a11, a11, a11, a12, a12, a11])
            self.beamY.a_over_l = np.array([0.5, 0.5, 0.5, 0.5, 0.5, (astair/2)/ay, (astair/2)/ay, 0.50])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        else:
            a1 = (ax)*(ax/2)/2
            a2 = 0
            a3 = a1
            a4 = 2*a1
            a5 = (astair)*(astair/2)/2
            a6 = a4
            a7 = a1
            a8 = a5
            a9 = a7
            a11 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2
            a12 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])
            self.beamX.a_over_l = np.array([0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            self.beamY.Ainf3 = np.array([a11, a11, a11, a11, a11, a12, a12, a11])
            self.beamY.a_over_l = np.array([(ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)

        self.beamX.Astair3 = np.array([0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0])
        self.beamStair.Ainf3 = 0
        self.beamStair.Astair3 = ay/2 * astair
        self.beamY.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        
        # Dimension of the spans of the beams
        self.beamX.L = np.array([ax, astair, ax, ax, astair, ax, ax, astair, ax])
        self.beamStair.L = astair
        self.beamY.L = np.array([ay, ay, ay, ay, ay, ay, ay, ay])

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([1, 0, 1, 0, 0, 0, 1, 1, 1])
        self.beamStair.pwallsA = 0.50
        self.beamY.pwallsA = np.array([1, 1, 1, 1, 1, 0, 0, 1])

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 3, 0, 0, 4, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [1, 3, 5, 6, 7, 2, 4, 6, 7, 8]
        self.general.floor_truss_nodej_ref = [6, 8, 10, 11, 12, 5, 7, 9, 10, 11]
        self.general.roof_truss_nodei_ref = [1, 2, 3, 5, 6, 7, 2, 3, 4, 6, 7, 8]
        self.general.roof_truss_nodej_ref = [6, 7, 8, 10, 11, 12, 5, 6, 7, 9, 10, 11]
        self.general.truss_stiffness = 10000000000000 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 12 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]


    def _b02(self):
        """
        Building B02 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B02 - Needs to be changed for different buildings
        self.general.number_of_alignmentsX = 3
        self.general.number_of_alignmentsY = 6
        self.general.Reference = np.arange(1,19)
        
        # 2) Plan configuration
        self.general.Plan = np.array([[0, 0], [ax, 0], [2*ax, 0], [2*ax+astair, 0], [2*ax+astair+ax, 0], [2*ax+astair+2*ax, 0], 
                              [0, ay], [ax, ay], [2*ax, ay], [2*ax+astair, ay], [2*ax+astair+ax, ay], [2*ax+astair+2*ax, ay], 
                              [0, 2*ay], [ax, 2*ay], [2*ax, 2*ay], [2*ax+astair, 2*ay], [2*ax+astair+ax, 2*ay], [2*ax+astair+2*ax, 2*ay]])

        # 3) Column names including the two-sub-columns of the staircase
        self.column.nameref = np.array([[101, 102, 103, 20103, 104, 20104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
                                        [201, 202, 203, 20203, 204, 20204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218],
                                        [301, 302, 303, 20303, 304, 20304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318], 
                                        [401, 402, 403, 20403, 404, 20404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418],
                                        [501, 502, 503, 20503, 504, 20504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518],
                                        [601, 602, 603, 20603, 604, 20604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618],
                                        [701, 702, 703, 20703, 704, 20704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718],
                                        [801, 802, 803, 20803, 804, 20804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818]], dtype='int')

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        self.column.elasCnodeiref = np.array([[  1,   2,   3, 20103,   4, 20104,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18], 
                                              [101, 102, 103, 20203, 104, 20204, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118], 
                                              [201, 202, 203, 20303, 204, 20304, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218], 
                                              [301, 302, 303, 20403, 304, 20404, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318], 
                                              [401, 402, 403, 20503, 404, 20504, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418], 
                                              [501, 502, 503, 20603, 504, 20604, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518], 
                                              [601, 602, 603, 20703, 604, 20704, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618], 
                                              [701, 702, 703, 20803, 704, 20804, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718]], dtype='int')

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        self.column.elasCnodejref = np.array([[101, 102, 20103, 103, 20104, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
                                              [201, 202, 20203, 203, 20204, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218],
                                              [301, 302, 20303, 303, 20304, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318],
                                              [401, 402, 20403, 403, 20404, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418],
                                              [501, 502, 20503, 503, 20504, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518],
                                              [601, 602, 20603, 603, 20604, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618],
                                              [701, 702, 20703, 703, 20704, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718],
                                              [801, 802, 20803, 803, 20804, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818]], dtype='int')
        
        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        self.column.Ainfref = np.array([(ax/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2),
                                        (ax/2)*(ay), (ax)*(ay), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax)*(ay), (ax/2)*(ay),
                                        (ax/2)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................       
        self.column.Astairref = np.array([0, 0, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0, 0, 0, 0])
        # ...........................................................................
        self.column.Aroofref = np.array([(ax/2)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), 
                                         (ax)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay), ax*ay, (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), 
                                         (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), ax*ay, (ax/2)*(ay), (ax/2)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), 
                                         (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................        
        self.column.positionfactor_ref = np.array([[1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3], # bottom storeys 1.3 for periferic and 1.1 for central
                                                   [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5,  1.5, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]]) # top storeys 1.5 for periferic and 1.3 for central
        # ...........................................................................
        self.column.Colindex1 = np.array([2, 7, 15, 16, 17, 18, 19, 20], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
        self.column.Colindex2 = np.array([1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        self.column.Lref = np.array([1, 1, 0.50, 0.50, 0.50, 0.50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        # ...........................................................................
        self.column.walllength = np.array([ax/2+ay/2, ax, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax, ax/2+ay/2, 0, 0, ay/2, ay/2, 0, 0, ax/2+ay/2, ax, ax/2+astair/2, ax/2+astair/2, ax, ax/2+ay/2])
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 3
        self.general.stair_node_right_mirror_1st_storey = 4
        self.general.stairXleft = 2*ax
        self.general.stairXright = 2*ax + astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4], dtype='int') # to define the different continuous beams
        self.beamY.index = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50116)  # beamX names
        self.beamY.auxvY = np.arange(50151, 50163)  # beamY names
        self.beamStair.auxvStair = 51103  # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([101, 102, 103, 104, 105, 107, 108, 109, 110, 111, 113, 114, 115, 116, 117], dtype='int')
        self.beamY.auxvY1 = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112], dtype='int')
        self.beamStair.auxvStair1 = 20103
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 6
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        self.beamX.Ainf1 = np.array([(ax)*(ay/2), (ax)*(ay/2), 0, (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay), (ax)*(ay), (astair)*(ay/2), (ax)*(ay), (ax)*(ay), (ax)*(ay/2), (ax)*(ay/2), (astair)*(ay/2), (ax)*(ay/2), (ax)*(ay/2)])
        self.beamX.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamY.Ainf1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamY.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slaborient = 2 - Unloading in Y beams
        self.beamX.Ainf2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamX.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        self.beamY.Ainf2 = np.array([(ax/2)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax)*(ay), (ax/2)*(ay)])
        self.beamY.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay and ay >= astair:
            a1 = (ax-2*ay/2)*(ay/2) + 2*(ay/2)*(ay/2)/2
            a2 = (astair)*(astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a1, 0, a1, a1, 2*a1, 2*a1, a2, 2*a1, 2*a1, a1, a1, a2, a1, a1])
            self.beamX.a_over_l = np.array([(ay/2)/ax, (ay/2)/ax, 0, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            a11=(ay)*(ay/2)/2
            a12=(ay)*(ay/2)/2 + (astair*ay-2*((astair*astair/2)/2))/2
            self.beamY.Ainf3 = np.array([a11, 2*a11, a11, a11, 2*a11, a11, a11, 2*a11, a12, a12, 2*a11, a11])
            self.beamY.a_over_l = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, (astair/2)/ay, (astair/2)/ay, 0.5, 0.5])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay and ay >= astair:
            a1 = (ax)*(ax/2)/2
            a2 = (astair)*(astair/2)/2
            a11 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2
            a12 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a1, 0, a1, a1, 2*a1, 2*a1, a2, 2*a1, 2*a1, a1, a1, a2, a1, a1])
            self.beamX.a_over_l = np.array([0.50, 0.50, 0, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            self.beamY.Ainf3 = np.array([a11, 2*a11, a11, a11, 2*a11, a11, a11, 2*a11, a12, a12, 2*a11, a11])
            self.beamY.a_over_l = np.array([(ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        # Else is not possible as ax is always greater than astair maybe clean up is required here
        
        self.beamX.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2*astair 
        self.beamY.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Dimension of the spans of the beams
        self.beamX.L = np.array([ax, ax, astair, ax, ax, ax, ax, astair, ax, ax, ax, ax, astair, ax, ax])
        self.beamStair.L = astair
        self.beamY.L = np.array([ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay])

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        self.beamStair.pwallsA = 0.50
        self.beamY.pwallsA = np.array([1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1])

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [1, 2, 4, 5, 7, 8, 9, 10, 11, 2, 3, 5, 6, 8, 9, 10, 11, 12]
        self.general.floor_truss_nodej_ref = [8, 9, 11, 12, 14, 15, 16, 17, 18, 7, 8, 10, 11, 13, 14, 15, 16, 17]
        self.general.roof_truss_nodei_ref = [1, 2, 4, 5, 7, 8, 9, 10, 11, 2, 3, 5, 6, 8, 9, 10, 11, 12, 3, 4]
        self.general.roof_truss_nodej_ref = [8, 9, 11, 12, 14, 15, 16, 17, 18, 7, 8, 10, 11, 13, 14, 15, 16, 17, 10, 9]
        self.general.truss_stiffness = 10000000000 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 18 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]


    def _b03(self):
        """
        Building B03 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B03 - Needs to be changed for different buildings
        self.general.number_of_alignmentsX = 3
        self.general.number_of_alignmentsY = 8
        self.general.Reference = np.arange(1,25)

        # 2) Plan configuration
        self.general.Plan = np.array([[0, 0], [ax, 0], [2*ax, 0], [3*ax, 0], [3*ax+astair, 0], [3*ax+astair+ax, 0], [3*ax+astair+2*ax, 0], [3*ax+astair+3*ax, 0], 
                              [0, ay], [ax, ay], [2*ax, ay], [3*ax, ay], [3*ax+astair, ay], [3*ax+astair+ax, ay], [3*ax+astair+2*ax, ay], [3*ax+astair+3*ax, ay], 
                              [0, 2*ay], [ax, 2*ay], [2*ax, 2*ay], [3*ax, 2*ay], [3*ax+astair, 2*ay], [3*ax+astair+ax, 2*ay], [3*ax+astair+2*ax, 2*ay], [3*ax+astair+3*ax, 2*ay]])
        
        # 3) Column names including the two-sub-columns of the staircase
        self.column.nameref = np.array([[101, 102, 103, 104, 20104, 105, 20105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124],
                                        [201, 202, 203, 204, 20204, 205, 20205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
                                        [301, 302, 303, 304, 20304, 305, 20305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324],
                                        [401, 402, 403, 404, 20404, 405, 20405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424],
                                        [501, 502, 503, 504, 20504, 505, 20505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524],
                                        [601, 602, 603, 604, 20604, 605, 20605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624],
                                        [701, 702, 703, 704, 20704, 705, 20705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724],
                                        [801, 802, 803, 804, 20804, 805, 20805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824]], dtype='int')

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        self.column.elasCnodeiref = np.array([[  1,   2,   3,   4, 20104,   5, 20105,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24],
                                              [101, 102, 103, 104, 20204, 105, 20205, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124],
                                              [201, 202, 203, 204, 20304, 205, 20305, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
                                              [301, 302, 303, 304, 20404, 305, 20405, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324],
                                              [401, 402, 403, 404, 20504, 405, 20505, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424],
                                              [501, 502, 503, 504, 20604, 505, 20605, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524],
                                              [601, 602, 603, 604, 20704, 605, 20705, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624],
                                              [701, 702, 703, 704, 20804, 705, 20805, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724]], dtype='int')

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        self.column.elasCnodejref = np.array([[101, 102, 103, 20104, 104, 20105, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124],
                                              [201, 202, 203, 20204, 204, 20205, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
                                              [301, 302, 303, 20304, 304, 20305, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324],
                                              [401, 402, 403, 20404, 404, 20405, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424],
                                              [501, 502, 503, 20504, 504, 20505, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524],
                                              [601, 602, 603, 20604, 604, 20605, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624],
                                              [701, 702, 703, 20704, 704, 20705, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724],
                                              [801, 802, 803, 20804, 804, 20805, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824]], dtype='int') 

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        self.column.Ainfref = np.array([(ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), 
                                        (ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax)*(ay), (ax)*(ay), (ax/2)*(ay), 
                                        (ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................       
        self.column.Astairref = np.array([0, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        # ...........................................................................
        self.column.Aroofref = np.array([(ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), 
                                         (ax/2)*(ay), ax*ay, ax*ay, (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), ax*ay, ax*ay, (ax/2)*(ay), 
                                         (ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................        
        self.column.positionfactor_ref = np.array([[1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3], # bottom storeys 1.3 for periferic and 1.1 for central
                                                   [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]]) # top storeys 1.5 for periferic and 1.3 for central
        # ...........................................................................
        self.column.Colindex1 = np.array([1, 2, 3, 8, 9, 10, 19, 20, 21, 24, 25, 26], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
        self.column.Colindex2 = np.array([4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17, 18, 22, 23], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        self.column.Lref = np.array([1, 1, 1, 0.50, 0.50, 0.50, 0.50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        # ...........................................................................
        self.column.walllength = np.array([ax/2+ay/2, ax, ax, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax, ax, ax/2+ay/2, ay, 0, 0, ay/2, ay/2, 0, 0, ay, ax/2+ay/2, ax, ax, ax/2+astair/2, ax/2+astair/2, ax, ax, ax/2+ay/2])
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 4  # ground node
        self.general.stair_node_right_mirror_1st_storey = 5  # ground node
        self.general.stairXleft = 3 * ax
        self.general.stairXright = 3 * ax + astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4], dtype='int')  # to define the different continuous beams
        self.beamY.index = np.array([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8], dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50122)  # beamX names
        self.beamY.auxvY = np.arange(50151, 50167)  # beamY names
        self.beamStair.auxvStair = 51104
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([101, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 117, 118, 119, 120, 121, 122, 123], dtype='int')
        self.beamY.auxvY1 = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116], dtype='int')
        self.beamStair.auxvStair1 = 20104
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 8
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        self.beamX.Ainf1 = np.array([(ax)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), 0, (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay), (ax)*(ay), (ax)*(ay), (astair)*(ay/2), (ax)*(ay), (ax)*(ay), (ax)*(ay), (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (astair)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay/2)])
        self.beamX.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamY.Ainf1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamY.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slaborient = 2 - Unloading in Y beams
        self.beamX.Ainf2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamX.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        self.beamY.Ainf2 = np.array([(ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2)*(ay)])
        self.beamY.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        
        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay and ay >= astair:
            a1 = (ax-2*ay/2)*(ay/2) + 2*(ay/2)*(ay/2)/2
            a2 = (astair)*(astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a1, a1, 0, a1, a1, a1, 2*a1, 2*a1, 2*a1, a2, 2*a1, 2*a1, 2*a1, a1, a1, a1, a2, a1, a1, a1])
            self.beamX.a_over_l = np.array([(ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            a11 = (ay)*(ay/2)/2
            a12 = (ay)*(ay/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamY.Ainf3 = np.array([a11, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a12, a12, 2*a11, 2*a11, a11])
            self.beamY.a_over_l = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.50, 0.5, 0.5, 0.50, 0.5, (astair/2)/ay, (astair/2)/ay, 0.50, 0.50, 0.50])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay and ay >= astair:
            a1 = (ax)*(ax/2)/2
            a2 = (astair)*(astair/2)/2
            a11 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2
            a12 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a1, a1, 0, a1, a1, a1, 2*a1, 2*a1, 2*a1, a2, 2*a1, 2*a1, 2*a1, a1, a1, a1, a2, a1, a1, a1])
            self.beamX.a_over_l = np.array([0.50, 0.50, 0.50, 0, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            self.beamY.Ainf3 = np.array([a11, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a12, a12, 2*a11, 2*a11, a11])
            self.beamY.a_over_l = np.array([(ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        # Else is not possible as ax is always greater than astair maybe clean up is required here
        
        self.beamX.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2 * astair 
        self.beamY.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        
        # Dimension of the spans of the beams
        self.beamX.L = np.array([ax, ax, ax, astair, ax, ax, ax, ax, ax, ax, astair, ax, ax, ax, ax, ax, ax, astair, ax, ax, ax])
        self.beamStair.L = astair
        self.beamY.L = np.array([ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay])

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
        self.beamStair.pwallsA = 0.50
        self.beamY.pwallsA = np.array([1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1])

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]
        self.general.floor_truss_nodej_ref = [10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 9, 10, 11, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23]
        self.general.roof_truss_nodei_ref = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 4, 5]
        self.general.roof_truss_nodej_ref = [10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 9, 10, 11, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 13, 12]
        self.general.truss_stiffness = 10000000000 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 24 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]


    def _b04(self):
        """
        Building B04 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B04 - Needs to be changed for different buildings
        self.general.number_of_alignmentsX = 4
        self.general.number_of_alignmentsY = 4
        self.general.Reference = np.arange(1,17)
        
        # 2) Plan configuration
        self.general.Plan = np.array([[0, 0], [ ax, 0], [ ax+astair, 0], [ ax+astair+ax, 0],
                              [0, ay], [ ax, ay], [ ax+astair, ay], [ ax+astair+ax, ay],
                              [0, 2*ay], [ ax, 2*ay], [ ax+astair, 2*ay], [ ax+astair+ax, 2*ay],
                              [0, 3*ay], [ ax, 3*ay], [ ax+astair, 3*ay], [ ax+astair+ax, 3*ay]])

        # 3) Column names including the two-sub-columns of the staircase
        self.column.nameref = np.array([[101, 102, 20102, 103, 20103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116],
                                        [201, 202, 20202, 203, 20203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216],
                                        [301, 302, 20302, 303, 20303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316],
                                        [401, 402, 20402, 403, 20403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416],
                                        [501, 502, 20502, 503, 20503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516],
                                        [601, 602, 20602, 603, 20603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616],
                                        [701, 702, 20702, 703, 20703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716],
                                        [801, 802, 20802, 803, 20803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816]], dtype='int')

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        self.column.elasCnodeiref = np.array([[  1,   2, 20102,   3, 20103,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16],  # 1102 is the half height node for the staircase beam
                                              [101, 102, 20202, 103, 20203, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116], 
                                              [201, 202, 20302, 203, 20303, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216], 
                                              [301, 302, 20402, 303, 20403, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316], 
                                              [401, 402, 20502, 403, 20503, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416], 
                                              [501, 502, 20602, 503, 20603, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516], 
                                              [601, 602, 20702, 603, 20703, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616], 
                                              [701, 702, 20802, 703, 20803, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716]], dtype='int')

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        self.column.elasCnodejref = np.array([[101, 20102, 102, 20103, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116],  # 1102 half height node for the staircase beam
                                              [201, 20202, 202, 20203, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216],
                                              [301, 20302, 302, 20303, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316],
                                              [401, 20402, 402, 20403, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416],
                                              [501, 20502, 502, 20503, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516],
                                              [601, 20602, 602, 20603, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616],
                                              [701, 20702, 702, 20703, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716],
                                              [801, 20802, 802, 20803, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816]], dtype='int')

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        self.column.Ainfref = np.array([(ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), 
                                        (ax/2)*(ay), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay), 
                                        (ax/2)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax/2)*(ay), (ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................       
        self.column.Astairref = np.array([0, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        # ...........................................................................
        self.column.Aroofref = np.array([(ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2), 
                                         (ax/2)*(ay), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay), 
                                         (ax/2)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax/2)*(ay), (ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................        
        self.column.positionfactor_ref = np.array([[1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.1, 1.1, 1.3, 1.3, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.3], # bottom storeys 1.3 for periferic and 1.1 for central
                                                   [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.3, 1.3, 1.5, 1.5, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.5]]) # top storeys 1.5 for periferic and 1.3 for central
        # ...........................................................................
        self.column.Colindex1 = np.array([2, 3, 4, 5, 12, 13, 15, 16, 17, 18], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
        self.column.Colindex2 = np.array([1, 6, 7, 8, 9, 10, 11, 14], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        self.column.Lref = np.array([1, 0.50, 0.50, 0.50, 0.50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        # ...........................................................................
        self.column.walllength = np.array([ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ay, ay/2, ay/2, ay, ay, 0, 0, ay, ax/2+ay/2, ax/2+astair/2, ax/2+astair/2, ax/2+ay/2])
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 2
        self.general.stair_node_right_mirror_1st_storey = 3
        self.general.stairXleft = ax
        self.general.stairXright = ax + astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5], dtype='int') # to define the different continuous beams
        self.beamY.index = np.array([2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5], dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50113)  # beamX names
        self.beamY.auxvY = np.arange(50151, 50163)  # beamY names
        self.beamStair.auxvStair = 51102 # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([101, 102, 103, 105, 106, 107, 109, 110, 111, 113, 114, 115], dtype='int')
        self.beamY.auxvY1 = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112], dtype='int')
        self.beamStair.auxvStair1 = 20102
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                            300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                            600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                            300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                            600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 4
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        self.beamX.Ainf1 = np.array([(ax)*(ay/2), 0, (ax)*(ay/2), (ax)*(ay), (astair)*(ay/2), (ax)*(ay), (ax)*(ay), (astair)*(ay), (ax)*(ay), (ax)*(ay/2), (astair)*(ay/2), (ax)*(ay/2)])
        self.beamX.Astair1 = np.array([0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamY.Ainf1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamY.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slaborient = 2 - Unloading in Y beams
        self.beamX.Ainf2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamX.Astair2 = np.array([0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        self.beamY.Ainf2 = np.array([(ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax/2)*(ay),  (ax/2)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax/2)*(ay)])
        self.beamY.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay and ay >= astair:
            a1 = (ax-2*ay/2)*(ay/2) + 2*(ay/2)*(ay/2)/2
            a2 = 0
            a4 = 2*a1
            a5 = (astair)*(astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a2, a1, a4, a5, a4, 2*a1, 2*a5, 2*a1, a1, a5, a1])
            self.beamX.a_over_l = np.array([(ay/2)/ax, 0.00, (ay/2)/ax, (ay/2)/ax, 0.50, (ay/2)/ax, (ay/2)/ax, 0.50, (ay/2)/ax, (ay/2)/ax, 0.50, (ay/2)/ax])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            a11 = (ay)*(ay/2)/2
            a12 = (ay)*(ay/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamY.Ainf3 = np.array([a11, a11, a11, a11, a11, a12, a12, a11, a11, a12, a12, a11])
            self.beamY.a_over_l = np.array([0.5, 0.5, 0.5, 0.5, 0.5, (astair/2)/ay, (astair/2)/ay, 0.5, 0.5, (astair/2)/ay, (astair/2)/ay, 0.5])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay and ay >= astair:
            a1 = (ax)*(ax/2)/2
            a2 = 0
            a3 = 2*a1
            a5 = (astair)*(astair/2)/2
            a6 = 2*a5
            a11 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2
            a12 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a2, a1, a3, a5, a3, a3, a6, a3, a1, a5, a1])
            self.beamX.a_over_l = np.array([0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            self.beamY.Ainf3 = np.array([a11, a11, a11, a11, a11, a12, a12, a11, a11, a12, a12, a11])
            self.beamY.a_over_l = np.array([(ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        # Else is not possible as ax is always greater than astair maybe clean up is required here
        
        self.beamX.Astair3 = np.array([0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2*astair 
        self.beamY.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Dimension of the spans of the beams
        self.beamX.L = np.array([ax, astair, ax, ax, astair, ax, ax, astair, ax, ax, astair, ax])
        self.beamStair.L = astair
        self.beamY.L = np.array([ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay])

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1])
        self.beamStair.pwallsA = 0.10
        self.beamY.pwallsA = np.array([1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1])

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 3, 0, 0, 4, 3, 0, 0, 4, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [1, 3, 5, 6, 7, 9, 10, 11, 2, 4, 6, 7, 8, 10, 11, 12]
        self.general.floor_truss_nodej_ref = [6, 8, 10, 11, 12, 14, 15, 16, 5, 7, 9, 10, 11, 13, 14, 15]
        self.general.roof_truss_nodei_ref = [1, 3, 5, 6, 7, 9, 10, 11, 2, 4, 6, 7, 8, 10, 11, 12]
        self.general.roof_truss_nodej_ref = [6, 8, 10, 11, 12, 14, 15, 16, 5, 7, 9, 10, 11, 13, 14, 15]
        self.general.truss_stiffness = 10.e12 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 16 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]
        # originally the parameter above was 32


    def _b04b(self):
        """
        Building B04b - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B04b - Needs to be changed for different buildings
        self.general.number_of_alignmentsX = 4
        self.general.number_of_alignmentsY = 4
        self.general.Reference = np.arange(1,17)
        
        # 2) Plan configuration
        self.general.Plan = np.array([[0, 0], [ax, 0], [ax+astair, 0], [ax+astair+ax, 0],
                             [0, ay], [ax, ay], [ax+astair, ay], [ax+astair+ax, ay],
                             [0, 2*ay], [ax, 2*ay], [ax+astair, 2*ay], [ax+astair+ax, 2*ay],
                             [0, 3*ay], [ax, 3*ay], [ax+astair, 3*ay], [ax+astair+ax, 3*ay]])

        # 3) Column names including the two-sub-columns of the staircase
        self.column.nameref = np.array([[101, 102, 103, 104, 105, 106, 20106, 107, 20107, 108, 109, 110, 111, 112, 113, 114, 115, 116],
                                        [201, 202, 203, 204, 205, 206, 20206, 207, 20207, 208, 209, 210, 211, 212, 213, 214, 215, 216],
                                        [301, 302, 303, 304, 305, 306, 20306, 307, 20307, 308, 309, 310, 311, 312, 313, 314, 315, 316],
                                        [401, 402, 403, 404, 405, 406, 20406, 407, 20407, 408, 409, 410, 411, 412, 413, 414, 415, 416],
                                        [501, 502, 503, 504, 505, 506, 20506, 507, 20507, 508, 509, 510, 511, 512, 513, 514, 515, 516],
                                        [601, 602, 603, 604, 605, 606, 20606, 607, 20607, 608, 609, 610, 611, 612, 613, 614, 615, 616],
                                        [701, 702, 703, 704, 705, 706, 20706, 707, 20707, 708, 709, 710, 711, 712, 713, 714, 715, 716],
                                        [801, 802, 803, 804, 805, 806, 20806, 807, 20807, 808, 809, 810, 811, 812, 813, 814, 815, 816]], dtype='int')


        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        self.column.elasCnodeiref = np.array([[  1,   2,   3,   4,   5,   6, 20106,   7, 20107,   8,   9,  10,  11,  12,  13,  14,  15,  16],  # 1102 is the half height node for the staircase beam
                                              [101, 102, 103, 104, 105, 106, 20206, 107, 20207, 108, 109, 110, 111, 112, 113, 114, 115, 116], 
                                              [201, 202, 203, 204, 205, 206, 20306, 207, 20307, 208, 209, 210, 211, 212, 213, 214, 215, 216], 
                                              [301, 302, 303, 304, 305, 306, 20406, 307, 20407, 308, 309, 310, 311, 312, 313, 314, 315, 316], 
                                              [401, 402, 403, 404, 405, 406, 20506, 407, 20507, 408, 409, 410, 411, 412, 413, 414, 415, 416], 
                                              [501, 502, 503, 504, 505, 506, 20606, 507, 20607, 508, 509, 510, 511, 512, 513, 514, 515, 516], 
                                              [601, 602, 603, 604, 605, 606, 20706, 607, 20707, 608, 609, 610, 611, 612, 613, 614, 615, 616], 
                                              [701, 702, 703, 704, 705, 706, 20806, 707, 20807, 708, 709, 710, 711, 712, 713, 714, 715, 716]], dtype='int')

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        self.column.elasCnodejref = np.array([[101, 102, 103, 104, 105, 20106, 106, 20107, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116],  # 1102 half height node for the staircase beam
                                              [201, 202, 203, 204, 205, 20206, 206, 20207, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216],
                                              [301, 302, 303, 304, 305, 20306, 306, 20307, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316],
                                              [401, 402, 403, 404, 405, 20406, 406, 20407, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416],
                                              [501, 502, 503, 504, 505, 20506, 506, 20507, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516],
                                              [601, 602, 603, 604, 605, 20606, 606, 20607, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616],
                                              [701, 702, 703, 704, 705, 20706, 706, 20707, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716],
                                              [801, 802, 803, 804, 805, 20806, 806, 20807, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816]], dtype='int')

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        self.column.Ainfref = np.array([(ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay), (ax/2)*(ay)+(astair/2)*(ay/2), 
                                        (ax/2)*(ay)+(astair/2)*(ay/2), (ax/2)*(ay)+(astair/2)*(ay/2), (ax/2)*(ay)+(astair/2)*(ay/2), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay)+(astair/2)*(ay/2), 
                                        (ax/2)*(ay)+(astair/2)*(ay/2), (ax/2)*(ay), (ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................       
        self.column.Astairref = np.array([0, 0, 0, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0])
        # ...........................................................................
        self.column.Aroofref = np.array([(ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay), (ay)*(ax/2+astair/2), 
                                         (ay)*(ax/2+astair/2), (ay)*(ax/2+astair/2), (ay)*(ax/2+astair/2), (ax/2)*(ay), (ax/2)*(ay), (ay)*(ax/2+astair/2), 
                                         (ay)*(ax/2+astair/2), (ax/2)*(ay), (ax/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................        
        self.column.positionfactor_ref = np.array([[1.3, 1.3, 1.3, 1.3, 1.3, 1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.3], # bottom storeys 1.3 for periferic and 1.1 for central
                                                   [1.5, 1.5, 1.5, 1.5, 1.5, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.5]]) # top storeys 1.5 for periferic and 1.3 for central
        # ...........................................................................
        self.column.Colindex1 = np.array([1, 2, 3, 4, 15, 16, 17, 18], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
        self.column.Colindex2 = np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        self.column.Lref = np.array([1, 1, 1, 1, 1, 0.50, 0.50, 0.50, 0.50, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        # ...........................................................................
        self.column.walllength = np.array([ax/2+ay/2, ax/2+astair/2, ax/2+astair/2, ax/2+ay/2, ay, ay/2, ay/2, ay/2, ay/2, ay, ay, ay/2, ay/2, ay, ax/2+ay/2, ax/2+astair/2, ax/2+astair/2, ax/2+ay/2])
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 6  # ground node
        self.general.stair_node_right_mirror_1st_storey = 7  # ground node
        self.general.stairXleft = ax
        self.general.stairXright = ax + astair
        self.general.stairY = ay
        # ...........................................................................
        self.beamX.index = np.array([2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5], dtype='int') # to define the different continuous beams
        self.beamY.index = np.array([2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5], dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50113)  # beamX names
        self.beamY.auxvY = np.arange(50151, 50163)  # beamY names
        self.beamStair.auxvStair = 51106 # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')

        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')

        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([101, 102, 103, 105, 106, 107, 109, 110, 111, 113, 114, 115], dtype='int')
        self.beamY.auxvY1 = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112], dtype='int')
        self.beamStair.auxvStair1 = 20106
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 4
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        self.beamX.Ainf1 = np.array([(ax)*(ay/2), (astair)*(ay/2), (ax)*(ay/2), (ax)*(ay), (astair)*(ay/2), (ax)*(ay), (ax)*(ay), (astair)*(ay/2), (ax)*(ay), (ax)*(ay/2), (astair)*(ay/2), (ax)*(ay/2)])
        self.beamX.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0])
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamY.Ainf1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamY.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slaborient = 2 - Unloading in Y beams
        self.beamX.Ainf2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamX.Astair2 = np.array([0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        self.beamY.Ainf2 = np.array([(ax/2)*(ay), (ax/2)*(ay)+(astair/2)*(ay), (ax/2)*(ay)+(astair/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax/2)*(ay)+(astair/2)*(ay), (ax/2)*(ay)+(astair/2)*(ay), (ax/2)*(ay)])
        self.beamY.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay and ay >= astair:
            a1 = (ax-2*ay/2)*(ay/2) + 2*(ay/2)*(ay/2)/2
            a5 = (astair)*(astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a5, a1,  2*a1, a5, 2*a1, 2*a1, a5, 2*a1, a1, a5, a1])
            self.beamX.a_over_l = np.array([(ay/2)/ax, 0.50, (ay/2)/ax, (ay/2)/ax, 0.50, (ay/2)/ax, (ay/2)/ax, 0.50, (ay/2)/ax, (ay/2)/ax, 0.50, (ay/2)/ax])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            a11 = (ay)*(ay/2)/2
            a12 = (ay)*(ay/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamY.Ainf3 = np.array([a11, a12, a12, a11, a11, a11, a11, a11, a11, a12, a12, a11])
            self.beamY.a_over_l = np.array([0.5, (astair/2)/ay, (astair/2)/ay, 0.50, 0.5, 0.5, 0.5, 0.5, 0.5, (astair/2)/ay, (astair/2)/ay, 0.50])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay and ay >= astair:
            a1 = (ax)*(ax/2)/2
            a2 = (astair)*(astair/2)/2
            a11 = (ax*ay - 4*((ax/2*ax/2)/2))/2
            a12 = a11 + (astair*ay - 4*((astair/2*astair/2)/2))/2
            self.beamX.Ainf3 = np.array([a1, a2, a1, 2*a1, a2, 2*a1, 2*a1, a2, 2*a1, a1, a2, a1])
            self.beamX.a_over_l = np.array([0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            a11 = (ax*ay - 4*((ax/2*ax/2)/2))/2
            a12 = a11 + (astair*ay - 4*((astair/2*astair/2)/2))/2
            self.beamY.Ainf3 = np.array([a11, a12, a12, a11, a11, a11, a11, a11, a11, a12, a12, a11])
            self.beamY.a_over_l = np.array([(ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        # Else is not possible as ax is always greater than astair maybe clean up is required here
        
        self.beamX.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0])
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2*astair 
        self.beamY.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Dimension of the spans of the beams
        self.beamX.L = np.array([ax, astair, ax, ax, astair, ax, ax, astair, ax, ax, astair, ax])
        self.beamStair.L = astair
        self.beamY.L = np.array([ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay])

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1])
        self.beamStair.pwallsA = 1.0
        self.beamY.pwallsA = np.array([1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1])

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 3, 0, 0, 0, 0, 4, 3, 0, 0, 4, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [1, 3, 5, 6, 7, 9, 10, 11, 2, 4, 6, 7, 8, 10, 11, 12]
        self.general.floor_truss_nodej_ref = [6, 8, 10, 11, 12, 14, 15, 16, 5, 7, 9, 10, 11, 13, 14, 15]
        self.general.roof_truss_nodei_ref = [1, 3, 5, 6, 7, 9, 10, 11, 2, 4, 6, 7, 8, 10, 11, 12]
        self.general.roof_truss_nodej_ref = [6, 8, 10, 11, 12, 14, 15, 16, 5, 7, 9, 10, 11, 13, 14, 15]
        self.general.truss_stiffness = 10.e12 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 16 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]


    def _b05(self):
        """
        Building B05 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B05 - Needs to be changed for different buildings
        self.general.number_of_alignmentsX = 4
        self.general.number_of_alignmentsY = 6
        self.general.Reference = np.arange(1,25)
        
        # 2) Plan configuration
        self.general.Plan = np.array([[0, 0], [ax, 0], [2*ax, 0], [2*ax+astair, 0], [2*ax+astair+ax, 0], [2*ax+astair+2*ax, 0],
                              [0, ay], [ax, ay], [2*ax, ay], [2*ax+astair, ay], [2*ax+astair+ax, ay], [2*ax+astair+2*ax, ay],
                              [0, 2*ay], [ax, 2*ay], [2*ax, 2*ay], [2*ax+astair, 2*ay], [2*ax+astair+ax, 2*ay], [2*ax+astair+2*ax, 2*ay],
                              [0, 3*ay], [ax, 3*ay], [2*ax, 3*ay], [2*ax+astair, 3*ay], [2*ax+astair+ax, 3*ay], [2*ax+astair+2*ax, 3*ay]])

        # 3) Column names including the two-sub-columns of the staircase
        self.column.nameref = np.array([[101, 102, 103, 20103, 104, 20104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124],
                                        [201, 202, 203, 20203, 204, 20204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
                                        [301, 302, 303, 20303, 304, 20304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324],
                                        [401, 402, 403, 20403, 404, 20404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424],
                                        [501, 502, 503, 20503, 504, 20504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524],
                                        [601, 602, 603, 20603, 604, 20604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624],
                                        [701, 702, 703, 20703, 704, 20704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724],
                                        [801, 802, 803, 20803, 804, 20804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824]], dtype='int')

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        self.column.elasCnodeiref = np.array([[  1,   2,   3, 20103,   4, 20104,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24],
                                              [101, 102, 103, 20203, 104, 20204, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124],
                                              [201, 202, 203, 20303, 204, 20304, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
                                              [301, 302, 303, 20403, 304, 20404, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324],
                                              [401, 402, 403, 20503, 404, 20504, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424],
                                              [501, 502, 503, 20603, 504, 20604, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524],
                                              [601, 602, 603, 20703, 604, 20704, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624],
                                              [701, 702, 703, 20803, 704, 20804, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724]], dtype='int')

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        self.column.elasCnodejref = np.array([[101, 102, 20103, 103, 20104, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124],
                                              [201, 202, 20203, 203, 20204, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
                                              [301, 302, 20303, 303, 20304, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324],
                                              [401, 402, 20403, 403, 20404, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424],
                                              [501, 502, 20503, 503, 20504, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524],
                                              [601, 602, 20603, 603, 20604, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624],
                                              [701, 702, 20703, 703, 20704, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724],
                                              [801, 802, 20803, 803, 20804, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824]], dtype='int')  

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        self.column.Ainfref = np.array([(ax/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay), (ax)*(ay), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), 
                                        (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax/2)*(ay/2)+(astair/2)*(ay), (ax/2)*(ay/2)+(astair/2)*(ay), 
                                        (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................       
        self.column.Astairref = np.array([0, 0, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        # ...........................................................................
        self.column.Aroofref = np.array([(ax/2)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), 
                                         (ax/2)*(ay), (ax*ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax*ay), (ax/2)*(ay), (ax/2)*(ay), (ax*ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), 
                                         (ax*ay), (ax/2)*(ay), (ax/2)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................        
        self.column.positionfactor_ref = np.array([[1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3], # bottom storeys 1.3 for periferic and 1.1 for central
                                                   [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]]) # top storeys 1.5 for periferic and 1.3 for central
        # ...........................................................................
        self.column.Colindex1 = np.array([1, 2, 7, 8, 10, 13, 16, 19, 22, 23, 24, 25], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
        self.column.Colindex2 = np.array([3, 4, 5, 6, 9, 11, 12, 14, 15, 17, 18, 20, 21, 26], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        self.column.Lref = np.array([1, 1, 0.50, 0.50, 0.50, 0.50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        # ...........................................................................
        self.column.walllength = np.array([ax/2+ay/2, ax, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax, ax/2+ay/2, 0, 0, ay/2, ay/2, 0, 0, 0, 0, 0, 0, 0, 0, ax/2+ay/2, ax, ax/2+astair/2, ax/2+astair/2, ax, ax/2+ay/2])
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 3  # ground node
        self.general.stair_node_right_mirror_1st_storey = 4  # ground node
        self.general.stairXleft = 2 * ax
        self.general.stairXright = 2 * ax + astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5], dtype='int')  # to define the different continuous beams
        self.beamY.index = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], dtype='int')  # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50121)  # beamX names
        self.beamY.auxvY = np.arange(50151, 50169)  # beamY names
        self.beamStair.auxvStair = 51103
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')

        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')

        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([101, 102, 103, 104, 105, 107, 108, 109, 110, 111, 113, 114, 115, 116, 117, 119, 120, 121, 122, 123], dtype='int')  # beam initial nodes in XX
        self.beamY.auxvY1 = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118], dtype='int')  # beam initial nodes in YY
        self.beamStair.auxvStair1 = 20103
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 6
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        self.beamX.Ainf1 = np.array([(ax)*(ay/2), (ax)*(ay/2), 0, (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay), (ax)*(ay), (astair)*(ay/2), (ax)*(ay), (ax)*(ay), (ax)*(ay), (ax)*(ay), (astair)*(ay), (ax)*(ay), (ax)*(ay), (ax)*(ay/2), (ax)*(ay/2), (astair)*(ay/2), (ax)*(ay/2), (ax)*(ay/2)])
        self.beamX.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamY.Ainf1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamY.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slaborient = 2 - Unloading in Y beams
        self.beamX.Ainf2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamX.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        self.beamY.Ainf2 = np.array([(ax/2)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax)*(ay), (ax/2)*(ay)])
        self.beamY.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay and ay >= astair:
            a1 = ((ax*ay)-4*(ay/2*(ay/2)/2))/2
            a2 = (astair)*(astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a1, 0, a1, a1, 2*a1, 2*a1, a2, 2*a1, 2*a1, 2*a1, 2*a1, 2*a2, 2*a1, 2*a1, a1, a1, a2, a1, a1])
            self.beamX.a_over_l = np.array([(ay/2)/ax, (ay/2)/ax, 0, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            a11 = (ay)*(ay/2)/2
            a12 = (ay)*(ay/2)/2 + (astair*ay-2*((astair*astair/2)/2))/2
            self.beamY.Ainf3 = np.array([a11, 2*a11, a11, a11, 2*a11, a11, a11, 2*a11, a12, a12, 2*a11, a11, a11, 2*a11, a12, a12, 2*a11, a11])
            self.beamY.a_over_l = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, (astair/2)/ay, (astair/2)/ay, 0.5, 0.5, 0.5, 0.5, (astair/2)/ay, (astair/2)/ay, 0.5, 0.5])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay and ay >= astair:
            a1 = (ax)*(ax/2)/2
            a2 = (astair)*(astair/2)/2
            a11 = (ay*ax-(2*(ax*(ax/2)/2)))/2
            a12 = (ay*ax-(2*(ax*(ax/2)/2)))/2 + (astair*ay-2*(astair*(astair/2)/2))/2
            self.beamX.Ainf3 = np.array([a1, a1, 0, a1, a1, 2*a1, 2*a1, a2, 2*a1, 2*a1, 2*a1, 2*a1, 2*a2, 2*a1, 2*a1, a1, a1, a2, a1, a1])
            self.beamX.a_over_l = np.array([0.50, 0.50, 0, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            self.beamY.Ainf3 = np.array([a11, 2*a11, a11, a11, 2*a11, a11, a11, 2*a11, a12, a12, 2*a11, a11, a11, 2*a11, a12, a12, 2*a11, a11])
            self.beamY.a_over_l = np.array([(ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        # Else is not possible as ax is always greater than astair maybe clean up is required here
        
        self.beamX.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2 * astair 
        self.beamY.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Dimension of the spans of the beams
        self.beamX.L = np.array([ax, ax, astair, ax, ax, ax, ax, astair, ax, ax, ax, ax, astair, ax, ax, ax, ax, astair, ax, ax])
        self.beamStair.L = astair
        self.beamY.L = np.array([ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay])

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        self.beamStair.pwallsA = 0.50
        self.beamY.pwallsA = np.array([1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1])

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [1, 2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 2, 3, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18]
        self.general.floor_truss_nodej_ref = [8, 9, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 7, 8, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23]
        self.general.roof_truss_nodei_ref = [1, 2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 2, 3, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18]
        self.general.roof_truss_nodej_ref = [8, 9, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 7, 8, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23]
        self.general.truss_stiffness = 10000000000 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 24 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]
        # originally the parameter above was 32


    def _b06(self):
        """
        Building B06 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B06 - Needs to be changed for different buildings
        self.general.number_of_alignmentsX = 4
        self.general.number_of_alignmentsY = 8
        self.general.Reference = np.arange(1,33)
        
        # 2) Plan configuration
        self.general.Plan = np.array([[0, 0], [ax, 0], [2*ax, 0], [3*ax, 0], [3*ax+astair, 0], [3*ax+astair+ax, 0], [3*ax+astair+2*ax, 0], [3*ax+astair+3*ax, 0], 
                              [0, ay], [ax, ay], [2*ax, ay], [3*ax, ay], [3*ax+astair, ay], [3*ax+astair+ax, ay], [3*ax+astair+2*ax, ay], [3*ax+astair+3*ax, ay], 
                              [0, 2*ay], [ax, 2*ay], [2*ax, 2*ay], [3*ax, 2*ay], [3*ax+astair, 2*ay], [3*ax+astair+ax, 2*ay], [3*ax+astair+2*ax, 2*ay], [3*ax+astair+3*ax, 2*ay], 
                              [0, 3*ay], [ax, 3*ay], [2*ax, 3*ay], [3*ax, 3*ay], [3*ax+astair, 3*ay], [3*ax+astair+ax, 3*ay], [3*ax+astair+2*ax, 3*ay], [3*ax+astair+3*ax, 3*ay]])

        # 3) Column names including the two-sub-columns of the staircase
        self.column.nameref = np.array([[101, 102, 103, 104, 20104, 105, 20105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132],
                                        [201, 202, 203, 204, 20204, 205, 20205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232],
                                        [301, 302, 303, 304, 20304, 305, 20305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332],
                                        [401, 402, 403, 404, 20404, 405, 20405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432],
                                        [501, 502, 503, 504, 20504, 505, 20505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532],
                                        [601, 602, 603, 604, 20604, 605, 20605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632],
                                        [701, 702, 703, 704, 20704, 705, 20705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732],
                                        [801, 802, 803, 804, 20804, 805, 20805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832]], dtype='int')

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        self.column.elasCnodeiref = np.array([[  1,   2,   3,   4, 20104,   5, 20105,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32],
                                              [101, 102, 103, 104, 20204, 105, 20205, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132],
                                              [201, 202, 203, 204, 20304, 205, 20305, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232],
                                              [301, 302, 303, 304, 20404, 305, 20405, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332],
                                              [401, 402, 403, 404, 20504, 405, 20505, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432],
                                              [501, 502, 503, 504, 20604, 505, 20605, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532],
                                              [601, 602, 603, 604, 20704, 605, 20705, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632],
                                              [701, 702, 703, 704, 20804, 705, 20805, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732]], dtype='int')

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        self.column.elasCnodejref = np.array([[101, 102, 103, 20104, 104, 20105, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132],
                                              [201, 202, 203, 20204, 204, 20205, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232],
                                              [301, 302, 303, 20304, 304, 20305, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332],
                                              [401, 402, 403, 20404, 404, 20405, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432],
                                              [501, 502, 503, 20504, 504, 20505, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532],
                                              [601, 602, 603, 20604, 604, 20605, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632],
                                              [701, 702, 703, 20704, 704, 20705, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732],
                                              [801, 802, 803, 20804, 804, 20805, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832]], dtype='int')

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        self.column.Ainfref = np.array([(ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay), (ax)*(ay), (ax)*(ay), 
                                        (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2+astair/2)*(ay), 
                                        (ax/2+astair/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................       
        self.column.Astairref = np.array([0, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0, 0, (astair/2)*ay/2, (astair/2)*ay/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        # ...........................................................................
        self.column.Aroofref = np.array([(ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2), (ax/2)*(ay), 
                                         (ax*ay), (ax*ay), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax*ay), (ax*ay), (ax/2)*(ay), (ax/2)*(ay), (ax*ay), (ax*ay), 
                                         (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax/2)*(ay/2)+(ax/2)*(ay/2)+(astair/2)*(ay/2), (ax*ay), (ax*ay), (ax/2)*(ay), (ax/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), 
                                         (ax/2+astair/2)*(ay/2), (ax/2+astair/2)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax/2)*(ay/2)])
        # ...........................................................................        
        self.column.positionfactor_ref = np.array([[1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3], # bottom storeys 1.3 for periferic and 1.1 for central
                                                   [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]]) # top storeys 1.5 for periferic and 1.3 for central
        # ...........................................................................
        if self.general.slaborient == 1:
            self.column.Colindex1 = np.array([2, 3, 8, 9, 12, 13, 16, 17, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
            self.column.Colindex2 = np.array([1, 4, 5, 6, 7, 10, 11, 14, 15, 18, 19, 26, 27, 34], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        elif self.general.slaborient == 2:
            self.column.Colindex1 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 28, 29, 30, 31, 32, 33], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
            self.column.Colindex2 = np.array([1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 34], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        else:
            self.column.Colindex1 = np.array([2, 3, 4, 5, 6, 7, 8, 9, 28, 29, 30, 31, 32, 33], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
            self.column.Colindex2 = np.array([1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 34], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        self.column.Lref = np.array([1, 1, 1, 0.50, 0.50, 0.50, 0.50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        # ...........................................................................
        self.column.walllength = np.array([ax/2+ay/2, ax, ax, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax/2+ay/2, ax, ax, ax/2+ay/2, ay, 0, 0, ay/2, ay/2, 0, 0, ay, ay, 0, 0, 0, 0, 0, 0, ay, ax/2+ay/2, ax, ax, ax/2+astair/2, ax/2+astair/2, ax, ax, ax/2+ay/2])
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 4
        self.general.stair_node_right_mirror_1st_storey = 5
        self.general.stairXleft = 3* ax
        self.general.stairXright = 3 * ax + astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5], dtype='int') # to define the different continuous beams
        self.beamY.index = np.array([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8], dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50129)  # beamX names
        self.beamY.auxvY = np.arange(50151, 50175)  # beamY names
        self.beamStair.auxvStair = 51104  # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([101, 102, 103, 104, 105, 106, 107, 109, 110, 111, 112, 113, 114, 115, 117, 118, 119, 120, 121, 122, 123, 125, 126, 127, 128, 129, 130, 131], dtype='int')
        self.beamY.auxvY1 = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124], dtype='int')
        self.beamStair.auxvStair1 = 20104
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 8
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        self.beamX.Ainf1 = np.array([(ax)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), 0, (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay), (ax)*(ay), (ax)*(ay), (astair)*(ay/2), (ax)*(ay), (ax)*(ay), (ax)*(ay), 
                                    (ax)*(ay), (ax)*(ay), (ax)*(ay), (astair)*(ay), (ax)*(ay), (ax)*(ay), (ax)*(ay), (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (astair)*(ay/2), (ax)*(ay/2), (ax)*(ay/2), (ax)*(ay/2)])
        self.beamX.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamY.Ainf1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamY.Astair1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slaborient = 2 - Unloading in Y beams
        self.beamX.Ainf2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamX.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        self.beamY.Ainf2 = np.array([(ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), 
                                    (ax)*(ay), (ax)*(ay), (ax/2)*(ay), (ax/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2+astair/2)*(ay), (ax/2+astair/2)*(ay), (ax)*(ay), (ax)*(ay), (ax/2)*(ay)])
        self.beamY.Astair2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay and ay >= astair:
            a1 = (ax-2*ay/2)*(ay/2) + 2*(ay/2)*(ay/2)/2
            a2 = (astair)*(astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a1, a1, 0, a1, a1, a1, 2*a1, 2*a1, 2*a1, a2, 2*a1, 2*a1, 2*a1, 2*a1, 2*a1, 2*a1, 2*a2, 2*a1, 2*a1, 2*a1, a1, a1, a1, a2, a1, a1, a1])
            self.beamX.a_over_l = np.array([(ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.0, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 
                                           (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax, 0.5, (ay/2)/ax, (ay/2)/ax, (ay/2)/ax])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            a11 = (ay)*(ay/2)/2
            a12 = (ay)*(ay/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamY.Ainf3 = np.array([a11, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a12, a12, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a12, a12, 2*a11, 2*a11, a11])
            self.beamY.a_over_l = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.50, 0.5, 0.5, 0.50, 0.5, (astair/2)/ay, (astair/2)/ay, 0.50, 0.50, 0.50, 0.5, 0.50, 0.5, (astair/2)/ay, (astair/2)/ay, 0.50, 0.50, 0.50])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay and ay >= astair:
            a1 = (ax)*(ax/2)/2
            a2 = (astair)*(astair/2)/2
            a11 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2
            a12 = (ay-2*ax/2)*(ax/2) + 2*(ax/2)*(ax/2)/2 + astair/2*(ay-2*astair/2)+2*(astair/2*astair/2)/2
            self.beamX.Ainf3 = np.array([a1, a1, a1, 0, a1, a1, a1, 2*a1, 2*a1, 2*a1, a2, 2*a1, 2*a1, 2*a1, 2*a1, 2*a1, 2*a1, 2*a2, 2*a1, 2*a1, 2*a1, a1, a1, a1, a2, a1, a1, a1])
            self.beamX.a_over_l = np.array([0.50, 0.50, 0.50, 0, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50])
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            self.beamY.Ainf3 = np.array([a11, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a12, a12, 2*a11, 2*a11, a11, a11, 2*a11, 2*a11, a12, a12, 2*a11, 2*a11, a11])
            self.beamY.a_over_l = np.array([(ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, 
                                            (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay])
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        # Else is not possible as ax is always greater than astair maybe clean up is required here

        self.beamX.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ay/2*astair, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2*astair 
        self.beamY.Astair3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Dimension of the spans of the beams
        self.beamX.L = np.array([ax, ax, ax, astair, ax, ax, ax, ax, ax, ax, astair, ax, ax, ax, ax, ax, ax, astair, ax, ax, ax, ax, ax, ax, astair, ax, ax, ax])
        self.beamStair.L = astair
        self.beamY.L = np.array([ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay, ay])

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])
        self.beamStair.pwallsA = 0.50
        self.beamY.pwallsA = np.array([1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1])

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 4, 2, 2, 2, 2, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 17, 18, 19, 20, 21, 22, 23]
        self.general.floor_truss_nodej_ref = [10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 9, 10, 11, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 26, 27, 28, 29, 30, 31, 32]
        self.general.roof_truss_nodei_ref = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 17, 18, 19, 20, 21, 22, 23, 4, 5]
        self.general.roof_truss_nodej_ref = [10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 9, 10, 11, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 26, 27, 28, 29, 30, 31, 32, 13, 12]
        self.general.truss_stiffness = 10000000000 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 32 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]


    def _b07(self):
        """
        Building B07 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B07 - Needs to be changed for different buildings
        nextarbaysX = 2
        nextarbaysY = 2
        self.general.number_of_alignmentsX = nextarbaysX + 2
        self.general.number_of_alignmentsY = nextarbaysY + 1
        self.general.Reference = np.arange(1, 4 * (nextarbaysY + 2) + 1)
        
        # 2) Plan configuration
        planX = [0, astair, astair+ax, astair+ax+ax]
        planY = [ay * i for i in range(nextarbaysY + 2)]
        self.general.Plan = None
        for j in range(nextarbaysY + 2):
            for i in range(4):
                if self.general.Plan is not None:
                    self.general.Plan = np.append(self.general.Plan, np.array([[planX[i], planY[j]]]), axis = 0)
                else:
                    self.general.Plan = np.array([[planX[i], planY[j]]])
        
        # 3) Column names including the two-sub-columns of the staircase
        colname1 = np.array([101, 20101, 102, 20102, 103, 104], dtype='int')
        colname2 = np.arange(105, 104 + 4 * (nextarbaysY + 1) + 1)
        colnamesref = np.append(colname1, colname2)
        self.column.nameref = np.zeros((8,len(colnamesref)), dtype='int')
        for i in range(8):
            self.column.nameref[i, :] = colnamesref + 100 * i

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        elasCnodeiref1 = np.array([1, 20101, 2, 20102, 3, 4], dtype='int')
        elasCnodeiref2 = np.arange(5, 4 * (nextarbaysY + 2) + 1)
        elasCnodeiref = np.append(elasCnodeiref1, elasCnodeiref2)
        self.column.elasCnodeiref = np.zeros((8,len(elasCnodeiref)), dtype='int')
        for i in range(8):
            self.column.elasCnodeiref[i, :] = elasCnodeiref + 100 * i

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        elasCnodejref1 = np.array([20101, 101, 20102, 102, 103, 104], dtype='int')
        elasCnodejref2 = np.arange(105, 104 + 4 * (nextarbaysY + 1) + 1)
        elasCnodejref = np.append(elasCnodejref1, elasCnodejref2)
        self.column.elasCnodejref = np.zeros((8,len(elasCnodejref)), dtype='int')
        for i in range(8):
            self.column.elasCnodejref[i, :] = elasCnodejref + 100 * i

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        Ainfref0 = np.array([0, 0, (ax/2)*(ay/2), (ax/2)*(ay/2), ax*(ay/2), (ax/2)*(ay/2)])
        Ainfref1 = np.array([(astair/2)*(ay/2), (ax/2)*ay+(astair/2)*(ay/2), ax*(ay), (ax/2)*(ay)])
        Ainfint = np.array([ay*astair/2, (astair/2+ax/2)*ay, ay*ax, (ax/2)*(ay)] * (nextarbaysY-1))
        Ainfend = np.array([(astair/2)*(ay/2), (astair/2+ax/2)*(ay/2), (ay/2)*(ax), (ax/2)*(ay/2)])
        self.column.Ainfref = np.hstack((Ainfref0, Ainfref1, Ainfint, Ainfend))
        # ...........................................................................
        Astairref0 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), 0, 0])
        Astairref1 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), 0, 0])
        Astairint = np.array([0, 0, 0, 0] * (nextarbaysY-1))
        Astairend = np.array([0, 0, 0, 0])
        self.column.Astairref = np.hstack((Astairref0, Astairref1, Astairint, Astairend))
        # ...........................................................................
        Aroofref0 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), ax*(ay/2), (ax/2)*(ay/2)])
        Aroofref1 = np.array([(astair/2)*(ay/2), (ax/2)*ay+(astair/2)*(ay), ax*(ay), (ax/2)*(ay)])
        Aroofint = np.array([ay*astair/2, (astair/2+ax/2)*ay, ay*ax, (ax/2)*(ay)] * (nextarbaysY-1))
        Aroofend = np.array([(astair/2)*(ay/2), (astair/2+ax/2)*(ay/2), (ay/2)*(ax), (ax/2)*(ay/2)])
        self.column.Aroofref = np.hstack((Aroofref0, Aroofref1, Aroofint, Aroofend))
        # ...........................................................................
        ncols_bot_end11 = np.array([1.3, 1.3, 1.3, 1.3, 1.3, 1.3])
        ncols_bot_end12 = np.array([1.3, 1.3, 1.3, 1.3])
        ncols_bot_int1 = np.array([1.3, 1.1, 1.1, 1.3] * nextarbaysY)
        ncols_bot1 = np.hstack((ncols_bot_end11, ncols_bot_int1, ncols_bot_end12))
        # ...........................................................................
        ncols_bot_end21 = np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
        ncols_bot_end22 = np.array([1.5, 1.5, 1.5, 1.5])
        ncols_bot_int2 = np.array([1.5, 1.3, 1.3, 1.5] * nextarbaysY)
        ncols_bot2 = np.hstack((ncols_bot_end21, ncols_bot_int2, ncols_bot_end22)) 
        self.column.positionfactor_ref = np.vstack((ncols_bot1, ncols_bot2))
        # ...........................................................................
        if nextarbaysX == 2:
            if nextarbaysY == 2:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 15, 16, 17, 18], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 3:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 19, 20, 21, 22], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 4:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 21, 23, 24, 25, 26], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 5:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 21, 25, 27, 28, 29, 30], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22, 23, 24, 26], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        Lref1 = np.array([0.50, 0.50, 0.50, 0.50, 1, 1])
        Lref2 = np.array([1, 1, 1, 1] * (nextarbaysY+1))
        self.column.Lref = np.hstack((Lref1, Lref2))
        # ...........................................................................
        wall_legth1=np.array([astair/2+ay/2, astair/2+ay/2, astair/2+ay/2+ax/2, astair/2+ay/2+ax/2, ax, ax+ay/2])
        wall_legth2=np.array([ay/2, ay/2+ax/2, 0, ay])
        wall_legthend=np.array([astair/2, astair/2+ax/2, ax, ax])
        walls = np.array([ay, 0, 0, ay] * (nextarbaysY-1))
        self.column.walllength = np.hstack((wall_legth1, wall_legth2, walls, wall_legthend))
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 1
        self.general.stair_node_right_mirror_1st_storey = 2
        self.general.stairXleft = 0
        self.general.stairXright = astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([], dtype='int') # to define the different continuous beams
        for i in range(nextarbaysY+2):
            self.beamX.index = np.append(self.beamX.index, (i+2) * np.ones(3, dtype='int')) 
        self.beamY.index = np.array([2, 3, 4, 5] * (nextarbaysY+1), dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50100 + len(self.beamX.index) + 1, dtype='int')  # beamX names
        self.beamY.auxvY = np.arange(50151, 50150 + len(self.beamY.index) + 1, dtype='int')  # beamY names
        self.beamStair.auxvStair = 51101  # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([], dtype='int') # beam initial nodes in XX
        for i in range(nextarbaysY+2):
            aux1 = 101 + 4 * i
            self.beamX.auxvX1 = np.append(self.beamX.auxvX1, np.array([aux1, aux1+1, aux1+2], dtype='int'))
        self.beamY.auxvY1 = np.arange(101, 104 + nextarbaysY*4 + 1, dtype='int')
        self.beamStair.auxvStair1 = 20101
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 4
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        Ainf1X = [0, ax*ay/2, ax*ay/2]
        Ainf2X = [astair*ay/2, (ax*ay), (ax*ay)]
        Ainf3X = [(astair*ay), (ax*ay), (ax*ay)] * (nextarbaysY-1)
        Ainf4X = [(astair*astair/2)/2, (ax*ay/2), (ax*ay/2)]
        Astair3x1 = [ay/2*astair, 0, 0, ay/2*astair, 0, 0]
        Astair2x2 = [0, 0, 0] * nextarbaysY
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamX.Astair1 = np.array(Astair3x1 + Astair2x2)
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamX.Ainf1 = np.array(Ainf1X + Ainf2X + Ainf3X + Ainf4X)
        self.beamY.Astair1 = Astair3y.flatten()
        self.beamY.Ainf1 = Astair3y.flatten()
  
        # Case slaborient = 2 - Unloading in Y beams
        Astair3x = np.zeros((3, nextarbaysY+2))
        self.beamX.Astair2 = Astair3x.flatten()
        self.beamX.Ainf2 = Astair3x.flatten()
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamY.Astair2 = Astair3y.flatten()
        ainf2y1 = [0, ay*ax/2, ay*ax, ay*ax/2]
        ainf2y2 = [astair/2*ay, ay*ax/2+ay*astair/2, ay*ax, ay*ax/2] * nextarbaysY
        self.beamY.Ainf2 = np.array(ainf2y1 + ainf2y2)
        self.beamY.Astair2 = self.beamY.Astair1.copy()

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay:
            d1 = ax-2*(ay/2)
            a1 = (ay/2*ay/2)/2 + d1*ay/2 + (ay/2*ay/2)/2
            a2 = 2*a1
            Ainf1 = [0, a1, a1]
            a_over_l1 = [0, (ay/2)/ax, (ay/2)/ax]
            Ainf2 = [(astair*astair/2)/2,  a2, a2]
            a_over_l2 = [0.50, (ay/2)/ax, (ay/2)/ax]
            Ainf3 = [2*(astair*astair/2)/2, a2, a2] * (nextarbaysY-1)
            a_over_l3 = [0.50, (ay/2)/ax, (ay/2)/ax] * (nextarbaysY-1)
            Ainf4 = [(astair*astair/2)/2, a1, a1]
            a_over_l4 = [0.50, (ay/2)/ax, (ay/2)/ax]
            self.beamX.Ainf3 = np.array(Ainf1 + Ainf2 + Ainf3 + Ainf4)
            self.beamX.a_over_l = np.array(a_over_l1 + a_over_l2 + a_over_l3 + a_over_l4)
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            # ...........................................................................
            d1 = ay-2*(astair/2)
            a1 = (ay/2*astair/2)/2 + (d1*astair/2) + (ay/2*astair/2)/2
            a2 = 2*(ay/2*ay/2)/2
            a3 = a1 + a2
            Ainf1 = [0, a2, 2*a2, a2]
            a_over_l1 = [0, 0.5, 0.5, 0.5]
            Ainf2 = [a1, a3, 2*a2, a2] * nextarbaysY
            a_over_l2 = [(astair/2)/ay, 0.5, 0.5, 0.5] * nextarbaysY
            self.beamY.Ainf3 = np.array(Ainf1 + Ainf2)
            self.beamY.a_over_l = np.array(a_over_l1 + a_over_l2)
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay:
            a1 = 2*(ax/2*ax/2)/2
            a2 = 2*a1
            Ainf1 = [0, a1, a1]
            a_over_l1 = [0, 0.5, 0.5]
            Ainf2 = [2*(astair/2*astair/2)/2,  a2, a2]
            a_over_l2 = [0.50, 0.50, 0.50]
            Ainf3 = [2*(astair*astair/2)/2, a2, a2] * (nextarbaysY-1)
            a_over_l3 = [0.50, 0.50, 0.50] * (nextarbaysY-1)
            Ainf4 = [(astair*astair/2)/2, a1, a1]
            a_over_l4 = [0.50, 0.50, 0.50]
            self.beamX.Ainf3 = np.array(Ainf1 + Ainf2 + Ainf3 + Ainf4)
            self.beamX.a_over_l = np.array(a_over_l1 + a_over_l2 + a_over_l3 + a_over_l4)
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            # ...........................................................................
            aux2 = (ay-ax/2)*ax/2
            aux3 = (ay-astair/2)*astair/2
            Ainf1 = [0, aux2, 2*aux2, aux2]
            a_over_l1 = [0, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay]
            Ainf2 = [aux3, aux2+aux3, 2*aux2, aux2] * nextarbaysY
            a_over_l2 = [(astair/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay] * nextarbaysY
            self.beamY.Ainf3 = np.array(Ainf1 + Ainf2)
            self.beamY.a_over_l = np.array(a_over_l1 + a_over_l2)
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)

        Astair3x1 = [ay/2*astair, 0, 0, ay/2*astair, 0, 0]
        Astair2x2 = [0, 0, 0] * nextarbaysY
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamX.Astair3 = np.array(Astair3x1 + Astair2x2)
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2*astair
        self.beamY.Astair3 = Astair3y.flatten()

        # Dimension of the spans of the beams
        self.beamX.L = np.array([astair, ax, ax] * (nextarbaysY+2))
        self.beamStair.L = astair
        lyy = ay * np.ones((4, nextarbaysY+1))
        self.beamY.L = lyy.flatten()

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([0, 1, 1] + [0, 0, 0] * nextarbaysY + [1, 1, 1])
        self.beamStair.pwallsA = 0.5
        self.beamY.pwallsA = np.array([1, 1, 0, 0] + [1, 0, 0, 1] * nextarbaysY)

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 3, 0, 0, 4, 3, 0, 0, 4, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [2, 3, 5, 6, 7, 9, 10, 11, 3, 4, 6, 7, 8, 10, 11, 12]
        self.general.floor_truss_nodej_ref = [7, 8, 10, 11, 12, 14, 15, 16, 6, 7, 9, 10, 11, 13, 14, 15]
        self.general.roof_truss_nodei_ref = [2, 3, 5, 6, 7, 9, 10, 11, 3, 4, 6, 7, 8, 10, 11, 12]
        self.general.roof_truss_nodej_ref = [7, 8, 10, 11, 12, 14, 15, 16, 6, 7, 9, 10, 11, 13, 14, 15]
        self.general.truss_stiffness = 10.e12 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        # originally both values below were 32 (fixed)
        self.general.nonlin_diaph_nodeid_max = 16 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]
        

    def _b08(self):
        """
        Building B08 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B08 - Needs to be changed for different buildings
        nextarbaysX = 2
        nextarbaysY = 3
        self.general.number_of_alignmentsX = nextarbaysX + 2
        self.general.number_of_alignmentsY = nextarbaysY + 1
        self.general.Reference = np.arange(1, 4 * (nextarbaysY + 2) + 1)
        
        # 2) Plan configuration
        planX = [0, astair, astair+ax, astair+ax+ax]
        planY = [ay * i for i in range(nextarbaysY + 2)]
        self.general.Plan = None
        for j in range(nextarbaysY + 2):
            for i in range(4):
                if self.general.Plan is not None:
                    self.general.Plan = np.append(self.general.Plan, np.array([[planX[i], planY[j]]]), axis = 0)
                else:
                    self.general.Plan = np.array([[planX[i], planY[j]]])
        
        # 3) Column names including the two-sub-columns of the staircase
        colname1 = np.array([101, 20101, 102, 20102, 103, 104], dtype='int')
        colname2 = np.arange(105, 104 + 4 * (nextarbaysY + 1) + 1)
        colnamesref = np.append(colname1, colname2)
        self.column.nameref = np.zeros((8,len(colnamesref)), dtype='int')
        for i in range(8):
            self.column.nameref[i, :] = colnamesref + 100 * i

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        elasCnodeiref1 = np.array([1, 20101, 2, 20102, 3, 4], dtype='int')
        elasCnodeiref2 = np.arange(5, 4 * (nextarbaysY + 2) + 1)
        elasCnodeiref = np.append(elasCnodeiref1, elasCnodeiref2)
        self.column.elasCnodeiref = np.zeros((8,len(elasCnodeiref)), dtype='int')
        for i in range(8):
            self.column.elasCnodeiref[i, :] = elasCnodeiref + 100 * i

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        elasCnodejref1 = np.array([20101, 101, 20102, 102, 103, 104], dtype='int')
        elasCnodejref2 = np.arange(105, 104 + 4 * (nextarbaysY + 1) + 1)
        elasCnodejref = np.append(elasCnodejref1, elasCnodejref2)
        self.column.elasCnodejref = np.zeros((8,len(elasCnodejref)), dtype='int')
        for i in range(8):
            self.column.elasCnodejref[i, :] = elasCnodejref + 100 * i

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        Ainfref0 = np.array([0, 0, (ax/2)*(ay/2), (ax/2)*(ay/2), ax*(ay/2), (ax/2)*(ay/2)])
        Ainfref1 = np.array([(astair/2)*(ay/2), (ax/2)*ay+(astair/2)*(ay/2), ax*(ay), (ax/2)*(ay)])
        Ainfint = np.array([ay*astair/2, (astair/2+ax/2)*ay, ay*ax, (ax/2)*(ay)] * (nextarbaysY-1))
        Ainfend = np.array([(astair/2)*(ay/2), (astair/2+ax/2)*(ay/2), (ay/2)*(ax), (ax/2)*(ay/2)])
        self.column.Ainfref = np.hstack((Ainfref0, Ainfref1, Ainfint, Ainfend))
        # ...........................................................................
        Astairref0 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), 0, 0])
        Astairref1 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), 0, 0])
        Astairint = np.array([0, 0, 0, 0] * (nextarbaysY-1))
        Astairend = np.array([0, 0, 0, 0])
        self.column.Astairref = np.hstack((Astairref0, Astairref1, Astairint, Astairend))
        # ...........................................................................
        Aroofref0 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), ax*(ay/2), (ax/2)*(ay/2)])
        Aroofref1 = np.array([(astair/2)*(ay/2), (ax/2)*ay+(astair/2)*(ay), ax*(ay), (ax/2)*(ay)])
        Aroofint = np.array([ay*astair/2, (astair/2+ax/2)*ay, ay*ax, (ax/2)*(ay)] * (nextarbaysY-1))
        Aroofend = np.array([(astair/2)*(ay/2), (astair/2+ax/2)*(ay/2), (ay/2)*(ax), (ax/2)*(ay/2)])
        self.column.Aroofref = np.hstack((Aroofref0, Aroofref1, Aroofint, Aroofend))
        # ...........................................................................
        ncols_bot_end11 = np.array([1.3, 1.3, 1.3, 1.3, 1.3, 1.3])
        ncols_bot_end12 = np.array([1.3, 1.3, 1.3, 1.3])
        ncols_bot_int1 = np.array([1.3, 1.1, 1.1, 1.3] * nextarbaysY)
        ncols_bot1 = np.hstack((ncols_bot_end11, ncols_bot_int1, ncols_bot_end12))
        # ...........................................................................
        ncols_bot_end21 = np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
        ncols_bot_end22 = np.array([1.5, 1.5, 1.5, 1.5])
        ncols_bot_int2 = np.array([1.5, 1.3, 1.3, 1.5] * nextarbaysY)
        ncols_bot2 = np.hstack((ncols_bot_end21, ncols_bot_int2, ncols_bot_end22)) 
        self.column.positionfactor_ref = np.vstack((ncols_bot1, ncols_bot2))
        # ...........................................................................
        self.column.Colindex1 = np.array([1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
        self.column.Colindex2 = np.array([5, 6, 17, 18, 19, 20, 21, 22], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        Lref1 = np.array([0.50, 0.50, 0.50, 0.50, 1, 1])
        Lref2 = np.array([1, 1, 1, 1] * (nextarbaysY+1))
        self.column.Lref = np.hstack((Lref1, Lref2))
        # ...........................................................................
        wall_legth1=np.array([astair/2+ay/2, astair/2+ay/2, astair/2+ay/2+ax/2, astair/2+ay/2+ax/2, ax, ax+ay/2])
        wall_legth2=np.array([ay/2, ay/2+ax/2, 0, ay])
        wall_legthend=np.array([astair/2, astair/2+ax/2, ax, ax])
        walls = np.array([ay, 0, 0, ay] * (nextarbaysY-1))
        self.column.walllength = np.hstack((wall_legth1, wall_legth2, walls, wall_legthend))
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 1
        self.general.stair_node_right_mirror_1st_storey = 2
        self.general.stairXleft = 0
        self.general.stairXright = astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([], dtype='int') # to define the different continuous beams
        for i in range(nextarbaysY+2):
            self.beamX.index = np.append(self.beamX.index, (i+2) * np.ones(3, dtype='int')) 
        self.beamY.index = np.array([2, 3, 4, 5] * (nextarbaysY+1), dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50100 + len(self.beamX.index) + 1, dtype='int')  # beamX names
        self.beamY.auxvY = np.arange(50151, 50150 + len(self.beamY.index) + 1, dtype='int')  # beamY names
        self.beamStair.auxvStair = 51101  # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([], dtype='int') # beam initial nodes in XX
        for i in range(nextarbaysY+2):
            aux1 = 101 + 4 * i
            self.beamX.auxvX1 = np.append(self.beamX.auxvX1, np.array([aux1, aux1+1, aux1+2], dtype='int'))
        self.beamY.auxvY1 = np.arange(101, 104 + nextarbaysY*4 + 1, dtype='int')
        self.beamStair.auxvStair1 = 20101
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 4
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        Ainf1X = [0, ax*ay/2, ax*ay/2]
        Ainf2X = [astair*ay/2, (ax*ay), (ax*ay)]
        Ainf3X = [(astair*ay), (ax*ay), (ax*ay)] * (nextarbaysY-1)
        Ainf4X = [(astair*astair/2)/2, (ax*ay/2), (ax*ay/2)]
        Astair3x1 = [ay/2*astair, 0, 0, ay/2*astair, 0, 0]
        Astair2x2 = [0, 0, 0] * nextarbaysY
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamX.Astair1 = np.array(Astair3x1 + Astair2x2)
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamX.Ainf1 = np.array(Ainf1X + Ainf2X + Ainf3X + Ainf4X)
        self.beamY.Astair1 = Astair3y.flatten()
        self.beamY.Ainf1 = Astair3y.flatten()
  
        # Case slaborient = 2 - Unloading in Y beams
        Astair3x = np.zeros((3, nextarbaysY+2))
        self.beamX.Astair2 = Astair3x.flatten()
        self.beamX.Ainf2 = Astair3x.flatten()
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamY.Astair2 = Astair3y.flatten()
        ainf2y1 = [0, ay*ax/2, ay*ax, ay*ax/2]
        ainf2y2 = [astair/2*ay, ay*ax/2+ay*astair/2, ay*ax, ay*ax/2] * nextarbaysY
        self.beamY.Ainf2 = np.array(ainf2y1 + ainf2y2)
        self.beamY.Astair2 = self.beamY.Astair1.copy()

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay:
            d1 = ax-2*(ay/2)
            a1 = (ay/2*ay/2)/2 + d1*ay/2 + (ay/2*ay/2)/2
            a2 = 2*a1
            Ainf1 = [0, a1, a1]
            a_over_l1 = [0, (ay/2)/ax, (ay/2)/ax]
            Ainf2 = [(astair*astair/2)/2,  a2, a2]
            a_over_l2 = [0.50, (ay/2)/ax, (ay/2)/ax]
            Ainf3 = [2*(astair*astair/2)/2, a2, a2] * (nextarbaysY-1)
            a_over_l3 = [0.50, (ay/2)/ax, (ay/2)/ax] * (nextarbaysY-1)
            Ainf4 = [(astair*astair/2)/2, a1, a1]
            a_over_l4 = [0.50, (ay/2)/ax, (ay/2)/ax]
            self.beamX.Ainf3 = np.array(Ainf1 + Ainf2 + Ainf3 + Ainf4)
            self.beamX.a_over_l = np.array(a_over_l1 + a_over_l2 + a_over_l3 + a_over_l4)
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            # ...........................................................................
            d1 = ay-2*(astair/2)
            a1 = (ay/2*astair/2)/2 + (d1*astair/2) + (ay/2*astair/2)/2
            a2 = 2*(ay/2*ay/2)/2
            a3 = a1 + a2
            Ainf1 = [0, a2, 2*a2, a2]
            a_over_l1 = [0, 0.5, 0.5, 0.5]
            Ainf2 = [a1, a3, 2*a2, a2] * nextarbaysY
            a_over_l2 = [(astair/2)/ay, 0.5, 0.5, 0.5] * nextarbaysY
            self.beamY.Ainf3 = np.array(Ainf1 + Ainf2)
            self.beamY.a_over_l = np.array(a_over_l1 + a_over_l2)
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay:
            a1 = 2*(ax/2*ax/2)/2
            a2 = 2*a1
            Ainf1 = [0, a1, a1]
            a_over_l1 = [0, 0.5, 0.5]
            Ainf2 = [2*(astair/2*astair/2)/2,  a2, a2]
            a_over_l2 = [0.50, 0.50, 0.50]
            Ainf3 = [2*(astair*astair/2)/2, a2, a2] * (nextarbaysY-1)
            a_over_l3 = [0.50, 0.50, 0.50] * (nextarbaysY-1)
            Ainf4 = [(astair*astair/2)/2, a1, a1]
            a_over_l4 = [0.50, 0.50, 0.50]
            self.beamX.Ainf3 = np.array(Ainf1 + Ainf2 + Ainf3 + Ainf4)
            self.beamX.a_over_l = np.array(a_over_l1 + a_over_l2 + a_over_l3 + a_over_l4)
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            # ...........................................................................
            aux2 = (ay-ax/2)*ax/2
            aux3 = (ay-astair/2)*astair/2
            Ainf1 = [0, aux2, 2*aux2, aux2]
            a_over_l1 = [0, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay]
            Ainf2 = [aux3, aux2+aux3, 2*aux2, aux2] * nextarbaysY
            a_over_l2 = [(astair/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay] * nextarbaysY
            self.beamY.Ainf3 = np.array(Ainf1 + Ainf2)
            self.beamY.a_over_l = np.array(a_over_l1 + a_over_l2)
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)

        Astair3x1 = [ay/2*astair, 0, 0, ay/2*astair, 0, 0]
        Astair2x2 = [0, 0, 0] * nextarbaysY
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamX.Astair3 = np.array(Astair3x1 + Astair2x2)
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2*astair
        self.beamY.Astair3 = Astair3y.flatten()

        # Dimension of the spans of the beams
        self.beamX.L = np.array([astair, ax, ax] * (nextarbaysY+2))
        self.beamStair.L = astair
        lyy = ay * np.ones((4, nextarbaysY+1))
        self.beamY.L = lyy.flatten()

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([0, 1, 1] + [0, 0, 0] * nextarbaysY + [1, 1, 1])
        self.beamStair.pwallsA = 0.5
        self.beamY.pwallsA = np.array([1, 1, 0, 0] + [1, 0, 0, 1] * nextarbaysY)

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 3, 0, 0, 4, 3, 0, 0, 4, 3, 0, 0, 4, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16]
        self.general.floor_truss_nodej_ref = [7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19]
        self.general.roof_truss_nodei_ref = [2, 3, 5, 6, 7, 9, 10, 11, 2, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 14, 15, 16]
        self.general.roof_truss_nodej_ref = [7, 8, 10, 11, 12, 14, 15, 16, 5, 7, 9, 10, 11, 13, 14, 15, 18, 19, 20, 17, 18, 19]
        self.general.truss_stiffness = 10.e12 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 20 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]


    def _b09(self):
        """
        Building B09 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B09 - Needs to be changed for different buildings
        nextarbaysX = 2
        nextarbaysY = 4
        self.general.number_of_alignmentsX = nextarbaysX + 2
        self.general.number_of_alignmentsY = nextarbaysY + 1
        self.general.Reference = np.arange(1, 4 * (nextarbaysY + 2) + 1)
        
        # 2) Plan configuration
        planX = [0, astair, astair+ax, astair+ax+ax]
        planY = [ay * i for i in range(nextarbaysY + 2)]
        self.general.Plan = None
        for j in range(nextarbaysY + 2):
            for i in range(4):
                if self.general.Plan is not None:
                    self.general.Plan = np.append(self.general.Plan, np.array([[planX[i], planY[j]]]), axis = 0)
                else:
                    self.general.Plan = np.array([[planX[i], planY[j]]])
        
        # 3) Column names including the two-sub-columns of the staircase
        colname1 = np.array([101, 20101, 102, 20102, 103, 104], dtype='int')
        colname2 = np.arange(105, 104 + 4 * (nextarbaysY + 1) + 1)
        colnamesref = np.append(colname1, colname2)
        self.column.nameref = np.zeros((8,len(colnamesref)), dtype='int')
        for i in range(8):
            self.column.nameref[i, :] = colnamesref + 100 * i

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        elasCnodeiref1 = np.array([1, 20101, 2, 20102, 3, 4], dtype='int')
        elasCnodeiref2 = np.arange(5, 4 * (nextarbaysY + 2) + 1)
        elasCnodeiref = np.append(elasCnodeiref1, elasCnodeiref2)
        self.column.elasCnodeiref = np.zeros((8,len(elasCnodeiref)), dtype='int')
        for i in range(8):
            self.column.elasCnodeiref[i, :] = elasCnodeiref + 100 * i

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        elasCnodejref1 = np.array([20101, 101, 20102, 102, 103, 104], dtype='int')
        elasCnodejref2 = np.arange(105, 104 + 4 * (nextarbaysY + 1) + 1)
        elasCnodejref = np.append(elasCnodejref1, elasCnodejref2)
        self.column.elasCnodejref = np.zeros((8,len(elasCnodejref)), dtype='int')
        for i in range(8):
            self.column.elasCnodejref[i, :] = elasCnodejref + 100 * i

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        Ainfref0 = np.array([0, 0, (ax/2)*(ay/2), (ax/2)*(ay/2), ax*(ay/2), (ax/2)*(ay/2)])
        Ainfref1 = np.array([(astair/2)*(ay/2), (ax/2)*ay+(astair/2)*(ay/2), ax*(ay), (ax/2)*(ay)])
        Ainfint = np.array([ay*astair/2, (astair/2+ax/2)*ay, ay*ax, (ax/2)*(ay)] * (nextarbaysY-1))
        Ainfend = np.array([(astair/2)*(ay/2), (astair/2+ax/2)*(ay/2), (ay/2)*(ax), (ax/2)*(ay/2)])
        self.column.Ainfref = np.hstack((Ainfref0, Ainfref1, Ainfint, Ainfend))
        # ...........................................................................
        Astairref0 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), 0, 0])
        Astairref1 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), 0, 0])
        Astairint = np.array([0, 0, 0, 0] * (nextarbaysY-1))
        Astairend = np.array([0, 0, 0, 0])
        self.column.Astairref = np.hstack((Astairref0, Astairref1, Astairint, Astairend))
        # ...........................................................................
        Aroofref0 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), ax*(ay/2), (ax/2)*(ay/2)])
        Aroofref1 = np.array([(astair/2)*(ay/2), (ax/2)*ay+(astair/2)*(ay), ax*(ay), (ax/2)*(ay)])
        Aroofint = np.array([ay*astair/2, (astair/2+ax/2)*ay, ay*ax, (ax/2)*(ay)] * (nextarbaysY-1))
        Aroofend = np.array([(astair/2)*(ay/2), (astair/2+ax/2)*(ay/2), (ay/2)*(ax), (ax/2)*(ay/2)])
        self.column.Aroofref = np.hstack((Aroofref0, Aroofref1, Aroofint, Aroofend))
        # ...........................................................................
        ncols_bot_end11 = np.array([1.3, 1.3, 1.3, 1.3, 1.3, 1.3])
        ncols_bot_end12 = np.array([1.3, 1.3, 1.3, 1.3])
        ncols_bot_int1 = np.array([1.3, 1.1, 1.1, 1.3] * nextarbaysY)
        ncols_bot1 = np.hstack((ncols_bot_end11, ncols_bot_int1, ncols_bot_end12))
        # ...........................................................................
        ncols_bot_end21 = np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
        ncols_bot_end22 = np.array([1.5, 1.5, 1.5, 1.5])
        ncols_bot_int2 = np.array([1.5, 1.3, 1.3, 1.5] * nextarbaysY)
        ncols_bot2 = np.hstack((ncols_bot_end21, ncols_bot_int2, ncols_bot_end22)) 
        self.column.positionfactor_ref = np.vstack((ncols_bot1, ncols_bot2))
        # ...........................................................................
        if nextarbaysX == 2:
            if nextarbaysY == 2:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 15, 16, 17, 18], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 3:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 19, 20, 21, 22], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 4:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 21, 23, 24, 25, 26], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 5:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 21, 25, 27, 28, 29, 30], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22, 23, 24, 26], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
        Lref1 = np.array([0.50, 0.50, 0.50, 0.50, 1, 1])
        Lref2 = np.array([1, 1, 1, 1] * (nextarbaysY+1))
        self.column.Lref = np.hstack((Lref1, Lref2))
        # ...........................................................................
        wall_legth1=np.array([astair/2+ay/2, astair/2+ay/2, astair/2+ay/2+ax/2, astair/2+ay/2+ax/2, ax, ax+ay/2])
        wall_legth2=np.array([ay/2, ay/2+ax/2, 0, ay])
        wall_legthend=np.array([astair/2, astair/2+ax/2, ax, ax])
        walls = np.array([ay, 0, 0, ay] * (nextarbaysY-1))
        self.column.walllength = np.hstack((wall_legth1, wall_legth2, walls, wall_legthend))
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 1
        self.general.stair_node_right_mirror_1st_storey = 2
        self.general.stairXleft = 0
        self.general.stairXright = astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([], dtype='int') # to define the different continuous beams
        for i in range(nextarbaysY+2):
            self.beamX.index = np.append(self.beamX.index, (i+2) * np.ones(3, dtype='int'))
        self.beamY.index = np.array([2, 3, 4, 5] * (nextarbaysY+1), dtype='int') # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50100 + len(self.beamX.index) + 1, dtype='int')  # beamX names
        self.beamY.auxvY = np.arange(50151, 50150 + len(self.beamY.index) + 1, dtype='int')  # beamY names
        self.beamStair.auxvStair = 51101  # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([], dtype='int') # beam initial nodes in XX
        for i in range(nextarbaysY+2):
            aux1 = 101 + 4 * i
            self.beamX.auxvX1 = np.append(self.beamX.auxvX1, np.array([aux1, aux1+1, aux1+2], dtype='int'))
        self.beamY.auxvY1 = np.arange(101, 104 + nextarbaysY*4 + 1, dtype='int')
        self.beamStair.auxvStair1 = 20101
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 4
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        Ainf1X = [0, ax*ay/2, ax*ay/2]
        Ainf2X = [astair*ay/2, (ax*ay), (ax*ay)]
        Ainf3X = [(astair*ay), (ax*ay), (ax*ay)] * (nextarbaysY-1)
        Ainf4X = [(astair*astair/2)/2, (ax*ay/2), (ax*ay/2)]
        Astair3x1 = [ay/2*astair, 0, 0, ay/2*astair, 0, 0]
        Astair2x2 = [0, 0, 0] * nextarbaysY
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamX.Astair1 = np.array(Astair3x1 + Astair2x2)
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamX.Ainf1 = np.array(Ainf1X + Ainf2X + Ainf3X + Ainf4X)
        self.beamY.Astair1 = Astair3y.flatten()
        self.beamY.Ainf1 = Astair3y.flatten()
  
        # Case slaborient = 2 - Unloading in Y beams
        Astair3x = np.zeros((3, nextarbaysY+2))
        self.beamX.Astair2 = Astair3x.flatten()
        self.beamX.Ainf2 = Astair3x.flatten()
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamY.Astair2 = Astair3y.flatten()
        ainf2y1 = [0, ay*ax/2, ay*ax, ay*ax/2]
        ainf2y2 = [astair/2*ay, ay*ax/2+ay*astair/2, ay*ax, ay*ax/2] * nextarbaysY
        self.beamY.Ainf2 = np.array(ainf2y1 + ainf2y2)
        self.beamY.Astair2 = self.beamY.Astair1.copy()

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay:
            d1 = ax-2*(ay/2)
            a1 = (ay/2*ay/2)/2 + d1*ay/2 + (ay/2*ay/2)/2
            a2 = 2*a1
            Ainf1 = [0, a1, a1]
            a_over_l1 = [0, (ay/2)/ax, (ay/2)/ax]
            Ainf2 = [(astair*astair/2)/2,  a2, a2]
            a_over_l2 = [0.50, (ay/2)/ax, (ay/2)/ax]
            Ainf3 = [2*(astair*astair/2)/2, a2, a2] * (nextarbaysY-1)
            a_over_l3 = [0.50, (ay/2)/ax, (ay/2)/ax] * (nextarbaysY-1)
            Ainf4 = [(astair*astair/2)/2, a1, a1]
            a_over_l4 = [0.50, (ay/2)/ax, (ay/2)/ax]
            self.beamX.Ainf3 = np.array(Ainf1 + Ainf2 + Ainf3 + Ainf4)
            self.beamX.a_over_l = np.array(a_over_l1 + a_over_l2 + a_over_l3 + a_over_l4)
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            # ...........................................................................
            d1 = ay-2*(astair/2)
            a1 = (astair/2*astair/2)/2 + (d1*astair/2) + (astair/2*astair/2)/2 # TODO: Check this one, is this correct?
            a2 = 2*(ay/2*ay/2)/2
            a3 = a1 + a2
            Ainf1 = [0, a2, 2*a2, a2]
            a_over_l1 = [0, 0.5, 0.5, 0.5]
            Ainf2 = [a1, a3, 2*a2, a2] * nextarbaysY
            a_over_l2 = [(astair/2)/ay, 0.5, 0.5, 0.5] * nextarbaysY
            self.beamY.Ainf3 = np.array(Ainf1 + Ainf2)
            self.beamY.a_over_l = np.array(a_over_l1 + a_over_l2)
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay:
            a1 = 2*(ax/2*ax/2)/2
            a2 = 2*a1
            Ainf1 = [0, a1, a1]
            a_over_l1 = [0, 0.5, 0.5]
            Ainf2 = [2*(astair/2*astair/2)/2,  a2, a2]
            a_over_l2 = [0.50, 0.50, 0.50]
            Ainf3 = [4*(astair/2*astair/2)/2, a2, a2] * (nextarbaysY-1)
            a_over_l3 = [0.50, 0.50, 0.50] * (nextarbaysY-1)
            Ainf4 = [(astair*astair/2)/2, a1, a1]
            a_over_l4 = [0.50, 0.50, 0.50]
            self.beamX.Ainf3 = np.array(Ainf1 + Ainf2 + Ainf3 + Ainf4)
            self.beamX.a_over_l = np.array(a_over_l1 + a_over_l2 + a_over_l3 + a_over_l4)
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            # ...........................................................................
            aux2 = (ay-ax/2)*ax/2
            aux3 = (ay-astair/2)*astair/2
            Ainf1 = [0, aux2, 2*aux2, aux2]
            a_over_l1 = [0, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay]
            Ainf2 = [aux3, aux2+aux3, 2*aux2, aux2] * nextarbaysY
            a_over_l2 = [(astair/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay] * nextarbaysY
            self.beamY.Ainf3 = np.array(Ainf1 + Ainf2)
            self.beamY.a_over_l = np.array(a_over_l1 + a_over_l2)
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)

        Astair3x1 = [ay/2*astair, 0, 0, ay/2*astair, 0, 0]
        Astair2x2 = [0, 0, 0] * nextarbaysY
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamX.Astair3 = np.array(Astair3x1 + Astair2x2)
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2*astair
        self.beamY.Astair3 = Astair3y.flatten()

        # Dimension of the spans of the beams
        self.beamX.L = np.array([astair, ax, ax] * (nextarbaysY+2))
        self.beamStair.L = astair
        lyy = ay * np.ones((4, nextarbaysY+1))
        self.beamY.L = lyy.flatten()

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([0, 1, 1] + [0, 0, 0] * nextarbaysY + [1, 1, 1])
        self.beamStair.pwallsA = 0.5
        self.beamY.pwallsA = np.array([1, 1, 0, 0] + [1, 0, 0, 1] * nextarbaysY)

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 3, 0, 0, 4, 3, 0, 0, 4, 3, 0, 0, 4, 3, 0, 0, 4, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 18, 19, 20]
        self.general.floor_truss_nodej_ref = [7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 22, 23, 24, 21, 22, 23]
        self.general.roof_truss_nodei_ref = [2, 3, 5, 6, 7, 9, 10, 11, 2, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 14, 15, 16, 17, 18, 19, 18, 19, 20]
        self.general.roof_truss_nodej_ref = [7, 8, 10, 11, 12, 14, 15, 16, 5, 7, 9, 10, 11, 13, 14, 15, 18, 19, 20, 17, 18, 19, 22, 23, 24, 21, 22, 23]
        self.general.truss_stiffness = 10.e12 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 24 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]


    def _b10(self):
        """
        Building B10 - nodes, columns and beams are counted from left to right
        hand side along X first, then moved up to next Y level of the plan view:
        Y
        |
        |---->X
        """
        # Copy these for easier coding
        ax = self.general.ax
        ay = self.general.ay
        astair = self.general.astair

        # 1) Reference files for B10 - Needs to be changed for different buildings
        nextarbaysX = 2
        nextarbaysY = 5
        self.general.number_of_alignmentsX = nextarbaysX + 2
        self.general.number_of_alignmentsY = nextarbaysY + 1
        self.general.Reference = np.arange(1, 4 * (nextarbaysY + 2) + 1)
        
        # 2) Plan configuration
        planX = [0, astair, astair+ax, astair+ax+ax]
        planY = [ay * i for i in range(nextarbaysY + 2)]
        self.general.Plan = None
        for j in range(nextarbaysY + 2):
            for i in range(4):
                if self.general.Plan is not None:
                    self.general.Plan = np.append(self.general.Plan, np.array([[planX[i], planY[j]]]), axis = 0)
                else:
                    self.general.Plan = np.array([[planX[i], planY[j]]])
        
        # 3) Column names including the two-sub-columns of the staircase
        colname1 = np.array([101, 20101, 102, 20102, 103, 104], dtype='int')
        colname2 = np.arange(105, 104 + 4 * (nextarbaysY + 1) + 1)
        colnamesref = np.append(colname1, colname2)
        self.column.nameref = np.zeros((8,len(colnamesref)), dtype='int')
        for i in range(8):
            self.column.nameref[i, :] = colnamesref + 100 * i

        # 4) Initial(BOT) mid-point nodes "Elastic model" for each column defined in 3)
        elasCnodeiref1 = np.array([1, 20101, 2, 20102, 3, 4], dtype='int')
        elasCnodeiref2 = np.arange(5, 4 * (nextarbaysY + 2) + 1)
        elasCnodeiref = np.append(elasCnodeiref1, elasCnodeiref2)
        self.column.elasCnodeiref = np.zeros((8,len(elasCnodeiref)), dtype='int')
        for i in range(8):
            self.column.elasCnodeiref[i, :] = elasCnodeiref + 100 * i

        # 5) Final(TOP) mid-point nodes "Elastic model" for each column defined in 4)
        elasCnodejref1 = np.array([20101, 101, 20102, 102, 103, 104], dtype='int')
        elasCnodejref2 = np.arange(105, 104 + 4 * (nextarbaysY + 1) + 1)
        elasCnodejref = np.append(elasCnodejref1, elasCnodejref2)
        self.column.elasCnodejref = np.zeros((8,len(elasCnodejref)), dtype='int')
        for i in range(8):
            self.column.elasCnodejref[i, :] = elasCnodejref + 100 * i

        # 6) Loading influence area for each column following the first line (one storey) of 4), 5) and 6) 
        Ainfref0 = np.array([0, 0, (ax/2)*(ay/2), (ax/2)*(ay/2), ax*(ay/2), (ax/2)*(ay/2)])
        Ainfref1 = np.array([(astair/2)*(ay/2), (ax/2)*ay+(astair/2)*(ay/2), ax*(ay), (ax/2)*(ay)])
        Ainfint = np.array([ay*astair/2, (astair/2+ax/2)*ay, ay*ax, (ax/2)*(ay)] * (nextarbaysY-1))
        Ainfend = np.array([(astair/2)*(ay/2), (astair/2+ax/2)*(ay/2), (ay/2)*(ax), (ax/2)*(ay/2)])
        self.column.Ainfref = np.hstack((Ainfref0, Ainfref1, Ainfint, Ainfend))
        # ...........................................................................
        Astairref0 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), 0, 0])
        Astairref1 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), 0, 0])
        Astairint = np.array([0, 0, 0, 0] * (nextarbaysY-1))
        Astairend = np.array([0, 0, 0, 0])
        self.column.Astairref = np.hstack((Astairref0, Astairref1, Astairint, Astairend))
        # ...........................................................................
        Aroofref0 = np.array([(astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), (astair/2)*(ay/2), ax*(ay/2), (ax/2)*(ay/2)])
        Aroofref1 = np.array([(astair/2)*(ay/2), (ax/2)*ay+(astair/2)*(ay), ax*(ay), (ax/2)*(ay)])
        Aroofint = np.array([ay*astair/2, (astair/2+ax/2)*ay, ay*ax, (ax/2)*(ay)] * (nextarbaysY-1))
        Aroofend = np.array([(astair/2)*(ay/2), (astair/2+ax/2)*(ay/2), (ay/2)*(ax), (ax/2)*(ay/2)])
        self.column.Aroofref = np.hstack((Aroofref0, Aroofref1, Aroofint, Aroofend))
        # ...........................................................................
        ncols_bot_end11 = np.array([1.3, 1.3, 1.3, 1.3, 1.3, 1.3])
        ncols_bot_end12 = np.array([1.3, 1.3, 1.3, 1.3])
        ncols_bot_int1 = np.array([1.3, 1.1, 1.1, 1.3] * nextarbaysY)
        ncols_bot1 = np.hstack((ncols_bot_end11, ncols_bot_int1, ncols_bot_end12))
        # ...........................................................................
        ncols_bot_end21 = np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
        ncols_bot_end22 = np.array([1.5, 1.5, 1.5, 1.5])
        ncols_bot_int2 = np.array([1.5, 1.3, 1.3, 1.5] * nextarbaysY)
        ncols_bot2 = np.hstack((ncols_bot_end21, ncols_bot_int2, ncols_bot_end22)) 
        self.column.positionfactor_ref = np.vstack((ncols_bot1, ncols_bot2))
        # ...........................................................................
        if nextarbaysX == 2:
            if nextarbaysY == 2:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 15, 16, 17, 18], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 3:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 19, 20, 21, 22], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 4:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 21, 23, 24, 25, 26], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis
            elif nextarbaysY == 5:
                self.column.Colindex1 = np.array([1, 2, 3, 4, 5, 6, 8, 9, 13, 17, 21, 25, 27, 28, 29, 30], dtype='int')  # these columns have HY=Bfixed. max dimension oriented along global X axis
                self.column.Colindex2 = np.array([7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 22, 23, 24, 26], dtype='int')  # these columns have HX=Bfixed. max dimension oriented along global Y axis

        Lref1 = np.array([0.50, 0.50, 0.50, 0.50, 1, 1])
        Lref2 = np.array([1, 1, 1, 1] * (nextarbaysY+1))
        self.column.Lref = np.hstack((Lref1, Lref2))
        # ...........................................................................
        wall_legth1=np.array([astair/2+ay/2, astair/2+ay/2, astair/2+ay/2+ax/2, astair/2+ay/2+ax/2, ax, ax+ay/2])
        wall_legth2=np.array([ay/2, ay/2+ax/2, 0, ay])
        wall_legthend=np.array([astair/2, astair/2+ax/2, ax, ax])
        walls = np.array([ay, 0, 0, ay] * (nextarbaysY-1))
        self.column.walllength = np.hstack((wall_legth1, wall_legth2, walls, wall_legthend))
        # ...........................................................................
        self.general.stair_node_left_mirror_1st_storey = 1
        self.general.stair_node_right_mirror_1st_storey = 2
        self.general.stairXleft = 0
        self.general.stairXright = astair
        self.general.stairY = 0
        # ...........................................................................
        self.beamX.index = np.array([], dtype='int') # to define the different continuous beams
        for i in range(nextarbaysY+2):
            self.beamX.index = np.append(self.beamX.index, (i+2) * np.ones(3, dtype='int'))
        self.beamY.index = np.array([2, 3, 4, 5] * (nextarbaysY+1), dtype='int')  # to define the different continuous beams
        # ...........................................................................
        self.beamX.auxvX = np.arange(50101, 50100 + len(self.beamX.index) + 1, dtype='int')  # beamX names
        self.beamY.auxvY = np.arange(50151, 50150 + len(self.beamY.index) + 1, dtype='int')  # beamY names
        self.beamStair.auxvStair = 51101  # the beam refers to the stairs' inter-storey supporting beam...
        self.beamX.beamXnameref = np.array([self.beamX.auxvX, 100+self.beamX.auxvX, 200+self.beamX.auxvX,
                                            300+self.beamX.auxvX, 400+self.beamX.auxvX, 500+self.beamX.auxvX,
                                            600+self.beamX.auxvX, 700+self.beamX.auxvX], dtype='int')
        self.beamY.beamYnameref = np.array([self.beamY.auxvY, 100+self.beamY.auxvY, 200+self.beamY.auxvY,
                                            300+self.beamY.auxvY, 400+self.beamY.auxvY, 500+self.beamY.auxvY,
                                            600+self.beamY.auxvY, 700+self.beamY.auxvY], dtype='int')
        self.beamStair.beamStairnameref = np.array([[self.beamStair.auxvStair], [100+self.beamStair.auxvStair], [200+self.beamStair.auxvStair],
                                                    [300+self.beamStair.auxvStair], [400+self.beamStair.auxvStair], [500+self.beamStair.auxvStair],
                                                    [600+self.beamStair.auxvStair], [700+self.beamStair.auxvStair]], dtype='int')
        # ...........................................................................
        self.beamX.auxvX1 = np.array([], dtype='int') # beam initial nodes in XX
        for i in range(nextarbaysY+2):
            aux1 = 101 + 4 * i
            self.beamX.auxvX1 = np.append(self.beamX.auxvX1, np.array([aux1, aux1+1, aux1+2], dtype='int'))
        self.beamY.auxvY1 = np.arange(101, 104 + nextarbaysY*4 + 1, dtype='int')
        self.beamStair.auxvStair1 = 20101
        self.beamX.elasXnodeiref = np.array([self.beamX.auxvX1, 100+self.beamX.auxvX1, 200+self.beamX.auxvX1,
                                             300+self.beamX.auxvX1, 400+self.beamX.auxvX1, 500+self.beamX.auxvX1,
                                             600+self.beamX.auxvX1, 700+self.beamX.auxvX1], dtype='int')
        self.beamX.elasXnodejref = self.beamX.elasXnodeiref + 1
        self.beamY.elasYnodeiref = np.array([self.beamY.auxvY1, 100+self.beamY.auxvY1, 200+self.beamY.auxvY1,
                                             300+self.beamY.auxvY1, 400+self.beamY.auxvY1, 500+self.beamY.auxvY1,
                                             600+self.beamY.auxvY1, 700+self.beamY.auxvY1], dtype='int')
        self.beamY.elasYnodejref = self.beamY.elasYnodeiref + 4
        self.beamStair.elasStairnodeiref =  np.array([[self.beamStair.auxvStair1], [100+self.beamStair.auxvStair1], [200+self.beamStair.auxvStair1],
                                                      [300+self.beamStair.auxvStair1], [400+self.beamStair.auxvStair1], [500+self.beamStair.auxvStair1],
                                                      [600+self.beamStair.auxvStair1], [700+self.beamStair.auxvStair1]], dtype='int')
        self.beamStair.elasStairnodejref = self.beamStair.elasStairnodeiref + 1

        # Case slaborient = 1 - Unloading in X beams
        Ainf1X = [0, ax*ay/2, ax*ay/2]
        Ainf2X = [astair*ay/2, (ax*ay), (ax*ay)]
        Ainf3X = [(astair*ay), (ax*ay), (ax*ay)] * (nextarbaysY-1)
        Ainf4X = [(astair*astair/2)/2, (ax*ay/2), (ax*ay/2)]
        Astair3x1 = [ay/2*astair, 0, 0, ay/2*astair, 0, 0]
        Astair2x2 = [0, 0, 0] * nextarbaysY
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamX.Astair1 = np.array(Astair3x1 + Astair2x2)
        self.beamStair.Ainf1 = 0
        self.beamStair.Astair1 = ay/2 * astair
        self.beamX.Ainf1 = np.array(Ainf1X + Ainf2X + Ainf3X + Ainf4X)
        self.beamY.Astair1 = Astair3y.flatten()
        self.beamY.Ainf1 = Astair3y.flatten()
  
        # Case slaborient = 2 - Unloading in Y beams
        Astair3x = np.zeros((3, nextarbaysY+2))
        self.beamX.Astair2 = Astair3x.flatten()
        self.beamX.Ainf2 = Astair3x.flatten()
        self.beamStair.Ainf2 = 0
        self.beamStair.Astair2 = ay/2 * astair
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamY.Astair2 = Astair3y.flatten()
        ainf2y1 = [0, ay*ax/2, ay*ax, ay*ax/2]
        ainf2y2 = [astair/2*ay, ay*ax/2+ay*astair/2, ay*ax, ay*ax/2] * nextarbaysY
        self.beamY.Ainf2 = np.array(ainf2y1 + ainf2y2)
        self.beamY.Astair2 = self.beamY.Astair1.copy()

        # Case slab_orient = 3 - Unloading in both directions
        if ax >= ay:
            d1 = ax-2*(ay/2)
            a1 = (ay/2*ay/2)/2 + d1*ay/2 + (ay/2*ay/2)/2
            a2 = 2*a1
            Ainf1 = [0, a1, a1]
            a_over_l1 = [0, (ay/2)/ax, (ay/2)/ax]
            Ainf2 = [(astair*astair/2)/2,  a2, a2]
            a_over_l2 = [0.50, (ay/2)/ax, (ay/2)/ax]
            Ainf3 = [2*(astair*astair/2)/2, a2, a2] * (nextarbaysY-1)
            a_over_l3 = [0.50, (ay/2)/ax, (ay/2)/ax] * (nextarbaysY-1)
            Ainf4 = [(astair*astair/2)/2, a1, a1]
            a_over_l4 = [0.50, (ay/2)/ax, (ay/2)/ax]
            self.beamX.Ainf3 = np.array(Ainf1 + Ainf2 + Ainf3 + Ainf4)
            self.beamX.a_over_l = np.array(a_over_l1 + a_over_l2 + a_over_l3 + a_over_l4)
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            # ...........................................................................
            d1 = ay-2*(astair/2)
            a1 = (ay/2*astair/2)/2 + (d1*astair/2) + (ay/2*astair/2)/2
            a2 = 2*(ay/2*ay/2)/2
            a3 = a1 + a2
            Ainf1 = [0, a2, 2*a2, a2]
            a_over_l1 = [0, 0.5, 0.5, 0.5]
            Ainf2 = [a1, a3, 2*a2, a2] * nextarbaysY
            a_over_l2 = [(astair/2)/ay, 0.5, 0.5, 0.5] * nextarbaysY
            self.beamY.Ainf3 = np.array(Ainf1 + Ainf2)
            self.beamY.a_over_l = np.array(a_over_l1 + a_over_l2)
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)
        elif ax < ay:
            a1 = 2*(ax/2*ax/2)/2
            a2 = 2*a1
            Ainf1 = [0, a1, a1]
            a_over_l1 = [0, 0.5, 0.5]
            Ainf2 = [2*(astair/2*astair/2)/2,  a2, a2]
            a_over_l2 = [0.50, 0.50, 0.50]
            Ainf3 = [2*(astair*astair/2)/2, a2, a2] * (nextarbaysY-1)
            a_over_l3 = [0.50, 0.50, 0.50] * (nextarbaysY-1)
            Ainf4 = [(astair*astair/2)/2, a1, a1]
            a_over_l4 = [0.50, 0.50, 0.50]
            self.beamX.Ainf3 = np.array(Ainf1 + Ainf2 + Ainf3 + Ainf4)
            self.beamX.a_over_l = np.array(a_over_l1 + a_over_l2 + a_over_l3 + a_over_l4)
            self.beamX.alpha = _get_alpha_load(self.beamX.a_over_l)
            # ...........................................................................
            aux2 = (ay-ax/2)*ax/2
            aux3 = (ay-astair/2)*astair/2
            Ainf1 = [0, aux2, 2*aux2, aux2]
            a_over_l1 = [0, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay]
            Ainf2 = [aux3, aux2+aux3, 2*aux2, aux2] * nextarbaysY
            a_over_l2 = [(astair/2)/ay, (ax/2)/ay, (ax/2)/ay, (ax/2)/ay] * nextarbaysY
            self.beamY.Ainf3 = np.array(Ainf1 + Ainf2)
            self.beamY.a_over_l = np.array(a_over_l1 + a_over_l2)
            self.beamY.alpha = _get_alpha_load(self.beamY.a_over_l)

        Astair3x1 = [ay/2*astair, 0, 0, ay/2*astair, 0, 0]
        Astair2x2 = [0, 0, 0] * nextarbaysY
        Astair3y = np.zeros((4, nextarbaysY+1))
        self.beamX.Astair3 = np.array(Astair3x1 + Astair2x2)
        self.beamStair.Ainf3 = 0.0
        self.beamStair.Astair3 = ay/2*astair
        self.beamY.Astair3 = Astair3y.flatten()

        # Dimension of the spans of the beams
        self.beamX.L = np.array([astair, ax, ax] * (nextarbaysY+2))
        self.beamStair.L = astair
        lyy = ay * np.ones((4, nextarbaysY+1))
        self.beamY.L = lyy.flatten()

        # Exterior infiill walls on beams
        self.beamX.pwallsA = np.array([0, 1, 1] + [0, 0, 0] * nextarbaysY + [1, 1, 1])
        self.beamStair.pwallsA = 0.5
        self.beamY.pwallsA = np.array([1, 1, 0, 0] + [1, 0, 0, 1] * nextarbaysY)

        # This is related to location of columns (facades 1 to 4)
        # 6) Smail's stuff
        # 1 front facade including staircase pilasters (2 halves)
        # 2 rear facade
        # 3 Left facade
        # 4 right facade
        self.column.perimeter = np.array([1, 1, 1, 1, 1, 1, 3, 0, 0, 4, 3, 0, 0, 4, 3, 0, 0, 4, 3, 0, 0, 4, 3, 0, 0, 4, 2, 2, 2, 2])
        self.column.perimeter = repmat(self.column.perimeter, self.general.nstoreys, 1)
        aux_col_per = self.column.perimeter * 0
        self.column.storey = np.array([i+1 + aux_col_per[i] * 0 for i in range(len(aux_col_per))])

        # The values in these lists are used to define flexible diaphragms (added by VO)
        self.general.floor_truss_nodei_ref = [2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 18, 19, 20, 21, 22, 23, 22, 23, 24]
        self.general.floor_truss_nodej_ref = [7, 8, 10, 11, 12, 14, 15, 16, 18, 19, 20, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 22, 23, 24, 21, 22, 23, 26, 27, 28, 25, 26, 27]
        self.general.roof_truss_nodei_ref = [2, 3, 5, 6, 7, 9, 10, 11, 2, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 14, 15, 16, 17, 18, 19, 18, 19, 20, 21, 22, 23, 22, 23, 24]
        self.general.roof_truss_nodej_ref = [7, 8, 10, 11, 12, 14, 15, 16, 5, 7, 9, 10, 11, 13, 14, 15, 18, 19, 20, 17, 18, 19, 22, 23, 24, 21, 22, 23, 26, 27, 28, 25, 26, 27]
        self.general.truss_stiffness = 10.e12 # I do not know why, but it seems that stiffness values are different. TODO: why not single value?
        # The identifiers used to define rigid-diaphragms in nonlinear models (added by VO)
        self.general.nonlin_diaph_nodeid_max = 28 # the maximum of identifiers for diaphragm nodes used in nonlinear models [expr $x*100+1] [expr $x*100+2] ... [expr $x*100+nonlin_diaph_nodeid_max]
