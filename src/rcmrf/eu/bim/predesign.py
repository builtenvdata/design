from src.rcmrf.eu.bim.buildings import LayoutManager
import numpy as np
from numpy.matlib import repmat

class Predesigner(LayoutManager):

    def make_predesign(self):

        # Pre-design of column dimensions
        self._predesign_columns()
        # Beam loads for pre-design
        self._predesign_load_beams()
        # Pre-design of beams
        if self.general.slaborient == 0: # This one is incomplete (flat slabs)
            self._predesign_beams0()
        elif self.general.slaborient == 1:
            self._predesign_beams1()
        elif self.general.slaborient == 2:
            self._predesign_beams2()
        elif self.general.slaborient == 3:
            self._predesign_beams3()

        # Originally joints are defined here, but I think it is a mistake. --> I do this after final design
        # self._get_joint_geometry()
        
        # Calculates the generic properties of each element for elastic analysis depending on slaborient Elastic analysis variables for beams and columns
        self.beamX.update_mechanical_properties()
        self.beamStair.update_mechanical_properties()
        self.beamY.update_mechanical_properties()
        self.column.update_mechanical_properties()

    def _predesign_columns(self):
        """Pre-design of column dimensions
        """

        ## Expected axial load, and area needed to sustain axial loads
        self.column.Ned = self.column.storeyfactor * self.column.positionfactor * (self.general.ped * self.column.Ainf + self.general.pedstair * self.column.Astair + self.general.pedwall * self.column.walllength) + self.column.rooffactor * self.general.pedroof * self.column.Aroof * self.column.positionfactor
        ## Serviciability pre-verification, area needed to sustain axial loads
        self.column.N_CP = self.column.storeyfactor * self.column.positionfactor * (self.general.pCP * self.column.Ainf + self.general.pCPstair * self.column.Astair + self.general.pedwall * self.column.walllength) + self.column.rooffactor * self.general.pedroof * self.column.Aroof * self.column.positionfactor
        ## Load for nonlinear analysis
        self.column.N_EQfinal = self.column.storeyfactor * self.column.positionfactor * (self.general.pedEQfinal * self.column.Ainf + self.general.pedstairEQfinal * self.column.Astair + self.general.pedwall * self.column.walllength) + self.column.rooffactor * self.general.pedroofEQfinal * self.column.Aroof * self.column.positionfactor
        ## Area Column - Final Verifications
        # Initial guess for the column concrete area is N/fc at the moment. 
        # TODO: I would say lets introduce a factor here. 0.4? Usually we do not want 2nd order effects. Is this requirement forced for CDM and CDH?
        self.column.sigma = self.general.fcd.copy()
        if self.general.designlevel in ['CDN', 'CDL']:
            self.column.AreaULS = self.column.Ned / (1000 * self.general.fcd)
            self.column.AreaCP = 0 * self.column.N_CP
        else: # TODO: Could be modified for more optimum solutions in case of other classes
            self.column.AreaULS = self.column.Ned / (1000 * self.general.fcd)
            self.column.AreaCP = 0 * self.column.N_CP / (0.40 * 1000 * self.general.fcd)
        # Using np.maximum for element-wise comparison in arrays
        self.column.AreaNeeded = np.maximum(self.column.AreaULS, self.column.AreaCP)
        ## Determine initial dimensions
        if self.general.ColumnType == 1:
            self.column.HX = np.sqrt(self.column.AreaNeeded)
            self.column.HY = self.column.HX.copy()
        else:
            self.column.HY = np.zeros((self.general.nstoreys, len(self.column.Colindex1) + len(self.column.Colindex2)))
            self.column.HX = np.zeros((self.general.nstoreys, len(self.column.Colindex1) + len(self.column.Colindex2)))
            for i in range(self.general.nstoreys):
                if self.general.designlevel in ['CDN', 'CDL']:
                        self.column.HY[i, self.column.Colindex1] = self.general.Bcolfix + 0*self.column.AreaNeeded[i, self.column.Colindex1]
                        self.column.HX[i, self.column.Colindex1] = self.column.AreaNeeded[i, self.column.Colindex1] / self.column.HY[i, self.column.Colindex1]
                        self.column.HX[i, self.column.Colindex2] = self.general.Bcolfix + 0*self.column.AreaNeeded[i, self.column.Colindex2]
                        self.column.HY[i, self.column.Colindex2] = self.column.AreaNeeded[i, self.column.Colindex2] / self.column.HX[i, self.column.Colindex2]
                else: # we multiply by 2 to account for the load combinations here
                    self.column.HX[i, self.column.Colindex1] = np.sqrt(2*self.column.AreaNeeded[i, self.column.Colindex1])
                    self.column.HY[i, self.column.Colindex1] = 0.50*self.column.HX[i, self.column.Colindex1]
                    self.column.HY[i, self.column.Colindex2] = np.sqrt(2*self.column.AreaNeeded[i, self.column.Colindex2])
                    self.column.HX[i, self.column.Colindex2] = 0.50*self.column.HY[i, self.column.Colindex2]
        self.column.HX = np.maximum(np.ceil(20*self.column.HX)/20, 0.30)
        self.column.HY = np.maximum(np.ceil(20*self.column.HY)/20, 0.30)
        ## Calculate initial mechanical properties
        self.column.update_mechanical_properties()
        ## Identify pairing sections --> the columns with the stair beams
        aucx = np.where(self.column.Astairref[0, :] > 0)[0]
        aux2 = self.column.HX.shape
        equalsections = np.zeros(aux2, dtype='int')
        HX = self.column.HX.flatten()
        HY = self.column.HY.flatten()
        for i in range(aux2[0]):
            equalsections[i, aucx[:2]] = (i+1) * 10 + 1
            equalsections[i, aucx[2:4]]= (i+1) * 10 + 2
        equalsections = equalsections.T
        self.column.equalsections = equalsections.copy()
        # ...........................................................................
        aux11 = self.column.equalsections.T
        stair_column_idxs = np.where(aux11[0, :] != 0)[0]
        for i in range(self.general.nstoreys):
            for j in range(stair_column_idxs[0], stair_column_idxs[-1] + 1, 2): # fixed the mistake in the original version
                if aux11[i, j] == aux11[i, j+1] and aux11[i, j] > 0.1:
                    self.column.HX[i, j+1] = max(self.column.HX[i, j], self.column.HX[i, j+1])
                    self.column.HY[i, j+1] = max(self.column.HY[i, j], self.column.HY[i, j+1])
                    self.column.HX[i, j] = max(self.column.HX[i, j], self.column.HX[i, j+1]) # Added by VO to the original version
                    self.column.HY[i, j] = max(self.column.HY[i, j], self.column.HY[i, j+1]) # Added by VO to the original version
        # ...........................................................................
        # TODO: What do we do here?
        for i in range(self.column.HX.shape[1]):
            Hmax = 0
            for j in range(self.general.nstoreys-1, -1, -1):
                if j == self.general.nstoreys-1:
                    self.column.HX[j, i] = self.column.HX[j, i]
                else:
                    Hmax = max([Hmax, self.column.HX[j, i], self.column.HX[j+1, i]])
                    if self.column.HX[j, i] <= Hmax:
                        self.column.HX[j, i] = Hmax
                    elif self.column.HX[j, i] <= self.column.HX[j-1, i] - 0.10:
                        self.column.HX[j, i] = self.column.HX[j-1, i] - 0.10
                    else:
                        self.column.HX[j, i] = self.column.HX[j, i]
            self.column.HX[0, i] = max(Hmax, self.column.HX[0, i])
        # ...........................................................................
        for i in range(self.column.HY.shape[1]):
            Hmax = 0
            for j in range(self.general.nstoreys-1, -1, -1):
                if j == self.general.nstoreys-1:
                    self.column.HY[j, i] = self.column.HY[j, i]
                else:
                    Hmax = max([Hmax, self.column.HY[j, i], self.column.HY[j+1, i]])
                    if self.column.HY[j, i] <= Hmax:
                        self.column.HY[j, i] = Hmax
                    elif self.column.HY[j, i] <= self.column.HY[j-1, i] - 0.10:
                        self.column.HY[j, i] = self.column.HY[j-1, i] - 0.10
                    else:
                        self.column.HY[j, i] = self.column.HY[j, i]
            self.column.HY[0, i] = max(Hmax, self.column.HY[0, i])
        # ...........................................................................
        # Uniformizes the section geometry (HX and HY) every 2 storeys (Up to 9 storeys only)
        if self.general.designlevel == 'CDH':
            for j in range(self.column.HX.shape[1]):
                HXmax = max(self.column.HX[:, j])
                HYmax = max(self.column.HY[:, j])
                Hmaxmax = max(HXmax, HYmax)
                self.column.HX[:, j] = np.ones(self.column.HX.shape[0]) * Hmaxmax
                self.column.HY[:, j] = np.ones(self.column.HX.shape[0]) * Hmaxmax
        else:
            if self.general.nstoreys == 3:
                for j in range(self.column.HX.shape[1]):
                    HXmax = max(self.column.HX[:, j])
                    HYmax = max(self.column.HY[:, j])
                    self.column.HX[:, j] = np.ones(self.column.HX.shape[0]) * HXmax
                    self.column.HY[:, j] = np.ones(self.column.HX.shape[0]) * HYmax
            else:
                for i in range(1, self.general.nstoreys, 2):
                    if i == 1:
                        self.column.HX[i, :] = np.maximum(self.column.HX[i, :], self.column.HX[i-1, :])
                        self.column.HX[i-1, :] = self.column.HX[i, :]
                        self.column.HY[i, :] = np.maximum(self.column.HY[i, :], self.column.HY[i-1, :])
                        self.column.HY[i-1, :] = self.column.HY[i, :]
                    else:
                        self.column.HX[i, :] = np.maximum(self.column.HX[i, :], self.column.HX[i-1, :])
                        self.column.HX[i, :] = np.maximum(self.column.HX[i, :], self.column.HX[i-2, :] - 0.10)
                        self.column.HX[i-1, :] = self.column.HX[i, :]
                        self.column.HY[i, :] = np.maximum(self.column.HY[i, :], self.column.HY[i-1, :])
                        self.column.HY[i, :] = np.maximum(self.column.HY[i, :], self.column.HY[i-2, :] - 0.10)
                        self.column.HY[i-1, :] = self.column.HY[i, :]                    
                if self.general.nstoreys % 2 == 1:
                    i = self.general.nstoreys - 1
                    self.column.HX[i, :] = np.maximum(self.column.HX[i, :], self.column.HX[i-1, :] - 0.10)
                    self.column.HY[i, :] = np.maximum(self.column.HY[i, :], self.column.HY[i-1, :] - 0.10)

    def _predesign_load_beams(self):
        """Defines beam loads for pre-design (all load combinations)
        """

        # Calculate beam loads - equivalent rectangular loads to maximize moments
        aux1 = self.general.pedwall * self.beamX.pwallsA
        self.beamX.pwalls = repmat(aux1, self.general.nstoreys, 1)
        aux2 = self.general.pedwall * self.beamStair.pwallsA
        self.beamStair.pwalls = repmat(aux2, self.general.nstoreys, 1)
        aux3 = self.general.pedwall * self.beamY.pwallsA
        self.beamY.pwalls=repmat(aux3, self.general.nstoreys, 1)
        # ...................................................................................................................................................
        aux1 = self.general.pedwallEQ * self.beamX.pwallsA
        self.beamX.pwallsEQ = repmat(aux1, self.general.nstoreys, 1)
        aux2 = self.general.pedwallEQ * self.beamStair.pwallsA
        self.beamStair.pwallsEQ = repmat(aux2, self.general.nstoreys, 1)
        aux3 = self.general.pedwallEQ * self.beamY.pwallsA
        self.beamY.pwallsEQ = repmat(aux3, self.general.nstoreys, 1)
        # ...................................................................................................................................................
        aux1 = self.general.pedwallEQfinal * self.beamX.pwallsA
        self.beamX.pwallsEQFinal = repmat(aux1, self.general.nstoreys, 1)
        aux2 = self.general.pedwallEQfinal * self.beamStair.pwallsA
        self.beamStair.pwallsEQFinal = repmat(aux2, self.general.nstoreys, 1)
        aux3 = self.general.pedwallEQfinal * self.beamY.pwallsA
        self.beamY.pwallsEQFinal = repmat(aux3, self.general.nstoreys, 1)
        # ...................................................................................................................................................
        self.beamX.ped3 = self.beamX.Ainf3 * self.general.ped / self.beamX.L + self.beamX.Astair3 * self.general.pedstair / self.beamX.L + self.beamX.pwalls + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in YY
        self.beamX.ped2 = self.beamX.Ainf2 * self.general.ped / self.beamX.L + self.beamX.Astair2 * self.general.pedstair / self.beamX.L + self.beamX.pwalls + self.general.Bbeamfix_X * self.general.Hslab * self.general.pconcrete                     
        self.beamX.ped1 = self.beamX.Ainf1 * self.general.ped / self.beamX.L + self.beamX.Astair1 * self.general.pedstair / self.beamX.L + self.beamX.pwalls + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        self.beamX.ped0 = 0.00
        # ...................................................................................................................................................
        self.beamX.ped3EQ = self.beamX.Ainf3 * self.general.pedEQ / self.beamX.L + self.beamX.Astair3 * self.general.pedstairEQ / self.beamX.L + self.beamX.pwallsEQ + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in YY
        self.beamX.ped2EQ = self.beamX.Ainf2 * self.general.pedEQ / self.beamX.L + self.beamX.Astair2 * self.general.pedstairEQ / self.beamX.L + self.beamX.pwallsEQ + self.general.Bbeamfix_X * self.general.Hslab * self.general.pconcrete                     
        self.beamX.ped1EQ = self.beamX.Ainf1 * self.general.pedEQ / self.beamX.L + self.beamX.Astair1 * self.general.pedstairEQ / self.beamX.L + self.beamX.pwallsEQ + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        self.beamX.ped0EQ = 0.00
        # ...................................................................................................................................................
        self.beamX.ped3EQFinal = self.beamX.Ainf3 * self.general.pedEQfinal / self.beamX.L + self.beamX.Astair3 * self.general.pedstairEQfinal / self.beamX.L + self.beamX.pwallsEQFinal + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in YY
        self.beamX.ped2EQFinal = self.beamX.Ainf2 * self.general.pedEQfinal / self.beamX.L + self.beamX.Astair2 * self.general.pedstairEQfinal / self.beamX.L + self.beamX.pwallsEQFinal + self.general.Bbeamfix_X * self.general.Hslab * self.general.pconcrete                       
        self.beamX.ped1EQFinal = self.beamX.Ainf1 * self.general.pedEQfinal / self.beamX.L + self.beamX.Astair1 * self.general.pedstairEQfinal / self.beamX.L + self.beamX.pwallsEQFinal + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        self.beamX.ped0EQFinal = 0.00
        # ...................................................................................................................................................
        self.beamStair.ped3 = self.beamStair.Astair3 * self.general.pedstair / self.beamStair.L + self.beamStair.pwalls + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped2 = self.beamStair.Astair2 * self.general.pedstair / self.beamStair.L + self.beamStair.pwalls + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped1 = self.beamStair.Astair1 * self.general.pedstair / self.beamStair.L + self.beamStair.pwalls + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped0 = 0.00
        # ...................................................................................................................................................
        self.beamStair.ped3EQ = self.beamStair.Astair3 * self.general.pedstairEQ / self.beamStair.L + self.beamStair.pwallsEQ + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped2EQ = self.beamStair.Astair2 * self.general.pedstairEQ / self.beamStair.L + self.beamStair.pwallsEQ + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped1EQ = self.beamStair.Astair1 * self.general.pedstairEQ / self.beamStair.L + self.beamStair.pwallsEQ + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped0EQ = 0.00  
        # ...................................................................................................................................................
        self.beamStair.ped3EQFinal = self.beamStair.Astair3 * self.general.pedstairEQfinal / self.beamStair.L + self.beamStair.pwallsEQFinal + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped2EQFinal = self.beamStair.Astair2 * self.general.pedstairEQfinal / self.beamStair.L + self.beamStair.pwallsEQFinal + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped1EQFinal = self.beamStair.Astair1 * self.general.pedstairEQfinal / self.beamStair.L + self.beamStair.pwallsEQFinal + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.ped0EQFinal = 0.00
        # ...................................................................................................................................................
        self.beamY.ped3 = self.beamY.Ainf3 * self.general.ped / self.beamY.L + self.beamY.Astair3 * self.general.pedstair / self.beamY.L + self.beamY.pwalls + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete 
        self.beamY.ped2 = self.beamY.Ainf2 * self.general.ped / self.beamY.L + self.beamY.Astair2 * self.general.pedstair / self.beamY.L + self.beamY.pwalls + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete 
        # general.Hslab because slab unloads in XX
        self.beamY.ped1 = self.beamY.Ainf1 * self.general.ped / self.beamY.L + self.beamY.Astair1 * self.general.pedstair / self.beamY.L + self.beamY.pwalls + self.general.Bbeamfix_Y * self.general.Hslab * self.general.pconcrete 
        self.beamY.ped0 = 0.00 
        # ...................................................................................................................................................
        self.beamY.ped3EQ = self.beamY.Ainf3 * self.general.pedEQ / self.beamY.L + self.beamY.Astair3 * self.general.pedstairEQ / self.beamY.L + self.beamY.pwallsEQ + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        self.beamY.ped2EQ = self.beamY.Ainf2 * self.general.pedEQ / self.beamY.L + self.beamY.Astair2 * self.general.pedstairEQ / self.beamY.L + self.beamY.pwallsEQ + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in XX
        self.beamY.ped1EQ = self.beamY.Ainf1 * self.general.pedEQ / self.beamY.L + self.beamY.Astair1 * self.general.pedstairEQ / self.beamY.L + self.beamY.pwallsEQ + self.general.Bbeamfix_Y * self.general.Hslab * self.general.pconcrete                     
        self.beamY.ped0EQ = 0.00
        # ...................................................................................................................................................
        self.beamY.ped3EQFinal = self.beamY.Ainf3 * self.general.pedEQfinal / self.beamY.L + self.beamY.Astair3 * self.general.pedstairEQfinal / self.beamY.L + self.beamY.pwallsEQFinal + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        self.beamY.ped2EQFinal = self.beamY.Ainf2 * self.general.pedEQfinal / self.beamY.L + self.beamY.Astair2 * self.general.pedstairEQfinal / self.beamY.L + self.beamY.pwallsEQFinal + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in XX
        self.beamY.ped1EQFinal = self.beamY.Ainf1 * self.general.pedEQfinal / self.beamY.L + self.beamY.Astair1 * self.general.pedstairEQfinal / self.beamY.L + self.beamY.pwallsEQFinal + self.general.Bbeamfix_Y * self.general.Hslab * self.general.pconcrete  
        self.beamY.ped0EQFinal = 0.00
        # ...................................................................................................................................................
        self.beamX.proof3 = self.beamX.Ainf3 * self.general.pedroof / self.beamX.L + self.beamX.Astair3 * self.general.pedstair / self.beamX.L + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in YY
        self.beamX.proof2 = self.beamX.Ainf2 * self.general.pedroof / self.beamX.L + self.beamX.Astair2 * self.general.pedstair / self.beamX.L + self.general.Bbeamfix_X * self.general.Hslab * self.general.pconcrete
        self.beamX.proof1 = self.beamX.Ainf1 * self.general.pedroof / self.beamX.L + self.beamX.Astair1 * self.general.pedstair / self.beamX.L + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        self.beamX.proof0 = 0.00
        # ...................................................................................................................................................
        self.beamX.proof3EQ = self.beamX.Ainf3 * self.general.pedroofEQ / self.beamX.L + self.beamX.Astair3 * self.general.pedstairEQ / self.beamX.L + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in YY
        self.beamX.proof2EQ = self.beamX.Ainf2 * self.general.pedroofEQ / self.beamX.L + self.beamX.Astair2 * self.general.pedstairEQ / self.beamX.L + self.general.Bbeamfix_X * self.general.Hslab * self.general.pconcrete
        self.beamX.proof1EQ = self.beamX.Ainf1 * self.general.pedroofEQ / self.beamX.L + self.beamX.Astair1 * self.general.pedstairEQ / self.beamX.L + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        self.beamX.proof0EQ = 0.00    
        # ...................................................................................................................................................
        self.beamX.proof3EQFinal = self.beamX.Ainf3 * self.general.pedroofEQfinal / self.beamX.L + self.beamX.Astair3 * self.general.pedstairEQfinal / self.beamX.L + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in YY
        self.beamX.proof2EQFinal = self.beamX.Ainf2 * self.general.pedroofEQfinal / self.beamX.L + self.beamX.Astair2 * self.general.pedstairEQfinal / self.beamX.L + self.general.Bbeamfix_X * self.general.Hslab * self.general.pconcrete
        self.beamX.proof1EQFinal = self.beamX.Ainf1 * self.general.pedroofEQfinal / self.beamX.L + self.beamX.Astair1 * self.general.pedstairEQfinal / self.beamX.L + self.general.Bbeamfix_X * (self.beamX.L / 10) * self.general.pconcrete
        self.beamX.proof0EQFinal = 0.00
        # ...................................................................................................................................................
        self.beamStair.proof3 = self.beamStair.Astair3 * self.general.pedstair / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof2 = self.beamStair.Astair2 * self.general.pedstair / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof1 = self.beamStair.Astair1 * self.general.pedstair / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof0 = 0.00
        # ...................................................................................................................................................
        self.beamStair.proof3EQ = self.beamStair.Astair3 * self.general.pedstairEQ / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof2EQ = self.beamStair.Astair2 * self.general.pedstairEQ / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof1EQ = self.beamStair.Astair1 * self.general.pedstairEQ / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof0EQ = 0.00       
        # ...................................................................................................................................................
        self.beamStair.proof3EQFinal = self.beamStair.Astair3 * self.general.pedstairEQfinal / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof2EQFinal = self.beamStair.Astair2 * self.general.pedstairEQfinal / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof1EQFinal = self.beamStair.Astair1 * self.general.pedstairEQfinal / self.beamStair.L + self.general.Bbeamfix_X * (self.beamStair.L / 10) * self.general.pconcrete
        self.beamStair.proof0EQFinal = 0.00
        # ...................................................................................................................................................
        self.beamY.proof3 = self.beamY.Ainf3 * self.general.pedroof / self.beamY.L + self.beamY.Astair3 * self.general.pedstair / self.beamY.L + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        self.beamY.proof2 = self.beamY.Ainf2 * self.general.pedroof / self.beamY.L + self.beamY.Astair2 * self.general.pedstair / self.beamY.L + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in XX
        self.beamY.proof1 = self.beamY.Ainf1 * self.general.pedroof / self.beamY.L + self.beamY.Astair1 * self.general.pedstair / self.beamY.L + self.general.Bbeamfix_Y * self.general.Hslab * self.general.pconcrete
        self.beamY.proof0 = 0.00
        # ...................................................................................................................................................
        self.beamY.proof3EQ = self.beamY.Ainf3 * self.general.pedroofEQ / self.beamY.L + self.beamY.Astair3 * self.general.pedstairEQ / self.beamY.L + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        self.beamY.proof2EQ = self.beamY.Ainf2 * self.general.pedroofEQ / self.beamY.L + self.beamY.Astair2 * self.general.pedstairEQ / self.beamY.L + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in XX
        self.beamY.proof1EQ = self.beamY.Ainf1 * self.general.pedroofEQ / self.beamY.L + self.beamY.Astair1 * self.general.pedstairEQ / self.beamY.L + self.general.Bbeamfix_Y * self.general.Hslab * self.general.pconcrete
        self.beamY.proof0EQ = 0.00
        # ...................................................................................................................................................
        self.beamY.proof3EQFinal = self.beamY.Ainf3 * self.general.pedroofEQfinal / self.beamY.L + self.beamY.Astair3 * self.general.pedstairEQfinal / self.beamY.L + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        self.beamY.proof2EQFinal = self.beamY.Ainf2 * self.general.pedroofEQfinal / self.beamY.L + self.beamY.Astair2 * self.general.pedstairEQfinal / self.beamY.L + self.general.Bbeamfix_Y * (self.beamY.L / 10) * self.general.pconcrete
        # general.Hslab because slab unloads in XX
        self.beamY.proof1EQFinal = self.beamY.Ainf1 * self.general.pedroofEQfinal / self.beamY.L + self.beamY.Astair1 * self.general.pedstairEQfinal / self.beamY.L + self.general.Bbeamfix_Y * self.general.Hslab * self.general.pconcrete
        self.beamY.proof0EQFinal = 0.00

    # Pre-design of beams
    def _predesign_beams0(self):
        """Pre-design of beams for the case of slaborient = 0 (flat slabs) |-> This is incomplete!
        """
        pass

    def _predesign_beams1(self):
        """Pre-design of beams for the case of slaborient = 1 |-> Unloading on XX beams
        """
        reference_miu = 0.25
        reference_miu_wide = 0.25
        # 1) calculate the moment
        self.beamX.Med1 = self.beamX.ped1 * (self.beamX.L ** 2) / 12
        ix = self.beamX.Med1.shape[0] - 1
        self.beamX.Med1[ix, :] = self.beamX.proof1[ix, :] * (self.beamX.L[ix, :] ** 2) / 12
        self.beamStair.Med1 = self.beamStair.ped1 * (self.beamStair.L ** 2) / 12
        self.beamY.Med1 = self.beamY.ped1 * (self.beamY.L ** 2) / 12
        iy = self.beamY.Med1.shape[0] - 1
        self.beamY.Med1[iy, :] = self.beamY.proof1[iy ,:] * (self.beamY.L[iy, :] ** 2) / 12
        # ...................................................................................................................................................
        # TODO: Make sure that Ved1 and Med1 has the same size
        self.beamX.Ved1 = self.beamX.ped1 * (self.beamX.L) / 2
        self.beamX.Ved1[ix, :] = self.beamX.proof1[ix, :] * (self.beamX.L[ix, :]) / 2
        self.beamStair.Ved1 = self.beamStair.ped1 * (self.beamStair.L) / 2
        self.beamY.Ved1 = self.beamY.ped1 * (self.beamY.L) / 2
        self.beamY.Ved1[iy, :] = self.beamY.proof1[iy, :] * (self.beamY.L[iy, :]) / 2
        # ...................................................................................................................................................
        self.beamX.B1      = self.general.Bbeamfix_X * np.ones(self.beamX.Med1.shape)
        self.beamY.B1      = self.general.Bbeamfix_Y * np.ones(self.beamY.Med1.shape)
        self.beamStair.B1  = self.general.Bbeamfix_X * np.ones(self.beamStair.Med1.shape)
        # ...................................................................................................................................................
        self.beamX.H1      = np.maximum(self.general.Bbeamfix_X, (1 / 0.90) * np.sqrt(self.beamX.Med1 / (reference_miu * self.general.Bbeamfix_X * 1000 * self.general.fcd)))
        self.beamY.H1      = np.maximum(self.general.Bbeamfix_Y, (1 / 0.90) * np.sqrt(self.beamY.Med1 / (reference_miu * self.general.Bbeamfix_Y * 1000 * self.general.fcd)))
        self.beamStair.H1  = np.maximum(self.general.Bbeamfix_X, (1 / 0.90) * np.sqrt(self.beamStair.Med1 / (reference_miu * self.general.Bbeamfix_X * 1000 * self.general.fcd)))
        # ...................................................................................................................................................
        # beam deformation control
        if self.general.designlevel in ['CDN', 'CDL']:
            self.beamX.H1      = np.maximum(self.beamX.H1, self.beamX.L / (0.9 * 18))               
            self.beamY.H1      = np.maximum(self.beamY.H1, self.beamY.L / (0.9 * 18))
            self.beamStair.H1  = np.maximum(self.beamStair.H1, self.beamStair.L / (0.9 * 18))
        else:
            self.beamX.H1      = np.maximum(self.beamX.H1, self.beamX.L / 12)
            self.beamY.H1      = np.maximum(self.beamY.H1, self.beamY.L / (0.9 * 18))
            self.beamStair.H1  = np.maximum(self.beamStair.H1, self.beamStair.L / 12)
        # ...................................................................................................................................................
        self.beamX.H1      = np.maximum(self.beamX.H1, self.general.Hslab)
        self.beamStair.H1  = np.maximum(self.beamStair.H1, self.general.Hslab)
        self.beamY.H1      = np.maximum(self.beamY.H1, self.general.Hslab)
        # ...................................................................................................................................................
        self.beamX.H1      = np.ceil(20 * self.beamX.H1) / 20
        self.beamStair.H1  = np.ceil(20 * self.beamStair.H1) / 20
        self.beamY.H1      = np.ceil(20 * self.beamY.H1) / 20
        # ...................................................................................................................................................
        # beamtype = 1 |-> Wide beams EB in X; Tranverse beams in YY
        self.beamX.B = np.zeros((self.general.nstoreys, self.beamX.L.shape[1]))
        self.beamX.H = np.zeros((self.general.nstoreys, self.beamX.L.shape[1]))
        self.beamY.B = np.zeros((self.general.nstoreys, self.beamY.L.shape[1]))
        self.beamY.H = np.zeros((self.general.nstoreys, self.beamY.L.shape[1])) 
        if  self.general.BeamType == 1:
            self.beamX.WB_bc = np.zeros((self.general.nstoreys, self.beamX.L.shape[1]))
            self.beamX.B_A = np.zeros((self.general.nstoreys, self.beamX.L.shape[1]))                       
            self.beamX.B_B = np.zeros((self.general.nstoreys, self.beamX.L.shape[1]))                       
            for i in range(self.general.nstoreys):
                for j in range(self.beamX.L.shape[1]):
                    if self.beamX.index[j] == np.min(self.beamX.index) or self.beamX.index[j] == np.max(self.beamX.index):
                        self.beamX.B[i, j] = self.beamX.B1[i, j]
                        self.beamX.H[i, j] = self.beamX.H1[i, j]  
                    else:
                        nodei = self.beamX.elasnodei[i, j]
                        nodej = self.beamX.elasnodej[i, j]
                        bci = self.column.HY[np.where(self.column.nameref == nodei)]
                        bcj = self.column.HY[np.where(self.column.nameref == nodej)]
                        self.beamX.WB_bc[i, j] = np.maximum(bci, bcj)
                        self.beamX.H[i, j] = np.maximum(self.general.Hslab, 0.30)
                        self.beamX.B_A[i, j] = self.beamX.WB_bc[i, j] + 1.50 * self.general.Hslab
                        self.beamX.B_B[i, j] = self.beamX.Med1[i, j] / (reference_miu_wide * (self.beamX.H[i, j] ** 2) * 1000 * self.general.fcd)
                        self.beamX.B[i, j] = np.maximum(self.beamX.B_A[i, j], self.beamX.B_B[i, j])
                        self.beamX.B[i, j] = np.ceil(20 * self.beamX.B[i, j]) / 20
            # ...................................................................................................................................................
            # the stair beams have to be EB to support the weight
            for i in range(self.general.nstoreys):
                for j in range(self.beamX.L.shape[1]):
                    if self.beamX.Astair1[i, j] > 0:
                        self.beamX.B[i, j] = self.beamX.B1[i, j]
                        self.beamX.H[i, j] = self.beamX.H1[i, j]
                    else:
                        pass
            # ...................................................................................................................................................
            for i in range(self.general.nstoreys):
                for j in range(self.beamY.L.shape[1]):
                    if self.beamY.index[j] == np.min(self.beamY.index) or self.beamY.index[j] == np.max(self.beamY.index):
                        self.beamY.B[i, j] = self.beamY.B1[i, j]
                        self.beamY.H[i, j] = self.beamY.H1[i, j]
                    else:
                        self.beamY.B[i, j] = self.general.Bbeamfix_Y
                        self.beamY.H[i, j] = self.general.Hslab
            # ...................................................................................................................................................
            self.beamStair.H = self.beamStair.H1.copy()
            self.beamStair.B = self.beamStair.B1.copy()
        else:
            # ...................................................................................................................................................
            # beamtype = 2 |-> Emergent beams EB
            if self.general.BeamType == 2:
                self.beamX.H = self.beamX.H1.copy()
                self.beamX.B = self.beamX.B1.copy()
                self.beamY.H = self.beamY.H1.copy()
                self.beamY.B = self.beamY.B1.copy()
                self.beamStair.H = self.beamStair.H1.copy()
                self.beamStair.B = self.beamStair.B1.copy()
        # Adjusts the height of continuous beams according to beam index
        auxaa = np.unique(self.beamX.index)
        for j in range(len(auxaa)):
            indaux = self.beamX.index == auxaa[j]
            for i in range(self.general.nstoreys):
                self.beamX.H[i, indaux] = np.max(self.beamX.H[i, indaux])
                self.beamX.B[i, indaux] = np.max(self.beamX.B[i, indaux])
        # ...................................................................................................................................................
        auxaa = np.unique(self.beamY.index)
        for j in range(len(auxaa)):
            indaux = self.beamY.index == auxaa[j]
            for i in range(self.general.nstoreys):
                self.beamY.H[i, indaux] = np.max(self.beamY.H[i, indaux])
                self.beamY.B[i, indaux] = np.max(self.beamY.B[i, indaux])
        # Defines the final loads
        self.beamX.ped = self.beamX.ped1.copy()
        self.beamY.ped = self.beamY.ped1.copy()
        self.beamStair.ped = self.beamStair.ped1.copy()
        self.beamX.pedEQ = self.beamX.ped1EQ.copy()
        self.beamY.pedEQ = self.beamY.ped1EQ.copy()
        self.beamStair.pedEQ = self.beamStair.ped1EQ.copy()
        # ...................................................................................................................................................
        self.beamX.pedroof = self.beamX.proof1.copy()
        self.beamY.pedroof = self.beamY.proof1.copy()
        self.beamStair.pedroof = self.beamStair.proof1.copy()
        self.beamX.pedroofEQ = self.beamX.proof1EQ.copy()
        self.beamY.pedroofEQ = self.beamY.proof1EQ.copy()
        self.beamStair.pedroofEQ = self.beamStair.proof1EQ.copy()
        # ...................................................................................................................................................
        self.beamX.pedEQFinal = self.beamX.ped1EQFinal.copy()
        self.beamY.pedEQFinal = self.beamY.ped1EQFinal.copy()
        self.beamStair.pedEQFinal = self.beamStair.ped1EQFinal.copy()
        self.beamX.proofEQFinal = self.beamX.proof1EQFinal.copy()
        self.beamY.proofEQFinal = self.beamY.proof1EQFinal.copy()
        self.beamStair.proofEQFinal = self.beamStair.proof1EQFinal.copy()
        # ...................................................................................................................................................
        self.beamX.H      = np.ceil(20 * self.beamX.H) / 20
        self.beamStair.H  = np.ceil(20 * self.beamStair.H) / 20
        self.beamY.H      = np.ceil(20 * self.beamY.H) / 20
        self.beamX.B      = np.ceil(20 * self.beamX.B) / 20
        self.beamStair.B  = np.ceil(20 * self.beamStair.B) / 20
        self.beamY.B      = np.ceil(20 * self.beamY.B) / 20

    def _predesign_beams2(self):
        """Pre-design of beams for the case of slaborient = 2 |-> Unloading on YY beams
        """
        reference_miu = 0.25
        reference_miu_wide = 0.25
        # 1) calculate the moment
        self.beamX.Med2 = self.beamX.ped2 * (self.beamX.L ** 2) / 12
        ix = self.beamX.Med2.shape[0] - 1
        self.beamX.Med2[ix, :] = self.beamX.proof2[ix, :] * (self.beamX.L[ix, :] ** 2) / 12
        self.beamStair.Med2 = self.beamStair.ped2 * (self.beamStair.L ** 2) / 12
        self.beamY.Med2 = self.beamY.ped2 * (self.beamY.L ** 2) / 12
        iy = self.beamY.Med2.shape[0] - 1
        self.beamY.Med2[iy, :] = self.beamY.proof2[iy ,:] * (self.beamY.L[iy, :] ** 2) / 12
        # ...................................................................................................................................................
        # TODO: Make sure that Ved2 and Med2 has the same size
        self.beamX.Ved2 = self.beamX.ped2 * (self.beamX.L) / 2
        self.beamX.Ved2[ix, :] = self.beamX.proof2[ix, :] * (self.beamX.L[ix, :]) / 2
        self.beamStair.Ved2 = self.beamStair.ped2 * (self.beamStair.L) / 2
        self.beamY.Ved2 = self.beamY.ped2 * (self.beamY.L) / 2
        self.beamY.Ved2[iy, :] = self.beamY.proof2[iy, :] * (self.beamY.L[iy, :]) / 2
        # ...................................................................................................................................................
        self.beamX.B2      = self.general.Bbeamfix_X * np.ones(self.beamX.Med2.shape)
        self.beamY.B2      = self.general.Bbeamfix_Y * np.ones(self.beamY.Med2.shape)
        self.beamStair.B2  = self.general.Bbeamfix_X * np.ones(self.beamStair.Med2.shape)
        # ...................................................................................................................................................
        self.beamX.H2      = np.maximum(self.general.Bbeamfix_X, (1 / 0.90) * np.sqrt(self.beamX.Med2 / (reference_miu * self.general.Bbeamfix_X * 1000 * self.general.fcd)))
        self.beamY.H2      = np.maximum(self.general.Bbeamfix_Y, (1 / 0.90) * np.sqrt(self.beamY.Med2 / (reference_miu * self.general.Bbeamfix_Y * 1000 * self.general.fcd)))
        self.beamStair.H2  = np.maximum(self.general.Bbeamfix_X, (1 / 0.90) * np.sqrt(self.beamStair.Med2 / (reference_miu * self.general.Bbeamfix_X * 1000 * self.general.fcd)))
        # ...................................................................................................................................................
        # beam deformation control
        if self.general.designlevel in ['CDN', 'CDL']:
            self.beamX.H2      = np.maximum(self.beamX.H2, self.beamX.L / (0.9 * 18))               
            self.beamY.H2      = np.maximum(self.beamY.H2, self.beamY.L / (0.9 * 18))
            self.beamStair.H2  = np.maximum(self.beamStair.H2, self.beamStair.L / (0.9 * 18))
        else:
            self.beamX.H2      = np.maximum(self.beamX.H2,self.beamX.L / (0.9 * 18))
            self.beamY.H2      = np.maximum(self.beamY.H2,self.beamY.L / 12)
            self.beamStair.H2  = np.maximum(self.beamStair.H2,self.beamStair.L / 12)
        # ...................................................................................................................................................
        self.beamX.H2      = np.maximum(self.beamX.H2, self.general.Hslab)
        self.beamStair.H2  = np.maximum(self.beamStair.H2, self.general.Hslab)
        self.beamY.H2      = np.maximum(self.beamY.H2, self.general.Hslab)
        # ...................................................................................................................................................
        self.beamX.H2      = np.ceil(20 * self.beamX.H2) / 20
        self.beamStair.H2  = np.ceil(20 * self.beamStair.H2) / 20
        self.beamY.H2      = np.ceil(20 * self.beamY.H2) / 20
        # ...................................................................................................................................................
        # beamtype = 1 |-> Wide beams EB in X; Tranverse beams in YY
        self.beamX.B = np.zeros((self.general.nstoreys, self.beamX.L.shape[1]))
        self.beamX.H = np.zeros((self.general.nstoreys, self.beamX.L.shape[1]))
        self.beamY.B = np.zeros((self.general.nstoreys, self.beamY.L.shape[1]))
        self.beamY.H = np.zeros((self.general.nstoreys, self.beamY.L.shape[1])) 
        if  self.general.BeamType == 1:
            self.beamY.WB_bc = np.zeros((self.general.nstoreys, self.beamY.L.shape[1]))
            self.beamY.B_A = np.zeros((self.general.nstoreys, self.beamY.L.shape[1]))                       
            self.beamY.B_B = np.zeros((self.general.nstoreys, self.beamY.L.shape[1]))                       
            for i in range(self.general.nstoreys):
                for j in range(self.beamY.L.shape[1]):
                    if self.beamY.index[j] == np.min(self.beamY.index) or self.beamY.index[j] == np.max(self.beamY.index):
                        self.beamY.B[i, j] = self.beamY.B2[i, j]
                        self.beamY.H[i, j] = self.beamY.H2[i, j]  
                    else:
                        nodei = self.beamY.elasnodei[i, j]
                        nodej = self.beamY.elasnodej[i, j]
                        bci = self.column.HX[np.where(self.column.nameref == nodei)]
                        bcj = self.column.HX[np.where(self.column.nameref == nodej)]
                        self.beamY.WB_bc[i, j] = np.maximum(bci, bcj)
                        self.beamY.H[i, j] = self.general.Hslab + 0 # TODO: ask about this to Hossam, it is different for predesign1
                        self.beamY.B_A[i, j] = self.beamY.WB_bc[i, j] + 1.50 * self.general.Hslab
                        self.beamY.B_B[i, j] = self.beamY.Med2[i, j] / (reference_miu_wide * (self.beamY.H[i, j] ** 2) * 1000 * self.general.fcd)
                        self.beamY.B[i, j] = np.maximum(self.beamY.B_A[i, j], self.beamY.B_B[i, j])
                        self.beamY.B[i, j] = np.ceil(20 * self.beamY.B[i, j]) / 20
            # ...................................................................................................................................................
            # the stair beams have to be EB to support the weight --> stairs are always in XX
            for i in range(self.general.nstoreys):
                for j in range(self.beamX.L.shape[1]):
                    if self.beamX.Astair1[i, j] > 0:
                        self.beamX.B[i, j] = self.beamX.B2[i, j]
                        self.beamX.H[i, j] = self.beamX.H2[i, j]
                    else:
                        pass
            # ...................................................................................................................................................
            for i in range(self.general.nstoreys):
                for j in range(self.beamX.L.shape[1]):
                    if self.beamX.index[j] == np.min(self.beamX.index) or self.beamX.index[j] == np.max(self.beamX.index):
                        self.beamX.B[i, j] = self.beamX.B2[i, j]
                        self.beamX.H[i, j] = self.beamX.H2[i, j]
                    else:
                        self.beamX.B[i, j] = self.general.Bbeamfix_X
                        self.beamX.H[i, j] = self.general.Hslab
            # ...................................................................................................................................................
            self.beamStair.H = self.beamStair.H2.copy()
            self.beamStair.B = self.beamStair.B2.copy()
        else:
            # ...................................................................................................................................................
            # beamtype = 2 |-> Emergent beams EB
            if self.general.BeamType == 2:
                self.beamX.H = self.beamX.H2.copy()
                self.beamX.B = self.beamX.B2.copy()
                self.beamY.H = self.beamY.H2.copy()
                self.beamY.B = self.beamY.B2.copy()
                self.beamStair.H = self.beamStair.H2.copy()
                self.beamStair.B = self.beamStair.B2.copy()
        # Adjusts the height of continuous beams according to beam index
        auxaa = np.unique(self.beamX.index)
        for j in range(len(auxaa)):
            indaux = self.beamX.index == auxaa[j]
            for i in range(self.general.nstoreys):
                self.beamX.H[i, indaux] = np.max(self.beamX.H[i, indaux])
                self.beamX.B[i, indaux] = np.max(self.beamX.B[i, indaux])
        # ...................................................................................................................................................
        auxaa = np.unique(self.beamY.index)
        for j in range(len(auxaa)):
            indaux = self.beamY.index == auxaa[j]
            for i in range(self.general.nstoreys):
                self.beamY.H[i, indaux] = np.max(self.beamY.H[i, indaux])
                self.beamY.B[i, indaux] = np.max(self.beamY.B[i, indaux])
        # Defines the final loads
        self.beamX.ped = self.beamX.ped2.copy()
        self.beamY.ped = self.beamY.ped2.copy()
        self.beamStair.ped = self.beamStair.ped2.copy()
        self.beamX.pedEQ = self.beamX.ped2EQ.copy()
        self.beamY.pedEQ = self.beamY.ped2EQ.copy()
        self.beamStair.pedEQ = self.beamStair.ped2EQ.copy()
        # ...................................................................................................................................................
        self.beamX.pedroof = self.beamX.proof2.copy()
        self.beamY.pedroof = self.beamY.proof2.copy()
        self.beamStair.pedroof = self.beamStair.proof2.copy()
        self.beamX.pedroofEQ = self.beamX.proof2EQ.copy()
        self.beamY.pedroofEQ = self.beamY.proof2EQ.copy()
        self.beamStair.pedroofEQ = self.beamStair.proof2EQ.copy()
        # ...................................................................................................................................................
        self.beamX.pedEQFinal = self.beamX.ped2EQFinal.copy()
        self.beamY.pedEQFinal = self.beamY.ped2EQFinal.copy()
        self.beamStair.pedEQFinal = self.beamStair.ped2EQFinal.copy()
        self.beamX.proofEQFinal = self.beamX.proof2EQFinal.copy()
        self.beamY.proofEQFinal = self.beamY.proof2EQFinal.copy()
        self.beamStair.proofEQFinal = self.beamStair.proof2EQFinal.copy()
        # ...................................................................................................................................................
        self.beamX.H      = np.ceil(20 * self.beamX.H) / 20
        self.beamStair.H  = np.ceil(20 * self.beamStair.H) / 20
        self.beamY.H      = np.ceil(20 * self.beamY.H) / 20
        self.beamX.B      = np.ceil(20 * self.beamX.B) / 20
        self.beamStair.B  = np.ceil(20 * self.beamStair.B) / 20
        self.beamY.B      = np.ceil(20 * self.beamY.B) / 20

    def _predesign_beams3(self):
        """Pre-design of beams for the case of slaborient = 3 |-> Unloading on XX and on YY beams
        """
        reference_miu = 0.25
        reference_miu_wide = 0.35  # Not applicable here!
        # 1) calculate the moment
        self.beamX.Med3 = self.beamX.ped3 * (self.beamX.L ** 2) / 12
        ix = self.beamX.Med3.shape[0] - 1
        self.beamX.Med3[ix, :] = self.beamX.proof3[ix, :] * (self.beamX.L[ix, :] ** 2) / 12
        self.beamStair.Med3 = self.beamStair.ped3 * (self.beamStair.L ** 2) / 12
        self.beamY.Med3 = self.beamY.ped3 * (self.beamY.L ** 2) / 12
        iy = self.beamY.Med3.shape[0] - 1
        self.beamY.Med3[iy, :] = self.beamY.proof3[iy ,:] * (self.beamY.L[iy, :] ** 2) / 12
        # ...................................................................................................................................................
        # TODO: Make sure that Ved2 and Med2 has the same size
        self.beamX.Ved3 = self.beamX.ped3 * (self.beamX.L) / 2
        self.beamX.Ved3[ix, :] = self.beamX.proof3[ix, :] * (self.beamX.L[ix, :]) / 2
        self.beamStair.Ved3 = self.beamStair.ped3 * (self.beamStair.L) / 2
        self.beamY.Ved3 = self.beamY.ped3 * (self.beamY.L) / 2
        self.beamY.Ved3[iy, :] = self.beamY.proof3[iy, :] * (self.beamY.L[iy, :]) / 2
        # ...................................................................................................................................................
        self.beamX.B3      = self.general.Bbeamfix_X * np.ones(self.beamX.Med3.shape)
        self.beamY.B3      = self.general.Bbeamfix_Y * np.ones(self.beamY.Med3.shape)
        self.beamStair.B3  = self.general.Bbeamfix_X * np.ones(self.beamStair.Med3.shape)
        # ...................................................................................................................................................
        self.beamX.H3      = np.maximum(self.general.Bbeamfix_X, (1 / 0.90) * np.sqrt(self.beamX.Med3 / (reference_miu * self.general.Bbeamfix_X * 1000 * self.general.fcd)))
        self.beamY.H3      = np.maximum(self.general.Bbeamfix_Y, (1 / 0.90) * np.sqrt(self.beamY.Med3 / (reference_miu * self.general.Bbeamfix_Y * 1000 * self.general.fcd)))
        self.beamStair.H3  = np.maximum(self.general.Bbeamfix_X, (1 / 0.90) * np.sqrt(self.beamStair.Med3 / (reference_miu * self.general.Bbeamfix_X * 1000 * self.general.fcd)))
        # ...................................................................................................................................................
        # beam deformation control
        if self.general.designlevel in ['CDN', 'CDL']:
            self.beamX.H3      = np.maximum(self.beamX.H3, self.beamX.L / (0.9 * 18))               
            self.beamY.H3      = np.maximum(self.beamY.H3, self.beamY.L / (0.9 * 18))
            self.beamStair.H3  = np.maximum(self.beamStair.H3, self.beamStair.L / (0.9 * 18))
        else:
            self.beamX.H3      = np.maximum(self.beamX.H3,self.beamX.L / 12)
            self.beamY.H3      = np.maximum(self.beamY.H3,self.beamY.L / 12)
            self.beamStair.H3  = np.maximum(self.beamStair.H3,self.beamStair.L / 12)
        # ...................................................................................................................................................
        self.beamX.H3      = np.maximum(self.beamX.H3, self.general.Hslab)
        self.beamStair.H3  = np.maximum(self.beamStair.H3, self.general.Hslab)
        self.beamY.H3      = np.maximum(self.beamY.H3, self.general.Hslab)
        # ...................................................................................................................................................
        self.beamX.H3      = np.ceil(20 * self.beamX.H3) / 20
        self.beamStair.H3  = np.ceil(20 * self.beamStair.H3) / 20
        self.beamY.H3      = np.ceil(20 * self.beamY.H3) / 20
        # ...................................................................................................................................................
        # beamtype = 2 |-> Emergent beams EB
        self.beamX.H = self.beamX.H3.copy()
        self.beamX.B = self.beamX.B3.copy()
        self.beamY.H = self.beamY.H3.copy()
        self.beamY.B = self.beamY.B3.copy()
        self.beamStair.H = self.beamStair.H3.copy()
        self.beamStair.B = self.beamStair.B3.copy()
        # Adjusts the height of continuous beams according to beam index
        auxaa = np.unique(self.beamX.index)
        for j in range(len(auxaa)):
            indaux = self.beamX.index == auxaa[j]
            for i in range(self.general.nstoreys):
                self.beamX.H[i, indaux] = np.max(self.beamX.H[i, indaux])
                self.beamX.B[i, indaux] = np.max(self.beamX.B[i, indaux])
        # ...................................................................................................................................................
        auxaa = np.unique(self.beamY.index)
        for j in range(len(auxaa)):
            indaux = self.beamY.index == auxaa[j]
            for i in range(self.general.nstoreys):
                self.beamY.H[i, indaux] = np.max(self.beamY.H[i, indaux])
                self.beamY.B[i, indaux] = np.max(self.beamY.B[i, indaux])
        # Defines the final loads
        self.beamX.ped = self.beamX.ped3.copy()
        self.beamY.ped = self.beamY.ped3.copy()
        self.beamStair.ped = self.beamStair.ped3.copy()
        self.beamX.pedEQ = self.beamX.ped3EQ.copy()
        self.beamY.pedEQ = self.beamY.ped3EQ.copy()
        self.beamStair.pedEQ = self.beamStair.ped3EQ.copy()
        # ...................................................................................................................................................
        self.beamX.pedroof = self.beamX.proof3.copy()
        self.beamY.pedroof = self.beamY.proof3.copy()
        self.beamStair.pedroof = self.beamStair.proof3.copy()
        self.beamX.pedroofEQ = self.beamX.proof3EQ.copy()
        self.beamY.pedroofEQ = self.beamY.proof3EQ.copy()
        self.beamStair.pedroofEQ = self.beamStair.proof3EQ.copy()
        # ...................................................................................................................................................
        self.beamX.pedEQFinal = self.beamX.ped3EQFinal.copy()
        self.beamY.pedEQFinal = self.beamY.ped3EQFinal.copy()
        self.beamStair.pedEQFinal = self.beamStair.ped3EQFinal.copy()
        self.beamX.proofEQFinal = self.beamX.proof3EQFinal.copy()
        self.beamY.proofEQFinal = self.beamY.proof3EQFinal.copy()
        self.beamStair.proofEQFinal = self.beamStair.proof3EQFinal.copy()
        # ...................................................................................................................................................
        self.beamX.H      = np.ceil(20 * self.beamX.H) / 20
        self.beamStair.H  = np.ceil(20 * self.beamStair.H) / 20
        self.beamY.H      = np.ceil(20 * self.beamY.H) / 20
        self.beamX.B      = np.ceil(20 * self.beamX.B) / 20
        self.beamStair.B  = np.ceil(20 * self.beamStair.B) / 20
        self.beamY.B      = np.ceil(20 * self.beamY.B) / 20

    def _get_joint_geometry(self):
        
        class Joint:
            pass

        self.joint = Joint()
        # ...................................................................................................................................................
        nodeaux = np.zeros((self.general.nstoreys, len(self.general.Reference)))
        HXreal = np.zeros(nodeaux.shape)
        HYreal = np.zeros(nodeaux.shape)
        FlagHXY = np.zeros(nodeaux.shape)
        nodeaux1 = np.zeros(self.general.nstoreys)
        nodeaux2 = np.zeros(self.general.nstoreys)
        HXreal1 = np.zeros(self.general.nstoreys)
        HXreal2 = np.zeros(self.general.nstoreys)
        HYreal1 = np.zeros(self.general.nstoreys)
        HYreal2 = np.zeros(self.general.nstoreys)
        for i in range(self.general.nstoreys):
            for j in range(len(self.general.Reference)):
                nodeaux[i, j] = (i+1)*100 + (j+1)
                if i == self.general.nstoreys - 1:
                    ind2 = np.where(self.column.elasCnodejref == nodeaux[i, j])
                    HXreal[i, j] = self.column.HX[ind2].copy()
                    HYreal[i, j] = self.column.HY[ind2].copy()
                    FlagHXY[i, j] = 0
                else:
                    ind1 = np.where(self.column.elasCnodeiref == nodeaux[i, j])
                    ind2 = np.where(self.column.elasCnodejref == nodeaux[i, j])
                    HXreal[i, j] = 0.50 * (self.column.HX[ind1] + self.column.HX[ind2])
                    HYreal[i, j] = 0.50 * (self.column.HY[ind1] + self.column.HY[ind2])
                    FlagHXY[i, j] = 1
            nodeaux1[i] = 20000 + (i+1)*100 + self.general.stair_node_left_mirror_1st_storey
            nodeaux2[i] = 20000 + (i+1)*100 + self.general.stair_node_left_mirror_1st_storey + 1
            ind1 = np.where(self.column.elasCnodeiref == nodeaux1[i])
            ind2 = np.where(self.column.elasCnodejref == nodeaux1[i])
            HXreal1[i] = 0.50 * (self.column.HX[ind1] + self.column.HX[ind2])
            HYreal1[i] = 0.50 * (self.column.HY[ind1] + self.column.HY[ind2])
            ind1 = np.where(self.column.elasCnodeiref == nodeaux2[i])
            ind2 = np.where(self.column.elasCnodejref == nodeaux2[i])
            HXreal2[i] = 0.50 * (self.column.HX[ind1] + self.column.HX[ind2])
            HYreal2[i] = 0.50 * (self.column.HY[ind1] + self.column.HY[ind2])
        # ...................................................................................................................................................
        FlagBEAMXright = np.zeros(nodeaux.shape)
        FlagBEAMXleft = np.zeros(nodeaux.shape)
        FlagBEAMYright = np.zeros(nodeaux.shape)
        FlagBEAMYleft = np.zeros(nodeaux.shape)
        HTOPBOT = np.zeros(nodeaux.shape)
        HBX = np.zeros(nodeaux.shape)
        HBY = np.zeros(nodeaux.shape)
        FlagBEAMXright1 = np.zeros(self.general.nstoreys)
        FlagBEAMXleft1 = np.zeros(self.general.nstoreys)
        FlagBEAMXright2 = np.zeros(self.general.nstoreys)
        FlagBEAMXleft2 = np.zeros(self.general.nstoreys)
        HTOPBOT1 = np.zeros(self.general.nstoreys)
        HTOPBOT2 = np.zeros(self.general.nstoreys)

        for i in range(self.general.nstoreys):
            for j in range(len(self.general.Reference)):
                nodeaux[i, j] = (i+1)*100 + (j+1)

                ind1 = np.where(self.beamX.elasnodei == nodeaux[i, j])
                if len(ind1[0]) != 0:
                    B1 = self.beamX.H[ind1].copy()
                    FlagBEAMXright[i, j] = 1
                else:
                    B1 = np.array([])
                    FlagBEAMXright[i, j] = 0

                ind2 = np.where(self.beamX.elasnodej == nodeaux[i, j])
                if len(ind2[0]) != 0:
                    B2 = self.beamX.H[ind2].copy()
                    FlagBEAMXleft[i, j] = 1
                else:
                    B2 = np.array([])
                    FlagBEAMXleft[i, j] = 0

                ind3 = np.where(self.beamY.elasnodei == nodeaux[i, j])
                if len(ind3[0]) != 0:
                    B3 = self.beamY.H[ind3].copy()
                    FlagBEAMYright[i, j] = 1
                else:
                    B3 = np.array([])
                    FlagBEAMYright[i, j] = 0

                ind4 = np.where(self.beamY.elasnodej == nodeaux[i, j])
                if len(ind4[0]) != 0:
                    B4 = self.beamY.H[ind4].copy()
                    FlagBEAMYleft[i, j] = 1
                else:
                    B4 = np.array([])
                    FlagBEAMYleft[i, j] = 0

                HTOPBOT[i, j] = np.max(np.concatenate([B1,B2,B3,B4]))
                HBX[i, j] = np.max(np.concatenate([B1,B2]))
                HBY[i, j] = np.max(np.concatenate([B3,B4]))

            nodeaux1[i] = 20000 + (i+1)*100 + self.general.stair_node_left_mirror_1st_storey
            nodeaux2[i] = 20000 + (i+1)*100 + self.general.stair_node_left_mirror_1st_storey + 1

            ind1 = np.where(self.beamStair.elasnodei == nodeaux1[i])
            if len(ind1[0]) != 0:
                B1 = self.beamX.H[ind1].copy()
                FlagBEAMXright1[i] = 1
            else:
                B1 = np.array([])
                FlagBEAMXright1[i] = 0
            ind2 = np.where(self.beamStair.elasnodej == nodeaux1[i])
            if len(ind2[0]) != 0:
                B2 = self.beamX.H[ind2].copy()
                FlagBEAMXleft1[i] = 1
            else:
                B2 = np.array([])
                FlagBEAMXleft1[i] = 0
            HTOPBOT1[i] = np.max(np.concatenate([B1,B2,B3,B4]))

            ind1 = np.where(self.beamStair.elasnodei == nodeaux2[i])
            if len(ind1[0]) != 0:
                B1 = self.beamX.H[ind1].copy()
                FlagBEAMXright2[i] = 1
            else:
                B1 = np.array([])
                FlagBEAMXright2[i] = 0
            ind2 = np.where(self.beamStair.elasnodej == nodeaux2[i])
            if len(ind2[0]) != 0:
                B2 = self.beamX.H[ind2].copy()
                FlagBEAMXleft2[i] = 1
            else:
                B2 = np.array([])
                FlagBEAMXleft2[i] = 0
            HTOPBOT2[i] = np.max(np.concatenate([B1,B2,B3,B4]))
        # ...................................................................................................................................................
        Coordinates = np.delete(self.general.Coords, self.general.Coords[:, 2] == 0, 0)
        Nodereal = (nodeaux.flatten()).reshape(-1, 1)
        HXreal = (HXreal.flatten()).reshape(-1, 1)
        HYreal = (HYreal.flatten()).reshape(-1, 1)
        HTOPBOT = (HTOPBOT.flatten()).reshape(-1, 1)
        HBX = (HBX.flatten()).reshape(-1, 1)
        HBY = (HBY.flatten()).reshape(-1, 1)
        FlagHXY = (FlagHXY.flatten()).reshape(-1, 1)
        FlagBEAMXleft = (FlagBEAMXleft.flatten()).reshape(-1, 1)
        FlagBEAMXright = (FlagBEAMXright.flatten()).reshape(-1, 1)
        FlagBEAMYleft = (FlagBEAMYleft.flatten()).reshape(-1, 1)
        FlagBEAMYright = (FlagBEAMYright.flatten()).reshape(-1, 1)
        aux111 = np.zeros(len(FlagBEAMYright))
        FlagType = np.zeros((len(FlagBEAMYright), 1))
        for i in range(len(FlagBEAMYright)):
            aux111[i] = FlagBEAMXleft[i] + FlagBEAMXright[i] + FlagBEAMYleft[i] + FlagBEAMYright[i]
            if FlagHXY[i] == 0:
                FlagType[i] = 3
            else:
                if aux111[i] < 4:
                    FlagType[i] = 1
                else:
                    FlagType[i] = 2
        # ...................................................................................................................................................
        self.joint.Data = np.hstack((Nodereal,HXreal,HYreal,HTOPBOT,Coordinates,FlagHXY,FlagBEAMXleft,FlagBEAMXright,FlagBEAMYleft,FlagBEAMYright,FlagType,HBX,HBY))
        joint1000 = np.hstack((1000 + Nodereal, Coordinates))
        joint2000 = np.hstack((2000 + Nodereal, Coordinates[:, 0:2], Coordinates[:, 2].reshape(-1, 1)-HTOPBOT/2))
        joint3000 = np.hstack((3000 + Nodereal, Coordinates[:, 0].reshape(-1, 1)+HXreal/2, Coordinates[:, 1:]))
        joint4000 = np.hstack((4000 + Nodereal, Coordinates[:, 0].reshape(-1, 1), Coordinates[:, 1].reshape(-1, 1)+HYreal/2, Coordinates[:, 2].reshape(-1, 1)))
        joint5000 = np.hstack((5000 + Nodereal, Coordinates[:, 0].reshape(-1, 1)-HXreal/2, Coordinates[:, 1:]))
        joint6000 = np.hstack((6000 + Nodereal, Coordinates[:, 0].reshape(-1, 1), Coordinates[:, 1].reshape(-1, 1)-HYreal/2, Coordinates[:, 2].reshape(-1, 1)))
        joint7000 = np.hstack((7000 + Nodereal, Coordinates[:, 0:2], Coordinates[:, 2].reshape(-1, 1)+HTOPBOT/2))
        self.joint.nodes = np.hstack((joint1000,joint2000,joint3000,joint4000,joint5000,joint6000,joint7000))
        # ...................................................................................................................................................
        self.joint.Lstair1000 = self.general.CoordsExtra1.copy(); self.joint.Lstair1000[:, 0] += 1000
        self.joint.Lstair2000 = self.general.CoordsExtra1.copy(); self.joint.Lstair2000[:, 0] += 2000 
        self.joint.Lstair2000[:, 3] -= HTOPBOT1/2
        self.joint.Lstair3000 = self.general.CoordsExtra1.copy(); self.joint.Lstair3000[:, 0] += 3000 
        self.joint.Lstair3000[:, 1] += HXreal1/2
        self.joint.Lstair7000 = self.general.CoordsExtra1.copy(); self.joint.Lstair7000[:, 0] += 7000 
        self.joint.Lstair7000[:, 3] += HTOPBOT1/2

        self.joint.Rstair1000 = self.general.CoordsExtra2.copy(); self.joint.Rstair1000[:, 0] += 1000
        self.joint.Rstair2000 = self.general.CoordsExtra2.copy(); self.joint.Rstair2000[:, 0] += 2000 
        self.joint.Rstair2000[:, 3] -= HTOPBOT2/2
        self.joint.Rstair5000 = self.general.CoordsExtra2.copy(); self.joint.Rstair5000[:, 0] += 5000 
        self.joint.Rstair5000[:, 1] -= HXreal2/2
        self.joint.Rstair7000 = self.general.CoordsExtra2.copy(); self.joint.Rstair7000[:, 0] += 7000 
        self.joint.Rstair7000[:, 3] += HTOPBOT2/2
