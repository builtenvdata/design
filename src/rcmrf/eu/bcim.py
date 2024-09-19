"""
Building Class Information Model (BCIM)
"""

import numpy as np

from scipy.stats import norm, uniform, randint
from src.utils import log_normal_truncated_ab_sample, log_normal_truncated_ab_cdf_inv, get_time_based_seed, multivariate_normal_sample

AVAILABLE_BUILDING_LAYOUTS = ['B01', 'B02', 'B03', 'B04', 'B04b', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10']

class BuildingClassInformationModel:
    """
    Centered on mutually exclusive, collectively exhaustive building classes that can be mapped
    Enumerates the attributes of the building taxonomy that are collapsed into the building class
    Uses probability distributions for basic input parameters + 10 building layouts
    Uses engineering judgement + rules-of-thumb to introduce practice-based aspects
    Makes simple assumptions for unknown parameters such as construction quality
    """

    def __init__(self):
        """
        Declares the attributes of BCIM class

        Yields:
            _type_: _description_
        """
        self.Bcolfix = None # (numpy.ndarray): fixed width of columns used in initial design
        self.Bbeamfix_X = None # (numpy.ndarray): fixed width of beams in X direction used in initial design
        self.Bbeamfix_Y = None # (numpy.ndarray): fixed width of beams in Y direction used in initial design 
        self.Hstairs = None # (numpy.ndarray): thickness of slab for the staircase
        self.ppinfill = None # (numpy.ndarray): load corresponding to the infill weight
        self.DesignClass = None # (numpy.ndarray): design class 
        self.astair = None # (numpy.ndarray): span length of the stair bay (see layout)
        self.ax = None # (numpy.ndarray): span length in x direction (see layout)
        self.ay = None # (numpy.ndarray): span length in y direction (see layout)
        self.Layout = None # (numpy.ndarray): type of plan layout
        self.LX = None # (numpy.ndarray): total length of the building in the X direction
        self.LY = None # (numpy.ndarray): total length of the building in the Y direction
        self.L_over_S = None # (numpy.ndarray): ratio of Lx over Ly
        self.Area = None # (numpy.ndarray): total floor area of the building 
        self.Hupper = None # (numpy.ndarray): height of the typical floor 
        self.Hground = None # (numpy.ndarray): height of the ground floor 
        self.Hslab = None # (numpy.ndarray): slab thickness 
        self.ppslab = None # (numpy.ndarray): slab self weight (kN/m2)
        self.slabtype = None # (numpy.ndarray): slab type: 1 two-way solid slab; 2 one way solid slab; 3 ligthweigth slab with ceramic blocks and RC joists or pre-stressed beams
        self.slaborient = None # (numpy.ndarray): load orientation: 1 one way in x; 2 one way in y; 3 two-way slab
        self.beamtype = None # (numpy.ndarray): type of beam: 1 low-depth (hidden) beam; 2 emergent beam 
        self.Columnorient = None # (numpy.ndarray): column cross section shape: 1 square; 2 rectangular
        self.fsyk = None # (numpy.ndarray): characteristic value of steel yield strength
        self.fsyd = None # (numpy.ndarray): design value of steel yield strength
        self.fsyd_EQ = None # (numpy.ndarray): design value of steel yield strength considered for seismic design
        self.fck = None # (numpy.ndarray): characteristic value of the concrete compressive strength (cylinder)
        self.fckcube = None # (numpy.ndarray): characteristic value of the concrete compressive strength (cube)
        self.fcd = None # (numpy.ndarray): design value of concrete compressive strength
        self.fcd_EQ = None # (numpy.ndarray): design value of the concrete compressive strength considered for seismic design
        self.quality = None # (numpy.ndarray): quality indicator (1: high quality; 2: moderate quality;  3: low quality) 

    def generate_new(self, parameters:dict, seed:int=1987):
        """
        Generates new taxonomy and saves the all relevant attributes in the BCIM class

        Args:
            parameters (dict): parameters defined by user to generate a new building taxonomy
        """

        # set the random number generator seed
        if seed: 
            np.random.seed(seed) # user defined
        else:
            np.random.seed(get_time_based_seed()) # based on the date and time

        self.Bcolfix      = np.ones(parameters['Nsimul']) * parameters['Bcolfix']
        self.Bbeamfix_X   = np.ones(parameters['Nsimul']) * parameters['Bbeamfix_X']
        self.Bbeamfix_Y   = np.ones(parameters['Nsimul']) * parameters['Bbeamfix_Y']
        self.Hstairs      = np.ones(parameters['Nsimul']) * parameters['Hstairs']
        self.ppinfill     = np.ones(parameters['Nsimul']) * parameters['ppinfill']
        self.DesignClass  = np.array([parameters['DesignClass']] * parameters['Nsimul'], dtype=object)
        self.Beta         = np.ones(parameters['Nsimul']) * parameters['Beta']
        self.NStoreys     = (np.ones(parameters['Nsimul']) * parameters['NStoreys']).astype(np.int32)
        self._box1(parameters['Nsimul'], parameters['DesignClass'])
        self._box2(parameters['PSS1'], parameters['PSS2'])
        self._box3(parameters['PWBa'])
        self._box4(parameters['Nsimul'], parameters['Psquared'])
        self._box5(parameters['Nsimul'], parameters['PQHigh'], parameters['PQModer'], parameters['DesignClass'])

    def adapt_for_test(self, test_taxonomy:dict):
        """
        Adapts the test dictionary to the BCIM class

        Args:
            test_taxonomy (dict): test dictionary contains BCIM outputs used to test BIM module
        """

        for attribute, value in test_taxonomy.items():
            if attribute in ['DesignClass', 'Layout']:
                value = np.array(value, dtype=object)
            elif attribute == 'NStoreys':
                value = np.array(value, dtype=np.int32)
            else:
                value = np.array(value)
            setattr(self, attribute, value)


    def _box1(self, Nsimul, DesignClass):
        """
        Random value generator
        Updates the attributes: astair, ax, ay, layout, Lx, Ly, L_over_S, area, Hupper, Hground

        Notes:
            * In SciPy or NumPy there is no method for getting inverse of many non-standard cdf (i.e. truncated log-normal distribution). So, I am using the user-define methods in utils.py

            * Stair span length
            - It was assumed that the stair span could be represented by a uniform distribution with minimum length 2.8 and maximum span length of 3.2.

            * Beam span length related (Number of storeys > 2)
            - Silva et al. (2012) analysed the Portuguese RC MRF building stock and observed that the beam span length was on average 4.37m with a CoV of 0.11, following a log-normal distribution.
            - Furtado et al. (2016) investigated 78 RC buildings (484 beams) following a normal distribution with mean 4.42m and a CoV of 0.22.
            - Eroglu et al. (2014) defined statistical parameters for the beam span length with average 3.55m and CoV of 0.19.
            - For the short direction, the analysis of continuous frames indicated that the mean(CoV) was 3.51m (0.21) for the average span length, 2.37m (0.32) for the minimum length and 4.41m (0.24) for the maximum length.
            - With respect to the longer direction, continuous frames analysed had average span lengths of 3.59m (0.17), with minimum bay length of 2.38m (0.28) and maximum length of 4.80m (0.22).
            - Del Gaudio et al. (2015) analysed the RC building stock in the city of Avellino, Italy, and found the bay length distribution to be on average 4.42m with a CoV of 0.18.
            - Average model selected: ax ~ LN(4.10,0.25)  <----> I think this is an old assumption

            * Storey height related (Number of storeys > 2)
            - Furtado et al. (2016) estimated the ground storey height with mean 3.09m and a CoV of 0.08, using a normal distribution. For the upper storeys, the mean is 2.77m and the CoV 0.05.
            - Silva et al. (2012) proposed a log-normal model with mean 3.21 and a CoV of 0.13 to represent the ground storey height, and a normal distribution with mean 2.88 and a CoV of 0.07 for the upper storeys.
            - Del Gaudio et al. (2015) estimated the ground storey height with mean 3.58 with a CoV of 0.17, and the upper storey to be distributed according to a mean value of 3.21 and a CoV of 0.07.
            - Bal et al. (2008) referred that the regular storey height could be represented by a log-normal model with mean 2.84m and a CoV of 0.08. The ground story has a height of 3.23m with a CoV of 0.15.
            - Akkar et al. (2014) identified a mean ground storey height of 3.01 (0.13) while the upper storeys have a mean storey height of 2.71 with a CoV of 0.07.
            - Similar results have been reported by Ozmen et al. (2015).
            - Average model selected for ground storey: hground ~ LN(3.20,0.15) <----> I think this is an old assumption
            - Average model selected for upper storeys: upper ~ LN(2.90,0.07)

            * TODO: Instead of Monte Carlo Simulation, Latin Hypercube Sampling could be an option: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.LatinHypercube.html

        """

        # 1) Generate a random dimension for the stair span length.
        a_uniform = 2.8
        b_uniform = 3.2
        # self.astair = 0.05 * np.round(20 * np.random.uniform(low=a_uniform, high=b_uniform, size=Nsimul))
        self.astair = 0.05 * np.round(20 * uniform.ppf(np.random.rand(Nsimul), loc=a_uniform, scale=b_uniform-a_uniform) + 1e-12) # For compatibility with MATLAB

        # 2) Generate random values for span lengths in x and y directions (see layout)
        rho = -0.92  # correlation coefficient
        mu = np.array([0, 0])  # mean of the multivariate normal, multi-normal or Gaussian distribution
        cov = np.array([[1, rho], [rho, 1]])  # covariance matrix
        # Truncated log-normal distribution parameters of the span length in x direction
        a1 = 3.5  # lower bound for truncated log-normal distribution
        b1 = 7.5  # upper bound for truncated log-normal distribution
        mu1 = np.log(4.5)  # logarithmic mean of log-normal distribution
        sigma1 = 0.350  # logarithmic standard deviation of log-normal distribution
        # Truncated log-normal distribution parameters of the span length in y direction
        if DesignClass == 'CDN' or DesignClass == 'CDL':
            a2 = 3.5  # lower bound for truncated log-normal distribution
            b2 = 6.0  # upper bound for truncated log-normal distribution
        else:
            a2 = 3.5  # lower bound for truncated log-normal distribution
            b2 = 7.5  # upper bound for truncated log-normal distribution
        mu2 = np.log(4.5)  # logarithmic mean of log-normal distribution
        sigma2 = 0.350  # logarithmic standard deviation of log-normal distribution
        # Realisations
        # Z = np.random.multivariate_normal(mu, cov, size=Nsimul)
        Z = multivariate_normal_sample(mu, cov, Nsimul) # Let's use the function defined in utils to be compatible with MATLAB
        U = norm.cdf(Z, loc=0.0, scale=1.0)
        r1 = log_normal_truncated_ab_cdf_inv(U[:,0], mu=mu1, sigma=sigma1, a=a1, b=b1)
        r2 = log_normal_truncated_ab_cdf_inv(U[:,1], mu=mu2, sigma=sigma2, a=a2, b=b2)
        self.ax = 0.05 * np.round(20 * r1 + 1e-12)
        self.ay = 0.05 * np.round(20 * r2 + 1e-12)
        # layout_id = np.random.randint(low=0, high=len(available_layouts), size=Nsimul, dtype=int)  # building layout ids
        layout_id = randint.ppf(np.random.rand(Nsimul), low=0, high=len(AVAILABLE_BUILDING_LAYOUTS)).astype(int)  # For compatibility with MATLAB
        self.Layout = np.array([AVAILABLE_BUILDING_LAYOUTS[i] for i in layout_id], dtype=object)
        removed_area = np.zeros(Nsimul)  # Area to be removed in case of an irregular buildings
        Lx = np.zeros((Nsimul, 22))  # total length of the building in the X direction
        Ly = np.zeros((Nsimul, 22))  # total length of the building in the Y direction
        factors_ax = [2, 4, 6, 2, 2, 4, 6, 2, 2, 2, 2, 6, 4, 2, 2, 2, 2, 4, 2, 4, 4.4, 4.2]
        factors_astair = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
        factors_ay = [2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 3, 2, 3, 4, 5, 6, 4, 3, 3, 4, 4]
        add_to_Ly = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.5, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(Lx.shape[1]):
            Lx[:, i] = factors_ax[i] * self.ax + factors_astair[i] * self.astair
            Ly[:, i] = factors_ay[i] * self.ay + add_to_Ly[i]
        
        # Final total length of the building in the X direction
        self.LX = np.array([Lx[i, layout_id[i] + 1] if Lx[i, layout_id[i]] < 8 else Lx[i, layout_id[i]] for i in range(Nsimul)])
        # Final total length of the building in the X direction
        self.LY = np.array([Ly[i, layout_id[i] + 1] if Lx[i, layout_id[i]] > 8 > Ly[i, layout_id[i]] else Ly[i, layout_id[i]] for i in range(Nsimul)])
        
        removed_area_Final = removed_area.copy()
        tmp = np.concatenate((self.LX.reshape(-1, 1), self.LY.reshape(-1, 1)), axis=1)
        self.L_over_S = np.max(tmp, axis=1) / np.min(tmp, axis=1)
        self.Area = self.LX * self.LY - removed_area_Final

        # 3) Generate a random values for the ground storey height
        sigma_Hupper = (np.log(1 + 0.07 ** 2)) ** 0.5
        mu_Hupper = np.log(2.90) - 0.5 * sigma_Hupper ** 2
        a_Hupper, b_Hupper = 2.30, 3.8
        # Realisations
        self.Hupper = log_normal_truncated_ab_sample(Nsimul, mu_Hupper, sigma_Hupper, a_Hupper, b_Hupper)
        self.Hupper = 0.05 * np.round(20 * self.Hupper + 1e-12)
        self.Hground = np.zeros(len(self.Hupper))
        aux = np.random.rand(Nsimul)
        mask1 = aux <= 0.55
        mask2 = (0.55 < aux) & (aux <= 0.65)
        mask3 = (0.65 < aux) & (aux <= 0.85)
        mask4 = (0.85 < aux) & (aux <= 0.95)
        mask5 = 0.95 < aux
        self.Hground[mask1] = np.minimum(self.Hupper[mask1], 4.20)
        self.Hground[mask2] = np.minimum(0.05 * np.round(20 * 1.1 * self.Hupper[mask2] + 1e-12), 4.20)
        self.Hground[mask3] = np.minimum(0.05 * np.round(20 * 1.2 * self.Hupper[mask3] + 1e-12), 4.20)
        self.Hground[mask4] = np.minimum(0.05 * np.round(20 * 1.3 * self.Hupper[mask4] + 1e-12), 4.20)
        self.Hground[mask5] = np.minimum(0.05 * np.round(20 * 1.4 * self.Hupper[mask5] + 1e-12), 4.20)


    def _box2(self, PSS1, PSS2):
        """
        Decision tree for selecting slab type based on ax, ay and astair
        Updates the attributes: Hslab, ppslab, slabtype, slaborient

        Notes:
            - slabtype=1 - 2D solid slab
            - slabtype=2 - 1D solid slab
            - slabtype=3 - Composite slab with ceramic blocks and RC joists or pre-stressed beams.

            - slaborient=1 - Unloading in X beams
            - slaborient=2 - Unloading in Y beams
            - slaborient=3 - Unloading in both directions

            * Solid Slab (1): L=4m: h=0.15;  L=5m: h=0.20; L=6m: h=0.20; L=7m: h=0.25
            Lightened slab (Composite) (3): L=5m: h=0.225; L=6-7m: h=0.25; L=8m: h=0.30
            the approximate curve was assumed: 
            PPRCslab=24 (old)*H (kN/m2)
            PPpre-stressed beams and ceramics (assumption the mean model according to all typologies presented in the catalogue
            http://www.presdouro.pt/12/pdf/DT_PD2016.pdf
            PPRCslab=14.05*Hslab
            Hslab=max(min(spanX,spanY)/25,0.10)

        """
        ratio = np.zeros(len(self.ax))
        self.Hslab = np.zeros(len(self.ax))
        self.ppslab = np.zeros(len(self.ax))
        self.slabtype = np.zeros(len(self.ax), dtype='int')
        self.slaborient = np.zeros(len(self.ax), dtype='int')

        for i in range(len(self.Hslab)):
            l1 = max(self.ax[i], self.ay[i])
            l2 = min(self.ax[i], self.ay[i])
            ratio[i] = l1/l2

            if self.ax[i] / self.ay[i] > 1:
                slab_orient = 1
            else:
                slab_orient = 2

            if l2 > 6.0:
                self.slabtype[i] = 3
                self.slaborient[i] = slab_orient

            else:
                if ratio[i] >= 2.0:
                    aux1 = np.random.rand()
                    if aux1 <= PSS1:
                        self.slabtype[i] = 2
                        self.slaborient[i] = slab_orient
                    else:
                        self.slabtype[i] = 3
                        self.slaborient[i] = slab_orient
                else:
                    aux2 = np.random.rand()
                    if aux2 <= PSS2:
                        self.slabtype[i] = 1
                        self.slaborient[i] = 3
                    else:
                        self.slabtype[i] = 3
                        self.slaborient[i] = slab_orient

            if self.slabtype[i] == 1:  # 2D solid slab
                self.Hslab[i] = min(round(100 * l2/30 + 1e-12)/100, 0.85) # 0.032*l2+0.032
                self.ppslab[i] = 24 * self.Hslab[i]
            elif self.slabtype[i] == 2:  # 1D solid slab, this is the same as 2D solid slab case? TODO
                self.Hslab[i] = min(round(100 * l2/30 + 1e-12)/100, 0.85) # 0.032*l2+0.032
                self.ppslab[i] = 24 * self.Hslab[i]                    
            elif self.slabtype[i] == 3:  # Composite slabs ceramic blocks and pre-stressed joists
                self.Hslab[i] = min(round(100 * (0.032 * l2 + 0.065) + 1e-12)/100, 0.85) # 0.032*l2+0.032
                self.ppslab[i] = 2.20 * np.log(self.Hslab[i]) + 6.50


    def _box3(self, PWBa):
        """
        Decision tree for selecting beam typology (EB, WB or NB) for eac aligment based on the type of slab system.
        Updates the attributes: beam_types

        Notes:
            - slabtype = 1: 2D solid slab 
            - slabtype = 2: 1D solid slab 
            - slabtype = 3: Composite slab with ceramic blocks and RC joists or pre-stressed beams.
            - slaborient = 1: Unloading in X beams
            - slaborient = 2: Unloading in Y beams
            - slaborient = 3: Unloading in both directions
            - beamtype = 1: Wide beams
            - beamtype = 2: Emergent beams
            
        """

        self.beamtype = np.zeros(len(self.slabtype), dtype = 'int')

        for i in range(len(self.slabtype)):
            aux = np.random.rand()
            if self.slabtype[i] in [1, 2]:
                self.beamtype[i] = 2
            else:
                if aux <= PWBa:
                    # There were redundant lines here in the original code. They were removed
                    self.beamtype[i] = 1
                else:
                    self.beamtype[i] = 2


    def _box4(self, Nsimul, Psquared):
        """
        Decision tree for selecting the type of column cross-section geometry.
        Updates the attributes: column_orients

        Notes:
            - 1 represents the case where square columns are adopted while
            - 2 represents the case where rectangular columns are considered.
            - the distribution of the column orientations is presented in the companion document (Which is?)

        """
        aux = np.random.rand(Nsimul)
        mask = aux > Psquared
        self.Columnorient = np.ones(Nsimul, dtype = 'int')
        self.Columnorient[mask] = 2
        

    def _box5(self, Nsimul, PQHigh, PQModer, DesignClass):
        """
        Decision tree for selecting the material design and level of construction quality
        Updates the attributes: fsyk, fsyd, fsyd_eq, fck, fck_cube, fcd_eq, quality

        """
        
        self.fsyk = np.zeros(Nsimul)
        self.fsyd = np.zeros(Nsimul)
        self.fsyd_EQ = np.zeros(Nsimul)
        self.fck = np.zeros(Nsimul)
        self.fckcube = np.zeros(Nsimul)
        self.fcd = np.zeros(Nsimul)
        self.fcd_EQ = np.zeros(Nsimul)
        self.quality = np.zeros(Nsimul, dtype = 'int')

        # aux1s = np.random.rand(Nsimul)  # Defines the material design classes for steel based on the design class adopted
        # aux2s = np.random.rand(Nsimul)  # Defines the concrete class for concrete based on the design class adopted
        # aux3s = np.random.rand(Nsimul)  # Defines the quality based on the year of construction

        for i in range(Nsimul):

            aux1 = np.random.rand()  # Defines the material design classes for steel based on the design class adopted
            aux2 = np.random.rand()  # Defines the concrete class for concrete based on the design class adopted
            aux3 = np.random.rand()  # Defines the quality based on the year of construction

            # aux1 = aux1s[i]  # Defines the material design classes for steel based on the design class adopted
            # aux2 = aux2s[i]  # Defines the concrete class for concrete based on the design class adopted
            # aux3 = aux3s[i]  # Defines the quality based on the year of construction

            if DesignClass == 'CDN':
                # STEEL MATERIAL
                if aux1 <= 0.60:
                    self.fsyk[i] = 240
                    self.fsyd[i] = 120
                    self.fsyd_EQ[i] = 240
                else:
                    self.fsyk[i] = 400
                    self.fsyd[i] = 240
                    self.fsyd_EQ[i] = 400
                # CONCRETE MATERIAL
                if aux2 <= 0.40:
                    self.fck[i] = 14.0
                    self.fckcube[i] = 16.0
                    self.fcd[i] = 6.0
                    self.fcd_EQ[i] = 14.0
                elif aux2 <= 0.80:
                    self.fck[i] = 16.0
                    self.fckcube[i] = 18.0
                    self.fcd[i] = 6.0
                    self.fcd_EQ[i] = 16.0
                else:
                    self.fck[i] = 20.0
                    self.fckcube[i] = 22.5
                    self.fcd[i] = 7.5
                    self.fcd_EQ[i] = 20.0
                # CONSTRUCTION QUALITY
                if aux3 <= PQHigh:
                    self.quality[i] = 1
                elif aux3 <= PQHigh + PQModer:
                    self.quality[i] = 2
                else:
                    self.quality[i] = 3

            elif DesignClass == 'CDL':
                # STEEL MATERIAL
                if aux1 <= 0.20:
                    self.fsyk[i] = 240
                    self.fsyd[i] = 140
                    self.fsyd_EQ[i] = 240
                elif aux1 <= 0.90:
                    self.fsyk[i] = 400
                    self.fsyd[i] = 240
                    self.fsyd_EQ[i] = 400
                else:
                    self.fsyk[i] = 500
                    self.fsyd[i] = 300
                    self.fsyd_EQ[i] = 500
                # CONCRETE MATERIAL
                if aux2 <= 0.40:
                    self.fck[i] = 14.0
                    self.fckcube[i] = 180  # Note: This is kg/cm2 because of the design formula
                    self.fcd[i] = 7.0
                    self.fcd_EQ[i] = 10.5
                elif aux2 <= 0.80:
                    self.fck[i] = 19.0
                    self.fckcube[i] = 225  # Note: This is kg/cm2 because of the design formula
                    self.fcd[i] = 8.5
                    self.fcd_EQ[i] = 12.75
                else:
                    self.fck[i] = 25.0
                    self.fckcube[i] = 300  # Note: This is kg/cm2 because of the design formula
                    self.fcd[i] = 11.5
                    self.fcd_EQ[i] = 17.5
                # CONSTRUCTION QUALITY
                if aux3 <= PQHigh:
                    self.quality[i] = 1
                elif aux3 <= PQHigh + PQModer:
                    self.quality[i] = 2
                else:
                    self.quality[i] = 3

            elif DesignClass == 'CDM':
                # STEEL MATERIAL
                if aux1 <= 0.50:
                    self.fsyk[i] = 400
                    self.fsyd[i] = 400/1.15
                    self.fsyd_EQ[i] = 400/1.15
                else:
                    self.fsyk[i] = 500
                    self.fsyd[i] = 500/1.15
                    self.fsyd_EQ[i] = 500/1.15
                # CONCRETE MATERIAL
                if aux2 <= 0.30:
                    self.fck[i] = 16.0
                    self.fckcube[i] = 20.0
                    self.fcd[i] = self.fck[i]/1.5
                    self.fcd_EQ[i] = self.fck[i]/1.5
                elif aux2 <= 0.60:
                    self.fck[i] = 20.0
                    self.fckcube[i] = 25.0
                    self.fcd[i] = self.fck[i]/1.5
                    self.fcd_EQ[i] = self.fck[i]/1.5
                else:
                    self.fck[i] = 25.0
                    self.fckcube[i] = 30.0
                    self.fcd[i] = self.fck[i]/1.5
                    self.fcd_EQ[i] = self.fck[i]/1.5
                # CONSTRUCTION QUALITY
                if aux3 <= PQHigh:
                    self.quality[i] = 1
                elif aux3 <= PQHigh + PQModer:
                    self.quality[i] = 2
                else:
                    self.quality[i] = 3

            elif DesignClass == 'CDH':
                # STEEL MATERIAL
                if aux1 <= 0.10:
                    self.fsyk[i] = 400
                    self.fsyd[i] = 400/1.15
                    self.fsyd_EQ[i] = 400/1.15
                else:
                    self.fsyk[i] = 500
                    self.fsyd[i] = 500/1.15
                    self.fsyd_EQ[i] = 500/1.15
                # CONCRETE MATERIAL
                if aux2 <= 0.30:
                    self.fck[i] = 20.0
                    self.fckcube[i] = 25.0
                    self.fcd[i] = self.fck[i]/1.5
                    self.fcd_EQ[i] = self.fck[i]/1.5
                elif aux2 <= 0.75:
                    self.fck[i] = 25.0
                    self.fckcube[i] = 30.0
                    self.fcd[i] = self.fck[i]/1.5
                    self.fcd_EQ[i] = self.fck[i]/1.5
                elif aux2 <= 0.95:
                    self.fck[i] = 30.0
                    self.fckcube[i] = 35.0
                    self.fcd[i] = self.fck[i]/1.5
                    self.fcd_EQ[i] = self.fck[i]/1.5
                else:
                    self.fck[i] = 35.0
                    self.fckcube[i] = 40.0
                    self.fcd[i] = self.fck[i]/1.5
                    self.fcd_EQ[i] = self.fck[i]/1.5
                # CONSTRUCTION QUALITY
                if aux3 <= PQHigh:
                    self.quality[i] = 1
                elif aux3 <= PQHigh + PQModer:
                    self.quality[i] = 2
                else:
                    self.quality[i] = 3

            else:
                print('You have entered an invalid input for DesignClass!')
