"""
Building information model (BIM)

- Predesign
- Gravity analysis
- Lateral load analysis
- Maximum allowable stress design, Limit state design and capacity design
- Section uniformization, iterative design, section increase and material change routines

"""

from src.rcmrf.eu.bim.design import Designer
import numpy as np
from src.utils import get_time_based_seed
from scipy.stats import lognorm, uniform

seed = get_time_based_seed()  # determine the random number generator set based on the date and time
np.random.seed(seed)  # set the random number generator seed

class BuildingInformationModel(Designer):

    def make_final_design(self):

        aux = 9999  # Flag to define the stage of the design, 9999: initial design 
        # ...........................................................................
        self.beamX.Hgrav = self.beamX.H.copy()
        self.beamY.Hgrav = self.beamY.H.copy()
        self.beamStair.Hgrav = self.beamStair.H.copy()
        # ...........................................................................
        self.beamX.Bgrav = self.beamX.B.copy()
        self.beamY.Bgrav = self.beamY.B.copy()
        self.beamStair.Bgrav = self.beamStair.B.copy()
        # ...........................................................................
        self.column.HXgrav = self.column.HX.copy()
        self.column.HYgrav = self.column.HY.copy()
        # ...........................................................................
        self.general.fckgrav = self.general.fck.copy()
        self.general.fckcubegrav = self.general.fckcube.copy()
        self.general.fcdgrav = self.general.fcd.copy()
        self.general.fcdEQgrav = self.general.fcdEQ.copy()
        self.general.fsygrav = self.general.fsyk.copy()
        self.general.fsykgrav = self.general.fsyk.copy()
        self.general.fsydgrav = self.general.fsyd.copy()
        self.general.fsydEQgrav = self.general.fsydEQ.copy()
        self.general.ColITER = 0
        ncounting = 0
        max_niters = 50
        # ...........................................................................
        # Setting some limitations based on engineering judgement. They can be changed.
        if self.general.designlevel == 'CDN':
            if self.general.nstoreys <= 3:
                self.column.maxHsquared = 0.45
                self.column.maxHrectangular = 0.70
            elif self.general.nstoreys <= 6:
                self.column.maxHsquared = 0.60
                self.column.maxHrectangular = 1.00
            elif self.general.nstoreys <= 9:
                self.column.maxHsquared = 0.85
                self.column.maxHrectangular = 1.20
            else:
                raise NotImplementedError('Frame buildings are not allowed to have more than 9 stories.')
        elif self.general.designlevel == 'CDL':
            if self.general.nstoreys <= 3:
                if self.general.ag <= 0.20:
                    self.column.maxHsquared = 0.45
                    self.column.maxHrectangular = 0.70
                else:
                    self.column.maxHsquared = 0.60
                    self.column.maxHrectangular = 0.80                    
            elif self.general.nstoreys <= 6:
                if self.general.ag <= 0.20:
                    self.column.maxHsquared = 0.60
                    self.column.maxHrectangular = 1.00
                else:
                    self.column.maxHsquared = 0.80
                    self.column.maxHrectangular = 1.20  
            elif self.general.nstoreys <= 9:
                if self.general.ag <= 0.20:
                    self.column.maxHsquared = 0.80
                    self.column.maxHrectangular = 1.20
                else:
                    self.column.maxHsquared = 1.00
                    self.column.maxHrectangular = 1.40  
            else:
                raise NotImplementedError('Frame buildings are not allowed to have more than 9 stories.')
        elif self.general.designlevel in ['CDM', 'CDH']:
            if self.general.nstoreys <= 3:
                self.column.maxHsquared = 0.60
                self.column.maxHrectangular = 0.80
            elif self.general.nstoreys <= 6:
                self.column.maxHsquared = 0.80
                self.column.maxHrectangular = 1.00
            elif self.general.nstoreys <= 9:
                self.column.maxHsquared = 0.80
                self.column.maxHrectangular = 1.30
            else:
                raise NotImplementedError('Frame buildings are not allowed to have more than 9 stories.')
        # ...........................................................................
        while aux > 0.1 and ncounting <= max_niters:
            # Do modifications to satisfy the design requirements. 
            # Make use of the flags to identify necessary modifications.
            if aux == 9999: # The initial design
                pass
            elif aux == 8888: # Exceeded number of iterations, no solution
                ncounting = max_niters + 1
            # ...........................................................................
            elif aux == 7777: # I think this one does not work
                ncounting += 1
                self.beamX.H = self.beamX.Hgrav.copy()
                self.beamY.H = self.beamY.Hgrav.copy()
                self.beamStair.H = self.beamStair.Hgrav.copy()
                self.beamX.B = 0 * self.beamX.Hgrav + self.general.Bbeamfix_X
                self.beamY.B = 0 * self.beamY.Hgrav + self.general.Bbeamfix_Y
                self.beamX.Bgrav = self.beamX.B.copy()
                self.beamY.Bgrav = self.beamY.B.copy()
                self.column.HX = self.column.HXgrav.copy()
                self.column.HY = self.column.HYgrav.copy()
                if ncounting < 1:  # to not use the same value once it has been change in design element i.e. beam or column (added by #HMA)
                    # TODO: But this part in fact would never be activated. We just increased ncounting by 1?
                    self.general.fck = self.general.fckgrav.copy()
                    self.general.fckcube = self.general.fckcubegrav.copy()
                    self.general.fcd = self.fcdgrav.copy()
                    self.general.fcdEQ = self.general.fcdEQgrav.copy()
                    self.general.fsyk = self.general.fsykgrav.copy()
                    self.general.fsyd = self.general.fsydgrav.copy()
                    self.general.fsydEQ = self.general.fsydEQgrav.copy()
            # ...........................................................................
            elif aux == 5555: # changing column to square
                ncounting += 1
                self.general.Flag1 = 1
                self.general.ColumnType = 1
                self.beamX.H = self.beamX.Hgrav.copy()
                self.beamY.H = self.beamY.Hgrav.copy()
                self.beamStair.H = self.beamStair.Hgrav.copy()
                self.beamX.B = 0 * self.beamX.Hgrav + self.general.Bbeamfix_X
                self.beamY.B = 0 * self.beamY.Hgrav + self.general.Bbeamfix_Y
                self.column.HX = (self.column.HXgrav * self.column.HYgrav) ** 0.5
                self.column.HY = self.column.HX.copy()
                self.column.HX = np.maximum(np.ceil(20 * self.column.HX) / 20, 0.30)
                self.column.HY = np.maximum(np.ceil(20 * self.column.HY) / 20, 0.30)
                self.column.HXgrav = self.column.HX.copy()
                self.column.HYgrav = self.column.HY.copy()
                self.general.fck = self.general.fckgrav.copy()
                self.general.fckcube = self.general.fckcubegrav.copy()
                self.general.fcd = self.general.fcdgrav.copy()
                self.general.fcdEQ = self.general.fcdEQgrav.copy()
                self.general.fsyk = self.general.fsykgrav.copy()
                self.general.fsyd = self.general.fsydgrav.copy()
                self.general.fsydEQ = self.general.fsydEQgrav.copy()
            # ...........................................................................
            else:
                ncounting += 1
                ###################################################################################
                # BEAMS 
                ###################################################################################
                if self.general.BeamType == 2: # emergent beam
                    self.beamX.H[CvFLAGX > 0] = self.beamX.H[CvFLAGX > 0] + 0.05
                    self.beamY.H[CvFLAGY > 0] = self.beamY.H[CvFLAGY > 0] + 0.05
                    self.beamStair.H[CvFLAGSTAIR > 0] = self.beamStair.H[CvFLAGSTAIR > 0] + 0.05
                elif self.general.BeamType == 1: # wide beam (low-depth)
                    # ...........................................................................
                    if self.general.slaborient == 1:
                        for i in range(self.general.nstoreys):
                            for j in range(self.beamX.L.shape[1]):
                                if self.beamX.index[j] == np.min(self.beamX.index) or self.beamX.index[j] == np.max(self.beamX.index): 
                                    if CvFLAGX[i, j] == 1: # Change depth of the beams
                                        self.beamX.H[i, j] = self.beamX.H[i, j] + 0.05
                                else:
                                    if CvFLAGX[i, j] == 1: # Change width of the beams
                                        self.beamX.B[i, j] = self.beamX.B[i, j] + 0.05
                                if self.beamX.B[i, j] > 0.80:
                                    self.beamX.B[i, j] = self.beamX.Bgrav[i, j].copy()
                                    self.beamX.H[i, j] = self.beamX.H[i, j] + 0.05
                        self.beamY.H[CvFLAGY > 0] = self.beamY.H[CvFLAGY > 0] + 0.05
                        self.beamStair.H[CvFLAGSTAIR > 0] = self.beamStair.H[CvFLAGSTAIR > 0] + 0.05
                    # ...........................................................................
                    elif self.general.slaborient == 2:
                        for i in range(self.general.nstoreys):
                            for j in range(self.beamY.L.shape[1]):
                                if self.beamY.index[j] == np.min(self.beamY.index) or self.beamY.index[j] == np.max(self.beamY.index):
                                    if CvFLAGY[i, j] == 1: # Change depth of the beams
                                        self.beamY.H[i, j] = self.beamY.H[i, j] + 0.05
                                else:
                                    if CvFLAGY[i, j] == 1: # Change width of the beams
                                        self.beamY.B[i, j] = self.beamY.B[i, j] + 0.05
                                if self.beamY.B[i, j] > 0.80:
                                    self.beamY.B[i, j] = self.beamY.Bgrav[i, j].copy()
                                    self.beamY.H[i, j] = self.beamY.H[i, j] + 0.05
                        self.beamX.H[CvFLAGX > 0] = self.beamX.H[CvFLAGX > 0] + 0.05
                        self.beamStair.H[CvFLAGSTAIR > 0] = self.beamStair.H[CvFLAGSTAIR > 0] + 0.05
                # ...........................................................................
                # Adjusts the height of continuous beams according to beam index
                auxaa = np.unique(self.beamX.index)
                for j in range(len(auxaa)):
                    indaux = self.beamX.index == auxaa[j]
                    for i in range(self.general.nstoreys):
                        self.beamX.H[i, indaux] = np.max(self.beamX.H[i, indaux])
                        self.beamX.B[i, indaux] = np.max(self.beamX.B[i, indaux])
                auxaa = np.unique(self.beamY.index)
                for j in range(len(auxaa)):
                    indaux = self.beamY.index == auxaa[j]
                    for i in range(self.general.nstoreys):
                        self.beamY.H[i, indaux] = np.max(self.beamY.H[i, indaux])
                        self.beamY.B[i, indaux] = np.max(self.beamY.B[i, indaux])
                ###################################################################################
                # COLUMNS 
                ###################################################################################
                if self.general.ColumnType == 1:
                    self.column.HX[CpFLAGX > 0] = self.column.HX[CpFLAGX > 0] + 0.05
                    self.column.HY[CpFLAGY > 0] = self.column.HY[CpFLAGY > 0] + 0.05
                    self.column.Hmax = np.maximum(self.column.HX, self.column.HY)
                    self.column.HX = self.column.Hmax.copy()
                    self.column.HY = self.column.HX.copy()
                else:
                    self.column.HX[CpFLAGX > 0] = self.column.HX[CpFLAGX > 0] + 0.05
                    self.column.HY[CpFLAGY > 0] = self.column.HY[CpFLAGY > 0] + 0.05
                    if self.general.designlevel in ['CDM', 'CDH']:
                        self.column.HY[:, self.column.Colindex1] = np.maximum(self.column.HY[:, self.column.Colindex1], 0.50 * self.column.HX[:, self.column.Colindex1])
                        self.column.HX[:, self.column.Colindex2] = np.maximum(self.column.HX[:, self.column.Colindex2], 0.50 * self.column.HY[:, self.column.Colindex2])
                        self.column.HY[:, self.column.Colindex1] = np.ceil(20 * self.column.HY[:, self.column.Colindex1]) / 20
                        self.column.HX[:, self.column.Colindex2] = np.ceil(20 * self.column.HX[:, self.column.Colindex2]) / 20
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
                for ii in range(self.column.HX.shape[1]):
                    Hmax = 0.0
                    for jj in range(self.general.nstoreys-1, -1, -1): # going backwards
                        if jj == self.general.nstoreys - 1: # last storey
                            pass
                        else:
                            Hmax = max(Hmax, self.column.HX[jj, ii], self.column.HX[jj+1, ii])
                            if self.column.HX[jj, ii] <= Hmax:
                                self.column.HX[jj, ii] = Hmax.copy()
                            elif self.column.HX[jj, ii] <= self.column.HX[jj-1, ii] - 0.10:
                                self.column.HX[jj, ii] = self.column.HX[jj-1, ii] - 0.10
                            else:
                                pass
                    
                    self.column.HX[0, ii] = max(Hmax, self.column.HX[0, ii])
                # ...........................................................................
                for ii in range(self.column.HY.shape[1]):
                    Hmax = 0
                    for jj in range(self.general.nstoreys-1, -1, -1): # going backwards
                        if jj == self.general.nstoreys - 1: # last storey
                            pass
                        else:
                            Hmax = max(Hmax, self.column.HY[jj, ii], self.column.HY[jj+1, ii])
                            if self.column.HY[jj, ii] <= Hmax:
                                self.column.HY[jj, ii] = Hmax.copy()
                            elif self.column.HY[jj, ii] <= self.column.HY[jj-1, ii] - 0.10:
                                self.column.HY[jj, ii] = self.column.HY[jj-1, ii] - 0.10
                            else:
                                pass
                    
                    self.column.HY[0, ii] = max(Hmax, self.column.HY[0, ii])
                # ...........................................................................
                # uniformizes the section geometry (HX and HY) every 2 storeys (Up to 9 storeys only)
                if self.general.designlevel == 'CDH':
                    HXmax = self.column.HX.max(axis=0)
                    HYmax = self.column.HY.max(axis=0)
                    self.column.HX = np.ones(self.column.HX.shape) * HXmax # putting maximum always makes CDH always with Square columns (HMA)
                    self.column.HY = np.ones(self.column.HY.shape) * HYmax # putting maximum always makes CDH always with Square columns (HMA)
                else:
                    if self.general.nstoreys <= 3:
                        HXmax = self.column.HX.max(axis=0)
                        HYmax = self.column.HY.max(axis=0)
                        self.column.HX = np.ones(self.column.HX.shape) * HXmax
                        self.column.HY = np.ones(self.column.HY.shape) * HYmax
                    else:
                        for jj in range(1, self.general.nstoreys, 2):
                            if jj == 1:
                                self.column.HX[jj, :] = np.maximum(self.column.HX[jj, :], self.column.HX[jj-1, :])
                                self.column.HX[jj-1, :] = self.column.HX[jj, :].copy()
                                self.column.HY[jj, :] = np.maximum(self.column.HY[jj, :], self.column.HY[jj-1, :])
                                self.column.HY[jj-1, :] = self.column.HY[jj, :].copy()
                            else:
                                self.column.HX[jj, :] = np.maximum(self.column.HX[jj, :], self.column.HX[jj-1, :])
                                self.column.HX[jj, :] = np.maximum(self.column.HX[jj, :], self.column.HX[jj-2, :] - 0.10)
                                self.column.HX[jj-1, :] = self.column.HX[jj, :].copy()
                                self.column.HY[jj, :] = np.maximum(self.column.HY[jj, :], self.column.HY[jj-1, :])
                                self.column.HY[jj, :] = np.maximum(self.column.HY[jj, :], self.column.HY[jj-2, :] - 0.10)
                                self.column.HY[jj-1, :] = self.column.HY[jj, :].copy()
                        if self.general.nstoreys % 2 == 1:
                            jj = self.general.nstoreys - 1
                            self.column.HX[jj, :] = np.maximum(self.column.HX[jj, :], self.column.HX[jj-1, :] - 0.10)
                            self.column.HY[jj, :] = np.maximum(self.column.HY[jj, :], self.column.HY[jj-1, :] - 0.10)
            
            print(f'\nDesign iteration {ncounting}')
            self._do_all_analyses()
            CvFLAGX, CvFLAGY, CvFLAGSTAIR, CpFLAGX, CpFLAGY, aux, auxbeam = self._make_trial_design()
        # ...........................................................................
        # Check the maximum number of iterations and save the datatables... 
        # ...........................................................................
        self.final_design = {}
        if ncounting >= max_niters:
            print('------------------------------------')
            print('Design routine interrupted due to the excessive number of trials...')
            print('------------------------------------')
        else:
            self._do_extra_analyses()
            self._adjust_for_quality()
            self._get_joint_geometry()
            keys = ('Name','Nodei','Nodej','B','H','L',
                    'Ntopcorner1','Ntopcorner9','FItopcorner1','FItopcorner9',
                    'Nbotcorner1','Nbotcorner9','FIbotcorner1','FIbotcorner9',
                    'FIw1','sw1','Nlegsyy1','Nlegszz1',
                    'FIw9','sw9','Nlegsyy9','Nlegszz9',
                    'Ntopint1','Ntopint9','FItopint1','FItopint9',
                    'Nbotint1','Nbotint9','FIbotint1','FIbotint9',
                    'Mneg1','Mpos1','Mneg9','Mpos9',
                    'fcm_Q','fsyl_Q','fsyw_Q','cover_Q','sw_Q1','sw_Q9','bondslipfact_Q','pedEQ')
            self.final_design['beamX'] = {key: self.beamX.Matrix[:, i] for i, key in enumerate(keys)}
            self.final_design['beamY'] = {key: self.beamY.Matrix[:, i] for i, key in enumerate(keys)}
            self.final_design['beamStair'] = {key: self.beamStair.Matrix[:, i] for i, key in enumerate(keys)}
            keys = ('Name','Nodei','Nodej','HX','HY','L','Storey','Perimeter',
                    'nBarHminus','nlayintX','fi_corner','fi_layint','RHosl','sw','fiw','nw_paraleltoX','nw_paraleltoY','N_CP',
                    'fcm_Q','fsyl_Q','fsyw_Q','cover_Q','sw_Q','fi_corner_Q','fi_layint_Q','fiw_Q','bondslipfact_Q')
            self.final_design['column'] = {key: self.column.Matrix[:, i] for i, key in enumerate(keys)}
            self.final_design['results'] = self.results.copy()
            self.final_design['general'] = self.general.__dict__
            self.final_design['joint'] = self.joint.__dict__

    def _adjust_for_quality(self):
        """
        adjusts the material and stirrup spacing of columns based on the construction quality or
        deterioration level asssumed for the ductility.
        """
        np.random.seed(1987) # seed number used in MATLAB, TODO: could be removed after validation stage

        self.beamX.cover = 0.03
        self.beamY.cover = 0.03
        self.beamStair.cover = 0.03
        self.column.cover = 0.03
        ncolumns = self.column.Matrix.shape[0]
        nbeamX = self.beamX.Matrix.shape[0]
        nbeamY = self.beamY.Matrix.shape[0]
        nbeamStair = self.beamStair.Matrix.shape[0]
        # ...........................................................................
        if self.general.quality == 1:
            if self.general.designlevel in ['CDM', 'CDH']:
                bondslipfact = 0.0
            elif self.general.designlevel == 'CDL':
                bondslipfact = 0.50
            else:
                bondslipfact = 1.00

            sigma_fck = 0.10
            sigma_fsyk = 0.01
            sigma_cover = 0.10
            uniform_low = 1.00
            uniform_high = 1.05

        elif self.general.quality == 2:
            if self.general.designlevel in ['CDM', 'CDH']:
                bondslipfact = 0.5
            else:
                bondslipfact = 1.00

            sigma_fck = 0.20
            sigma_fsyk = 0.025
            sigma_cover = 0.20
            uniform_low = 1.00
            uniform_high = 1.30

        elif self.general.quality == 3:
            bondslipfact = 1.00
            sigma_fck = 0.30
            sigma_fsyk = 0.05
            sigma_cover = 0.30
            uniform_low = 1.00
            uniform_high = 1.50
        # ...........................................................................
        # Generating lognormal-distributed and uniform distributed numbers following:
        # https://towardsdatascience.com/generating-random-numbers-and-arrays-in-matlab-and-numpy-47dcc9997650
        # So that we can make a comparison between results from matlab and python codes
        # ...........................................................................
        mu = np.log(1.0)
        meanfcrat = np.log(lognorm.ppf(np.random.rand(), s=sigma_fck, scale=np.exp(mu)))
        aa = (self.general.fck + 8) * lognorm.ppf(np.random.rand(ncolumns), s=sigma_fck, scale=np.exp(meanfcrat))
        aa[aa < 6] = 6
        self.column.Matrix[:, 18] = aa.copy()
        bb = (self.general.fck + 8) * lognorm.ppf(np.random.rand(nbeamX), s=sigma_fck, scale=np.exp(meanfcrat))
        bb[bb < 6] = 6
        self.beamX.Matrix[:, 34] = bb.copy()
        cc = (self.general.fck + 8) * lognorm.ppf(np.random.rand(nbeamY), s=sigma_fck, scale=np.exp(meanfcrat))
        cc[cc < 6] = 6
        self.beamY.Matrix[:, 34] = cc.copy()
        dd = (self.general.fck + 8) * lognorm.ppf(np.random.rand(nbeamStair), s=sigma_fck, scale=np.exp(meanfcrat))
        dd[dd < 6] = 6
        self.beamStair.Matrix[:, 34] = dd.copy()
        # ...........................................................................
        self.column.Matrix[:, 19] = self.general.fsyk * lognorm.ppf(np.random.rand(ncolumns), s=sigma_fsyk, scale=np.exp(mu))
        self.column.Matrix[:, 20] = self.general.fsyk * lognorm.ppf(np.random.rand(ncolumns), s=sigma_fsyk, scale=np.exp(mu))
        self.column.Matrix[:, 21] = self.column.cover * lognorm.ppf(np.random.rand(ncolumns), s=sigma_cover, scale=np.exp(mu))
        self.column.Matrix[:, 22] = self.column.Matrix[:, 13] * uniform.ppf(np.random.rand(ncolumns), loc=uniform_low, scale=uniform_high-uniform_low)
        self.column.Matrix[:, 23] = self.column.Matrix[:, 10] + uniform.ppf(np.random.rand(ncolumns), loc=-0.0001, scale=0.0002) # change 4 MITRISK - fiint TODO: ask MITRISK?
        self.column.Matrix[:, 24] = self.column.Matrix[:, 11] + uniform.ppf(np.random.rand(ncolumns), loc=-0.0001, scale=0.0002) # change 4 MITRISK - ficorner
        self.column.Matrix[:, 25] = self.column.Matrix[:, 14] + uniform.ppf(np.random.rand(ncolumns), loc=-0.0001, scale=0.0002) # change 4 MITRISK - fiw
        # ...........................................................................
        self.beamX.Matrix[:, 35] = self.general.fsyk * lognorm.ppf(np.random.rand(nbeamX), s=sigma_fsyk, scale=np.exp(mu)) # fsyl
        self.beamX.Matrix[:, 36] = self.general.fsyk * lognorm.ppf(np.random.rand(nbeamX), s=sigma_fsyk, scale=np.exp(mu)) # fsyw
        self.beamX.Matrix[:, 37] = self.beamX.cover * lognorm.ppf(np.random.rand(nbeamX), s=sigma_cover, scale=np.exp(mu)) # cover
        self.beamX.Matrix[:, 38] = self.beamX.Matrix[:, 15] * uniform.ppf(np.random.rand(nbeamX), loc=uniform_low, scale=uniform_high-uniform_low) # sw1
        self.beamX.Matrix[:, 39] = self.beamX.Matrix[:, 19] * uniform.ppf(np.random.rand(nbeamX), loc=uniform_low, scale=uniform_high-uniform_low) # sw9
        # ...........................................................................    
        self.beamY.Matrix[:, 35] = self.general.fsyk * lognorm.ppf(np.random.rand(nbeamY), s=sigma_fsyk, scale=np.exp(mu))
        self.beamY.Matrix[:, 36] = self.general.fsyk * lognorm.ppf(np.random.rand(nbeamY), s=sigma_fsyk, scale=np.exp(mu))
        self.beamY.Matrix[:, 37] = self.beamY.cover * lognorm.ppf(np.random.rand(nbeamY), s=sigma_cover, scale=np.exp(mu))
        self.beamY.Matrix[:, 38] = self.beamY.Matrix[:, 15] * uniform.ppf(np.random.rand(nbeamY), loc=uniform_low, scale=uniform_high-uniform_low)
        self.beamY.Matrix[:, 39] = self.beamY.Matrix[:, 19] * uniform.ppf(np.random.rand(nbeamY), loc=uniform_low, scale=uniform_high-uniform_low)

        self.beamStair.Matrix[:, 35] = self.general.fsyk * lognorm.ppf(np.random.rand(nbeamStair), s=sigma_fsyk, scale=np.exp(mu))
        self.beamStair.Matrix[:, 36] = self.general.fsyk * lognorm.ppf(np.random.rand(nbeamStair), s=sigma_fsyk, scale=np.exp(mu))
        self.beamStair.Matrix[:, 37] = self.beamStair.cover * lognorm.ppf(np.random.rand(nbeamStair), s=sigma_cover, scale=np.exp(mu))
        self.beamStair.Matrix[:, 38] = self.beamStair.Matrix[:, 15] * uniform.ppf(np.random.rand(nbeamStair), loc=uniform_low, scale=uniform_high-uniform_low)
        self.beamStair.Matrix[:, 39] = self.beamStair.Matrix[:, 19] * uniform.ppf(np.random.rand(nbeamStair), loc=uniform_low, scale=uniform_high-uniform_low)
        # ...........................................................................
        self.column.Matrix[:, 26] = 0.0 * self.column.Matrix[:, 0] + bondslipfact
        self.beamX.Matrix[:, 40] = 0.0 * self.beamX.Matrix[:, 0] + bondslipfact
        self.beamY.Matrix[:, 40] = 0.0 * self.beamY.Matrix[:, 0] + bondslipfact
        self.beamStair.Matrix[:, 40] = 0.0 * self.beamStair.Matrix[:, 0] + bondslipfact
