from src.rcmrf.eu.bim.analysis import ElasticModelBuilder
import numpy as np
from scipy.interpolate import RegularGridInterpolator

# CONSTANTS
ABACUS_X = np.array([0, 0.0277777777777778, 0.0555555555555556, 0.0833333333333333, 0.111111111111111, 0.138888888888889, 0.166666666666667, 0.194444444444444, 0.222222222222222, 0.250000000000000])
ABACUS_Y = np.array([0.000000000000000, 0.0777777777777778, 0.155555555555556, 0.233333333333333, 0.311111111111111, 0.388888888888889, 0.466666666666667, 0.544444444444444, 0.622222222222222, 0.700000000000000])
ABACUS_Z = np.fromstring("""
0 0.00970555555555555 0.0194111111111111 0.0291166666666667 0.0440915555555555 0.0702232222222222 0.102243666666667 0.131266888888889 0.164154666666667 0.198892000000000
0 0.0102261111111111 0.0205228888888889 0.0309256666666667 0.0472451111111111 0.0758481111111111 0.108280777777778 0.141384444444444 0.178964000000000 0.217524333333333
0 0.0100394444444444 0.0200788888888889 0.0301183333333333 0.0487321111111111 0.0823443333333333 0.117531222222222 0.155449111111111 0.195662444444444 0.236222222222222
0 0.00899250000000000 0.0164730000000000 0.0235755000000000 0.0437693333333333 0.0865265555555556 0.127303000000000 0.170060666666667 0.213891555555556 0.257134666666667
0 0.00529166666666667 0.0105833333333333 0.0155798888888889 0.0384402222222222 0.0905643333333333 0.137157222222222 0.185445111111111 0.232910444444444 0.279392888888889
0 0.00386794444444444 0.00794322222222222 0.0120185000000000 0.0384363333333333 0.0967137777777778 0.150187333333333 0.203398333333333 0.253433222222222 0.299813444444444
0 0.00610583333333333 0.0122116666666667 0.0204363333333333 0.0506684444444444 0.110025777777778 0.166942333333333 0.220166777777778 0.271086333333333 0.315488333333333
0 0.0122712222222222 0.0262984444444444 0.0403256666666666 0.0718958888888889 0.129945222222222 0.186308666666667 0.238572111111111 0.289164000000000 0.332430555555556
0 0.0195072222222222 0.0390144444444444 0.0639063888888889 0.100675333333333 0.156645555555556 0.210372888888889 0.260533555555556 0.312908111111111 0.359491777777778
0 0.0309847222222222 0.0619694444444444 0.0929541666666667 0.132961000000000 0.185786555555556 0.239298333333333 0.283691888888889 0.338197000000000 0.387725000000000
""", dtype=float, sep=" ").reshape(10, 10)
# TODO: Allow extrapolation --> bounds_error=False, fill_value=None. This is not possible in MATLAB
cdl_column_rho_interpolator = RegularGridInterpolator((ABACUS_X, ABACUS_Y), ABACUS_Z.T, method='linear', bounds_error=False)
# cdl_column_rho_interpolator = RegularGridInterpolator((ABACUS_X, ABACUS_Y), ABACUS_Z.T, method='linear', bounds_error=False, fill_value=None)

class Designer(ElasticModelBuilder):

    def _make_trial_design(self):

        # Load the results from the analyses conducted all loads applied to the buildings and establish the final load combinations.
        self._force_in_beams()
        self._force_in_columns()

        # Increases the dimensions and, if ok = 0, designs the reinforcement.
        if self.general.designlevel == 'CDN':
            CvFLAGX, CvFLAGY, CvFLAGStair, auxbeam = self._cdn_beams()
            CpFLAGX, CpFLAGY, CpFLAGfc, auxcol = self._cdn_columns(auxbeam)
        elif self.general.designlevel == 'CDL':
            CvFLAGX, CvFLAGY, CvFLAGStair, auxbeam = self._cdl_beams()
            CpFLAGX, CpFLAGY, CpFLAGfc, auxcol = self._cdl_columns(auxbeam)
        elif self.general.designlevel == 'CDM':
            CvFLAGX, CvFLAGY, CvFLAGStair, auxbeam = self._cdm_beams()
            CpFLAGX, CpFLAGY, CpFLAGfc, auxcol = self._cdm_columns(auxbeam)
        elif self.general.designlevel == 'CDH':
            CvFLAGX, CvFLAGY, CvFLAGStair, auxbeam = self._cdh_beams()
            CpFLAGX, CpFLAGY, CpFLAGfc, auxcol = self._cdh_columns(auxbeam)
        aux = auxcol + auxbeam
        # ...........................................................................
        # Final check for the dimensions. If column HX or HY is greater than Hmax, we have
        # to increase the concrete class (fc). The flag aux=7777 flags indicates that fc must be increased
        # and the whole design process restarted form the initial HX and HY defined in pre-design.
        # ...........................................................................
        if CpFLAGfc == 222:
            aux = 7777
            print('------------------------------------')
            # print('Maximum HX is %4.6f...' % float(np.max(self.column.HX)))
            # print('Maximum HY is %4.6f...' % float(np.max(self.column.HY)))
            # print('Minimum HX is %4.6f...' % float(np.min(self.column.HX)))
            # print('Minimum HY is %4.6f...' % float(np.min(self.column.HY)))
            print('Columns too wide! increasing fck...') # TODO: the change of strength is implemented within specific design class functions, maybe change this in later versions
            print('------------------------------------')
        elif CpFLAGfc == 333:
            aux = 5555
            print('------------------------------------')
            # print('Maximum HX is %4.6f...' % float(np.max(self.column.HX)))
            # print('Maximum HY is %4.6f...' % float(np.max(self.column.HY)))
            # print('Minimum HX is %4.6f...' % float(np.min(self.column.HX)))
            # print('Minimum HY is %4.6f...' % float(np.min(self.column.HY)))
            print('Columns too wide! Changing to Squared Columns...')
            print('------------------------------------')
        elif CpFLAGfc == 1:
            aux = 8888
        # ...........................................................................
        # Final check for the dimensions of wide beams. If column B_wide exceeds 1.00m and fsyk < 600MPa (used as a flag here), we have
        # to increase the concrete class (fc) of the steel class (fsy). The flag aux=7777 indicates that fc must be increased
        # and the whole design process restarted form the initial HX and HY defined in pre-design. If fsyk == 600MPa, 
        # we change it to Emergent beams and we restart the entire process with beams 30xHnecessary for gravity loads, 
        # and with the fck and fsyk initially considered.
        # ...........................................................................
        if np.max(self.beamX.B) > 1.00 or np.max(self.beamY.B) > 1.00:
            self.general.BeamType = 2
            aux = 7777 # TODO: Materials are not resetted here. I think we need to have another aux case where we also reset the materials?
            print('------------------------------------')
            print('Wide beams with B > 1.00m...')
            print('Changing to deep beams!')
            print('------------------------------------')

        return CvFLAGX, CvFLAGY, CvFLAGStair, CpFLAGX, CpFLAGY, aux, auxbeam

    def _force_in_beams(self):
        """
        The maximum bending moment of the alignement (max of all M1s and of all M9s) is used to assess the maximum As-.
        The maximum bending moment of the mid spans (max of all M5s) is used to compute the required As+.
        """
        SEISMIC_FACTOR = 1.00
        MX1_E = []; MStair1_E = []; MY1_E = []
        MX5_E = []; MStair5_E = []; MY5_E = []
        MX9_E = []; MStair9_E = []; MY9_E = []
        VX1_E = []; VStair1_E = []; VY1_E = []
        VX5_E = []; VStair5_E = []; VY5_E = []
        VX9_E = []; VStair9_E = []; VY9_E = []
        
        forces = ['M', 'V']
        sections = ['1', '5', '9']
        beams = ['X', 'Stair', 'Y']
        factors = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], 
                   [1, 0.3], [1, 0.3], [1, 0.3], [1, 0.3], [0.3, 1], [0.3, 1], [0.3, 1], [0.3, 1]]
        combinations = [['ULS'], ['EQ'], ['LFA+X'], ['LFA-X'], ['LFA+Y'], ['LFA-Y'], ['LFA+X'], ['LFA-X'], ['LFA+Y'], ['LFA-Y'], 
                        ['LFA+X', 'LFA+Y'], ['LFA+X', 'LFA-Y'], ['LFA-X', 'LFA-Y'], ['LFA-X', 'LFA+Y'], ['LFA+X', 'LFA+Y'], ['LFA+X', 'LFA-Y'], ['LFA-X', 'LFA+Y'], ['LFA-X', 'LFA-Y']]
        for force in forces:
            for beam in beams:
                for section in sections:
                    for values, combination in zip(factors, combinations):
                        sum = 0
                        for factor, load_case in zip(values, combination):
                            sum += self.results[load_case]['beam' + beam][force + section] * factor

                        locals()[force + beam + section + '_E'].append(sum)

        # Separate alignments
        # ...........................................................................
        self.beamX.BB = {}
        self.beamX.HH = {}
        self.beamX.LL = {}
        self.beamX.NName = {}
        self.beamX.NNodei = {}
        self.beamX.NNodej = {}
        self.beamX.Moment = {}
        self.beamX.Shear = {}
        aux = np.unique(self.beamX.index)
        for i in range(len(aux)):
            for j in range(self.general.nstoreys):
                for iicomb in range(18):
                    auxvect = self.beamX.index == aux[i]
                    if iicomb <= 5:
                        M1 = MX1_E[iicomb]
                        M5 = MX5_E[iicomb]
                        M9 = MX9_E[iicomb]
                        V1 = VX1_E[iicomb]
                        V5 = VX5_E[iicomb]
                        V9 = VX9_E[iicomb]
                    elif iicomb <= 9:
                        M1 = SEISMIC_FACTOR * MX1_E[iicomb] + MX1_E[1]
                        M5 = SEISMIC_FACTOR * MX5_E[iicomb] + MX5_E[1]
                        M9 = SEISMIC_FACTOR * MX9_E[iicomb] + MX9_E[1]
                        V1 = SEISMIC_FACTOR * VX1_E[iicomb] + VX1_E[1]
                        V5 = SEISMIC_FACTOR * VX5_E[iicomb] + VX5_E[1]
                        V9 = SEISMIC_FACTOR * VX9_E[iicomb] + VX9_E[1]
                    else:
                        M1 = MX1_E[iicomb] + MX1_E[1]
                        M5 = MX5_E[iicomb] + MX5_E[1]
                        M9 = MX9_E[iicomb] + MX9_E[1]
                        V1 = VX1_E[iicomb] + VX1_E[1]
                        V5 = VX5_E[iicomb] + VX5_E[1]
                        V9 = VX9_E[iicomb] + VX9_E[1]

                    B1 = self.beamX.B[j, auxvect]
                    B5 = self.beamX.B[j, auxvect]
                    B9 = self.beamX.B[j, auxvect]
                    H1 = self.beamX.H[j, auxvect]
                    H5 = self.beamX.H[j, auxvect]
                    H9 = self.beamX.H[j, auxvect]
                    L1 = self.beamX.L[j, auxvect]
                    L5 = self.beamX.L[j, auxvect]
                    L9 = self.beamX.L[j, auxvect]
                    nodei1 = self.beamX.elasnodei[j, auxvect] + 3000
                    nodei5 = self.beamX.elasnodei[j, auxvect] + 3000
                    nodei9 = self.beamX.elasnodei[j, auxvect] + 3000
                    nodej1 = self.beamX.elasnodej[j, auxvect] + 5000
                    nodej5 = self.beamX.elasnodej[j, auxvect] + 5000
                    nodej9 = self.beamX.elasnodej[j, auxvect] + 5000
                    name1 = self.beamX.name[j, auxvect]
                    name5 = self.beamX.name[j, auxvect] 
                    name9 = self.beamX.name[j, auxvect]
                    aa = np.array([M1[j, auxvect], M5[j, auxvect], M9[j, auxvect]]).T
                    zz = np.array([V1[j, auxvect], V5[j, auxvect], V9[j, auxvect]]).T
                    bb = np.array([B1, B5, B9]).T
                    bb = bb.flatten()
                    hh = np.array([H1, H5, H9]).T
                    hh = hh.flatten()
                    ll = np.array([L1, L5, L9]).T
                    ll = ll.flatten()
                    nn = np.array([name1, name5, name9]).T
                    nn = nn.flatten()
                    ni = np.array([nodei1, nodei5, nodei9]).T
                    ni = ni.flatten()
                    nj = np.array([nodej1, nodej5, nodej9]).T
                    nj = nj.flatten()
                    if iicomb == 0:
                        MomX = (aa.flatten()).reshape(-1, 1)
                        VomX = (np.abs(zz.flatten())).reshape(-1, 1)
                    else:
                        MomX = np.append(MomX, (aa.flatten()).reshape(-1, 1), axis=1)
                        VomX = np.append(VomX, (np.abs(zz.flatten())).reshape(-1, 1), axis=1)
                self.beamX.BB[f'{i}, {j}'] = bb.copy()
                self.beamX.HH[f'{i}, {j}'] = hh.copy()
                self.beamX.LL[f'{i}, {j}'] = ll.copy()
                self.beamX.NName[f'{i}, {j}'] = nn.copy()
                self.beamX.NNodei[f'{i}, {j}'] = ni.copy()
                self.beamX.NNodej[f'{i}, {j}'] = nj.copy()
                self.beamX.Moment[f'{i}, {j}'] = MomX.copy()
                self.beamX.Shear[f'{i}, {j}'] = VomX.copy()
        # ...........................................................................
        self.beamY.BB = {}
        self.beamY.HH = {}
        self.beamY.LL = {}
        self.beamY.NName = {}
        self.beamY.NNodei = {}
        self.beamY.NNodej = {}
        self.beamY.Moment = {}
        self.beamY.Shear = {}
        aux = np.unique(self.beamY.index)
        for i in range(len(aux)):
            for j in range(self.general.nstoreys):
                for iicomb in range(18):
                    auxvect = self.beamY.index == aux[i]
                    if iicomb <= 5:
                        M1 = MY1_E[iicomb]
                        M5 = MY5_E[iicomb]
                        M9 = MY9_E[iicomb]
                        V1 = VY1_E[iicomb]
                        V5 = VY5_E[iicomb]
                        V9 = VY9_E[iicomb]
                    elif iicomb <= 9:
                        M1 = SEISMIC_FACTOR * MY1_E[iicomb] + MY1_E[1]
                        M5 = SEISMIC_FACTOR * MY5_E[iicomb] + MY5_E[1]
                        M9 = SEISMIC_FACTOR * MY9_E[iicomb] + MY9_E[1]
                        V1 = SEISMIC_FACTOR * VY1_E[iicomb] + VY1_E[1]
                        V5 = SEISMIC_FACTOR * VY5_E[iicomb] + VY5_E[1]
                        V9 = SEISMIC_FACTOR * VY9_E[iicomb] + VY9_E[1]
                    else:
                        M1 = MY1_E[iicomb] + MY1_E[1]
                        M5 = MY5_E[iicomb] + MY5_E[1]
                        M9 = MY9_E[iicomb] + MY9_E[1]
                        V1 = VY1_E[iicomb] + VY1_E[1]
                        V5 = VY5_E[iicomb] + VY5_E[1]
                        V9 = VY9_E[iicomb] + VY9_E[1]

                    B1 = self.beamY.B[j, auxvect]
                    B5 = self.beamY.B[j, auxvect]
                    B9 = self.beamY.B[j, auxvect]
                    H1 = self.beamY.H[j, auxvect]
                    H5 = self.beamY.H[j, auxvect]
                    H9 = self.beamY.H[j, auxvect]
                    L1 = self.beamY.L[j, auxvect]
                    L5 = self.beamY.L[j, auxvect]
                    L9 = self.beamY.L[j, auxvect]
                    nodei1 = self.beamY.elasnodei[j, auxvect] + 4000
                    nodei5 = self.beamY.elasnodei[j, auxvect] + 4000
                    nodei9 = self.beamY.elasnodei[j, auxvect] + 4000
                    nodej1 = self.beamY.elasnodej[j, auxvect] + 6000
                    nodej5 = self.beamY.elasnodej[j, auxvect] + 6000
                    nodej9 = self.beamY.elasnodej[j, auxvect] + 6000
                    name1 = self.beamY.name[j, auxvect]
                    name5 = self.beamY.name[j, auxvect] 
                    name9 = self.beamY.name[j, auxvect]
                    aa = np.array([M1[j, auxvect], M5[j, auxvect], M9[j, auxvect]]).T
                    zz = np.array([V1[j, auxvect], V5[j, auxvect], V9[j, auxvect]]).T
                    bb = np.array([B1, B5, B9]).T
                    bb = bb.flatten()
                    hh = np.array([H1, H5, H9]).T
                    hh = hh.flatten()
                    ll = np.array([L1, L5, L9]).T
                    ll = ll.flatten()
                    nn = np.array([name1, name5, name9]).T
                    nn = nn.flatten()
                    ni = np.array([nodei1, nodei5, nodei9]).T
                    ni = ni.flatten()
                    nj = np.array([nodej1, nodej5, nodej9]).T
                    nj = nj.flatten()
                    if iicomb == 0:
                        MomY = (aa.flatten()).reshape(-1, 1)
                        VomY = (np.abs(zz.flatten())).reshape(-1, 1)
                    else:
                        MomY = np.append(MomY, (aa.flatten()).reshape(-1, 1), axis=1)
                        VomY = np.append(VomY, (np.abs(zz.flatten())).reshape(-1, 1), axis=1)
                self.beamY.BB[f'{i}, {j}'] = bb.copy()
                self.beamY.HH[f'{i}, {j}'] = hh.copy()
                self.beamY.LL[f'{i}, {j}'] = ll.copy()
                self.beamY.NName[f'{i}, {j}'] = nn.copy()
                self.beamY.NNodei[f'{i}, {j}'] = ni.copy()
                self.beamY.NNodej[f'{i}, {j}'] = nj.copy()
                self.beamY.Moment[f'{i}, {j}'] = MomY.copy()
                self.beamY.Shear[f'{i}, {j}'] = VomY.copy()
        # ...........................................................................
        self.beamStair.BB = {}
        self.beamStair.HH = {}
        self.beamStair.LL = {}
        self.beamStair.NName = {}
        self.beamStair.NNodei = {}
        self.beamStair.NNodej = {}
        self.beamStair.Moment = {}
        self.beamStair.Shear = {}
        for j in range(self.general.nstoreys):
            for iicomb in range(18):
                if iicomb <= 5:
                    M1 = MStair1_E[iicomb]
                    M5 = MStair5_E[iicomb]
                    M9 = MStair9_E[iicomb]
                    V1 = VStair1_E[iicomb]
                    V5 = VStair5_E[iicomb]
                    V9 = VStair9_E[iicomb]
                elif iicomb <= 9:
                    M1 = SEISMIC_FACTOR * MStair1_E[iicomb] + MStair1_E[1]
                    M5 = SEISMIC_FACTOR * MStair5_E[iicomb] + MStair5_E[1]
                    M9 = SEISMIC_FACTOR * MStair9_E[iicomb] + MStair9_E[1]
                    V1 = SEISMIC_FACTOR * VStair1_E[iicomb] + VStair1_E[1]
                    V5 = SEISMIC_FACTOR * VStair5_E[iicomb] + VStair5_E[1]
                    V9 = SEISMIC_FACTOR * VStair9_E[iicomb] + VStair9_E[1]
                else:
                    M1 = MStair1_E[iicomb] + MStair1_E[1]
                    M5 = MStair5_E[iicomb] + MStair5_E[1]
                    M9 = MStair9_E[iicomb] + MStair9_E[1]
                    V1 = VStair1_E[iicomb] + VStair1_E[1]
                    V5 = VStair5_E[iicomb] + VStair5_E[1]
                    V9 = VStair9_E[iicomb] + VStair9_E[1]

                B1 = self.beamStair.B[j]
                B5 = self.beamStair.B[j]
                B9 = self.beamStair.B[j]
                H1 = self.beamStair.H[j]
                H5 = self.beamStair.H[j]
                H9 = self.beamStair.H[j]
                L1 = self.beamStair.L[j]
                L5 = self.beamStair.L[j]
                L9 = self.beamStair.L[j]
                nodei1 = self.beamStair.elasnodei[j] + 3000
                nodei5 = self.beamStair.elasnodei[j] + 3000
                nodei9 = self.beamStair.elasnodei[j] + 3000
                nodej1 = self.beamStair.elasnodej[j] + 5000
                nodej5 = self.beamStair.elasnodej[j] + 5000
                nodej9 = self.beamStair.elasnodej[j] + 5000
                name1 = self.beamStair.name[j]
                name5 = self.beamStair.name[j] 
                name9 = self.beamStair.name[j]
                aa = np.array([M1[j], M5[j], M9[j]]).T
                zz = np.array([V1[j], V5[j], V9[j]]).T
                bb = np.array([B1, B5, B9]).T
                bb = bb.flatten()
                hh = np.array([H1, H5, H9]).T
                hh = hh.flatten()
                ll = np.array([L1, L5, L9]).T
                ll = ll.flatten()
                nn = np.array([name1, name5, name9]).T
                nn = nn.flatten()
                ni = np.array([nodei1, nodei5, nodei9]).T
                ni = ni.flatten()
                nj = np.array([nodej1, nodej5, nodej9]).T
                nj = nj.flatten()
                if iicomb == 0:
                    MomStair = (aa.flatten()).reshape(-1, 1)
                    VomStair = (np.abs(zz.flatten())).reshape(-1, 1)
                else:
                    MomStair = np.append(MomStair, (aa.flatten()).reshape(-1, 1), axis=1)
                    VomStair = np.append(VomStair, (np.abs(zz.flatten())).reshape(-1, 1), axis=1)
            self.beamStair.BB[f'{j}'] = bb.copy()
            self.beamStair.HH[f'{j}'] = hh.copy()
            self.beamStair.LL[f'{j}'] = ll.copy()
            self.beamStair.NName[f'{j}'] = nn.copy()
            self.beamStair.NNodei[f'{j}'] = ni.copy()
            self.beamStair.NNodej[f'{j}'] = nj.copy()
            self.beamStair.Moment[f'{j}'] = MomStair.copy()
            self.beamStair.Shear[f'{j}'] = VomStair.copy()
        # ...........................................................................
        DCL_combs = [0, 1, 2, 3, 4, 5]
        DCM_combs = [0, 1, 6, 7, 8, 9]
        DCH_combs = [0, 1, 10, 11, 12, 13, 14, 15, 16, 17]
        # ...........................................................................
        self.beamX.MomentEnvelopePlusCDH = {}
        self.beamX.MomentEnvelopeNegCDH = {}
        self.beamX.MomentEnvelopePlusCDM = {}
        self.beamX.MomentEnvelopeNegCDM = {}
        self.beamX.MomentEnvelopePlusCDL = {}
        self.beamX.MomentEnvelopeNegCDL = {}
        self.beamX.MomentEnvelopePlusCDN = {}
        self.beamX.MomentEnvelopeNegCDN = {}
        self.beamX.ShearEnvelopeCDH = {}
        self.beamX.ShearEnvelopeCDM = {}
        self.beamX.ShearEnvelopeCDL = {}
        self.beamX.ShearEnvelopeCDN = {}
        aux = np.unique(self.beamX.index)
        for i in range(len(aux)):
            for j in range(self.general.nstoreys):
                mommX = self.beamX.Moment[f'{i}, {j}'].copy()
                vommX = self.beamX.Shear[f'{i}, {j}'].copy()
                self.beamX.MomentEnvelopePlusCDH[f'{i}, {j}'] = np.max(mommX[:, DCH_combs], axis=1)
                self.beamX.MomentEnvelopeNegCDH[f'{i}, {j}'] = np.min(mommX[:, DCH_combs], axis=1)
                self.beamX.MomentEnvelopePlusCDM[f'{i}, {j}'] = np.max(mommX[:, DCM_combs], axis=1)
                self.beamX.MomentEnvelopeNegCDM[f'{i}, {j}'] = np.min(mommX[:, DCM_combs], axis=1)
                self.beamX.MomentEnvelopePlusCDL[f'{i}, {j}'] = np.max(mommX[:, DCL_combs], axis=1)
                self.beamX.MomentEnvelopeNegCDL[f'{i}, {j}'] = np.min(mommX[:, DCL_combs], axis=1)
                self.beamX.MomentEnvelopePlusCDN[f'{i}, {j}'] = mommX[:, 0] + 0
                self.beamX.MomentEnvelopeNegCDN[f'{i}, {j}'] = mommX[:, 0] + 0
                self.beamX.ShearEnvelopeCDH[f'{i}, {j}'] = np.max(vommX[:, DCH_combs], axis=1)
                self.beamX.ShearEnvelopeCDM[f'{i}, {j}'] = np.max(vommX[:, DCM_combs], axis=1)
                self.beamX.ShearEnvelopeCDL[f'{i}, {j}'] = np.max(vommX[:, DCL_combs], axis=1)
                self.beamX.ShearEnvelopeCDN[f'{i}, {j}'] = vommX[:, 0] + 0
        # ...........................................................................
        self.beamY.MomentEnvelopePlusCDH = {}
        self.beamY.MomentEnvelopeNegCDH = {}
        self.beamY.MomentEnvelopePlusCDM = {}
        self.beamY.MomentEnvelopeNegCDM = {}
        self.beamY.MomentEnvelopePlusCDL = {}
        self.beamY.MomentEnvelopeNegCDL = {}
        self.beamY.MomentEnvelopePlusCDN = {}
        self.beamY.MomentEnvelopeNegCDN = {}
        self.beamY.ShearEnvelopeCDH = {}
        self.beamY.ShearEnvelopeCDM = {}
        self.beamY.ShearEnvelopeCDL = {}
        self.beamY.ShearEnvelopeCDN = {}
        aux = np.unique(self.beamY.index)
        for i in range(len(aux)):
            for j in range(self.general.nstoreys):
                mommY = self.beamY.Moment[f'{i}, {j}'].copy()
                vommY = self.beamY.Shear[f'{i}, {j}'].copy()
                self.beamY.MomentEnvelopePlusCDH[f'{i}, {j}'] = np.max(mommY[:, DCH_combs], axis=1)
                self.beamY.MomentEnvelopeNegCDH[f'{i}, {j}'] = np.min(mommY[:, DCH_combs], axis=1)
                self.beamY.MomentEnvelopePlusCDM[f'{i}, {j}'] = np.max(mommY[:, DCM_combs], axis=1)
                self.beamY.MomentEnvelopeNegCDM[f'{i}, {j}'] = np.min(mommY[:, DCM_combs], axis=1)
                self.beamY.MomentEnvelopePlusCDL[f'{i}, {j}'] = np.max(mommY[:, DCL_combs], axis=1)
                self.beamY.MomentEnvelopeNegCDL[f'{i}, {j}'] = np.min(mommY[:, DCL_combs], axis=1)
                self.beamY.MomentEnvelopePlusCDN[f'{i}, {j}'] = mommY[:, 0] + 0
                self.beamY.MomentEnvelopeNegCDN[f'{i}, {j}'] = mommY[:, 0] + 0
                self.beamY.ShearEnvelopeCDH[f'{i}, {j}'] = np.max(vommY[:, DCH_combs], axis=1)
                self.beamY.ShearEnvelopeCDM[f'{i}, {j}'] = np.max(vommY[:, DCM_combs], axis=1)
                self.beamY.ShearEnvelopeCDL[f'{i}, {j}'] = np.max(vommY[:, DCL_combs], axis=1)
                self.beamY.ShearEnvelopeCDN[f'{i}, {j}'] = vommY[:, 0] + 0
        # ...........................................................................
        self.beamStair.MomentEnvelopePlusCDH = {}
        self.beamStair.MomentEnvelopeNegCDH = {}
        self.beamStair.MomentEnvelopePlusCDM = {}
        self.beamStair.MomentEnvelopeNegCDM = {}
        self.beamStair.MomentEnvelopePlusCDL = {}
        self.beamStair.MomentEnvelopeNegCDL = {}
        self.beamStair.MomentEnvelopePlusCDN = {}
        self.beamStair.MomentEnvelopeNegCDN = {}
        self.beamStair.ShearEnvelopeCDH = {}
        self.beamStair.ShearEnvelopeCDM = {}
        self.beamStair.ShearEnvelopeCDL = {}
        self.beamStair.ShearEnvelopeCDN = {}
        for j in range(self.general.nstoreys):
            self.beamStair.MomentEnvelopePlusCDH[f'{j}'] = np.max(MomStair[:, DCH_combs], axis=1)
            self.beamStair.MomentEnvelopeNegCDH[f'{j}'] = np.min(MomStair[:, DCH_combs], axis=1)
            self.beamStair.MomentEnvelopePlusCDM[f'{j}'] = np.max(MomStair[:, DCM_combs], axis=1)
            self.beamStair.MomentEnvelopeNegCDM[f'{j}'] = np.min(MomStair[:, DCM_combs], axis=1)
            self.beamStair.MomentEnvelopePlusCDL[f'{j}'] = np.max(MomStair[:, DCL_combs], axis=1)
            self.beamStair.MomentEnvelopeNegCDL[f'{j}'] = np.min(MomStair[:, DCL_combs], axis=1)
            self.beamStair.MomentEnvelopePlusCDN[f'{j}'] = MomStair[:, 0] + 0
            self.beamStair.MomentEnvelopeNegCDN[f'{j}'] = MomStair[:, 0] + 0
            self.beamStair.ShearEnvelopeCDH[f'{j}'] = np.max(VomStair[:, DCH_combs], axis=1)
            self.beamStair.ShearEnvelopeCDM[f'{j}'] = np.max(VomStair[:, DCM_combs], axis=1)
            self.beamStair.ShearEnvelopeCDL[f'{j}'] = np.max(VomStair[:, DCL_combs], axis=1)
            self.beamStair.ShearEnvelopeCDN[f'{j}'] = VomStair[:, 0] + 0
    
    def _force_in_columns(self):
        """
        The maximum bending moment of the alignement (max of all M1s and of all M9s) is used to assess the maximum As-.
        The maximum bending moment of the mid spans (max of all M5s) is used to compute the required As+.
        The corresponding solution in terms of rebars is calculated for As- ans As+ usign the same diameter.
        Calculate the rebar solution and exports the key elements for the nonlinear modelling
        """
        # ..............................................................................................................
        self.column.MrdX_columns = np.zeros((self.general.nstoreys, self.column.name.shape[1]))
        aaax = np.unique(self.beamX.index)
        for j in range(self.general.nstoreys):
            aux1 = np.array([])
            for i in range(len(aaax)):
                auxa = self.beamX.MomentEnvelopeNegCDH[f"{i}, {j}"]
                auxb = self.beamX.MomentEnvelopePlusCDH[f"{i}, {j}"]
                auxa = np.delete(auxa, slice(1, len(auxa), 3))
                auxb = np.delete(auxb, slice(1, len(auxb), 3))
                for t in range(1, len(auxa)-1, 2):
                    auxa[t] = max(auxa[t], auxa[t+1])
                    auxa[t+1] = auxa[t]
                    auxb[t] = max(auxb[t], auxb[t+1])
                    auxb[t+1] = auxb[t]
                auxa = np.delete(auxa, slice(2, len(auxa), 2))
                auxb = np.delete(auxb, slice(2, len(auxb), 2))
                aux = np.abs(auxa) + np.abs(auxb)
                aux[0] = abs(auxa[0])
                aux[-1] = abs(auxa[-1])
                aux1 = np.append(aux1, 1.30 * aux)
            
            self.column.MrdX_columns[j, self.column.name[0, :] < 200] = np.abs(aux1)

        # TODO: it looks like these stuff are not used
        MrdX_PLUS_columns = np.zeros((self.general.nstoreys, self.column.name.shape[1]))
        for j in range(self.general.nstoreys):
            auxS = self.beamStair.MomentEnvelopeNegCDH[f"{j}"]
            auxS = np.delete(auxS, 1)
            MrdX_PLUS_columns[j, self.column.name[0, :] > 200] = np.abs(auxS)

        MRD1_y = np.append(np.zeros((1, self.column.MrdX_columns.shape[1])), 0.50 * self.column.MrdX_columns[0:-1, :], axis=0)
        MRD9_y = 0.50 * self.column.MrdX_columns

        # ..............................................................................................................
        self.column.MrdY_columns = np.zeros((self.general.nstoreys, self.column.name.shape[1]))
        aaay = np.unique(self.beamY.index)
        for j in range(self.general.nstoreys):
            aux1 = np.array([])
            for i in range(len(aaay)):
                auxa = self.beamY.MomentEnvelopeNegCDH[f"{i}, {j}"]
                auxb = self.beamY.MomentEnvelopePlusCDH[f"{i}, {j}"]
                auxa = np.delete(auxa, slice(1, len(auxa), 3))
                auxb = np.delete(auxb, slice(1, len(auxb), 3))
                for t in range(1, len(auxa)-1, 2):
                    auxa[t] = max(auxa[t], auxa[t+1])
                    auxa[t+1] = auxa[t]
                    auxb[t] = max(auxb[t], auxb[t+1])
                    auxb[t+1] = auxb[t]
                auxa = np.delete(auxa, slice(2, len(auxa), 2))
                auxb = np.delete(auxb, slice(2, len(auxb), 2))
                aux = np.abs(auxa) + np.abs(auxb)
                aux[0] = abs(auxa[0])
                aux[-1] = abs(auxa[-1])
                aux1 = np.append(aux1, 1.30 * aux)
            
            self.column.MrdY_columns[j, self.column.name[0, :] < 200] = np.abs(aux1)

        # TODO: it looks like these stuff are not used
        MRD1_z = np.append(np.zeros((1, self.column.MrdY_columns.shape[1])), 0.50 * self.column.MrdY_columns[0:-1, :], axis=0)
        MRD9_z = 0.50 * self.column.MrdY_columns

        # LOAD COMBINATIONS
        # CDN and CDL use only first 6 and lateral load analysis is carried out including quasi-static loads
        N1_E = []; N9_E = []
        Mz1_E = []; Mz9_E = []
        My1_E = []; My9_E = []
        Vz1_E = []; Vz9_E = []
        Vy1_E = []; Vy9_E = []

        forces = ['N', 'Mz', 'My', 'Vz', 'Vy']
        sections = ['1', '9']
        factors = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], 
                   [1, 0.3], [1, 0.3], [1, 0.3], [1, 0.3], [0.3, 1], [0.3, 1], [0.3, 1], [0.3, 1]]
        combinations = [['ULS'], ['EQ'], ['LFA+X'], ['LFA-X'], ['LFA+Y'], ['LFA-Y'], ['LFA+X'], ['LFA-X'], ['LFA+Y'], ['LFA-Y'], 
                        ['LFA+X', 'LFA+Y'], ['LFA+X', 'LFA-Y'], ['LFA-X', 'LFA-Y'], ['LFA-X', 'LFA+Y'], ['LFA+X', 'LFA+Y'], ['LFA+X', 'LFA-Y'], ['LFA-X', 'LFA+Y'], ['LFA-X', 'LFA-Y']]
        for force in forces:
            for section in sections:
                for values, combination in zip(factors, combinations):
                    sum = 0
                    for factor, load_case in zip(values, combination):
                        sum += self.results[load_case]['Column'][force + section] * factor
                    locals()[force + section + '_E'].append(sum)

        # Separate alignments
        # ...........................................................................
        SEISMIC_FACTOR = 1.0
        self.column.N1 = []
        self.column.M1_y = []
        self.column.M1_z = []
        self.column.N9 = []
        self.column.M9_y = []
        self.column.M9_z = []
        self.column.V1_x = [] # it has been changed to vy instead of vz to be consistent (HMA)
        self.column.V1_y = []
        self.column.V9_x = [] # it has been changed to vy instead of vz to be consistent (HMA)
        self.column.V9_y = []
        for iicomb in range(18):
            if iicomb <= 5:
                self.column.N1.append(N1_E[iicomb])
                self.column.M1_z.append(Mz1_E[iicomb])
                self.column.M1_y.append(My1_E[iicomb])
                self.column.V1_x.append(Vz1_E[iicomb])
                self.column.V1_y.append(Vy1_E[iicomb])
                self.column.N9.append(N9_E[iicomb])
                self.column.M9_z.append(Mz9_E[iicomb])
                self.column.M9_y.append(My9_E[iicomb])
                self.column.V9_x.append(Vz9_E[iicomb])
                self.column.V9_y.append(Vy9_E[iicomb])

            elif iicomb <= 9:
                self.column.N1.append(SEISMIC_FACTOR * N1_E[iicomb] + N1_E[1])
                self.column.M1_z.append(SEISMIC_FACTOR * Mz1_E[iicomb] + Mz1_E[1])
                self.column.M1_y.append(SEISMIC_FACTOR * My1_E[iicomb] + My1_E[1])
                self.column.V1_x.append(SEISMIC_FACTOR * Vz1_E[iicomb] + Vz1_E[1])
                self.column.V1_y.append(SEISMIC_FACTOR * Vy1_E[iicomb] + Vy1_E[1])
                self.column.N9.append(SEISMIC_FACTOR * N9_E[iicomb] + N9_E[1])
                self.column.M9_z.append(SEISMIC_FACTOR * Mz9_E[iicomb] + Mz9_E[1])
                self.column.M9_y.append(SEISMIC_FACTOR * My9_E[iicomb] + My9_E[1])
                self.column.V9_x.append(SEISMIC_FACTOR * Vz9_E[iicomb] + Vz9_E[1])
                self.column.V9_y.append(SEISMIC_FACTOR * Vy9_E[iicomb] + Vy9_E[1])
            else:
                self.column.N1.append(N1_E[iicomb] + N1_E[1])
                self.column.M1_z.append(Mz1_E[iicomb] + Mz1_E[1])
                self.column.M1_y.append(My1_E[iicomb] + My1_E[1])
                self.column.V1_x.append(Vz1_E[iicomb] + Vz1_E[1])
                self.column.V1_y.append(Vy1_E[iicomb] + Vy1_E[1])
                self.column.N9.append(N9_E[iicomb] + N9_E[1])
                self.column.M9_z.append(Mz9_E[iicomb] + Mz9_E[1])
                self.column.M9_y.append(My9_E[iicomb] + My9_E[1])
                self.column.V9_x.append(Vz9_E[iicomb] + Vz9_E[1])
                self.column.V9_y.append(Vy9_E[iicomb] + Vy9_E[1])
        # ...........................................................................
        self.column.Niu1 = []
        self.column.MuX1 = []
        self.column.MuY1 = []
        self.column.Niu9 = []
        self.column.MuX9 = []
        self.column.MuY9 = []
        self.column.tauX1 = []
        self.column.tauY1 = []
        self.column.tauX9 = []
        self.column.tauY9 = []
        self.column.eccX1 = []
        self.column.eccX9 = []
        self.column.eccY1 = []
        self.column.eccY9 = []
        for icomb in range(18):
            if icomb == 0 or icomb == 1: # Changed this to include also icomb 1 (another gravity load case)
                self.column.Niu1.append( self.column.N1[icomb] / (self.column.HY * self.column.HX * self.general.fcd * 1000) )
                self.column.Niu9.append( self.column.N9[icomb] / (self.column.HX * self.column.HY * self.general.fcd * 1000) )
                self.column.MuX1.append( np.abs(self.column.M1_y[icomb]) / (self.column.HY * (self.column.HX ** 2) * self.general.fcd * 1000) )
                self.column.MuY1.append( np.abs(self.column.M1_z[icomb]) / (self.column.HX * (self.column.HY ** 2) * self.general.fcd * 1000) )
                self.column.MuX9.append( np.abs(self.column.M9_y[icomb]) / (self.column.HY * (self.column.HX ** 2) * self.general.fcd * 1000) )
                self.column.MuY9.append( np.abs(self.column.M9_z[icomb]) / (self.column.HX * (self.column.HY ** 2) * self.general.fcd * 1000) )
                
                self.column.tauX1.append( np.abs(self.column.V1_x[icomb]) / (self.column.HY * 0.90 * self.column.HX) )
                self.column.tauY1.append( np.abs(self.column.V1_y[icomb]) / (self.column.HX * 0.90 * self.column.HY) )
                self.column.tauX9.append( np.abs(self.column.V9_x[icomb]) / (self.column.HY * 0.90 * self.column.HX) )
                self.column.tauY9.append( np.abs(self.column.V9_y[icomb]) / (self.column.HX * 0.90 * self.column.HY) )

                self.column.eccX1.append( self.column.M1_y[icomb] / self.column.N1[icomb] )
                self.column.eccX9.append( self.column.M9_y[icomb] / self.column.N9[icomb] )
                self.column.eccY1.append( self.column.M1_z[icomb] / self.column.N1[icomb] )
                self.column.eccY9.append( self.column.M9_z[icomb] / self.column.N9[icomb] )
            else:
                self.column.Niu1.append( self.column.N1[icomb] / (self.column.HY * self.column.HX * self.general.fcdEQ * 1000) )
                self.column.Niu9.append( self.column.N9[icomb] / (self.column.HX * self.column.HY * self.general.fcdEQ * 1000) )
                self.column.MuX1.append( np.abs(self.column.M1_y[icomb]) / (self.column.HY * (self.column.HX ** 2) * self.general.fcdEQ * 1000) )
                self.column.MuY1.append( np.abs(self.column.M1_z[icomb]) / (self.column.HX * (self.column.HY ** 2) * self.general.fcdEQ * 1000) )
                self.column.MuX9.append( np.abs(self.column.M9_y[icomb]) / (self.column.HY * (self.column.HX ** 2) * self.general.fcdEQ * 1000) )
                self.column.MuY9.append( np.abs(self.column.M9_z[icomb]) / (self.column.HX * (self.column.HY ** 2) * self.general.fcdEQ * 1000) )
                
                self.column.tauX1.append( np.abs(self.column.V1_x[icomb]) / (self.column.HY * 0.90 * self.column.HX) )
                self.column.tauY1.append( np.abs(self.column.V1_y[icomb]) / (self.column.HX * 0.90 * self.column.HY) )
                self.column.tauX9.append( np.abs(self.column.V9_x[icomb]) / (self.column.HY * 0.90 * self.column.HX) )
                self.column.tauY9.append( np.abs(self.column.V9_y[icomb]) / (self.column.HX * 0.90 * self.column.HY) )

                self.column.eccX1.append( self.column.M1_y[icomb] / self.column.N1[icomb] )
                self.column.eccX9.append( self.column.M9_y[icomb] / self.column.N9[icomb] )
                self.column.eccY1.append( self.column.M1_z[icomb] / self.column.N1[icomb] )
                self.column.eccY9.append( self.column.M9_z[icomb] / self.column.N9[icomb] )

    def _cdn_beams(self):
        """
        Design methodology for beams considering the case of DCL1 (REBAP83_PT) design.
        The beams are separated into different alignments and a single section is used. 
        1) The maximum bending moment of the alignement (max of all M1s and of all M9s) is used to assess the maximum As-.
        2) The maximum bending moment of the mid spans (max of all M5s) is used to compute the required As+.
        3) The corresponding solution in terms of rebars is calculated for As- ans As+ using the same diameter.
        4) Calculate the rebar solution and exports the key elements for the nonlinear modelling
        """
        # ...........................................................................
        # Variables for the design based on the DCL1 Design Routines
        # ...........................................................................
        tau1 = 0.40  # Allowable shear stress carried by concrete or design shear strength of concrete
        taumax = 1.40  # Allowable shear stress carried by the beams
        sigmac = self.general.fcd + 0  # Design steel yield strength
        sigmas = self.general.fsyd + 0  # Design concrete compressive strength
        n = 15  # Modular ratio
        top_to_bot_ratio = 0.50 # Top to bottom reinforcement ratio
        dmax_between_long_bars = 0.10 # Maximum distance between longitudinal bars
        sw_min_over_fi = 12  # Minimum stirrup spacing to longitudinal rebar diameter ratio
        cover = 0.03  # Concrete cover 
        epscU = 3.5 / 1000  # Concrete crushing strain used to compute section capacity
        esy = self.general.fsyk / 200000  # Steel yield strain used to compute section capacity
        if self.general.fck < 27.6:  # Stress-block coefficient used to compute section capacity
            betafc = 0.85
        elif self.general.fck > 55.17:
            betafc = 0.65
        else:
            betafc = 1.05 - 0.05 * self.general.fck / 6.9
        rhomin_tens = 0.00 # This parameter is not being used 
        dmin = 0.04 # Minimum distance between longitudinal bars
        # ...........................................................................
        # Verifies the adequacy of the sectional dimensions
        # ...........................................................................
        alignmentsX = np.unique(self.beamX.index)
        CvFLAGX = np.zeros((self.general.nstoreys, self.beamX.index.shape[0]))
        for i in range(len(alignmentsX)):
            mask = self.beamX.index == alignmentsX[i]
            for j in range(self.general.nstoreys):
                BB = self.beamX.BB[f'{i}, {j}'].copy()
                HH = self.beamX.HH[f'{i}, {j}'].copy()
                maximum_shear = self.beamX.ShearEnvelopeCDN[f'{i}, {j}'].copy()
                tauX = np.abs(maximum_shear) / (BB * (0.81 * HH) * 1000)
                if max(tauX) > taumax:
                    CvFLAGX[j, mask] = 1 # not satisfied
                else:
                    CvFLAGX[j, mask] = 0 # satisfied
        # ...........................................................................
        alignmentsY = np.unique(self.beamY.index)
        CvFLAGY = np.zeros((self.general.nstoreys, self.beamY.index.shape[0]))
        for i in range(len(alignmentsY)):
            mask = self.beamY.index == alignmentsY[i]
            for j in range(self.general.nstoreys):
                BB = self.beamY.BB[f'{i}, {j}'].copy()
                HH = self.beamY.HH[f'{i}, {j}'].copy()
                maximum_shear = self.beamY.ShearEnvelopeCDN[f'{i}, {j}'].copy()
                tauY = np.abs(maximum_shear) / (BB * (0.81 * HH) * 1000)
                if max(tauY) > taumax:
                    CvFLAGY[j, mask] = 1 # not satisfied
                else:
                    CvFLAGY[j, mask] = 0 # satisfied
        # ...........................................................................
        CvFLAGStair = np.zeros(self.general.nstoreys)
        for j in range(self.general.nstoreys):
            BB = self.beamStair.BB[f'{j}'].copy()
            HH = self.beamStair.HH[f'{j}'].copy()
            maximum_shear = self.beamStair.ShearEnvelopeCDN[f'{j}'].copy()
            tauStair = np.abs(maximum_shear) / (BB * (0.81 * HH) * 1000)
            if max(tauStair) > taumax:
                CvFLAGStair[j] = 1 # not satisfied
            else:
                CvFLAGStair[j] = 0 # satisfied                    
        # ...........................................................................
        # Verifies the need for a new section
        # ...........................................................................
        auxbeam = np.sum(CvFLAGX) + np.sum(CvFLAGY) + np.sum(CvFLAGStair)
        if auxbeam > 0.99:
            print(f"Beams Not OK ... still {auxbeam:.0f} to change")
        else:
            print("Beams stage 1 complete")
            # ...........................................................................
            # When ok, selects the longitudinal steel rebar solution and the tranverse steel rebar solution
            # ...........................................................................
            # BeamX
            NeededAsTOPX = {}
            NeededAsBOTX = {}
            NeededAsw_sX = {}
            swmax_X = {}
            self.beamX.NeededAsTOP = {}
            self.beamX.NeededAsBOT = {}
            self.beamX.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                for i in range(len(alignmentsX)):
                    BB = self.beamX.BB[f'{i}, {j}'].copy()
                    HH = self.beamX.HH[f'{i}, {j}'].copy()
                    moment_plus = self.beamX.MomentEnvelopePlusCDN[f'{i}, {j}'].copy()
                    moment_neg = self.beamX.MomentEnvelopeNegCDN[f'{i}, {j}'].copy()
                    maximum_shear = np.abs(self.beamX.ShearEnvelopeCDN[f'{i}, {j}'])
                    moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                    moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                    moment_plus = np.abs(moment_plus)
                    moment_neg = np.abs(moment_neg)
                    # Calculates the balanced moment capacity
                    xbal = (sigmac * 0.90 * HH) / (sigmac + sigmas / n)
                    Cbal = 0.50 * sigmac * 1000 * BB * xbal
                    Mbal = Cbal * (0.90 * HH - 0.3333 * xbal)
                    # Calculate longitudinal steel area
                    AsTOPX = np.zeros(moment_plus.shape)  # Required steel area at top
                    AsBOTX = np.zeros(moment_plus.shape)  # Required steel area at bottom
                    # For envelope of positive moments (+)
                    mask1 = moment_plus <= Mbal # Mask for identifying singly reinforced beams
                    Mexcess = moment_plus[~mask1] - Mbal[~mask1] # Excessive moment (doubly reinforced beam case)
                    AsTOPX[mask1] = moment_plus[mask1] / (1000 * sigmas * (0.9 * HH[mask1] - xbal[mask1] / 3)) # Tension reinforcement (singly reinforced beam)
                    As1 = moment_plus[~mask1] / (1000 * sigmas * (0.9 * HH[~mask1] - xbal[~mask1] / 3)) # As1 (Doubly reinforced beam)
                    As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # As2 (doubly reinforced beam) --> Corrected
                    AsTOPX[~mask1] = As1 + As2 # Total tension reinforcement reinforcement (doubly reinforced beam)
                    sigmas_line = (2 * 1000 * sigmas * (xbal[~mask1] - 0.10 * HH[~mask1])) / (0.90 * HH[~mask1] - xbal[~mask1]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                    AsBOTX[~mask1] = (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # Compression reinforcement (doubly reinforced beam)
                    # For envelope of negative moments (-)
                    mask2 = moment_neg <= Mbal # Mask for identifying singly reinforced beams
                    Mexcess = moment_neg[~mask2] - Mbal[~mask2] # Excessive moment (doubly reinforced beam case)
                    AsBOTX[mask2] = np.maximum(AsBOTX[mask2], moment_neg[mask2] / (1000 * sigmas * (0.9 * HH[mask2] - xbal[mask2] / 3))) # Tension reinforcement (singly reinforced beam)
                    As1 = moment_neg[~mask2] / (1000 * sigmas * (0.9 * HH[~mask2] - xbal[~mask2] / 3)) # As1 (doubly reinforced beam)
                    As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask2] - 0.10*HH[~mask2])) # As2 (doubly reinforced beam) --> Corrected
                    AsBOTX[~mask2] = np.maximum(As1 + As2, AsBOTX[~mask2]) # Total tension reinforcement reinforcement (doubly reinforced beam)
                    sigmas_line = (2 * 1000 * sigmas * (xbal[~mask2] - 0.10 * HH[~mask2])) / (0.90 * HH[~mask2] - xbal[~mask2]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                    AsTOPX[~mask2] = np.maximum( (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask2] - 0.10*HH[~mask2])), AsTOPX[~mask2]) # Compression reinforcement (doubly reinforced beam)
                    # Save required longitudinal steel area
                    NeededAsTOPX[f'{i}, {j}'] = AsTOPX.copy()
                    NeededAsBOTX[f'{i}, {j}'] = AsBOTX.copy()
                    self.beamX.NeededAsTOP[f'{i}, {j}'] = AsTOPX.copy()
                    self.beamX.NeededAsBOT[f'{i}, {j}'] = AsBOTX.copy()
                    # ...........................................................................
                    Vrd = 1000 * tau1 * BB * 0.81 * HH
                    mask = maximum_shear > Vrd
                    Asw_sX = np.maximum(maximum_shear / (0.9 * 1000 * sigmas * HH), 1.1310e-04)
                    Asw_sX[~mask] = 1.1310e-04
                    NeededAsw_sX[f'{i}, {j}'] = Asw_sX.copy()
                    swmax_X[f'{i}, {j}'] = np.minimum(HH, 0.20)
                    self.beamX.NeededAsw_s[f'{i}, {j}'] = Asw_sX.copy()
            # ...........................................................................
            # BeamY
            NeededAsTOPY = {}
            NeededAsBOTY = {}
            NeededAsw_sY = {}
            swmax_Y = {}
            self.beamY.NeededAsTOP = {}
            self.beamY.NeededAsBOT = {}
            self.beamY.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                for i in range(len(alignmentsY)):
                    BB = self.beamY.BB[f'{i}, {j}'].copy()
                    HH = self.beamY.HH[f'{i}, {j}'].copy()
                    moment_plus = self.beamY.MomentEnvelopePlusCDN[f'{i}, {j}'].copy()
                    moment_neg = self.beamY.MomentEnvelopeNegCDN[f'{i}, {j}'].copy()
                    maximum_shear = np.abs(self.beamY.ShearEnvelopeCDN[f'{i}, {j}'])
                    moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                    moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                    moment_plus = np.abs(moment_plus)
                    moment_neg = np.abs(moment_neg)
                    # Calculates the balanced moment capacity
                    xbal = (sigmac * 0.90 * HH) / (sigmac + sigmas / n)
                    Cbal = 0.50 * sigmac * 1000 * BB * xbal
                    Mbal = Cbal * (0.90 * HH - 0.3333 * xbal)
                    # Calculate longitudinal steel area
                    AsTOPY = np.zeros(moment_plus.shape)  # Required steel area at top
                    AsBOTY = np.zeros(moment_plus.shape)  # Required steel area at bottom
                    # For envelope of positive moments (+)
                    mask1 = moment_plus <= Mbal # Mask for identifying singly reinforced beams
                    Mexcess = moment_plus[~mask1] - Mbal[~mask1] # Excessive moment (doubly reinforced beam case)
                    AsTOPY[mask1] = moment_plus[mask1] / (1000 * sigmas * (0.9 * HH[mask1] - xbal[mask1] / 3)) # Tension reinforcement (singly reinforced beam)
                    As1 = moment_plus[~mask1] / (1000 * sigmas * (0.9 * HH[~mask1] - xbal[~mask1] / 3)) # As1 (Doubly reinforced beam)
                    As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # As2 (doubly reinforced beam) --> Corrected
                    AsTOPY[~mask1] = As1 + As2 # Total tension reinforcement reinforcement (doubly reinforced beam)
                    sigmas_line = (2 * 1000 * sigmas * (xbal[~mask1] - 0.10 * HH[~mask1])) / (0.90 * HH[~mask1] - xbal[~mask1]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                    AsBOTY[~mask1] = (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # Compression reinforcement (doubly reinforced beam)
                    # For envelope of negative moments (-)
                    mask2 = moment_neg <= Mbal # Mask for identifying singly reinforced beams
                    Mexcess = moment_neg[~mask2] - Mbal[~mask2] # Excessive moment (doubly reinforced beam case)
                    AsBOTY[mask2] = np.maximum(AsBOTY[mask2], moment_neg[mask2] / (1000 * sigmas * (0.9 * HH[mask2] - xbal[mask2] / 3))) # Tension reinforcement (singly reinforced beam)
                    As1 = moment_neg[~mask2] / (1000 * sigmas * (0.9 * HH[~mask2] - xbal[~mask2] / 3)) # As1 (doubly reinforced beam)
                    As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask2] - 0.10*HH[~mask2])) # As2 (doubly reinforced beam) --> Corrected
                    AsBOTY[~mask2] = np.maximum(As1 + As2, AsBOTY[~mask2]) # Total tension reinforcement reinforcement (doubly reinforced beam)
                    sigmas_line = (2 * 1000 * sigmas * (xbal[~mask2] - 0.10 * HH[~mask2])) / (0.90 * HH[~mask2] - xbal[~mask2]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                    AsTOPY[~mask2] = np.maximum( (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask2] - 0.10*HH[~mask2])), AsTOPY[~mask2]) # Compression reinforcement (doubly reinforced beam)
                    # Save required longitudinal steel area
                    NeededAsTOPY[f'{i}, {j}'] = AsTOPY.copy()
                    NeededAsBOTY[f'{i}, {j}'] = AsBOTY.copy()
                    self.beamY.NeededAsTOP[f'{i}, {j}'] = AsTOPY.copy()
                    self.beamY.NeededAsBOT[f'{i}, {j}'] = AsBOTY.copy()
                    # ...........................................................................
                    Vrd = 1000 * tau1 * BB * 0.81 * HH
                    mask = maximum_shear > Vrd
                    Asw_sY = np.maximum(maximum_shear / (0.9 * 1000 * sigmas * HH), 1.1310e-04)
                    Asw_sY[~mask] = 1.1310e-04
                    NeededAsw_sY[f'{i}, {j}'] = Asw_sY.copy()
                    swmax_Y[f'{i}, {j}'] = np.minimum(HH, 0.20)
                    self.beamY.NeededAsw_s[f'{i}, {j}'] = Asw_sY.copy()
            # ...........................................................................
            # BeamStair
            NeededAsTOPStair = {}
            NeededAsBOTStair = {}
            NeededAsw_sStair = {}
            swmax_Stair = {}
            self.beamStair.NeededAsTOP = {}
            self.beamStair.NeededAsBOT = {}
            self.beamStair.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                BB = self.beamStair.BB[f'{j}'].copy()
                HH = self.beamStair.HH[f'{j}'].copy()
                moment_plus = self.beamStair.MomentEnvelopePlusCDN[f'{j}'].copy()
                moment_neg = self.beamStair.MomentEnvelopeNegCDN[f'{j}'].copy()
                maximum_shear = np.abs(self.beamStair.ShearEnvelopeCDN[f'{j}'])
                moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                moment_plus = np.abs(moment_plus)
                moment_neg = np.abs(moment_neg)
                # Calculates the balanced moment capacity
                xbal = (sigmac * 0.90 * HH) / (sigmac + sigmas / n)
                Cbal = 0.50 * sigmac * 1000 * BB * xbal
                Mbal = Cbal * (0.90 * HH - 0.3333 * xbal)
                # Calculate longitudinal steel area
                AsTOPStair = np.zeros(moment_plus.shape)  # Required steel area at top
                AsBOTStair = np.zeros(moment_plus.shape)  # Required steel area at bottom
                # For envelope of positive moments (+)
                mask1 = moment_plus <= Mbal # Mask for identifying singly reinforced beams
                Mexcess = moment_plus[~mask1] - Mbal[~mask1] # Excessive moment (doubly reinforced beam case)
                AsTOPStair[mask1] = moment_plus[mask1] / (1000 * sigmas * (0.9 * HH[mask1] - xbal[mask1] / 3)) # Tension reinforcement (singly reinforced beam)
                As1 = moment_plus[~mask1] / (1000 * sigmas * (0.9 * HH[~mask1] - xbal[~mask1] / 3)) # As1 (Doubly reinforced beam)
                As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # As2 (doubly reinforced beam) --> Corrected
                AsTOPStair[~mask1] = As1 + As2 # Total tension reinforcement reinforcement (doubly reinforced beam)
                sigmas_line = (2 * 1000 * sigmas * (xbal[~mask1] - 0.10 * HH[~mask1])) / (0.90 * HH[~mask1] - xbal[~mask1]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                AsBOTStair[~mask1] = (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # Compression reinforcement (doubly reinforced beam)
                # For envelope of negative moments (-)
                mask2 = moment_neg <= Mbal # Mask for identifying singly reinforced beams
                Mexcess = moment_neg[~mask2] - Mbal[~mask2] # Excessive moment (doubly reinforced beam case)
                AsBOTStair[mask2] = np.maximum(AsBOTStair[mask2], moment_neg[mask2] / (1000 * sigmas * (0.9 * HH[mask2] - xbal[mask2] / 3))) # Tension reinforcement (singly reinforced beam)
                As1 = moment_neg[~mask2] / (1000 * sigmas * (0.9 * HH[~mask2] - xbal[~mask2] / 3)) # As1 (doubly reinforced beam)
                As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask2] - 0.10*HH[~mask2])) # As2 (doubly reinforced beam) --> Corrected
                AsBOTStair[~mask2] = np.maximum(As1 + As2, AsBOTStair[~mask2]) # Total tension reinforcement reinforcement (doubly reinforced beam)
                sigmas_line = (2 * 1000 * sigmas * (xbal[~mask2] - 0.10 * HH[~mask2])) / (0.90 * HH[~mask2] - xbal[~mask2]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                AsTOPStair[~mask2] = np.maximum( (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask2] - 0.10*HH[~mask2])), AsTOPStair[~mask2]) # Compression reinforcement (doubly reinforced beam)
                # Save required longitudinal steel area
                NeededAsTOPStair[f'{j}'] = AsTOPStair.copy()
                NeededAsBOTStair[f'{j}'] = AsBOTStair.copy()
                self.beamStair.NeededAsTOP[f'{j}'] = AsTOPStair.copy()
                self.beamStair.NeededAsBOT[f'{j}'] = AsBOTStair.copy()
                # ...........................................................................
                Vrd = 1000 * tau1 * BB * 0.81 * HH
                mask = maximum_shear > Vrd
                Asw_sStair = np.maximum(maximum_shear / (0.9 * 1000 * sigmas * HH), 1.1310e-04)
                Asw_sStair[~mask] = 1.1310e-04
                NeededAsw_sStair[f'{j}'] = Asw_sStair.copy()
                swmax_Stair[f'{j}'] = np.minimum(HH, 0.20)
                self.beamStair.NeededAsw_s[f'{j}'] = Asw_sStair.copy()
            # ...........................................................................
            # Starts selecting the longitudinal steel rebar solution and the tranverse steel rebar solution
            # ...........................................................................
            attributes = ['ficornerTOP', 'ncornerTOP', 'fiintTOP', 'nintTOP', 'ficornerBOT', 'ncornerBOT', 'fiintBOT', 'nintBOT', 'fiw', 'sw', 'nwparallel_to_b', 'nwparallel_to_h']
            for attr in attributes:
                val = {f'{i}, {j}':None for i in range(len(alignmentsX)) for j in range(self.general.nstoreys)}
                setattr(self.beamX, attr, val)
                val = {f'{i}, {j}':None for i in range(len(alignmentsY)) for j in range(self.general.nstoreys)}
                setattr(self.beamY, attr, val)
                val = {f'{j}':None  for j in range(self.general.nstoreys)}
                setattr(self.beamStair, attr, val)
            # ...........................................................................
            for i in range(len(alignmentsX)):            
                for j in range(self.general.nstoreys):
                    self.beamX.ficornerTOP[f'{i}, {j}'], self.beamX.ncornerTOP[f'{i}, {j}'], self.beamX.fiintTOP[f'{i}, {j}'], self.beamX.nintTOP[f'{i}, {j}'], self.beamX.ficornerBOT[f'{i}, {j}'], self.beamX.ncornerBOT[f'{i}, {j}'], self.beamX.fiintBOT[f'{i}, {j}'], self.beamX.nintBOT[f'{i}, {j}'], self.beamX.fiw[f'{i}, {j}'], self.beamX.sw[f'{i}, {j}'], self.beamX.nwparallel_to_b[f'{i}, {j}'], self.beamX.nwparallel_to_h[f'{i}, {j}'] = _get_beam_rebars(NeededAsBOTX[f'{i}, {j}'], NeededAsTOPX[f'{i}, {j}'], self.beamX.BB[f'{i}, {j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sX[f'{i}, {j}'], swmax_X[f'{i}, {j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            for i in range(len(alignmentsY)):
                for j in range(self.general.nstoreys):
                    self.beamY.ficornerTOP[f'{i}, {j}'], self.beamY.ncornerTOP[f'{i}, {j}'], self.beamY.fiintTOP[f'{i}, {j}'], self.beamY.nintTOP[f'{i}, {j}'], self.beamY.ficornerBOT[f'{i}, {j}'], self.beamY.ncornerBOT[f'{i}, {j}'], self.beamY.fiintBOT[f'{i}, {j}'], self.beamY.nintBOT[f'{i}, {j}'], self.beamY.fiw[f'{i}, {j}'], self.beamY.sw[f'{i}, {j}'], self.beamY.nwparallel_to_b[f'{i}, {j}'], self.beamY.nwparallel_to_h[f'{i}, {j}'] = _get_beam_rebars(NeededAsBOTY[f'{i}, {j}'], NeededAsTOPY[f'{i}, {j}'], self.beamY.BB[f'{i}, {j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sY[f'{i}, {j}'], swmax_Y[f'{i}, {j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            for j in range(self.general.nstoreys):
                self.beamStair.ficornerTOP[f'{j}'], self.beamStair.ncornerTOP[f'{j}'], self.beamStair.fiintTOP[f'{j}'], self.beamStair.nintTOP[f'{j}'], self.beamStair.ficornerBOT[f'{j}'], self.beamStair.ncornerBOT[f'{j}'], self.beamStair.fiintBOT[f'{j}'], self.beamStair.nintBOT[f'{j}'], self.beamStair.fiw[f'{j}'], self.beamStair.sw[f'{j}'], self.beamStair.nwparallel_to_b[f'{j}'], self.beamStair.nwparallel_to_h[f'{j}'] = _get_beam_rebars(NeededAsBOTStair[f'{j}'], NeededAsTOPStair[f'{j}'], self.beamStair.BB[f'{j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sStair[f'{j}'], swmax_Stair[f'{j}'], sw_min_over_fi, dmin) 
            # uniformize the number of rebars at each common section 
            # (section 9 from  previous to 1 from next) at the same alignment 
            # -xx (HMA)
            attributes = ['BBbb', 'DDdd']
            for attr in attributes:
                val = {f'{j}, {i}':None for i in range(len(alignmentsX)) for j in range(self.general.nstoreys)}
                setattr(self.beamX, attr, val)
                val = {f'{j}, {i}':None for i in range(len(alignmentsY)) for j in range(self.general.nstoreys)}
                setattr(self.beamY, attr, val)

            for j in range(self.general.nstoreys): # loop over the storeys
                for i in range(len(alignmentsX)): # loop over the alignment
                    aa = self.beamX.ncornerTOP[f'{i}, {j}']
                    bb = self.beamX.nintTOP[f'{i}, {j}']
                    cc = self.beamX.ncornerBOT[f'{i}, {j}']
                    dd = self.beamX.nintBOT[f'{i}, {j}']
                    for kk in range(2, len(dd)-3, 3):
                        aa[kk] = max(aa[kk], aa[kk+1])
                        aa[kk+1] = max(aa[kk], aa[kk+1])
                        bb[kk] = max(bb[kk], bb[kk+1])
                        bb[kk+1] = max(bb[kk], bb[kk+1])
                        cc[kk] = max(cc[kk], cc[kk+1])
                        cc[kk+1] = max(cc[kk], cc[kk+1])
                        dd[kk] = max(dd[kk], dd[kk+1])
                        dd[kk+1] = max(dd[kk], dd[kk+1])

                    self.beamX.ncornerTOP[f'{i}, {j}'] = aa.copy()
                    self.beamX.nintTOP[f'{i}, {j}'] = bb.copy()
                    self.beamX.ncornerBOT[f'{i}, {j}'] = cc.copy()
                    self.beamX.nintBOT[f'{i}, {j}'] = dd.copy()
                    self.beamX.BBbb[f'{i}, {j}'] = bb.copy()
                    self.beamX.DDdd[f'{i}, {j}'] = dd.copy()

            # -yy (HMA)
            for j in range(self.general.nstoreys): # loop over the storeys
                for i in range(len(alignmentsY)): # loop over the alignement
                    aa = self.beamY.ncornerTOP[f'{i}, {j}']
                    bb = self.beamY.nintTOP[f'{i}, {j}']
                    cc = self.beamY.ncornerBOT[f'{i}, {j}']
                    dd = self.beamY.nintBOT[f'{i}, {j}']
                    for kk in range(2, len(dd)-3, 3):
                        aa[kk] = max(aa[kk], aa[kk+1])
                        aa[kk+1] = max(aa[kk], aa[kk+1])
                        bb[kk] = max(bb[kk], bb[kk+1])
                        bb[kk+1] = max(bb[kk], bb[kk+1])
                        cc[kk] = max(cc[kk], cc[kk+1])
                        cc[kk+1] = max(cc[kk], cc[kk+1])
                        dd[kk] = max(dd[kk], dd[kk+1])
                        dd[kk+1] = max(dd[kk], dd[kk+1])

                    self.beamY.ncornerTOP[f'{i}, {j}'] = aa.copy()
                    self.beamY.nintTOP[f'{i}, {j}'] = bb.copy()
                    self.beamY.ncornerBOT[f'{i}, {j}'] = cc.copy()
                    self.beamY.nintBOT[f'{i}, {j}'] = dd.copy()
                    self.beamY.BBbb[f'{i}, {j}'] = bb.copy()
                    self.beamY.DDdd[f'{i}, {j}'] = dd.copy()
            # ...........................................................................
            # Calculation of My for the beams in -XX (Note: we do not really need this)
            # ...........................................................................
            fsyd = sigmas + 0
            fcd  = sigmac + 0
            neles = len(self.beamX.Area.flatten())
            pedXEQ = self.beamX.pedEQFinal.copy()
            pedXEQ[-1, :] = self.beamX.proofEQFinal[-1, :]
            pedXEQ = pedXEQ.flatten()
            self.beamX.Matrix = np.zeros((neles, 42))
            iele  = 0
            for j in range(self.general.nstoreys): # loop over the storeys
                auxMyPos = np.array([])
                auxMyNeg = np.array([])
                for i in range(len(alignmentsX)): # loop over the alignment
                    namesly = self.beamX.NName[f'{i}, {j}']
                    nodeily = self.beamX.NNodei[f'{i}, {j}']
                    nodejly = self.beamX.NNodej[f'{i}, {j}']
                    HHly    = self.beamX.HH[f'{i}, {j}']
                    BBly    = self.beamX.BB[f'{i}, {j}']
                    LLly    = self.beamX.LL[f'{i}, {j}']
                    Ntopc   = self.beamX.ncornerTOP[f'{i}, {j}']
                    Ftopc   = self.beamX.ficornerTOP[f'{i}, {j}']
                    Ntopi   = self.beamX.nintTOP[f'{i}, {j}']
                    Ftopi   = self.beamX.fiintTOP[f'{i}, {j}']
                    Nbotc   = self.beamX.ncornerBOT[f'{i}, {j}']
                    Fbotc   = self.beamX.ficornerBOT[f'{i}, {j}']
                    Nboti   = self.beamX.nintBOT[f'{i}, {j}']
                    Fboti   = self.beamX.fiintBOT[f'{i}, {j}']
                    fiw     = self.beamX.fiw[f'{i}, {j}']
                    sw      = self.beamX.sw[f'{i}, {j}']
                    nwparallel_to_b = self.beamX.nwparallel_to_b[f'{i}, {j}']
                    nwparallel_to_h = self.beamX.nwparallel_to_h[f'{i}, {j}']
                    # ...........................................................................
                    dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                    dD_line  = 1000 * HHly - dD                                                               # in mm
                    cB       = (epscU * dD) / (epscU + esy)
                    Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    Ec       = (57000 * (fcd * 145)**0.5) / 145
                    Es       = 200000
                    nyoung   = Es / Ec
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control = np.ones(dD.shape)
                    AtoUse  = AtensCntrl + 0
                    BtoUse  = BtensCntrl + 0
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control[cC < cB] = 1
                    AtoUse[cC < cB] = AtensCntrl[cC < cB]
                    BtoUse[cC < cB] = BtensCntrl[cC < cB]
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    nameslyuni = np.unique(namesly)
                    for kk in range(len(nameslyuni)):
                        indexly = np.where(namesly==nameslyuni[kk])[0]
                        self.beamX.Matrix[iele, 0] = namesly[indexly[0]]
                        self.beamX.Matrix[iele, 1] = nodeily[indexly[0]]
                        self.beamX.Matrix[iele, 2] = nodejly[indexly[0]]
                        self.beamX.Matrix[iele, 3] = BBly[indexly[0]]
                        self.beamX.Matrix[iele, 4] = HHly[indexly[0]]
                        self.beamX.Matrix[iele, 5] = LLly[indexly[0]]
                        self.beamX.Matrix[iele, 6] = Ntopc[indexly[0]]
                        self.beamX.Matrix[iele, 7] = Ntopc[indexly[-1]]
                        self.beamX.Matrix[iele, 8] = Ftopc[indexly[0]]
                        self.beamX.Matrix[iele, 9] = Ftopc[indexly[-1]]
                        self.beamX.Matrix[iele, 10] = Nbotc[indexly[0]]
                        self.beamX.Matrix[iele, 11] = Nbotc[indexly[-1]]
                        self.beamX.Matrix[iele, 12] = Fbotc[indexly[0]]
                        self.beamX.Matrix[iele, 13] = Fbotc[indexly[-1]]
                        self.beamX.Matrix[iele, 14] = fiw[indexly[0]]
                        self.beamX.Matrix[iele, 15] = sw[indexly[0]]
                        self.beamX.Matrix[iele, 16] = nwparallel_to_b[indexly[0]]
                        self.beamX.Matrix[iele, 17] = nwparallel_to_h[indexly[0]]
                        self.beamX.Matrix[iele, 18] = fiw[indexly[-1]]
                        self.beamX.Matrix[iele, 19] = sw[indexly[-1]]
                        self.beamX.Matrix[iele, 20] = nwparallel_to_b[indexly[-1]]
                        self.beamX.Matrix[iele, 21] = nwparallel_to_h[indexly[-1]]
                        self.beamX.Matrix[iele, 22] = Ntopi[indexly[0]]
                        self.beamX.Matrix[iele, 23] = Ntopi[indexly[-1]]
                        self.beamX.Matrix[iele, 24] = Ftopi[indexly[0]]
                        self.beamX.Matrix[iele, 25] = Ftopi[indexly[-1]]
                        self.beamX.Matrix[iele, 26] = Nboti[indexly[0]]
                        self.beamX.Matrix[iele, 27] = Nboti[indexly[-1]]
                        self.beamX.Matrix[iele, 28] = Fboti[indexly[0]]
                        self.beamX.Matrix[iele, 29] = Fboti[indexly[-1]]
                        self.beamX.Matrix[iele, 30] = MyNeg[indexly[0]]
                        self.beamX.Matrix[iele, 31] = MyPos[indexly[0]]
                        self.beamX.Matrix[iele, 32] = MyNeg[indexly[-1]]
                        self.beamX.Matrix[iele, 33] = MyPos[indexly[-1]]
                        
                        iele += 1                   

                    auxMyPos = np.append(auxMyPos, np.concatenate(([0], MyPos[2:-3:3], [0])))
                    auxMyNeg = np.append(auxMyNeg, np.concatenate(([MyNeg[0]], MyNeg[2:-3:3], [MyNeg[-1]])))

                if not hasattr(self.beamX, 'MyPos'):
                    self.beamX.MyPos = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamX.MyNeg = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamX.sumMrd = np.zeros((self.general.nstoreys, len(auxMyPos)))

                self.beamX.MyPos[j, :] = auxMyPos
                self.beamX.MyNeg[j, :] = auxMyNeg
                self.beamX.sumMrd[j, :] = auxMyPos + auxMyNeg

            self.beamX.Matrix[:, 41] = pedXEQ
            # ...........................................................................
            # Calculation of My for the beams in -YY
            # ...........................................................................
            neles = len(self.beamY.Area.flatten())
            pedYEQ = self.beamY.pedEQFinal.copy()
            pedYEQ[-1, :] = self.beamY.proofEQFinal[-1, :]
            pedYEQ = pedYEQ.flatten()
            self.beamY.Matrix = np.zeros((neles, 42))
            iele  = 0
            for j in range(self.general.nstoreys): # loop over the storeys
                auxMyPos = np.array([])
                auxMyNeg = np.array([])
                for i in range(len(alignmentsY)): # loop over the alignment
                    namesly = self.beamY.NName[f'{i}, {j}']
                    nodeily = self.beamY.NNodei[f'{i}, {j}']
                    nodejly = self.beamY.NNodej[f'{i}, {j}']
                    HHly    = self.beamY.HH[f'{i}, {j}']
                    BBly    = self.beamY.BB[f'{i}, {j}']
                    LLly    = self.beamY.LL[f'{i}, {j}']
                    Ntopc   = self.beamY.ncornerTOP[f'{i}, {j}']
                    Ftopc   = self.beamY.ficornerTOP[f'{i}, {j}']
                    Ntopi   = self.beamY.nintTOP[f'{i}, {j}']
                    Ftopi   = self.beamY.fiintTOP[f'{i}, {j}']
                    Nbotc   = self.beamY.ncornerBOT[f'{i}, {j}']
                    Fbotc   = self.beamY.ficornerBOT[f'{i}, {j}']
                    Nboti   = self.beamY.nintBOT[f'{i}, {j}']
                    Fboti   = self.beamY.fiintBOT[f'{i}, {j}']
                    fiw     = self.beamY.fiw[f'{i}, {j}']
                    sw      = self.beamY.sw[f'{i}, {j}']
                    nwparallel_to_b = self.beamY.nwparallel_to_b[f'{i}, {j}']
                    nwparallel_to_h = self.beamY.nwparallel_to_h[f'{i}, {j}']
                    # ...........................................................................
                    dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                    dD_line  = 1000 * HHly - dD                                                               # in mm
                    cB       = (epscU * dD) / (epscU + esy)
                    Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    Ec       = (57000 * (fcd * 145)**0.5) / 145
                    Es       = 200000
                    nyoung   = Es / Ec
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control = np.ones(dD.shape)
                    AtoUse  = AtensCntrl + 0
                    BtoUse  = BtensCntrl + 0
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control[cC < cB] = 1
                    AtoUse[cC < cB] = AtensCntrl[cC < cB]
                    BtoUse[cC < cB] = BtensCntrl[cC < cB]
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    nameslyuni = np.unique(namesly)
                    for kk in range(len(nameslyuni)):
                        indexly = np.where(namesly==nameslyuni[kk])[0]
                        self.beamY.Matrix[iele, 0] = namesly[indexly[0]]
                        self.beamY.Matrix[iele, 1] = nodeily[indexly[0]]
                        self.beamY.Matrix[iele, 2] = nodejly[indexly[0]]
                        self.beamY.Matrix[iele, 3] = BBly[indexly[0]]
                        self.beamY.Matrix[iele, 4] = HHly[indexly[0]]
                        self.beamY.Matrix[iele, 5] = LLly[indexly[0]]
                        self.beamY.Matrix[iele, 6] = Ntopc[indexly[0]]
                        self.beamY.Matrix[iele, 7] = Ntopc[indexly[-1]]
                        self.beamY.Matrix[iele, 8] = Ftopc[indexly[0]]
                        self.beamY.Matrix[iele, 9] = Ftopc[indexly[-1]]
                        self.beamY.Matrix[iele, 10] = Nbotc[indexly[0]]
                        self.beamY.Matrix[iele, 11] = Nbotc[indexly[-1]]
                        self.beamY.Matrix[iele, 12] = Fbotc[indexly[0]]
                        self.beamY.Matrix[iele, 13] = Fbotc[indexly[-1]]
                        self.beamY.Matrix[iele, 14] = fiw[indexly[0]]
                        self.beamY.Matrix[iele, 15] = sw[indexly[0]]
                        self.beamY.Matrix[iele, 16] = nwparallel_to_b[indexly[0]]
                        self.beamY.Matrix[iele, 17] = nwparallel_to_h[indexly[0]]
                        self.beamY.Matrix[iele, 18] = fiw[indexly[-1]]
                        self.beamY.Matrix[iele, 19] = sw[indexly[-1]]
                        self.beamY.Matrix[iele, 20] = nwparallel_to_b[indexly[-1]]
                        self.beamY.Matrix[iele, 21] = nwparallel_to_h[indexly[-1]]
                        self.beamY.Matrix[iele, 22] = Ntopi[indexly[0]]
                        self.beamY.Matrix[iele, 23] = Ntopi[indexly[-1]]
                        self.beamY.Matrix[iele, 24] = Ftopi[indexly[0]]
                        self.beamY.Matrix[iele, 25] = Ftopi[indexly[-1]]
                        self.beamY.Matrix[iele, 26] = Nboti[indexly[0]]
                        self.beamY.Matrix[iele, 27] = Nboti[indexly[-1]]
                        self.beamY.Matrix[iele, 28] = Fboti[indexly[0]]
                        self.beamY.Matrix[iele, 29] = Fboti[indexly[-1]]
                        self.beamY.Matrix[iele, 30] = MyNeg[indexly[0]]
                        self.beamY.Matrix[iele, 31] = MyPos[indexly[0]]
                        self.beamY.Matrix[iele, 32] = MyNeg[indexly[-1]]
                        self.beamY.Matrix[iele, 33] = MyPos[indexly[-1]]
                        
                        iele += 1                   

                    auxMyPos = np.append(auxMyPos, np.concatenate(([0], MyPos[2:-3:3], [0])))
                    auxMyNeg = np.append(auxMyNeg, np.concatenate(([MyNeg[0]], MyNeg[2:-3:3], [MyNeg[-1]])))

                if not hasattr(self.beamY, 'MyPos'):
                    self.beamY.MyPos = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.MyNeg = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.sumMrd = np.zeros((self.general.nstoreys, len(auxMyPos)))

                self.beamY.MyPos[j, :] = auxMyPos
                self.beamY.MyNeg[j, :] = auxMyNeg
                self.beamY.sumMrd[j, :] = auxMyPos + auxMyNeg

            self.beamY.Matrix[:, 41] = pedYEQ
            # ...........................................................................
            # Calculation of My for the beams in Stairs
            # ...........................................................................
            neles = len(self.beamStair.Area.flatten())
            pedStairEQ = self.beamStair.pedEQFinal.copy()
            pedStairEQ = pedStairEQ.flatten()
            self.beamStair.Matrix = np.zeros((neles, 42))
            iele  = 0
            auxMyPos = np.array([])
            auxMyNeg = np.array([])
            for j in range(self.general.nstoreys):
                namesly = self.beamStair.NName[f'{j}']
                nodeily = self.beamStair.NNodei[f'{j}']
                nodejly = self.beamStair.NNodej[f'{j}']
                HHly    = self.beamStair.HH[f'{j}']
                BBly    = self.beamStair.BB[f'{j}']
                LLly    = self.beamStair.LL[f'{j}']
                Ntopc   = self.beamStair.ncornerTOP[f'{j}']
                Ftopc   = self.beamStair.ficornerTOP[f'{j}']
                Ntopi   = self.beamStair.nintTOP[f'{j}']
                Ftopi   = self.beamStair.fiintTOP[f'{j}']
                Nbotc   = self.beamStair.ncornerBOT[f'{j}']
                Fbotc   = self.beamStair.ficornerBOT[f'{j}']
                Nboti   = self.beamStair.nintBOT[f'{j}']
                Fboti   = self.beamStair.fiintBOT[f'{j}']
                fiw     = self.beamStair.fiw[f'{j}']
                sw      = self.beamStair.sw[f'{j}']
                nwparallel_to_b = self.beamStair.nwparallel_to_b[f'{j}']
                nwparallel_to_h = self.beamStair.nwparallel_to_h[f'{j}']
                # ...........................................................................
                dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                dD_line  = 1000 * HHly - dD                                                               # in mm
                cB       = (epscU * dD) / (epscU + esy)
                Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                rostens  = Astens / (BBly * 1000 * dD)
                As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                ros_line = As_line / (BBly * 1000 * dD)
                cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                Ec       = (57000 * (fcd * 145)**0.5) / 145
                Es       = 200000
                nyoung   = Es / Ec
                AcomprCntrl = rostens + ros_line
                AtensCntrl  = rostens + ros_line
                BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                Control = np.ones(dD.shape)
                AtoUse  = AtensCntrl + 0
                BtoUse  = BtensCntrl + 0
                Control[cC >= cB] = 0
                AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                fiy = fiy1 + 0
                fiy[Control==0] = fiy2[Control==0]
                Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                # ...........................................................................
                Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                rostens  = Astens / (BBly * 1000 * dD)
                As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                ros_line = As_line / (BBly * 1000 * dD)
                cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                AcomprCntrl = rostens + ros_line
                AtensCntrl  = rostens + ros_line
                BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                Control[cC < cB] = 1
                AtoUse[cC < cB] = AtensCntrl[cC < cB]
                BtoUse[cC < cB] = BtensCntrl[cC < cB]
                Control[cC >= cB] = 0
                AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                fiy = fiy1 + 0
                fiy[Control==0] = fiy2[Control==0]
                Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                # ...........................................................................
                self.beamStair.Matrix[iele, 0] = namesly[0]
                self.beamStair.Matrix[iele, 1] = nodeily[0]
                self.beamStair.Matrix[iele, 2] = nodejly[0]
                self.beamStair.Matrix[iele, 3] = BBly[0]
                self.beamStair.Matrix[iele, 4] = HHly[0]
                self.beamStair.Matrix[iele, 5] = LLly[0]
                self.beamStair.Matrix[iele, 6] = Ntopc[0]
                self.beamStair.Matrix[iele, 7] = Ntopc[-1]
                self.beamStair.Matrix[iele, 8] = Ftopc[0]
                self.beamStair.Matrix[iele, 9] = Ftopc[-1]
                self.beamStair.Matrix[iele, 10] = Nbotc[0]
                self.beamStair.Matrix[iele, 11] = Nbotc[-1]
                self.beamStair.Matrix[iele, 12] = Fbotc[0]
                self.beamStair.Matrix[iele, 13] = Fbotc[-1]
                self.beamStair.Matrix[iele, 14] = fiw[0]
                self.beamStair.Matrix[iele, 15] = sw[0]
                self.beamStair.Matrix[iele, 16] = nwparallel_to_b[0]
                self.beamStair.Matrix[iele, 17] = nwparallel_to_h[0]
                self.beamStair.Matrix[iele, 18] = fiw[-1]
                self.beamStair.Matrix[iele, 19] = sw[-1]
                self.beamStair.Matrix[iele, 20] = nwparallel_to_b[-1]
                self.beamStair.Matrix[iele, 21] = nwparallel_to_h[-1]
                self.beamStair.Matrix[iele, 22] = Ntopi[0]
                self.beamStair.Matrix[iele, 23] = Ntopi[-1]
                self.beamStair.Matrix[iele, 24] = Ftopi[0]
                self.beamStair.Matrix[iele, 25] = Ftopi[-1]
                self.beamStair.Matrix[iele, 26] = Nboti[0]
                self.beamStair.Matrix[iele, 27] = Nboti[-1]
                self.beamStair.Matrix[iele, 28] = Fboti[0]
                self.beamStair.Matrix[iele, 29] = Fboti[-1]
                self.beamStair.Matrix[iele, 30] = MyNeg[0]
                self.beamStair.Matrix[iele, 31] = MyPos[0]
                self.beamStair.Matrix[iele, 32] = MyNeg[-1]
                self.beamStair.Matrix[iele, 33] = MyPos[-1]
                iele += 1                   

                if not hasattr(self.beamStair, 'MyPos'):
                    self.beamStair.MyPos = np.zeros((self.general.nstoreys, 2))
                    self.beamStair.MyNeg = np.zeros((self.general.nstoreys, 2))
                    self.beamStair.sumMrd = np.zeros((self.general.nstoreys, 2))

                self.beamStair.MyPos[j, :] = np.array([0, 0])
                self.beamStair.MyNeg[j, :] = MyNeg[[0,2]]
                self.beamStair.sumMrd[j, :]= self.beamStair.MyPos[j, :] + self.beamStair.MyNeg[j, :]

            self.beamStair.Matrix[:, 41] = pedStairEQ

        return CvFLAGX, CvFLAGY, CvFLAGStair, auxbeam
    
    def _cdn_columns(self, auxbeam):
        """
        Designs columns usign DCL1 properties
        Refrences: RBA, 1935 + RSCSS 1958
        No seismic loads included, so no flags to export
        Design based on ultimate strength analysis
        """
        # ...........................................................................
        # General Material Propeties
        # ...........................................................................
        rho_min = 0.005  # Minimum reinforcement ratio
        rho_max = 0.05   # Maximum reinforcement ratio
        dmin = 0.035     # Minimum spacing between longitudinal rebar centroids
        dmax = 0.15      # Maximum spacing between longitudinal rebar centroids
        sw_min_over_fi = 12  # Minimum ratio between stirrup spacing and longitudinal rebar diameter
        cover = 0.03  # Concrete cover
        fiw_min = 0.006  # Minimum stirrup diameter
        # ...........................................................................
        # Sets the maximum column dimensions
        # ...........................................................................
        if self.general.ColumnType == 1:
            maxH = self.column.maxHsquared + 0
        else:
            maxH = self.column.maxHrectangular + 0
        # ...........................................................................
        # Variables for the design based on the DCN Design Routines
        # ...........................................................................
        CpFLAGX = np.zeros(self.column.name.shape)
        CpFLAGY = np.zeros(self.column.name.shape)
        # ...........................................................................
        HX = self.column.HX.copy()
        HY = self.column.HY.copy()
        L = self.column.L.copy()
        if np.max(HX) > maxH or np.max(HY) > maxH:
            CpFLAGfc = 222
        else:
            CpFLAGfc = 0
        # ...........................................................................
        # Checks if the design should be finished or not
        # ...........................................................................
        print('Columns OK. Stage 1 complete!')
        # ...........................................................................
        # Determination of the necessary reinforcement using just the minimum rebar reinforcement
        # ...........................................................................
        aux = np.zeros(self.column.name.shape)
        Area = HX * HY
        Lambda = L / np.minimum(HX, HY)
        aux = 0.005 + 0.0006 * (Lambda - 5)
        aux[aux < 0.005] = 0.005
        aux[aux > 0.008] = 0.008
        Asmin = aux * Area
        self.column.AsX = (0.50**2) * Asmin
        self.column.AsY = (0.50**2) * Asmin
        if self.general.ColumnType != 1:
            # This part has been modified, there was a mistake in the original version
            sizeRatio = HX / HY
            mask1 = np.logical_and(sizeRatio < 1.20, sizeRatio > 0.80) # meaning that dimensions are close
            mask2 = np.logical_and(~mask1, sizeRatio >= 1.20) # meaning that HX is much larger
            self.column.AsX[mask2] = 0.33 * Asmin[mask2]
            self.column.AsY[mask2] = 0.17 * Asmin[mask2]
            mask3 = np.logical_and(~mask1, sizeRatio <= 0.80) # meaning that HY is much larger
            self.column.AsX[mask3] = 0.17 * Asmin[mask3]
            self.column.AsY[mask3] = 0.33 * Asmin[mask3]

        self.column.AsX_sw = np.ones(self.column.name.shape) * 1.1310e-04  # initial assumption for AshX/sw
        self.column.AsY_sw = np.ones(self.column.name.shape) * 1.1310e-04  # initial assumption for AshY/sw
        sw_max = np.minimum(np.minimum(HX, HY), 0.25)  # maximum stirrup spacing
        # ...........................................................................
        # Get the rebar solution
        # ...........................................................................
        attributes = ['fi_corner', 'fi_layintX', 'nbar_HminusX', 'nlayintX', 'Rhosl', 'RhoslX', 'RhoslY', 'nintBOT', 'sw', 'fiw', 'nwparallel_to_X', 'nwparallel_to_Y']
        for attr in attributes:
            setattr(self.column, attr, np.zeros(self.column.AsX.shape))
        for jj in range(self.column.AsX.shape[1]):
            self.column.fi_corner[:, jj], self.column.fi_layintX[:, jj], self.column.nbar_HminusX[:, jj], self.column.nlayintX[:, jj], self.column.Rhosl[:, jj], self.column.RhoslX[:, jj], self.column.RhoslY[:, jj], self.column.sw[:, jj], self.column.fiw[:, jj], self.column.nwparallel_to_X[:, jj], self.column.nwparallel_to_Y[:, jj] = _get_column_rebars(self.column.AsX[:, jj], self.column.AsY[:, jj], HX[:, jj], HY[:, jj], rho_min, dmin, dmax, cover, self.column.AsX_sw[:, jj], self.column.AsY_sw[:, jj], sw_min_over_fi, sw_max[:, jj], fiw_min)
        # ...........................................................................
        # Save stuff
        # ...........................................................................
        nrow = self.column.name.shape[0] * self.column.name.shape[1]
        ncol = 27
        self.column.Matrix = np.zeros((nrow, ncol))
        self.column.Matrix[:, 0] = (self.column.name.T).flatten()
        self.column.Matrix[:, 1] = (self.column.elasnodei.T).flatten() + 7000
        self.column.Matrix[:, 2] = (self.column.elasnodej.T).flatten() + 2000
        self.column.Matrix[:, 3] = (self.column.HX.T).flatten()
        self.column.Matrix[:, 4] = (self.column.HY.T).flatten()
        self.column.Matrix[:, 5] = (self.column.L.T).flatten()
        self.column.Matrix[:, 6] = (self.column.storey.T).flatten()
        self.column.Matrix[:, 7] = (self.column.perimeter.T).flatten()
        self.column.Matrix[:, 8] = (self.column.nbar_HminusX.T).flatten()
        self.column.Matrix[:, 9]  = (self.column.nlayintX.T).flatten()
        self.column.Matrix[:, 10]  = (self.column.fi_corner.T).flatten()
        self.column.Matrix[:, 11] = (self.column.fi_layintX.T).flatten()
        self.column.Matrix[:, 12] = (self.column.Rhosl.T).flatten()
        self.column.Matrix[:, 13] = (self.column.sw.T).flatten()
        self.column.Matrix[:, 14] = (self.column.fiw.T).flatten()
        self.column.Matrix[:, 15] = (self.column.nwparallel_to_X.T).flatten()
        self.column.Matrix[:, 16] = (self.column.nwparallel_to_Y.T).flatten()
        self.column.Matrix[:, 17] = (self.column.N_EQfinal.T).flatten()
        auxDir = np.ones(self.column.Rhosl.shape[1])
        auxDir[self.column.Colindex2] = 2
        # ...........................................................................
        # Checking the maximum rho_l condition
        # ...........................................................................
        if np.max(self.column.Rhosl) > rho_max:
            aux1 = self.column.Rhosl > rho_max
            aux2 = self.column.Rhosl <= rho_max
            CpFLAGX[aux1] = 1
            CpFLAGX[aux2] = 0
            CpFLAGY[aux1] = 1
            CpFLAGY[aux2] = 0
            for i in range(self.column.Rhosl.shape[0]):
                for j in range(self.column.Rhosl.shape[1]):
                    if self.column.Rhosl[i, j]> rho_max:
                        if self.general.ColumnType == 1:
                            CpFLAGX[i, j] = 1
                            CpFLAGY[i, j] = 1
                        else:
                            if auxDir[j] == 1:
                                CpFLAGX[i, self.column.Colindex1] = 1                                                       
                                CpFLAGY[i, self.column.Colindex1] = 0
                            else:
                                CpFLAGX[i, self.column.Colindex2] = 0                                                       
                                CpFLAGY[i, self.column.Colindex2] = 1
                    else:
                        CpFLAGX[i, j] = 0
                        CpFLAGY[i, j] = 0                                                                                            

        aucx = np.where(self.column.Astair[0, :] > 0)[0]
        for i in range(self.general.nstoreys):
            CpFLAGX[i, aucx[0]] = max(CpFLAGX[i, aucx[0]], CpFLAGX[i, aucx[1]])
            CpFLAGY[i, aucx[0]] = max(CpFLAGY[i, aucx[0]], CpFLAGY[i, aucx[1]])
            CpFLAGX[i, aucx[1]] = CpFLAGX[i, aucx[0]]
            CpFLAGY[i, aucx[1]] = CpFLAGY[i, aucx[0]]
            CpFLAGX[i, aucx[2]] = max(CpFLAGX[i, aucx[2]], CpFLAGX[i, aucx[3]])
            CpFLAGY[i, aucx[2]] = max(CpFLAGY[i, aucx[2]], CpFLAGY[i, aucx[3]])
            CpFLAGX[i, aucx[3]] = CpFLAGX[i, aucx[2]]
            CpFLAGY[i, aucx[3]] = CpFLAGY[i, aucx[2]]

        aux = np.sum(CpFLAGY) + np.sum(CpFLAGX) + auxbeam
        if aux > 0:
            print('Columns Not OK...the maximum Rho_l condition... still %d to change' % int(sum(CpFLAGY.flatten()) + sum(CpFLAGX.flatten())))
        else:
            print('Columns Rho_l condition OK!')

        return CpFLAGX, CpFLAGY, CpFLAGfc, aux

    def _cdl_beams(self):
        """
        Design methodology for beams considering the case of DCL1 (REBAP83_PT) design.
        The beams are separated into different alignments and a single section is used. 
        1) The maximum bending moment of the alignement (max of all M1s and of all M9s) is used to assess the maximum As-.
        2) The maximum bending moment of the mid spans (max of all M5s) is used to compute the required As+.
        3) The corresponding solution in terms of rebars is calculated for As- ans As+ usign the same diameter.
        4) Calculate the rebar solution and exports the key elements for the nonlinear modelling
        """
        # ...........................................................................
        # Designs columns usign DCL properties
        # Refrences: RBA, 1935 + RSCSS 1958 + improved materials
        # Design based on working stress method
        # ...........................................................................
        fckvect = [180, 225, 300, 350, 400]
        tau1vect = [0.4, 0.45, 0.50, 0.55, 0.60]
        tausmaxvect = [2.4, 2.7, 3.0, 3.3, 3.6]
        # ...........................................................................
        tau1 = 1000 * np.interp(self.general.fckcube, fckvect, tau1vect)  # allowable shear stress values that can be carried by the concrete in beam
        taumax = 1000 * np.interp(self.general.fckcube, fckvect, tausmaxvect)  # allowable shear stress values that can be carried by the beam
        dmin = 0.035  # minimum distance between longitudinal rebars
        dmax_between_long_bars = 0.10  # maximum distance between longitudinal rebars
        miueconomic = 0.25
        top_to_bot_ratio = 0.50  # top to bottom reinforcement ratio
        sw_min_over_fi = 12.00  # minimum stirrup spacing to longitudinal rebar diameter ratio
        cover = 0.03  # concrete cover
        epscU = 3.5/1000  # Concrete crushing strain used to compute section capacity
        esy = self.general.fsyk/200000  # Steel yield strain used to compute section capacity
        n = 15  # Modular ratio
        if self.general.ag > 0.05: 
            sigmac = self.general.fcdEQ + 0  # allowed concrete compressive stress (or design strength)
            sigmas = self.general.fsydEQ + 0  # allowed steel yield stress (or design strength)
        else:
            sigmac = self.general.fcd + 0
            sigmas = self.general.fsyd + 0

        if self.general.fck < 27.6: 
            betafc = 0.85  # Stress-block coefficient used to compute section capacity
        elif self.general.fck > 55.17:
            betafc = 0.65
        else:
            betafc = 1.05 - 0.05*self.general.fck/6.9
        # ...........................................................................
        # Verifies the adequcy of the sectional dimensions
        # ...........................................................................
        alignmentsX = np.unique(self.beamX.index)
        CvFLAGX = np.zeros((self.general.nstoreys, self.beamX.index.shape[0]))
        for i in range(len(alignmentsX)):
            mask = self.beamX.index == alignmentsX[i]
            for j in range(self.general.nstoreys):
                BB = self.beamX.BB[f'{i}, {j}'].copy()
                HH = self.beamX.HH[f'{i}, {j}'].copy()
                moment_plus = self.beamX.MomentEnvelopePlusCDL[f'{i}, {j}'].copy()
                moment_neg = self.beamX.MomentEnvelopeNegCDL[f'{i}, {j}'].copy()
                maximum_shear = self.beamX.ShearEnvelopeCDL[f'{i}, {j}'].copy()
                muplusX = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * sigmac * 1000)
                munegX = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * sigmac * 1000)
                tauX = np.abs(maximum_shear) / (BB * (0.81 * HH))
                if max(muplusX) > miueconomic or max(munegX) > miueconomic or max(tauX) > taumax:
                    CvFLAGX[j, mask] = 1 # not satisfied
                else:
                    CvFLAGX[j, mask] = 0 # satisfied
        # ...........................................................................
        alignmentsY = np.unique(self.beamY.index)
        CvFLAGY = np.zeros((self.general.nstoreys, self.beamY.index.shape[0]))
        for i in range(len(alignmentsY)):
            mask = self.beamY.index == alignmentsY[i]
            for j in range(self.general.nstoreys):
                BB = self.beamY.BB[f'{i}, {j}'].copy()
                HH = self.beamY.HH[f'{i}, {j}'].copy()
                moment_plus = self.beamY.MomentEnvelopePlusCDL[f'{i}, {j}'].copy()
                moment_neg = self.beamY.MomentEnvelopeNegCDL[f'{i}, {j}'].copy()
                maximum_shear = self.beamY.ShearEnvelopeCDL[f'{i}, {j}'].copy()
                muplusY = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * sigmac * 1000)
                munegY = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * sigmac * 1000)
                tauY = np.abs(maximum_shear) / (BB * (0.81 * HH))
                if max(muplusY) > miueconomic or max(munegY) > miueconomic or max(tauY) > taumax:
                    CvFLAGY[j, mask] = 1 # not satisfied
                else:
                    CvFLAGY[j, mask] = 0 # satisfied
        # ...........................................................................
        CvFLAGStair = np.zeros(self.general.nstoreys)
        for j in range(self.general.nstoreys):
            BB = self.beamStair.BB[f'{j}'].copy()
            HH = self.beamStair.HH[f'{j}'].copy()
            moment_plus = self.beamStair.MomentEnvelopePlusCDL[f'{j}'].copy()
            moment_neg = self.beamStair.MomentEnvelopeNegCDL[f'{j}'].copy()
            maximum_shear = self.beamStair.ShearEnvelopeCDL[f'{j}'].copy()
            muplusStair = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * sigmac * 1000)
            munegStair = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * sigmac * 1000)
            tauStair = np.abs(maximum_shear) / (BB * (0.81 * HH))
            if max(muplusStair) > miueconomic or max(munegStair) > miueconomic or max(tauStair) > taumax:
                CvFLAGStair[j] = 1 # not satisfied
            else:
                CvFLAGStair[j] = 0 # satisfied
        # ...........................................................................
        # Verifies the need for a new section
        # ...........................................................................
        auxbeam = np.sum(CvFLAGX) + np.sum(CvFLAGY) + np.sum(CvFLAGStair)
        if auxbeam > 0.99:
            print(f"Beams Not OK ... still {auxbeam:.0f} to change")
        else:
            print("Beams stage 1 complete")
            # ...........................................................................
            # When ok, selects the longitudinal steel rebar solution and the tranverse steel rebar solution
            # ...........................................................................
            As_sw_rational = 2 * np.pi * 0.25 * (0.006**2) / 0.3 # It is two legs stirrups with 6 mm diameter and sw equals to 0.30 m 
            # BeamX
            NeededAsTOPX = {}
            NeededAsBOTX = {}
            NeededAsw_sX = {}
            swmax_X = {}
            self.beamX.NeededAsTOP = {}
            self.beamX.NeededAsBOT = {}
            self.beamX.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                for i in range(len(alignmentsX)):
                    BB = self.beamX.BB[f'{i}, {j}'].copy()
                    HH = self.beamX.HH[f'{i}, {j}'].copy()
                    moment_plus = self.beamX.MomentEnvelopePlusCDL[f'{i}, {j}'].copy()
                    moment_neg = self.beamX.MomentEnvelopeNegCDL[f'{i}, {j}'].copy()
                    maximum_shear = self.beamX.ShearEnvelopeCDL[f'{i}, {j}'].copy()
                    moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                    moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                    moment_plus = np.abs(moment_plus) # for just to have the real envelope (by HMA)
                    moment_neg = np.abs(moment_neg) # for just to have the real envelope (by HMA)
                    # Calculates the balanced moment capacity
                    xbal = (sigmac * 0.90 * HH) / (sigmac + sigmas / n)
                    Cbal = 0.50 * sigmac * 1000 * BB * xbal
                    Mbal = Cbal * (0.90 * HH - 0.3333 * xbal)
                    # Calculate longitudinal steel area
                    AsTOPX = np.zeros(moment_plus.shape)  # Required steel area at top
                    AsBOTX = np.zeros(moment_plus.shape)  # Required steel area at bottom
                    # For envelope of positive moments (+)
                    mask1 = moment_plus <= Mbal # Mask for identifying singly reinforced beams
                    Mexcess = moment_plus[~mask1] - Mbal[~mask1] # Excessive moment (doubly reinforced beam case)
                    AsTOPX[mask1] = moment_plus[mask1] / (1000 * sigmas * (0.9 * HH[mask1] - xbal[mask1] / 3)) # Tension reinforcement (singly reinforced beam)
                    As1 = moment_plus[~mask1] / (1000 * sigmas * (0.9 * HH[~mask1] - xbal[~mask1] / 3)) # As1 (Doubly reinforced beam)
                    As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # As2 (doubly reinforced beam) --> Corrected
                    AsTOPX[~mask1] = As1 + As2 # Total tension reinforcement reinforcement (doubly reinforced beam)
                    sigmas_line = (2 * 1000 * sigmas * (xbal[~mask1] - 0.10 * HH[~mask1])) / (0.90 * HH[~mask1] - xbal[~mask1]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                    AsBOTX[~mask1] = (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # Compression reinforcement (doubly reinforced beam)
                    # For envelope of negative moments (-)
                    mask2 = moment_neg <= Mbal # Mask for identifying singly reinforced beams
                    Mexcess = moment_neg[~mask2] - Mbal[~mask2] # Excessive moment (doubly reinforced beam case)
                    AsBOTX[mask2] = np.maximum(AsBOTX[mask2], moment_neg[mask2] / (1000 * sigmas * (0.9 * HH[mask2] - xbal[mask2] / 3))) # Tension reinforcement (singly reinforced beam)
                    As1 = moment_neg[~mask2] / (1000 * sigmas * (0.9 * HH[~mask2] - xbal[~mask2] / 3)) # As1 (doubly reinforced beam)
                    As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask2] - 0.10*HH[~mask2])) # As2 (doubly reinforced beam) --> Corrected
                    AsBOTX[~mask2] = np.maximum(As1 + As2, AsBOTX[~mask2]) # Total tension reinforcement reinforcement (doubly reinforced beam)
                    sigmas_line = (2 * 1000 * sigmas * (xbal[~mask2] - 0.10 * HH[~mask2])) / (0.90 * HH[~mask2] - xbal[~mask2]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                    AsTOPX[~mask2] = np.maximum( (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask2] - 0.10*HH[~mask2])), AsTOPX[~mask2]) # Compression reinforcement (doubly reinforced beam)
                    # Save required longitudinal steel area
                    NeededAsTOPX[f'{i}, {j}'] = AsTOPX.copy()
                    NeededAsBOTX[f'{i}, {j}'] = AsBOTX.copy()
                    self.beamX.NeededAsTOP[f'{i}, {j}'] = AsTOPX.copy()
                    self.beamX.NeededAsBOT[f'{i}, {j}'] = AsBOTX.copy()
                    # ...........................................................................
                    # calculate the shear reinforcement
                    Vrd = tau1 * BB * 0.90 * HH
                    mask = 1000 * np.maximum(AsTOPX, AsBOTX) * 0.81 * HH * sigmas < Vrd * 0.90 * HH
                    Asw_sX = np.maximum(maximum_shear / (0.9 * 1000 * sigmas * HH), As_sw_rational)
                    Asw_sX[~mask] = np.maximum((maximum_shear - Vrd) / (0.9 * 1000 * sigmas * HH), As_sw_rational)[~mask]
                    NeededAsw_sX[f'{i}, {j}'] = Asw_sX.copy()
                    swmax_X[f'{i}, {j}'] = np.minimum(HH, 0.20)
                    self.beamX.NeededAsw_s[f'{i}, {j}'] = Asw_sX.copy()
            # ...........................................................................
            # BeamY
            NeededAsTOPY = {}
            NeededAsBOTY = {}
            NeededAsw_sY = {}
            swmax_Y = {}
            self.beamY.NeededAsTOP = {}
            self.beamY.NeededAsBOT = {}
            self.beamY.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                for i in range(len(alignmentsY)):
                    BB = self.beamY.BB[f'{i}, {j}'].copy()
                    HH = self.beamY.HH[f'{i}, {j}'].copy()
                    moment_plus = self.beamY.MomentEnvelopePlusCDL[f'{i}, {j}'].copy()
                    moment_neg = self.beamY.MomentEnvelopeNegCDL[f'{i}, {j}'].copy()
                    maximum_shear = np.abs(self.beamY.ShearEnvelopeCDL[f'{i}, {j}'])
                    moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                    moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                    moment_plus = np.abs(moment_plus) # for just to have the real envelope (by HMA)
                    moment_neg = np.abs(moment_neg) # for just to have the real envelope (by HMA)
                    # Calculates the balanced moment capacity
                    xbal = (sigmac * 0.90 * HH) / (sigmac + sigmas / n)
                    Cbal = 0.50 * sigmac * 1000 * BB * xbal
                    Mbal = Cbal * (0.90 * HH - 0.3333 * xbal)
                    # Calculate longitudinal steel area
                    AsTOPY = np.zeros(moment_plus.shape)  # Required steel area at top
                    AsBOTY = np.zeros(moment_plus.shape)  # Required steel area at bottom
                    # For envelope of positive moments (+)
                    mask1 = moment_plus <= Mbal # Mask for identifying singly reinforced beams
                    Mexcess = moment_plus[~mask1] - Mbal[~mask1] # Excessive moment (doubly reinforced beam case)
                    AsTOPY[mask1] = moment_plus[mask1] / (1000 * sigmas * (0.9 * HH[mask1] - xbal[mask1] / 3)) # Tension reinforcement (singly reinforced beam)
                    As1 = moment_plus[~mask1] / (1000 * sigmas * (0.9 * HH[~mask1] - xbal[~mask1] / 3)) # As1 (Doubly reinforced beam)
                    As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # As2 (doubly reinforced beam) --> Corrected
                    AsTOPY[~mask1] = As1 + As2 # Total tension reinforcement reinforcement (doubly reinforced beam)
                    sigmas_line = (2 * 1000 * sigmas * (xbal[~mask1] - 0.10 * HH[~mask1])) / (0.90 * HH[~mask1] - xbal[~mask1]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                    AsBOTY[~mask1] = (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # Compression reinforcement (doubly reinforced beam)
                    # For envelope of negative moments (-)
                    mask2 = moment_neg <= Mbal # Mask for identifying singly reinforced beams
                    Mexcess = moment_neg[~mask2] - Mbal[~mask2] # Excessive moment (doubly reinforced beam case)
                    AsBOTY[mask2] = np.maximum(AsBOTY[mask2], moment_neg[mask2] / (1000 * sigmas * (0.9 * HH[mask2] - xbal[mask2] / 3))) # Tension reinforcement (singly reinforced beam)
                    As1 = moment_neg[~mask2] / (1000 * sigmas * (0.9 * HH[~mask2] - xbal[~mask2] / 3)) # As1 (doubly reinforced beam)
                    As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask2] - 0.10*HH[~mask2])) # As2 (doubly reinforced beam) --> Corrected
                    AsBOTY[~mask2] = np.maximum(As1 + As2, AsBOTY[~mask2]) # Total tension reinforcement reinforcement (doubly reinforced beam)
                    sigmas_line = (2 * 1000 * sigmas * (xbal[~mask2] - 0.10 * HH[~mask2])) / (0.90 * HH[~mask2] - xbal[~mask2]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                    AsTOPY[~mask2] = np.maximum( (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask2] - 0.10*HH[~mask2])), AsTOPY[~mask2]) # Compression reinforcement (doubly reinforced beam)
                    # Save required longitudinal steel area
                    NeededAsTOPY[f'{i}, {j}'] = AsTOPY.copy()
                    NeededAsBOTY[f'{i}, {j}'] = AsBOTY.copy()
                    self.beamY.NeededAsTOP[f'{i}, {j}'] = AsTOPY.copy()
                    self.beamY.NeededAsBOT[f'{i}, {j}'] = AsBOTY.copy()
                    # ...........................................................................
                    # calculate the shear reinforcement
                    Vrd = tau1 * BB * 0.90 * HH
                    mask = 1000 * np.maximum(AsTOPY, AsBOTY) * 0.81 * HH * sigmas < Vrd * 0.9 * HH
                    Asw_sY = np.maximum(maximum_shear / (0.9 * 1000 * sigmas * HH), As_sw_rational)
                    Asw_sY[~mask] = np.maximum((maximum_shear - Vrd) / (0.9 * 1000 * sigmas * HH), As_sw_rational)[~mask]
                    NeededAsw_sY[f'{i}, {j}'] = Asw_sY.copy()
                    swmax_Y[f'{i}, {j}'] = np.minimum(HH, 0.20)
                    self.beamY.NeededAsw_s[f'{i}, {j}'] = Asw_sY.copy()
            # ...........................................................................
            # BeamStair
            NeededAsTOPStair = {}
            NeededAsBOTStair = {}
            NeededAsw_sStair = {}
            swmax_Stair = {}
            self.beamStair.NeededAsTOP = {}
            self.beamStair.NeededAsBOT = {}
            self.beamStair.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                BB = self.beamStair.BB[f'{j}'].copy()
                HH = self.beamStair.HH[f'{j}'].copy()
                moment_plus = self.beamStair.MomentEnvelopePlusCDL[f'{j}'].copy()
                moment_neg = self.beamStair.MomentEnvelopeNegCDL[f'{j}'].copy()
                maximum_shear = np.abs(self.beamStair.ShearEnvelopeCDL[f'{j}'])
                moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                moment_plus = np.abs(moment_plus)
                moment_neg = np.abs(moment_neg)
                # Calculates the balanced moment capacity
                xbal = (sigmac * 0.90 * HH) / (sigmac + sigmas / n)
                Cbal = 0.50 * sigmac * 1000 * BB * xbal
                Mbal = Cbal * (0.90 * HH - 0.3333 * xbal)
                # Calculate longitudinal steel area
                AsTOPStair = np.zeros(moment_plus.shape)  # Required steel area at top
                AsBOTStair = np.zeros(moment_plus.shape)  # Required steel area at bottom
                # For envelope of positive moments (+)
                mask1 = moment_plus <= Mbal # Mask for identifying singly reinforced beams
                Mexcess = moment_plus[~mask1] - Mbal[~mask1] # Excessive moment (doubly reinforced beam case)
                AsTOPStair[mask1] = moment_plus[mask1] / (1000 * sigmas * (0.9 * HH[mask1] - xbal[mask1] / 3)) # Tension reinforcement (singly reinforced beam)
                As1 = moment_plus[~mask1] / (1000 * sigmas * (0.9 * HH[~mask1] - xbal[~mask1] / 3)) # As1 (Doubly reinforced beam)
                As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # As2 (doubly reinforced beam) --> Corrected
                AsTOPStair[~mask1] = As1 + As2 # Total tension reinforcement reinforcement (doubly reinforced beam)
                sigmas_line = (2 * 1000 * sigmas * (xbal[~mask1] - 0.10 * HH[~mask1])) / (0.90 * HH[~mask1] - xbal[~mask1]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                AsBOTStair[~mask1] = (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask1] - 0.10*HH[~mask1])) # Compression reinforcement (doubly reinforced beam)
                # For envelope of negative moments (-)
                mask2 = moment_neg <= Mbal # Mask for identifying singly reinforced beams
                Mexcess = moment_neg[~mask2] - Mbal[~mask2] # Excessive moment (doubly reinforced beam case)
                AsBOTStair[mask2] = np.maximum(AsBOTStair[mask2], moment_neg[mask2] / (1000 * sigmas * (0.9 * HH[mask2] - xbal[mask2] / 3))) # Tension reinforcement (singly reinforced beam)
                As1 = moment_neg[~mask2] / (1000 * sigmas * (0.9 * HH[~mask2] - xbal[~mask2] / 3)) # As1 (doubly reinforced beam)
                As2 = Mexcess / (1000 * sigmas * (0.90*HH[~mask2] - 0.10*HH[~mask2])) # As2 (doubly reinforced beam) --> Corrected
                AsBOTStair[~mask2] = np.maximum(As1 + As2, AsBOTStair[~mask2]) # Total tension reinforcement reinforcement (doubly reinforced beam)
                sigmas_line = (2 * 1000 * sigmas * (xbal[~mask2] - 0.10 * HH[~mask2])) / (0.90 * HH[~mask2] - xbal[~mask2]) # Maximum stress of the compression reinforcement (doubly reinforced beam)
                AsTOPStair[~mask2] = np.maximum( (2 * n * Mexcess) / (np.minimum(sigmas_line, sigmas*1000) * (2*n - 1) * (0.90*HH[~mask2] - 0.10*HH[~mask2])), AsTOPStair[~mask2]) # Compression reinforcement (doubly reinforced beam)
                # Save required longitudinal steel area
                NeededAsTOPStair[f'{j}'] = AsTOPStair.copy()
                NeededAsBOTStair[f'{j}'] = AsBOTStair.copy()
                self.beamStair.NeededAsTOP[f'{j}'] = AsTOPStair.copy()
                self.beamStair.NeededAsBOT[f'{j}'] = AsBOTStair.copy()
                # ...........................................................................
                # calculate the shear reinforcement
                Vrd = tau1 * BB * 0.90 * HH
                mask = 1000 * np.maximum(AsTOPStair, AsBOTStair) * 0.81 * HH * sigmas < Vrd * 0.9 * HH
                Asw_sStair = np.maximum(maximum_shear / (0.9 * 1000 * sigmas * HH), As_sw_rational)
                Asw_sStair[~mask] = np.maximum((maximum_shear - Vrd) / (0.9 * 1000 * sigmas * HH), As_sw_rational)[~mask]
                NeededAsw_sStair[f'{j}'] = Asw_sStair.copy()
                swmax_Stair[f'{j}'] = np.minimum(HH, 0.20)
                self.beamStair.NeededAsw_s[f'{j}'] = Asw_sStair.copy()
            # ...........................................................................
            # Starts selecting the longitudinal steel rebar solution and the tranverse steel rebar solution
            # ...........................................................................
            attributes = ['ficornerTOP', 'ncornerTOP', 'fiintTOP', 'nintTOP', 'ficornerBOT', 'ncornerBOT', 'fiintBOT', 'nintBOT', 'fiw', 'sw', 'nwparallel_to_b', 'nwparallel_to_h']
            for attr in attributes:
                val = {f'{i}, {j}':None for i in range(len(alignmentsX)) for j in range(self.general.nstoreys)}
                setattr(self.beamX, attr, val)
                val = {f'{i}, {j}':None for i in range(len(alignmentsY)) for j in range(self.general.nstoreys)}
                setattr(self.beamY, attr, val)
                val = {f'{j}':None  for j in range(self.general.nstoreys)}
                setattr(self.beamStair, attr, val)
            # ...........................................................................
            for i in range(len(alignmentsX)):            
                for j in range(self.general.nstoreys):
                    self.beamX.ficornerTOP[f'{i}, {j}'], self.beamX.ncornerTOP[f'{i}, {j}'], self.beamX.fiintTOP[f'{i}, {j}'], self.beamX.nintTOP[f'{i}, {j}'], self.beamX.ficornerBOT[f'{i}, {j}'], self.beamX.ncornerBOT[f'{i}, {j}'], self.beamX.fiintBOT[f'{i}, {j}'], self.beamX.nintBOT[f'{i}, {j}'], self.beamX.fiw[f'{i}, {j}'], self.beamX.sw[f'{i}, {j}'], self.beamX.nwparallel_to_b[f'{i}, {j}'], self.beamX.nwparallel_to_h[f'{i}, {j}'] = _get_beam_rebars(NeededAsBOTX[f'{i}, {j}'], NeededAsTOPX[f'{i}, {j}'], self.beamX.BB[f'{i}, {j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sX[f'{i}, {j}'], swmax_X[f'{i}, {j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            for i in range(len(alignmentsY)):
                for j in range(self.general.nstoreys):
                    self.beamY.ficornerTOP[f'{i}, {j}'], self.beamY.ncornerTOP[f'{i}, {j}'], self.beamY.fiintTOP[f'{i}, {j}'], self.beamY.nintTOP[f'{i}, {j}'], self.beamY.ficornerBOT[f'{i}, {j}'], self.beamY.ncornerBOT[f'{i}, {j}'], self.beamY.fiintBOT[f'{i}, {j}'], self.beamY.nintBOT[f'{i}, {j}'], self.beamY.fiw[f'{i}, {j}'], self.beamY.sw[f'{i}, {j}'], self.beamY.nwparallel_to_b[f'{i}, {j}'], self.beamY.nwparallel_to_h[f'{i}, {j}'] = _get_beam_rebars(NeededAsBOTY[f'{i}, {j}'], NeededAsTOPY[f'{i}, {j}'], self.beamY.BB[f'{i}, {j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sY[f'{i}, {j}'], swmax_Y[f'{i}, {j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            for j in range(self.general.nstoreys):
                self.beamStair.ficornerTOP[f'{j}'], self.beamStair.ncornerTOP[f'{j}'], self.beamStair.fiintTOP[f'{j}'], self.beamStair.nintTOP[f'{j}'], self.beamStair.ficornerBOT[f'{j}'], self.beamStair.ncornerBOT[f'{j}'], self.beamStair.fiintBOT[f'{j}'], self.beamStair.nintBOT[f'{j}'], self.beamStair.fiw[f'{j}'], self.beamStair.sw[f'{j}'], self.beamStair.nwparallel_to_b[f'{j}'], self.beamStair.nwparallel_to_h[f'{j}'] = _get_beam_rebars(NeededAsBOTStair[f'{j}'], NeededAsTOPStair[f'{j}'], self.beamStair.BB[f'{j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sStair[f'{j}'], swmax_Stair[f'{j}'], sw_min_over_fi, dmin) 
            # uniformize the number of rebars at each common section 
            # (section 9 from  previous to 1 from next) at the same alignment 
            # -xx (HMA)
            attributes = ['BBbb', 'DDdd']
            for attr in attributes:
                val = {f'{j}, {i}':None for i in range(len(alignmentsX)) for j in range(self.general.nstoreys)}
                setattr(self.beamX, attr, val)
                val = {f'{j}, {i}':None for i in range(len(alignmentsY)) for j in range(self.general.nstoreys)}
                setattr(self.beamY, attr, val)

            for j in range(self.general.nstoreys): # loop over the storeys
                for i in range(len(alignmentsX)): # loop over the alignment
                    aa = self.beamX.ncornerTOP[f'{i}, {j}']
                    bb = self.beamX.nintTOP[f'{i}, {j}']
                    cc = self.beamX.ncornerBOT[f'{i}, {j}']
                    dd = self.beamX.nintBOT[f'{i}, {j}']
                    for kk in range(2, len(dd)-3, 3):
                        aa[kk] = max(aa[kk], aa[kk+1])
                        aa[kk+1] = max(aa[kk], aa[kk+1])
                        bb[kk] = max(bb[kk], bb[kk+1])
                        bb[kk+1] = max(bb[kk], bb[kk+1])
                        cc[kk] = max(cc[kk], cc[kk+1])
                        cc[kk+1] = max(cc[kk], cc[kk+1])
                        dd[kk] = max(dd[kk], dd[kk+1])
                        dd[kk+1] = max(dd[kk], dd[kk+1])

                    self.beamX.ncornerTOP[f'{i}, {j}'] = aa.copy()
                    self.beamX.nintTOP[f'{i}, {j}'] = bb.copy()
                    self.beamX.ncornerBOT[f'{i}, {j}'] = cc.copy()
                    self.beamX.nintBOT[f'{i}, {j}'] = dd.copy()
                    self.beamX.BBbb[f'{i}, {j}'] = bb.copy()
                    self.beamX.DDdd[f'{i}, {j}'] = dd.copy()

            # -yy (HMA)
            for j in range(self.general.nstoreys): # loop over the storeys
                for i in range(len(alignmentsY)): # loop over the alignement
                    aa = self.beamY.ncornerTOP[f'{i}, {j}']
                    bb = self.beamY.nintTOP[f'{i}, {j}']
                    cc = self.beamY.ncornerBOT[f'{i}, {j}']
                    dd = self.beamY.nintBOT[f'{i}, {j}']
                    for kk in range(2, len(dd)-3, 3):
                        aa[kk] = max(aa[kk], aa[kk+1])
                        aa[kk+1] = max(aa[kk], aa[kk+1])
                        bb[kk] = max(bb[kk], bb[kk+1])
                        bb[kk+1] = max(bb[kk], bb[kk+1])
                        cc[kk] = max(cc[kk], cc[kk+1])
                        cc[kk+1] = max(cc[kk], cc[kk+1])
                        dd[kk] = max(dd[kk], dd[kk+1])
                        dd[kk+1] = max(dd[kk], dd[kk+1])

                    self.beamY.ncornerTOP[f'{i}, {j}'] = aa.copy()
                    self.beamY.nintTOP[f'{i}, {j}'] = bb.copy()
                    self.beamY.ncornerBOT[f'{i}, {j}'] = cc.copy()
                    self.beamY.nintBOT[f'{i}, {j}'] = dd.copy()
                    self.beamY.BBbb[f'{i}, {j}'] = bb.copy()
                    self.beamY.DDdd[f'{i}, {j}'] = dd.copy()
            # ...........................................................................
            # Calculation of My for the beams in -XX
            # ...........................................................................
            fsyd = sigmas + 0
            fcd = sigmac + 0
            neles = len(self.beamX.Area.flatten())
            pedXEQ = self.beamX.pedEQFinal.copy()
            pedXEQ[-1, :] = self.beamX.proofEQFinal[-1, :]
            pedXEQ = pedXEQ.flatten()
            self.beamX.Matrix = np.zeros((neles, 42))
            iele  = 0
            for j in range(self.general.nstoreys): # loop over the storeys
                auxMyPos = np.array([])
                auxMyNeg = np.array([])
                for i in range(len(alignmentsX)): # loop over the alignment
                    namesly = self.beamX.NName[f'{i}, {j}']
                    nodeily = self.beamX.NNodei[f'{i}, {j}']
                    nodejly = self.beamX.NNodej[f'{i}, {j}']
                    HHly    = self.beamX.HH[f'{i}, {j}']
                    BBly    = self.beamX.BB[f'{i}, {j}']
                    LLly    = self.beamX.LL[f'{i}, {j}']
                    Ntopc   = self.beamX.ncornerTOP[f'{i}, {j}']
                    Ftopc   = self.beamX.ficornerTOP[f'{i}, {j}']
                    Ntopi   = self.beamX.nintTOP[f'{i}, {j}']
                    Ftopi   = self.beamX.fiintTOP[f'{i}, {j}']
                    Nbotc   = self.beamX.ncornerBOT[f'{i}, {j}']
                    Fbotc   = self.beamX.ficornerBOT[f'{i}, {j}']
                    Nboti   = self.beamX.nintBOT[f'{i}, {j}']
                    Fboti   = self.beamX.fiintBOT[f'{i}, {j}']
                    fiw     = self.beamX.fiw[f'{i}, {j}']
                    sw      = self.beamX.sw[f'{i}, {j}']
                    nwparallel_to_b = self.beamX.nwparallel_to_b[f'{i}, {j}']
                    nwparallel_to_h = self.beamX.nwparallel_to_h[f'{i}, {j}']
                    # ...........................................................................
                    dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                    dD_line  = 1000 * HHly - dD                                                               # in mm
                    cB       = (epscU * dD) / (epscU + esy)
                    Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    Ec       = (57000 * (fcd * 145)**0.5) / 145
                    Es       = 200000
                    nyoung   = Es / Ec
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control = np.ones(dD.shape)
                    AtoUse  = AtensCntrl + 0
                    BtoUse  = BtensCntrl + 0
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control[cC < cB] = 1
                    AtoUse[cC < cB] = AtensCntrl[cC < cB]
                    BtoUse[cC < cB] = BtensCntrl[cC < cB]
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    nameslyuni = np.unique(namesly)
                    for kk in range(len(nameslyuni)):
                        indexly = np.where(namesly==nameslyuni[kk])[0]
                        self.beamX.Matrix[iele, 0] = namesly[indexly[0]]
                        self.beamX.Matrix[iele, 1] = nodeily[indexly[0]]
                        self.beamX.Matrix[iele, 2] = nodejly[indexly[0]]
                        self.beamX.Matrix[iele, 3] = BBly[indexly[0]]
                        self.beamX.Matrix[iele, 4] = HHly[indexly[0]]
                        self.beamX.Matrix[iele, 5] = LLly[indexly[0]]
                        self.beamX.Matrix[iele, 6] = Ntopc[indexly[0]]
                        self.beamX.Matrix[iele, 7] = Ntopc[indexly[-1]]
                        self.beamX.Matrix[iele, 8] = Ftopc[indexly[0]]
                        self.beamX.Matrix[iele, 9] = Ftopc[indexly[-1]]
                        self.beamX.Matrix[iele, 10] = Nbotc[indexly[0]]
                        self.beamX.Matrix[iele, 11] = Nbotc[indexly[-1]]
                        self.beamX.Matrix[iele, 12] = Fbotc[indexly[0]]
                        self.beamX.Matrix[iele, 13] = Fbotc[indexly[-1]]
                        self.beamX.Matrix[iele, 14] = fiw[indexly[0]]
                        self.beamX.Matrix[iele, 15] = sw[indexly[0]]
                        self.beamX.Matrix[iele, 16] = nwparallel_to_b[indexly[0]]
                        self.beamX.Matrix[iele, 17] = nwparallel_to_h[indexly[0]]
                        self.beamX.Matrix[iele, 18] = fiw[indexly[-1]]
                        self.beamX.Matrix[iele, 19] = sw[indexly[-1]]
                        self.beamX.Matrix[iele, 20] = nwparallel_to_b[indexly[-1]]
                        self.beamX.Matrix[iele, 21] = nwparallel_to_h[indexly[-1]]
                        self.beamX.Matrix[iele, 22] = Ntopi[indexly[0]]
                        self.beamX.Matrix[iele, 23] = Ntopi[indexly[-1]]
                        self.beamX.Matrix[iele, 24] = Ftopi[indexly[0]]
                        self.beamX.Matrix[iele, 25] = Ftopi[indexly[-1]]
                        self.beamX.Matrix[iele, 26] = Nboti[indexly[0]]
                        self.beamX.Matrix[iele, 27] = Nboti[indexly[-1]]
                        self.beamX.Matrix[iele, 28] = Fboti[indexly[0]]
                        self.beamX.Matrix[iele, 29] = Fboti[indexly[-1]]
                        self.beamX.Matrix[iele, 30] = MyNeg[indexly[0]]
                        self.beamX.Matrix[iele, 31] = MyPos[indexly[0]]
                        self.beamX.Matrix[iele, 32] = MyNeg[indexly[-1]]
                        self.beamX.Matrix[iele, 33] = MyPos[indexly[-1]]
                        
                        iele += 1                   

                    auxMyPos = np.append(auxMyPos, np.concatenate(([0], MyPos[2:-3:3], [0])))
                    auxMyNeg = np.append(auxMyNeg, np.concatenate(([MyNeg[0]], MyNeg[2:-3:3], [MyNeg[-1]])))

                if not hasattr(self.beamX, 'MyPos'):
                    self.beamX.MyPos = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamX.MyNeg = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamX.sumMrd = np.zeros((self.general.nstoreys, len(auxMyPos)))

                self.beamX.MyPos[j, :] = auxMyPos
                self.beamX.MyNeg[j, :] = auxMyNeg
                self.beamX.sumMrd[j, :] = auxMyPos + auxMyNeg

            self.beamX.Matrix[:, 41] = pedXEQ
            # ...........................................................................
            # Calculation of My for the beams in -YY
            # ...........................................................................
            neles = len(self.beamY.Area.flatten())
            pedYEQ = self.beamY.pedEQFinal.copy()
            pedYEQ[-1, :] = self.beamY.proofEQFinal[-1, :]
            pedYEQ = pedYEQ.flatten()
            self.beamY.Matrix = np.zeros((neles, 42))
            iele  = 0
            for j in range(self.general.nstoreys): # loop over the storeys
                auxMyPos = np.array([])
                auxMyNeg = np.array([])
                for i in range(len(alignmentsY)): # loop over the alignment
                    namesly = self.beamY.NName[f'{i}, {j}']
                    nodeily = self.beamY.NNodei[f'{i}, {j}']
                    nodejly = self.beamY.NNodej[f'{i}, {j}']
                    HHly    = self.beamY.HH[f'{i}, {j}']
                    BBly    = self.beamY.BB[f'{i}, {j}']
                    LLly    = self.beamY.LL[f'{i}, {j}']
                    Ntopc   = self.beamY.ncornerTOP[f'{i}, {j}']
                    Ftopc   = self.beamY.ficornerTOP[f'{i}, {j}']
                    Ntopi   = self.beamY.nintTOP[f'{i}, {j}']
                    Ftopi   = self.beamY.fiintTOP[f'{i}, {j}']
                    Nbotc   = self.beamY.ncornerBOT[f'{i}, {j}']
                    Fbotc   = self.beamY.ficornerBOT[f'{i}, {j}']
                    Nboti   = self.beamY.nintBOT[f'{i}, {j}']
                    Fboti   = self.beamY.fiintBOT[f'{i}, {j}']
                    fiw     = self.beamY.fiw[f'{i}, {j}']
                    sw      = self.beamY.sw[f'{i}, {j}']
                    nwparallel_to_b = self.beamY.nwparallel_to_b[f'{i}, {j}']
                    nwparallel_to_h = self.beamY.nwparallel_to_h[f'{i}, {j}']
                    # ...........................................................................
                    dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                    dD_line  = 1000 * HHly - dD                                                               # in mm
                    cB       = (epscU * dD) / (epscU + esy)
                    Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    Ec       = (57000 * (fcd * 145)**0.5) / 145
                    Es       = 200000
                    nyoung   = Es / Ec
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control = np.ones(dD.shape)
                    AtoUse  = AtensCntrl + 0
                    BtoUse  = BtensCntrl + 0
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control[cC < cB] = 1
                    AtoUse[cC < cB] = AtensCntrl[cC < cB]
                    BtoUse[cC < cB] = BtensCntrl[cC < cB]
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    nameslyuni = np.unique(namesly)
                    for kk in range(len(nameslyuni)):
                        indexly = np.where(namesly==nameslyuni[kk])[0]
                        self.beamY.Matrix[iele, 0] = namesly[indexly[0]]
                        self.beamY.Matrix[iele, 1] = nodeily[indexly[0]]
                        self.beamY.Matrix[iele, 2] = nodejly[indexly[0]]
                        self.beamY.Matrix[iele, 3] = BBly[indexly[0]]
                        self.beamY.Matrix[iele, 4] = HHly[indexly[0]]
                        self.beamY.Matrix[iele, 5] = LLly[indexly[0]]
                        self.beamY.Matrix[iele, 6] = Ntopc[indexly[0]]
                        self.beamY.Matrix[iele, 7] = Ntopc[indexly[-1]]
                        self.beamY.Matrix[iele, 8] = Ftopc[indexly[0]]
                        self.beamY.Matrix[iele, 9] = Ftopc[indexly[-1]]
                        self.beamY.Matrix[iele, 10] = Nbotc[indexly[0]]
                        self.beamY.Matrix[iele, 11] = Nbotc[indexly[-1]]
                        self.beamY.Matrix[iele, 12] = Fbotc[indexly[0]]
                        self.beamY.Matrix[iele, 13] = Fbotc[indexly[-1]]
                        self.beamY.Matrix[iele, 14] = fiw[indexly[0]]
                        self.beamY.Matrix[iele, 15] = sw[indexly[0]]
                        self.beamY.Matrix[iele, 16] = nwparallel_to_b[indexly[0]]
                        self.beamY.Matrix[iele, 17] = nwparallel_to_h[indexly[0]]
                        self.beamY.Matrix[iele, 18] = fiw[indexly[-1]]
                        self.beamY.Matrix[iele, 19] = sw[indexly[-1]]
                        self.beamY.Matrix[iele, 20] = nwparallel_to_b[indexly[-1]]
                        self.beamY.Matrix[iele, 21] = nwparallel_to_h[indexly[-1]]
                        self.beamY.Matrix[iele, 22] = Ntopi[indexly[0]]
                        self.beamY.Matrix[iele, 23] = Ntopi[indexly[-1]]
                        self.beamY.Matrix[iele, 24] = Ftopi[indexly[0]]
                        self.beamY.Matrix[iele, 25] = Ftopi[indexly[-1]]
                        self.beamY.Matrix[iele, 26] = Nboti[indexly[0]]
                        self.beamY.Matrix[iele, 27] = Nboti[indexly[-1]]
                        self.beamY.Matrix[iele, 28] = Fboti[indexly[0]]
                        self.beamY.Matrix[iele, 29] = Fboti[indexly[-1]]
                        self.beamY.Matrix[iele, 30] = MyNeg[indexly[0]]
                        self.beamY.Matrix[iele, 31] = MyPos[indexly[0]]
                        self.beamY.Matrix[iele, 32] = MyNeg[indexly[-1]]
                        self.beamY.Matrix[iele, 33] = MyPos[indexly[-1]]
                        
                        iele += 1                   

                    auxMyPos = np.append(auxMyPos, np.concatenate(([0], MyPos[2:-3:3], [0])))
                    auxMyNeg = np.append(auxMyNeg, np.concatenate(([MyNeg[0]], MyNeg[2:-3:3], [MyNeg[-1]])))

                if not hasattr(self.beamY, 'MyPos'):
                    self.beamY.MyPos = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.MyNeg = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.sumMrd = np.zeros((self.general.nstoreys, len(auxMyPos)))

                self.beamY.MyPos[j, :] = auxMyPos
                self.beamY.MyNeg[j, :] = auxMyNeg
                self.beamY.sumMrd[j, :] = auxMyPos + auxMyNeg

            self.beamY.Matrix[:, 41] = pedYEQ
            # ...........................................................................
            # Calculation of My for the beams in Stairs
            # ...........................................................................
            neles = len(self.beamStair.Area.flatten())
            pedStairEQ = self.beamStair.pedEQFinal.copy()
            pedStairEQ = pedStairEQ.flatten()
            self.beamStair.Matrix = np.zeros((neles, 42))
            iele  = 0
            auxMyPos = np.array([])
            auxMyNeg = np.array([])
            for j in range(self.general.nstoreys):
                namesly = self.beamStair.NName[f'{j}']
                nodeily = self.beamStair.NNodei[f'{j}']
                nodejly = self.beamStair.NNodej[f'{j}']
                HHly    = self.beamStair.HH[f'{j}']
                BBly    = self.beamStair.BB[f'{j}']
                LLly    = self.beamStair.LL[f'{j}']
                Ntopc   = self.beamStair.ncornerTOP[f'{j}']
                Ftopc   = self.beamStair.ficornerTOP[f'{j}']
                Ntopi   = self.beamStair.nintTOP[f'{j}']
                Ftopi   = self.beamStair.fiintTOP[f'{j}']
                Nbotc   = self.beamStair.ncornerBOT[f'{j}']
                Fbotc   = self.beamStair.ficornerBOT[f'{j}']
                Nboti   = self.beamStair.nintBOT[f'{j}']
                Fboti   = self.beamStair.fiintBOT[f'{j}']
                fiw     = self.beamStair.fiw[f'{j}']
                sw      = self.beamStair.sw[f'{j}']
                nwparallel_to_b = self.beamStair.nwparallel_to_b[f'{j}']
                nwparallel_to_h = self.beamStair.nwparallel_to_h[f'{j}']
                # ...........................................................................
                dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                dD_line  = 1000 * HHly - dD                                                               # in mm
                cB       = (epscU * dD) / (epscU + esy)
                Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                rostens  = Astens / (BBly * 1000 * dD)
                As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                ros_line = As_line / (BBly * 1000 * dD)
                cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                Ec       = (57000 * (fcd * 145)**0.5) / 145
                Es       = 200000
                nyoung   = Es / Ec
                AcomprCntrl = rostens + ros_line
                AtensCntrl  = rostens + ros_line
                BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                Control = np.ones(dD.shape)
                AtoUse  = AtensCntrl + 0
                BtoUse  = BtensCntrl + 0
                Control[cC >= cB] = 0
                AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                fiy = fiy1 + 0
                fiy[Control==0] = fiy2[Control==0]
                Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                # ...........................................................................
                Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                rostens  = Astens / (BBly * 1000 * dD)
                As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                ros_line = As_line / (BBly * 1000 * dD)
                cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                AcomprCntrl = rostens + ros_line
                AtensCntrl  = rostens + ros_line
                BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                Control[cC < cB] = 1
                AtoUse[cC < cB] = AtensCntrl[cC < cB]
                BtoUse[cC < cB] = BtensCntrl[cC < cB]
                Control[cC >= cB] = 0
                AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                fiy = fiy1 + 0
                fiy[Control==0] = fiy2[Control==0]
                Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                # ...........................................................................
                self.beamStair.Matrix[iele, 0] = namesly[0]
                self.beamStair.Matrix[iele, 1] = nodeily[0]
                self.beamStair.Matrix[iele, 2] = nodejly[0]
                self.beamStair.Matrix[iele, 3] = BBly[0]
                self.beamStair.Matrix[iele, 4] = HHly[0]
                self.beamStair.Matrix[iele, 5] = LLly[0]
                self.beamStair.Matrix[iele, 6] = Ntopc[0]
                self.beamStair.Matrix[iele, 7] = Ntopc[-1]
                self.beamStair.Matrix[iele, 8] = Ftopc[0]
                self.beamStair.Matrix[iele, 9] = Ftopc[-1]
                self.beamStair.Matrix[iele, 10] = Nbotc[0]
                self.beamStair.Matrix[iele, 11] = Nbotc[-1]
                self.beamStair.Matrix[iele, 12] = Fbotc[0]
                self.beamStair.Matrix[iele, 13] = Fbotc[-1]
                self.beamStair.Matrix[iele, 14] = fiw[0]
                self.beamStair.Matrix[iele, 15] = sw[0]
                self.beamStair.Matrix[iele, 16] = nwparallel_to_b[0]
                self.beamStair.Matrix[iele, 17] = nwparallel_to_h[0]
                self.beamStair.Matrix[iele, 18] = fiw[-1]
                self.beamStair.Matrix[iele, 19] = sw[-1]
                self.beamStair.Matrix[iele, 20] = nwparallel_to_b[-1]
                self.beamStair.Matrix[iele, 21] = nwparallel_to_h[-1]
                self.beamStair.Matrix[iele, 22] = Ntopi[0]
                self.beamStair.Matrix[iele, 23] = Ntopi[-1]
                self.beamStair.Matrix[iele, 24] = Ftopi[0]
                self.beamStair.Matrix[iele, 25] = Ftopi[-1]
                self.beamStair.Matrix[iele, 26] = Nboti[0]
                self.beamStair.Matrix[iele, 27] = Nboti[-1]
                self.beamStair.Matrix[iele, 28] = Fboti[0]
                self.beamStair.Matrix[iele, 29] = Fboti[-1]
                self.beamStair.Matrix[iele, 30] = MyNeg[0]
                self.beamStair.Matrix[iele, 31] = MyPos[0]
                self.beamStair.Matrix[iele, 32] = MyNeg[-1]
                self.beamStair.Matrix[iele, 33] = MyPos[-1]
                iele += 1                   

                if not hasattr(self.beamStair, 'MyPos'):
                    self.beamStair.MyPos = np.zeros((self.general.nstoreys, 2))
                    self.beamStair.MyNeg = np.zeros((self.general.nstoreys, 2))
                    self.beamStair.sumMrd = np.zeros((self.general.nstoreys, 2))

                self.beamStair.MyPos[j, :] = np.array([0, 0])
                self.beamStair.MyNeg[j, :] = MyNeg[[0,2]]
                self.beamStair.sumMrd[j, :]= self.beamStair.MyPos[j, :] + self.beamStair.MyNeg[j, :]

            self.beamStair.Matrix[:, 41] = pedStairEQ

        return CvFLAGX, CvFLAGY, CvFLAGStair, auxbeam

    def _cdl_columns(self, auxbeam):
        """
        Designs columns usign DCL1 properties
        Refrences: REBA, 1967 + RSCSS 1958 
        --> French book followed by the most of EUROPE
        Seismic loading is considered with q=1.0, 1.0 DEAD + 1.0 LIVE
        Design based on ultimate strength analysis

        Args:
            auxbeam (float): auxiliary variable describing the number of beams that do not satisfy design requirements
        """
        # ...........................................................................
        # General Material Propeties
        # ...........................................................................
        miueconomic = 0.25
        fckvect = [180, 225, 300, 350, 400]
        tau1vect = [0.4, 0.45, 0.50, 0.55, 0.60]
        tausmaxvect = [2.4, 2.7, 3.0, 3.3, 3.6]
        n = 15

        tau1 = 1000 * np.interp(self.general.fckcube, fckvect, tau1vect)
        taumax = 1000 * np.interp(self.general.fckcube, fckvect, tausmaxvect)
        dmin = 0.035
        dmax = 0.350
        sw_min_over_fi = 12.00
        cover = 0.030
        if self.general.fckcube <= 180:
            rho_max = 0.03
        elif self.general.fckcube <= 225:
            rho_max = 0.04
        elif self.general.fckcube <= 300:
            rho_max = 0.05
        elif self.general.fckcube <= 350:
            rho_max = 0.06
        elif self.general.fckcube <= 400:
            rho_max = 0.06
        rho_min = 0.01 * 0.66  # REBA, 1967; Portugal; assuming the area of core concrete = 80% total area of the section (0.81HX*0.81HY)/(HX*HY)
        fiw_min = 0.006
        # ...........................................................................
        # Sets the maximum column dimensions
        # ...........................................................................
        if self.general.ColumnType == 1:
            self.column.maxH = self.column.maxHsquared + 0
        else:
            self.column.maxH = self.column.maxHrectangular + 0
        # ...........................................................................
        # Variables for the design based on the DCL Design Routines
        # ...........................................................................
        Combinations_2_use = [i for i in range(6)]
        MMMX1 = [self.column.MuX1[comb] for comb in Combinations_2_use]
        MMMY1 = [self.column.MuY1[comb] for comb in Combinations_2_use]
        MMMX9 = [self.column.MuX9[comb] for comb in Combinations_2_use]
        MMMY9 = [self.column.MuY9[comb] for comb in Combinations_2_use]
        # ...........................................................................
        TTTX1 = [self.column.tauX1[comb] for comb in Combinations_2_use]
        TTTY1 = [self.column.tauY1[comb] for comb in Combinations_2_use]
        TTTX9 = [self.column.tauX9[comb] for comb in Combinations_2_use]
        TTTY9 = [self.column.tauY9[comb] for comb in Combinations_2_use]
        # ...........................................................................
        NNN1 = [self.column.Niu1[comb] for comb in Combinations_2_use]
        NNN9 = [self.column.Niu9[comb] for comb in Combinations_2_use]  # Fixed the in original version, Niu1 was being used.
        # ...........................................................................
        MuX1_maxo = np.max(np.array(MMMX1), axis=0)
        MuX9_maxo = np.max(np.array(MMMX9), axis=0)
        MuY1_maxo = np.max(np.array(MMMY1), axis=0)
        MuY9_maxo = np.max(np.array(MMMY9), axis=0)
        MuXmax = np.maximum(MuX1_maxo, MuX9_maxo)
        MuYmax = np.maximum(MuY1_maxo, MuY9_maxo)
        # ...........................................................................
        tauX1_maxo = np.max(np.array(TTTX1), axis=0)
        tauX9_maxo = np.max(np.array(TTTX9), axis=0)
        tauY1_maxo = np.max(np.array(TTTY1), axis=0)
        tauY9_maxo = np.max(np.array(TTTY9), axis=0)
        tauXmax = np.maximum(tauX1_maxo, tauX9_maxo) / 0.90 # because taumax > Ved/(B*z) => taumax > (Ved/(B*d))*(1/0.90)
        tauYmax = np.maximum(tauY1_maxo, tauY9_maxo) / 0.90 # because taumax > Ved/(B*z) => taumax > (Ved/(B*d))*(1/0.90)
        # ...........................................................................
        Niu1_maxo = np.max(np.array(NNN1), axis=0)
        Niu9_maxo = np.max(np.array(NNN9), axis=0)
        Niumax = np.maximum(Niu1_maxo, Niu9_maxo)
        # ...........................................................................
        CpFLAGX = np.zeros(self.column.name.shape)
        CpFLAGY = np.zeros(self.column.name.shape)
        CpFLAGN = np.zeros(self.column.name.shape)
        CpFLAGX[tauXmax > taumax] = 1
        CpFLAGX[MuXmax > miueconomic] = 1
        CpFLAGY[tauYmax > taumax] = 1
        CpFLAGY[MuYmax > miueconomic] = 1
        CpFLAGN[Niumax > 0.50] = 1
        # ...........................................................................
        # Variables for the design based on the DCL Design Routines
        # ...........................................................................
        if np.max(self.column.HX) > self.column.maxH or np.max(self.column.HY) > self.column.maxH:
            CpFLAGfc = 222
            if self.general.fsyk == 240:
                self.general.fsyk = 400
                self.general.fsyd = 240
                self.general.fsydEQ = 400
                self.general.fck = self.general.fckgrav.copy()
                self.general.fckcube = self.general.fckcubegrav.copy()
                self.general.fcd = self.general.fcdgrav.copy()
                self.general.fcdEQ = self.general.fcdEQgrav.copy()
            elif self.general.fckcube == 180: # fckcube is in kg/cm2 because of the design formula
                self.general.fck = 19
                self.general.fckcube = 225 
                self.general.fcd = 8.50
                self.general.fcdEQ = 11.90
            elif self.general.fckcube == 225:
                self.general.fck = 25
                self.general.fckcube = 300
                self.general.fcd = 11.50
                self.general.fcdEQ = 17.50
            elif self.general.fsyk == 400:
                self.general.fsyk = 500
                self.general.fsyd = 300
                self.general.fsydEQ = 500
                self.general.fck = self.general.fckgrav.copy()
                self.general.fckcube = self.general.fckcubegrav.copy()
                self.general.fcd = self.general.fcdgrav.copy()
                self.general.fcdEQ = self.general.fcdEQgrav.copy()
            elif self.general.fsyk == 500:
                if self.general.ColumnType == 2 and self.general.ColITER == 0:
                    CpFLAGfc = 333 # changing to square columns from rectangular columns
                    self.general.ColITER = 1
                else:
                    CpFLAGfc = 1
        else: # check_Column_dims.m --> TODO: What do we do here?
            CpFLAGfc = 0
            aucx = np.where(self.column.Astair[0, :] > 0)[0]
            for i in range(self.general.nstoreys):
                CpFLAGX[i, aucx[0]] = max(CpFLAGX[i, aucx[0]], CpFLAGX[i, aucx[1]])
                CpFLAGY[i, aucx[0]] = max(CpFLAGY[i, aucx[0]], CpFLAGY[i, aucx[1]])
                CpFLAGX[i, aucx[1]] = CpFLAGX[i, aucx[0]].copy()
                CpFLAGY[i, aucx[1]] = CpFLAGY[i, aucx[0]].copy()
                CpFLAGX[i, aucx[2]] = max(CpFLAGX[i, aucx[2]], CpFLAGX[i, aucx[3]])
                CpFLAGY[i, aucx[2]] = max(CpFLAGY[i, aucx[2]], CpFLAGY[i, aucx[3]])
                CpFLAGX[i, aucx[3]] = CpFLAGX[i, aucx[2]].copy()
                CpFLAGY[i, aucx[3]] = CpFLAGY[i, aucx[2]].copy()
        # ...........................................................................
        # Checks if the design should be finished or not
        # ...........................................................................
        aux = np.sum(CpFLAGY) + np.sum(CpFLAGX) + auxbeam
        if aux > 0.99:
            print('Columns Not OK.... still %d to change!' % int(np.sum(CpFLAGY) + np.sum(CpFLAGX)))
            print('Maximum HX is %4.6f...' % float(np.max(np.max(self.column.HX))))
            print('Maximum HY is %4.6f...' % float(np.max(np.max(self.column.HY))))
            print('Minimum HX is %4.6f...' % float(np.min(np.min(self.column.HX))))
            print('Minimum HY is %4.6f...' % float(np.min(np.min(self.column.HY))))
            print('Maximum HX2 is %4.6f...' % float(np.max(np.max(self.column.HX[0, self.column.Colindex1]))))
            print('Maximum HY2 is %4.6f...' % float(np.max(np.max(self.column.HY[0, self.column.Colindex2]))))
            print('Minimum HX2 is %4.6f...' % float(np.min(np.min(self.column.HX[0, self.column.Colindex1]))))
            print('Minimum HY2 is %4.6f...' % float(np.min(np.min(self.column.HY[0, self.column.Colindex2]))))
        else:
            print('Column Geometry OK!')
            # ...........................................................................
            # Determination of the necessary reinforcement
            # ...........................................................................
            AsX = []
            AsY = []
            AsX_sw = []
            AsY_sw = []
            HX = self.column.HX.copy()
            HY = self.column.HY.copy()
            As_sw_rational = 2* np.pi * 0.25 * (0.006**2) / 0.3 # It is two legs stirrups with 6 mm diameter and sw equals to 0.30 m
            for i, icomb in enumerate(Combinations_2_use):
                if icomb < 2:
                    sigmacEQ = self.general.fcd + 0
                    sigmasEQ = self.general.fsyd + 0
                else:
                    sigmacEQ = self.general.fcdEQ + 0
                    sigmasEQ = self.general.fsydEQ + 0
                # ...........................................................................
                # Determination of the necessary longitudinal rebar area
                # ...........................................................................
                N1 = -1 * self.column.N1[icomb]
                MX1 = np.abs(self.column.M1_y[icomb])
                VX1 = np.abs(self.column.V1_x[icomb])
                MY1 = np.abs(self.column.M1_z[icomb])
                VY1 = np.abs(self.column.V1_y[icomb])
                N9 = -1 * self.column.N9[icomb]
                MX9 = np.abs(self.column.M9_y[icomb])
                VX9 = np.abs(self.column.V9_x[icomb])
                MY9 = np.abs(self.column.M9_z[icomb])
                VY9 = np.abs(self.column.V9_y[icomb])
                Ned1 = self.column.N1[icomb].copy()
                Ned9 = self.column.N1[icomb].copy()
                e_t_x1 = self.column.eccX1[icomb] / (HX - 2*cover) # TO define big and small ecc. section for tensile force to discard concrete contribution for small ecc. (HMA)
                e_t_x9 = self.column.eccX9[icomb] / (HX - 2*cover) # TO define big and small ecc. section for tensile force to discard concrete contribution for small ecc. (HMA)
                e_t_y1 = self.column.eccY1[icomb] / (HY - 2*cover) # TO define big and small ecc. section for tensile force to discard concrete contribution for small ecc. (HMA)
                e_t_y9 = self.column.eccY9[icomb] / (HY - 2*cover) # TO define big and small ecc. section for tensile force to discard concrete contribution for small ecc. (HMA)
                # ...........................................................................
                muX1 = MX1 / (sigmacEQ * 1000 * HY * HX**2)
                muY1 = MY1 / (sigmacEQ * 1000 * HX * HY**2)
                niu1 =  N1 / (sigmacEQ * 1000 * HX * HY)
                # ...........................................................................
                muX9 = MX9 / (sigmacEQ * 1000 * HY * HX**2)
                muY9 = MY9 / (sigmacEQ * 1000 * HX * HY**2)
                niu9 =  N9 / (sigmacEQ * 1000 * HX * HY)
                RhoX1 = np.zeros(niu1.shape)
                RhoY1 = np.zeros(niu1.shape)
                RhoX9 = np.zeros(niu1.shape)
                RhoY9 = np.zeros(niu1.shape)
                for jj in range(niu1.shape[0]):
                    for kk in range(niu1.shape[1]):
                        RhoX1[jj, kk], RhoY1[jj, kk] = _get_rosh_guerrin(niu1[jj, kk], muX1[jj, kk], muY1[jj, kk], sigmacEQ, sigmasEQ)
                        RhoX9[jj, kk], RhoY9[jj, kk] = _get_rosh_guerrin(niu9[jj, kk], muX9[jj, kk], muY9[jj, kk], sigmacEQ, sigmasEQ)
                # Convert nan to zero --> Python gives error while using NaN, MATLAB does not.
                # TODO: Maybe use extrapolation instead after validation with MATLAB is complete.
                RhoX1 = np.nan_to_num(RhoX1, nan=As_sw_rational)
                RhoY1 = np.nan_to_num(RhoY1, nan=As_sw_rational)
                RhoX9 = np.nan_to_num(RhoX9, nan=As_sw_rational)
                RhoY9 = np.nan_to_num(RhoY9, nan=As_sw_rational)
                # ...........................................................................
                AsXPos1 = 0.50 * RhoX1 * (HY * HX) / n
                AsYPos1 = 0.50 * RhoY1 * (HY * HX) / n
                AsXPos9 = 0.50 * RhoX9 * (HY * HX) / n
                AsYPos9 = 0.50 * RhoY9 * (HY * HX) / n
                AsX.append(np.maximum(AsXPos1, AsXPos9))
                AsY.append(np.maximum(AsYPos1, AsYPos9))   
                # ...........................................................................
                # Determination of the necessary transversal rebar area
                # ...........................................................................
                VcdX = tau1 * HY * 0.9 * HX
                VcdY = tau1 * HX * 0.9 * HY
                Asw_sX1 = np.zeros(VcdX.shape)
                Asw_sX9 = np.zeros(VcdX.shape)
                Asw_sY1 = np.zeros(VcdX.shape)
                Asw_sY9 = np.zeros(VcdX.shape)
                for ii in range(VcdX.shape[0]):
                    for jj in range(VcdX.shape[1]):
                        # X direction ...........................................................................
                        # Section 1
                        if (1000.0 * max(AsXPos1[ii, jj], AsXPos9[ii, jj]) * self.general.fsyd * 0.9 * 0.9 * HX[ii, jj] < VcdX[ii, jj] * 0.9 * HX[ii, jj]) or (Ned1[ii, jj] > 0 and abs(e_t_x1[ii, jj]) < 0.5):
                            # criteria for ignoring the concrete contribution based on the longitudinal reinforcement and small eccentric tensile force (HMA)
                            Asw_sX1[ii, jj] = max((VX1[ii, jj]) / (0.9 * 0.9 * HX[ii, jj] * 1000 * sigmasEQ), As_sw_rational)
                        elif VX1[ii, jj] > VcdX[ii, jj]:
                            Asw_sX1[ii, jj] = max((VX1[ii, jj] - VcdX[ii, jj]) / (0.9 * 0.9 * HX[ii, jj] * 1000 * sigmasEQ), As_sw_rational)
                        else:
                            Asw_sX1[ii, jj] = As_sw_rational + 0 
                        # Section 9
                        if (1000.0 * max(AsXPos1[ii, jj], AsXPos9[ii, jj]) * self.general.fsyd * 0.9 * 0.9 * HX[ii, jj] < VcdX[ii, jj] * 0.9 * HX[ii, jj]) or (Ned9[ii, jj] > 0 and abs(e_t_x9[ii, jj]) < 0.5):
                            Asw_sX9[ii, jj] = max((VX9[ii, jj]) / (0.9 * 0.9 * HX[ii, jj] * 1000 * sigmasEQ), As_sw_rational)
                        elif VX1[ii, jj] > VcdX[ii, jj]:
                            Asw_sX9[ii, jj] = max((VX9[ii, jj] - VcdX[ii, jj]) / (0.9 * 0.9 * HX[ii, jj] * 1000 * sigmasEQ), As_sw_rational)
                        else:
                            Asw_sX9[ii, jj] = As_sw_rational + 0 
                        # Y direction ...........................................................................
                        # Section 1
                        if (1000.0 * max(AsYPos1[ii, jj], AsYPos9[ii, jj]) * self.general.fsyd * 0.9 * 0.9 * HY[ii, jj] < VcdY[ii, jj] * 0.9 * HY[ii, jj]) or (Ned1[ii, jj] > 0 and abs(e_t_y1[ii, jj]) < 0.5):
                            # criteria for ignoring the concrete contribution based on the longitudinal reinforcement and small eccentric tensile force (HMA)
                            Asw_sY1[ii, jj] = max((VY1[ii, jj]) / (0.9 * 0.9 * HY[ii, jj] * 1000 * sigmasEQ), As_sw_rational)
                        elif VY1[ii, jj] > VcdY[ii, jj]:
                            Asw_sY1[ii, jj] = max((VY1[ii, jj] - VcdY[ii, jj]) / (0.9 * 0.9 * HY[ii, jj] * 1000 * sigmasEQ), As_sw_rational)
                        else:
                            Asw_sY1[ii, jj] = As_sw_rational + 0 
                        # Section 9
                        if (1000.0 * max(AsYPos1[ii, jj], AsYPos9[ii, jj]) * self.general.fsyd * 0.9 * 0.9 * HY[ii, jj] < VcdY[ii, jj] * 0.9 * HY[ii, jj]) or (Ned9[ii, jj] > 0 and abs(e_t_y9[ii, jj]) < 0.5):
                            Asw_sY9[ii, jj] = max((VY9[ii, jj]) / (0.9 * 0.9 * HY[ii, jj] * 1000 * sigmasEQ), As_sw_rational)
                        elif VX1[ii, jj] > VcdX[ii, jj]:
                            Asw_sY9[ii, jj] = max((VY9[ii, jj] - VcdY[ii, jj]) / (0.9 * 0.9 * HY[ii, jj] * 1000 * sigmasEQ), As_sw_rational)
                        else:
                            Asw_sY9[ii, jj] = As_sw_rational + 0 

                AsX_sw.append(np.maximum(Asw_sX1, Asw_sX9))
                AsY_sw.append(np.maximum(Asw_sY1, Asw_sY9))
                
            self.column.AsX = np.max(np.array(AsX), axis=0)
            self.column.AsY = np.max(np.array(AsY), axis=0)
            self.column.AsX_sw = np.max(np.array(AsX_sw), axis=0)
            self.column.AsY_sw = np.max(np.array(AsY_sw), axis=0)
            sw_max = 1.0 * HX
            # ...........................................................................
            # Get the rebar solution
            # ...........................................................................
            attributes = ['fi_corner', 'fi_layintX', 'nbar_HminusX', 'nlayintX', 'Rhosl', 'RhoslX', 'RhoslY', 'nintBOT', 'sw', 'fiw', 'nwparallel_to_X', 'nwparallel_to_Y']
            for attr in attributes:
                setattr(self.column, attr, np.zeros(self.column.AsX.shape))
            for jj in range(self.column.AsX.shape[1]):
                self.column.fi_corner[:, jj], self.column.fi_layintX[:, jj], self.column.nbar_HminusX[:, jj], self.column.nlayintX[:, jj], self.column.Rhosl[:, jj], self.column.RhoslX[:, jj], self.column.RhoslY[:, jj], self.column.sw[:, jj], self.column.fiw[:, jj], self.column.nwparallel_to_X[:, jj], self.column.nwparallel_to_Y[:, jj] = _get_column_rebars(self.column.AsX[:, jj], self.column.AsY[:, jj], HX[:, jj], HY[:, jj], rho_min, dmin, dmax, cover, self.column.AsX_sw[:, jj], self.column.AsY_sw[:, jj], sw_min_over_fi, sw_max[:, jj], fiw_min)
            # ...........................................................................
            # Save stuff
            # ...........................................................................
            nrow = self.column.name.shape[0] * self.column.name.shape[1]
            ncol = 27
            self.column.Matrix = np.zeros((nrow, ncol))
            self.column.Matrix[:, 0] = (self.column.name.T).flatten()
            self.column.Matrix[:, 1] = (self.column.elasnodei.T).flatten() + 7000
            self.column.Matrix[:, 2] = (self.column.elasnodej.T).flatten() + 2000
            self.column.Matrix[:, 3] = (self.column.HX.T).flatten()
            self.column.Matrix[:, 4] = (self.column.HY.T).flatten()
            self.column.Matrix[:, 5] = (self.column.L.T).flatten()
            self.column.Matrix[:, 6] = (self.column.storey.T).flatten()
            self.column.Matrix[:, 7] = (self.column.perimeter.T).flatten()
            self.column.Matrix[:, 8] = (self.column.nbar_HminusX.T).flatten()
            self.column.Matrix[:, 9]  = (self.column.nlayintX.T).flatten()
            self.column.Matrix[:, 10]  = (self.column.fi_corner.T).flatten()
            self.column.Matrix[:, 11] = (self.column.fi_layintX.T).flatten()
            self.column.Matrix[:, 12] = (self.column.Rhosl.T).flatten()
            self.column.Matrix[:, 13] = (self.column.sw.T).flatten()
            self.column.Matrix[:, 14] = (self.column.fiw.T).flatten()
            self.column.Matrix[:, 15] = (self.column.nwparallel_to_X.T).flatten()
            self.column.Matrix[:, 16] = (self.column.nwparallel_to_Y.T).flatten()
            self.column.Matrix[:, 17] = (self.column.N_EQfinal.T).flatten()
            # ...........................................................................
            # Checking the maximum rho_l condition
            # ...........................................................................
            if np.max(self.column.Rhosl) > rho_max:
                aux1 = self.column.Rhosl > rho_max
                aux2 = self.column.Rhosl <= rho_max
                CpFLAGX[aux1] = 1
                CpFLAGX[aux2] = 0
                CpFLAGY[aux1] = 1
                CpFLAGY[aux2] = 0      

            aucx = np.where(self.column.Astair[0, :] > 0)[0]
            for i in range(self.general.nstoreys):
                CpFLAGX[i, aucx[0]] = max(CpFLAGX[i, aucx[0]], CpFLAGX[i, aucx[1]])
                CpFLAGY[i, aucx[0]] = max(CpFLAGY[i, aucx[0]], CpFLAGY[i, aucx[1]])
                CpFLAGX[i, aucx[1]] = CpFLAGX[i, aucx[0]]
                CpFLAGY[i, aucx[1]] = CpFLAGY[i, aucx[0]]
                CpFLAGX[i, aucx[2]] = max(CpFLAGX[i, aucx[2]], CpFLAGX[i, aucx[3]])
                CpFLAGY[i, aucx[2]] = max(CpFLAGY[i, aucx[2]], CpFLAGY[i, aucx[3]])
                CpFLAGX[i, aucx[3]] = CpFLAGX[i, aucx[2]]
                CpFLAGY[i, aucx[3]] = CpFLAGY[i, aucx[2]]

            aux = np.sum(CpFLAGY) + np.sum(CpFLAGX) + auxbeam
            if aux > 0:
                print('Columns Not OK...the maximum Rho_l condition... still %d to change' % int(sum(CpFLAGY.flatten()) + sum(CpFLAGX.flatten())))
            else:
                print('Columns Rho_l condition OK!')

        return CpFLAGX, CpFLAGY, CpFLAGfc, aux

    def _cdm_beams(self):
        """
        Designs columns usign DCM properties
        Refrence: Betao armado: esforços normais e de flexao (REBAP, 1983)
        Design based on ultimate strength analysis
        The beams are separated into different alignments and a single section is used. 
        1) The maximum bending moment of the alignement (max of all M1s and of all M9s) is used to assess the maximum As-.
        2) The maximum bending momento of the mid spans (max of all M5s) is used to compute the required As+.
        3) The corresponding solution in terms of rebars is calculated for As- ans As+ usign the same diameter.
        4) Calculate the rebar solution and exports the key elements for the nonlinear modelling
        """
        # ...........................................................................
        # Variables for the design based on the DCM Design Routines
        # ...........................................................................
        fckvect = [12, 16, 20, 25, 30, 35, 40, 45, 50]
        tau1vect = [0.5, 0.6, 0.65, 0.75, 0.85, 0.90, 1.00, 1.10, 1.15]
        tausmaxvect = [2.4, 3.2, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        fcd = self.general.fcd + 0
        fsyd = self.general.fsyd + 0
        tau1 = 1000 * np.interp(self.general.fck, fckvect, tau1vect)
        taumax = 1000 * np.interp(self.general.fck, fckvect, tausmaxvect)
        miueconomic = 0.25
        top_to_bot_ratio = 0.50
        dmax_between_long_bars = 0.10
        sw_min_over_fi = 12
        cover = 0.03
        dmin = 0.04
        epscU = 3.5/1000
        esy = self.general.fsyk / 200000
        if self.general.fck < 27.6:
            betafc = 0.85
        elif self.general.fck > 55.17:
            betafc = 0.65
        else:
            betafc = 1.05 - 0.05 * self.general.fck/6.9
        if self.general.fsyk == 500:
            rhomin_tens = 0.12  # 90.1 REBAP
        elif self.general.fsyk == 400:
            rhomin_tens = 0.15  # 90.1 REBAP
        else:
            rhomin_tens = 0.25  # 90.1 REBAP
        # ...........................................................................
        # Verifies the adequcy of the sectional dimensions
        # ...........................................................................
        alignmentsX = np.unique(self.beamX.index)
        CvFLAGX = np.zeros((self.general.nstoreys, self.beamX.index.shape[0]))
        for i in range(len(alignmentsX)):
            mask = self.beamX.index == alignmentsX[i]
            for j in range(self.general.nstoreys):
                BB = self.beamX.BB[f'{i}, {j}'].copy()
                HH = self.beamX.HH[f'{i}, {j}'].copy()
                moment_plus = self.beamX.MomentEnvelopePlusCDM[f'{i}, {j}'].copy()
                moment_neg = self.beamX.MomentEnvelopeNegCDM[f'{i}, {j}'].copy()
                maximum_shear = self.beamX.ShearEnvelopeCDM[f'{i}, {j}'].copy()
                muplusX = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                munegX = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                tauX = np.abs(maximum_shear) / (BB * (0.90 * HH))
                if max(muplusX) > miueconomic or max(munegX) > miueconomic or max(tauX) > taumax:
                    CvFLAGX[j, mask] = 1 # not satisfied
                else:
                    CvFLAGX[j, mask] = 0 # satisfied
        # ...........................................................................
        alignmentsY = np.unique(self.beamY.index)
        CvFLAGY = np.zeros((self.general.nstoreys, self.beamY.index.shape[0]))
        for i in range(len(alignmentsY)):
            mask = self.beamY.index == alignmentsY[i]
            for j in range(self.general.nstoreys):
                BB = self.beamY.BB[f'{i}, {j}'].copy()
                HH = self.beamY.HH[f'{i}, {j}'].copy()
                moment_plus = self.beamY.MomentEnvelopePlusCDM[f'{i}, {j}'].copy()
                moment_neg = self.beamY.MomentEnvelopeNegCDM[f'{i}, {j}'].copy()
                maximum_shear = self.beamY.ShearEnvelopeCDM[f'{i}, {j}'].copy()
                muplusY = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                munegY = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                tauY = np.abs(maximum_shear) / (BB * (0.90 * HH))
                if max(muplusY) > miueconomic or max(munegY) > miueconomic or max(tauY) > taumax:
                    CvFLAGY[j, mask] = 1 # not satisfied
                else:
                    CvFLAGY[j, mask] = 0 # satisfied
        # ...........................................................................
        CvFLAGStair = np.zeros(self.general.nstoreys)
        for j in range(self.general.nstoreys):
            BB = self.beamStair.BB[f'{j}'].copy()
            HH = self.beamStair.HH[f'{j}'].copy()
            moment_plus = self.beamStair.MomentEnvelopePlusCDM[f'{j}'].copy()
            moment_neg = self.beamStair.MomentEnvelopeNegCDM[f'{j}'].copy()
            maximum_shear = self.beamStair.ShearEnvelopeCDM[f'{j}'].copy()
            muplusStair = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
            munegStair = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
            tauStair = np.abs(maximum_shear) / (BB * (0.90 * HH))
            if max(muplusStair) > miueconomic or max(munegStair) > miueconomic or max(tauStair) > taumax:
                CvFLAGStair[j] = 1 # not satisfied
            else:
                CvFLAGStair[j] = 0 # satisfied
        # ...........................................................................
        # Verifies the need for a new section
        # ...........................................................................
        auxbeam = np.sum(CvFLAGX) + np.sum(CvFLAGY) + np.sum(CvFLAGStair)
        if auxbeam > 0.99:
            print(f"Beams Not OK ... still {auxbeam:.0f} to change")
        else:
            print("Beams stage 1 complete")
            # ...........................................................................
            # When ok, selects the longitudinal steel rebar solution and the tranverse steel rebar solution
            # ...........................................................................
            mulim = 0.31
            omegalim = 0.41
            # ...........................................................................
            # BeamX
            NeededAsTOPX = {}
            NeededAsBOTX = {}
            NeededAsw_sX = {}
            swmax_X = {}
            self.beamX.NeededAsTOP = {}
            self.beamX.NeededAsBOT = {}
            self.beamX.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                for i in range(len(alignmentsX)):
                    BB = self.beamX.BB[f'{i}, {j}'].copy()
                    HH = self.beamX.HH[f'{i}, {j}'].copy()
                    moment_plus = self.beamX.MomentEnvelopePlusCDM[f'{i}, {j}'].copy()
                    moment_neg = self.beamX.MomentEnvelopeNegCDM[f'{i}, {j}'].copy()
                    maximum_shear = self.beamX.ShearEnvelopeCDM[f'{i}, {j}'].copy()
                    moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                    moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                    # ...........................................................................
                    muplusX = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000) # REBAP pp. 33
                    munegX = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000) # REBAP pp. 33
                    # ...........................................................................
                    omega_plusX_prime = (muplusX - mulim) / (1 - (cover / (0.90 * HH))) # REBAP pp. 35, eq 11
                    omega_plusX_prime[muplusX <= mulim] = 0 # REBAP pp. 35, eq 10
                    omega_plusX = omegalim + omega_plusX_prime # REBAP pp. 35, eq 11
                    omega_plusX[muplusX <= mulim] = muplusX[muplusX <= mulim] * (1 + muplusX[muplusX <= mulim]) # REBAP pp. 35, eq 10
                    # ...........................................................................
                    omega_negX_prime = (munegX - mulim) / (1 - (cover / (0.90 * HH))) # REBAP pp. 35, eq 11
                    omega_negX_prime[munegX <= mulim] = 0 # REBAP pp. 35, eq 10
                    omega_negX = omegalim + omega_negX_prime # REBAP pp. 35, eq 11
                    omega_negX[munegX <= mulim] = munegX[munegX <= mulim] * (1 + munegX[munegX <= mulim]) # REBAP pp. 35, eq 10
                    # ...........................................................................
                    omega_plusX = np.maximum(omega_plusX, omega_negX_prime) # prime is used for compression reinf. it can be both at top and bottom due to seismic loading
                    omega_negX = np.maximum(omega_negX, omega_plusX_prime) # prime is used for compression reinf. it can be both at top and bottom due to seismic loading
                    # ...........................................................................
                    AsminTOPX = rhomin_tens * BB * 0.90 * HH / 100                           
                    AsminBOTX = rhomin_tens * BB * 0.90 * HH / 100
                    AsTOPX = np.maximum(omega_negX * BB * 0.90 * HH * fcd / fsyd, AsminTOPX)
                    AsBOTX = np.maximum(omega_plusX * BB * 0.90 * HH * fcd / fsyd, AsminBOTX)
                    NeededAsTOPX[f'{i}, {j}'] = AsTOPX.copy()
                    NeededAsBOTX[f'{i}, {j}'] = AsBOTX.copy()
                    self.beamX.NeededAsTOP[f'{i}, {j}'] = AsTOPX.copy()
                    self.beamX.NeededAsBOT[f'{i}, {j}'] = AsBOTX.copy()
                    VcdX = tau1 * BB * 0.9 * HH
                    VswconstX = 0.9 * 0.9 *HH * 1000 * fsyd  # 53.3 rebap, assuming vertical stirrups
                    if fsyd < 230:
                        Asw_minX = 0.16 * BB / 100 
                    elif fsyd < 400:
                        Asw_minX = 0.10 * BB / 100
                    else:
                        Asw_minX = 0.08 * BB / 100
                    Asw_sX = (np.abs(maximum_shear) - VcdX) / VswconstX    # 53.3 rebap, assuming vertical stirrups
                    Asw_sX[Asw_sX < Asw_minX] = Asw_minX[Asw_sX<Asw_minX]  # 53.3 rebap, assuming vertical stirrups
                    NeededAsw_sX[f'{i}, {j}'] = Asw_sX.copy()
                    swmax_X[f'{i}, {j}'] = np.minimum(HH, 0.20)
                    self.beamX.NeededAsw_s[f'{i}, {j}'] = Asw_sX.copy()
            # ...........................................................................
            # BeamY
            NeededAsTOPY = {}
            NeededAsBOTY = {}
            NeededAsw_sY = {}
            swmax_Y = {}
            self.beamY.NeededAsTOP = {}
            self.beamY.NeededAsBOT = {}
            self.beamY.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                for i in range(len(alignmentsY)):
                    BB = self.beamY.BB[f'{i}, {j}'].copy()
                    HH = self.beamY.HH[f'{i}, {j}'].copy()
                    moment_plus = self.beamY.MomentEnvelopePlusCDM[f'{i}, {j}'].copy()
                    moment_neg = self.beamY.MomentEnvelopeNegCDM[f'{i}, {j}'].copy()
                    maximum_shear = self.beamY.ShearEnvelopeCDM[f'{i}, {j}'].copy()
                    moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                    moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                    # ...........................................................................
                    muplusY = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                    munegY = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                    # ...........................................................................
                    omega_plusY_prime = (muplusY - mulim) / (1 - (cover / (0.90 * HH)))
                    omega_plusY_prime[muplusY <= mulim] = 0
                    omega_plusY = omegalim + omega_plusY_prime
                    omega_plusY[muplusY <= mulim] = muplusY[muplusY <= mulim] * (1 + muplusY[muplusY <= mulim])
                    # ...........................................................................
                    omega_negY_prime = (munegY - mulim) / (1 - (cover / (0.90 * HH)))
                    omega_negY_prime[munegY <= mulim] = 0
                    omega_negY = omegalim + omega_negY_prime
                    omega_negY[munegY <= mulim] = munegY[munegY <= mulim] * (1 + munegY[munegY <= mulim])
                    # ...........................................................................
                    omega_plusY = np.maximum(omega_plusY, omega_negY_prime)
                    omega_negY = np.maximum(omega_negY, omega_plusY_prime)
                    # ...........................................................................
                    AsminTOPY = rhomin_tens * BB * 0.90 * HH / 100                           
                    AsminBOTY = rhomin_tens * BB * 0.90 * HH / 100
                    AsTOPY = np.maximum(omega_negY * BB * 0.90 * HH * fcd / fsyd, AsminTOPY)
                    AsBOTY = np.maximum(omega_plusY * BB * 0.90 * HH * fcd / fsyd, AsminBOTY)
                    NeededAsTOPY[f'{i}, {j}'] = AsTOPY.copy()
                    NeededAsBOTY[f'{i}, {j}'] = AsBOTY.copy()
                    self.beamY.NeededAsTOP[f'{i}, {j}'] = AsTOPY.copy()
                    self.beamY.NeededAsBOT[f'{i}, {j}'] = AsBOTY.copy()
                    # ...........................................................................
                    VcdY = tau1 * BB * 0.9 * HH
                    VswconstY = 0.9 * 0.9 * HH * 1000 * fsyd  # 53.3 rebap, assuming vertical stirrups
                    if fsyd < 230:
                        Asw_minY = 0.16 * BB / 100 
                    elif fsyd < 400:
                        Asw_minY = 0.10 * BB / 100
                    else:
                        Asw_minY = 0.08 * BB / 100
                    Asw_sY = (np.abs(maximum_shear) - VcdY) / VswconstY    # 53.3 rebap, assuming vertical stirrups
                    Asw_sY[Asw_sY < Asw_minY] = Asw_minY[Asw_sY<Asw_minY]  # 53.3 rebap, assuming vertical stirrups
                    NeededAsw_sY[f'{i}, {j}'] = Asw_sY.copy()
                    swmax_Y[f'{i}, {j}'] = np.minimum(HH, 0.20)
                    self.beamY.NeededAsw_s[f'{i}, {j}'] = Asw_sY.copy()
            # ...........................................................................
            # BeamStair
            NeededAsTOPStair = {}
            NeededAsBOTStair = {}
            NeededAsw_sStair = {}
            swmax_Stair = {}
            self.beamStair.NeededAsTOP = {}
            self.beamStair.NeededAsBOT = {}
            self.beamStair.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                BB = self.beamStair.BB[f'{j}'].copy()
                HH = self.beamStair.HH[f'{j}'].copy()
                moment_plus = self.beamStair.MomentEnvelopePlusCDM[f'{j}'].copy()
                moment_neg = self.beamStair.MomentEnvelopeNegCDM[f'{j}'].copy()
                maximum_shear = self.beamStair.ShearEnvelopeCDM[f'{j}'].copy()
                moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                # ...........................................................................
                muplusStair = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                munegStair = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                # ...........................................................................
                omega_plusStair_prime = (muplusStair - mulim) / (1 - (cover / (0.90 * HH)))
                omega_plusStair_prime[muplusStair <= mulim] = 0
                omega_plusStair = omegalim + omega_plusStair_prime
                omega_plusStair[muplusStair <= mulim] = muplusStair[muplusStair <= mulim] * (1 + muplusStair[muplusStair <= mulim])
                # ...........................................................................
                omega_negStair_prime = (munegStair - mulim) / (1 - (cover / (0.90 * HH)))
                omega_negStair_prime[munegStair <= mulim] = 0
                omega_negStair = omegalim + omega_negStair_prime
                omega_negStair[munegStair <= mulim] = munegStair[munegStair <= mulim] * (1 + munegStair[munegStair <= mulim])
                # ...........................................................................
                omega_plusStair = np.maximum(omega_plusStair, omega_negStair_prime)
                omega_negStair = np.maximum(omega_negStair, omega_plusStair_prime)
                # ...........................................................................
                AsminTOPStair = rhomin_tens * BB * 0.90 * HH / 100                           
                AsminBOTStair = rhomin_tens * BB * 0.90 * HH / 100
                AsTOPStair = np.maximum(omega_negStair * BB * 0.90 * HH * fcd / fsyd, AsminTOPStair)
                AsBOTStair = np.maximum(omega_plusStair * BB * 0.90 * HH * fcd / fsyd, AsminBOTStair)
                NeededAsTOPStair[f'{j}'] = AsTOPStair.copy()
                NeededAsBOTStair[f'{j}'] = AsBOTStair.copy()
                self.beamStair.NeededAsTOP[f'{j}'] = AsTOPStair.copy()
                self.beamStair.NeededAsBOT[f'{j}'] = AsBOTStair.copy()
                # ...........................................................................
                VcdStair = tau1 * BB * 0.9 * HH
                VswconstStair = 0.9 * 0.9 * HH * 1000 * fsyd  # 53.3 rebap, assuming vertical stirrups
                if fsyd < 230:
                    Asw_minStair = 0.16 * BB / 100 
                elif fsyd < 400:
                    Asw_minStair = 0.10 * BB / 100
                else:
                    Asw_minStair = 0.08 * BB / 100
                Asw_sStair = (np.abs(maximum_shear) - VcdStair) / VswconstStair                # 53.3 rebap, assuming vertical stirrups
                Asw_sStair[Asw_sStair < Asw_minStair] = Asw_minStair[Asw_sStair<Asw_minStair]  # 53.3 rebap, assuming vertical stirrups
                NeededAsw_sStair[f'{j}'] = Asw_sStair.copy()
                swmax_Stair[f'{j}'] = np.minimum(HH, 0.20)
                self.beamStair.NeededAsw_s[f'{j}'] = Asw_sStair.copy()
            # ...........................................................................
            # Starts selecting the longitudinal steel rebar solution and the tranverse steel rebar solution
            # ...........................................................................
            attributes = ['ficornerTOP', 'ncornerTOP', 'fiintTOP', 'nintTOP', 'ficornerBOT', 'ncornerBOT', 'fiintBOT', 'nintBOT', 'fiw', 'sw', 'nwparallel_to_b', 'nwparallel_to_h']
            for attr in attributes:
                val = {f'{i}, {j}':None for i in range(len(alignmentsX)) for j in range(self.general.nstoreys)}
                setattr(self.beamX, attr, val)
                val = {f'{i}, {j}':None for i in range(len(alignmentsY)) for j in range(self.general.nstoreys)}
                setattr(self.beamY, attr, val)
                val = {f'{j}':None  for j in range(self.general.nstoreys)}
                setattr(self.beamStair, attr, val)
            # ...........................................................................
            for i in range(len(alignmentsX)):            
                for j in range(self.general.nstoreys):
                    self.beamX.ficornerTOP[f'{i}, {j}'], self.beamX.ncornerTOP[f'{i}, {j}'], self.beamX.fiintTOP[f'{i}, {j}'], self.beamX.nintTOP[f'{i}, {j}'], self.beamX.ficornerBOT[f'{i}, {j}'], self.beamX.ncornerBOT[f'{i}, {j}'], self.beamX.fiintBOT[f'{i}, {j}'], self.beamX.nintBOT[f'{i}, {j}'], self.beamX.fiw[f'{i}, {j}'], self.beamX.sw[f'{i}, {j}'], self.beamX.nwparallel_to_b[f'{i}, {j}'], self.beamX.nwparallel_to_h[f'{i}, {j}'] = _get_beam_rebars(NeededAsBOTX[f'{i}, {j}'], NeededAsTOPX[f'{i}, {j}'], self.beamX.BB[f'{i}, {j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sX[f'{i}, {j}'], swmax_X[f'{i}, {j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            for i in range(len(alignmentsY)):
                for j in range(self.general.nstoreys):
                    self.beamY.ficornerTOP[f'{i}, {j}'], self.beamY.ncornerTOP[f'{i}, {j}'], self.beamY.fiintTOP[f'{i}, {j}'], self.beamY.nintTOP[f'{i}, {j}'], self.beamY.ficornerBOT[f'{i}, {j}'], self.beamY.ncornerBOT[f'{i}, {j}'], self.beamY.fiintBOT[f'{i}, {j}'], self.beamY.nintBOT[f'{i}, {j}'], self.beamY.fiw[f'{i}, {j}'], self.beamY.sw[f'{i}, {j}'], self.beamY.nwparallel_to_b[f'{i}, {j}'], self.beamY.nwparallel_to_h[f'{i}, {j}'] = _get_beam_rebars(NeededAsBOTY[f'{i}, {j}'], NeededAsTOPY[f'{i}, {j}'], self.beamY.BB[f'{i}, {j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sY[f'{i}, {j}'], swmax_Y[f'{i}, {j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            for j in range(self.general.nstoreys):
                self.beamStair.ficornerTOP[f'{j}'], self.beamStair.ncornerTOP[f'{j}'], self.beamStair.fiintTOP[f'{j}'], self.beamStair.nintTOP[f'{j}'], self.beamStair.ficornerBOT[f'{j}'], self.beamStair.ncornerBOT[f'{j}'], self.beamStair.fiintBOT[f'{j}'], self.beamStair.nintBOT[f'{j}'], self.beamStair.fiw[f'{j}'], self.beamStair.sw[f'{j}'], self.beamStair.nwparallel_to_b[f'{j}'], self.beamStair.nwparallel_to_h[f'{j}'] = _get_beam_rebars(NeededAsBOTStair[f'{j}'], NeededAsTOPStair[f'{j}'], self.beamStair.BB[f'{j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sStair[f'{j}'], swmax_Stair[f'{j}'], sw_min_over_fi, dmin) 
            # uniformize the number of rebars at each common section 
            # (section 9 from  previous to 1 from next) at the same alignment 
            # -xx (HMA)
            attributes = ['BBbb', 'DDdd']
            for attr in attributes:
                val = {f'{j}, {i}':None for i in range(len(alignmentsX)) for j in range(self.general.nstoreys)}
                setattr(self.beamX, attr, val)
                val = {f'{j}, {i}':None for i in range(len(alignmentsY)) for j in range(self.general.nstoreys)}
                setattr(self.beamY, attr, val)

            for j in range(self.general.nstoreys): # loop over the storeys
                for i in range(len(alignmentsX)): # loop over the alignment
                    aa = self.beamX.ncornerTOP[f'{i}, {j}']
                    bb = self.beamX.nintTOP[f'{i}, {j}']
                    cc = self.beamX.ncornerBOT[f'{i}, {j}']
                    dd = self.beamX.nintBOT[f'{i}, {j}']
                    for kk in range(2, len(dd)-3, 3):
                        aa[kk] = max(aa[kk], aa[kk+1])
                        aa[kk+1] = max(aa[kk], aa[kk+1])
                        bb[kk] = max(bb[kk], bb[kk+1])
                        bb[kk+1] = max(bb[kk], bb[kk+1])
                        cc[kk] = max(cc[kk], cc[kk+1])
                        cc[kk+1] = max(cc[kk], cc[kk+1])
                        dd[kk] = max(dd[kk], dd[kk+1])
                        dd[kk+1] = max(dd[kk], dd[kk+1])

                    self.beamX.ncornerTOP[f'{i}, {j}'] = aa.copy()
                    self.beamX.nintTOP[f'{i}, {j}'] = bb.copy()
                    self.beamX.ncornerBOT[f'{i}, {j}'] = cc.copy()
                    self.beamX.nintBOT[f'{i}, {j}'] = dd.copy()
                    self.beamX.BBbb[f'{i}, {j}'] = bb.copy()
                    self.beamX.DDdd[f'{i}, {j}'] = dd.copy()

            # -yy (HMA)
            for j in range(self.general.nstoreys): # loop over the storeys
                for i in range(len(alignmentsY)): # loop over the alignement
                    aa = self.beamY.ncornerTOP[f'{i}, {j}']
                    bb = self.beamY.nintTOP[f'{i}, {j}']
                    cc = self.beamY.ncornerBOT[f'{i}, {j}']
                    dd = self.beamY.nintBOT[f'{i}, {j}']
                    for kk in range(2, len(dd)-3, 3):
                        aa[kk] = max(aa[kk], aa[kk+1])
                        aa[kk+1] = max(aa[kk], aa[kk+1])
                        bb[kk] = max(bb[kk], bb[kk+1])
                        bb[kk+1] = max(bb[kk], bb[kk+1])
                        cc[kk] = max(cc[kk], cc[kk+1])
                        cc[kk+1] = max(cc[kk], cc[kk+1])
                        dd[kk] = max(dd[kk], dd[kk+1])
                        dd[kk+1] = max(dd[kk], dd[kk+1])

                    self.beamY.ncornerTOP[f'{i}, {j}'] = aa.copy()
                    self.beamY.nintTOP[f'{i}, {j}'] = bb.copy()
                    self.beamY.ncornerBOT[f'{i}, {j}'] = cc.copy()
                    self.beamY.nintBOT[f'{i}, {j}'] = dd.copy()
                    self.beamY.BBbb[f'{i}, {j}'] = bb.copy()
                    self.beamY.DDdd[f'{i}, {j}'] = dd.copy()
            # ...........................................................................
            # Calculation of My for the beams in -XX
            # ...........................................................................
            neles = len(self.beamX.Area.flatten())
            pedXEQ = self.beamX.pedEQFinal.copy()
            pedXEQ[-1, :] = self.beamX.proofEQFinal[-1, :]
            pedXEQ = pedXEQ.flatten()
            self.beamX.Matrix = np.zeros((neles, 42))
            iele  = 0
            for j in range(self.general.nstoreys): # loop over the storeys
                auxMyPos = np.array([])
                auxMyNeg = np.array([])
                for i in range(len(alignmentsX)): # loop over the alignment
                    namesly = self.beamX.NName[f'{i}, {j}']
                    nodeily = self.beamX.NNodei[f'{i}, {j}']
                    nodejly = self.beamX.NNodej[f'{i}, {j}']
                    HHly    = self.beamX.HH[f'{i}, {j}']
                    BBly    = self.beamX.BB[f'{i}, {j}']
                    LLly    = self.beamX.LL[f'{i}, {j}']
                    Ntopc   = self.beamX.ncornerTOP[f'{i}, {j}']
                    Ftopc   = self.beamX.ficornerTOP[f'{i}, {j}']
                    Ntopi   = self.beamX.nintTOP[f'{i}, {j}']
                    Ftopi   = self.beamX.fiintTOP[f'{i}, {j}']
                    Nbotc   = self.beamX.ncornerBOT[f'{i}, {j}']
                    Fbotc   = self.beamX.ficornerBOT[f'{i}, {j}']
                    Nboti   = self.beamX.nintBOT[f'{i}, {j}']
                    Fboti   = self.beamX.fiintBOT[f'{i}, {j}']
                    fiw     = self.beamX.fiw[f'{i}, {j}']
                    sw      = self.beamX.sw[f'{i}, {j}']
                    nwparallel_to_b = self.beamX.nwparallel_to_b[f'{i}, {j}']
                    nwparallel_to_h = self.beamX.nwparallel_to_h[f'{i}, {j}']
                    # ...........................................................................
                    dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                    dD_line  = 1000 * HHly - dD                                                               # in mm
                    cB       = (epscU * dD) / (epscU + esy)
                    Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    Ec       = (57000 * (fcd * 145)**0.5) / 145
                    Es       = 200000
                    nyoung   = Es / Ec
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control = np.ones(dD.shape)
                    AtoUse  = AtensCntrl + 0
                    BtoUse  = BtensCntrl + 0
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control[cC < cB] = 1
                    AtoUse[cC < cB] = AtensCntrl[cC < cB]
                    BtoUse[cC < cB] = BtensCntrl[cC < cB]
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    nameslyuni = np.unique(namesly)
                    for kk in range(len(nameslyuni)):
                        indexly = np.where(namesly==nameslyuni[kk])[0]
                        self.beamX.Matrix[iele, 0] = namesly[indexly[0]]
                        self.beamX.Matrix[iele, 1] = nodeily[indexly[0]]
                        self.beamX.Matrix[iele, 2] = nodejly[indexly[0]]
                        self.beamX.Matrix[iele, 3] = BBly[indexly[0]]
                        self.beamX.Matrix[iele, 4] = HHly[indexly[0]]
                        self.beamX.Matrix[iele, 5] = LLly[indexly[0]]
                        self.beamX.Matrix[iele, 6] = Ntopc[indexly[0]]
                        self.beamX.Matrix[iele, 7] = Ntopc[indexly[-1]]
                        self.beamX.Matrix[iele, 8] = Ftopc[indexly[0]]
                        self.beamX.Matrix[iele, 9] = Ftopc[indexly[-1]]
                        self.beamX.Matrix[iele, 10] = Nbotc[indexly[0]]
                        self.beamX.Matrix[iele, 11] = Nbotc[indexly[-1]]
                        self.beamX.Matrix[iele, 12] = Fbotc[indexly[0]]
                        self.beamX.Matrix[iele, 13] = Fbotc[indexly[-1]]
                        self.beamX.Matrix[iele, 14] = fiw[indexly[0]]
                        self.beamX.Matrix[iele, 15] = sw[indexly[0]]
                        self.beamX.Matrix[iele, 16] = nwparallel_to_b[indexly[0]]
                        self.beamX.Matrix[iele, 17] = nwparallel_to_h[indexly[0]]
                        self.beamX.Matrix[iele, 18] = fiw[indexly[-1]]
                        self.beamX.Matrix[iele, 19] = sw[indexly[-1]]
                        self.beamX.Matrix[iele, 20] = nwparallel_to_b[indexly[-1]]
                        self.beamX.Matrix[iele, 21] = nwparallel_to_h[indexly[-1]]
                        self.beamX.Matrix[iele, 22] = Ntopi[indexly[0]]
                        self.beamX.Matrix[iele, 23] = Ntopi[indexly[-1]]
                        self.beamX.Matrix[iele, 24] = Ftopi[indexly[0]]
                        self.beamX.Matrix[iele, 25] = Ftopi[indexly[-1]]
                        self.beamX.Matrix[iele, 26] = Nboti[indexly[0]]
                        self.beamX.Matrix[iele, 27] = Nboti[indexly[-1]]
                        self.beamX.Matrix[iele, 28] = Fboti[indexly[0]]
                        self.beamX.Matrix[iele, 29] = Fboti[indexly[-1]]
                        self.beamX.Matrix[iele, 30] = MyNeg[indexly[0]]
                        self.beamX.Matrix[iele, 31] = MyPos[indexly[0]]
                        self.beamX.Matrix[iele, 32] = MyNeg[indexly[-1]]
                        self.beamX.Matrix[iele, 33] = MyPos[indexly[-1]]
                        
                        iele += 1                   

                    auxMyPos = np.append(auxMyPos, np.concatenate(([0], MyPos[2:-3:3], [0])))
                    auxMyNeg = np.append(auxMyNeg, np.concatenate(([MyNeg[0]], MyNeg[2:-3:3], [MyNeg[-1]])))

                if not hasattr(self.beamX, 'MyPos'):
                    self.beamX.MyPos = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamX.MyNeg = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamX.sumMrd = np.zeros((self.general.nstoreys, len(auxMyPos)))

                self.beamX.MyPos[j, :] = auxMyPos
                self.beamX.MyNeg[j, :] = auxMyNeg
                self.beamX.sumMrd[j, :] = auxMyPos + auxMyNeg

            self.beamX.Matrix[:, 41] = pedXEQ
            # ...........................................................................
            # Calculation of My for the beams in -YY
            # ...........................................................................
            neles = len(self.beamY.Area.flatten())
            pedYEQ = self.beamY.pedEQFinal.copy()
            pedYEQ[-1, :] = self.beamY.proofEQFinal[-1, :]
            pedYEQ = pedYEQ.flatten()
            self.beamY.Matrix = np.zeros((neles, 42))
            iele  = 0
            for j in range(self.general.nstoreys): # loop over the storeys
                auxMyPos = np.array([])
                auxMyNeg = np.array([])
                for i in range(len(alignmentsY)): # loop over the alignment
                    namesly = self.beamY.NName[f'{i}, {j}']
                    nodeily = self.beamY.NNodei[f'{i}, {j}']
                    nodejly = self.beamY.NNodej[f'{i}, {j}']
                    HHly    = self.beamY.HH[f'{i}, {j}']
                    BBly    = self.beamY.BB[f'{i}, {j}']
                    LLly    = self.beamY.LL[f'{i}, {j}']
                    Ntopc   = self.beamY.ncornerTOP[f'{i}, {j}']
                    Ftopc   = self.beamY.ficornerTOP[f'{i}, {j}']
                    Ntopi   = self.beamY.nintTOP[f'{i}, {j}']
                    Ftopi   = self.beamY.fiintTOP[f'{i}, {j}']
                    Nbotc   = self.beamY.ncornerBOT[f'{i}, {j}']
                    Fbotc   = self.beamY.ficornerBOT[f'{i}, {j}']
                    Nboti   = self.beamY.nintBOT[f'{i}, {j}']
                    Fboti   = self.beamY.fiintBOT[f'{i}, {j}']
                    fiw     = self.beamY.fiw[f'{i}, {j}']
                    sw      = self.beamY.sw[f'{i}, {j}']
                    nwparallel_to_b = self.beamY.nwparallel_to_b[f'{i}, {j}']
                    nwparallel_to_h = self.beamY.nwparallel_to_h[f'{i}, {j}']
                    # ...........................................................................
                    dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                    dD_line  = 1000 * HHly - dD                                                               # in mm
                    cB       = (epscU * dD) / (epscU + esy)
                    Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    Ec       = (57000 * (fcd * 145)**0.5) / 145
                    Es       = 200000
                    nyoung   = Es / Ec
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control = np.ones(dD.shape)
                    AtoUse  = AtensCntrl + 0
                    BtoUse  = BtensCntrl + 0
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control[cC < cB] = 1
                    AtoUse[cC < cB] = AtensCntrl[cC < cB]
                    BtoUse[cC < cB] = BtensCntrl[cC < cB]
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    nameslyuni = np.unique(namesly)
                    for kk in range(len(nameslyuni)):
                        indexly = np.where(namesly==nameslyuni[kk])[0]
                        self.beamY.Matrix[iele, 0] = namesly[indexly[0]]
                        self.beamY.Matrix[iele, 1] = nodeily[indexly[0]]
                        self.beamY.Matrix[iele, 2] = nodejly[indexly[0]]
                        self.beamY.Matrix[iele, 3] = BBly[indexly[0]]
                        self.beamY.Matrix[iele, 4] = HHly[indexly[0]]
                        self.beamY.Matrix[iele, 5] = LLly[indexly[0]]
                        self.beamY.Matrix[iele, 6] = Ntopc[indexly[0]]
                        self.beamY.Matrix[iele, 7] = Ntopc[indexly[-1]]
                        self.beamY.Matrix[iele, 8] = Ftopc[indexly[0]]
                        self.beamY.Matrix[iele, 9] = Ftopc[indexly[-1]]
                        self.beamY.Matrix[iele, 10] = Nbotc[indexly[0]]
                        self.beamY.Matrix[iele, 11] = Nbotc[indexly[-1]]
                        self.beamY.Matrix[iele, 12] = Fbotc[indexly[0]]
                        self.beamY.Matrix[iele, 13] = Fbotc[indexly[-1]]
                        self.beamY.Matrix[iele, 14] = fiw[indexly[0]]
                        self.beamY.Matrix[iele, 15] = sw[indexly[0]]
                        self.beamY.Matrix[iele, 16] = nwparallel_to_b[indexly[0]]
                        self.beamY.Matrix[iele, 17] = nwparallel_to_h[indexly[0]]
                        self.beamY.Matrix[iele, 18] = fiw[indexly[-1]]
                        self.beamY.Matrix[iele, 19] = sw[indexly[-1]]
                        self.beamY.Matrix[iele, 20] = nwparallel_to_b[indexly[-1]]
                        self.beamY.Matrix[iele, 21] = nwparallel_to_h[indexly[-1]]
                        self.beamY.Matrix[iele, 22] = Ntopi[indexly[0]]
                        self.beamY.Matrix[iele, 23] = Ntopi[indexly[-1]]
                        self.beamY.Matrix[iele, 24] = Ftopi[indexly[0]]
                        self.beamY.Matrix[iele, 25] = Ftopi[indexly[-1]]
                        self.beamY.Matrix[iele, 26] = Nboti[indexly[0]]
                        self.beamY.Matrix[iele, 27] = Nboti[indexly[-1]]
                        self.beamY.Matrix[iele, 28] = Fboti[indexly[0]]
                        self.beamY.Matrix[iele, 29] = Fboti[indexly[-1]]
                        self.beamY.Matrix[iele, 30] = MyNeg[indexly[0]]
                        self.beamY.Matrix[iele, 31] = MyPos[indexly[0]]
                        self.beamY.Matrix[iele, 32] = MyNeg[indexly[-1]]
                        self.beamY.Matrix[iele, 33] = MyPos[indexly[-1]]
                        
                        iele += 1                   

                    auxMyPos = np.append(auxMyPos, np.concatenate(([0], MyPos[2:-3:3], [0])))
                    auxMyNeg = np.append(auxMyNeg, np.concatenate(([MyNeg[0]], MyNeg[2:-3:3], [MyNeg[-1]])))

                if not hasattr(self.beamY, 'MyPos'):
                    self.beamY.MyPos = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.MyNeg = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.sumMrd = np.zeros((self.general.nstoreys, len(auxMyPos)))

                self.beamY.MyPos[j, :] = auxMyPos
                self.beamY.MyNeg[j, :] = auxMyNeg
                self.beamY.sumMrd[j, :] = auxMyPos + auxMyNeg

            self.beamY.Matrix[:, 41] = pedYEQ
            # ...........................................................................
            # Calculation of My for the beams in Stairs
            # ...........................................................................
            neles = len(self.beamStair.Area.flatten())
            pedStairEQ = self.beamStair.pedEQFinal.copy()
            pedStairEQ = pedStairEQ.flatten()
            self.beamStair.Matrix = np.zeros((neles, 42))
            iele  = 0
            auxMyPos = np.array([])
            auxMyNeg = np.array([])
            for j in range(self.general.nstoreys):
                namesly = self.beamStair.NName[f'{j}']
                nodeily = self.beamStair.NNodei[f'{j}']
                nodejly = self.beamStair.NNodej[f'{j}']
                HHly    = self.beamStair.HH[f'{j}']
                BBly    = self.beamStair.BB[f'{j}']
                LLly    = self.beamStair.LL[f'{j}']
                Ntopc   = self.beamStair.ncornerTOP[f'{j}']
                Ftopc   = self.beamStair.ficornerTOP[f'{j}']
                Ntopi   = self.beamStair.nintTOP[f'{j}']
                Ftopi   = self.beamStair.fiintTOP[f'{j}']
                Nbotc   = self.beamStair.ncornerBOT[f'{j}']
                Fbotc   = self.beamStair.ficornerBOT[f'{j}']
                Nboti   = self.beamStair.nintBOT[f'{j}']
                Fboti   = self.beamStair.fiintBOT[f'{j}']
                fiw     = self.beamStair.fiw[f'{j}']
                sw      = self.beamStair.sw[f'{j}']
                nwparallel_to_b = self.beamStair.nwparallel_to_b[f'{j}']
                nwparallel_to_h = self.beamStair.nwparallel_to_h[f'{j}']
                # ...........................................................................
                dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                dD_line  = 1000 * HHly - dD                                                               # in mm
                cB       = (epscU * dD) / (epscU + esy)
                Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                rostens  = Astens / (BBly * 1000 * dD)
                As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                ros_line = As_line / (BBly * 1000 * dD)
                cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                Ec       = (57000 * (fcd * 145)**0.5) / 145
                Es       = 200000
                nyoung   = Es / Ec
                AcomprCntrl = rostens + ros_line
                AtensCntrl  = rostens + ros_line
                BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                Control = np.ones(dD.shape)
                AtoUse  = AtensCntrl + 0
                BtoUse  = BtensCntrl + 0
                Control[cC >= cB] = 0
                AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                fiy = fiy1 + 0
                fiy[Control==0] = fiy2[Control==0]
                Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                # ...........................................................................
                Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                rostens  = Astens / (BBly * 1000 * dD)
                As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                ros_line = As_line / (BBly * 1000 * dD)
                cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                AcomprCntrl = rostens + ros_line
                AtensCntrl  = rostens + ros_line
                BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                Control[cC < cB] = 1
                AtoUse[cC < cB] = AtensCntrl[cC < cB]
                BtoUse[cC < cB] = BtensCntrl[cC < cB]
                Control[cC >= cB] = 0
                AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                fiy = fiy1 + 0
                fiy[Control==0] = fiy2[Control==0]
                Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                # ...........................................................................
                self.beamStair.Matrix[iele, 0] = namesly[0]
                self.beamStair.Matrix[iele, 1] = nodeily[0]
                self.beamStair.Matrix[iele, 2] = nodejly[0]
                self.beamStair.Matrix[iele, 3] = BBly[0]
                self.beamStair.Matrix[iele, 4] = HHly[0]
                self.beamStair.Matrix[iele, 5] = LLly[0]
                self.beamStair.Matrix[iele, 6] = Ntopc[0]
                self.beamStair.Matrix[iele, 7] = Ntopc[-1]
                self.beamStair.Matrix[iele, 8] = Ftopc[0]
                self.beamStair.Matrix[iele, 9] = Ftopc[-1]
                self.beamStair.Matrix[iele, 10] = Nbotc[0]
                self.beamStair.Matrix[iele, 11] = Nbotc[-1]
                self.beamStair.Matrix[iele, 12] = Fbotc[0]
                self.beamStair.Matrix[iele, 13] = Fbotc[-1]
                self.beamStair.Matrix[iele, 14] = fiw[0]
                self.beamStair.Matrix[iele, 15] = sw[0]
                self.beamStair.Matrix[iele, 16] = nwparallel_to_b[0]
                self.beamStair.Matrix[iele, 17] = nwparallel_to_h[0]
                self.beamStair.Matrix[iele, 18] = fiw[-1]
                self.beamStair.Matrix[iele, 19] = sw[-1]
                self.beamStair.Matrix[iele, 20] = nwparallel_to_b[-1]
                self.beamStair.Matrix[iele, 21] = nwparallel_to_h[-1]
                self.beamStair.Matrix[iele, 22] = Ntopi[0]
                self.beamStair.Matrix[iele, 23] = Ntopi[-1]
                self.beamStair.Matrix[iele, 24] = Ftopi[0]
                self.beamStair.Matrix[iele, 25] = Ftopi[-1]
                self.beamStair.Matrix[iele, 26] = Nboti[0]
                self.beamStair.Matrix[iele, 27] = Nboti[-1]
                self.beamStair.Matrix[iele, 28] = Fboti[0]
                self.beamStair.Matrix[iele, 29] = Fboti[-1]
                self.beamStair.Matrix[iele, 30] = MyNeg[0]
                self.beamStair.Matrix[iele, 31] = MyPos[0]
                self.beamStair.Matrix[iele, 32] = MyNeg[-1]
                self.beamStair.Matrix[iele, 33] = MyPos[-1]
                iele += 1                   

                if not hasattr(self.beamStair, 'MyPos'):
                    self.beamStair.MyPos = np.zeros((self.general.nstoreys, 2))
                    self.beamStair.MyNeg = np.zeros((self.general.nstoreys, 2))
                    self.beamStair.sumMrd = np.zeros((self.general.nstoreys, 2))

                self.beamStair.MyPos[j, :] = np.array([0, 0])
                self.beamStair.MyNeg[j, :] = MyNeg[[0,2]]
                self.beamStair.sumMrd[j, :]= self.beamStair.MyPos[j, :] + self.beamStair.MyNeg[j, :]

            self.beamStair.Matrix[:, 41] = pedStairEQ

        return CvFLAGX, CvFLAGY, CvFLAGStair, auxbeam

    def _cdm_columns(self, auxbeam):
        """
        Designs columns usign DCM properties
        Refrence: Betao armado: esforços normais e de flexao (REBAP, 1983)
        Design based on ultimate strength analysis

        Args:
            auxbeam (float): auxiliary variable describing the number of beams that do not satisfy design requirements
        """
        # ...........................................................................
        # General Material Propeties
        # ...........................................................................
        fckvect = [12, 16, 20, 25, 30, 35, 40, 45, 50]
        tau1vect = [0.5, 0.6, 0.65, 0.75, 0.85, 0.90, 1.00, 1.10, 1.15]
        tausmaxvect = [2.4, 3.2, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        fcd = self.general.fcd + 0
        fsyd = self.general.fsyd + 0
        tau1 = 1000 * np.interp(self.general.fck, fckvect, tau1vect)
        taumax = 1000 * np.interp(self.general.fck, fckvect, tausmaxvect)
        miueconomic = 0.25
        rho_min = 0.010
        dmin = 0.035
        dmax = 0.150  # maximum distance between restrrained steel bars
        sw_min_over_fi = 12
        cover = 0.03
        if self.general.fsyk <= 400:
            rho_max = 0.03
        else:
            rho_max = 0.04
        fiw_min = 0.006
        # ...........................................................................
        # Sets the maximum column dimensions
        # ...........................................................................
        if self.general.ColumnType == 1:
            self.column.maxH = self.column.maxHsquared + 0
        else:
            self.column.maxH = self.column.maxHrectangular + 0
        # ...........................................................................
        # Variables for the design based on the DCM Design Routines
        # ...........................................................................
        Combinations_2_use = [0, 1, 6, 7, 8, 9]
        MMMX1 = [self.column.MuX1[comb] for comb in Combinations_2_use]
        MMMY1 = [self.column.MuY1[comb] for comb in Combinations_2_use]
        MMMX9 = [self.column.MuX9[comb] for comb in Combinations_2_use]
        MMMY9 = [self.column.MuY9[comb] for comb in Combinations_2_use]
        # ...........................................................................
        TTTX1 = [self.column.tauX1[comb] for comb in Combinations_2_use]
        TTTY1 = [self.column.tauY1[comb] for comb in Combinations_2_use]
        TTTX9 = [self.column.tauX9[comb] for comb in Combinations_2_use]
        TTTY9 = [self.column.tauY9[comb] for comb in Combinations_2_use]
        # ...........................................................................
        MuX1_maxo = np.max(np.array(MMMX1), axis=0)
        MuX9_maxo = np.max(np.array(MMMX9), axis=0)
        MuY1_maxo = np.max(np.array(MMMY1), axis=0)
        MuY9_maxo = np.max(np.array(MMMY9), axis=0)
        MuXmax = np.maximum(MuX1_maxo, MuX9_maxo)
        MuYmax = np.maximum(MuY1_maxo, MuY9_maxo)
        # ...........................................................................
        tauX1_maxo = np.max(np.array(TTTX1), axis=0)
        tauX9_maxo = np.max(np.array(TTTX9), axis=0)
        tauY1_maxo = np.max(np.array(TTTY1), axis=0)
        tauY9_maxo = np.max(np.array(TTTY9), axis=0)
        tauXmax = np.maximum(tauX1_maxo, tauX9_maxo)
        tauYmax = np.maximum(tauY1_maxo, tauY9_maxo)
        # ...........................................................................
        CpFLAGX = np.zeros(self.column.name.shape)
        CpFLAGY = np.zeros(self.column.name.shape)
        CpFLAGX[tauXmax > taumax] = 1
        CpFLAGX[MuXmax > miueconomic] = 1
        CpFLAGY[tauYmax > taumax] = 1
        CpFLAGY[MuYmax > miueconomic] = 1
        # ...........................................................................
        # Variables for the design based on the DCL Design Routines
        # ...........................................................................
        if np.max(self.column.HX) > self.column.maxH or np.max(self.column.HY) > self.column.maxH:
            CpFLAGfc = 222
            if self.general.fsyk == 240:
                self.general.fsyk = 400
                self.general.fsyd = 348
                self.general.fsydEQ = 348
                self.general.fck = self.general.fckgrav.copy()
                self.general.fckcube = self.general.fckcubegrav.copy()
                self.general.fcd = self.general.fcdgrav.copy()
                self.general.fcdEQ = self.general.fcdEQgrav.copy()
            elif self.general.fck == 16:
                self.general.fck = 20
                self.general.fckcube = 25
                self.general.fcd = 13.3
                self.general.fcdEQ = 13.3
            elif self.general.fck == 20:
                self.general.fck = 25
                self.general.fckcube = 30
                self.general.fcd = 16.7
                self.general.fcdEQ = 16.7
            elif self.general.fck == 25:
                self.general.fck = 30
                self.general.fckcube = 35
                self.general.fcd = 16.7
                self.general.fcdEQ = 16.7
            elif self.general.fsyk == 400:
                self.general.fsyk = 500
                self.general.fsyd = 435
                self.general.fsydEQ = 435
                self.general.fck = self.general.fckgrav.copy()
                self.general.fckcube = self.general.fckcubegrav.copy()
                self.general.fcd = self.general.fcdgrav.copy()
                self.general.fcdEQ = self.general.fcdEQgrav.copy()
            elif self.general.fsyk == 500:
                if self.general.ColumnType == 2 and self.general.ColITER == 0:
                    CpFLAGfc = 333
                    self.general.ColITER = 1
                else:
                    CpFLAGfc = 1
        else: # check_Column_dims.m --> TODO: What do we do here?
            CpFLAGfc = 0
            aucx = np.where(self.column.Astair[0, :] > 0)[0]
            for i in range(self.general.nstoreys):
                CpFLAGX[i, aucx[0]] = max(CpFLAGX[i, aucx[0]], CpFLAGX[i, aucx[1]])
                CpFLAGY[i, aucx[0]] = max(CpFLAGY[i, aucx[0]], CpFLAGY[i, aucx[1]])
                CpFLAGX[i, aucx[1]] = CpFLAGX[i, aucx[0]].copy()
                CpFLAGY[i, aucx[1]] = CpFLAGY[i, aucx[0]].copy()
                CpFLAGX[i, aucx[2]] = max(CpFLAGX[i, aucx[2]], CpFLAGX[i, aucx[3]])
                CpFLAGY[i, aucx[2]] = max(CpFLAGY[i, aucx[2]], CpFLAGY[i, aucx[3]])
                CpFLAGX[i, aucx[3]] = CpFLAGX[i, aucx[2]].copy()
                CpFLAGY[i, aucx[3]] = CpFLAGY[i, aucx[2]].copy()
        # ...........................................................................
        # Checks if the design should be finished or not
        # ...........................................................................
        aux = np.sum(CpFLAGY) + np.sum(CpFLAGX) + auxbeam
        if aux > 0.99:
            print('Columns Not OK.... still %d to change!' % int(np.sum(CpFLAGY) + np.sum(CpFLAGX)))
            print('Maximum HX is %4.6f...' % float(np.max(np.max(self.column.HX))))
            print('Maximum HY is %4.6f...' % float(np.max(np.max(self.column.HY))))
            print('Minimum HX is %4.6f...' % float(np.min(np.min(self.column.HX))))
            print('Minimum HY is %4.6f...' % float(np.min(np.min(self.column.HY))))
            print('Maximum HX2 is %4.6f...' % float(np.max(np.max(self.column.HX[0, self.column.Colindex1]))))
            print('Maximum HY2 is %4.6f...' % float(np.max(np.max(self.column.HY[0, self.column.Colindex2]))))
            print('Minimum HX2 is %4.6f...' % float(np.min(np.min(self.column.HX[0, self.column.Colindex1]))))
            print('Minimum HY2 is %4.6f...' % float(np.min(np.min(self.column.HY[0, self.column.Colindex2]))))
        else:
            print('Columns OK. Stage 1 complete!')
            # ...........................................................................
            # Determination of the necessary reinforcement
            # ...........................................................................
            AsX = []
            AsY = []
            AsX_sw = []
            AsY_sw = []
            HX = self.column.HX.copy()
            HY = self.column.HY.copy()
            for i, icomb in enumerate(Combinations_2_use):
                # ...........................................................................
                # Determination of the necessary longitudinal rebar area
                # ...........................................................................
                NIU1 = -1 * self.column.Niu1[icomb]
                NIU9 = -1 * self.column.Niu9[icomb]
                MuX1 = np.abs(self.column.MuX1[icomb])
                MuX9 = np.abs(self.column.MuX9[icomb])
                MuY1 = np.abs(self.column.MuY1[icomb])
                MuY9 = np.abs(self.column.MuY9[icomb])
                # ...........................................................................
                lambdaX = 0.50 - cover / HX
                lambdaY = 0.50 - cover / HY
                betavector = [1.0, 1.00, 0.93, 0.88, 0.88, 0.93, 0.93]
                niuvector  = [-100, 0.40, 0.50, 0.60, 0.70, 0.85, 1000] # to cover those negative value for tensile forces HMA, original table does not include first and last terms
                beta1 = np.interp(NIU1, niuvector, betavector)
                beta9 = np.interp(NIU9, niuvector, betavector)
                niuc1 = NIU1 - 0.85
                niuc9 = NIU9 - 0.85
                omegaX = np.zeros(NIU1.shape)
                omegaY = np.zeros(NIU1.shape)
                AsXPos9 = omegaX.copy()
                AsXPos1 = omegaX.copy()
                AsYPos9 = omegaY.copy()
                AsYPos1 = omegaY.copy()
                # ...........................................................................
                for jj in range(NIU1.shape[0]):
                    for kk in range(NIU1.shape[1]):
                        if NIU1[jj, kk] < 0:
                            omegaX[jj, kk] = -NIU1[jj, kk] + (MuX1[jj, kk] / (beta1[jj, kk] * lambdaX[jj, kk])) # page 48 REBAP-83 EQ 22 (HMA)
                            omegaY[jj, kk] = -NIU1[jj, kk] + (MuY1[jj, kk] / (beta1[jj, kk] * lambdaY[jj, kk])) # page 48 REBAP-83 EQ 22 (HMA)
                        elif NIU1[jj, kk] <= 0.85:
                            omegaX[jj, kk]  = (MuX1[jj, kk] + 0.55 * NIU1[jj, kk] * niuc1[jj, kk]) / (beta1[jj, kk] * lambdaX[jj, kk])
                            omegaY[jj, kk]  = (MuY1[jj, kk] + 0.55 * NIU1[jj, kk] * niuc1[jj, kk]) / (beta1[jj, kk] * lambdaY[jj, kk])
                        else:
                            omegaX[jj, kk]  = (niuc1[jj, kk])+(MuX1[jj, kk] / (beta1[jj, kk] * lambdaX[jj, kk]))
                            omegaY[jj, kk]  = (niuc1[jj, kk])+(MuY1[jj, kk] / (beta1[jj, kk] * lambdaY[jj, kk]))

                        AsXPos1[jj, kk] = 0.50 * (omegaX[jj, kk] * HY[jj, kk] * HX[jj, kk] * fcd / fsyd)
                        AsYPos1[jj, kk] = 0.50 * (omegaY[jj, kk] * HY[jj, kk] * HX[jj, kk] * fcd / fsyd)
                        # ...........................................................................
                        if NIU9[jj, kk] < 0:
                            omegaX[jj, kk] = -NIU9[jj, kk] + (MuX9[jj, kk] / (beta9[jj, kk] * lambdaX[jj, kk])) # page 48 REBAP-83 EQ 22 (HMA)
                            omegaY[jj, kk] = -NIU9[jj, kk] + (MuY9[jj, kk] / (beta9[jj, kk] * lambdaY[jj, kk])) # page 48 REBAP-83 EQ 22 (HMA)
                        elif NIU9[jj, kk] <= 0.85:
                            omegaX[jj, kk]  = (MuX9[jj, kk] + 0.55 * NIU9[jj, kk] * niuc9[jj, kk]) / (beta9[jj, kk] * lambdaX[jj, kk])
                            omegaY[jj, kk]  = (MuY9[jj, kk] + 0.55 * NIU9[jj, kk] * niuc9[jj, kk]) / (beta9[jj, kk] * lambdaY[jj, kk])
                        else:
                            omegaX[jj, kk]  = (niuc9[jj, kk]) + (MuX9[jj, kk] / (beta9[jj, kk] * lambdaX[jj, kk]))
                            omegaY[jj, kk]  = (niuc9[jj, kk]) + (MuY9[jj, kk] / (beta9[jj, kk] * lambdaY[jj, kk]))
                        
                        AsXPos9[jj, kk] = 0.50 * (omegaX[jj, kk] * HY[jj, kk] * HX[jj, kk] * fcd / fsyd)
                        AsYPos9[jj, kk] = 0.50 * (omegaY[jj, kk] * HY[jj, kk] * HX[jj, kk] * fcd / fsyd)

                AsXPos1[AsXPos1 <= 0] = 0.000226195 # at least 2fi12mm will be placed, even if no need for the
                AsYPos1[AsYPos1 <= 0] = 0.000226195 # at least 2fi12mm will be placed, even if no need for the
                AsXPos9[AsXPos9 <= 0] = 0.000226195 # at least 2fi12mm will be placed, even if no need for the
                AsYPos9[AsYPos9 <= 0] = 0.000226195 # at least 2fi12mm will be placed, even if no need for the
                AsX.append(np.maximum(AsXPos1, AsXPos9))
                AsY.append(np.maximum(AsYPos1, AsYPos9))
                # ...........................................................................
                # Determination of the necessary transversal rebar area
                # ...........................................................................
                e_t_x1 = self.column.eccX1[icomb] / (0.90 * HX) # TO define big and small ecc. section for tensile force to discard concrete contribution for small ecc. (HMA)
                e_t_x9 = self.column.eccX9[icomb] / (0.90 * HX) # TO define big and small ecc. section for tensile force to discard concrete contribution for small ecc. (HMA)
                e_t_y1 = self.column.eccY1[icomb] / (0.90 * HY) # TO define big and small ecc. section for tensile force to discard concrete contribution for small ecc. (HMA)
                e_t_y9 = self.column.eccY9[icomb] / (0.90 * HY) # TO define big and small ecc. section for tensile force to discard concrete contribution for small ecc. (HMA)
                self.column.e_t_x1 = e_t_x1 + 0
                self.column.e_t_x9 = e_t_x9 + 0
                self.column.e_t_y1 = e_t_y1 + 0
                self.column.e_t_y9 = e_t_y9 + 0
                Ned1 = self.column.N1[icomb] + 0
                Ned9 = self.column.N9[icomb] + 0
                VedX1 = self.column.V1_x[icomb] + 0
                VedY1 = self.column.V1_y[icomb] + 0
                VedX9 = self.column.V9_x[icomb] + 0
                VedY9 = self.column.V9_y[icomb] + 0
                VcdX = tau1 * HY * 0.9 * HX  # tau*B*0.90*H, 0.90H = useful height
                VcdY = tau1 * HX * 0.9 * HY
                VswconstX = 0.9 * 0.9 * HX * 1000 * fsyd  # 53.3 rebap, assuming vertical stirrups
                VswconstY = 0.9 * 0.9 * HY * 1000 * fsyd  # 53.3 rebap, assuming vertical stirrups
                Asw_sX1 = np.zeros(VcdX.shape)
                Asw_sY1 = np.zeros(VcdX.shape)
                Asw_sX9 = np.zeros(VcdX.shape)
                Asw_sY9 = np.zeros(VcdX.shape)
                AsX_sww = np.zeros(VcdX.shape)
                AsY_sww = np.zeros(VcdX.shape)
                for jj in range(VcdX.shape[0]):
                    for kk in range(VcdX.shape[1]):
                        if Ned1[jj, kk] > 0 and abs(e_t_x1[jj, kk]) < 0.5: # tensile force with small eccentricity (cracked concrete) (HMA)   
                            Asw_sX1[jj, kk] = abs(VedX1[jj, kk] / VswconstX[jj, kk])  # 53.3 rebap, assuming vertical stirrups
                        else:
                            Asw_sX1[jj, kk] = (abs(VedX1[jj, kk]) - VcdX[jj, kk]) / VswconstX[jj, kk] # 53.3 rebap, assuming vertical stirrups

                        if Ned1[jj, kk] > 0 and abs(e_t_y1[jj, kk]) < 0.5:  # tensile force with small eccentricity (cracked concrete) (HMA) 
                            Asw_sY1[jj, kk] = abs(VedY1[jj, kk]) / VswconstY[jj, kk]  # 53.3 rebap, assuming vertical stirrups
                        else:
                            Asw_sY1[jj, kk] = (abs(VedY1[jj, kk]) - VcdY[jj, kk]) / VswconstY[jj, kk] # 53.3 rebap, assuming vertical stirrups    

                        if Ned9[jj, kk] > 0 and abs(e_t_x9[jj, kk]) < 0.5:  # tensile force with small eccentricity (cracked concrete) (HMA)
                            Asw_sX9[jj, kk] = abs(VedX9[jj, kk]) / VswconstX[jj, kk]  # 53.3 rebap, assuming vertical stirrups
                        else:
                            Asw_sX9[jj, kk] = (abs(VedX9[jj, kk]) - VcdX[jj, kk]) / VswconstX[jj, kk]  # 53.3 rebap, assuming vertical stirrups
 
                        if Ned9[jj, kk] > 0 and abs(e_t_y9[jj, kk]) < 0.5:  # tensile force with small eccentricity (cracked concrete)  (HMA)
                            Asw_sY9[jj, kk] = abs(VedY9[jj, kk]) / VswconstY[jj, kk]  # 53.3 rebap, assuming vertical stirrups
                        else:
                            Asw_sY9[jj, kk] = (abs(VedY9[jj, kk]) - VcdY[jj, kk])/VswconstY[jj, kk]  # 53.3 rebap, assuming vertical stirrups
                        AsX_sww[jj, kk] = max(Asw_sX1[jj, kk], Asw_sX9[jj, kk])
                        AsY_sww[jj, kk] = max(Asw_sY1[jj, kk], Asw_sY9[jj, kk])

                if fsyd < 230:
                    Asw_sminX = 0.16 * HY / 100
                    Asw_sminY = 0.16 * HX / 100
                elif fsyd < 400:
                    Asw_sminX = 0.10 * HY / 100
                    Asw_sminY = 0.10 * HX / 100
                else:
                    Asw_sminX = 0.08 * HY / 100
                    Asw_sminY = 0.08 * HX / 100
                AsX_sw.append(np.maximum(AsX_sww, Asw_sminX))
                AsY_sw.append(np.maximum(AsY_sww, Asw_sminY))

            self.column.AsX = np.max(np.array(AsX), axis=0)
            self.column.AsY = np.max(np.array(AsY), axis=0)
            self.column.AsX_sw = np.max(np.array(AsX_sw), axis=0)
            self.column.AsY_sw = np.max(np.array(AsY_sw), axis=0)
            sw_max = 1.0 * HX
            # ...........................................................................
            # Get the rebar solution
            # ...........................................................................
            attributes = ['fi_corner', 'fi_layintX', 'nbar_HminusX', 'nlayintX', 'Rhosl', 'RhoslX', 'RhoslY', 'nintBOT', 'sw', 'fiw', 'nwparallel_to_X', 'nwparallel_to_Y']
            for attr in attributes:
                setattr(self.column, attr, np.zeros(self.column.AsX.shape))
            for jj in range(self.column.AsX.shape[1]):
                self.column.fi_corner[:, jj], self.column.fi_layintX[:, jj], self.column.nbar_HminusX[:, jj], self.column.nlayintX[:, jj], self.column.Rhosl[:, jj], self.column.RhoslX[:, jj], self.column.RhoslY[:, jj], self.column.sw[:, jj], self.column.fiw[:, jj], self.column.nwparallel_to_X[:, jj], self.column.nwparallel_to_Y[:, jj] = _get_column_rebars(self.column.AsX[:, jj], self.column.AsY[:, jj], HX[:, jj], HY[:, jj], rho_min, dmin, dmax, cover, self.column.AsX_sw[:, jj], self.column.AsY_sw[:, jj], sw_min_over_fi, sw_max[:, jj], fiw_min)
            # ...........................................................................
            # Save stuff
            # ...........................................................................
            nrow = self.column.name.shape[0] * self.column.name.shape[1]
            ncol = 27
            self.column.Matrix = np.zeros((nrow, ncol))
            self.column.Matrix[:, 0] = (self.column.name.T).flatten()
            self.column.Matrix[:, 1] = (self.column.elasnodei.T).flatten() + 7000
            self.column.Matrix[:, 2] = (self.column.elasnodej.T).flatten() + 2000
            self.column.Matrix[:, 3] = (self.column.HX.T).flatten()
            self.column.Matrix[:, 4] = (self.column.HY.T).flatten()
            self.column.Matrix[:, 5] = (self.column.L.T).flatten()
            self.column.Matrix[:, 6] = (self.column.storey.T).flatten()
            self.column.Matrix[:, 7] = (self.column.perimeter.T).flatten()
            self.column.Matrix[:, 8] = (self.column.nbar_HminusX.T).flatten()
            self.column.Matrix[:, 9]  = (self.column.nlayintX.T).flatten()
            self.column.Matrix[:, 10]  = (self.column.fi_corner.T).flatten()
            self.column.Matrix[:, 11] = (self.column.fi_layintX.T).flatten()
            self.column.Matrix[:, 12] = (self.column.Rhosl.T).flatten()
            self.column.Matrix[:, 13] = (self.column.sw.T).flatten()
            self.column.Matrix[:, 14] = (self.column.fiw.T).flatten()
            self.column.Matrix[:, 15] = (self.column.nwparallel_to_X.T).flatten()
            self.column.Matrix[:, 16] = (self.column.nwparallel_to_Y.T).flatten()
            self.column.Matrix[:, 17] = (self.column.N_EQfinal.T).flatten()
            # ...........................................................................
            # Checking the maximum rho_l condition
            # ...........................................................................
            if np.max(self.column.Rhosl) > rho_max:
                aux1 = self.column.Rhosl > rho_max
                aux2 = self.column.Rhosl <= rho_max
                CpFLAGX[aux1] = 1
                CpFLAGX[aux2] = 0
                CpFLAGY[aux1] = 1
                CpFLAGY[aux2] = 0      

            aucx = np.where(self.column.Astair[0, :] > 0)[0]
            for i in range(self.general.nstoreys):
                CpFLAGX[i, aucx[0]] = max(CpFLAGX[i, aucx[0]], CpFLAGX[i, aucx[1]])
                CpFLAGY[i, aucx[0]] = max(CpFLAGY[i, aucx[0]], CpFLAGY[i, aucx[1]])
                CpFLAGX[i, aucx[1]] = CpFLAGX[i, aucx[0]]
                CpFLAGY[i, aucx[1]] = CpFLAGY[i, aucx[0]]
                CpFLAGX[i, aucx[2]] = max(CpFLAGX[i, aucx[2]], CpFLAGX[i, aucx[3]])
                CpFLAGY[i, aucx[2]] = max(CpFLAGY[i, aucx[2]], CpFLAGY[i, aucx[3]])
                CpFLAGX[i, aucx[3]] = CpFLAGX[i, aucx[2]]
                CpFLAGY[i, aucx[3]] = CpFLAGY[i, aucx[2]]

            aux = np.sum(CpFLAGY) + np.sum(CpFLAGX) + auxbeam
            if aux > 0:
                print('Columns Not OK...the maximum Rho_l condition... still %d to change' % int(sum(CpFLAGY.flatten()) + sum(CpFLAGX.flatten())))
            else:
                print('Columns Rho_l condition OK!')

        return CpFLAGX, CpFLAGY, CpFLAGfc, aux

    def _cdh_beams(self):
        """
        Designs columns usign DCH properties
        Refrences: Eurocode 2 and Eurocode 8-1
        1) The maximum bending moment of the alignement (max of all M1s and of all M9s) is used to assess the maximum As-.
        2) The maximum bending momento of the mid spans (max of all M5s) is used to compute the required As+.
        3) The corresponding solution in terms of rebars is calculated for As- ans As+ usign the same diameter.
        4) Calculate the rebar solution and exports the key elements for the nonlinear modelling
        TODO: The routine is very similar to cdh_beams, convert some stuff to functions to avoid repetition
        """
        # ...........................................................................
        # Variables for the design based on the DCH Design Routines
        # ...........................................................................
        niu1 = 0.60 # Eurocode 2 (EQ.6.9) TODO: (EQ.6.10aN)?
        cota = 2.50 # theta is 21.8º degrees
        taumax = (1.0 * 0.90 * niu1 * self.general.fcd * 1000) / cota # Eurocode 2 (EQ.6.5) TODO: I think this is different?
        fck = self.general.fck + 0
        fcd = self.general.fcd + 0
        fsyd = self.general.fsyd + 0
        fsyk = self.general.fsyk + 0
        fctm = 0.3 * self.general.fck ** (2/3)
        fcm = self.general.fck + 8
        Ec = 5000 * (fcm ** 0.5) # TODO: computed but not used
        Gc = Ec / (2 * (1 + 0.2)) # TODO: computed but not used
        epsc0 = 2/1000 # TODO: computed but not used
        epscU = 3.5/1000
        esy = self.general.fsyk / 200000
        if self.general.fck < 27.6: # are they from eurocode?
            betafc = 0.85
        elif self.general.fck > 55.17:
            betafc = 0.65
        else:
            betafc = 1.05 - 0.05 * self.general.fck / 6.9
        if self.general.fck <= 50:
            k1 = 0.44
            k2 = 1.25 * (0.6 + 0.0014 / 3.5e-3)
            xOvD = 0.25 # maximum x/d ratio
            deltaMax = max(0.7, k1 + k2 * xOvD) # TODO: computed but not used
        else:
            epscU2 = np.mean([3.1, 2.9, 2.7, 2.6, 2.6]) / 1000
            k3 = 0.54
            k4 = 1.25 * (0.6 + 0.0014 / epscU2)
            xOvD = 0.15 # maximum x/d ratio 
            deltaMax = max([0.7, k3 + k4 * xOvD]) # TODO: computed but not used
        cover = 0.03
        miueconomic = 0.25 # value to start design for the chart in eurocode
        top_to_bot_ratio = 0.50 # Ratio of compressive to tensile reinforcement ratio
        dmax_between_long_bars = 0.10 # code enforcement
        k1 = 0.810
        k2 = 0.416
        rhomin_tens = 0.50 * (fctm / fsyk) # minimum tensile reinforcement ratio
        sw_min_over_fi = 8 # minimum of the ratio of spacing between stirrup diameter
        dmin = 0.04 # minimum distance between rebars
        # ...........................................................................
        # Verifies the adequacy of the sectional dimensions
        # ...........................................................................
        alignmentsX = np.unique(self.beamX.index)
        CvFLAGX = np.zeros((self.general.nstoreys, self.beamX.index.shape[0]))
        for i in range(len(alignmentsX)):
            mask = self.beamX.index == alignmentsX[i]
            for j in range(self.general.nstoreys):
                BB = self.beamX.BB[f'{i}, {j}'].copy()
                HH = self.beamX.HH[f'{i}, {j}'].copy()
                moment_plus = self.beamX.MomentEnvelopePlusCDH[f'{i}, {j}'].copy()
                moment_neg = self.beamX.MomentEnvelopeNegCDH[f'{i}, {j}'].copy()
                maximum_shear = self.beamX.ShearEnvelopeCDH[f'{i}, {j}'].copy()
                muplusX = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                munegX = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                tauX = np.abs(maximum_shear) / (BB * (0.90 * HH))
                if max(muplusX) > miueconomic or max(munegX) > miueconomic or max(tauX) > taumax:
                    CvFLAGX[j, mask] = 1 # not satisfied
                else:
                    CvFLAGX[j, mask] = 0 # satisfied
        # ...........................................................................
        alignmentsY = np.unique(self.beamY.index)
        CvFLAGY = np.zeros((self.general.nstoreys, self.beamY.index.shape[0]))
        for i in range(len(alignmentsY)):
            mask = self.beamY.index == alignmentsY[i]
            for j in range(self.general.nstoreys):
                BB = self.beamY.BB[f'{i}, {j}'].copy()
                HH = self.beamY.HH[f'{i}, {j}'].copy()
                moment_plus = self.beamY.MomentEnvelopePlusCDH[f'{i}, {j}'].copy()
                moment_neg = self.beamY.MomentEnvelopeNegCDH[f'{i}, {j}'].copy()
                maximum_shear = self.beamY.ShearEnvelopeCDH[f'{i}, {j}'].copy()
                muplusY = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                munegY = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                tauY = np.abs(maximum_shear) / (BB * (0.90 * HH))
                if max(muplusY) > miueconomic or max(munegY) > miueconomic or max(tauY) > taumax:
                    CvFLAGY[j, mask] = 1 # not satisfied
                else:
                    CvFLAGY[j, mask] = 0 # satisfied
        # ...........................................................................
        CvFLAGStair = np.zeros(self.general.nstoreys)
        for j in range(self.general.nstoreys):
            BB = self.beamStair.BB[f'{j}'].copy()
            HH = self.beamStair.HH[f'{j}'].copy()
            moment_plus = self.beamStair.MomentEnvelopePlusCDH[f'{j}'].copy()
            moment_neg = self.beamStair.MomentEnvelopeNegCDH[f'{j}'].copy()
            maximum_shear = self.beamStair.ShearEnvelopeCDH[f'{j}'].copy()
            muplusStair = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
            munegStair = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
            tauStair = np.abs(maximum_shear) / (BB * (0.90 * HH))
            if max(muplusStair) > miueconomic or max(munegStair) > miueconomic or max(tauStair) > taumax:
                CvFLAGStair[j] = 1 # not satisfied
            else:
                CvFLAGStair[j] = 0 # satisfied
        # ...........................................................................
        # Verifies the need for a new section
        # ...........................................................................
        auxbeam = np.sum(CvFLAGX) + np.sum(CvFLAGY) + np.sum(CvFLAGStair)
        if auxbeam > 0.99:
            print(f"Beams Not OK ... still {auxbeam:.0f} to change")
        else:
            print("Beams stage 1 complete")
            # ...........................................................................
            # When ok, selects the longitudinal steel rebar solution and the tranverse steel rebar solution
            # ...........................................................................
            mulim = 0.31
            omegalim = 0.41
            # ...........................................................................
            # BeamX
            NeededAsTOPX = {}
            NeededAsBOTX = {}
            NeededAsw_sX = {}
            swmax_X = {}
            self.beamX.NeededAsTOP = {}
            self.beamX.NeededAsBOT = {}
            self.beamX.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                for i in range(len(alignmentsX)):
                    BB = self.beamX.BB[f'{i}, {j}'].copy()
                    HH = self.beamX.HH[f'{i}, {j}'].copy()
                    moment_plus = self.beamX.MomentEnvelopePlusCDH[f'{i}, {j}'].copy()
                    moment_neg = self.beamX.MomentEnvelopeNegCDH[f'{i}, {j}'].copy()
                    maximum_shear = self.beamX.ShearEnvelopeCDH[f'{i}, {j}'].copy()
                    moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                    moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                    # ...........................................................................
                    muplusX = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                    munegX = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                    # ...........................................................................
                    omega_plusX_prime = (muplusX - mulim) / (1 - (cover / (0.90 * HH)))
                    omega_plusX_prime[muplusX <= mulim] = 0
                    omega_plusX = omegalim + omega_plusX_prime
                    omega_plusX[muplusX <= mulim] = muplusX[muplusX <= mulim] * (1 + muplusX[muplusX <= mulim])
                    # ...........................................................................
                    omega_negX_prime = (munegX - mulim) / (1 - (cover / (0.90 * HH)))
                    omega_negX_prime[munegX <= mulim] = 0
                    omega_negX = omegalim + omega_negX_prime
                    omega_negX[munegX <= mulim] = munegX[munegX <= mulim] * (1 + munegX[munegX <= mulim])
                    # ...........................................................................
                    omega_plusX = np.maximum(omega_plusX, omega_negX_prime)
                    omega_negX = np.maximum(omega_negX, omega_plusX_prime)
                    # ...........................................................................
                    AsminTOPX = rhomin_tens * BB * 0.90 * HH                          
                    AsminBOTX = rhomin_tens * BB * 0.90 * HH
                    AsTOPX = np.maximum(omega_negX * BB * 0.90 * HH * fcd / fsyd, AsminTOPX)
                    AsBOTX = np.maximum(omega_plusX * BB * 0.90 * HH * fcd / fsyd, AsminBOTX)
                    NeededAsTOPX[f'{i}, {j}'] = AsTOPX.copy()
                    NeededAsBOTX[f'{i}, {j}'] = AsBOTX.copy()
                    self.beamX.NeededAsTOP[f'{i}, {j}'] = AsTOPX.copy()
                    self.beamX.NeededAsBOT[f'{i}, {j}'] = AsBOTX.copy()
                    # ...........................................................................
                    # rhoplus = omega_negX * (fcd / fsyd)
                    # k_d_V = 1 + (200 / (1000 * 0.90 * HH))**0.5                 # Eurocode 2 (EQ.6.2B)
                    # tau1 = 0.12 * (k_d_V) * (100 * rhoplus *fck) ** (1/3)       # Eurocode 2 (EQ.6.2b)
                    tau1 = 0.0
                    VcdX = 1000 * tau1 * BB * 0.9 * HH
                    VswconstX = 0.9 * 0.9 * HH * 1000 * fsyd                      # 53.3 rebap, assuming vertical stirrups
                    Asw_minX = (0.08 * (fck**0.5) / fsyk) * BB
                    Asw_sX = (np.abs(maximum_shear) - VcdX) / VswconstX           # 53.3 rebap, assuming vertical stirrups
                    Asw_sX[Asw_sX < Asw_minX] = Asw_minX[Asw_sX<Asw_minX]         # 53.3 rebap, assuming vertical stirrups
                    NeededAsw_sX[f'{i}, {j}'] = Asw_sX.copy()
                    swmax_X[f'{i}, {j}'] = np.minimum(HH / 4, 0.225)
                    self.beamX.NeededAsw_s[f'{i}, {j}'] = Asw_sX.copy()
            # ...........................................................................
            # BeamY
            NeededAsTOPY = {}
            NeededAsBOTY = {}
            NeededAsw_sY = {}
            swmax_Y = {}
            self.beamY.NeededAsTOP = {}
            self.beamY.NeededAsBOT = {}
            self.beamY.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                for i in range(len(alignmentsY)):
                    BB = self.beamY.BB[f'{i}, {j}'].copy()
                    HH = self.beamY.HH[f'{i}, {j}'].copy()
                    moment_plus = self.beamY.MomentEnvelopePlusCDH[f'{i}, {j}'].copy()
                    moment_neg = self.beamY.MomentEnvelopeNegCDH[f'{i}, {j}'].copy()
                    maximum_shear = self.beamY.ShearEnvelopeCDH[f'{i}, {j}'].copy()
                    moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                    moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                    # ...........................................................................
                    muplusY = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                    munegY = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                    # ...........................................................................
                    omega_plusY_prime = (muplusY - mulim) / (1 - (cover / (0.90 * HH)))
                    omega_plusY_prime[muplusY <= mulim] = 0
                    omega_plusY = omegalim + omega_plusY_prime
                    omega_plusY[muplusY <= mulim] = muplusY[muplusY <= mulim] * (1 + muplusY[muplusY <= mulim])
                    # ...........................................................................
                    omega_negY_prime = (munegY - mulim) / (1 - (cover / (0.90 * HH)))
                    omega_negY_prime[munegY <= mulim] = 0
                    omega_negY = omegalim + omega_negY_prime
                    omega_negY[munegY <= mulim] = munegY[munegY <= mulim] * (1 + munegY[munegY <= mulim])
                    # ...........................................................................
                    omega_plusY = np.maximum(omega_plusY, omega_negY_prime)
                    omega_negY = np.maximum(omega_negY, omega_plusY_prime)
                    # ...........................................................................
                    AsminTOPY = rhomin_tens * BB * 0.90 * HH                          
                    AsminBOTY = rhomin_tens * BB * 0.90 * HH
                    AsTOPY = np.maximum(omega_negY * BB * 0.90 * HH * fcd / fsyd, AsminTOPY)
                    AsBOTY = np.maximum(omega_plusY * BB * 0.90 * HH * fcd / fsyd, AsminBOTY)
                    NeededAsTOPY[f'{i}, {j}'] = AsTOPY.copy()
                    NeededAsBOTY[f'{i}, {j}'] = AsBOTY.copy()
                    self.beamY.NeededAsTOP[f'{i}, {j}'] = AsTOPY.copy()
                    self.beamY.NeededAsBOT[f'{i}, {j}'] = AsBOTY.copy()
                    # ...........................................................................
                    # rhoplus = omega_negX * (fcd / fsyd)
                    # k_d_V = 1 + (200 / (1000 * 0.90 * HH))**0.5                 # Eurocode 2 (EQ.6.2B)
                    # tau1 = 0.12 * (k_d_V) * (100 * rhoplus *fck) ** (1/3)       # Eurocode 2 (EQ.6.2b)
                    tau1 = 0.0
                    VcdY = 1000 * tau1 * BB * 0.9 * HH
                    VswconstY = 0.9 * 0.9 * HH * 1000 * fsyd                      # 53.3 rebap, assuming vertical stirrups
                    Asw_minY = (0.08 * (fck**0.5) / fsyk) * BB
                    Asw_sY = (np.abs(maximum_shear) - VcdY) / VswconstY           # 53.3 rebap, assuming vertical stirrups
                    Asw_sY[Asw_sY < Asw_minY] = Asw_minY[Asw_sY<Asw_minY]         # 53.3 rebap, assuming vertical stirrups
                    NeededAsw_sY[f'{i}, {j}'] = Asw_sY.copy()
                    swmax_Y[f'{i}, {j}'] = np.minimum(HH / 4, 0.225)
                    self.beamY.NeededAsw_s[f'{i}, {j}'] = Asw_sY.copy()
            # ...........................................................................
            # BeamStair
            NeededAsTOPStair = {}
            NeededAsBOTStair = {}
            NeededAsw_sStair = {}
            swmax_Stair = {}
            self.beamStair.NeededAsTOP = {}
            self.beamStair.NeededAsBOT = {}
            self.beamStair.NeededAsw_s = {}
            for j in range(self.general.nstoreys):
                BB = self.beamStair.BB[f'{j}'].copy()
                HH = self.beamStair.HH[f'{j}'].copy()
                moment_plus = self.beamStair.MomentEnvelopePlusCDH[f'{j}'].copy()
                moment_neg = self.beamStair.MomentEnvelopeNegCDH[f'{j}'].copy()
                maximum_shear = self.beamStair.ShearEnvelopeCDH[f'{j}'].copy()
                moment_plus[moment_plus < 0] = 0 # for just to have the real envelope (by HMA)
                moment_neg[moment_neg > 0] = 0 # for just to have the real envelope (by HMA)
                # ...........................................................................
                muplusStair = np.abs(moment_plus) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                munegStair = np.abs(moment_neg) / (BB * ((0.90 * HH) ** 2) * fcd * 1000)
                # ...........................................................................
                omega_plusStair_prime = (muplusStair - mulim) / (1 - (cover / (0.90 * HH)))
                omega_plusStair_prime[muplusStair <= mulim] = 0
                omega_plusStair = omegalim + omega_plusStair_prime
                omega_plusStair[muplusStair <= mulim] = muplusStair[muplusStair <= mulim] * (1 + muplusStair[muplusStair <= mulim])
                # ...........................................................................
                omega_negStair_prime = (munegStair - mulim) / (1 - (cover / (0.90 * HH)))
                omega_negStair_prime[munegStair <= mulim] = 0
                omega_negStair = omegalim + omega_negStair_prime
                omega_negStair[munegStair <= mulim] = munegStair[munegStair <= mulim] * (1 + munegStair[munegStair <= mulim])
                # ...........................................................................
                omega_plusStair = np.maximum(omega_plusStair, omega_negStair_prime)
                omega_negStair = np.maximum(omega_negStair, omega_plusStair_prime)
                # ...........................................................................
                AsminTOPStair = rhomin_tens * BB * 0.90 * HH                          
                AsminBOTStair = rhomin_tens * BB * 0.90 * HH
                AsTOPStair = np.maximum(omega_negStair * BB * 0.90 * HH * fcd / fsyd, AsminTOPStair)
                AsBOTStair = np.maximum(omega_plusStair * BB * 0.90 * HH * fcd / fsyd, AsminBOTStair)
                NeededAsTOPStair[f'{j}'] = AsTOPStair.copy()
                NeededAsBOTStair[f'{j}'] = AsBOTStair.copy()
                self.beamStair.NeededAsTOP[f'{j}'] = AsTOPStair.copy()
                self.beamStair.NeededAsBOT[f'{j}'] = AsBOTStair.copy()
                # ...........................................................................
                # rhoplus = omega_negX * (fcd / fsyd)
                # k_d_V = 1 + (200 / (1000 * 0.90 * HH))**0.5                 # Eurocode 2 (EQ.6.2B)
                # tau1 = 0.12 * (k_d_V) * (100 * rhoplus *fck) ** (1/3)       # Eurocode 2 (EQ.6.2b)
                tau1 = 0.0
                VcdStair = 1000 * tau1 * BB * 0.9 * HH
                VswconstStair = 0.9 * 0.9 * HH * 1000 * fsyd                                    # 53.3 rebap, assuming vertical stirrups
                Asw_minStair = (0.08 * (fck**0.5) / fsyk) * BB
                Asw_sStair = (np.abs(maximum_shear) - VcdStair) / VswconstStair                 # 53.3 rebap, assuming vertical stirrups
                Asw_sStair[Asw_sStair < Asw_minStair] = Asw_minStair[Asw_sStair<Asw_minStair]   # 53.3 rebap, assuming vertical stirrups
                NeededAsw_sStair[f'{j}'] = Asw_sStair.copy()
                swmax_Stair[f'{j}'] = np.minimum(HH / 4, 0.225)
                self.beamStair.NeededAsw_s[f'{j}'] = Asw_sStair.copy()
            # ...........................................................................
            # Starts selecting the longitudinal steel rebar solution and the tranverse steel rebar solution
            # ...........................................................................
            attributes = ['ficornerTOP', 'ncornerTOP', 'fiintTOP', 'nintTOP', 'ficornerBOT', 'ncornerBOT', 'fiintBOT', 'nintBOT', 'fiw', 'sw', 'nwparallel_to_b', 'nwparallel_to_h']
            for attr in attributes:
                val = {f'{i}, {j}':None for i in range(len(alignmentsX)) for j in range(self.general.nstoreys)}
                setattr(self.beamX, attr, val)
                val = {f'{i}, {j}':None for i in range(len(alignmentsY)) for j in range(self.general.nstoreys)}
                setattr(self.beamY, attr, val)
                val = {f'{j}':None  for j in range(self.general.nstoreys)}
                setattr(self.beamStair, attr, val)
            # ...........................................................................
            for i in range(len(alignmentsX)):            
                for j in range(self.general.nstoreys):
                    self.beamX.ficornerTOP[f'{i}, {j}'], self.beamX.ncornerTOP[f'{i}, {j}'], self.beamX.fiintTOP[f'{i}, {j}'], self.beamX.nintTOP[f'{i}, {j}'], self.beamX.ficornerBOT[f'{i}, {j}'], self.beamX.ncornerBOT[f'{i}, {j}'], self.beamX.fiintBOT[f'{i}, {j}'], self.beamX.nintBOT[f'{i}, {j}'], self.beamX.fiw[f'{i}, {j}'], self.beamX.sw[f'{i}, {j}'], self.beamX.nwparallel_to_b[f'{i}, {j}'], self.beamX.nwparallel_to_h[f'{i}, {j}'] = _get_beam_rebars(NeededAsBOTX[f'{i}, {j}'], NeededAsTOPX[f'{i}, {j}'], self.beamX.BB[f'{i}, {j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sX[f'{i}, {j}'], swmax_X[f'{i}, {j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            for i in range(len(alignmentsY)):
                for j in range(self.general.nstoreys):
                    self.beamY.ficornerTOP[f'{i}, {j}'], self.beamY.ncornerTOP[f'{i}, {j}'], self.beamY.fiintTOP[f'{i}, {j}'], self.beamY.nintTOP[f'{i}, {j}'], self.beamY.ficornerBOT[f'{i}, {j}'], self.beamY.ncornerBOT[f'{i}, {j}'], self.beamY.fiintBOT[f'{i}, {j}'], self.beamY.nintBOT[f'{i}, {j}'], self.beamY.fiw[f'{i}, {j}'], self.beamY.sw[f'{i}, {j}'], self.beamY.nwparallel_to_b[f'{i}, {j}'], self.beamY.nwparallel_to_h[f'{i}, {j}'] = _get_beam_rebars(NeededAsBOTY[f'{i}, {j}'], NeededAsTOPY[f'{i}, {j}'], self.beamY.BB[f'{i}, {j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sY[f'{i}, {j}'], swmax_Y[f'{i}, {j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            for j in range(self.general.nstoreys):
                self.beamStair.ficornerTOP[f'{j}'], self.beamStair.ncornerTOP[f'{j}'], self.beamStair.fiintTOP[f'{j}'], self.beamStair.nintTOP[f'{j}'], self.beamStair.ficornerBOT[f'{j}'], self.beamStair.ncornerBOT[f'{j}'], self.beamStair.fiintBOT[f'{j}'], self.beamStair.nintBOT[f'{j}'], self.beamStair.fiw[f'{j}'], self.beamStair.sw[f'{j}'], self.beamStair.nwparallel_to_b[f'{j}'], self.beamStair.nwparallel_to_h[f'{j}'] = _get_beam_rebars(NeededAsBOTStair[f'{j}'], NeededAsTOPStair[f'{j}'], self.beamStair.BB[f'{j}'], top_to_bot_ratio, dmax_between_long_bars, NeededAsw_sStair[f'{j}'], swmax_Stair[f'{j}'], sw_min_over_fi, dmin) 
            # ...........................................................................
            # uniformize the number of rebars at each common section 
            # (section 9 from  previous to 1 from next) at the same alignment 
            # -xx (HMA)
            attributes = ['BBbb', 'DDdd']
            for attr in attributes:
                val = {f'{j}, {i}':None for i in range(len(alignmentsX)) for j in range(self.general.nstoreys)}
                setattr(self.beamX, attr, val)
                val = {f'{j}, {i}':None for i in range(len(alignmentsY)) for j in range(self.general.nstoreys)}
                setattr(self.beamY, attr, val)

            for j in range(self.general.nstoreys): # loop over the storeys
                for i in range(len(alignmentsX)): # loop over the alignment
                    aa = self.beamX.ncornerTOP[f'{i}, {j}']
                    bb = self.beamX.nintTOP[f'{i}, {j}']
                    cc = self.beamX.ncornerBOT[f'{i}, {j}']
                    dd = self.beamX.nintBOT[f'{i}, {j}']
                    for kk in range(2, len(dd)-3, 3):
                        aa[kk] = max(aa[kk], aa[kk+1])
                        aa[kk+1] = max(aa[kk], aa[kk+1])
                        bb[kk] = max(bb[kk], bb[kk+1])
                        bb[kk+1] = max(bb[kk], bb[kk+1])
                        cc[kk] = max(cc[kk], cc[kk+1])
                        cc[kk+1] = max(cc[kk], cc[kk+1])
                        dd[kk] = max(dd[kk], dd[kk+1])
                        dd[kk+1] = max(dd[kk], dd[kk+1])

                    self.beamX.ncornerTOP[f'{i}, {j}'] = aa.copy()
                    self.beamX.nintTOP[f'{i}, {j}'] = bb.copy()
                    self.beamX.ncornerBOT[f'{i}, {j}'] = cc.copy()
                    self.beamX.nintBOT[f'{i}, {j}'] = dd.copy()
                    self.beamX.BBbb[f'{i}, {j}'] = bb.copy()
                    self.beamX.DDdd[f'{i}, {j}'] = dd.copy()

            # -yy (HMA)
            for j in range(self.general.nstoreys): # loop over the storeys
                for i in range(len(alignmentsY)): # loop over the alignement
                    aa = self.beamY.ncornerTOP[f'{i}, {j}']
                    bb = self.beamY.nintTOP[f'{i}, {j}']
                    cc = self.beamY.ncornerBOT[f'{i}, {j}']
                    dd = self.beamY.nintBOT[f'{i}, {j}']
                    for kk in range(2, len(dd)-3, 3):
                        aa[kk] = max(aa[kk], aa[kk+1])
                        aa[kk+1] = max(aa[kk], aa[kk+1])
                        bb[kk] = max(bb[kk], bb[kk+1])
                        bb[kk+1] = max(bb[kk], bb[kk+1])
                        cc[kk] = max(cc[kk], cc[kk+1])
                        cc[kk+1] = max(cc[kk], cc[kk+1])
                        dd[kk] = max(dd[kk], dd[kk+1])
                        dd[kk+1] = max(dd[kk], dd[kk+1])

                    self.beamY.ncornerTOP[f'{i}, {j}'] = aa.copy()
                    self.beamY.nintTOP[f'{i}, {j}'] = bb.copy()
                    self.beamY.ncornerBOT[f'{i}, {j}'] = cc.copy()
                    self.beamY.nintBOT[f'{i}, {j}'] = dd.copy()
                    self.beamY.BBbb[f'{i}, {j}'] = bb.copy()
                    self.beamY.DDdd[f'{i}, {j}'] = dd.copy()
            # ...........................................................................
            # Calculation of My for the beams in -XX
            # ...........................................................................
            neles = len(self.beamX.Area.flatten())
            pedXEQ = self.beamX.pedEQFinal.copy()
            pedXEQ[-1, :] = self.beamX.proofEQFinal[-1, :]
            pedXEQ = pedXEQ.flatten()
            self.beamX.Matrix = np.zeros((neles, 42))
            iele  = 0
            for j in range(self.general.nstoreys): # loop over the storeys
                auxMyPos = np.array([])
                auxMyNeg = np.array([])
                for i in range(len(alignmentsX)): # loop over the alignment
                    namesly = self.beamX.NName[f'{i}, {j}']
                    nodeily = self.beamX.NNodei[f'{i}, {j}']
                    nodejly = self.beamX.NNodej[f'{i}, {j}']
                    HHly    = self.beamX.HH[f'{i}, {j}']
                    BBly    = self.beamX.BB[f'{i}, {j}']
                    LLly    = self.beamX.LL[f'{i}, {j}']
                    Ntopc   = self.beamX.ncornerTOP[f'{i}, {j}']
                    Ftopc   = self.beamX.ficornerTOP[f'{i}, {j}']
                    Ntopi   = self.beamX.nintTOP[f'{i}, {j}']
                    Ftopi   = self.beamX.fiintTOP[f'{i}, {j}']
                    Nbotc   = self.beamX.ncornerBOT[f'{i}, {j}']
                    Fbotc   = self.beamX.ficornerBOT[f'{i}, {j}']
                    Nboti   = self.beamX.nintBOT[f'{i}, {j}']
                    Fboti   = self.beamX.fiintBOT[f'{i}, {j}']
                    fiw     = self.beamX.fiw[f'{i}, {j}']
                    sw      = self.beamX.sw[f'{i}, {j}']
                    nwparallel_to_b = self.beamX.nwparallel_to_b[f'{i}, {j}']
                    nwparallel_to_h = self.beamX.nwparallel_to_h[f'{i}, {j}']
                    # ...........................................................................
                    dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                    dD_line  = 1000 * HHly - dD                                                               # in mm
                    cB       = (epscU * dD) / (epscU + esy)
                    Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    Ec       = (57000 * (fcd * 145)**0.5) / 145
                    Es       = 200000
                    nyoung   = Es / Ec
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control = np.ones(dD.shape)
                    AtoUse  = AtensCntrl + 0
                    BtoUse  = BtensCntrl + 0
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control[cC < cB] = 1
                    AtoUse[cC < cB] = AtensCntrl[cC < cB]
                    BtoUse[cC < cB] = BtensCntrl[cC < cB]
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    nameslyuni = np.unique(namesly)
                    for kk in range(len(nameslyuni)):
                        indexly = np.where(namesly==nameslyuni[kk])[0]
                        self.beamX.Matrix[iele, 0] = namesly[indexly[0]]
                        self.beamX.Matrix[iele, 1] = nodeily[indexly[0]]
                        self.beamX.Matrix[iele, 2] = nodejly[indexly[0]]
                        self.beamX.Matrix[iele, 3] = BBly[indexly[0]]
                        self.beamX.Matrix[iele, 4] = HHly[indexly[0]]
                        self.beamX.Matrix[iele, 5] = LLly[indexly[0]]
                        self.beamX.Matrix[iele, 6] = Ntopc[indexly[0]]
                        self.beamX.Matrix[iele, 7] = Ntopc[indexly[-1]]
                        self.beamX.Matrix[iele, 8] = Ftopc[indexly[0]]
                        self.beamX.Matrix[iele, 9] = Ftopc[indexly[-1]]
                        self.beamX.Matrix[iele, 10] = Nbotc[indexly[0]]
                        self.beamX.Matrix[iele, 11] = Nbotc[indexly[-1]]
                        self.beamX.Matrix[iele, 12] = Fbotc[indexly[0]]
                        self.beamX.Matrix[iele, 13] = Fbotc[indexly[-1]]
                        self.beamX.Matrix[iele, 14] = fiw[indexly[0]]
                        self.beamX.Matrix[iele, 15] = sw[indexly[0]]
                        self.beamX.Matrix[iele, 16] = nwparallel_to_b[indexly[0]]
                        self.beamX.Matrix[iele, 17] = nwparallel_to_h[indexly[0]]
                        self.beamX.Matrix[iele, 18] = fiw[indexly[-1]]
                        self.beamX.Matrix[iele, 19] = sw[indexly[-1]]
                        self.beamX.Matrix[iele, 20] = nwparallel_to_b[indexly[-1]]
                        self.beamX.Matrix[iele, 21] = nwparallel_to_h[indexly[-1]]
                        self.beamX.Matrix[iele, 22] = Ntopi[indexly[0]]
                        self.beamX.Matrix[iele, 23] = Ntopi[indexly[-1]]
                        self.beamX.Matrix[iele, 24] = Ftopi[indexly[0]]
                        self.beamX.Matrix[iele, 25] = Ftopi[indexly[-1]]
                        self.beamX.Matrix[iele, 26] = Nboti[indexly[0]]
                        self.beamX.Matrix[iele, 27] = Nboti[indexly[-1]]
                        self.beamX.Matrix[iele, 28] = Fboti[indexly[0]]
                        self.beamX.Matrix[iele, 29] = Fboti[indexly[-1]]
                        self.beamX.Matrix[iele, 30] = MyNeg[indexly[0]]
                        self.beamX.Matrix[iele, 31] = MyPos[indexly[0]]
                        self.beamX.Matrix[iele, 32] = MyNeg[indexly[-1]]
                        self.beamX.Matrix[iele, 33] = MyPos[indexly[-1]]
                        
                        iele += 1                   

                    auxMyPos = np.append(auxMyPos, np.concatenate(([0], MyPos[2:-3:3], [0])))
                    auxMyNeg = np.append(auxMyNeg, np.concatenate(([MyNeg[0]], MyNeg[2:-3:3], [MyNeg[-1]])))

                if not hasattr(self.beamX, 'MyPos'):
                    self.beamX.MyPos = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamX.MyNeg = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamX.sumMrd = np.zeros((self.general.nstoreys, len(auxMyPos)))

                self.beamX.MyPos[j, :] = auxMyPos
                self.beamX.MyNeg[j, :] = auxMyNeg
                self.beamX.sumMrd[j, :] = auxMyPos + auxMyNeg

            self.beamX.Matrix[:, 41] = pedXEQ
            # ...........................................................................
            # Calculation of My for the beams in -YY
            # ...........................................................................
            neles = len(self.beamY.Area.flatten())
            pedYEQ = self.beamY.pedEQFinal.copy()
            pedYEQ[-1, :] = self.beamY.proofEQFinal[-1, :]
            pedYEQ = pedYEQ.flatten()
            self.beamY.Matrix = np.zeros((neles, 42))
            iele  = 0
            for j in range(self.general.nstoreys): # loop over the storeys
                auxMyPos = np.array([])
                auxMyNeg = np.array([])
                for i in range(len(alignmentsY)): # loop over the alignment
                    namesly = self.beamY.NName[f'{i}, {j}']
                    nodeily = self.beamY.NNodei[f'{i}, {j}']
                    nodejly = self.beamY.NNodej[f'{i}, {j}']
                    HHly    = self.beamY.HH[f'{i}, {j}']
                    BBly    = self.beamY.BB[f'{i}, {j}']
                    LLly    = self.beamY.LL[f'{i}, {j}']
                    Ntopc   = self.beamY.ncornerTOP[f'{i}, {j}']
                    Ftopc   = self.beamY.ficornerTOP[f'{i}, {j}']
                    Ntopi   = self.beamY.nintTOP[f'{i}, {j}']
                    Ftopi   = self.beamY.fiintTOP[f'{i}, {j}']
                    Nbotc   = self.beamY.ncornerBOT[f'{i}, {j}']
                    Fbotc   = self.beamY.ficornerBOT[f'{i}, {j}']
                    Nboti   = self.beamY.nintBOT[f'{i}, {j}']
                    Fboti   = self.beamY.fiintBOT[f'{i}, {j}']
                    fiw     = self.beamY.fiw[f'{i}, {j}']
                    sw      = self.beamY.sw[f'{i}, {j}']
                    nwparallel_to_b = self.beamY.nwparallel_to_b[f'{i}, {j}']
                    nwparallel_to_h = self.beamY.nwparallel_to_h[f'{i}, {j}']
                    # ...........................................................................
                    dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                    dD_line  = 1000 * HHly - dD                                                               # in mm
                    cB       = (epscU * dD) / (epscU + esy)
                    Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    Ec       = (57000 * (fcd * 145)**0.5) / 145
                    Es       = 200000
                    nyoung   = Es / Ec
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control = np.ones(dD.shape)
                    AtoUse  = AtensCntrl + 0
                    BtoUse  = BtensCntrl + 0
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                    rostens  = Astens / (BBly * 1000 * dD)
                    As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                    ros_line = As_line / (BBly * 1000 * dD)
                    cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                    AcomprCntrl = rostens + ros_line
                    AtensCntrl  = rostens + ros_line
                    BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                    Control[cC < cB] = 1
                    AtoUse[cC < cB] = AtensCntrl[cC < cB]
                    BtoUse[cC < cB] = BtensCntrl[cC < cB]
                    Control[cC >= cB] = 0
                    AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                    BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                    ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                    fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                    fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                    fiy = fiy1 + 0
                    fiy[Control==0] = fiy2[Control==0]
                    Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                    Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                    MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                    # ...........................................................................
                    nameslyuni = np.unique(namesly)
                    for kk in range(len(nameslyuni)):
                        indexly = np.where(namesly==nameslyuni[kk])[0]
                        self.beamY.Matrix[iele, 0] = namesly[indexly[0]]
                        self.beamY.Matrix[iele, 1] = nodeily[indexly[0]]
                        self.beamY.Matrix[iele, 2] = nodejly[indexly[0]]
                        self.beamY.Matrix[iele, 3] = BBly[indexly[0]]
                        self.beamY.Matrix[iele, 4] = HHly[indexly[0]]
                        self.beamY.Matrix[iele, 5] = LLly[indexly[0]]
                        self.beamY.Matrix[iele, 6] = Ntopc[indexly[0]]
                        self.beamY.Matrix[iele, 7] = Ntopc[indexly[-1]]
                        self.beamY.Matrix[iele, 8] = Ftopc[indexly[0]]
                        self.beamY.Matrix[iele, 9] = Ftopc[indexly[-1]]
                        self.beamY.Matrix[iele, 10] = Nbotc[indexly[0]]
                        self.beamY.Matrix[iele, 11] = Nbotc[indexly[-1]]
                        self.beamY.Matrix[iele, 12] = Fbotc[indexly[0]]
                        self.beamY.Matrix[iele, 13] = Fbotc[indexly[-1]]
                        self.beamY.Matrix[iele, 14] = fiw[indexly[0]]
                        self.beamY.Matrix[iele, 15] = sw[indexly[0]]
                        self.beamY.Matrix[iele, 16] = nwparallel_to_b[indexly[0]]
                        self.beamY.Matrix[iele, 17] = nwparallel_to_h[indexly[0]]
                        self.beamY.Matrix[iele, 18] = fiw[indexly[-1]]
                        self.beamY.Matrix[iele, 19] = sw[indexly[-1]]
                        self.beamY.Matrix[iele, 20] = nwparallel_to_b[indexly[-1]]
                        self.beamY.Matrix[iele, 21] = nwparallel_to_h[indexly[-1]]
                        self.beamY.Matrix[iele, 22] = Ntopi[indexly[0]]
                        self.beamY.Matrix[iele, 23] = Ntopi[indexly[-1]]
                        self.beamY.Matrix[iele, 24] = Ftopi[indexly[0]]
                        self.beamY.Matrix[iele, 25] = Ftopi[indexly[-1]]
                        self.beamY.Matrix[iele, 26] = Nboti[indexly[0]]
                        self.beamY.Matrix[iele, 27] = Nboti[indexly[-1]]
                        self.beamY.Matrix[iele, 28] = Fboti[indexly[0]]
                        self.beamY.Matrix[iele, 29] = Fboti[indexly[-1]]
                        self.beamY.Matrix[iele, 30] = MyNeg[indexly[0]]
                        self.beamY.Matrix[iele, 31] = MyPos[indexly[0]]
                        self.beamY.Matrix[iele, 32] = MyNeg[indexly[-1]]
                        self.beamY.Matrix[iele, 33] = MyPos[indexly[-1]]
                        
                        iele += 1                   

                    auxMyPos = np.append(auxMyPos, np.concatenate(([0], MyPos[2:-3:3], [0])))
                    auxMyNeg = np.append(auxMyNeg, np.concatenate(([MyNeg[0]], MyNeg[2:-3:3], [MyNeg[-1]])))

                if not hasattr(self.beamY, 'MyPos'):
                    self.beamY.MyPos = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.MyNeg = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.sumMrdaux = np.zeros((self.general.nstoreys, len(auxMyPos)))
                    self.beamY.sumMrd = np.zeros((self.general.nstoreys, len(auxMyPos)))

                self.beamY.MyPos[j, :] = auxMyPos
                self.beamY.MyNeg[j, :] = auxMyNeg
                self.beamY.sumMrdaux[j, :] = auxMyPos + auxMyNeg

            self.beamY.Matrix[:, 41] = pedYEQ

            # Convert the  beamY.sumMrd values to the correct order for columns
            # ...........................................................................
            actual_order = []
            Npoints = self.beamY.sumMrdaux.shape[1]
            actual_order1 = np.arange(0, Npoints, len(alignmentsX))
            for i in range(len(alignmentsX)):
                aux_order = i + actual_order1
                actual_order.extend(aux_order.tolist())

            for istor in range(self.general.nstoreys):
                self.beamY.sumMrd[istor, :] = self.beamY.sumMrdaux[istor, actual_order]
            # ...........................................................................
            # Calculation of My for the beams in Stairs
            # ...........................................................................
            neles = len(self.beamStair.Area.flatten())
            pedStairEQ = self.beamStair.pedEQFinal.copy()
            pedStairEQ = pedStairEQ.flatten()
            self.beamStair.Matrix = np.zeros((neles, 42))
            iele  = 0
            auxMyPos = np.array([])
            auxMyNeg = np.array([])
            for j in range(self.general.nstoreys):
                namesly = self.beamStair.NName[f'{j}']
                nodeily = self.beamStair.NNodei[f'{j}']
                nodejly = self.beamStair.NNodej[f'{j}']
                HHly    = self.beamStair.HH[f'{j}']
                BBly    = self.beamStair.BB[f'{j}']
                LLly    = self.beamStair.LL[f'{j}']
                Ntopc   = self.beamStair.ncornerTOP[f'{j}']
                Ftopc   = self.beamStair.ficornerTOP[f'{j}']
                Ntopi   = self.beamStair.nintTOP[f'{j}']
                Ftopi   = self.beamStair.fiintTOP[f'{j}']
                Nbotc   = self.beamStair.ncornerBOT[f'{j}']
                Fbotc   = self.beamStair.ficornerBOT[f'{j}']
                Nboti   = self.beamStair.nintBOT[f'{j}']
                Fboti   = self.beamStair.fiintBOT[f'{j}']
                fiw     = self.beamStair.fiw[f'{j}']
                sw      = self.beamStair.sw[f'{j}']
                nwparallel_to_b = self.beamStair.nwparallel_to_b[f'{j}']
                nwparallel_to_h = self.beamStair.nwparallel_to_h[f'{j}']
                # ...........................................................................
                dD       = 1000 * HHly - 1000 * cover - 1000 * fiw - 1000 * 0.5 * Ftopc                   # in mm
                dD_line  = 1000 * HHly - dD                                                               # in mm
                cB       = (epscU * dD) / (epscU + esy)
                Astens   = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)  # in mm2
                rostens  = Astens / (BBly * 1000 * dD)
                As_line  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)
                ros_line = As_line / (BBly * 1000 * dD)
                cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                Ec       = (57000 * (fcd * 145)**0.5) / 145
                Es       = 200000
                nyoung   = Es / Ec
                AcomprCntrl = rostens + ros_line
                AtensCntrl  = rostens + ros_line
                BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                Control = np.ones(dD.shape)
                AtoUse  = AtensCntrl + 0
                BtoUse  = BtensCntrl + 0
                Control[cC >= cB] = 0
                AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                fiy1 = (10**3) * fsyd / (Es * (1 - ky) * dD)
                fiy2 = (10**3) * (1.8 * (fcd) / (Ec * ky * dD))
                fiy = fiy1 + 0
                fiy[Control==0] = fiy2[Control==0]
                Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                MyNeg = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                # ...........................................................................
                Astens  = Nbotc * ((0.25 * np.pi) * (Fbotc * 1000)**2) + Nboti * ((0.25 * np.pi) * (Fboti * 1000)**2)   # in mm2
                rostens  = Astens / (BBly * 1000 * dD)
                As_line  = Ntopc * ((0.25 * np.pi) * (Ftopc * 1000)**2) + Ntopi * ((0.25 * np.pi) * (Ftopi * 1000)**2)
                ros_line = As_line / (BBly * 1000 * dD)
                cC       = (Astens * fsyd - As_line * fsyd) / (0.85 * fcd * BBly * 1000 * betafc)
                AcomprCntrl = rostens + ros_line
                AtensCntrl  = rostens + ros_line
                BcomprCntrl = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                BtensCntrl  = rostens + ros_line * (dD_line / dD) * (1 + (dD_line / dD))
                Control[cC < cB] = 1
                AtoUse[cC < cB] = AtensCntrl[cC < cB]
                BtoUse[cC < cB] = BtensCntrl[cC < cB]
                Control[cC >= cB] = 0
                AtoUse[cC >= cB] = AcomprCntrl[cC >= cB]
                BtoUse[cC >= cB] = BcomprCntrl[cC >= cB]
                ky   = ((nyoung**2) * (AtoUse**2) + (2*nyoung*BtoUse))**0.5 - nyoung*AtoUse
                fiy1 = 10**3 * fsyd / (Es * (1 - ky) * dD)
                fiy2 = 10**3 * (1.8 * (fcd) / (Ec * ky * dD))
                fiy = fiy1 + 0
                fiy[Control==0] = fiy2[Control==0]
                Term1 = (10**6) * Ec * 0.5 * (ky**2) * (0.5 * (1 + (dD_line / dD)) - (ky / 3))
                Term2 = (10**6) * (0.50 * Es) * ((1 - ky) * rostens + (ky - (dD_line / dD)) * ros_line) * (1 - (dD_line / dD))
                MyPos = (10**-3) * ((BBly) * ((dD / 1000)**3)) * fiy * (Term1 + Term2)
                # ...........................................................................
                self.beamStair.Matrix[iele, 0] = namesly[0]
                self.beamStair.Matrix[iele, 1] = nodeily[0]
                self.beamStair.Matrix[iele, 2] = nodejly[0]
                self.beamStair.Matrix[iele, 3] = BBly[0]
                self.beamStair.Matrix[iele, 4] = HHly[0]
                self.beamStair.Matrix[iele, 5] = LLly[0]
                self.beamStair.Matrix[iele, 6] = Ntopc[0]
                self.beamStair.Matrix[iele, 7] = Ntopc[-1]
                self.beamStair.Matrix[iele, 8] = Ftopc[0]
                self.beamStair.Matrix[iele, 9] = Ftopc[-1]
                self.beamStair.Matrix[iele, 10] = Nbotc[0]
                self.beamStair.Matrix[iele, 11] = Nbotc[-1]
                self.beamStair.Matrix[iele, 12] = Fbotc[0]
                self.beamStair.Matrix[iele, 13] = Fbotc[-1]
                self.beamStair.Matrix[iele, 14] = fiw[0]
                self.beamStair.Matrix[iele, 15] = sw[0]
                self.beamStair.Matrix[iele, 16] = nwparallel_to_b[0]
                self.beamStair.Matrix[iele, 17] = nwparallel_to_h[0]
                self.beamStair.Matrix[iele, 18] = fiw[-1]
                self.beamStair.Matrix[iele, 19] = sw[-1]
                self.beamStair.Matrix[iele, 20] = nwparallel_to_b[-1]
                self.beamStair.Matrix[iele, 21] = nwparallel_to_h[-1]
                self.beamStair.Matrix[iele, 22] = Ntopi[0]
                self.beamStair.Matrix[iele, 23] = Ntopi[-1]
                self.beamStair.Matrix[iele, 24] = Ftopi[0]
                self.beamStair.Matrix[iele, 25] = Ftopi[-1]
                self.beamStair.Matrix[iele, 26] = Nboti[0]
                self.beamStair.Matrix[iele, 27] = Nboti[-1]
                self.beamStair.Matrix[iele, 28] = Fboti[0]
                self.beamStair.Matrix[iele, 29] = Fboti[-1]
                self.beamStair.Matrix[iele, 30] = MyNeg[0]
                self.beamStair.Matrix[iele, 31] = MyPos[0]
                self.beamStair.Matrix[iele, 32] = MyNeg[-1]
                self.beamStair.Matrix[iele, 33] = MyPos[-1]
                iele += 1                   

                if not hasattr(self.beamStair, 'MyPos'):
                    self.beamStair.MyPos = np.zeros((self.general.nstoreys, 2))
                    self.beamStair.MyNeg = np.zeros((self.general.nstoreys, 2))
                    self.beamStair.sumMrd = np.zeros((self.general.nstoreys, 2))

                self.beamStair.MyPos[j, :] = np.array([0, 0])
                self.beamStair.MyNeg[j, :] = MyNeg[[0,2]]
                self.beamStair.sumMrd[j, :]= self.beamStair.MyPos[j, :] + self.beamStair.MyNeg[j, :]

            self.beamStair.Matrix[:, 41] = pedStairEQ

        return CvFLAGX, CvFLAGY, CvFLAGStair, auxbeam

    def _cdh_columns(self, auxbeam):
        """        
        Designs columns usign DCH properties
        Refrences: Eurocode 2 and Eurocode 8-1
        Design based on ultimate strength analysis

        Args:
            auxbeam (float): auxiliary variable describing the number of beams that do not satisfy design requirements
        """
        # ...........................................................................
        # General Material Propeties
        # ...........................................................................
        niu1 = 0.60  # Eurocode 2 (EQ.6.9)
        cota = 2.50  # theta is 21.8º degrees
        taumax = 1000 * (1.0 * 0.90 * niu1 * self.general.fcd) / cota # Eurocode 2 (EQ.6.5)
        fcd = self.general.fcd + 0
        fsyd = self.general.fsyd + 0
        cover = 0.03
        if self.general.nstoreys < 6:
            miueconomic = 0.25
        else:
            miueconomic    = 0.25
        sw_min_over_fi = 8
        rho_min = 0.010
        dmin = 0.035
        dmax = 0.15 # maximum distance between restrrained steel bars
        rhow_min = 0.08 * (self.general.fck**0.5) / self.general.fsyk  # Eurocode 2 (EQ.9.5N)
        if self.general.fsyk <= 400:
            rho_max = 0.03
        else:
            rho_max = 0.04
        fiw_min = 0.008  
        # ...........................................................................
        # Sets the maximum column dimensions
        # ...........................................................................
        if self.general.ColumnType == 1:
            self.column.maxH = self.column.maxHsquared + 0
        else:
            self.column.maxH = self.column.maxHrectangular + 0
        # ...........................................................................
        # Get the Mrd values from the beams in XX and YY (for capacity design)
        # ...........................................................................
        if auxbeam == 0:
            sumMrCX = np.zeros(self.column.HX.shape)
            MrdX1 = np.zeros(self.column.HX.shape)
            MrdX9 = np.zeros(self.column.HX.shape)
            for i in range(self.general.nstoreys):
                aux1 = self.column.equalsections[:, i].copy() # should copy (direct assignment)
                aux = np.where(aux1 > 0)[0]
                sumMrCX[i, aux[[0, 1]]] = 0 * aux[[0, 1]] + self.beamX.sumMrd[i, aux[0]]
                sumMrCX[i, aux[[2, 3]]] = 0 * aux[[0, 1]] + self.beamX.sumMrd[i, aux[0] + 1]
                aux1[aux[[1, 3]]] = 0
                aux2 = np.where(aux1 == 0)[0]
                sumMrCX[i, aux2] = self.beamX.sumMrd[i, :].copy()
            for i in range(self.general.nstoreys):
                if i == 0 and self.general.nstoreys == 1:
                    MrdX9[i, :] = 1.30 * 1.00 * sumMrCX[i, :]
                    MrdX9[i, aux[0]] = 1.30 * 0.50 * sumMrCX[i, aux[0]]
                    MrdX1[i, aux[1]] = 1.30 * 0.50 * sumMrCX[i, aux[1]]
                    MrdX9[i, aux[2]] = 1.30 * 0.50 * sumMrCX[i, aux[2]]
                    MrdX1[i, aux[3]] = 1.30 * 0.50 * sumMrCX[i, aux[3]]				
                elif i == 0 and self.general.nstoreys != 1:
                    MrdX9[i, :] = 1.30 * 0.50 * sumMrCX[i, :]
                    MrdX9[i, aux[0]] = 1.30 * 0.50 * sumMrCX[i, aux[0]]
                    MrdX1[i, aux[1]] = 1.30 * 0.50 * sumMrCX[i, aux[1]]
                    MrdX9[i, aux[2]] = 1.30 * 0.50 * sumMrCX[i, aux[2]]
                    MrdX1[i, aux[3]] = 1.30 * 0.50 * sumMrCX[i, aux[3]]	
                elif i == self.general.nstoreys-1 and self.general.nstoreys > 1:
                    MrdX1[i, :] = 1.30 * 0.50 * sumMrCX[i-1, :]
                    MrdX9[i, :] = 1.30 * 1.00 * sumMrCX[i, :]
                    MrdX9[i, aux[0]] = 1.30 * 0.50 * sumMrCX[i, aux[0]]
                    MrdX1[i, aux[1]] = 1.30 * 0.50 * sumMrCX[i, aux[1]]
                    MrdX9[i, aux[2]] = 1.30 * 0.50 * sumMrCX[i, aux[2]]
                    MrdX1[i, aux[3]] = 1.30 * 0.50 * sumMrCX[i, aux[3]]		
                else:
                    MrdX1[i, :] = 1.30 * 0.50 * sumMrCX[i-1, :]
                    MrdX9[i, :] = 1.30 * 0.50 * sumMrCX[i, :]
                    MrdX9[i, aux[0]] = 1.30 * 0.50 * sumMrCX[i, aux[0]]
                    MrdX1[i, aux[1]] = 1.30 * 0.50 * sumMrCX[i, aux[1]]
                    MrdX9[i, aux[2]] = 1.30 * 0.50 * sumMrCX[i, aux[2]]
                    MrdX1[i, aux[3]] = 1.30 * 0.50 * sumMrCX[i, aux[3]]	
            # ...........................................................................
            sumMrCY = np.zeros(self.column.HX.shape)
            MrdY1 = np.zeros(self.column.HX.shape)
            MrdY9 = np.zeros(self.column.HX.shape)
            for i in range(self.general.nstoreys):
                aux1 = self.column.equalsections[:, i].copy()
                aux = np.where(aux1 > 0)[0]
                sumMrCY[i, aux[[0, 2]]] = 0
                aux1[aux[[1, 3]]] = 0
                aux2 = np.where(aux1 == 0)[0]
                sumMrCY[i, aux2] = self.beamY.sumMrd[i, :].copy()
            for i in range(self.general.nstoreys):
                if i == 0 and self.general.nstoreys == 1:
                    MrdY9[i, :] = 1.30 * 1.00 * sumMrCY[i, :]
                    MrdY9[i, aux[0]] = 1.30 * 0.50 * sumMrCY[i, aux[0]]
                    MrdY1[i, aux[1]] = 1.30 * 0.50 * sumMrCY[i, aux[1]]
                    MrdY9[i, aux[2]] = 1.30 * 0.50 * sumMrCY[i, aux[2]]
                    MrdY1[i, aux[3]] = 1.30 * 0.50 * sumMrCY[i, aux[3]]				
                elif i == 0 and self.general.nstoreys != 1:
                    MrdY9[i, :] = 1.30 * 0.50 * sumMrCY[i, :]
                    MrdY9[i, aux[0]] = 1.30 * 0.50 * sumMrCY[i, aux[0]]
                    MrdY1[i, aux[1]] = 1.30 * 0.50 * sumMrCY[i, aux[1]]
                    MrdY9[i, aux[2]] = 1.30 * 0.50 * sumMrCY[i, aux[2]]
                    MrdY1[i, aux[3]] = 1.30 * 0.50 * sumMrCY[i, aux[3]]	
                elif i == self.general.nstoreys-1 and self.general.nstoreys > 1:
                    MrdY1[i, :] = 1.30 * 0.50 * sumMrCY[i-1, :]
                    MrdY9[i, :] = 1.30 * 1.00 * sumMrCY[i, :]
                    MrdY9[i, aux[0]] = 1.30 * 0.50 * sumMrCY[i, aux[0]]
                    MrdY1[i, aux[1]] = 1.30 * 0.50 * sumMrCY[i, aux[1]]
                    MrdY9[i, aux[2]] = 1.30 * 0.50 * sumMrCY[i, aux[2]]
                    MrdY1[i, aux[3]] = 1.30 * 0.50 * sumMrCY[i, aux[3]]		
                else:
                    MrdY1[i, :] = 1.30 * 0.50 * sumMrCY[i-1, :]
                    MrdY9[i, :] = 1.30 * 0.50 * sumMrCY[i, :]
                    MrdY9[i, aux[0]] = 1.30 * 0.50 * sumMrCY[i, aux[0]]
                    MrdY1[i, aux[1]] = 1.30 * 0.50 * sumMrCY[i, aux[1]]
                    MrdY9[i, aux[2]] = 1.30 * 0.50 * sumMrCY[i, aux[2]]
                    MrdY1[i, aux[3]] = 1.30 * 0.50 * sumMrCY[i, aux[3]]	
            # ...........................................................................
            # Append forces obtained for capacity design
            self.column.MuX1.append(MrdX1 / (self.column.HY * self.column.HX**2 * fcd * 1000))
            self.column.MuX9.append(MrdX9 / (self.column.HY * self.column.HX**2 * fcd * 1000))
            self.column.MuY1.append(MrdY1 / (self.column.HX * self.column.HY**2 * fcd * 1000))
            self.column.MuY9.append(MrdY9 / (self.column.HX * self.column.HY**2 * fcd * 1000))
            self.column.Niu1.append(self.column.Niu1[1].copy()) # These forces correspond to the normal forces for capacity flexural design. They are retrieved from the gravity load case as an aproximation.
            self.column.Niu9.append(self.column.Niu9[1].copy()) # These forces correspond to the normal forces for capacity flexural design. They are retrieved from the gravity load case as an aproximation.
            self.column.V1_x.append(self.column.V1_x[1].copy()) # But what about shear forces? TODO: ask HMA
            self.column.V1_y.append(self.column.V1_y[1].copy()) 
            self.column.V9_x.append(self.column.V9_x[1].copy()) 
            self.column.V9_y.append(self.column.V9_y[1].copy())
            self.column.tauX1.append(self.column.V1_x[18] / (self.column.HY * 0.90 * self.column.HX * fcd))
            self.column.tauX9.append(self.column.V1_y[18] / (self.column.HY * 0.90 * self.column.HX * fcd))
            self.column.tauY1.append(self.column.V9_x[18] / (self.column.HX * 0.90 * self.column.HY * fcd))
            self.column.tauY9.append(self.column.V9_y[18] / (self.column.HX * 0.90 * self.column.HY * fcd))
        else:
            self.column.MuX1.append(0 * (self.column.HY * self.column.HX**2 * fcd * 1000))
            self.column.MuX9.append(0 * (self.column.HY * self.column.HX**2 * fcd * 1000))
            self.column.MuY1.append(0 * (self.column.HX * self.column.HY**2 * fcd * 1000))
            self.column.MuY9.append(0 * (self.column.HX * self.column.HY**2 * fcd * 1000))
            self.column.Niu1.append(0 * self.column.Niu1[1]) 
            self.column.Niu9.append(0 * self.column.Niu9[1]) 
            self.column.V1_x.append(0 * self.column.V1_x[1]) 
            self.column.V1_y.append(0 * self.column.V1_y[1]) 
            self.column.V9_x.append(0 * self.column.V9_x[1]) 
            self.column.V9_y.append(0 * self.column.V9_y[1])
            self.column.tauX1.append(0 * (self.column.HY * 0.90 * self.column.HX * fcd))
            self.column.tauX9.append(0 * (self.column.HY * 0.90 * self.column.HX * fcd))
            self.column.tauY1.append(0 * (self.column.HX * 0.90 * self.column.HY * fcd))
            self.column.tauY9.append(0 * (self.column.HX * 0.90 * self.column.HY * fcd))
        # ...........................................................................
        # Variables for the design based on the DCH Design Routines
        # ...........................................................................
        Combinations_2_use = [0, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18] # 18th combination refers to the capacity design
        MMMX1 = [self.column.MuX1[comb] for comb in Combinations_2_use]
        MMMY1 = [self.column.MuY1[comb] for comb in Combinations_2_use]
        MMMX9 = [self.column.MuX9[comb] for comb in Combinations_2_use]
        MMMY9 = [self.column.MuY9[comb] for comb in Combinations_2_use]
        # ...........................................................................
        TTTX1 = [self.column.tauX1[comb] for comb in Combinations_2_use]
        TTTY1 = [self.column.tauY1[comb] for comb in Combinations_2_use]
        TTTX9 = [self.column.tauX9[comb] for comb in Combinations_2_use]
        TTTY9 = [self.column.tauY9[comb] for comb in Combinations_2_use]
        # ...........................................................................
        MuX1_maxo = np.max(np.array(MMMX1), axis=0)
        MuX9_maxo = np.max(np.array(MMMX9), axis=0)
        MuY1_maxo = np.max(np.array(MMMY1), axis=0)
        MuY9_maxo = np.max(np.array(MMMY9), axis=0)
        MuXmax = np.maximum(MuX1_maxo, MuX9_maxo) / 0.70
        MuYmax = np.maximum(MuY1_maxo, MuY9_maxo) / 0.70
        # ...........................................................................
        tauX1_maxo = np.max(np.array(TTTX1), axis=0)
        tauX9_maxo = np.max(np.array(TTTX9), axis=0)
        tauY1_maxo = np.max(np.array(TTTY1), axis=0)
        tauY9_maxo = np.max(np.array(TTTY9), axis=0)
        tauXmax = np.maximum(tauX1_maxo, tauX9_maxo)
        tauYmax = np.maximum(tauY1_maxo, tauY9_maxo)
        # ...........................................................................
        CpFLAGX = np.zeros(self.column.name.shape)
        CpFLAGY = np.zeros(self.column.name.shape)
        CpFLAGX[tauXmax > taumax] = 1
        CpFLAGX[MuXmax > miueconomic] = 1
        CpFLAGY[tauYmax > taumax] = 1
        CpFLAGY[MuYmax > miueconomic] = 1
        # ...........................................................................
        # Variables for the design based on the DCL Design Routines
        # ...........................................................................
        if np.max(self.column.HX) > self.column.maxH or np.max(self.column.HY) > self.column.maxH:
            CpFLAGfc = 222
            if self.general.fsyk == 240:
                self.general.fsyk = 400
                self.general.fsyd = 348
                self.general.fsydEQ = 348
                self.general.fck = self.general.fckgrav.copy()
                self.general.fckcube = self.general.fckcubegrav.copy()
                self.general.fcd = self.general.fcdgrav.copy()
                self.general.fcdEQ = self.general.fcdEQgrav.copy()
            elif self.general.fck == 16:
                self.general.fck = 20
                self.general.fckcube = 25
                self.general.fcd = 13.3
                self.general.fcdEQ = 13.3
            elif self.general.fck == 20:
                self.general.fck = 25
                self.general.fckcube = 30
                self.general.fcd = 16.7
                self.general.fcdEQ = 16.7
            elif self.general.fck == 25:
                self.general.fck = 30
                self.general.fckcube = 35
                self.general.fcd = 16.7
                self.general.fcdEQ = 16.7
            elif self.general.fsyk == 400:
                self.general.fsyk = 500
                self.general.fsyd = 435
                self.general.fsydEQ = 435
                self.general.fck = self.general.fckgrav.copy()
                self.general.fckcube = self.general.fckcubegrav.copy()
                self.general.fcd = self.general.fcdgrav.copy()
                self.general.fcdEQ = self.general.fcdEQgrav.copy()
            elif self.general.fsyk == 500:
                if self.general.ColumnType == 2 and self.general.ColITER == 0:
                    CpFLAGfc = 333
                    self.general.ColITER = 1
                else:
                    CpFLAGfc = 1
        else: # check_Column_dims.m --> TODO: What do we do here?
            CpFLAGfc = 0
            aucx = np.where(self.column.Astair[0, :] > 0)[0]
            for i in range(self.general.nstoreys):
                CpFLAGX[i, aucx[0]] = max(CpFLAGX[i, aucx[0]], CpFLAGX[i, aucx[1]])
                CpFLAGY[i, aucx[0]] = max(CpFLAGY[i, aucx[0]], CpFLAGY[i, aucx[1]])
                CpFLAGX[i, aucx[1]] = CpFLAGX[i, aucx[0]].copy()
                CpFLAGY[i, aucx[1]] = CpFLAGY[i, aucx[0]].copy()
                CpFLAGX[i, aucx[2]] = max(CpFLAGX[i, aucx[2]], CpFLAGX[i, aucx[3]])
                CpFLAGY[i, aucx[2]] = max(CpFLAGY[i, aucx[2]], CpFLAGY[i, aucx[3]])
                CpFLAGX[i, aucx[3]] = CpFLAGX[i, aucx[2]].copy()
                CpFLAGY[i, aucx[3]] = CpFLAGY[i, aucx[2]].copy()
        # ...........................................................................
        # Checks if the design should be finished or not
        # ...........................................................................
        aux = np.sum(CpFLAGY) + np.sum(CpFLAGX) + auxbeam
        if aux > 0.99:
            print('Columns Not OK.... still %d to change!' % int(np.sum(CpFLAGY) + np.sum(CpFLAGX)))
            print('Maximum HX is %4.6f...' % float(np.max(np.max(self.column.HX))))
            print('Maximum HY is %4.6f...' % float(np.max(np.max(self.column.HY))))
            print('Minimum HX is %4.6f...' % float(np.min(np.min(self.column.HX))))
            print('Minimum HY is %4.6f...' % float(np.min(np.min(self.column.HY))))
            print('Maximum HX2 is %4.6f...' % float(np.max(np.max(self.column.HX[0, self.column.Colindex1]))))
            print('Maximum HY2 is %4.6f...' % float(np.max(np.max(self.column.HY[0, self.column.Colindex2]))))
            print('Minimum HX2 is %4.6f...' % float(np.min(np.min(self.column.HX[0, self.column.Colindex1]))))
            print('Minimum HY2 is %4.6f...' % float(np.min(np.min(self.column.HY[0, self.column.Colindex2]))))
        else:
            print('Columns OK. Stage 1 complete!')
            # ...........................................................................
            # Determination of the necessary longitudinal rebar area
            # ...........................................................................
            AsX = []
            AsY = []
            AsX_sw = []
            AsY_sw = []
            HX = self.column.HX.copy()
            HY = self.column.HY.copy()
            for i, icomb in enumerate(Combinations_2_use):
                NIU1 = -1 * self.column.Niu1[icomb]
                NIU9 = -1 * self.column.Niu9[icomb]
                MuX1 = np.abs(self.column.MuX1[icomb]) / 0.70
                MuX9 = np.abs(self.column.MuX9[icomb]) / 0.70
                MuY1 = np.abs(self.column.MuY1[icomb]) / 0.70
                MuY9 = np.abs(self.column.MuY9[icomb]) / 0.70
                # ...........................................................................
                lambdaX = 0.50 - cover / HX
                lambdaY = 0.50 - cover / HY
                betavector = [1.0, 1.00, 0.93, 0.88, 0.88, 0.93, 0.93]
                niuvector  = [-100, 0.40, 0.50, 0.60, 0.70, 0.85, 1000] # to cover those negative value for tensile forces HMA
                beta1 = np.interp(NIU1, niuvector, betavector)
                beta9 = np.interp(NIU9, niuvector, betavector)
                niuc1 = NIU1 - 0.85
                niuc9 = NIU9 - 0.85
                omegaX = np.zeros(NIU1.shape)
                omegaY = np.zeros(NIU1.shape)
                AsXPos9 = omegaX.copy()
                AsXPos1 = omegaX.copy()
                AsYPos9 = omegaY.copy()
                AsYPos1 = omegaY.copy()
                # ...........................................................................
                for jj in range(NIU1.shape[0]):
                    for kk in range(NIU1.shape[1]):
                        if NIU1[jj, kk] < 0:
                            omegaX[jj, kk] = -NIU1[jj, kk] + (MuX1[jj, kk] / (beta1[jj, kk] * lambdaX[jj, kk])) # page 48 REBAP-83 EQ 22 (HMA)
                            omegaY[jj, kk] = -NIU1[jj, kk] + (MuY1[jj, kk] / (beta1[jj, kk] * lambdaY[jj, kk])) # page 48 REBAP-83 EQ 22 (HMA)
                        elif NIU1[jj, kk] <= 0.85:
                            omegaX[jj, kk]  = (MuX1[jj, kk] + 0.55 * NIU1[jj, kk] * niuc1[jj, kk]) / (beta1[jj, kk] * lambdaX[jj, kk])
                            omegaY[jj, kk]  = (MuY1[jj, kk] + 0.55 * NIU1[jj, kk] * niuc1[jj, kk]) / (beta1[jj, kk] * lambdaY[jj, kk])
                        else:
                            omegaX[jj, kk]  = (niuc1[jj, kk])+(MuX1[jj, kk] / (beta1[jj, kk] * lambdaX[jj, kk]))
                            omegaY[jj, kk]  = (niuc1[jj, kk])+(MuY1[jj, kk] / (beta1[jj, kk] * lambdaY[jj, kk]))

                        AsXPos1[jj, kk] = 0.50 * (omegaX[jj, kk] * HY[jj, kk] * HX[jj, kk] * fcd / fsyd)
                        AsYPos1[jj, kk] = 0.50 * (omegaY[jj, kk] * HY[jj, kk] * HX[jj, kk] * fcd / fsyd)
                        # ...........................................................................
                        if NIU9[jj, kk] < 0:
                            omegaX[jj, kk] = -NIU9[jj, kk] + (MuX9[jj, kk] / (beta9[jj, kk] * lambdaX[jj, kk])) # page 48 REBAP-83 EQ 22 (HMA)
                            omegaY[jj, kk] = -NIU9[jj, kk] + (MuY9[jj, kk] / (beta9[jj, kk] * lambdaY[jj, kk])) # page 48 REBAP-83 EQ 22 (HMA)
                        elif NIU9[jj, kk] <= 0.85:
                            omegaX[jj, kk]  = (MuX9[jj, kk] + 0.55 * NIU9[jj, kk] * niuc9[jj, kk]) / (beta9[jj, kk] * lambdaX[jj, kk])
                            omegaY[jj, kk]  = (MuY9[jj, kk] + 0.55 * NIU9[jj, kk] * niuc9[jj, kk]) / (beta9[jj, kk] * lambdaY[jj, kk])
                        else:
                            omegaX[jj, kk]  = (niuc9[jj, kk]) + (MuX9[jj, kk] / (beta9[jj, kk] * lambdaX[jj, kk]))
                            omegaY[jj, kk]  = (niuc9[jj, kk]) + (MuY9[jj, kk] / (beta9[jj, kk] * lambdaY[jj, kk]))
                        
                        AsXPos9[jj, kk] = 0.50 * (omegaX[jj, kk] * HY[jj, kk] * HX[jj, kk] * fcd / fsyd)
                        AsYPos9[jj, kk] = 0.50 * (omegaY[jj, kk] * HY[jj, kk] * HX[jj, kk] * fcd / fsyd)

                AsXPos1[AsXPos1 <= 0] = 0.000226195 # at least 2fi12mm will be placed, even if no need for the
                AsYPos1[AsYPos1 <= 0] = 0.000226195 # at least 2fi12mm will be placed, even if no need for the
                AsXPos9[AsXPos9 <= 0] = 0.000226195 # at least 2fi12mm will be placed, even if no need for the
                AsYPos9[AsYPos9 <= 0] = 0.000226195 # at least 2fi12mm will be placed, even if no need for the
                AsX.append(np.maximum(AsXPos1, AsXPos9))
                AsY.append(np.maximum(AsYPos1, AsYPos9))

                # Concrete contribution is discarded
                VedX1 = self.column.V1_x[icomb]  
                VedY1 = self.column.V1_y[icomb] 
                VedX9 = self.column.V9_x[icomb]
                VedY9 = self.column.V9_y[icomb]
                VswconstX = 0.9 * 0.9 * HX * 1000 * fsyd * cota # Eurocode 2 6.7N and 6.8
                VswconstY = 0.9 * 0.9 * HY * 1000 * fsyd * cota # Eurocode 2 6.7N and 6.8
                Asw_sX1 = (np.abs(VedX1)) / VswconstX                  
                Asw_sY1 = (np.abs(VedY1)) / VswconstY                  
                Asw_sX9 = (np.abs(VedX9)) / VswconstX                  
                Asw_sY9 = (np.abs(VedY9)) / VswconstY                  
                AsX_sww = np.maximum(Asw_sX1, Asw_sX9)
                AsY_sww = np.maximum(Asw_sY1, Asw_sY9)
                Asw_sminX = rhow_min * HY * 0.15 # assuming a sw smaller than 0.15 will be needed (not quite clear to me)
                Asw_sminY = rhow_min * HX * 0.15 # assuming a sw smaller than 0.15 will be needed
                AsX_sw.append(np.maximum(AsX_sww, Asw_sminX))
                AsY_sw.append(np.maximum(AsY_sww, Asw_sminY))

            self.column.AsX = np.max(np.array(AsX), axis=0)
            self.column.AsY = np.max(np.array(AsY), axis=0)
            self.column.AsX_sw = np.max(np.array(AsX_sw), axis=0)
            self.column.AsY_sw = np.max(np.array(AsY_sw), axis=0)
            sw_max = 1.0 * HX
            # ...........................................................................
            # Get the rebar solution
            # ...........................................................................
            attributes = ['fi_corner', 'fi_layintX', 'nbar_HminusX', 'nlayintX', 'Rhosl', 'RhoslX', 'RhoslY', 'nintBOT', 'sw', 'fiw', 'nwparallel_to_X', 'nwparallel_to_Y']
            for attr in attributes:
                setattr(self.column, attr, np.zeros(self.column.AsX.shape))
            for jj in range(self.column.AsX.shape[1]):
                self.column.fi_corner[:, jj], self.column.fi_layintX[:, jj], self.column.nbar_HminusX[:, jj], self.column.nlayintX[:, jj], self.column.Rhosl[:, jj], self.column.RhoslX[:, jj], self.column.RhoslY[:, jj], self.column.sw[:, jj], self.column.fiw[:, jj], self.column.nwparallel_to_X[:, jj], self.column.nwparallel_to_Y[:, jj] = _get_column_rebars(self.column.AsX[:, jj], self.column.AsY[:, jj], HX[:, jj], HY[:, jj], rho_min, dmin, dmax, cover, self.column.AsX_sw[:, jj], self.column.AsY_sw[:, jj], sw_min_over_fi, sw_max[:, jj], fiw_min)
            # ...........................................................................
            # Save stuff
            # ...........................................................................
            nrow = self.column.name.shape[0] * self.column.name.shape[1]
            ncol = 27
            self.column.Matrix = np.zeros((nrow, ncol))
            self.column.Matrix[:, 0] = (self.column.name.T).flatten()
            self.column.Matrix[:, 1] = (self.column.elasnodei.T).flatten() + 7000
            self.column.Matrix[:, 2] = (self.column.elasnodej.T).flatten() + 2000
            self.column.Matrix[:, 3] = (self.column.HX.T).flatten()
            self.column.Matrix[:, 4] = (self.column.HY.T).flatten()
            self.column.Matrix[:, 5] = (self.column.L.T).flatten()
            self.column.Matrix[:, 6] = (self.column.storey.T).flatten()
            self.column.Matrix[:, 7] = (self.column.perimeter.T).flatten()
            self.column.Matrix[:, 8] = (self.column.nbar_HminusX.T).flatten()
            self.column.Matrix[:, 9]  = (self.column.nlayintX.T).flatten()
            self.column.Matrix[:, 10]  = (self.column.fi_corner.T).flatten()
            self.column.Matrix[:, 11] = (self.column.fi_layintX.T).flatten()
            self.column.Matrix[:, 12] = (self.column.Rhosl.T).flatten()
            self.column.Matrix[:, 13] = (self.column.sw.T).flatten()
            self.column.Matrix[:, 14] = (self.column.fiw.T).flatten()
            self.column.Matrix[:, 15] = (self.column.nwparallel_to_X.T).flatten()
            self.column.Matrix[:, 16] = (self.column.nwparallel_to_Y.T).flatten()
            self.column.Matrix[:, 17] = (self.column.N_EQfinal.T).flatten()
            # ...........................................................................
            # Checking the maximum rho_l condition
            # ...........................................................................
            if np.max(self.column.Rhosl) > rho_max:
                aux1 = self.column.Rhosl > rho_max
                aux2 = self.column.Rhosl <= rho_max
                CpFLAGX[aux1] = 1
                CpFLAGX[aux2] = 0
                CpFLAGY[aux1] = 1
                CpFLAGY[aux2] = 0            

            aucx = np.where(self.column.Astair[0, :] > 0)[0]
            for i in range(self.general.nstoreys):
                CpFLAGX[i, aucx[0]] = max(CpFLAGX[i, aucx[0]], CpFLAGX[i, aucx[1]])
                CpFLAGY[i, aucx[0]] = max(CpFLAGY[i, aucx[0]], CpFLAGY[i, aucx[1]])
                CpFLAGX[i, aucx[1]] = CpFLAGX[i, aucx[0]]
                CpFLAGY[i, aucx[1]] = CpFLAGY[i, aucx[0]]
                CpFLAGX[i, aucx[2]] = max(CpFLAGX[i, aucx[2]], CpFLAGX[i, aucx[3]])
                CpFLAGY[i, aucx[2]] = max(CpFLAGY[i, aucx[2]], CpFLAGY[i, aucx[3]])
                CpFLAGX[i, aucx[3]] = CpFLAGX[i, aucx[2]]
                CpFLAGY[i, aucx[3]] = CpFLAGY[i, aucx[2]]

            aux = np.sum(CpFLAGY) + np.sum(CpFLAGX) + auxbeam
            if aux > 0:
                print('Columns Not OK...the maximum Rho_l condition... still %d to change' % int(sum(CpFLAGY.flatten()) + sum(CpFLAGX.flatten())))
            else:
                print('Columns Rho_l condition OK!')
            # ...........................................................................
            # Checking the ductility condition Eq. 5. 15 EC8-1 pp 98 (Not really though)
            # ...........................................................................
            bi_sectionX = self.column.HX / self.column.nwparallel_to_X
            nbi_sectionX = self.column.nwparallel_to_X.copy()
            bi_sectionY = self.column.HY / self.column.nwparallel_to_Y
            nbi_sectionY = self.column.nwparallel_to_Y.copy()
            alpha_n = 1 - ((2 * nbi_sectionX * (bi_sectionX**2) + 2 * nbi_sectionY * (bi_sectionY**2)) / (6 * self.column.HX * self.column.HY))
            HYc = self.column.HY - 2*0.03 - self.column.fiw
            HXc = self.column.HX - 2*0.03 - self.column.fiw
            alpha_sX = (1 - self.column.sw / (2 * HYc)) * (1 - self.column.sw / (2 * HXc))
            alpha_sY = (1 - self.column.sw / (2 * HXc)) * (1 - self.column.sw / (2 * HYc))
            alpha_X = alpha_n * alpha_sX
            alpha_Y = alpha_n * alpha_sY
            rho_w_X = (self.column.nwparallel_to_X * np.pi * (self.column.fiw**2) / 4) / (self.column.sw * self.column.HY)
            rho_w_Y = (self.column.nwparallel_to_Y * np.pi * (self.column.fiw**2) / 4) / (self.column.sw * self.column.HX)
            omega_wd = (rho_w_X + rho_w_Y) * (self.general.fsyd / self.general.fcd)
            alpha_omega_wd_X = alpha_X * omega_wd
            alpha_omega_wd_Y = alpha_Y * omega_wd
            epsyd = self.general.fsyd / 202000 # assumption
            self.column.EC8_min_max_local_ductility_X = 9999 + 0 * self.column.sw
            self.column.EC8_min_max_local_ductility_Y = 9999 + 0 * self.column.sw
            self.column.EC8_max_local_ductility_X = np.zeros((19, self.column.HX.shape[0], self.column.HX.shape[1]))
            self.column.EC8_max_local_ductility_Y = np.zeros((19, self.column.HX.shape[0], self.column.HX.shape[1]))
            for i, icomb in enumerate(Combinations_2_use):
                NIU1 = np.abs(self.column.Niu1[icomb])
                self.column.EC8_max_local_ductility_X[icomb] = (alpha_omega_wd_X + 0.035) / (30 * (HYc / self.column.HY) * epsyd * NIU1)
                self.column.EC8_max_local_ductility_Y[icomb] = (alpha_omega_wd_Y + 0.035) / (30 * (HXc / self.column.HX) * epsyd * NIU1)
                ## SECTION TITLE
                # DESCRIPTIVE TEXT
                self.column.EC8_min_max_local_ductility_X = np.minimum(self.column.EC8_min_max_local_ductility_X, self.column.EC8_max_local_ductility_X[icomb])
                self.column.EC8_min_max_local_ductility_Y = np.minimum(self.column.EC8_min_max_local_ductility_Y, self.column.EC8_max_local_ductility_Y[icomb])

        return CpFLAGX, CpFLAGY, CpFLAGfc, aux

def _get_column_rebars(AsHXminus,AsHYminus,HX,HY,rho_min,dmin,dmax,cover,Asw_sw_recX,Asw_sw_recY,sw_min_over_fi,sw_max,fiwmin):
    """    
    Selects the longitudinal and transverse steel solution for a generic columns with dimension HX[i] and HY[i] over i range(nstoreys)
    Ensures a continuous reinforcement layout over the height of the column

    Inputs are:
                                Y
                            ^
                            |
                 ---------------------      --  ---------------
                 |   o1     G1     #1 |     |   -- cover
                 |                    |     |
                 |                    |     |
                 |   o2     +      #2 |     HY
                 |                    |     |
                 |                    |     |
                 |   o3     G3     #3 |     |   -- cover
                 ---------------------      --  ---------------> X
                 |-------- HX --------|
    
    o1+o2+o3 = AsHXminus
    o3+G3+#3 = AsHYminus

    Example: 4 storey column
    AsHXminus = 1.0e-03 * np.array([0.3105, 0.1676, 0.1285, 0.0248])
    AsHYminus = 1.0e-03 * np.array([0.4017, 0.0627, 0.0144, 0.0128])
    HX = np.array([0.40, 0.40, 0.30, 0.30])
    HY = np.array([0.35, 0.35, 0.30, 0.30])
    rho_min = 0.010
    dmin  = 0.025
    dmax  = 0.15
    cover = 0.03
    Asw_sw_recX = 0.0020 * HX --> asw/sw necessario para X
    Asw_sw_recY = 0.0020 * HY --> asw/sw necessario para Y
    sw_min_over_fi = 12

    Args:
        AsHXminus (_type_): _description_
        AsHYminus (_type_): _description_
        HX (_type_): _description_
        HY (_type_): _description_
        rho_min (_type_): _description_
        dmin (_type_): _description_
        dmax (_type_): _description_
        cover (_type_): _description_
        Asw_sw_recX (_type_): _description_
        Asw_sw_recY (_type_): _description_
        sw_min_over_fi (_type_): _description_
        sw_max (_type_): _description_
        rho_max (_type_): _description_
        fiwmin (_type_): _description_

    Returns:
        _type_: _description_
    """

    Asmin = rho_min * HX * HY
    # ...........................................................................
    # Solutions with only one diameter %fi corner goes to the other dir
    # ...........................................................................
    nfi12X = np.maximum(np.ceil(AsHXminus / (np.pi * (0.012**2) * 0.25)), 2)
    nfi12Y = np.maximum(np.ceil(AsHYminus / (np.pi * (0.012**2) * 0.25)), 2)
    nfi16X = np.maximum(np.ceil(AsHXminus / (np.pi * (0.016**2) * 0.25)), 2)
    nfi16Y = np.maximum(np.ceil(AsHYminus / (np.pi * (0.016**2) * 0.25)), 2)
    nfi20X = np.maximum(np.ceil(AsHXminus / (np.pi * (0.020**2) * 0.25)), 2)
    nfi20Y = np.maximum(np.ceil(AsHYminus / (np.pi * (0.020**2) * 0.25)), 2)
    nfi25X = np.maximum(np.ceil(AsHXminus / (np.pi * (0.025**2) * 0.25)), 2)
    nfi25Y = np.maximum(np.ceil(AsHYminus / (np.pi * (0.025**2) * 0.25)), 2)
    Distfi12X = (HY - (nfi12X)*0.012 - 2*cover - 2*0.006) / (nfi12X - 1)
    Distfi12Y = (HX - (nfi12Y)*0.012 - 2*cover - 2*0.006) / (nfi12Y - 1)
    Distfi16X = (HY - (nfi16X)*0.016 - 2*cover - 2*0.006) / (nfi16X - 1)
    Distfi16Y = (HX - (nfi16Y)*0.016 - 2*cover - 2*0.006) / (nfi16Y - 1)
    Distfi20X = (HY - (nfi20X)*0.020 - 2*cover - 2*0.006) / (nfi20X - 1)
    Distfi20Y = (HX - (nfi20Y)*0.020 - 2*cover - 2*0.006) / (nfi20Y - 1)
    Distfi25X = (HY - (nfi25X)*0.025 - 2*cover - 2*0.008) / (nfi25X - 1)
    Distfi25Y = (HX - (nfi25Y)*0.025 - 2*cover - 2*0.008) / (nfi25Y - 1)
    nfi12X[Distfi12X > 0.3] = nfi12X[Distfi12X > 0.3] + 1
    nfi16X[Distfi16X > 0.3] = nfi16X[Distfi16X > 0.3] + 1
    nfi20X[Distfi20X > 0.3] = nfi20X[Distfi20X > 0.3] + 1
    nfi25X[Distfi25X > 0.3] = nfi25X[Distfi25X > 0.3] + 1
    nfi12Y[Distfi12Y > 0.3] = nfi12Y[Distfi12Y > 0.3] + 1
    nfi16Y[Distfi16Y > 0.3] = nfi16Y[Distfi16Y > 0.3] + 1
    nfi20Y[Distfi20Y > 0.3] = nfi20Y[Distfi20Y > 0.3] + 1
    nfi25Y[Distfi25Y > 0.3] = nfi25Y[Distfi25Y > 0.3] + 1
    Distfi12X = (HY - (nfi12X)*0.012 - 2*cover - 2*0.006) / (nfi12X - 1)
    Distfi12Y = (HX - (nfi12Y)*0.012 - 2*cover - 2*0.006) / (nfi12Y - 1)
    Distfi16X = (HY - (nfi16X)*0.016 - 2*cover - 2*0.006) / (nfi16X - 1)
    Distfi16Y = (HX - (nfi16Y)*0.016 - 2*cover - 2*0.006) / (nfi16Y - 1)
    Distfi20X = (HY - (nfi20X)*0.020 - 2*cover - 2*0.006) / (nfi20X - 1)
    Distfi20Y = (HX - (nfi20Y)*0.020 - 2*cover - 2*0.006) / (nfi20Y - 1)
    Distfi25X = (HY - (nfi25X)*0.025 - 2*cover - 2*0.008) / (nfi25X - 1)
    Distfi25Y = (HX - (nfi25Y)*0.025 - 2*cover - 2*0.008) / (nfi25Y - 1)
    Area12 = (2*nfi12X + 2*(nfi12Y - 2)) * (np.pi * (0.012**2) * 0.25)
    Area16 = (2*nfi16X + 2*(nfi16Y - 2)) * (np.pi * (0.016**2) * 0.25)
    Area20 = (2*nfi20X + 2*(nfi20Y - 2)) * (np.pi * (0.020**2) * 0.25)
    Area25 = (2*nfi25X + 2*(nfi25Y - 2)) * (np.pi * (0.025**2) * 0.25)
    rho12  = Area12 / (HX * HY)
    rho16  = Area16 / (HX * HY)
    rho20  = Area20 / (HX * HY)
    rho25  = Area25 / (HX * HY)
    # ...........................................................................
    # fi12
    auxDistfi12X = np.zeros(len(HX))
    auxDistfi12Y = np.zeros(len(HX))
    for i in range(len(HX)):
        auxX = 0
        auxY = 0
        while Area12[i] - Asmin[i] < 0: # here a loop to increase the area from that fi, in case the required area less than the minumim reinforcement
            DISTVECTOR = np.array([Distfi12X[i], Distfi12Y[i]])
            aux = np.argmax(DISTVECTOR)
            if aux == 0 and auxX < 1:
                auxDistfi12X[i] = (HY[i] - nfi12X[i]*0.012 - 2*cover - 2*0.006) / (nfi12X[i] - 1)
                if auxDistfi12X[i] > dmin:
                    auxX = 0
                    nfi12X[i] = nfi12X[i] + 1
                    Distfi12X[i] = (HY[i] - nfi12X[i]*0.012 - 2*cover - 2*0.006) / (nfi12X[i] - 1)
                else:
                    auxX = 1
            elif aux == 1 and auxY < 1:
                auxDistfi12Y[i] = (HX[i] - nfi12Y[i]*0.012 - 2*cover - 2*0.006) / (nfi12Y[i] - 1)
                if auxDistfi12Y[i] > dmin:
                    auxY = 0
                    nfi12Y[i] = nfi12Y[i] + 1
                    Distfi12Y[i] = (HX[i] - nfi12Y[i]*0.012 - 2*cover - 2*0.006) / (nfi12Y[i] - 1)
                else:
                    auxY = 1
            else:
                auxX = 1
                auxY = 1
            # if auxX + auxX < 1: # This is not correct, changed to auxX + auxY (discussed with HMA)
            if auxX + auxY < 2:
                Area12[i] = (2*nfi12X[i] + 2*(nfi12Y[i]-2))*(np.pi * (0.012**2) * 0.25)
                rho12[i] = Area12[i]/HX[i]*HY[i]
            else:
                Area12[i] = 10
                rho12[i] = 10
    # ...........................................................................
    # fi16
    # ...........................................................................
    auxDistfi16X = np.zeros(len(HX))
    auxDistfi16Y = np.zeros(len(HX))
    for i in range(len(HX)):
        auxX = 0
        auxY = 0
        while Area16[i] - Asmin[i] < 0: # here a loop to increase the area from that fi, in case the required area less than the minumim reinforcement
            DISTVECTOR = np.array([Distfi16X[i], Distfi16Y[i]])
            aux = np.argmax(DISTVECTOR)
            if aux == 0 and auxX < 1:
                auxDistfi16X[i] = (HY[i] - nfi16X[i]*0.016 - 2*cover - 2*0.006) / (nfi16X[i] - 1)
                if auxDistfi16X[i] > dmin:
                    auxX = 0
                    nfi16X[i] = nfi16X[i] + 1
                    Distfi16X[i] = (HY[i] - nfi16X[i]*0.016 - 2*cover - 2*0.006) / (nfi16X[i] - 1)
                else:
                    auxX = 1
            elif aux == 1 and auxY < 1:
                auxDistfi16Y[i] = (HX[i] - nfi16Y[i]*0.016 - 2*cover - 2*0.006) / (nfi16Y[i] - 1)
                if auxDistfi16Y[i] > dmin:
                    auxY = 0
                    nfi16Y[i] = nfi16Y[i] + 1
                    Distfi16Y[i] = (HX[i] - nfi16Y[i]*0.016 - 2*cover - 2*0.006) / (nfi16Y[i] - 1)
                else:
                    auxY = 1
            else:
                auxX = 1
                auxY = 1
            # if auxX + auxX < 1: # This is not correct, changed to auxX + auxY (discussed with HMA)
            if auxX + auxY < 2:
                Area16[i] = (2*nfi16X[i] + 2*(nfi16Y[i]-2))*(np.pi * (0.016**2) * 0.25)
                rho16[i] = Area16[i]/HX[i]*HY[i]
            else:
                Area16[i] = 10
                rho16[i] = 10
    # ...........................................................................
    # fi20
    auxDistfi20X = np.zeros(len(HX))
    auxDistfi20Y = np.zeros(len(HX))
    for i in range(len(HX)):
        auxX = 0
        auxY = 0
        while Area20[i] - Asmin[i] < 0: # here a loop to increase the area from that fi, in case the required area less than the minumim reinforcement
            DISTVECTOR = np.array([Distfi20X[i], Distfi20Y[i]])
            aux = np.argmax(DISTVECTOR)
            if aux == 0 and auxX < 1:
                auxDistfi20X[i] = (HY[i] - nfi20X[i]*0.020 - 2*cover - 2*0.006) / (nfi20X[i] - 1)
                if auxDistfi20X[i] > dmin:
                    auxX = 0
                    nfi20X[i] = nfi20X[i] + 1
                    Distfi20X[i] = (HY[i] - nfi20X[i]*0.020 - 2*cover - 2*0.006) / (nfi20X[i] - 1)
                else:
                    auxX = 1
            elif aux == 1 and auxY < 1:
                auxDistfi20Y[i] = (HX[i] - nfi20Y[i]*0.020 - 2*cover - 2*0.006) / (nfi20Y[i] - 1)
                if auxDistfi20Y[i] > dmin:
                    auxY = 0
                    nfi20Y[i] = nfi20Y[i] + 1
                    Distfi20Y[i] = (HX[i] - nfi20Y[i]*0.020 - 2*cover - 2*0.006) / (nfi20Y[i] - 1)
                else:
                    auxY = 1
            else:
                auxX = 1
                auxY = 1
            # if auxX + auxX < 1: # This is not correct, changed to auxX + auxY (discussed with HMA)
            if auxX + auxY < 2:
                Area20[i] = (2*nfi20X[i] + 2*(nfi20Y[i]-2))*(np.pi * (0.020**2) * 0.25)
                rho20[i] = Area20[i]/HX[i]*HY[i]
            else:
                Area20[i] = 10
                rho20[i] = 10
    # ...........................................................................
    # fi25
    auxDistfi25X = np.zeros(len(HX))
    auxDistfi25Y = np.zeros(len(HX))
    for i in range(len(HX)):
        auxX = 0
        auxY = 0
        while Area25[i] - Asmin[i] < 0: # here a loop to increase the area from that fi, in case the required area less than the minumim reinforcement
            DISTVECTOR = np.array([Distfi25X[i], Distfi25Y[i]])
            aux = np.argmax(DISTVECTOR)
            if aux == 0 and auxX < 1:
                auxDistfi25X[i] = (HY[i] - nfi25X[i]*0.025 - 2*cover - 2*0.006) / (nfi25X[i] - 1)
                if auxDistfi25X[i] > dmin:
                    auxX = 0
                    nfi25X[i] = nfi25X[i] + 1
                    Distfi25X[i] = (HY[i] - nfi25X[i]*0.025 - 2*cover - 2*0.006) / (nfi25X[i] - 1)
                else:
                    auxX = 1
            elif aux == 1 and auxY < 1:
                auxDistfi25Y[i] = (HX[i] - nfi25Y[i]*0.025 - 2*cover - 2*0.006) / (nfi25Y[i] - 1)
                if auxDistfi25Y[i] > dmin:
                    auxY = 0
                    nfi25Y[i] = nfi25Y[i] + 1
                    Distfi25Y[i] = (HX[i] - nfi25Y[i]*0.025 - 2*cover - 2*0.006) / (nfi25Y[i] - 1)
                else:
                    auxY = 1
            else:
                auxX = 1
                auxY = 1
            # if auxX + auxX < 1: # This is not correct, changed to auxX + auxY (discussed with HMA)
            if auxX + auxY < 2:
                Area25[i] = (2*nfi25X[i] + 2*(nfi25Y[i]-2))*(np.pi * (0.025**2) * 0.25)
                rho25[i] = Area25[i]/HX[i]*HY[i]
            else:
                Area25[i] = 10
                rho25[i] = 10
    # ...........................................................................
    # Solution with lower fi interior bars and higher fi_corner %fi corner gos to the other dir
    # ...........................................................................
    nfi12Xint = np.maximum(np.ceil((AsHXminus - 2 * (np.pi * (0.016**2) * 0.25)) / (np.pi * (0.012**2) * 0.25)), 0)
    nfi12Yint = np.maximum(np.ceil((AsHYminus - 2 * (np.pi * (0.016**2) * 0.25)) / (np.pi * (0.012**2) * 0.25)), 0)
    nfi16Xint = np.maximum(np.ceil((AsHXminus - 2 * (np.pi * (0.020**2) * 0.25)) / (np.pi * (0.016**2) * 0.25)), 0)
    nfi16Yint = np.maximum(np.ceil((AsHYminus - 2 * (np.pi * (0.020**2) * 0.25)) / (np.pi * (0.016**2) * 0.25)), 0)
    nfi20Xint = np.maximum(np.ceil((AsHXminus - 2 * (np.pi * (0.025**2) * 0.25)) / (np.pi * (0.020**2) * 0.25)), 0)
    nfi20Yint = np.maximum(np.ceil((AsHYminus - 2 * (np.pi * (0.025**2) * 0.25)) / (np.pi * (0.020**2) * 0.25)), 0)
    Distfi12Xint = (HY - 2*0.016 - nfi12Xint*0.012 - 2*cover - 2*0.006) / (nfi12Xint + 2 - 1)
    Distfi12Yint = (HX - 2*0.016 - nfi12Yint*0.012 - 2*cover - 2*0.006) / (nfi12Yint + 2 - 1)
    Distfi16Xint = (HY - 2*0.020 - nfi16Xint*0.016 - 2*cover - 2*0.006) / (nfi16Xint + 2 - 1)
    Distfi16Yint = (HX - 2*0.020 - nfi16Yint*0.016 - 2*cover - 2*0.006) / (nfi16Yint + 2 - 1)
    Distfi20Xint = (HY - 2*0.025 - nfi20Xint*0.020 - 2*cover - 2*0.008) / (nfi20Xint + 2 - 1)
    Distfi20Yint = (HX - 2*0.025 - nfi20Yint*0.020 - 2*cover - 2*0.008) / (nfi20Yint + 2 - 1)
    Area12int = 4 * (np.pi * (0.016**2) *0.25) + (2*nfi12Xint + 2*nfi12Yint) * (np.pi *(0.012**2) * 0.25)
    Area16int = 4 * (np.pi * (0.020**2) *0.25) + (2*nfi16Xint + 2*nfi16Yint) * (np.pi *(0.016**2) * 0.25)
    Area20int = 4 * (np.pi * (0.025**2) *0.25) + (2*nfi20Xint + 2*nfi20Yint) * (np.pi *(0.020**2) * 0.25)
    rho12int = Area12int / (HX * HY)
    rho16int = Area16int / (HX * HY)
    rho20int = Area20int / (HX * HY)
    # ...........................................................................
    # fi12
    auxDistfi12Xint = np.zeros(len(HX))
    auxDistfi12Yint = np.zeros(len(HX))
    for i in range(len(HX)):
        auxX = 0
        auxY = 0
        while Area12int[i] - Asmin[i] < 0:
            DISTVECTOR = np.array([Distfi12Xint[i], Distfi12Yint[i]])
            aux = np.argmax(DISTVECTOR)
            if aux == 0 and auxX < 1:
                auxDistfi12Xint[i] = (HY[i] - 2*0.016 - nfi12Xint[i]*0.012 - 2*cover - 2*0.006) / (nfi12Xint[i] + 2 - 1)
                if auxDistfi12Xint[i] > dmin:
                    auxX = 0
                    nfi12Xint[i] = nfi12Xint[i] + 1
                    Distfi12Xint[i] = (HY[i] - 2*0.016 - nfi12Xint[i]*0.012 - 2*cover - 2*0.006) / (nfi12Xint[i] + 2 - 1)
                else:
                    auxX = 1
            elif aux == 1 and auxY < 1:
                auxDistfi12Yint[i] = (HX[i] - 2*0.016 - nfi12Yint[i]*0.012 - 2*cover - 2*0.006) / (nfi12Yint[i] + 2 - 1)
                if auxDistfi12Yint[i] > dmin:
                    auxY = 0
                    nfi12Yint[i] = nfi12Yint[i] + 1
                    Distfi12Yint[i] = (HX[i] - 2*0.016 - nfi12Yint[i]*0.012 - 2*cover - 2*0.006) / (nfi12Yint[i] + 2 - 1)
                else:
                    auxY = 1
            else:
                auxX = 1
                auxY = 1
            # if auxX + auxX < 2: # This is not correct, changed to auxX + auxY (discussed with HMA)
            if auxX + auxY < 2:
                Area12int[i] = 4 * (np.pi * (0.016**2) * 0.25) + (2*nfi12Xint[i] + 2*nfi12Yint[i]) * (np.pi * (0.012**2)*0.25)
                rho12int[i]  = Area12int[i] / HX[i] * HY[i]
            else:
                Area12int[i] = 10
                rho12int[i]  = 10
    # ...........................................................................
    # fi16
    auxDistfi16Xint = np.zeros(len(HX))
    auxDistfi16Yint = np.zeros(len(HX))
    for i in range(len(HX)):
        auxX = 0
        auxY = 0
        while Area16int[i] - Asmin[i] < 0:
            DISTVECTOR = np.array([Distfi16Xint[i], Distfi16Yint[i]])
            aux = np.argmax(DISTVECTOR)
            if aux == 0 and auxX < 1:
                auxDistfi16Xint[i] = (HY[i] - 2*0.02 - nfi16Xint[i]*0.016 - 2*cover - 2*0.006) / (nfi16Xint[i] + 2 - 1)
                if auxDistfi16Xint[i] > dmin:
                    auxX = 0
                    nfi16Xint[i] = nfi16Xint[i] + 1
                    Distfi16Xint[i] = (HY[i] - 2*0.02 - nfi16Xint[i]*0.016 - 2*cover - 2*0.006) / (nfi16Xint[i] + 2 - 1)
                else:
                    auxX = 1
            elif aux == 1 and auxY < 1:
                auxDistfi16Yint[i] = (HX[i] - 2*0.02 - nfi16Yint[i]*0.016 - 2*cover - 2*0.006) / (nfi16Yint[i] + 2 - 1)
                if auxDistfi16Yint[i] > dmin:
                    auxY = 0
                    nfi16Yint[i] = nfi16Yint[i] + 1
                    Distfi16Yint[i] = (HX[i] - 2*0.02 - nfi16Yint[i]*0.016 - 2*cover - 2*0.006) / (nfi16Yint[i] + 2 - 1)
                else:
                    auxY = 1
            else:
                auxX = 1
                auxY = 1
            # if auxX + auxX < 2: # This is not correct, changed to auxX + auxY (discussed with HMA)
            if auxX + auxY < 2:
                Area16int[i] = 4 * (np.pi * (0.02**2) * 0.25) + (2*nfi16Xint[i] + 2*nfi16Yint[i]) * (np.pi * (0.016**2) * 0.25)
                rho16int[i]  = Area16int[i] / HX[i] * HY[i]
            else:
                Area16int[i] = 10
                rho16int[i]  = 10
    # ...........................................................................
    # fi20
    auxDistfi20Xint = np.zeros(len(HX))
    auxDistfi20Yint = np.zeros(len(HX))
    for i in range(len(HX)):
        auxX = 0
        auxY = 0
        while Area20int[i] - Asmin[i] < 0:
            DISTVECTOR = np.array([Distfi20Xint[i], Distfi20Yint[i]])
            aux = np.argmax(DISTVECTOR)
            if aux == 0 and auxX < 1:
                auxDistfi20Xint[i] = (HY[i] - 2*0.025 - nfi20Xint[i]*0.020 - 2*cover - 2*0.006) / (nfi20Xint[i] + 2 - 1)
                if auxDistfi20Xint[i] > dmin:
                    auxX = 0
                    nfi20Xint[i] = nfi20Xint[i] + 1
                    Distfi20Xint[i] = (HY[i] - 2*0.025 - nfi20Xint[i]*0.020 - 2*cover - 2*0.006) / (nfi20Xint[i] + 2 - 1)
                else:
                    auxX = 1

            elif aux == 1 and auxY < 1:
                auxDistfi20Yint[i] = (HX[i] - 2*0.025 - nfi20Yint[i]*0.020 - 2*cover - 2*0.006) / (nfi20Yint[i] + 2 - 1)
                if auxDistfi20Yint[i] > dmin:
                    auxY = 0
                    nfi20Yint[i] = nfi20Yint[i] + 1
                    Distfi20Yint[i] = (HX[i] - 2*0.025 - nfi20Yint[i]*0.020 - 2*cover - 2*0.006) / (nfi20Yint[i] + 2 - 1)
                else:
                    auxY = 1
            else:
                auxX = 1
                auxY = 1
            # if auxX + auxX < 2: # This is not correct, changed to auxX + auxY (discussed with HMA)
            if auxX + auxY < 2:
                Area20int[i] = 4 * (np.pi * (0.025**2) * 0.25) + (2*nfi20Xint[i] + 2*nfi20Yint[i]) * (np.pi * (0.020**2) * 0.25)
                rho20int[i]  = Area20int[i] / HX[i] * HY[i]
            else:
                Area20int[i] = 10
                rho20int[i]  = 10
    # ...........................................................................
    # Get the minimum area using only one fi or a lower fi for interior bars. 
    # Verification made by compatibilization over the entire height of each column (ground to roof)
    # ...........................................................................
    # compute the distance between the rebars to check dmin
    # ...........................................................................
    Distfi12R = np.minimum(Distfi12X, Distfi12Y)
    Distfi16R = np.minimum(Distfi16X, Distfi16Y)
    Distfi20R = np.minimum(Distfi20X, Distfi16Y)
    # Distfi25R = np.minimum(Distfi25X, Distfi25Y)
    Distfi12Rint = np.minimum(Distfi12Xint, Distfi12Yint)
    Distfi16Rint = np.minimum(Distfi16Xint, Distfi16Yint)
    # Distfi20Rint = np.minimum(Distfi20Xint, Distfi20Yint)
    Area12[Distfi12R < dmin] = 10
    Area16[Distfi16R < dmin] = 10
    Area20[Distfi20R < dmin] = 10
    # Area25[Distfi25R < dmin]=1
    Area12int[Distfi12Rint < dmin] = 10
    Area16int[Distfi16Rint < dmin] = 10
    # Area20int[Distfi20Rint < dmin] = 1
    # ...........................................................................
    solfinal12corner = np.zeros(len(HX))
    solfinal16corner = np.zeros(len(HX))
    solfinal20corner = np.zeros(len(HX))
    solfinal25corner = np.zeros(len(HX))
    posit16 = np.zeros(len(HX))
    posit20 = np.zeros(len(HX))
    posit25 = np.zeros(len(HX))
    for i in range(len(HX)):
        solfinal12corner[i] = Area12[i].copy()
        solfinal16corner[i] = min([Area16[i], Area12int[i]])
        solfinal20corner[i] = min([Area20[i], Area16int[i]])
        solfinal25corner[i] = min([Area25[i], Area20int[i]])
        posit16[i] = [Area16[i], Area12int[i]].index(solfinal16corner[i])
        posit20[i] = [Area20[i], Area16int[i]].index(solfinal20corner[i])
        posit25[i] = [Area25[i], Area20int[i]].index(solfinal25corner[i])

    aux12 = np.sum(solfinal12corner)
    aux16 = np.sum(solfinal16corner)
    aux20 = np.sum(solfinal20corner)
    aux25 = np.sum(solfinal25corner)

    solutions = np.array([aux12, aux16, aux20, aux25])
    indexsol = np.argmin(solutions)
    # indexsol =2 
    # posit20 = np.ones(len(posit20.flatten()))
    # ...........................................................................
    # Get the final solution
    # ...........................................................................
    fi_corner = np.zeros(len(HX))
    fi_layintX = np.zeros(len(HX))
    nbar_HminusX = np.zeros(len(HX))
    nlayintX = np.zeros(len(HX))
    Rhosl = np.zeros(len(HX))
    RhoslX = np.zeros(len(HX))
    RhoslY = np.zeros(len(HX))
    Rhosla = np.zeros(len(HX))
    for j in range(len(HX)):
        if indexsol == 0:
            fi_corner[j] = 0.012
            fi_layintX[j] = 0.012
            nbar_HminusX[j] = nfi12X[j] + 0
            nlayintX[j] = nfi12Y[j] - 2
            Rhosl[j] = Area12[j] / (HX[j] * HY[j])
            RhoslX[j] = 2* (nfi12X[j] * np.pi * (0.012**2) * 0.25) / (HX[j] * HY[j])
            RhoslY[j] = 2* (nfi12Y[j] * np.pi * (0.012**2) * 0.25) / (HX[j] * HY[j])
            Rhosla[j] = RhoslY[j] + RhoslX[j] - ((4 * np.pi * (0.012**2) * 0.25) / (HX[j] * HY[j]))
        elif indexsol == 1:
            if posit16[j] == 0:
                fi_corner[j] = 0.016
                fi_layintX[j] = 0.016
                nbar_HminusX[j] = nfi16X[j] + 0
                nlayintX[j] = nfi16Y[j] - 2
                Rhosl[j] = Area16[j] / (HX[j] * HY[j])
                RhoslX[j] = 2 * (nfi16X[j] * np.pi * (0.016**2) * 0.25) / (HX[j] * HY[j])
                RhoslY[j] = 2 * (nfi16Y[j] * np.pi * (0.016**2) * 0.25) / (HX[j] * HY[j])
                Rhosla[j] = RhoslY[j] + RhoslX[j] - ((4 * np.pi * (0.016**2) * 0.25) / (HX[j] * HY[j]))
            else:
                fi_corner[j] = 0.016
                fi_layintX[j] = 0.012
                nbar_HminusX[j] = nfi12Xint[j] + 2
                nlayintX[j] = nfi12Yint[j] + 0
                Rhosl[j] = Area12int[j] / (HX[j] * HY[j])
                RhoslX[j] = 2 * (2 * (np.pi * (0.016**2) * 0.25) + (nfi12Xint[j]) * (np.pi * (0.012**2) * 0.25))/(HX[j] * HY[j])
                RhoslY[j] = 2 * (2 * (np.pi * (0.016**2) * 0.25) + (nfi12Yint[j]) * (np.pi * (0.012**2) * 0.25))/(HX[j] * HY[j])
                Rhosla[j] = RhoslY[j] + RhoslX[j] - ((4 * np.pi * (0.016**2) * 0.25) / (HX[j] * HY[j]))
        elif indexsol == 2:
            if posit20[j] == 0:
                fi_corner[j] = 0.020
                fi_layintX[j] = 0.020
                nbar_HminusX[j] = nfi20X[j] + 0
                nlayintX[j] = nfi20Y[j] - 2
                Rhosl[j] = Area20[j] / (HX[j] * HY[j])
                RhoslX[j] = 2 * (nfi20X[j] * np.pi * (0.020**2) * 0.25) / (HX[j] * HY[j])
                RhoslY[j] = 2 * (nfi20Y[j] * np.pi * (0.020**2) * 0.25) / (HX[j] * HY[j])
                Rhosla[j] = RhoslY[j] + RhoslX[j] - ((4 * np.pi * (0.02**2) * 0.25) / (HX[j] * HY[j]))
            else:
                fi_corner[j]  = 0.020
                fi_layintX[j] = 0.016
                nbar_HminusX[j] = nfi16Xint[j] + 2
                nlayintX[j] = nfi16Yint[j] + 0
                Rhosl[j] = Area16int[j] / (HX[j] * HY[j])
                RhoslX[j] = 2 * (2 * (np.pi * (0.020**2) * 0.25) + nfi16Xint[j] * (np.pi * (0.016**2) * 0.25)) / (HX[j] * HY[j])
                RhoslY[j] = 2 * (2 * (np.pi * (0.020**2) * 0.25) + nfi16Yint[j] * (np.pi * (0.016**2) * 0.25)) / (HX[j] * HY[j])
                Rhosla[j] = RhoslY[j] + RhoslX[j] - ((4 * np.pi * (0.02**2) * 0.25) / (HX[j] * HY[j]))
        else:
            if posit25[j] == 0:
                fi_corner[j] = 0.025
                fi_layintX[j] = 0.025
                nbar_HminusX[j] = nfi25X[j]
                nlayintX[j] = nfi25Y[j] - 2
                Rhosl[j] = Area25[j] / (HX[j] * HY[j])
                RhoslX[j] = 2 * (nfi25X[j] * np.pi * (0.025**2) * 0.25) / (HX[j] * HY[j])
                RhoslY[j] = 2 * (nfi25Y[j] * np.pi * (0.025**2) * 0.25) / (HX[j] * HY[j])
                Rhosla[j] = RhoslY[j] + RhoslX[j] - ((4 * np.pi * (0.025**2) * 0.25) / (HX[j] * HY[j]))
            else:
                fi_corner[j] = 0.025
                fi_layintX[j] = 0.020
                nbar_HminusX[j] = nfi20Xint[j] + 2
                nlayintX[j] = nfi20Yint[j]
                Rhosl[j] = Area20int[j] / (HX[j] * HY[j])
                RhoslX[j] = 2 * (2 * (np.pi * (0.025**2) * 0.25) + nfi20Xint[j] * (np.pi * (0.020**2) * 0.25)) / (HX[j] * HY[j])
                RhoslY[j] = 2 * (2 * (np.pi * (0.025**2) * 0.25) + nfi20Yint[j] * (np.pi * (0.020**2) * 0.25)) / (HX[j] * HY[j])
                Rhosla[j] = RhoslY[j] + RhoslX[j] - ((4 * np.pi * (0.025**2) * 0.25) / (HX[j] * HY[j]))
    # Rhosla/Rhosl
    # ...........................................................................
    # Transverse Steel
    # ...........................................................................
    nwparallel_to_X = np.zeros(len(HX))
    nwparallel_to_Y = np.zeros(len(HX))
    sw = np.zeros(len(HX)) 
    fiw = np.zeros(len(HX)) 
    for j in range(len(HX)):
        Dinf_per_bar = 10
        nwparallel_to_Xc = 1
        nwparallel_to_Yc = 1
        while Dinf_per_bar > dmax:
            nwparallel_to_Xc = nwparallel_to_Xc + 1
            nwparallel_to_Yc = nwparallel_to_Yc + 1
            Dinf_per_barX = 0.90 * HX[j] / nwparallel_to_Xc
            Dinf_per_barY = 0.90 * HY[j] / nwparallel_to_Yc
            Dinf_per_bar = max(Dinf_per_barX, Dinf_per_barY)

        nwparallel_to_X[j] = nwparallel_to_Xc
        nwparallel_to_Y[j] = nwparallel_to_Yc
        if fi_corner[j] > 0.020:
            fiwminc = 0.008
        else:
            fiwminc = 0.006

        fiwminc = max(fiwmin, fiwminc)
        swminim = min([sw_max[j], sw_min_over_fi*max(fi_corner[j], fi_layintX[j]), HX[j], HY[j]])
        AswsolX = 0
        AswsolY = 0
        while AswsolX == 0 or AswsolY == 0:
            AswX = 0.25 * np.pi * nwparallel_to_X[j] * (fiwminc**2)
            AswY = 0.25 * np.pi * nwparallel_to_Y[j] * (fiwminc**2)
            swcX = AswX / Asw_sw_recX[j]
            swcY = AswY / Asw_sw_recY[j]
            swc = min([swcX, swcY, swminim])
            if swc > 0.25:
                sw[j] = 0.25
                AswsolX = AswX / sw[j]
                AswsolY = AswY / sw[j]
            elif swc > 0.20:
                sw[j] = 0.20
                AswsolX = AswX / sw[j]
                AswsolY = AswY / sw[j]
            elif swc > 0.15:
                sw[j] = 0.15
                AswsolX = AswX / sw[j]
                AswsolY = AswY / sw[j]
            elif swc > 0.12:
                sw[j] = 0.125
                AswsolX = AswX / sw[j]
                AswsolY = AswY / sw[j]
            elif swc > 0.10:
                sw[j] = 0.10
                AswsolX = AswX / sw[j]
                AswsolY = AswY / sw[j]
            elif swc > 0.075:
                sw[j] = 0.075
                AswsolX = AswX / sw[j]
                AswsolY = AswY / sw[j]
            elif swc > 0.05:
                sw[j] = 0.05
                AswsolX = AswX / sw[j]
                AswsolY = AswY / sw[j]
            else:
                fiwminc = fiwminc + 0.002
                AswsolX = 0
                AswsolY = 0

        fiw[j] = fiwminc + 0

    return fi_corner, fi_layintX, nbar_HminusX, nlayintX, Rhosl, RhoslX, RhoslY, sw, fiw, nwparallel_to_X, nwparallel_to_Y

def _get_beam_rebars(NeededAsBOT,NeededAsTOP,Bbeams,top_to_bot_ratio,dmax,Asw_sw,sw_max,sw_min_over_fi,dmin):
    """
    Selects the longitudinal and transverse steel solution for a generic
    beam with dimension BB and HH over an alignment with n beam spans
    Ensures a continuous reinforcement layout over the alignement

                        Y
                        ^
                        |     
            ---------------------      -------------
            |   o1     o1     o1 |     |   -- cover
            |                    |     |
            |                    |     |
            |         +          |     HY  
            |                    |     |
            |                    |     |
            |   #2     #2     #2 |     |   -- cover
            ---------------------      -------------  ----> X
            |-------- HX --------|
    
    o1+o1+o1 = NeededAsTO
    #2+#2+#2 = NeededAsBOT

    Example: Beam alignement with 3 beam spans
    Bbeams = [0.3;0.3;0.3;0.3;0.3;0.3;0.3;0.3;0.3];
    NeededAsBOT = [0.000211660935387516;1.00000000000000e-08;0.000207567027067459;0.000206878174637212;1.15128354291670e-05;0.000206880524986188;0.000207565390516080;1.00000000000000e-08;0.000211659183816633];
    NeededAsTOP = 10.*[0.000211660935387516;1.00000000000000e-08;0.000207567027067459;0.000206878174637212;1.15128354291670e-05;0.000206880524986188;0.000207565390516080;1.00000000000000e-08;0.000211659183816633];
    top_to_bot_ratio = 0.30;
    dmax   = 0.1;
    Asw_sw = [0.000211660935387516;1.00000000000000e-08;0.000207567027067459;0.000206878174637212;1.15128354291670e-05;0.000206880524986188;0.000207565390516080;1.00000000000000e-08;0.000211659183816633];
    sw_max = [0.15;0.20;0.15;0.15;0.15;0.15;0.15;0.15;0.15];

    Args:
        NeededAsBOT (_type_): _description_
        NeededAsTOP (_type_): _description_
        Bbeams (_type_): _description_
        top_to_bot_ratio (_type_): _description_
        dmax (_type_): _description_
        Asw_sw (_type_): _description_
        sw_max (_type_): _description_
        sw_min_over_fi (_type_): _description_
        dmin (_type_): _description_

    Returns:
        _type_: _description_
    """
    NeededAsBOT = NeededAsBOT + top_to_bot_ratio * NeededAsTOP
    NeededAsTOP = NeededAsTOP + top_to_bot_ratio * NeededAsBOT
    NeededAs = NeededAsTOP.copy()
    NeededAs[NeededAs < 1.1310e-04] = 1.1310e-04

    # ...........................................................................
    # 1) Longitudinal Reinforcement
    # ...........................................................................
    # TOP Reinforcement
    # ...........................................................................
    # solutions with only one diameter
    # ...........................................................................
    nfi12 = np.maximum(np.ceil(NeededAs / (np.pi * (0.012**2) * 0.25)), 2)
    nfi16 = np.maximum(np.ceil(NeededAs / (np.pi * (0.016**2) * 0.25)), 2)
    nfi20 = np.maximum(np.ceil(NeededAs / (np.pi * (0.020**2) * 0.25)), 2)
    nfi25 = np.maximum(np.ceil(NeededAs / (np.pi * (0.025**2) * 0.25)), 2)
    Distfi12X = (Bbeams - (nfi12 * 0.012 + 2 * 0.03 + 2 * 0.006)) / (nfi12 - 1)
    Distfi16X = (Bbeams - (nfi16 * 0.016 + 2 * 0.03 + 2 * 0.006)) / (nfi16 - 1)
    Distfi20X = (Bbeams - (nfi20 * 0.020 + 2 * 0.03 + 2 * 0.006)) / (nfi20 - 1)
    Distfi25X = (Bbeams - (nfi25 * 0.025 + 2 * 0.03 + 2 * 0.006)) / (nfi25 - 1)
    Distfi12X = np.round(Distfi12X, 8)
    Distfi16X = np.round(Distfi16X, 8)
    Distfi20X = np.round(Distfi20X, 8)
    Distfi25X = np.round(Distfi25X, 8)

    for ii in range(len(nfi12)):
        while Distfi12X[ii] > dmax:
            nfi12[ii] = nfi12[ii] + 1
            Distfi12X[ii] = (Bbeams[ii] - (nfi12[ii] * 0.012 + 2 * 0.03 + 2 * 0.006)) / (nfi12[ii] - 1)
            Distfi12X = np.round(Distfi12X, 8)

        while Distfi16X[ii] > dmax:
            nfi16[ii] = nfi16[ii] + 1
            Distfi16X[ii] = (Bbeams[ii] - (nfi16[ii] * 0.016 + 2 * 0.03 + 2 * 0.006)) / (nfi16[ii] - 1)
            Distfi16X = np.round(Distfi16X, 8)

        while Distfi20X[ii] > dmax:
            nfi20[ii] = nfi20[ii] + 1
            Distfi20X[ii] = (Bbeams[ii] - (nfi20[ii] * 0.020 + 2 * 0.03 + 2 * 0.006)) / (nfi20[ii] - 1)
            Distfi20X = np.round(Distfi20X, 8)

        while Distfi25X[ii] > dmax:
            nfi25[ii] = nfi25[ii] + 1
            Distfi25X[ii] = (Bbeams[ii] - (nfi25[ii] * 0.025 + 2 * 0.03 + 2 * 0.006)) / (nfi25[ii] - 1)
            Distfi25X = np.round(Distfi25X, 8)

    Area12 = nfi12 * (np.pi * (0.012 ** 2) * 0.25)
    Area16 = nfi16 * (np.pi * (0.016 ** 2) * 0.25)
    Area20 = nfi20 * (np.pi * (0.020 ** 2) * 0.25)
    Area25 = nfi25 * (np.pi * (0.025 ** 2) * 0.25)
    Rat12 = Area12 / NeededAs
    Rat12[Rat12 < 1] = 1000  # Redundant (Rat is always greater than 1)
    Rat12[Distfi12X < dmin] = 1000
    Rat16 = Area16 / NeededAs
    Rat16[Rat16 < 1] = 1000
    Rat16[Distfi16X < dmin] = 1000 # changed from 100 to 1000
    Rat20 = Area20 / NeededAs
    Rat20[Rat20<1] = 1000
    Rat20[Distfi20X < dmin] = 1000
    Rat25 = Area25 / NeededAs
    Rat25[Rat25 < 1] = 1000
    Rat25[Distfi25X < dmin] = 1000

    # solution with lower 2fi(16 ou 20 ou 25 + interior bars with lower diameter
    # ...........................................................................
    n2fi16Xint = np.maximum(np.ceil((NeededAs - (2 * np.pi * (0.016**2) * 0.25)) / (np.pi * (0.012**2) * 0.25)), 1)
    n2fi20Xint = np.maximum(np.ceil((NeededAs - (2 * np.pi * (0.020**2) * 0.25)) / (np.pi * (0.016**2) * 0.25)), 1)
    n2fi25Xint = np.maximum(np.ceil((NeededAs - (2 * np.pi * (0.025**2) * 0.25)) / (np.pi * (0.020**2) * 0.25)), 1)
    Dist2fi16Xint = (Bbeams - (2*0.016 + n2fi16Xint*0.012 + 2 *0.03 + 2*0.006)) / (n2fi16Xint + 2 - 1)
    Dist2fi20Xint = (Bbeams - (2*0.020 + n2fi20Xint*0.016 + 2 *0.03 + 2*0.006)) / (n2fi20Xint + 2 - 1)
    Dist2fi25Xint = (Bbeams - (2*0.025 + n2fi25Xint*0.020 + 2 *0.03 + 2*0.006)) / (n2fi25Xint + 2 - 1)
    Dist2fi16Xint = np.round(Dist2fi16Xint, 8)
    Dist2fi20Xint = np.round(Dist2fi20Xint, 8)
    Dist2fi25Xint = np.round(Dist2fi25Xint, 8)
    for ii in range(len(n2fi16Xint)):
        while Dist2fi16Xint[ii] > dmax:
            n2fi16Xint[ii] = n2fi16Xint[ii] + 1
            Dist2fi16Xint[ii] = (Bbeams[ii] - (2 * 0.016 + n2fi16Xint[ii] * 0.012 + 2 * 0.03 + 2 * 0.006)) / (n2fi16Xint[ii] + 2 - 1)
            Dist2fi16Xint = np.round(Dist2fi16Xint, 8)

        while Dist2fi20Xint[ii] > dmax:
            n2fi20Xint[ii] = n2fi20Xint[ii] + 1
            Dist2fi20Xint[ii] = (Bbeams[ii] - (2 * 0.020 + n2fi20Xint[ii] * 0.016 + 2 * 0.03 + 2 * 0.006)) / (n2fi20Xint[ii] + 2 - 1)
            Dist2fi20Xint = np.round(Dist2fi20Xint, 8)

        while Dist2fi25Xint[ii] > dmax:
            n2fi25Xint[ii] = n2fi25Xint[ii] + 1
            Dist2fi25Xint[ii] = (Bbeams[ii] - (2 * 0.025 + n2fi25Xint[ii] * 0.020 + 2 * 0.03 + 2 * 0.006)) / (n2fi25Xint[ii] + 2 - 1) # The denominator was wrong in the original version, it was modified
            Dist2fi25Xint = np.round(Dist2fi25Xint, 8)

    Area2fi16Xint = 2 * (np.pi * (0.016**2) * 0.25) + n2fi16Xint * (np.pi * (0.012**2) * 0.25)
    Area2fi20Xint = 2 * (np.pi * (0.020**2) * 0.25) + n2fi20Xint * (np.pi * (0.016**2) * 0.25)
    Area2fi25Xint = 2 * (np.pi * (0.025**2) * 0.25) + n2fi25Xint * (np.pi * (0.020**2) * 0.25)
    Rat2fi16Xint = Area2fi16Xint / NeededAs
    Rat2fi16Xint[Rat2fi16Xint < 1] = 1000
    Rat2fi16Xint[Dist2fi16Xint < dmin] = 1000
    Rat2fi20Xint = Area2fi20Xint / NeededAs
    Rat2fi20Xint[Rat2fi20Xint < 1] = 1000
    Rat2fi20Xint[Dist2fi20Xint < dmin] = 1000
    Rat2fi25Xint = Area2fi25Xint / NeededAs
    Rat2fi25Xint[Rat2fi25Xint < 1] = 1000
    Rat2fi25Xint[Dist2fi25Xint < dmin] = 1000

    # solution with lower 3fi(16 ou 20 ou 25 + interior bars with lower diameter
    # TODO: What does this mean? We cannot have 3fi, we assume corners have 1 bar
    # ...........................................................................
    n3fi16Xint = np.maximum(np.ceil((NeededAs - (3 * np.pi * (0.016**2) * 0.25)) / (np.pi * (0.012**2) * 0.25)), 2)
    n3fi20Xint = np.maximum(np.ceil((NeededAs - (3 * np.pi * (0.020**2) * 0.25)) / (np.pi * (0.016**2) * 0.25)), 2)
    n3fi25Xint = np.maximum(np.ceil((NeededAs - (3 * np.pi * (0.025**2) * 0.25)) / (np.pi * (0.020**2) * 0.25)), 2)
    Dist3fi16Xint = (Bbeams - (3 * 0.016 + n3fi16Xint * 0.012 + 2 * 0.03 + 2 * 0.006)) / (n3fi16Xint + 3 - 1)
    Dist3fi20Xint = (Bbeams - (3 * 0.020 + n3fi20Xint * 0.016 + 2 * 0.03 + 2 * 0.006)) / (n3fi20Xint + 3 - 1)
    Dist3fi25Xint = (Bbeams - (3 * 0.025 + n3fi25Xint * 0.020 + 2 * 0.03 + 2 * 0.006)) / (n3fi25Xint + 3 - 1)
    Dist3fi16Xint = np.round(Dist3fi16Xint, 8)
    Dist3fi20Xint = np.round(Dist3fi20Xint, 8)
    Dist3fi25Xint = np.round(Dist3fi25Xint, 8)

    for ii in range(len(n3fi16Xint)):
        while Dist3fi16Xint[ii] > dmax:
            n3fi16Xint[ii] = n3fi16Xint[ii] + 1
            Dist3fi16Xint[ii] = (Bbeams[ii] - (3 * 0.016 + n3fi16Xint[ii] * 0.012 + 2 * 0.03 + 2 * 0.006)) / (n3fi16Xint[ii] + 3 - 1)
            Dist3fi16Xint = np.round(Dist3fi16Xint, 8)

        while Dist3fi20Xint[ii] > dmax:
            n3fi20Xint[ii] = n3fi20Xint[ii] + 1
            Dist3fi20Xint[ii] = (Bbeams[ii] - (3 * 0.020 + n3fi20Xint[ii] * 0.016 + 2 * 0.03 + 2 * 0.006)) / (n3fi20Xint[ii] + 3 - 1)
            Dist3fi20Xint = np.round(Dist3fi20Xint, 8)

        while Dist3fi25Xint[ii] > dmax:
            n3fi25Xint[ii] = n3fi25Xint[ii] + 1
            Dist3fi25Xint[ii] = (Bbeams[ii] - (3 * 0.025 + n3fi25Xint[ii] * 0.020 + 2 * 0.03 + 2 * 0.006)) / (n3fi25Xint[ii] + 3 - 1) # The denominator was wrong in the original version, it was modified
            Dist3fi25Xint = np.round(Dist3fi25Xint, 8)

    Area3fi16Xint = 3 * (np.pi * (0.016**2) * 0.25) + n3fi16Xint * (np.pi * (0.012**2) * 0.25)
    Area3fi20Xint = 3 * (np.pi * (0.020**2) * 0.25) + n3fi20Xint * (np.pi * (0.016**2) * 0.25)
    Area3fi25Xint = 3 * (np.pi * (0.025**2) * 0.25) + n3fi25Xint * (np.pi * (0.020**2) * 0.25)
    Rat3fi16Xint = Area3fi16Xint / NeededAs
    Rat3fi16Xint[Rat3fi16Xint < 1] = 1000
    Rat3fi16Xint[Dist3fi16Xint < dmin] = 1000
    Rat3fi20Xint = Area3fi20Xint / NeededAs
    Rat3fi20Xint[Rat3fi20Xint < 1] = 1000
    Rat3fi20Xint[Dist3fi20Xint < dmin] = 1000
    Rat3fi25Xint = Area3fi25Xint / NeededAs
    Rat3fi25Xint[Rat3fi25Xint < 1] = 1000
    Rat3fi25Xint[Dist3fi25Xint < dmin] = 1000

    # solution with lower 4fi(16 ou 20 ou 25 + interior bars with lower diameter
    # ...........................................................................
    n4fi16Xint = np.maximum(np.ceil((NeededAs - (4 * np.pi * (0.016**2) * 0.25)) / (np.pi * (0.012**2) * 0.25)), 3)
    n4fi20Xint = np.maximum(np.ceil((NeededAs - (4 * np.pi * (0.020**2) * 0.25)) / (np.pi * (0.016**2) * 0.25)), 3)
    n4fi25Xint = np.maximum(np.ceil((NeededAs - (4 * np.pi * (0.025**2) * 0.25)) / (np.pi * (0.020**2) * 0.25)), 3)
    Dist4fi16Xint = (Bbeams - (4 * 0.016 + n4fi16Xint * 0.012 + 2 * 0.03 + 2 * 0.006)) / (n4fi16Xint + 4 - 1)
    Dist4fi20Xint = (Bbeams - (4 * 0.020 + n4fi20Xint * 0.016 + 2 * 0.03 + 2 * 0.006)) / (n4fi20Xint + 4 - 1)
    Dist4fi25Xint = (Bbeams - (4 * 0.025 + n4fi25Xint * 0.020 + 2 * 0.03 + 2 * 0.006)) / (n4fi25Xint + 4 - 1)
    Dist4fi16Xint = np.round(Dist4fi16Xint, 8)
    Dist4fi20Xint = np.round(Dist4fi20Xint, 8)
    Dist4fi25Xint = np.round(Dist4fi25Xint, 8)

    for ii in range(len(n4fi16Xint)):
        while Dist4fi16Xint[ii] > dmax:
            n4fi16Xint[ii] = n4fi16Xint[ii] + 1
            Dist4fi16Xint[ii] = (Bbeams[ii] - (4 * 0.016 + n4fi16Xint[ii] * 0.012 + 2 * 0.03 + 2 * 0.006)) / (n4fi16Xint[ii] + 4 - 1)
            Dist4fi16Xint = np.round(Dist4fi16Xint, 8)

        while Dist4fi20Xint[ii] > dmax:
            n4fi20Xint[ii] = n4fi20Xint[ii] + 1
            Dist4fi20Xint[ii] = (Bbeams[ii] - (4 * 0.020 + n4fi20Xint[ii] * 0.016 + 2 * 0.03 + 2 * 0.006)) / (n4fi20Xint[ii] + 4 - 1)
            Dist4fi20Xint = np.round(Dist4fi20Xint, 8)

        while Dist4fi25Xint[ii] > dmax:
            n4fi25Xint[ii] = n4fi25Xint[ii] + 1
            Dist4fi25Xint[ii] = (Bbeams[ii] - (4 * 0.025 + n4fi25Xint[ii] * 0.020 + 2 * 0.03 + 2 * 0.006)) / (n4fi25Xint[ii] + 4 - 1)
            Dist4fi25Xint = np.round(Dist4fi25Xint, 8)

    Area4fi16Xint = 4 * (np.pi * (0.016**2) * 0.25) + n4fi16Xint * (np.pi * (0.012**2) * 0.25)
    Area4fi20Xint = 4 * (np.pi * (0.020**2) * 0.25) + n4fi20Xint * (np.pi * (0.016**2) * 0.25)
    Area4fi25Xint = 4 * (np.pi * (0.025**2) * 0.25) + n4fi25Xint * (np.pi * (0.020**2) * 0.25)
    Rat4fi16Xint = Area4fi16Xint / NeededAs
    Rat4fi16Xint[Rat4fi16Xint < 1] = 1000
    Rat4fi16Xint[Dist4fi16Xint < dmin] = 1000
    Rat4fi20Xint = Area4fi20Xint / NeededAs
    Rat4fi20Xint[Rat4fi20Xint < 1] = 1000
    Rat4fi20Xint[Dist4fi20Xint < dmin] = 1000
    Rat4fi25Xint = Area4fi25Xint / NeededAs
    Rat4fi25Xint[Rat4fi25Xint < 1] = 1000
    Rat4fi25Xint[Dist4fi25Xint < dmin] = 1000

    # Candidate solutions
    # ...........................................................................
    sol1 = nfi12.copy()
    sol2 = np.vstack((nfi16, n2fi16Xint, n3fi16Xint, n4fi16Xint))
    sol3 = np.vstack((nfi20, n2fi20Xint, n3fi20Xint, n4fi20Xint))
    sol4 = np.vstack((nfi25, n2fi25Xint, n3fi25Xint, n4fi25Xint))
    Rat_sol1 = Rat12.copy()
    Rat_sol2 = np.vstack((Rat16, Rat2fi16Xint, Rat3fi16Xint, Rat4fi16Xint))
    Rat_sol3 = np.vstack((Rat20, Rat2fi20Xint, Rat3fi20Xint, Rat4fi20Xint))
    Rat_sol4 = np.vstack((Rat25, Rat2fi25Xint, Rat3fi25Xint, Rat4fi25Xint))

    # Final solutions for the top reinforcement
    # ...........................................................................
    b12 = np.ones(len(Rat_sol1))
    cvalor12 = Rat_sol1.copy()
    nint12  = sol1.copy()
    b16 = np.argmin(Rat_sol2,axis=0)
    cvalor16 = np.zeros(len(b16))
    nint16 = np.zeros(len(b16))
    indexcol16 = np.zeros(len(b16))
    for i in range(len(b16)):
        cvalor16[i] = Rat_sol2[b16[i], i]
        nint16[i] = sol2[b16[i], i]
        indexcol16[i] = b16[i] + 1

    b20 = np.argmin(Rat_sol3,axis=0)
    cvalor20 = np.zeros(len(b20))
    nint20 = np.zeros(len(b20))
    indexcol20 = np.zeros(len(b20))
    for i in range(len(b20)):
        cvalor20[i] = Rat_sol3[b20[i], i]
        nint20[i] = sol3[b20[i], i]
        indexcol20[i] = b20[i] + 1

    b25 = np.argmin(Rat_sol4,axis=0)
    cvalor25 = np.zeros(len(b25))
    nint25 = np.zeros(len(b25))
    indexcol25 = np.zeros(len(b25))
    for i in range(len(b25)):
        cvalor25[i] = Rat_sol4[b25[i], i]
        nint25[i] = sol4[b25[i], i]
        indexcol25[i] = b25[i] + 1

    classif = np.array([np.sum(cvalor12), np.sum(cvalor16), np.sum(cvalor20), np.sum(cvalor25)])
    d = np.argmin(classif)
    if d == 0:
        ficornerTOP = 0.012 * np.ones(len(b12))
        ncornerTOP = 2 * np.ones(len(b12))
        ncornerTOP[ncornerTOP < 2] = 2
        fiintTOP = 0.012 * np.ones(len(b12))
        nintTOP = nint12 - 2
    elif d == 1:
        ficornerTOP = 0.016 * np.ones(len(b16))
        ncornerTOP = indexcol16.copy()
        ncornerTOP[ncornerTOP < 2] = 2
        fiintTOP = 0.012 * np.ones(len(b16))
        nintTOP = nint16 - ncornerTOP
        nintTOP[nintTOP < 1] = 0
    elif d == 2:
        ficornerTOP = 0.020 * np.ones(len(b20))
        ncornerTOP = indexcol20.copy()
        ncornerTOP[ncornerTOP < 2] = 2
        fiintTOP = 0.016 * np.ones(len(b20))
        nintTOP = nint20 - ncornerTOP
        nintTOP[nintTOP < 1] = 0
    else:
        ficornerTOP = 0.025 * np.ones(len(b25))
        ncornerTOP = indexcol25.copy()
        ncornerTOP[ncornerTOP < 2] = 2
        fiintTOP = 0.020 * np.ones(len(b25))
        nintTOP = nint25 - ncornerTOP
        nintTOP[nintTOP < 1] = 0
    # ...........................................................................
    # Now that we have defined the Final solutions for the top reinforcement, we have to define the solution for the
    # bottom reinforcement. Rules of practice dictate that no more than 2
    # diferent diameters should be used in a single beam alignement. This was
    # considered herein by enforcing the bottom reinforcement to be either the
    # same as that of the top reinf or, in the case where a single diameter is
    # used, by also allowing the use of the imediate lower diameter
    # ...........................................................................
    NeededAs = NeededAsBOT.copy()
    NeededAs[NeededAs < 1.1310e-04] = 1.1310e-04
    if d == 0:
        nfi12 = np.maximum(np.ceil(NeededAs / (np.pi * (0.012**2) * 0.25)), 2)
        ficornerBOT = 0.012 * np.ones(len(b12))
        ncornerBOT = 2 * np.ones(len(b12))
        fiintBOT = 0.012 * np.ones(len(b12))
        nintBOT = nfi12 - 2
        nintBOT[nintTOP < 1] = 0

    elif d == 1:
        nfi16 = np.maximum(np.ceil(NeededAs / (np.pi * (0.016**2) * 0.25)), 2)
        Distfi16X = (Bbeams - (nfi16*0.016 + 2*0.03 + 2*0.006)) / (nfi16 - 1)
        Distfi16X = np.round(Distfi16X, 8)
        Area16 = nfi16 * (np.pi * (0.016**2) * 0.25)
        Rat16 = Area16 / NeededAs
        Rat16[Rat16 < 1] = 100
        Rat16[Distfi16X < dmin] = 100
        n2fi16Xint = np.maximum(np.ceil((NeededAs - (2*np.pi * (0.016**2) * 0.25)) / (np.pi * (0.012**2) * 0.25)), 1)
        Dist2fi16Xint = (Bbeams - (2 * 0.016 + n2fi16Xint*0.012 + 2*0.03 + 2*0.006)) / (n2fi16Xint + 2 - 1)
        Dist2fi16Xint = np.round(Dist2fi16Xint, 8)
        Area2fi16Xint = 2 * (np.pi * (0.016**2) * 0.25) + n2fi16Xint * (np.pi * (0.012**2) * 0.25)
        Rat2fi16Xint = Area2fi16Xint / NeededAs
        Rat2fi16Xint[Rat2fi16Xint < 1] = 100
        Rat2fi16Xint[Dist2fi16Xint < dmin] = 100
        n3fi16Xint = np.maximum(np.ceil((NeededAs - (3 * np.pi * (0.016**2) * 0.25)) / (np.pi * (0.012**2) * 0.25)), 2)
        Dist3fi16Xint = (Bbeams - (3*0.016 + n3fi16Xint*0.012 + 2*0.03 + 2*0.006)) / (n3fi16Xint + 3 - 1)
        Dist3fi16Xint = np.round(Dist3fi16Xint, 8)
        Area3fi16Xint = 3 * (np.pi * (0.016**2) * 0.25) + n3fi16Xint * (np.pi * (0.012**2) * 0.25)
        Rat3fi16Xint = Area3fi16Xint / NeededAs
        Rat3fi16Xint[Rat3fi16Xint < 1] = 100
        Rat3fi16Xint[Dist3fi16Xint < dmin] = 100
        n4fi16Xint = np.maximum(np.ceil((NeededAs - (4 * np.pi * (0.016**2) * 0.25)) / (np.pi * (0.012**2) * 0.25)), 3)
        Dist4fi16Xint = (Bbeams - (4*0.016 + n4fi16Xint*0.012 + 2*0.03 + 2*0.006)) / (n4fi16Xint + 4 - 1)
        Dist4fi16Xint = np.round(Dist4fi16Xint, 8)
        Area4fi16Xint = 4 * (np.pi * (0.016**2) * 0.25) + n4fi16Xint * (np.pi * (0.012**2) * 0.25)
        Rat4fi16Xint = Area4fi16Xint / NeededAs
        Rat4fi16Xint[Rat4fi16Xint < 1] = 100
        Rat4fi16Xint[Dist4fi16Xint < dmin] = 100
        sol2 = np.vstack((nfi16, n2fi16Xint, n3fi16Xint, n4fi16Xint))
        Rat_sol2 = np.vstack((Rat16, Rat2fi16Xint, Rat3fi16Xint, Rat4fi16Xint))
        b16 = np.argmin(Rat_sol2,axis=0)
        cvalor16 = np.zeros(len(b16))
        nint16 = np.zeros(len(b16))
        indexcol16 = np.zeros(len(b16))
        for i in range(len(b16)):
            cvalor16[i] = Rat_sol2[b16[i], i]
            nint16[i] = sol2[b16[i], i]
            indexcol16[i] = b16[i] + 1

        ficornerBOT = 0.016 * np.ones(len(b16))
        ncornerBOT = indexcol16.copy()
        ncornerBOT[ncornerBOT < 2] = 2
        fiintBOT = 0.012 * np.ones(len(b16))
        nintBOT = nint16 - ncornerBOT
        nintBOT[nintBOT < 1] = 0
    
    elif d == 2:
        nfi20 = np.maximum(np.ceil(NeededAs / (np.pi * (0.020**2) * 0.25)), 2)
        Distfi20X = (Bbeams - (nfi20*0.020 + 2*0.03 + 2*0.006)) / (nfi20 - 1)
        Distfi20X = np.round(Distfi20X, 8)
        Area20 = nfi20 * (np.pi * (0.020**2) * 0.25)
        Rat20 = Area20 / NeededAs
        Rat20[Rat20 < 1] = 100
        Rat20[Distfi20X < dmin] = 100
        n2fi20Xint = np.maximum(np.ceil((NeededAs - (2 * np.pi * (0.020**2) * 0.25)) / (np.pi * (0.016**2) * 0.25)), 1)
        Dist2fi20Xint = (Bbeams - (2*0.020 + n2fi20Xint*0.016 + 2*0.03 + 2*0.006)) / (n2fi20Xint + 2 - 1)
        Dist2fi20Xint = np.round(Dist2fi20Xint, 8)
        Area2fi20Xint = 2 * (np.pi * (0.020**2) * 0.25) + n2fi20Xint * (np.pi * (0.016**2) * 0.25)
        Rat2fi20Xint = Area2fi20Xint / NeededAs
        Rat2fi20Xint[Rat2fi20Xint < 1] = 100
        Rat2fi20Xint[Dist2fi20Xint < dmin] = 100
        n3fi20Xint = np.maximum(np.ceil((NeededAs - (3 * np.pi * (0.020**2) * 0.25)) / (np.pi * (0.016**2) * 0.25)), 2)
        Dist3fi20Xint = (Bbeams - (3*0.020 + n3fi20Xint*0.016 + 2*0.03 + 2*0.006)) / (n3fi20Xint + 3 - 1)
        Dist3fi20Xint = np.round(Dist3fi20Xint, 8)
        Area3fi20Xint = 3 * (np.pi * (0.020**2) * 0.25) + n3fi20Xint * (np.pi * (0.016**2) * 0.25)
        Rat3fi20Xint = Area3fi20Xint / NeededAs
        Rat3fi20Xint[Rat3fi20Xint < 1] = 100
        Rat3fi20Xint[Dist3fi20Xint < dmin] = 100
        n4fi20Xint = np.maximum(np.ceil((NeededAs - (4 * np.pi * (0.020**2) * 0.25)) / (np.pi * (0.016**2) * 0.25)), 3)
        Dist4fi20Xint = (Bbeams - (4*0.020 + n4fi20Xint*0.016 + 2*0.03 + 2*0.006)) / (n4fi20Xint + 4 - 1)
        Dist4fi20Xint = np.round(Dist4fi20Xint, 8)
        Area4fi20Xint = 4 * (np.pi * (0.020**2) * 0.25) + n4fi20Xint * (np.pi * (0.016**2) * 0.25)
        Rat4fi20Xint = Area4fi20Xint / NeededAs
        Rat4fi20Xint[Rat4fi20Xint < 1] = 100
        Rat4fi20Xint[Dist4fi20Xint < dmin] = 100
        sol3 = np.vstack((nfi20, n2fi20Xint, n3fi20Xint, n4fi20Xint))
        Rat_sol3 = np.vstack((Rat20, Rat2fi20Xint, Rat3fi20Xint, Rat4fi20Xint))
        b20 = np.argmin(Rat_sol3,axis=0)
        cvalor20 = np.zeros(len(b20))
        nint20 = np.zeros(len(b20))
        indexcol20 = np.zeros(len(b20))
        for i in range(len(b20)):
            cvalor20[i] = Rat_sol3[b20[i], i]
            nint20[i] = sol3[b20[i], i]
            indexcol20[i] = b20[i] + 1
        ficornerBOT = 0.020 * np.ones(len(b20))
        ncornerBOT = indexcol20.copy()
        ncornerBOT[ncornerBOT < 2] = 2
        fiintBOT = 0.016 * np.ones(len(b20))
        nintBOT = nint20 - ncornerBOT
        nintBOT[nintBOT < 1] = 0

    elif d == 3:
        nfi25 = np.maximum(np.ceil(NeededAs / (np.pi * (0.025**2) * 0.25)), 2)
        Distfi25X = (Bbeams - nfi25*0.025 - 2*0.03 - 2*0.006) / (nfi25 - 1)
        Distfi25X = np.round(Distfi25X, 8)
        Area25 = nfi25 * (np.pi * (0.025**2) * 0.25)
        Rat25 = Area25 / NeededAs
        Rat25[Rat25<1] = 100
        Rat25[Distfi25X<dmin] = 100
        n2fi25Xint = np.maximum(np.ceil((NeededAs - (2 * np.pi * (0.025**2) * 0.25)) / (np.pi * (0.020**2) * 0.25)), 1)
        Dist2fi25Xint = (Bbeams - (2*0.025 + n2fi25Xint*0.020 + 2*0.03 + 2*0.006)) / (n2fi25Xint + 2 - 1)
        Dist2fi25Xint = np.round(Dist2fi25Xint, 8)
        Area2fi25Xint = 2 * (np.pi * (0.025**2) * 0.25) + n2fi25Xint * (np.pi * (0.020**2) * 0.25)
        Rat2fi25Xint = Area2fi25Xint / NeededAs
        Rat2fi25Xint[Rat2fi25Xint < 1] = 100
        Rat2fi25Xint[Dist2fi25Xint < dmin] = 100
        n3fi25Xint = np.maximum(np.ceil((NeededAs - (3 * np.pi * (0.025**2) * 0.25)) / (np.pi * (0.020**2) * 0.25)), 2)
        Dist3fi25Xint = (Bbeams - (3*0.025 + n3fi25Xint*0.020 + 2*0.03 + 2*0.006)) / (n3fi25Xint + 3 - 1)
        Dist3fi25Xint = np.round(Dist3fi25Xint, 8)
        Area3fi25Xint = 3 * (np.pi * (0.025**2) * 0.25) + n3fi25Xint * (np.pi * (0.020**2) * 0.25)
        Rat3fi25Xint = Area3fi25Xint / NeededAs
        Rat3fi25Xint[Rat3fi25Xint < 1] = 100
        Rat3fi25Xint[Dist3fi25Xint < dmin] = 100
        n4fi25Xint = np.maximum(np.ceil((NeededAs - (4 * np.pi * (0.025**2) * 0.25)) / (np.pi * (0.020**2) * 0.25)), 3)
        Dist4fi25Xint = (Bbeams - (4*0.025 + n4fi25Xint*0.020 + 2*0.03 + 2*0.006)) / (n4fi25Xint + 4 - 1)
        Dist4fi25Xint = np.round(Dist4fi25Xint, 8)
        Area4fi25Xint = 4 * (np.pi * (0.025**2) * 0.25) + n4fi25Xint * (np.pi * (0.020**2) * 0.25)
        Rat4fi25Xint = Area4fi25Xint / NeededAs
        Rat4fi25Xint[Rat4fi25Xint < 1] = 100
        Rat4fi25Xint[Dist4fi25Xint < dmin] = 100
        sol4 = np.vstack((nfi25, n2fi25Xint, n3fi25Xint, n4fi25Xint))
        Rat_sol4 = np.vstack((Rat25, Rat2fi25Xint, Rat3fi25Xint, Rat4fi25Xint))
        b25 = np.argmin(Rat_sol4,axis=0)
        cvalor25 = np.zeros(len(b25))
        nint25 = np.zeros(len(b25))
        indexcol25 = np.zeros(len(b25))
        for i in range(len(b25)):
            cvalor25[i] = Rat_sol4[b25[i], i]
            nint25[i] = sol4[b25[i], i]
            indexcol25[i] = b25[i] + 1
        ficornerBOT = 0.025 * np.ones(len(b25))
        ncornerBOT = indexcol25.copy()
        ncornerBOT[ncornerBOT < 2] = 2
        fiintBOT = 0.020 * np.ones(len(b25))
        nintBOT = nint25 - ncornerBOT
        nintBOT[nintBOT < 1] = 0

    # ...........................................................................
    # 2) Transverse Steel
    # ...........................................................................
    nwparallel_B = np.zeros(len(Asw_sw))
    nwparallel_H = np.zeros(len(Asw_sw))
    sw = np.zeros(len(Asw_sw))
    fiw1 = np.zeros(len(Asw_sw))
    sw1 = np.zeros(len(Asw_sw))
    nwparallel_B1 = np.zeros(len(Asw_sw))
    nwparallel_H1 = np.zeros(len(Asw_sw))
    for j in range(len(Asw_sw)):
        Dinf_per_bar = 10
        nwparallel_Hc = 1
        while Dinf_per_bar > 0.15:
            nwparallel_Hc = nwparallel_Hc + 1
            Dinf_per_bar = 0.90 * Bbeams[j] / nwparallel_Hc

        nwparallel_B[j] = 2
        nwparallel_H[j] = nwparallel_Hc + 0
        if ficornerTOP[j] > 0.020:
            fiwminc = 0.008
        else:
            fiwminc = 0.006

        Aswsol = 0
        nitera  = 0
        while Aswsol == 0 and nitera <= 5:
            nitera = nitera + 1
            swminim = min(sw_max[j], 24*fiwminc, sw_min_over_fi*ficornerTOP[j])
            AswX = 0.25 * np.pi * nwparallel_H[j] * fiwminc**2
            swc = min(AswX / Asw_sw[j], swminim)
            if swc > 0.25:
                sw[j] = 0.25
                Aswsol = AswX / sw[j]
            elif swc > 0.20:
                sw[j] = 0.20
                Aswsol = AswX / sw[j]
            elif swc > 0.15:
                sw[j] = 0.15
                Aswsol = AswX / sw[j]
            elif swc > 0.12:
                sw[j] = 0.125
                Aswsol = AswX / sw[j]
            elif swc > 0.10:
                sw[j] = 0.10
                Aswsol = AswX / sw[j]
            elif swc > 0.075:
                sw[j] = 0.075
                Aswsol = AswX / sw[j]
            elif swc > 0.05:
                sw[j] = 0.05  
                Aswsol = AswX / sw[j]
            elif np.all(nwparallel_H[j] <= 2 + nintTOP):
                nwparallel_H[j] = nwparallel_H[j] + 2
                Aswsol = 0
            else:
                fiwminc = fiwminc + 0.002
                Aswsol = 0

            if nitera == 5:
                fiwminc = 0.006
                sw[j] = 0.05
                nwparallel_H[j] = 4

        # TODO: seems unnecessary
        fiw1[j] = fiwminc + 0
        sw1[j] = sw[j] + 0
        nwparallel_B1[j] = nwparallel_B[j] + 0
        nwparallel_H1[j] = nwparallel_H[j] + 0

    return ficornerTOP, ncornerTOP, fiintTOP, nintTOP, ficornerBOT, ncornerBOT, fiintBOT, nintBOT, fiw1, sw1, nwparallel_B1, nwparallel_H1

def _get_rosh_guerrin(niu, muX, muY, sigmacEQ, sigmasEQ):
    """
    Uses the abacus presented in the book traité de beton arme by A Guerrin,
    Dunod, Paris, 1966. pp 146

    Args:
        niu (_type_): _description_
        muX (_type_): _description_
        muY (_type_): _description_
        sigmacEQ (_type_): _description_
        sigmaEQ (_type_): _description_
    """
    n = 15
    if niu < 0.00: # for tensile force
        roshXM = cdl_column_rho_interpolator((muX, 0.001))
        roshYM = cdl_column_rho_interpolator((muY, 0.001))
        # TODO: uniform distribution mean in X and in Y?
        roshX = roshXM - 0.50 * n * niu * sigmacEQ / sigmasEQ # 0.50 bcs it will be uniformally distributed over the cross-section 
        roshY = roshYM - 0.50 * n * niu * sigmacEQ / sigmasEQ
    else:
        roshX = cdl_column_rho_interpolator((muX, niu))
        roshY = cdl_column_rho_interpolator((muY, niu))  

    return roshX, roshY