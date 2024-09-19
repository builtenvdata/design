from src.rcmrf.eu.bim.predesign import Predesigner
from src.utils import make_dir, signif
import openseespy.opensees as ops
import numpy as np

class ElasticModelBuilder(Predesigner):

    def _do_all_analyses(self):
        # Calculates the generic properties of each element for elastic analysis depending on slaborient
        # Update elastic analysis variables for beams and columns
        self.beamX.update_mechanical_properties()
        self.beamStair.update_mechanical_properties()
        self.beamY.update_mechanical_properties()
        self.column.update_mechanical_properties()
        
        if self.general.designlevel == 'CDH' and self.general.ag > 0.01:
            reduction_factor = 0.50 # factor to represent the cracked concrete to affect Ix and Iy of the columns for EC8 analysis pp54
        else:
            reduction_factor = 1.00

        # Perform structural analyses
        self.results = {}
        self._get_uls_forces() # Gravity analysis with ULS load combination
        self._get_eq_forces() # Gravity analysis but using the load combination associated with the earthquake case to calculate the masses
        self._get_lfa_forces(reduction_factor) # Runs elastic model using equivalent lateral force analysis

    def _do_extra_analyses(self):

        self._get_modal_properties() # Modal analysis considering the load combination associated with the seismic case
        self._get_quasi_eq_forces() # Gravity analysis but using the load combination with 1.0*permanent + 0.30*service       
        self._get_quasi_modal_properties() # Runs modal analysis with the the load combination with 1.0*permanent + 0.30*service
        self.general.MassesQuasi = np.append(np.zeros(len(self.general.noderef)), self.general.MassesQuasi.flatten()) # To make it compatible with nonlin model
        self.general.TotalMassQuasi = np.sum(self.general.MassesQuasi)
        self.general.TotalWeightQuasi = self.general.TotalMassQuasi * 9.81

    def _get_uls_forces(self):
        """
        Runs a gravity analysis using the ULS load combination.
        """
        self._create_model()
        self._add_gravity_loads(floor_load="ped", roof_load='pedroof')
        self._do_linear_static_analysis()
        self.results['ULS'] = self._get_element_forces()

    def _get_eq_forces(self):
        """
        Runs a gravity analysis but using the load combination associated with the earthquake case to calculate the masses.
        """
        self._create_model()
        self._add_gravity_loads(floor_load="pedEQ", roof_load='pedroofEQ')
        self._do_linear_static_analysis()
        self.results['EQ'] = self._get_element_forces()
        self._extract_masses(load_case='EQ')

    def _get_quasi_eq_forces(self):
        """
        Runs the the load combination with 1.0*permanent + 0.30*service associated with the seismic case and calculates the generic variables for Nonlinear analysis
        """
        if self.general.designlevel == 'CDH':
            reduction_factor = 0.50 # factor to represent the cracked concrete to affect Ix and Iy of the columns for EC8 analysis pp54
        else:
            reduction_factor = 1.00

        self._create_model(stiffness_factor=reduction_factor)
        self._add_gravity_loads(floor_load="pedEQFinal", roof_load='proofEQFinal')
        self._do_linear_static_analysis()
        self.results['EQ_Quasi'] = self._get_element_forces()
        self._extract_masses(load_case='EQ_Quasi')

    def _get_modal_properties(self):
        """
        Runs modal analysis. TODO: replace this stuff later with built-in opensees modal analysis
        """

        if self.general.designlevel == 'CDH' and self.general.ag > 0.01:
            reduction_factor = 0.50 # factor to represent the cracked concrete to affect Ix and Iy of the columns for EC8 analysis pp54
        else:
            reduction_factor = 1.00

        # self._create_model(stiffness_factor=reduction_factor, mass_flag=1, diaphragm='rigid-like')
        self._create_model(stiffness_factor=reduction_factor, mass_flag=1)
        self._add_gravity_loads(floor_load="pedEQ", roof_load='pedroofEQ')
        self._do_linear_static_analysis()
        self.results['ModalD'] = self._do_modal_analysis(self.general.Masses)

    def _get_quasi_modal_properties(self):
        """
        Runs modal analysis. TODO: replace this stuff later with built-in opensees modal analysis
        """
        if self.general.designlevel == 'CDH':
            reduction_factor = 0.50 # factor to represent the cracked concrete to affect Ix and Iy of the columns for EC8 analysis pp54
        else:
            reduction_factor = 1.00

        # self._create_model(stiffness_factor=reduction_factor, mass_flag=1, diaphragm='rigid-like')
        self._create_model(stiffness_factor=reduction_factor, mass_flag=1)
        self._add_gravity_loads(floor_load="pedEQFinal", roof_load='proofEQFinal')
        self._do_linear_static_analysis()
        self.results['Modal'] = self._do_modal_analysis(self.general.MassesQuasi)

    def _get_lfa_forces(self, reduction_factor):
        """
        Computes base shear - horizontal forces for LFA used in DUCL
        """
        nodes, forces_nodes = self._calculate_horizontal_loads_lfa()
        for loading_case in ['LFA+X', 'LFA-X', 'LFA+Y', 'LFA-Y']:
            # self._create_model(stiffness_factor=reduction_factor, mass_flag=1, diaphragm='rigid-like')
            self._create_model(stiffness_factor=reduction_factor, mass_flag=1)
            self._add_horizontal_loads_lfa(loading_case, nodes, forces_nodes)
            self._do_linear_static_analysis()
            self.results[loading_case] = self._get_element_forces()

    def _do_modal_analysis(self, Masses):
        Masses2 = Masses.flatten()
        aa = np.zeros(len(self.general.noderef))
        Masses3 = np.append(aa, Masses2)
        eigenvalues = ops.eigen(self.general.nmodes)
        # periods = 2 * np.pi / np.array(eigenvalues) ** 0.5
        periods = 2 * 3.141596 / np.array(eigenvalues) ** 0.5  # Using the same pi value in Modal.tcl for compatibility
        mX = np.ones((self.general.nmodes, len(Masses3))) * Masses3
        mY = np.ones((self.general.nmodes, len(Masses3))) * Masses3
        fiX = np.zeros((self.general.nmodes, len(self.general.Coordsref)))
        fiY = np.zeros((self.general.nmodes, len(self.general.Coordsref)))
        for i in range(self.general.nmodes):
            eigenvectors = np.array([ops.nodeEigenvector(int(nodes[0]), i+1) for nodes in self.general.Coordsref])
            fiX[i] = eigenvectors[:, 0]
            fiY[i] = eigenvectors[:, 1]
        fimiX = fiX * mX
        fimiY = fiY * mY
        fi2miX = (fiX ** 2) * mX
        fi2miY = (fiY ** 2) * mY
        G2M = fi2miX + fi2miY
        GammaX = np.sum(fimiX, axis=1)/np.sum(G2M, axis=1)
        GammaY = np.sum(fimiY, axis=1)/np.sum(G2M, axis=1)
        MMX = ((np.sum(fimiX, axis=1)) ** 2)/np.sum(G2M, axis=1)
        MMY = ((np.sum(fimiY, axis=1)) ** 2)/np.sum(G2M, axis=1)
        angle = np.arctan(GammaY/GammaX)*180/np.pi
        MassMobilizedX = np.sum(MMX)/np.sum(Masses)
        MassMobilizedY = np.sum(MMY)/np.sum(Masses)
        results = {'Periods':periods, 'mX': mX, 'mY': mY, 'fiX': fiX, 'fiY': fiY, 'fimiX': fimiX, 'fimiY': fimiY, 
                   'G2M': G2M, 'GammaX': GammaX, 'GammaY': GammaY, 'MMX': MMX, 'MMY': MMY,
                   'Inclination_angle_with_X': angle, 'MassMobilizedX': MassMobilizedX, 'MassMobilizedY': MassMobilizedY}
        return results

    def _extract_masses(self, load_case):
        """
        The masses are calculated according to the axial load levels at the top of each column, by subtracting the total N of the above floors to the axial load at the lower storey: 
        Mass=(Axial@top_of_the_storey(1:end-1)-Axial@top_of_the_storey(2:end,:))./9.81
        TODO: I think this can be changed. We can directly assign the masses as they are. OpenSees now has built-in modal analysis procedure
        """
        if 'quasi' in load_case.lower():
            self.general.NjointQuasi = np.abs(self.results[load_case]['Column']['N9'])
            self.general.Njoint2Quasi = np.append(self.general.NjointQuasi, np.zeros((1, self.general.NjointQuasi.shape[1])), axis=0)
            self.general.MassesQuasi = -np.diff(self.general.Njoint2Quasi, axis=0) / 9.81
            self.general.Masses2Quasi = self.general.MassesQuasi[:, self.column.name[0,:]<2000]
            self.general.TotalMassQuasi = np.sum(self.general.MassesQuasi, axis=1)
            self.general.TotalWeightQuasi = self.general.TotalMassQuasi * 9.81
        else:
            self.general.Njoint = np.abs(self.results[load_case]['Column']['N9'])
            self.general.Njoint2 = np.append(self.general.Njoint, np.zeros((1, self.general.Njoint.shape[1])), axis=0)
            self.general.Masses = -np.diff(self.general.Njoint2, axis=0) / 9.81
            self.general.Masses2 = self.general.Masses[:, self.column.name[0,:]<2000]
            self.general.TotalMass = np.sum(self.general.Masses, axis=1)
            self.general.TotalWeight = self.general.TotalMass * 9.81

    def _create_model(self, stiffness_factor = 1, mass_flag = 0, diaphragm = 'rigid'):
        """
        Creates an elastic centreline model of the structure and run the elastic gravity analysis
        self.general.Coordsref includes the coordinates of the nodes.
        self.column as the column properties.
        self.beamX, self.beamY and self.BeamStair include the beam properties.

        
        """
        # Round everything. This can be removed later on, done just to for checking results against MATLAB
        Ec = np.round(self.general.Ec, 6)
        G = np.round(self.general.G, 6)
        column_Area = np.round(self.column.Area, 6)
        column_IX = np.round(stiffness_factor * self.column.IX, 6)
        column_IY = np.round(stiffness_factor * self.column.IY, 6)
        column_J = np.round(self.column.J, 6)
        beamX_Area = np.round(self.beamX.Area, 6)
        beamX_IZ = np.round(stiffness_factor * self.beamX.IZ, 6)
        beamX_IY = np.round(stiffness_factor * self.beamX.IY, 6)
        beamX_J = np.round(self.beamX.J, 6)
        beamStair_Area = np.round(self.beamStair.Area, 6)
        beamStair_IZ = np.round(stiffness_factor * self.beamStair.IZ, 6)
        beamStair_IY = np.round(stiffness_factor * self.beamStair.IY, 6)
        beamStair_J = np.round(self.beamStair.J, 6)
        beamY_Area = np.round(self.beamY.Area, 6)
        beamY_IZ = np.round(stiffness_factor * self.beamY.IZ, 6)
        beamY_IY = np.round(stiffness_factor * self.beamY.IY, 6)
        beamY_J = np.round(self.beamY.J, 6)

        # Start a clean model
        ops.wipe()
        ops.wipeAnalysis()
        ops.model('basic', '-ndm', 3, '-ndf', 6)
        # We do not need this
        # nodes2topolatload = self.general.Coordsref[(self.general.Coordsref[:, 0] > 100 * self.general.nstoreys), 0]
        # nodes2topolatload = nodes2topolatload[nodes2topolatload < 1000]
        # ...........................................................................
        # Define nodes
        for node in self.general.Coordsref:
            node = node.tolist(); node[0] = int(node[0])
            ops.node(*node)
        # ...........................................................................
        # Nodal masses
        if mass_flag == 1:
            masses = self.general.Masses.flatten()
            masses = np.round(masses, 6)
            nodes2mass = self.general.Coordsref[(self.general.Coordsref[:, 0] > 100), 0]
            for i, node in enumerate(nodes2mass):
                ops.mass(int(node), masses[i], masses[i], 0.01, 0.01, 0.01, 0.01)
        # ...........................................................................
        # Single-point constraints: Fix base nodes
        nodes2fix = self.general.Coordsref[(self.general.Coordsref[:, 0] < 100), 0]
        for node in nodes2fix:
            ops.fix(int(node), 1, 1, 1, 1, 1, 1)
        # ...........................................................................
        if diaphragm == 'rigid':
            # Multi-point constraints: Rigid diaphragms --> TODO: Change the retained node to floor centre of mass
            for i in range(self.beamX.name.shape[0]):
                nodes = [int((i+1)*100 + node) for node in nodes2fix]
                ops.rigidDiaphragm(3, *nodes)
        elif diaphragm == 'rigid-like':
            ops.uniaxialMaterial('Elastic', 99901, self.general.truss_stiffness)
            for i in range(1, self.general.nstoreys): # Floor level
                for j in range(len(self.general.floor_truss_nodei_ref)): 
                    ops.element('Truss', int(f'999{100*i + (j+1)}'), 100*i + self.general.floor_truss_nodei_ref[j], 100*i + self.general.floor_truss_nodej_ref[j], 1000.0, 99901)
            i = int(self.general.nstoreys)
            for j in range(len(self.general.roof_truss_nodei_ref)): # Roof level
                ops.element('Truss', int(f'999{100*i + (j+1)}'), 100*i + self.general.roof_truss_nodei_ref[j], 100*i + self.general.roof_truss_nodej_ref[j], 1000.0, 99901)
        # ...........................................................................
        # Geometric transformations
        transfCol = 1
        transfBeamX = 2
        transfBeamY = 3
        ops.geomTransf('Linear', transfCol, -1, 0, 0)
        ops.geomTransf('Linear', transfBeamX, 0, -1, 0)
        ops.geomTransf('Linear', transfBeamY, 1, 0, 0)
        # ...........................................................................
        # Elastic sections for the beams and columns
        # https://openseespydoc.readthedocs.io/en/latest/src/elasticSection.html
        # https://openseespydoc.readthedocs.io/en/latest/src/beamIntegration.html
        # https://openseespydoc.readthedocs.io/en/latest/src/element.html#beam-column-elements

        for i in range(self.column.name.shape[0]):
            for j in range(self.column.name.shape[1]):
                # ops.section('Elastic', int(self.column.name[i, j]), self.general.Ec, self.column.Area[i, j], stiffness_factor * self.column.IX[i, j], stiffness_factor * self.column.IY[i, j], self.general.G, self.column.J[i, j], 5/6, 5/6)
                ops.section('Elastic', int(self.column.name[i, j]), Ec, column_Area[i, j], column_IX[i, j], column_IY[i, j], G, column_J[i, j], 5/6, 5/6)
                ops.beamIntegration('Lobatto', int(self.column.name[i, j]), int(self.column.name[i, j]), 10) # TODO: is there any specific reason for 10 integration points?
                ops.element('forceBeamColumn', int(self.column.name[i, j]), int(self.column.elasnodei[i, j]), int(self.column.elasnodej[i, j]), transfCol, int(self.column.name[i, j]))
        for i in range(self.beamX.name.shape[0]):
            for j in range(self.beamX.name.shape[1]):
                # ops.section('Elastic', int(self.beamX.name[i, j]), self.general.Ec, self.beamX.Area[i, j], stiffness_factor * self.beamX.IZ[i, j], stiffness_factor * self.beamX.IY[i, j], self.general.G, self.beamX.J[i, j], 5/6, 5/6)
                ops.section('Elastic', int(self.beamX.name[i, j]), Ec, beamX_Area[i, j], beamX_IZ[i, j], beamX_IY[i, j], G, beamX_J[i, j], 5/6, 5/6)
                ops.beamIntegration('Lobatto', int(self.beamX.name[i, j]), int(self.beamX.name[i, j]), 9)
                ops.element('forceBeamColumn', int(self.beamX.name[i, j]), int(self.beamX.elasnodei[i, j]), int(self.beamX.elasnodej[i, j]), transfBeamX, int(self.beamX.name[i, j]))
        for i in range(self.beamStair.name.shape[0]):
            for j in range(self.beamStair.name.shape[1]):
                # ops.section('Elastic', int(self.beamStair.name[i, j]), self.general.Ec, self.beamStair.Area[i, j], stiffness_factor * self.beamStair.IZ[i, j], stiffness_factor * self.beamStair.IY[i, j], self.general.G, self.beamStair.J[i, j], 5/6, 5/6)
                ops.section('Elastic', int(self.beamStair.name[i, j]), Ec, beamStair_Area[i, j], beamStair_IZ[i, j], beamStair_IY[i, j], G, beamStair_J[i, j], 5/6, 5/6)
                ops.beamIntegration('Lobatto', int(self.beamStair.name[i, j]), int(self.beamStair.name[i, j]), 9)
                ops.element('forceBeamColumn', int(self.beamStair.name[i, j]), int(self.beamStair.elasnodei[i, j]), int(self.beamStair.elasnodej[i, j]), transfBeamX, int(self.beamStair.name[i, j]))
        for i in range(self.beamY.name.shape[0]):
            for j in range(self.beamY.name.shape[1]):
                # ops.section('Elastic', int(self.beamY.name[i, j]), self.general.Ec, self.beamY.Area[i, j], stiffness_factor * self.beamY.IZ[i, j], stiffness_factor * self.beamY.IY[i, j], self.general.G, self.beamY.J[i, j], 5/6, 5/6)
                ops.section('Elastic', int(self.beamY.name[i, j]), Ec, beamY_Area[i, j], beamY_IZ[i, j], beamY_IY[i, j], G, beamY_J[i, j], 5/6, 5/6)
                ops.beamIntegration('Lobatto', int(self.beamY.name[i, j]), int(self.beamY.name[i, j]), 9)
                ops.element('forceBeamColumn', int(self.beamY.name[i, j]), int(self.beamY.elasnodei[i, j]), int(self.beamY.elasnodej[i, j]), transfBeamY, int(self.beamY.name[i, j]))

    def _add_gravity_loads(self, floor_load="ped", roof_load='pedroof'):
        """
        Loads from ultimate limit state (ULS) load combination
        """
        # TODO: remove roundings after validation

        # constant time-series defines relationship between time-domain and loads
        ops.timeSeries("Linear", 1) 
        # plain load pattern added to the domain
        ops.pattern('Plain', 1, 1)

        # Floor loads
        for i in range(self.beamX.name.shape[0] - 1): 
            for j in range(self.beamX.name.shape[1]):
                # ops.eleLoad('-ele', int(self.beamX.name[i, j]), '-type', '-beamUniform', -getattr(self.beamX, floor_load)[i, j], 0.0)
                ops.eleLoad('-ele', int(self.beamX.name[i, j]), '-type', '-beamUniform', -np.round(getattr(self.beamX, floor_load)[i, j], 6), 0.0)
        for i in range(self.beamStair.name.shape[0] - 1): 
            for j in range(self.beamStair.name.shape[1]):
                # ops.eleLoad('-ele', int(self.beamStair.name[i, j]), '-type', '-beamUniform', -getattr(self.beamStair, floor_load)[i, j], 0.0)
                ops.eleLoad('-ele', int(self.beamStair.name[i, j]), '-type', '-beamUniform', -np.round(getattr(self.beamStair, floor_load)[i, j], 6), 0.0)
        for i in range(self.beamY.name.shape[0] - 1): 
            for j in range(self.beamY.name.shape[1]):
                # ops.eleLoad('-ele', int(self.beamY.name[i, j]), '-type', '-beamUniform', -getattr(self.beamY, floor_load)[i, j], 0.0)
                ops.eleLoad('-ele', int(self.beamY.name[i, j]), '-type', '-beamUniform', -np.round(getattr(self.beamY, floor_load)[i, j], 6), 0.0)
        # Roof loads
        for j in range(self.beamX.name.shape[1]):
            # ops.eleLoad('-ele', int(self.beamX.name[-1, j]), '-type', '-beamUniform', -getattr(self.beamX, roof_load)[-1, j], 0.0)
            ops.eleLoad('-ele', int(self.beamX.name[-1, j]), '-type', '-beamUniform', -np.round(getattr(self.beamX, roof_load)[-1, j], 6), 0.0)
        for j in range(self.beamStair.name.shape[1]):
            # ops.eleLoad('-ele', int(self.beamStair.name[-1, j]), '-type', '-beamUniform', -getattr(self.beamStair, roof_load)[-1, j], 0.0)
            ops.eleLoad('-ele', int(self.beamStair.name[-1, j]), '-type', '-beamUniform', -np.round(getattr(self.beamStair, roof_load)[-1, j], 6), 0.0)
        for j in range(self.beamY.name.shape[1]):
            # ops.eleLoad('-ele', int(self.beamY.name[-1, j]), '-type', '-beamUniform', -getattr(self.beamY, roof_load)[-1, j], 0.0)
            ops.eleLoad('-ele', int(self.beamY.name[-1, j]), '-type', '-beamUniform', -np.round(getattr(self.beamY, roof_load)[-1, j], 6), 0.0)

    def _calculate_horizontal_loads_lfa(self):
        his = self.general.Zvector.copy()
        Gis = np.append(0, self.general.TotalWeight)
        beta = self.general.ag.copy()
        sumGis = sum(Gis)
        sumhisHis = sum(his * Gis)
        if self.general.designlevel in ['CDN', 'CDL']:
            Fkis = beta * Gis
        else:
            Fkis = beta * Gis * his * (sumGis / sumhisHis)

        for ii in range(1, self.general.nstoreys + 2):
            tmp = self.general.Coordsref[(self.general.Coordsref[:, 0] < 100 * ii), 0]
            tmp = tmp[tmp > 100 * (ii - 1)].astype('int64')
            if ii == 1:
                nodes = tmp.reshape(1, -1)
            else:
                nodes = np.append(nodes, tmp.reshape(1, -1), axis=0)

        forces_nodes = np.ones(nodes.shape) * Fkis.reshape(-1, 1) / nodes.shape[1]

        return nodes, forces_nodes
    
    def _add_horizontal_loads_lfa(self, loading_case, nodes, forces_nodes):
        # Loading for the +xx direction
        if self.general.designlevel in ['CDN', 'CDL']:
            # Add the gravity loads for CDN and CDL. The loads are not combined later on with load factors.
            # In the cases of CDM and CDH, the lateral loads are then added to those of the quasi-permanent combination
            # so the analysis results under gravity loads were obtained separately and superposed later.
            self._add_gravity_loads(floor_load="pedEQ", roof_load='pedroofEQ')
            self._do_linear_static_analysis()
            ops.wipeAnalysis() 

        ops.timeSeries("Linear", 2)
        ops.pattern('Plain', 2, 2)
        for i in range(nodes.shape[0]):
            for j in range(nodes.shape[1]):
                node = int(nodes[i, j])
                force = round(float(forces_nodes[i, j]), 6)
                if loading_case == 'LFA+X': # in plus x direction
                    ops.load(node, force, 0.0, 0.0, 0.0, 0.0, 0.0)
                elif loading_case == 'LFA-X': # in negative x direction 
                    ops.load(node, -force, 0.0, 0.0, 0.0, 0.0, 0.0)
                elif loading_case == 'LFA+Y': # in plus y direction
                    ops.load(node, 0.0, force, 0.0, 0.0, 0.0, 0.0)
                elif loading_case == 'LFA-Y': # in negative y direction
                    ops.load(node, 0.0, -force, 0.0, 0.0, 0.0, 0.0)

    def _do_linear_static_analysis(self):
        # Perform load controlled linear static analysis
        ops.system('UmfPack')
        ops.numberer('RCM')
        ops.constraints('Transformation')
        ops.test('NormDispIncr', 1e-08, 6)
        ops.integrator('LoadControl', 1)
        ops.algorithm('Linear')
        ops.analysis('Static')
        ops.analyze(1)
        ops.loadConst('-time', 0.0)

    def _get_element_forces(self):
        beamX = {'M1': np.zeros(self.beamX.name.shape), 'M5': np.zeros(self.beamX.name.shape), 'M9': np.zeros(self.beamX.name.shape), 
                 'V1': np.zeros(self.beamX.name.shape), 'V5': np.zeros(self.beamX.name.shape), 'V9': np.zeros(self.beamX.name.shape)}
        for i in range(self.beamX.name.shape[0]): 
            for j in range(self.beamX.name.shape[1]):
                beamX['M1'][i, j] = ops.sectionForce(int(self.beamX.name[i, j]), 1, 2)
                beamX['M5'][i, j] = ops.sectionForce(int(self.beamX.name[i, j]), 5, 2)
                beamX['M9'][i, j] = ops.sectionForce(int(self.beamX.name[i, j]), 9, 2)
                beamX['V1'][i, j] = ops.sectionForce(int(self.beamX.name[i, j]), 1, 3)
                beamX['V5'][i, j] = ops.sectionForce(int(self.beamX.name[i, j]), 5, 3)
                beamX['V9'][i, j] = ops.sectionForce(int(self.beamX.name[i, j]), 9, 3)

        beamStair = {'M1': np.zeros(self.beamStair.name.shape), 'M5': np.zeros(self.beamStair.name.shape), 'M9': np.zeros(self.beamStair.name.shape), 
                 'V1': np.zeros(self.beamStair.name.shape), 'V5': np.zeros(self.beamStair.name.shape), 'V9': np.zeros(self.beamStair.name.shape)}
        for i in range(self.beamStair.name.shape[0]): 
            for j in range(self.beamStair.name.shape[1]):
                beamStair['M1'][i, j] = ops.sectionForce(int(self.beamStair.name[i, j]), 1, 2)
                beamStair['M5'][i, j] = ops.sectionForce(int(self.beamStair.name[i, j]), 5, 2)
                beamStair['M9'][i, j] = ops.sectionForce(int(self.beamStair.name[i, j]), 9, 2)
                beamStair['V1'][i, j] = ops.sectionForce(int(self.beamStair.name[i, j]), 1, 3)
                beamStair['V5'][i, j] = ops.sectionForce(int(self.beamStair.name[i, j]), 5, 3)
                beamStair['V9'][i, j] = ops.sectionForce(int(self.beamStair.name[i, j]), 9, 3)

        beamY = {'M1': np.zeros(self.beamY.name.shape), 'M5': np.zeros(self.beamY.name.shape), 'M9': np.zeros(self.beamY.name.shape), 
                 'V1': np.zeros(self.beamY.name.shape), 'V5': np.zeros(self.beamY.name.shape), 'V9': np.zeros(self.beamY.name.shape)}
        for i in range(self.beamY.name.shape[0]): 
            for j in range(self.beamY.name.shape[1]):
                beamY['M1'][i, j] = ops.sectionForce(int(self.beamY.name[i, j]), 1, 2)
                beamY['M5'][i, j] = ops.sectionForce(int(self.beamY.name[i, j]), 5, 2)
                beamY['M9'][i, j] = ops.sectionForce(int(self.beamY.name[i, j]), 9, 2)
                beamY['V1'][i, j] = ops.sectionForce(int(self.beamY.name[i, j]), 1, 3)
                beamY['V5'][i, j] = ops.sectionForce(int(self.beamY.name[i, j]), 5, 3)
                beamY['V9'][i, j] = ops.sectionForce(int(self.beamY.name[i, j]), 9, 3)

        column = {'N1': np.zeros(self.column.name.shape), 'Mz1': np.zeros(self.column.name.shape), 'Vy1': np.zeros(self.column.name.shape), 'My1': np.zeros(self.column.name.shape), 'Vz1': np.zeros(self.column.name.shape),
                 'N9': np.zeros(self.column.name.shape), 'Mz9': np.zeros(self.column.name.shape), 'Vy9': np.zeros(self.column.name.shape), 'My9': np.zeros(self.column.name.shape), 'Vz9': np.zeros(self.column.name.shape)}
        for i in range(self.column.name.shape[0]): 
            for j in range(self.column.name.shape[1]):
                column['N1'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 1, 1)
                column['Mz1'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 1, 2)
                column['Vy1'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 1, 3)
                column['My1'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 1, 4)
                column['Vz1'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 1, 5)
                column['N9'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 10, 1)
                column['Mz9'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 10, 2)
                column['Vy9'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 10, 3)
                column['My9'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 10, 4)
                column['Vz9'][i, j] = ops.sectionForce(int(self.column.name[i, j]), 10, 5)

        results = {'beamX': beamX, 'beamStair': beamStair, 'beamY': beamY, 'Column': column}
        # OpenSees recorders use precision of 6 by default, let's do the same TODO: remove after validation
        for element in results.keys():
            for force in results[element].keys():
                results[element][force] = signif(results[element][force], 6)

        return results


    def _write_opensees_tcl_model(self):
        """
        Generate models in tcl format for testing
        """

        self.general.Ec = np.round(self.general.Ec, 6)
        self.general.G = np.round(self.general.G, 6)
        self.column.Area = np.round(self.column.Area, 6)
        self.column.IX = np.round(self.column.IX, 6)
        self.column.IY = np.round(self.column.IY, 6)
        self.column.J = np.round(self.column.J, 6)
        self.beamX.Area = np.round(self.beamX.Area, 6)
        self.beamX.IZ = np.round(self.beamX.IZ, 6)
        self.beamX.IY = np.round(self.beamX.IY, 6)
        self.beamX.J = np.round(self.beamX.J, 6)
        self.beamX.ped = np.round(self.beamX.ped, 6)
        self.beamX.pedroof = np.round(self.beamX.pedroof, 6)
        self.beamStair.Area = np.round(self.beamStair.Area, 6)
        self.beamStair.IZ = np.round(self.beamStair.IZ, 6)
        self.beamStair.IY = np.round(self.beamStair.IY, 6)
        self.beamStair.J = np.round(self.beamStair.J, 6)
        self.beamStair.ped = np.round(self.beamStair.ped, 6)
        self.beamStair.pedroof = np.round(self.beamStair.pedroof, 6)
        self.beamY.Area = np.round(self.beamY.Area, 6)
        self.beamY.IZ = np.round(self.beamY.IZ, 6)
        self.beamY.IY = np.round(self.beamY.IY, 6)
        self.beamY.J = np.round(self.beamY.J, 6)
        self.beamY.ped = np.round(self.beamY.ped, 6)
        self.beamY.pedroof = np.round(self.beamY.pedroof, 6)

        file = open('elasticmodel1.tcl', 'w')
        file.write('wipe\n')
        file.write('wipeAnalysis\n')
        file.write('model BasicBuilder -ndm 3 -ndf 6\n')
        # Define nodes
        for node in self.general.Coordsref:
            node = node.tolist(); node[0] = int(node[0])
            file.write('node ' + ' '.join([str(item) for item in node]) + '\n')
        # ...........................................................................
        # Single-point constraints: Fix base nodes
        nodes2fix = self.general.Coordsref[(self.general.Coordsref[:, 0] < 100), 0]
        for node in nodes2fix:
            file.write(f'fix {node:.0f} 1 1 1 1 1 1\n')
        # ...........................................................................
        # Multi-point constraints: Rigid diaphragms --> TODO: Change the retained node to floor centre of mass
        for i in range(self.beamX.name.shape[0]):
            nodes = [int((i+1)*100 + node) for node in nodes2fix]
            file.write('rigidDiaphragm 3 ' + ' '.join([str(node) for node in nodes]) + '\n')
        # ...........................................................................
        # Geometric transformations
        file.write('set transfCol 1\n')
        file.write('set transfBeamX 2\n')
        file.write('set transfBeamY 3\n')
        file.write('geomTransf Linear $transfCol -1 0 0\n')
        file.write('geomTransf Linear $transfBeamX 0 -1 0\n')
        file.write('geomTransf Linear $transfBeamY 1 0 0\n')
        # ...........................................................................
        # Elastic sections for the beams and columns
        file.write('# Columns\n')
        for i in range(self.column.name.shape[0]):
            for j in range(self.column.name.shape[1]):
                file.write(f'section Elastic {self.column.name[i, j]:.0f} {self.general.Ec:4.6f} {self.column.Area[i, j]:4.6f} {self.column.IX[i, j]:4.6f} {self.column.IY[i, j]:4.6f} {self.general.G:4.6f} {self.column.J[i, j]:4.6f} [expr 5./6.] [expr 5./6.]\n')
                file.write(f'element forceBeamColumn {self.column.name[i, j]:.0f} {self.column.elasnodei[i, j]:.0f} {self.column.elasnodej[i, j]:.0f} $transfCol Lobatto {self.column.name[i, j]:.0f} 10\n')
        file.write('# BeamsX\n')
        for i in range(self.beamX.name.shape[0]):
            for j in range(self.beamX.name.shape[1]):
                file.write(f'section Elastic {self.beamX.name[i, j]:.0f} {self.general.Ec:4.6f} {self.beamX.Area[i, j]:4.6f} {self.beamX.IZ[i, j]:4.6f} {self.beamX.IY[i, j]:4.6f} {self.general.G:4.6f} {self.beamX.J[i, j]:4.6f} [expr 5./6.] [expr 5./6.]\n')
                file.write(f'element forceBeamColumn {self.beamX.name[i, j]:.0f} {self.beamX.elasnodei[i, j]:.0f} {self.beamX.elasnodej[i, j]:.0f} $transfBeamX Lobatto {self.beamX.name[i, j]:.0f} 9\n')
        file.write('# BeamsStair\n')
        for i in range(self.beamStair.name.shape[0]):
            for j in range(self.beamStair.name.shape[1]):
                file.write(f'section Elastic {self.beamStair.name[i, j]:.0f} {self.general.Ec:4.6f} {self.beamStair.Area[i, j]:4.6f} {self.beamStair.IZ[i, j]:4.6f} {self.beamStair.IY[i, j]:4.6f} {self.general.G:4.6f} {self.beamStair.J[i, j]:4.6f} [expr 5./6.] [expr 5./6.]\n')
                file.write(f'element forceBeamColumn {self.beamStair.name[i, j]:.0f} {self.beamStair.elasnodei[i, j]:.0f} {self.beamStair.elasnodej[i, j]:.0f} $transfBeamX Lobatto {self.beamStair.name[i, j]:.0f} 9\n')
        file.write('# BeamsY\n')
        for i in range(self.beamY.name.shape[0]):
            for j in range(self.beamY.name.shape[1]):
                file.write(f'section Elastic {self.beamY.name[i, j]:.0f} {self.general.Ec:4.6f} {self.beamY.Area[i, j]:4.6f} {self.beamY.IZ[i, j]:4.6f} {self.beamY.IY[i, j]:4.6f} {self.general.G:4.6f} {self.beamY.J[i, j]:4.6f} [expr 5./6.] [expr 5./6.]\n')
                file.write(f'element forceBeamColumn {self.beamY.name[i, j]:.0f} {self.beamY.elasnodei[i, j]:.0f} {self.beamY.elasnodej[i, j]:.0f} $transfBeamY Lobatto {self.beamY.name[i, j]:.0f} 9\n')
        # ...........................................................................
        file.write('pattern Plain 1 Linear {\n')
        # Floor loads
        file.write('# loading BeamsX\n')
        for i in range(self.beamX.name.shape[0] - 1): 
            for j in range(self.beamX.name.shape[1]):
                file.write(f'eleLoad -ele {self.beamX.name[i, j]:.0f} -type -beamUniform {-1 * self.beamX.pedEQ[i, j]:4.6f} 0.0\n')
        file.write('# loading BeamsStair\n')
        for i in range(self.beamStair.name.shape[0] - 1): 
            for j in range(self.beamStair.name.shape[1]):
                file.write(f'eleLoad -ele {self.beamStair.name[i, j]:.0f} -type -beamUniform {-1 * self.beamStair.pedEQ[i, j]:4.6f} 0.0\n')
        file.write('# loading BeamsY\n')
        for i in range(self.beamY.name.shape[0] - 1): 
            for j in range(self.beamY.name.shape[1]):
                file.write(f'eleLoad -ele {self.beamY.name[i, j]:.0f} -type -beamUniform {-1 * self.beamY.pedEQ[i, j]:4.6f} 0.0\n')
        # Roof loads
        file.write('# loading BeamsX\n')
        for j in range(self.beamX.name.shape[1]):
            file.write(f'eleLoad -ele {self.beamX.name[-1, j]:.0f} -type -beamUniform {-1 * self.beamX.pedroofEQ[-1, j]:4.6f} 0.0\n')
        file.write('# loading BeamsStair\n')
        for j in range(self.beamStair.name.shape[1]):
            file.write(f'eleLoad -ele {self.beamStair.name[-1, j]:.0f} -type -beamUniform {-1 * self.beamStair.pedroofEQ[-1, j]:4.6f} 0.0\n')
        file.write('# loading BeamsY\n')
        for j in range(self.beamY.name.shape[1]):
            file.write(f'eleLoad -ele {self.beamY.name[-1, j]:.0f} -type -beamUniform {-1 * self.beamY.pedroofEQ[-1, j]:4.6f} 0.0\n')
        file.write('}\n')
        # ...........................................................................
        # Recorders
        make_dir('Results/ResultsULS')
        file.write('# recorders Columns\n')
        for i in range(self.column.name.shape[0]):
            columns = [f'{col:.0f}' for col in self.column.name[i]]
            columns = ' '.join(columns)
            file.write(f'recorder Element -file Results/ResultsULS/column_storey_{i+1}_1.out -ele {columns} section 1 force\n')
            file.write(f'recorder Element -file Results/ResultsULS/column_storey_{i+1}_5.out -ele {columns} section 5 force\n')
            file.write(f'recorder Element -file Results/ResultsULS/column_storey_{i+1}_9.out -ele {columns} section 10 force\n')
        file.write('# recorders BeamsX\n')
        for i in range(self.beamX.name.shape[0]):
            file.write(f'recorder Element -file Results/ResultsULS/beamX_storey_{i+1}_1.out -eleRange {self.beamX.name[i,0]:.0f} {self.beamX.name[i,-1]:.0f} section 1 force\n')
            file.write(f'recorder Element -file Results/ResultsULS/beamX_storey_{i+1}_5.out -eleRange {self.beamX.name[i,0]:.0f} {self.beamX.name[i,-1]:.0f} section 5 force\n')
            file.write(f'recorder Element -file Results/ResultsULS/beamX_storey_{i+1}_9.out -eleRange {self.beamX.name[i,0]:.0f} {self.beamX.name[i,-1]:.0f} section 9 force\n')
        file.write('# recorders BeamsStair\n')
        file.write(f'recorder Element -file Results/ResultsULS/beamStair_1.out -eleRange {self.beamStair.name[0,0]:.0f} {self.beamStair.name[0,-1]:.0f} section 1 force\n')
        file.write(f'recorder Element -file Results/ResultsULS/beamStair_5.out -eleRange {self.beamStair.name[0,0]:.0f} {self.beamStair.name[0,-1]:.0f} section 5 force\n')
        file.write(f'recorder Element -file Results/ResultsULS/beamStair_9.out -eleRange {self.beamStair.name[0,0]:.0f} {self.beamStair.name[0,-1]:.0f} section 9 force\n')
        file.write('# recorders BeamsY\n')
        for i in range(self.beamY.name.shape[0]):
            file.write(f'recorder Element -file Results/ResultsULS/beamY_storey_{i+1}_1.out -eleRange {self.beamY.name[i,0]:.0f} {self.beamY.name[i,-1]:.0f} section 1 force\n')
            file.write(f'recorder Element -file Results/ResultsULS/beamY_storey_{i+1}_5.out -eleRange {self.beamY.name[i,0]:.0f} {self.beamY.name[i,-1]:.0f} section 5 force\n')
            file.write(f'recorder Element -file Results/ResultsULS/beamY_storey_{i+1}_9.out -eleRange {self.beamY.name[i,0]:.0f} {self.beamY.name[i,-1]:.0f} section 9 force\n')
        file.write(f'recorder Node -file Results/ResultsULS/nodeReactions.out -nodeRange {min(nodes2fix):.0f} {max(nodes2fix):.0f} -dof 1 2 3 4 5 6 reaction\n')

        file.write('system UmfPack\n')
        file.write('numberer RCM\n')
        file.write('constraints Transformation\n')
        file.write('test NormDispIncr 1e-08 6\n')
        file.write('integrator LoadControl 1\n')
        file.write('algorithm Linear\n')
        file.write('analysis Static\n')
        file.write('analyze 1\n')
        file.write('loadConst -time 0.0')
        file.write('wipe')
        file.close()