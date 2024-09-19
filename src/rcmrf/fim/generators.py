import numpy as np
import openseespy.opensees as ops

class OpsModel:

    def build_model(self):

        ops.wipe()
        ops.model('basic', '-ndm', 3, '-ndf', 6)
        self._add_nodes()
        self._add_joints()
        self._add_columns()
        self._add_beam('X')
        self._add_beam('Stair')
        self._add_beam('Y')
        self._do_gravity()

    def _add_nodes(self, rigM = 66666):

        # ---------------------------------------------------------------------------
        # Structural Nodes
        # ---------------------------------------------------------------------------
        Coordsref = np.round(self.general['Coordsref'], 2)
        for node in Coordsref:
            ops.node(int(node[0]), node[1], node[2], node[3])
        # ---------------------------------------------------------------------------
        # Single-point constraints: Fix base nodes
        # ---------------------------------------------------------------------------
        nodes2fix = Coordsref[(Coordsref[:, 0] < 100)]
        for node in nodes2fix:
            ops.fix(int(node[0]), 1, 1, 1, 1, 1, 1)
            ops.node(int(7000 + node[0]), node[1], node[2], node[3])
            ops.node(int(17000 + node[0]), node[1], node[2], node[3])
        # ---------------------------------------------------------------------------
        # Complementary Joint Nodes
        # ---------------------------------------------------------------------------
        joint1000 = np.round(self.joint['nodes'][:, 0:4], 2)
        joint2000 = np.round(self.joint['nodes'][:, 4:8], 2)
        joint3000 = np.round(self.joint['nodes'][:, 8:12], 2)
        joint4000 = np.round(self.joint['nodes'][:, 12:16], 2)
        joint5000 = np.round(self.joint['nodes'][:, 16:20], 2)
        joint6000 = np.round(self.joint['nodes'][:, 20:24], 2)
        joint7000 = np.round(self.joint['nodes'][:, 24:28], 2)
        FlagHXY = self.joint['Data'][:, 7]
        FlagBEAMXleft = self.joint['Data'][:, 8]
        FlagBEAMXright = self.joint['Data'][:, 9]
        FlagBEAMYleft = self.joint['Data'][:, 10]
        FlagBEAMYright = self.joint['Data'][:, 11]
        # ---------------------------------------------------------------------------
        # Nodes for the joint spring created to account for joint flexibility
        # ---------------------------------------------------------------------------
        for j in joint1000:
            ops.node(int(j[0]), j[1], j[2], j[3])
        # ---------------------------------------------------------------------------
        # Joint Rigid Elements - Ground
        # ---------------------------------------------------------------------------
        ops.geomTransf('Linear', 99999, -1, 0, 0)
        ops.geomTransf('Linear', 88888, 0, -1, 0)
        ops.geomTransf('Linear', 77777, 1, 0, 0)
        ops.uniaxialMaterial('Elastic', rigM, 1.e9)
        ops.section('Aggregator', 99999, rigM, 'P', rigM, 'Vy', rigM, 'Vz', rigM, 'My', rigM, 'Mz', rigM, 'T')
        # ---------------------------------------------------------------------------
        # All rigid nodes and elements - Ground Springs
        # ---------------------------------------------------------------------------
        for node in nodes2fix:
            ops.equalDOF(int(node[0]), int(7000 + node[0]), 1, 2, 3, 4, 5, 6)
        # ---------------------------------------------------------------------------
        # Joint Rigid Elements - Joint Offsets
        # ---------------------------------------------------------------------------
        for i in range(self.joint['nodes'].shape[0]):
            # Around node: int(self.joint['nodes'][i, 0])
            if FlagHXY[i] == 1:
                ops.node(int(joint2000[i, 0]), joint2000[i, 1], joint2000[i, 2], joint2000[i, 3])
                ops.node(int(joint7000[i, 0]), joint7000[i, 1], joint7000[i, 2], joint7000[i, 3])
                ops.node(int(10000 + joint2000[i, 0]), joint2000[i, 1], joint2000[i, 2], joint2000[i, 3])
                ops.node(int(10000 + joint7000[i, 0]), joint7000[i, 1], joint7000[i, 2], joint7000[i, 3])
                ops.element('elasticBeamColumn', int(joint2000[i, 0]), int(joint2000[i, 0]), int(self.joint['Data'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 99999)
                ops.element('elasticBeamColumn', int(joint7000[i, 0]), int(self.joint['Data'][i, 0]), int(joint7000[i, 0]), 1, 30000000, 15000000, 1, 1, 1, 99999)
            else:
                ops.node(int(joint2000[i, 0]), joint2000[i, 1], joint2000[i, 2], joint2000[i, 3])
                ops.node(int(10000 + joint2000[i, 0]), joint2000[i, 1], joint2000[i, 2], joint2000[i, 3])
                ops.element('elasticBeamColumn', int(joint2000[i, 0]), int(joint2000[i, 0]), int(self.joint['Data'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 99999)

            if FlagBEAMXleft[i] == 1:
                ops.node(int(joint5000[i, 0]), joint5000[i, 1], joint5000[i, 2], joint5000[i, 3])
                ops.node(int(10000 + joint5000[i, 0]), joint5000[i, 1], joint5000[i, 2], joint5000[i, 3])
                ops.element('elasticBeamColumn', int(joint5000[i, 0]), int(joint5000[i, 0]), int(self.joint['Data'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 88888)

            if FlagBEAMXright[i] == 1:
                ops.node(int(joint3000[i, 0]), joint3000[i, 1], joint3000[i, 2], joint3000[i, 3])
                ops.node(int(10000 + joint3000[i, 0]), joint3000[i, 1], joint3000[i, 2], joint3000[i, 3])
                ops.element('elasticBeamColumn', int(joint3000[i, 0]), int(self.joint['Data'][i, 0]), int(joint3000[i, 0]), 1, 30000000, 15000000, 1, 1, 1, 88888)

            if FlagBEAMYleft[i] == 1:
                ops.node(int(joint6000[i, 0]), joint6000[i, 1], joint6000[i, 2], joint6000[i, 3])
                ops.node(int(10000 + joint6000[i, 0]), joint6000[i, 1], joint6000[i, 2], joint6000[i, 3])
                ops.element('elasticBeamColumn', int(joint6000[i, 0]), int(joint6000[i, 0]), int(self.joint['Data'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 77777)
            
            if FlagBEAMYright[i] == 1:
                ops.node(int(joint4000[i, 0]), joint4000[i, 1], joint4000[i, 2], joint4000[i, 3])
                ops.node(int(10000 + joint4000[i, 0]), joint4000[i, 1], joint4000[i, 2], joint4000[i, 3])
                ops.element('elasticBeamColumn', int(joint4000[i, 0]), int(self.joint['Data'][i, 0]), int(joint4000[i, 0]), 1, 30000000, 15000000, 1, 1, 1, 77777)
        # ---------------------------------------------------------------------------
        # Staircase
        # ---------------------------------------------------------------------------
        for i in range(self.general['nstoreys']):
            ops.node(int(self.joint['Lstair2000'][i, 0]), self.joint['Lstair2000'][i, 1], self.joint['Lstair2000'][i, 2], self.joint['Lstair2000'][i, 3])
            ops.node(int(self.joint['Lstair7000'][i, 0]), self.joint['Lstair7000'][i, 1], self.joint['Lstair7000'][i, 2], self.joint['Lstair7000'][i, 3])
            ops.node(int(self.joint['Rstair2000'][i, 0]), self.joint['Rstair2000'][i, 1], self.joint['Rstair2000'][i, 2], self.joint['Rstair2000'][i, 3])
            ops.node(int(self.joint['Rstair7000'][i, 0]), self.joint['Rstair7000'][i, 1], self.joint['Rstair7000'][i, 2], self.joint['Rstair7000'][i, 3])
            ops.node(int(self.joint['Lstair3000'][i, 0]), self.joint['Lstair3000'][i, 1], self.joint['Lstair3000'][i, 2], self.joint['Lstair3000'][i, 3])
            ops.node(int(self.joint['Rstair5000'][i, 0]), self.joint['Rstair5000'][i, 1], self.joint['Rstair5000'][i, 2], self.joint['Rstair5000'][i, 3])

            ops.node(int(10000 + self.joint['Lstair2000'][i, 0]), self.joint['Lstair2000'][i, 1], self.joint['Lstair2000'][i, 2], self.joint['Lstair2000'][i, 3])
            ops.node(int(10000 + self.joint['Lstair7000'][i, 0]), self.joint['Lstair7000'][i, 1], self.joint['Lstair7000'][i, 2], self.joint['Lstair7000'][i, 3])
            ops.node(int(10000 + self.joint['Rstair2000'][i, 0]), self.joint['Rstair2000'][i, 1], self.joint['Rstair2000'][i, 2], self.joint['Rstair2000'][i, 3])
            ops.node(int(10000 + self.joint['Rstair7000'][i, 0]), self.joint['Rstair7000'][i, 1], self.joint['Rstair7000'][i, 2], self.joint['Rstair7000'][i, 3])
            ops.node(int(10000 + self.joint['Lstair3000'][i, 0]), self.joint['Lstair3000'][i, 1], self.joint['Lstair3000'][i, 2], self.joint['Lstair3000'][i, 3])
            ops.node(int(10000 + self.joint['Rstair5000'][i, 0]), self.joint['Rstair5000'][i, 1], self.joint['Rstair5000'][i, 2], self.joint['Rstair5000'][i, 3])
        
            ops.element('elasticBeamColumn', int(self.joint['Lstair2000'][i, 0]), int(self.general['CoordsExtra1'][i, 0]), int(self.joint['Lstair2000'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 99999)
            ops.element('elasticBeamColumn', int(self.joint['Lstair7000'][i, 0]), int(self.general['CoordsExtra1'][i, 0]), int(self.joint['Lstair7000'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 99999)
            ops.element('elasticBeamColumn', int(self.joint['Rstair2000'][i, 0]), int(self.general['CoordsExtra2'][i, 0]), int(self.joint['Rstair2000'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 99999)
            ops.element('elasticBeamColumn', int(self.joint['Rstair7000'][i, 0]), int(self.general['CoordsExtra2'][i, 0]), int(self.joint['Rstair7000'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 99999)
            ops.element('elasticBeamColumn', int(self.joint['Lstair3000'][i, 0]), int(self.general['CoordsExtra1'][i, 0]), int(self.joint['Lstair3000'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 88888)
            ops.element('elasticBeamColumn', int(self.joint['Rstair5000'][i, 0]), int(self.general['CoordsExtra2'][i, 0]), int(self.joint['Rstair5000'][i, 0]), 1, 30000000, 15000000, 1, 1, 1, 88888)
        # ---------------------------------------------------------------------------
        # Calculates the centre of mass of the roof
        # ---------------------------------------------------------------------------
        masses = self.general['Masses2']
        positions = self.general['Plan']
        heights = self.general['Zvector'][1:]
        for i, mass in enumerate(masses):
            aux_x = mass * positions[:, 0]
            aux_y = mass * positions[:, 1]
            X = sum(aux_x)/sum(mass)
            Y = sum(aux_y)/sum(mass)
            ops.node((100000*(i+1)+(i+1)), round(X, 6), round(Y, 6), round(heights[i], 6))
            ops.fix((100000*(i+1)+(i+1)), 0, 0, 1, 1, 1, 0)
        # ---------------------------------------------------------------------------
        # Multi-point constraints: Rigid diaphragms
        # ---------------------------------------------------------------------------
        perpDirn = 3
        for x in range(1, self.general['nstoreys']+1):
            rNodeTag = int(100000*x + x)
            cNodeTags = [int(x*100 + i) for i in range(1, self.general['nonlin_diaph_nodeid_max'] + 1)]
            ops.rigidDiaphragm(perpDirn, rNodeTag, *cNodeTags)
        # ---------------------------------------------------------------------------
        # Assign masses
        # ---------------------------------------------------------------------------
        Masses = self.general['MassesQuasi']
        for i in range(self.general['Coordsref'].shape[0]):
            ops.mass(int(self.general['Coordsref'][i, 0]), round(Masses[i]+0.01, 3), round(Masses[i]+0.01, 3), 0.01, 0.01, 0.01, 0.01)

    def _add_joints(self, rigidM = 100000):

        hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, gamm, P, Kspr = Common.preallocate_joint(self.joint, self.general)

        if self.general['BeamType'] == 1: # TODO: Rigid joints are imposed in the case of wide beams to force damage localization (""add reference""?????)--> Ask Nuno about this
            # Rigid joints have been selected since wide beams are used
            ops.uniaxialMaterial('Elastic', rigidM, 1e15)
            for i in range(self.joint['Data'].shape[0]): # Creating joint with central node self.joint['Data'][i,0]
                ops.element('zeroLength', int(10000 + self.joint['Data'][i,0]), int(self.joint['Data'][i,0]), int(1000+self.joint['Data'][i,0]), '-mat', rigidM, rigidM, rigidM, rigidM, rigidM, rigidM, '-dir', 1, 2, 3, 4, 5, 6, '-orient', 1, 0, 0, 0, 0, 1)

        else: # Defines joint type based on quality
            joint_type = Common.get_joint_type(self.general['designlevel'], self.general['quality']) # get the identifier

            if joint_type == 1: # Rigid joint
                ops.uniaxialMaterial('Elastic', rigidM, 1e9)
                for i in range(self.joint['Data'].shape[0]): # Creating joint with central node self.joint['Data'][i,0]
                    ops.element('zeroLength', int(10000+self.joint['Data'][i,0]), int(self.joint['Data'][i,0]), int(1000+self.joint['Data'][i,0]), '-mat', rigidM, rigidM, rigidM, rigidM, rigidM, rigidM, '-dir', 1, 2, 3, 4, 5, 6, '-orient', 1, 0, 0, 0, 0, 1)
            
            elif joint_type == 2: # Flexible elastic joint 
                ops.uniaxialMaterial('Elastic', rigidM, 1e12)
                for i in range(self.joint['Data'].shape[0]): # Creating joint with central node self.joint['Data'][i,0]
                    MEjX1, MEjY1 = Common.get_elastic_joint(hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, self.general['hstorey'], P, i)
                    ops.uniaxialMaterial('Elastic', int(200000+self.joint['Data'][i, 0]), Kspr[i])
                    ops.uniaxialMaterial('Elastic', int(300000+self.joint['Data'][i, 0]), MEjX1/0.0002)
                    ops.uniaxialMaterial('Elastic', int(400000+self.joint['Data'][i, 0]), MEjY1/0.0002)
                    ops.section('Aggregator', int(10000+self.joint['Data'][i, 0]), rigidM, 'P', rigidM, 'Vy', rigidM, 'Vz', int(400000+self.joint['Data'][i, 0]), 'My', int(300000+self.joint['Data'][i, 0]), 'Mz', rigidM, 'T')
                    ops.element('zeroLengthSection', int(1000+self.joint['Data'][i, 0]), int(1000+self.joint['Data'][i, 0]), int(self.joint['Data'][i, 0]), int(10000+self.joint['Data'][i, 0]), '-orient', 0, 0, 1, 0, 1, 0)

            elif joint_type == 3: # Flexible nonlinear joint joint
                ops.uniaxialMaterial('Elastic', rigidM, 1e9)

                for i in range(self.joint['Data'].shape[0]):  # Creating joint with central node self.joint['Data'][i,0]
                    MjX1, MjX2, MjX3, MjX4, MjX5, MjX6, MjY1, MjY2, MjY3, MjY4, MjY5, MjY6 = Common.get_inelastic_joint(hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, self.general['hstorey'], P, i)
                    ops.uniaxialMaterial('Elastic', int(200000+self.joint['Data'][i,0]), Kspr[i])
                    ops.uniaxialMaterial('Hysteretic', int(300000+self.joint['Data'][i,0]), MjX1, gamm[0], 1.1*MjX2, gamm[1], MjX3, gamm[2], -MjX4, -gamm[3], -1.1*MjX5, -gamm[4], -MjX6, -gamm[5], 0, 0, 0, 0, 0) # hyst_int[0] hyst_int[1] hyst_int[2] hyst_int[3] hyst_int[4])
                    ops.uniaxialMaterial('Hysteretic', int(400000+self.joint['Data'][i,0]), MjY1, gamm[0], 1.1*MjY2, gamm[1], MjY3, gamm[2], -MjY4, -gamm[3], -1.1*MjY5, -gamm[4], -MjY6, -gamm[5], 0, 0, 0, 0, 0) # hyst_int[0] hyst_int[1] hyst_int[2] hyst_int[3] hyst_int[4]
                    ops.element('zeroLength', int(1000+self.joint['Data'][i,0]), int(self.joint['Data'][i,0]), int(1000+self.joint['Data'][i,0]),' -mat', rigidM, rigidM, rigidM, int(400000+self.joint['Data'][i,0]), int(300000+self.joint['Data'][i,0]), rigidM, '-dir', 1, 2, 3, 4, 5, 6)

    def _add_columns(self, rigM = 66666):

        for i in range(len(self.column['Name'])):
            # Get inputs for plastic hinge
            comments, geomtransf, matflex, matshear, cdh_ele_inputs, notcdh_shear_inputsX, notcdh_shear_inputsY, noncdh_ele_inputs = Common.get_column_concentrated_plasticity(self.column, i)
            # ...........................................................................           
            geomtransf = [int(item) if j == 0 else item for j, item in enumerate(geomtransf)]
            mat_flexXtop = [int(item) if j == 0 else item for j, item in enumerate(matflex[0])]
            mat_flexXbot = [int(item) if j == 0 else item for j, item in enumerate(matflex[1])]
            mat_flexYtop = [int(item) if j == 0 else item for j, item in enumerate(matflex[2])]
            mat_flexYbot = [int(item) if j == 0 else item for j, item in enumerate(matflex[3])]
            # mattag_ShearXbot = [int(item) if j == 0 else item for j, item in enumerate(matshear[0])]
            # mattag_ShearXtop = [int(item) if j == 0 else item for j, item in enumerate(matshear[1])]
            # mattag_ShearYbot = [int(item) if j == 0 else item for j, item in enumerate(matshear[2])]
            # mattag_ShearYtop = [int(item) if j == 0 else item for j, item in enumerate(matshear[3])]
            # ...........................................................................
            ops.geomTransf('PDelta', *geomtransf)
            ops.uniaxialMaterial('Hysteretic', *mat_flexXtop)
            ops.uniaxialMaterial('Hysteretic', *mat_flexXbot)
            ops.uniaxialMaterial('Hysteretic', *mat_flexYtop)
            ops.uniaxialMaterial('Hysteretic', *mat_flexYbot)
            # ops.uniaxialMaterial('Hysteretic', *mattag_ShearXbot)
            # ops.uniaxialMaterial('Hysteretic', *mattag_ShearXtop)
            # ops.uniaxialMaterial('Hysteretic', *mattag_ShearYbot)
            # ops.uniaxialMaterial('Hysteretic', *mattag_ShearYtop)
            # ...........................................................................
            zero1_inputs = [int(item) for item in cdh_ele_inputs[2]]
            ele_inputs = [int(item) if j in [0, 1, 2, 9] else item for j, item in enumerate(cdh_ele_inputs[3])]
            zero2_inputs = [int(item) for item in cdh_ele_inputs[4]]
            # Even though capacity design for shear is not followed during design of CDH, it is assummed that there is no shear failure.
            # Therefore, shear springs are rigid. But they are nonlinear for other design classes. 
            # TODO: I think we need to do smth about the capacity design issue. At least consider during the design
            # if self.general['designlevel'] in ['CDH', 'CDM']:
            if self.general['designlevel'] == 'CDH':
                ops.section('Aggregator', int(cdh_ele_inputs[0][0]), rigM, 'P', rigM, 'Vy', rigM, 'Vz', int(cdh_ele_inputs[0][1]), 'My', int(cdh_ele_inputs[0][2]), 'Mz', rigM, 'T') # it has been corrected MyX will resist loads from XX pushover or Myy HMA
                ops.section('Aggregator', int(cdh_ele_inputs[1][0]), rigM, 'P', rigM, 'Vy', rigM, 'Vz', int(cdh_ele_inputs[1][1]), 'My', int(cdh_ele_inputs[1][2]), 'Mz', rigM, 'T') # it has been corrected  HMA
                ops.element('zeroLengthSection', *zero1_inputs, '-orient', 0, 0, 1, 0, 1, 0)
                ops.element('elasticBeamColumn', *ele_inputs)
                ops.element('zeroLengthSection', *zero2_inputs, '-orient', 0, 0, 1, 0, 1, 0)
            else:
                curve_Xtop =  [int(item) if j in [0, 1, 10, 11, 12, 13, 14, 15] else item for j, item in enumerate(notcdh_shear_inputsX[0])]
                limitstate_Xtop = [int(item) if j in [0, 18, 19] else item for j, item in enumerate(notcdh_shear_inputsX[1])]
                curve_Xbot =  [int(item) if j in [0, 1, 10, 11, 12, 13, 14, 15] else item for j, item in enumerate(notcdh_shear_inputsX[2])]
                limitstate_Xbot = [int(item) if j in [0, 18, 19] else item for j, item in enumerate(notcdh_shear_inputsX[3])]
                curve_Ytop =  [int(item) if j in [0, 1, 10, 11, 12, 13, 14, 15] else item for j, item in enumerate(notcdh_shear_inputsY[0])]
                limitstate_Ytop = [int(item) if j in [0, 18, 19] else item for j, item in enumerate(notcdh_shear_inputsY[1])]
                curve_Ybot =  [int(item) if j in [0, 1, 10, 11, 12, 13, 14, 15] else item for j, item in enumerate(notcdh_shear_inputsY[2])]
                limitstate_Ybot = [int(item) if j in [0, 18, 19] else item for j, item in enumerate(notcdh_shear_inputsY[3])]

                ops.limitCurve('ThreePoint', *curve_Xtop)
                ops.uniaxialMaterial('LimitState', *limitstate_Xtop)
                ops.limitCurve('ThreePoint', *curve_Xbot)
                ops.uniaxialMaterial('LimitState', *limitstate_Xbot)
                ops.limitCurve('ThreePoint', *curve_Ytop)
                ops.uniaxialMaterial('LimitState', *limitstate_Ytop)
                ops.limitCurve('ThreePoint', *curve_Ybot)
                ops.uniaxialMaterial('LimitState', *limitstate_Ybot)
                ops.section('Aggregator', int(noncdh_ele_inputs[0][0]), rigM, 'P', int(noncdh_ele_inputs[0][1]), 'Vy', int(noncdh_ele_inputs[0][2]), 'Vz', int(noncdh_ele_inputs[0][3]), 'My', int(noncdh_ele_inputs[0][4]), 'Mz', rigM, 'T') # it has been corrected HMA
                ops.section('Aggregator', int(noncdh_ele_inputs[1][0]), rigM, 'P', int(noncdh_ele_inputs[1][1]), 'Vy', int(noncdh_ele_inputs[1][2]), 'Vz', int(noncdh_ele_inputs[1][3]), 'My', int(noncdh_ele_inputs[1][4]), 'Mz', rigM, 'T') # it has been corrected HMA
                ops.element('zeroLengthSection', *zero1_inputs, '-orient', 0, 0, 1, 0, 1, 0)
                ops.element('elasticBeamColumn', *ele_inputs)
                ops.element('zeroLengthSection', *zero2_inputs, '-orient', 0, 0, 1, 0, 1, 0)

    def _add_beam(self, beam_type):
        
        if beam_type == "X":
            geo_transf_tag = 2
            mat_dir = 5
            equal_dof_4th = 4
            beam = self.beamX.copy()
            ops.uniaxialMaterial('Elastic', 101, 1e+010)
            ops.geomTransf('Linear', 2, 0, -1, 0)
        elif beam_type == "Y":
            geo_transf_tag = 3
            mat_dir = 4
            equal_dof_4th = 5
            beam = self.beamY.copy()
            ops.geomTransf('Linear', 3, 1, 0, 0)
        elif beam_type == "Stair":
            geo_transf_tag = 2
            mat_dir = 5
            equal_dof_4th = 4
            beam = self.beamStair.copy()

        for i in range(len(beam['Name'])):

            left_mat, right_mat, beam_ele, left_spring, right_spring, equaldof_left, equaldof_right = Common.get_beam_concentrated_plasticity(self.general, beam, i)
            left_mat = [int(item) if j == 0 else item for j, item in enumerate(left_mat)]
            right_mat = [int(item) if j == 0 else item for j, item in enumerate(right_mat)]
            beam_ele = [int(item) if j in [0, 1, 2] else item for j, item in enumerate(beam_ele)]

            ops.uniaxialMaterial('Hysteretic', *left_mat, 0.8, 0.2, 0.0, 0.0, 0.85)
            ops.uniaxialMaterial('Hysteretic', *right_mat, 0.8, 0.2, 0.0, 0.0, 0.85)
            ops.element('elasticBeamColumn', *beam_ele, geo_transf_tag)
            ops.element('zeroLength', int(left_spring[0]), int(left_spring[1]), int(left_spring[2]), '-mat', int(left_spring[3]), '-dir', mat_dir)
            ops.element('zeroLength', int(right_spring[0]), int(right_spring[1]), int(right_spring[2]), '-mat', int(right_spring[3]), '-dir', mat_dir)
            ops.equalDOF(int(equaldof_left[0]), int(equaldof_left[1]), 1, 2, 3, equal_dof_4th, 6)
            ops.equalDOF(int(equaldof_right[0]), int(equaldof_right[1]), 1, 2, 3, equal_dof_4th, 6)

    def _do_gravity(self):
        
        ops.timeSeries('Linear', 1) # constant time-series defines relationship between time-domain and loads
        ops.pattern('Plain', 1, 1) # plain load pattern added to the domain
        # Add gravity loads on beamX
        for i in range(len(self.beamX['pedEQ'])):
            ops.eleLoad('-ele', int(self.beamX['Name'][i]), '-type', '-beamUniform', -1*self.beamX['pedEQ'][i], 0)
        # Add gravity loads on beamY
        for i in range(len(self.beamY['pedEQ'])):
            ops.eleLoad('-ele', int(self.beamY['Name'][i]), '-type', '-beamUniform', -1*self.beamY['pedEQ'][i], 0)
        # Add gravity loads on beamStair
        for i in range(len(self.beamStair['pedEQ'])):
            ops.eleLoad('-ele', int(self.beamStair['Name'][i]), '-type', '-beamUniform', -1*self.beamStair['pedEQ'][i], 0)
        # Perform gravity analysis
        ops.system('UmfPack')
        ops.numberer('RCM')
        ops.constraints('Transformation')
        ops.test('NormDispIncr', 1e-06, 6)
        ops.integrator('LoadControl', 1)
        ops.algorithm('Linear')
        ops.analysis('Static')
        ops.analyze(1)
        ops.loadConst('-time', 0.0)
        ops.wipeAnalysis()

    def do_modal(self, results_folder, num_eigen=3):
        """Does modal analysis
        """
        print('Performing Modal Analysis...')
        self.build_model()
        report_file_path = (results_folder / 'ModalProperties.txt').as_posix()
        ops.eigen(num_eigen)
        ops.modalProperties('-file', report_file_path, '-unorm')
        print('Modal Analysis is finished')
        # TODO: Save eigen vectors here as well maybe

    def _solution_algorithm(self, ok, currentTolerance):
        
        if ok != 0:
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('KrylovNewton')
            ok = ops.analyze(1)
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('Newton', '-initial')

        if ok != 0:
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('NewtonLineSearch', 0.1)
            ok = ops.analyze(1)
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('Newton')

        if ok != 0:
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('Broyden', 50)
            ok = ops.analyze(1)
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('Newton')

        if ok != 0:
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('ModifiedNewton', 50)
            ok = ops.analyze(1)
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('Newton')

        if ok != 0:
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('BFGS')
            ok = ops.analyze(1)
            ops.test('NormDispIncr', currentTolerance, 10)
            ops.algorithm('Newton')

        return ok

    def do_nspa(self, results_folder, direction):
        """Does nonlinear static pushover analysis in both directions
        """
        # ...........................................................................
        # Initialisation 
        # ...........................................................................
        if direction == "X":
            filename = "nspa_x"
            IDctrlDOF = 1
        elif direction == "Y":
            filename = "nspa_y"
            IDctrlDOF = 2
        IDctrlNode = int(100000*self.general['nstoreys'] + self.general['nstoreys'])
        Dincr = 0.001
        report_file_path = (results_folder / f'{filename}.csv').as_posix() # File containing base shear vs. roof level deformation
        ctrl_disp = [0]
        base_shear = [0]
        Fi, Hi = Common.get_pushover_loads(self.general) # Get mass proportional loads and storey heights
        # ...........................................................................
        # Analysis
        # ...........................................................................
        print(f'Performing Nonlinear Static Pushover Analysis (NSPA) in -{direction}...')
        self.build_model() # Build numerical model
        ops.timeSeries('Linear', 200) # Define linear time-series defines relationship between time-domain and loads
        ops.pattern('Plain', 200, 200) # Define plain load pattern added to the domain
        for j in range(self.general['nstoreys']): # Horizontal loading for NSPA
            if direction == "X":
                ops.load(int((j+1)*100000+(j+1)), Fi[j], 0.0, 0.0, 0.0, 0.0, 0.0)
            elif direction == "Y":
                ops.load(int((j+1)*100000+(j+1)), 0.0, Fi[j], 0.0, 0.0, 0.0, 0.0)
        # ...........................................................................
        testTolerance0 = 1.0e-5
        testTolerance1 = 1.0e-4
        testTolerance2 = 1.0e-3
        testTolerance3 = 1.0e-2
        # Perform static horizontal analysis
        ops.system('UmfPack')
        ops.numberer('RCM')
        ops.constraints('Penalty', 10e9, 10e9)
        ops.test('NormDispIncr', testTolerance0, 30, 0)
        Dmax = 0.06*Hi[-1]
        ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)
        ops.algorithm('Newton')
        ops.analysis('Static')
        currentTime = 0
        ok = 0
        avect = 0
        currentDisp = ops.nodeDisp(IDctrlNode, IDctrlDOF)
        currentDrift = 100*currentDisp/Hi[-1]
        Tagum = 0
        Tagum1 = 0
        Tagum2 = 0
        maxavect = 0
        # ...........................................................................
        while ok == 0 and Tagum==0:
            ops.test('NormDispIncr', testTolerance0, 10, 0)
            ok = ops.analyze(1)
            if ok != 0:
                ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)
                ok = self._solution_algorithm(ok, testTolerance0)
        # ...........................................................................
            if ok != 0:
                ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)
                ok = self._solution_algorithm(ok, testTolerance1)
        # ...........................................................................
            if ok != 0:
                ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)
                ok = self._solution_algorithm(ok, testTolerance2)
        # ...........................................................................
            if ok != 0:
                ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)
                ok = self._solution_algorithm(ok, testTolerance3)
        # ...........................................................................
            if ok == 0:
                currentDisp = ops.nodeDisp(IDctrlNode, IDctrlDOF)
                avect = sum([ops.eleResponse(int(17000 + self.general['Reference'][i]), 'forces')[IDctrlDOF-1] for i in range(len(self.general['Reference']))])

                if avect < 0:
                    avect = -1*avect
            else:
                return
            if avect < 50000:
                pass
            else:
                return
            if avect < 100:
                avect = 0
            if avect >= maxavect:
                maxavect = avect + 0
            else:
                if avect >= 0.20*maxavect:
                    pass
                else:
                    Tagum1 = 1
        # ...........................................................................
            if currentDisp < Dmax:
                pass
            else:
                Tagum2 = 1
            Tagum = Tagum1 + Tagum2
            ops.reactions()
            ctrl_disp.append(ops.nodeDisp(IDctrlNode, IDctrlDOF))
            base_shear.append(-sum([ops.nodeReaction(int(7000 + self.general['Reference'][i]), IDctrlDOF) for i in range(len(self.general['Reference']))]))
        # ...........................................................................
        ops.wipe()
        data = np.array(list(zip(ctrl_disp, base_shear)))
        np.savetxt(report_file_path, data, delimiter=',', header='Roof Displacement [m], Base Shear [kN]', comments='')
        print(f'NSPA in -{direction} is finished')


class PyGenerator:

    def __init__(self):
        
        self.nodes = []
        self.joints = []
        self.columns = []
        self.beams_x = []
        self.beams_stair = []
        self.beams_y = []
        self.gravity = []
        self.modal = []
        self.solution_algorithm = []
        self.pushover_x = []
        self.pushover_y = []
        self.builder = []
        self.run_push_x = []
        self.run_push_y = []
        self.run_modal = []

    def get_writable_opensees_model(self):

        model = []
        analysis = []

        model.append("\n".join(self.builder))
        model.append("\n".join(self.nodes))
        model.append("\n".join(self.joints))
        model.append("\n".join(self.columns))
        model.append("\n".join(self.beams_x))
        model.append("\n".join(self.beams_stair))
        model.append("\n".join(self.beams_y))

        analysis.append("\n".join(self.gravity))
        analysis.append("\n".join(self.modal))
        analysis.append("\n".join(self.solution_algorithm))
        analysis.append("\n".join(self.pushover_x))
        analysis.append("\n".join(self.pushover_y))

        writable = {
        "model.py": "\n\n".join(model),
        "analysis.py": "\n\n".join(analysis),
        "run_push_x.py": "\n".join(self.run_push_x),
        "run_push_y.py": "\n".join(self.run_push_y),
        "run_modal.py": "\n".join(self.run_modal),
        }

        return writable

    def compile_opensees_model(self, general, joint, column, beamX, beamStair, beamY):

        self.add_model_builder(general['BuildingTYPE'])
        self.add_nodes(general, joint)
        self.nodes = ["def _nodes(rigM):\n"] + ["    " + item for item in self.nodes]
        self.add_joints(general, joint)
        self.joints = ["def _joints():\n"] + ["    " + item for item in self.joints]
        self.add_columns(general, column)
        self.columns = ["def _columns(rigM):\n"] + ["    " + item for item in self.columns]
        self.beams_x.append("ops.uniaxialMaterial('Elastic', 101, 1e+010)")
        self.beams_x.append("ops.geomTransf('Linear', 2, 0, -1, 0)")
        self.add_beam(general, beamX, 'beams_x')
        self.beams_x = ["def _beam_x():\n"] + ["    " + item for item in self.beams_x]
        self.add_beam(general, beamStair, 'beams_stair')
        self.beams_stair = ["def _beam_stair():\n"] + ["    " + item for item in self.beams_stair]
        self.beams_y.append("ops.geomTransf('Linear', 3, 1, 0, 0)")
        self.add_beam(general, beamY, 'beams_y')
        self.beams_y = ["def _beam_y():\n"] + ["    " + item for item in self.beams_y]

        self.add_gravity_analysis(beamX, beamStair, beamY)
        self.gravity = ["def gravity():\n"] + ["    " + item for item in self.gravity]
        self.gravity.insert(0, "import openseespy.opensees as ops\n")
        self.gravity.insert(0, "from pathlib import Path")
        self.add_modal_analysis()
        self.modal = ["def modal(num_eigen=3):\n"] + ["    " + item for item in self.modal]
        self.add_solution_algorithm()
        self.solution_algorithm = ["def _solution_algorithm(ok, currentTolerance):\n"] + ["    " + item for item in self.solution_algorithm]
        self.add_pushover(general, "X")
        self.pushover_x = ["def pushover_x():\n"] + ["    " + item for item in self.pushover_x]
        self.add_pushover(general, "Y")
        self.pushover_y = ["def pushover_y():\n"] + ["    " + item for item in self.pushover_y]
        
        self.add_run_push_x()
        
        self.add_run_push_y()
        
        self.add_run_modal()

    def add_run_push_x(self):
        self.run_push_x.append("import model")
        self.run_push_x.append("import analysis\n")
        self.run_push_x.append("model.build()")
        self.run_push_x.append("analysis.gravity()")
        self.run_push_x.append("analysis.pushover_x()")

    def add_run_push_y(self):
        self.run_push_y.append("import model")
        self.run_push_y.append("import analysis\n")
        self.run_push_y.append("model.build()")
        self.run_push_y.append("analysis.gravity()")
        self.run_push_y.append("analysis.pushover_y()")

    def add_run_modal(self):
        self.run_modal.append("import model")
        self.run_modal.append("import analysis\n")
        self.run_modal.append("model.build()")
        self.run_modal.append("analysis.gravity()")
        self.run_modal.append("analysis.modal(num_eigen=3)")

    def add_model_builder(self, layout):

        self.builder.append(f"# Building Layout: {layout}\n")
        self.builder.append("import openseespy.opensees as ops\n")
        self.builder.append("def build():\n")
        self.builder.append("    rigM = 66666 # Rigid-like material tag")
        # Model initialisation
        self.builder.append("    ops.wipe()")
        self.builder.append("    ops.model('basic', '-ndm', 3, '-ndf', 6)")
        self.builder.append("    _nodes(rigM)")
        self.builder.append("    _joints()")
        self.builder.append("    _columns(rigM)")
        self.builder.append("    _beam_x()")
        self.builder.append("    _beam_stair()")
        self.builder.append("    _beam_y()")

    def add_nodes(self, general, joint):

        Coordsref = general['Coordsref']

        # Structural Nodes
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Structural Nodes")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for node in Coordsref:
            self.nodes.append(f"ops.node({node[0]:.0f}, {node[1]:4.2f}, {node[2]:4.2f}, {node[3]:4.2f})")

        # Single-point constraints: Fix base nodes
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Supports")
        self.nodes.append("# ---------------------------------------------------------------------------")
        nodes2fix = Coordsref[(Coordsref[:, 0] < 100)]
        for node in nodes2fix:
            self.nodes.append(f"ops.fix({node[0]:.0f}, 1, 1, 1, 1, 1, 1)")
            self.nodes.append(f"ops.node({7000 + node[0]:.0f}, {node[1]:4.2f}, {node[2]:4.2f}, {node[3]:4.2f})")
            self.nodes.append(f"ops.node({17000 + node[0]:.0f}, {node[1]:4.2f}, {node[2]:4.2f}, {node[3]:4.2f})")

        # Complementary Joint Nodes
        joint1000 = joint['nodes'][:, 0:4]
        joint2000 = joint['nodes'][:, 4:8]
        joint3000 = joint['nodes'][:, 8:12]
        joint4000 = joint['nodes'][:, 12:16]
        joint5000 = joint['nodes'][:, 16:20]
        joint6000 = joint['nodes'][:, 20:24]
        joint7000 = joint['nodes'][:, 24:28]
        FlagHXY = joint['Data'][:, 7]
        FlagBEAMXleft = joint['Data'][:, 8]
        FlagBEAMXright = joint['Data'][:, 9]
        FlagBEAMYleft = joint['Data'][:, 10]
        FlagBEAMYright = joint['Data'][:, 11]

        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Nodes for the joint spring created to account for joint flexibility")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for i, j in enumerate(joint1000):
            self.nodes.append(f"ops.node({j[0]:.0f}, {j[1]:4.2f}, {j[2]:4.2f}, {j[3]:4.2f})")

        # Joint Rigid Elements - Ground
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Some stuff for the rigid elements")
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("ops.geomTransf('Linear', 99999, -1, 0, 0)")
        self.nodes.append("ops.geomTransf('Linear', 88888, 0, -1, 0)")
        self.nodes.append("ops.geomTransf('Linear', 77777, 1, 0, 0)")
        self.nodes.append("ops.uniaxialMaterial('Elastic', rigM, 1.e9)")
        self.nodes.append("ops.section('Aggregator', 99999, rigM, 'P', rigM, 'Vy', rigM, 'Vz', rigM, 'My', rigM, 'Mz', rigM, 'T')")
        self.nodes.append("# All rigid nodes and elements")
        self.nodes.append("# Ground Spring")
        for node in nodes2fix:
            self.nodes.append(f"ops.equalDOF({node[0]:.0f}, {7000 + node[0]:.0f}, 1, 2, 3, 4, 5, 6)")

        # Joint Rigid Elements - Offsets
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Joint Offsets")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for i in range(joint['nodes'].shape[0]):

            self.nodes.append(f"# Around node: {joint['nodes'][i, 0]:.0f}")
            if FlagHXY[i] == 1:
                self.nodes.append(f"ops.node({joint2000[i, 0]:.0f}, {joint2000[i, 1]:4.2f}, {joint2000[i, 2]:4.2f}, {joint2000[i, 3]:4.2f})")
                self.nodes.append(f"ops.node({joint7000[i, 0]:.0f}, {joint7000[i, 1]:4.2f}, {joint7000[i, 2]:4.2f}, {joint7000[i, 3]:4.2f})")
                self.nodes.append(f"ops.node({10000 + joint2000[i, 0]:.0f}, {joint2000[i, 1]:4.2f}, {joint2000[i, 2]:4.2f}, {joint2000[i, 3]:4.2f})")
                self.nodes.append(f"ops.node({10000 + joint7000[i, 0]:.0f}, {joint7000[i, 1]:4.2f}, {joint7000[i, 2]:4.2f}, {joint7000[i, 3]:4.2f})")
                self.nodes.append(f"ops.element('elasticBeamColumn', {joint2000[i, 0]:.0f}, {joint2000[i, 0]:.0f}, {joint['Data'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 99999)")
                self.nodes.append(f"ops.element('elasticBeamColumn', {joint7000[i, 0]:.0f}, {joint['Data'][i, 0]:.0f}, {joint7000[i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 99999)")
            else:
                self.nodes.append(f"ops.node({joint2000[i, 0]:.0f}, {joint2000[i, 1]:4.2f}, {joint2000[i, 2]:4.2f}, {joint2000[i, 3]:4.2f})")
                self.nodes.append(f"ops.node({10000 + joint2000[i, 0]:.0f}, {joint2000[i, 1]:4.2f}, {joint2000[i, 2]:4.2f}, {joint2000[i, 3]:4.2f})")
                self.nodes.append(f"ops.element('elasticBeamColumn', {joint2000[i, 0]:.0f}, {joint2000[i, 0]:.0f}, {joint['Data'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 99999)")

            if FlagBEAMXleft[i] == 1:
                self.nodes.append(f"ops.node({joint5000[i, 0]:.0f}, {joint5000[i, 1]:4.2f}, {joint5000[i, 2]:4.2f}, {joint5000[i, 3]:4.2f})")
                self.nodes.append(f"ops.node({10000 + joint5000[i, 0]:.0f}, {joint5000[i, 1]:4.2f}, {joint5000[i, 2]:4.2f}, {joint5000[i, 3]:4.2f})")
                self.nodes.append(f"ops.element('elasticBeamColumn', {joint5000[i, 0]:.0f}, {joint5000[i, 0]:.0f}, {joint['Data'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 88888)")

            if FlagBEAMXright[i] == 1:
                self.nodes.append(f"ops.node({joint3000[i, 0]:.0f}, {joint3000[i, 1]:4.2f}, {joint3000[i, 2]:4.2f}, {joint3000[i, 3]:4.2f})")
                self.nodes.append(f"ops.node({10000 + joint3000[i, 0]:.0f}, {joint3000[i, 1]:4.2f}, {joint3000[i, 2]:4.2f}, {joint3000[i, 3]:4.2f})")
                self.nodes.append(f"ops.element('elasticBeamColumn', {joint3000[i, 0]:.0f}, {joint['Data'][i, 0]:.0f}, {joint3000[i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 88888)")

            if FlagBEAMYleft[i] == 1:
                self.nodes.append(f"ops.node({joint6000[i, 0]:.0f}, {joint6000[i, 1]:4.2f}, {joint6000[i, 2]:4.2f}, {joint6000[i, 3]:4.2f})")
                self.nodes.append(f"ops.node({10000 + joint6000[i, 0]:.0f}, {joint6000[i, 1]:4.2f}, {joint6000[i, 2]:4.2f}, {joint6000[i, 3]:4.2f})")
                self.nodes.append(f"ops.element('elasticBeamColumn', {joint6000[i, 0]:.0f}, {joint6000[i, 0]:.0f}, {joint['Data'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 77777)")
            
            if FlagBEAMYright[i] == 1:
                self.nodes.append(f"ops.node({joint4000[i, 0]:.0f}, {joint4000[i, 1]:4.2f}, {joint4000[i, 2]:4.2f}, {joint4000[i, 3]:4.2f})")
                self.nodes.append(f"ops.node({10000 + joint4000[i, 0]:.0f}, {joint4000[i, 1]:4.2f}, {joint4000[i, 2]:4.2f}, {joint4000[i, 3]:4.2f})")
                self.nodes.append(f"ops.element('elasticBeamColumn', {joint4000[i, 0]:.0f}, {joint['Data'][i, 0]:.0f}, {joint4000[i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 77777)")

        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Staircase")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for i in range(general['nstoreys']):
            self.nodes.append(f"ops.node({joint['Lstair2000'][i, 0]:.0f}, {joint['Lstair2000'][i, 1]:4.2f}, {joint['Lstair2000'][i, 2]:4.2f}, {joint['Lstair2000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({joint['Lstair7000'][i, 0]:.0f}, {joint['Lstair7000'][i, 1]:4.2f}, {joint['Lstair7000'][i, 2]:4.2f}, {joint['Lstair7000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({joint['Rstair2000'][i, 0]:.0f}, {joint['Rstair2000'][i, 1]:4.2f}, {joint['Rstair2000'][i, 2]:4.2f}, {joint['Rstair2000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({joint['Rstair7000'][i, 0]:.0f}, {joint['Rstair7000'][i, 1]:4.2f}, {joint['Rstair7000'][i, 2]:4.2f}, {joint['Rstair7000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({joint['Lstair3000'][i, 0]:.0f}, {joint['Lstair3000'][i, 1]:4.2f}, {joint['Lstair3000'][i, 2]:4.2f}, {joint['Lstair3000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({joint['Rstair5000'][i, 0]:.0f}, {joint['Rstair5000'][i, 1]:4.2f}, {joint['Rstair5000'][i, 2]:4.2f}, {joint['Rstair5000'][i, 3]:4.2f})")

            self.nodes.append(f"ops.node({10000 + joint['Lstair2000'][i, 0]:.0f}, {joint['Lstair2000'][i, 1]:4.2f}, {joint['Lstair2000'][i, 2]:4.2f}, {joint['Lstair2000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({10000 + joint['Lstair7000'][i, 0]:.0f}, {joint['Lstair7000'][i, 1]:4.2f}, {joint['Lstair7000'][i, 2]:4.2f}, {joint['Lstair7000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({10000 + joint['Rstair2000'][i, 0]:.0f}, {joint['Rstair2000'][i, 1]:4.2f}, {joint['Rstair2000'][i, 2]:4.2f}, {joint['Rstair2000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({10000 + joint['Rstair7000'][i, 0]:.0f}, {joint['Rstair7000'][i, 1]:4.2f}, {joint['Rstair7000'][i, 2]:4.2f}, {joint['Rstair7000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({10000 + joint['Lstair3000'][i, 0]:.0f}, {joint['Lstair3000'][i, 1]:4.2f}, {joint['Lstair3000'][i, 2]:4.2f}, {joint['Lstair3000'][i, 3]:4.2f})")
            self.nodes.append(f"ops.node({10000 + joint['Rstair5000'][i, 0]:.0f}, {joint['Rstair5000'][i, 1]:4.2f}, {joint['Rstair5000'][i, 2]:4.2f}, {joint['Rstair5000'][i, 3]:4.2f})")
        
            self.nodes.append(f"ops.element('elasticBeamColumn', {joint['Lstair2000'][i, 0]:.0f}, {general['CoordsExtra1'][i, 0]:.0f}, {joint['Lstair2000'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 99999)")
            self.nodes.append(f"ops.element('elasticBeamColumn', {joint['Lstair7000'][i, 0]:.0f}, {general['CoordsExtra1'][i, 0]:.0f}, {joint['Lstair7000'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 99999)")
            self.nodes.append(f"ops.element('elasticBeamColumn', {joint['Rstair2000'][i, 0]:.0f}, {general['CoordsExtra2'][i, 0]:.0f}, {joint['Rstair2000'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 99999)")
            self.nodes.append(f"ops.element('elasticBeamColumn', {joint['Rstair7000'][i, 0]:.0f}, {general['CoordsExtra2'][i, 0]:.0f}, {joint['Rstair7000'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 99999)")
            self.nodes.append(f"ops.element('elasticBeamColumn', {joint['Lstair3000'][i, 0]:.0f}, {general['CoordsExtra1'][i, 0]:.0f}, {joint['Lstair3000'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 88888)")
            self.nodes.append(f"ops.element('elasticBeamColumn', {joint['Rstair5000'][i, 0]:.0f}, {general['CoordsExtra2'][i, 0]:.0f}, {joint['Rstair5000'][i, 0]:.0f}, 1, 30000000, 15000000, 1, 1, 1, 88888)")

        # Calculates the centre of mass of the roof
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append(f"# Rigid diaphragms")
        self.nodes.append("# ---------------------------------------------------------------------------")
        masses = general['Masses2']
        positions = general['Plan']
        heights = general['Zvector'][1:]
        for i, mass in enumerate(masses):
            aux_x = mass * positions[:, 0]
            aux_y = mass * positions[:, 1]
            X = sum(aux_x)/sum(mass)
            Y = sum(aux_y)/sum(mass)
            self.nodes.append(f"ops.node({100000*(i+1)+(i+1):.0f}, {X:.6f}, {Y:.6f}, {heights[i]:.6f})")
            self.nodes.append(f"ops.fix({100000*(i+1)+(i+1):.0f}, 0, 0, 1, 1, 1, 0)")

        # Multi-point constraints: Rigid diaphragms
        nodes = ["100000*x+x"]
        for i in range(1, general['nonlin_diaph_nodeid_max'] + 1):
            nodes.append(f"x*100+{i}")
        self.nodes.append(f"nstoreys = {general['nstoreys']}")
        self.nodes.append("for x in range(1, nstoreys+1):")
        self.nodes.append("    ops.rigidDiaphragm(3, " + ", ".join(nodes) + ")")

        # Assign masses
        Masses = general['MassesQuasi']
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Masses")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for i in range(general['Coordsref'].shape[0]):
            self.nodes.append(f"ops.mass({general['Coordsref'][i, 0]:.0f}, {Masses[i]+0.01:4.3f}, {Masses[i]+0.01:4.3f}, 0.01, 0.01, 0.01, 0.01)")

    def add_joints(self, general, joint):

        hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, gamm, P, Kspr = Common.preallocate_joint(joint, general)

        if general['BeamType'] == 1: # Rigid joints are imposed in the case of wide beams to force damage localization (""add reference""?????)--> Ask Nuno about this
            self.joints.append(f"# Rigid joints have been selected since DesignClass is {general['designlevel']} and wide beams are used")
            self.joints.append("rigidM = 100000")
            self.joints.append("ops.uniaxialMaterial('Elastic', rigidM, 1e15)")
            for i in range(joint['Data'].shape[0]):
                self.joints.append(f"# Creating joint with central node {joint['Data'][i,0]:.0f}")
                self.joints.append(f"ops.element('zeroLength', {10000+joint['Data'][i,0]:.0f}, {joint['Data'][i,0]:.0f}, {1000+joint['Data'][i,0]:.0f}, '-mat', rigidM, rigidM, rigidM, rigidM, rigidM, rigidM, '-dir', 1, 2, 3, 4, 5, 6, '-orient', 1, 0, 0, 0, 0, 1)")

        else: # defines joint type based on quality
            juntas = Common.get_joint_type(general['designlevel'], general['quality'])

            if juntas == 1: # Rigid joint
                self.joints.append(f"# Rigid joints have been selected for DesignClass: {general['designlevel']} and quality: {general['quality']}")
                self.joints.append("rigidM = 100000")
                self.joints.append("ops.uniaxialMaterial('Elastic', rigidM, 1e9)")
                for i in range(joint['Data'].shape[0]):
                    self.joints.append(f"# Creating joint with central node {joint['Data'][i,0]:.0f}")
                    self.joints.append(f"ops.element('zeroLength', {10000+joint['Data'][i,0]:.0f}, {joint['Data'][i,0]:.0f}, {1000+joint['Data'][i,0]:.0f}, '-mat', rigidM, rigidM, rigidM, rigidM, rigidM, rigidM, '-dir', 1, 2, 3, 4, 5, 6, '-orient', 1, 0, 0, 0, 0, 1)")
            
            elif juntas == 2: # Elastic joint 
                self.joints.append(f"# Elastic joints have been selected for DesignClass: {general['designlevel']} and quality: {general['quality']}")
                self.joints.append("rigidM = 100000")
                self.joints.append("ops.uniaxialMaterial('Elastic', rigidM, 1e12)")

                for i in range(joint['Data'].shape[0]):
                    MEjX1, MEjY1 = Common.get_elastic_joint(hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, general['hstorey'], P, i)

                    self.joints.append(f"# Creating joint with central node {joint['Data'][i,0]:.0f}")
                    self.joints.append(f"ops.uniaxialMaterial('Elastic', {200000+joint['Data'][i, 0]:.0f}, {Kspr[i]:4.6f})")
                    self.joints.append(f"ops.uniaxialMaterial('Elastic', {300000+joint['Data'][i, 0]:.0f}, {MEjX1/0.0002:4.6f})")
                    self.joints.append(f"ops.uniaxialMaterial('Elastic', {400000+joint['Data'][i, 0]:.0f}, {MEjY1/0.0002:4.6f})")
                    self.joints.append(f"ops.section('Aggregator', {10000+joint['Data'][i, 0]:.0f}, rigidM, 'P', rigidM, 'Vy', rigidM, 'Vz', {400000+joint['Data'][i, 0]:.0f}, 'My', {300000+joint['Data'][i, 0]:.0f}, 'Mz', rigidM, 'T')")
                    self.joints.append(f"ops.element('zeroLengthSection', {1000+joint['Data'][i, 0]:.0f}, {1000+joint['Data'][i, 0]:.0f}, {joint['Data'][i, 0]:.0f}, {10000+joint['Data'][i, 0]:.0f}, '-orient', 0, 0, 1, 0, 1, 0)")

            elif juntas == 3: # Flexible nonlinear joint joint
                self.joints.append(f"# Rigid joints have been selected for DesignClass: {general['designlevel']} and quality: {general['quality']}")
                self.joints.append("rigidM = 100000")
                self.joints.append("ops.uniaxialMaterial('Elastic', rigidM, 1e9)")

                for i in range(joint['Data'].shape[0]):
                    MjX1, MjX2, MjX3, MjX4, MjX5, MjX6, MjY1, MjY2, MjY3, MjY4, MjY5, MjY6 = Common.get_inelastic_joint(hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, general['hstorey'], P, i)

                    self.joints.append(f"# Creating joint with central node {joint['Data'][i,0]:.0f}")
                    self.joints.append(f"ops.uniaxialMaterial('Elastic', {200000+joint['Data'][i,0]:.0f}, {Kspr[i]:4.6f})")
                    self.joints.append(f"ops.uniaxialMaterial('Hysteretic', {300000+joint['Data'][i,0]:.0f}, {MjX1:4.6f}, {gamm[0]:4.6f}, {1.1*MjX2:4.6f}, {gamm[1]:4.6f}, {MjX3:4.6f}, {gamm[2]:4.6f}, {-MjX4:4.6f}, {-gamm[3]:4.6f}, {-1.1*MjX5:4.6f}, {-gamm[4]:4.6f}, {-MjX6:4.6f}, {-gamm[5]:4.6f}, 0, 0, 0, 0, 0)") # hyst_int[0] hyst_int[1] hyst_int[2] hyst_int[3] hyst_int[4]")
                    self.joints.append(f"ops.uniaxialMaterial('Hysteretic', {400000+joint['Data'][i,0]:.0f}, {MjY1:4.6f}, {gamm[0]:4.6f}, {1.1*MjY2:4.6f}, {gamm[1]:4.6f}, {MjY3:4.6f}, {gamm[2]:4.6f}, {-MjY4:4.6f}, {-gamm[3]:4.6f}, {-1.1*MjY5:4.6f}, {-gamm[4]:4.6f}, {-MjY6:4.6f}, {-gamm[5]:4.6f}, 0, 0, 0, 0, 0)") # hyst_int[0] hyst_int[1] hyst_int[2] hyst_int[3] hyst_int[4]")
                    self.joints.append(f"ops.element('zeroLength', {1000+joint['Data'][i,0]:.0f}, {joint['Data'][i,0]:.0f}, {1000+joint['Data'][i,0]:.0f},' -mat', rigidM, rigidM, rigidM, {400000+joint['Data'][i,0]:.0f}, {300000+joint['Data'][i,0]:.0f}, rigidM, '-dir', 1, 2, 3, 4, 5, 6)")

    def add_columns(self, general, column):

        for i in range(len(column['Name'])):
            # Get inputs for plastic hinge
            comments, geomtransf, matflex, matshear, cdh_ele_inputs, notcdh_shear_inputsX, notcdh_shear_inputsY, noncdh_ele_inputs = Common.get_column_concentrated_plasticity(column, i)
            # ...........................................................................           
            geomtransf_text = ", ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(geomtransf)])
            mat_flexXtop = ", ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matflex[0])])
            mat_flexXbot = ", ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matflex[1])])
            mat_flexYtop = ", ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matflex[2])])
            mat_flexYbot = ", ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matflex[3])])
            # mattag_ShearXbot = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matshear[0])])
            # mattag_ShearXtop = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matshear[1])])
            # mattag_ShearYbot = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matshear[2])])
            # mattag_ShearYtop = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matshear[3])])
            # ...........................................................................
            # Writes the OpenSees column model including all the nodes, springs and materials necessary for the definition of the column
            self.columns.extend(comments)
            self.columns.append(f"ops.geomTransf('PDelta', {geomtransf_text})")
            self.columns.append(f"ops.uniaxialMaterial('Hysteretic', {mat_flexXtop})")
            self.columns.append(f"ops.uniaxialMaterial('Hysteretic', {mat_flexXbot})")
            self.columns.append(f"ops.uniaxialMaterial('Hysteretic', {mat_flexYtop})")
            self.columns.append(f"ops.uniaxialMaterial('Hysteretic', {mat_flexYbot})")
            # self.columns.append(f"uniaxialMaterial Hysteretic {mattag_ShearXbot}")
            # self.columns.append(f"uniaxialMaterial Hysteretic {mattag_ShearXtop}")
            # self.columns.append(f"uniaxialMaterial Hysteretic {mattag_ShearYbot}")
            # self.columns.append(f"uniaxialMaterial Hysteretic {mattag_ShearYtop}")
            # ...........................................................................
            zero1_text = ", ".join([f"{item:.0f}" for item in cdh_ele_inputs[2]])
            ele_text = ", ".join([f"{item:.0f}" if j in [0, 1, 2, 9] else f"{item:4.6f}" for j, item in enumerate(cdh_ele_inputs[3])])
            zero2_text = ", ".join([f"{item:.0f}" for item in cdh_ele_inputs[4]])
            # Even though capacity design for shear is not followed during design of CDH, it is assummed that there is no shear failure.
            # Therefore, shear springs are rigid. But they are nonlinear for other design classes. 
            # TODO: I think we need to do smth about the capacity design issue. At least consider during the design
            # if general['designlevel'] in ['CDH', 'CDM']:
            if general['designlevel'] == 'CDH':
                self.columns.append(f"ops.section('Aggregator', {cdh_ele_inputs[0][0]:.0f}, rigM, 'P', rigM, 'Vy', rigM, 'Vz', {cdh_ele_inputs[0][1]:.0f}, 'My', {cdh_ele_inputs[0][2]:.0f}, 'Mz', rigM, 'T')") # it has been corrected MyX will resist loads from XX pushover or Myy HMA
                self.columns.append(f"ops.section('Aggregator', {cdh_ele_inputs[1][0]:.0f}, rigM, 'P', rigM, 'Vy', rigM, 'Vz', {cdh_ele_inputs[1][1]:.0f}, 'My', {cdh_ele_inputs[1][2]:.0f}, 'Mz', rigM, 'T')") # it has been corrected  HMA
                self.columns.append(f"ops.element('zeroLengthSection', {zero1_text}, '-orient', 0, 0, 1, 0, 1, 0)")
                self.columns.append(f"ops.element('elasticBeamColumn', {ele_text})")
                self.columns.append(f"ops.element('zeroLengthSection', {zero2_text}, '-orient', 0, 0, 1, 0, 1, 0)")
            else:
                curve_Xtop_text =  ", ".join([f"{item:.0f}" if j in [0, 1, 10, 11, 12, 13, 14, 15] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsX[0])])
                limitstate_Xtop_text = ", ".join([f"{item:.0f}" if j in [0, 18, 19] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsX[1])])
                curve_Xbot_text =  ", ".join([f"{item:.0f}" if j in [0, 1, 10, 11, 12, 13, 14, 15] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsX[2])])
                limitstate_Xbot_text = ", ".join([f"{item:.0f}" if j in [0, 18, 19] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsX[3])])
                curve_Ytop_text =  ", ".join([f"{item:.0f}" if j in [0, 1, 10, 11, 12, 13, 14, 15] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsY[0])])
                limitstate_Ytop_text = ", ".join([f"{item:.0f}" if j in [0, 18, 19] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsY[1])])
                curve_Ybot_text =  ", ".join([f"{item:.0f}" if j in [0, 1, 10, 11, 12, 13, 14, 15] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsY[2])])
                limitstate_Ybot_text = ", ".join([f"{item:.0f}" if j in [0, 18, 19] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsY[3])])

                self.columns.append(f"ops.limitCurve('ThreePoint', {curve_Xtop_text})")
                self.columns.append(f"ops.uniaxialMaterial('LimitState', {limitstate_Xtop_text})")
                self.columns.append(f"ops.limitCurve('ThreePoint', {curve_Xbot_text})")
                self.columns.append(f"ops.uniaxialMaterial('LimitState', {limitstate_Xbot_text})")
                self.columns.append(f"ops.limitCurve('ThreePoint', {curve_Ytop_text})")
                self.columns.append(f"ops.uniaxialMaterial('LimitState', {limitstate_Ytop_text})")
                self.columns.append(f"ops.limitCurve('ThreePoint', {curve_Ybot_text})")
                self.columns.append(f"ops.uniaxialMaterial('LimitState', {limitstate_Ybot_text})")
                self.columns.append(f"ops.section('Aggregator', {noncdh_ele_inputs[0][0]:.0f}, rigM, 'P', {noncdh_ele_inputs[0][1]:.0f}, 'Vy', {noncdh_ele_inputs[0][2]:.0f}, 'Vz', {noncdh_ele_inputs[0][3]:.0f}, 'My', {noncdh_ele_inputs[0][4]:.0f}, 'Mz', rigM, 'T')") # it has been corrected HMA
                self.columns.append(f"ops.section('Aggregator', {noncdh_ele_inputs[1][0]:.0f}, rigM, 'P', {noncdh_ele_inputs[1][1]:.0f}, 'Vy', {noncdh_ele_inputs[1][2]:.0f}, 'Vz', {noncdh_ele_inputs[1][3]:.0f}, 'My', {noncdh_ele_inputs[1][4]:.0f}, 'Mz', rigM, 'T')") # it has been corrected HMA
                self.columns.append(f"ops.element('zeroLengthSection', {zero1_text}, '-orient', 0, 0, 1, 0, 1, 0)")
                self.columns.append(f"ops.element('elasticBeamColumn', {ele_text})")
                self.columns.append(f"ops.element('zeroLengthSection', {zero2_text}, '-orient', 0, 0, 1, 0, 1, 0)")

    def add_beam(self, general, beam, attr):
        
        if attr == 'beams_x':
            tag = "X"
            geo_transf_tag = 2
            mat_dir = 5
            equal_dof_4th = 4
        elif attr == 'beams_y':
            tag = "Y"
            geo_transf_tag = 3
            mat_dir = 4
            equal_dof_4th = 5
        elif attr == 'beams_stair':
            tag = "Stair"
            geo_transf_tag = 2
            mat_dir = 5
            equal_dof_4th = 4

        for i in range(len(beam['Name'])):

            left_mat, right_mat, beam_ele, left_spring, right_spring, equaldof_left, equaldof_right = Common.get_beam_concentrated_plasticity(general, beam, i)
            left_mat_text = ", ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(left_mat)])
            right_mat_text = ", ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(right_mat)])
            beam_ele_text = ", ".join([f"{item:.0f}" if j in [0, 1, 2] else f"{item:4.6f}" for j, item in enumerate(beam_ele)])
            getattr(self, attr).append(f"# Beam{tag} {beam_ele[0]:.0f} {general['designlevel']} Linear")
            getattr(self, attr).append(f"ops.uniaxialMaterial('Hysteretic', {left_mat_text}, 0.8, 0.2, 0.0, 0.0, 0.85)")
            getattr(self, attr).append(f"ops.uniaxialMaterial('Hysteretic', {right_mat_text}, 0.8, 0.2, 0.0, 0.0, 0.85)")
            getattr(self, attr).append(f"ops.element('elasticBeamColumn', {beam_ele_text}, {geo_transf_tag})")
            getattr(self, attr).append(f"ops.element('zeroLength', {left_spring[0]:.0f}, {left_spring[1]:.0f}, {left_spring[2]:.0f}, '-mat', {left_spring[3]:.0f}, '-dir', {mat_dir})")
            getattr(self, attr).append(f"ops.element('zeroLength', {right_spring[0]:.0f}, {right_spring[1]:.0f}, {right_spring[2]:.0f}, '-mat', {right_spring[3]:.0f}, '-dir', {mat_dir})")
            getattr(self, attr).append(f"ops.equalDOF({equaldof_left[0]:.0f}, {equaldof_left[1]:.0f}, 1, 2, 3, {equal_dof_4th}, 6)")
            getattr(self, attr).append(f"ops.equalDOF({equaldof_right[0]:.0f}, {equaldof_right[1]:.0f}, 1, 2, 3, {equal_dof_4th}, 6)")

    def add_gravity_analysis(self, beamX, beamStair, beamY):
        
        # Add gravity loads
        # constant time-series defines relationship between time-domain and loads
        self.gravity.append("ops.timeSeries('Linear', 1)")
        # plain load pattern added to the domain
        self.gravity.append("ops.pattern('Plain', 1, 1)")
        self.gravity.append("# loading BeamsX")
        for i in range(len(beamX['pedEQ'])):
            self.gravity.append(f"ops.eleLoad('-ele', {beamX['Name'][i]:.0f}, '-type', '-beamUniform', {-1*beamX['pedEQ'][i]:4.1f}, 0)")
        self.gravity.append("# loading BeamsY")

        for i in range(len(beamY['pedEQ'])):
            self.gravity.append(f"ops.eleLoad('-ele', {beamY['Name'][i]:.0f}, '-type', '-beamUniform', {-1*beamY['pedEQ'][i]:4.1f}, 0)")
        self.gravity.append("# loading BeamsStair")

        for i in range(len(beamStair['pedEQ'])):
            self.gravity.append(f"ops.eleLoad('-ele', {beamStair['Name'][i]:.0f}, '-type', '-beamUniform', {-1*beamStair['pedEQ'][i]:4.1f}, 0)")

        # Perform gravity analysis
        self.gravity.append("# Perform gravity analysis")
        self.gravity.append("ops.system('UmfPack')")
        self.gravity.append("ops.numberer('RCM')")
        self.gravity.append("ops.constraints('Transformation')")
        self.gravity.append("ops.test('NormDispIncr', 1e-06, 6)")
        self.gravity.append("ops.integrator('LoadControl', 1)")
        self.gravity.append("ops.algorithm('Linear')")
        self.gravity.append("ops.analysis('Static')")
        self.gravity.append("ops.analyze(1)")
        self.gravity.append("print('Gravity analysis complete..')")
        self.gravity.append("ops.loadConst('-time', 0.0)")

    def add_modal_analysis(self):

        # Perform modal analysis
        self.modal.append("print('Wait a second... Ready to go for modal analysis...')")
        self.modal.append("output_directory = Path(__file__).parent / 'Modal'")
        self.modal.append("if not Path.exists(output_directory):")
        self.modal.append("    Path.mkdir(output_directory)")
        self.modal.append("report_file_path = (output_directory / 'ModalProperties.txt').as_posix()")
        self.modal.append("ops.eigen(num_eigen)")
        self.modal.append("ops.modalProperties('-print', '-file', report_file_path, '-unorm')")
        self.modal.append("print('Modal Analysis Done')")
        # TODO: Save eigen vectors here as well maybe

    def add_solution_algorithm(self):
        
        self.solution_algorithm.append("if ok != 0:")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('KrylovNewton')")
        self.solution_algorithm.append("    ok = ops.analyze(1)")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('Newton', '-initial')")

        self.solution_algorithm.append("if ok != 0:")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('NewtonLineSearch', 0.1)")
        self.solution_algorithm.append("    ok = ops.analyze(1)")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('Newton')")

        self.solution_algorithm.append("if ok != 0:")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('Broyden', 50)")
        self.solution_algorithm.append("    ok = ops.analyze(1)")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('Newton')")

        self.solution_algorithm.append("if ok != 0:")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('ModifiedNewton', 50)")
        self.solution_algorithm.append("    ok = ops.analyze(1)")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('Newton')")

        self.solution_algorithm.append("if ok != 0:")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('BFGS')")
        self.solution_algorithm.append("    ok = ops.analyze(1)")
        self.solution_algorithm.append("    ops.test('NormDispIncr', currentTolerance, 10)")
        self.solution_algorithm.append("    ops.algorithm('Newton')")

        self.solution_algorithm.append("return ok")

    def add_pushover(self, general, direction):
        
        # variables associated with direction
        if direction == "X":
            folder_name = "PUSH_X"
            dof = 1
            attr = 'pushover_x'
        elif direction == "Y":
            folder_name = "PUSH_Y"
            dof = 2
            attr = 'pushover_y'

        getattr(self, attr).append("ops.wipeAnalysis()")
        getattr(self, attr).append(f"output_directory = (Path(__file__).parent / '{folder_name}')")
        getattr(self, attr).append("if not Path.exists(output_directory):")
        getattr(self, attr).append("    Path.mkdir(output_directory)")
        getattr(self, attr).append("disp_file_path = (output_directory / 'nodeD.out').as_posix()")
        getattr(self, attr).append("reaction_file_path = (output_directory / 'nodesR.out').as_posix()")
        getattr(self, attr).append("drift_file_path = (output_directory / 'drifts.out').as_posix()")
        getattr(self, attr).append("floor_cm_disp_file_path = (output_directory / 'floor_cm_disp.out').as_posix()")
        getattr(self, attr).append("storey_heights_file_path = (output_directory / 'storey_heights.out').as_posix()")
        # ...........................................................................
        # Get mass proportional loads and storey heights
        Fi, Hi = Common.get_pushover_loads(general)
        # ...........................................................................
        getattr(self, attr).append("# LATERAL-LOAD distribution for static pushover analysis")
        getattr(self, attr).append("# Calculate distribution of lateral load based on mass/weight distributions along building height")
        getattr(self, attr).append("# Fj = WjHj/sum(WiHi) * Weight at each floor j")
        # linear time-series defines relationship between time-domain and loads
        getattr(self, attr).append("ops.timeSeries('Linear', 200)")
        # plain load pattern added to the domain
        getattr(self, attr).append("ops.pattern('Plain', 200, 200)")
        for j in range(general['nstoreys']):
            if direction == "X":
                getattr(self, attr).append(f"ops.load({(j+1)*100000+(j+1):.0f}, {Fi[j]:4.6f}, 0.0, 0.0, 0.0, 0.0, 0.0)")
            elif direction == "Y":
                getattr(self, attr).append(f"ops.load({(j+1)*100000+(j+1):.0f}, 0.0, {Fi[j]:4.6f}, 0.0, 0.0, 0.0, 0.0)") 
        # ...........................................................................
        # For some reason drift recorder does not work in OpenSeesPy for multiple nodes. Commented for now.
        montoringnode = 100000*general['nstoreys'] + general['nstoreys']
        getattr(self, attr).append(f"ops.recorder('Node', '-file', disp_file_path, '-node', {montoringnode:.0f}, '-dof', {dof}, 'disp')")
        getattr(self, attr).append(f"# ops.recorder('Drift', '-file', drift_file_path, '-iNode', ")
        getattr(self, attr)[-1] += ", ".join([f"{general['Reference'][-1] + i*100}" for i in range(general['nstoreys'])])
        getattr(self, attr)[-1] += ", '-jNode', "
        getattr(self, attr)[-1] += ", ".join([f"{general['Reference'][-1] + i*100}" for i in range(1, general['nstoreys'] + 1)])
        getattr(self, attr)[-1] += f", '-dof', {dof}, '-perpDirn', 3)"
        getattr(self, attr).append(f"ops.recorder('Node', '-file', reaction_file_path, '-node', ")
        getattr(self, attr)[-1] += ", ".join([f"{7000 + general['Reference'][i]}" for i in range(len(general['Reference']))])
        getattr(self, attr)[-1] += f", '-dof', {dof}, 'reaction')"
        getattr(self, attr).append(f"ops.recorder('Node', '-file', floor_cm_disp_file_path, '-node', ")
        getattr(self, attr)[-1] += ", ".join([f"{(i+1)*100000+(i+1):.0f}" for i in range(general['nstoreys'])])
        getattr(self, attr)[-1] += f", '-dof', {dof}, 'disp')"
        getattr(self, attr).append(f"storey_heights = [")
        getattr(self, attr)[-1] += ", ".join([f"{general['hground']}"] + [f"{general['hstorey']}"]*(general['nstoreys']-1))
        getattr(self, attr)[-1] += "]"
        getattr(self, attr).append("with open(storey_heights_file_path, 'w') as file:")
        getattr(self, attr).append("    for h in storey_heights:")
        getattr(self, attr).append("        file.write(f'{h}\\n')")
        # ...........................................................................
        getattr(self, attr).append("testTolerance0 = 1.0e-5")
        getattr(self, attr).append("testTolerance1 = 1.0e-4")
        getattr(self, attr).append("testTolerance2 = 1.0e-3")
        getattr(self, attr).append("testTolerance3 = 1.0e-2")
        getattr(self, attr).append("# Perform static horizontal analysis")
        getattr(self, attr).append("ops.system('UmfPack')")
        getattr(self, attr).append("ops.numberer('RCM')")
        getattr(self, attr).append("ops.constraints('Penalty', 10e9, 10e9)")
        getattr(self, attr).append("ops.test('NormDispIncr', testTolerance0, 30, 0)")
        getattr(self, attr).append(f"IDctrlNode = {montoringnode:.0f}")
        getattr(self, attr).append(f"IDctrlDOF = {dof}")
        getattr(self, attr).append(f"Dmax = {0.06*Hi[-1]:4.3f}")
        getattr(self, attr).append("Dincr = 0.001")
        getattr(self, attr).append("ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)")                                                
        getattr(self, attr).append("ops.algorithm('Newton')")
        getattr(self, attr).append("ops.analysis('Static')")
        getattr(self, attr).append("currentTolerance = testTolerance0")
        getattr(self, attr).append("currentTime = 0")
        getattr(self, attr).append("ok = 0")
        getattr(self, attr).append("avect = 0")
        getattr(self, attr).append("currentDisp = ops.nodeDisp(IDctrlNode, IDctrlDOF)")
        getattr(self, attr).append(f"currentDrift = 100*currentDisp/{Hi[-1]:4.3f}")
        getattr(self, attr).append("Tagum = 0")
        getattr(self, attr).append("Tagum1 = 0")
        getattr(self, attr).append("Tagum2 = 0")
        getattr(self, attr).append("maxavect = 0")
        # ...........................................................................
        getattr(self, attr).append("while ok == 0 and Tagum==0:")
        getattr(self, attr).append("    ops.test('NormDispIncr', currentTolerance, 10, 0)")
        getattr(self, attr).append("    ok = ops.analyze(1)")
        getattr(self, attr).append("    if ok != 0:")
        getattr(self, attr).append("        ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)")
        getattr(self, attr).append("        currentTolerance = testTolerance0")
        getattr(self, attr).append("        ok = _solution_algorithm(ok, currentTolerance)")
        # ...........................................................................
        getattr(self, attr).append("    if ok != 0:")
        getattr(self, attr).append("        ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)")
        getattr(self, attr).append("        currentTolerance = testTolerance1")
        getattr(self, attr).append("        ok = _solution_algorithm(ok, currentTolerance)")
        # ...........................................................................
        getattr(self, attr).append("    if ok != 0:")
        getattr(self, attr).append("        ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)")
        getattr(self, attr).append("        currentTolerance = testTolerance2")
        getattr(self, attr).append("        ok = _solution_algorithm(ok, currentTolerance)")
        # ...........................................................................
        getattr(self, attr).append("    if ok != 0:")
        getattr(self, attr).append("        ops.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)")
        getattr(self, attr).append("        currentTolerance = testTolerance3")
        getattr(self, attr).append("        ok = _solution_algorithm(ok, currentTolerance)")
        # ...........................................................................
        getattr(self, attr).append("    if ok == 0:")
        getattr(self, attr).append("        currentDisp = ops.nodeDisp(IDctrlNode, IDctrlDOF)")
        getattr(self, attr).append("        avect = ")
        getattr(self, attr)[-1] += " + ".join([f"ops.eleResponse({17000 + general['Reference'][i]}, 'forces')[{dof-1}]" for i in range(len(general['Reference']))])
        getattr(self, attr).append("        if avect < 0:")
        getattr(self, attr).append("            avect = -1*avect")
        getattr(self, attr).append("    else:")
        getattr(self, attr).append("        break")
        getattr(self, attr).append("    if avect < 50000:")
        getattr(self, attr).append("        pass")
        getattr(self, attr).append("    else:")
        getattr(self, attr).append("        break")
        getattr(self, attr).append("    if avect < 100:")
        getattr(self, attr).append("        avect = 0")
        getattr(self, attr).append("    if avect >= maxavect:")
        getattr(self, attr).append("        maxavect = avect + 0")
        getattr(self, attr).append("    else:")
        getattr(self, attr).append("        if avect >= 0.20*maxavect:")
        getattr(self, attr).append("            pass")
        getattr(self, attr).append("        else:")
        getattr(self, attr).append("            Tagum1 = 1")
        # ...........................................................................
        getattr(self, attr).append("    if currentDisp < Dmax:")
        getattr(self, attr).append("        pass")
        getattr(self, attr).append("    else:")
        getattr(self, attr).append("        Tagum2 = 1")
        getattr(self, attr).append("    Tagum = Tagum1 + Tagum2")
        # ...........................................................................
        getattr(self, attr).append("ops.wipe()")
        getattr(self, attr).append(f"print('Pushover {direction} done...')")


class TclGenerator:

    def __init__(self):
        
        self.nodes = []
        self.joints = []
        self.columns = []
        self.beams_x = []
        self.beams_stair = []
        self.beams_y = []
        self.gravity = []
        self.modal = []
        self.solution_algorithm = []
        self.pushover_x = []
        self.pushover_y = []
        self.go_x = ["source Node.tcl", "source Joint.tcl",  "source Column.tcl", "source BeamX.tcl" , "source BeamStairs.tcl", "source BeamY.tcl", "source Gravity.tcl", "source Modal.tcl", "source PushoverX.tcl"]
        self.go_y = self.go_x.copy()
        self.go_y[-1] = "source PushoverY.tcl"

    def get_writable_opensees_model(self):

        writable = {
        'Node.tcl': "\n".join(self.nodes),
        'Joint.tcl': "\n".join(self.joints),
        'Column.tcl': "\n".join(self.columns),
        'BeamX.tcl': "\n".join(self.beams_x),
        'BeamStairs.tcl': "\n".join(self.beams_stair),
        'BeamY.tcl': "\n".join(self.beams_y),
        'Gravity.tcl': "\n".join(self.gravity),
        'Modal.tcl': "\n".join(self.modal),
        'SolutionAlgorithm.tcl': "\n".join(self.solution_algorithm),
        'PushoverX.tcl': "\n".join(self.pushover_x),
        'PushoverY.tcl': "\n".join(self.pushover_y),
        'GoX.tcl': "\n".join(self.go_x),
        'GoY.tcl': "\n".join(self.go_y)
        }

        return writable

    def compile_opensees_model(self, general, joint, column, beamX, beamStair, beamY):
        self.add_nodes(general, joint)
        self.add_joints(general, joint)
        self.add_columns(general, column)
        self.beams_x.append("uniaxialMaterial Elastic 101 1e+010")
        self.beams_x.append("geomTransf Linear 2 0 -1 0")
        self.add_beam(general, beamX, 'beams_x')
        self.add_beam(general, beamStair, 'beams_stair')
        self.beams_y.append("geomTransf Linear 3 1 0 0")
        self.add_beam(general, beamY, 'beams_y')
        self.add_gravity_analysis(beamX, beamStair, beamY)
        self.add_modal_analysis(general)
        self.add_solution_algorithm()
        self.add_pushover(general, "X")
        self.add_pushover(general, "Y")

    def add_nodes(self, general, joint):

        Coordsref = general['Coordsref']

        # Model initialisation
        self.nodes.append(f"# Building Layout: {general['BuildingTYPE']}")
        self.nodes.append("wipe")
        self.nodes.append("model BasicBuilder -ndm 3 -ndf 6")

        # Structural Nodes
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Structural Nodes")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for node in Coordsref:
            self.nodes.append(f"node {node[0]:.0f} {node[1]:4.2f} {node[2]:4.2f} {node[3]:4.2f}")

        # Single-point constraints: Fix base nodes
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Supports")
        self.nodes.append("# ---------------------------------------------------------------------------")
        nodes2fix = Coordsref[(Coordsref[:, 0] < 100)]
        for node in nodes2fix:
            self.nodes.append(f"fix {node[0]:.0f} 1 1 1 1 1 1")
            self.nodes.append(f"node {7000 + node[0]:.0f} {node[1]:4.2f} {node[2]:4.2f} {node[3]:4.2f}")
            self.nodes.append(f"node {17000 + node[0]:.0f} {node[1]:4.2f} {node[2]:4.2f} {node[3]:4.2f}")

        # Complementary Joint Nodes
        joint1000 = joint['nodes'][:, 0:4]
        joint2000 = joint['nodes'][:, 4:8]
        joint3000 = joint['nodes'][:, 8:12]
        joint4000 = joint['nodes'][:, 12:16]
        joint5000 = joint['nodes'][:, 16:20]
        joint6000 = joint['nodes'][:, 20:24]
        joint7000 = joint['nodes'][:, 24:28]
        FlagHXY = joint['Data'][:, 7]
        FlagBEAMXleft = joint['Data'][:, 8]
        FlagBEAMXright = joint['Data'][:, 9]
        FlagBEAMYleft = joint['Data'][:, 10]
        FlagBEAMYright = joint['Data'][:, 11]

        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Nodes for the joint spring created to account for joint flexibility")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for i, j in enumerate(joint1000):
            self.nodes.append(f"node {j[0]:.0f} {j[1]:4.2f} {j[2]:4.2f} {j[3]:4.2f}")

        # Joint Rigid Elements - Ground
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Some stuff for the rigid elements")
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("geomTransf Linear 99999 -1 0 0")
        self.nodes.append("geomTransf Linear 88888 0 -1 0")
        self.nodes.append("geomTransf Linear 77777 1 0 0")
        self.nodes.append("set rigM 66666")
        self.nodes.append("uniaxialMaterial Elastic $rigM 1.e9")
        self.nodes.append("section Aggregator 99999 $rigM P $rigM Vy $rigM Vz $rigM My $rigM Mz $rigM T")
        self.nodes.append("# All rigid nodes and elements")
        self.nodes.append("# Ground Spring")
        for node in nodes2fix:
            self.nodes.append(f"equalDOF {node[0]:.0f} {7000 + node[0]:.0f} 1 2 3 4 5 6")

        # Joint Rigid Elements - Offsets
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Joint Offsets")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for i in range(joint['nodes'].shape[0]):

            self.nodes.append(f"# Around node: {joint['nodes'][i, 0]:.0f}")
            if FlagHXY[i] == 1:
                self.nodes.append(f"node {joint2000[i, 0]:.0f} {joint2000[i, 1]:4.2f} {joint2000[i, 2]:4.2f} {joint2000[i, 3]:4.2f}")
                self.nodes.append(f"node {joint7000[i, 0]:.0f} {joint7000[i, 1]:4.2f} {joint7000[i, 2]:4.2f} {joint7000[i, 3]:4.2f}")
                self.nodes.append(f"node {10000 + joint2000[i, 0]:.0f} {joint2000[i, 1]:4.2f} {joint2000[i, 2]:4.2f} {joint2000[i, 3]:4.2f}")
                self.nodes.append(f"node {10000 + joint7000[i, 0]:.0f} {joint7000[i, 1]:4.2f} {joint7000[i, 2]:4.2f} {joint7000[i, 3]:4.2f}")
                self.nodes.append(f"element elasticBeamColumn {joint2000[i, 0]:.0f} {joint2000[i, 0]:.0f} {joint['Data'][i, 0]:.0f} 1 30000000 15000000 1 1 1 99999")
                self.nodes.append(f"element elasticBeamColumn {joint7000[i, 0]:.0f} {joint['Data'][i, 0]:.0f} {joint7000[i, 0]:.0f} 1 30000000 15000000 1 1 1 99999")
            else:
                self.nodes.append(f"node {joint2000[i, 0]:.0f} {joint2000[i, 1]:4.2f} {joint2000[i, 2]:4.2f} {joint2000[i, 3]:4.2f}")
                self.nodes.append(f"node {10000 + joint2000[i, 0]:.0f} {joint2000[i, 1]:4.2f} {joint2000[i, 2]:4.2f} {joint2000[i, 3]:4.2f}")
                self.nodes.append(f"element elasticBeamColumn {joint2000[i, 0]:.0f} {joint2000[i, 0]:.0f} {joint['Data'][i, 0]:.0f} 1 30000000 15000000 1 1 1 99999")

            if FlagBEAMXleft[i] == 1:
                self.nodes.append(f"node {joint5000[i, 0]:.0f} {joint5000[i, 1]:4.2f} {joint5000[i, 2]:4.2f} {joint5000[i, 3]:4.2f}")
                self.nodes.append(f"node {10000 + joint5000[i, 0]:.0f} {joint5000[i, 1]:4.2f} {joint5000[i, 2]:4.2f} {joint5000[i, 3]:4.2f}")
                self.nodes.append(f"element elasticBeamColumn {joint5000[i, 0]:.0f} {joint5000[i, 0]:.0f} {joint['Data'][i, 0]:.0f} 1 30000000 15000000 1 1 1 88888")

            if FlagBEAMXright[i] == 1:
                self.nodes.append(f"node {joint3000[i, 0]:.0f} {joint3000[i, 1]:4.2f} {joint3000[i, 2]:4.2f} {joint3000[i, 3]:4.2f}")
                self.nodes.append(f"node {10000 + joint3000[i, 0]:.0f} {joint3000[i, 1]:4.2f} {joint3000[i, 2]:4.2f} {joint3000[i, 3]:4.2f}")
                self.nodes.append(f"element elasticBeamColumn {joint3000[i, 0]:.0f} {joint['Data'][i, 0]:.0f} {joint3000[i, 0]:.0f} 1 30000000 15000000 1 1 1 88888")

            if FlagBEAMYleft[i] == 1:
                self.nodes.append(f"node {joint6000[i, 0]:.0f} {joint6000[i, 1]:4.2f} {joint6000[i, 2]:4.2f} {joint6000[i, 3]:4.2f}")
                self.nodes.append(f"node {10000 + joint6000[i, 0]:.0f} {joint6000[i, 1]:4.2f} {joint6000[i, 2]:4.2f} {joint6000[i, 3]:4.2f}")
                self.nodes.append(f"element elasticBeamColumn {joint6000[i, 0]:.0f} {joint6000[i, 0]:.0f} {joint['Data'][i, 0]:.0f} 1 30000000 15000000 1 1 1 77777")
            
            if FlagBEAMYright[i] == 1:
                self.nodes.append(f"node {joint4000[i, 0]:.0f} {joint4000[i, 1]:4.2f} {joint4000[i, 2]:4.2f} {joint4000[i, 3]:4.2f}")
                self.nodes.append(f"node {10000 + joint4000[i, 0]:.0f} {joint4000[i, 1]:4.2f} {joint4000[i, 2]:4.2f} {joint4000[i, 3]:4.2f}")
                self.nodes.append(f"element elasticBeamColumn {joint4000[i, 0]:.0f} {joint['Data'][i, 0]:.0f} {joint4000[i, 0]:.0f} 1 30000000 15000000 1 1 1 77777")

        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Staircase")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for i in range(general['nstoreys']):
            self.nodes.append(f"node {joint['Lstair2000'][i, 0]:.0f} {joint['Lstair2000'][i, 1]:4.2f} {joint['Lstair2000'][i, 2]:4.2f} {joint['Lstair2000'][i, 3]:4.2f}")
            self.nodes.append(f"node {joint['Lstair7000'][i, 0]:.0f} {joint['Lstair7000'][i, 1]:4.2f} {joint['Lstair7000'][i, 2]:4.2f} {joint['Lstair7000'][i, 3]:4.2f}")
            self.nodes.append(f"node {joint['Rstair2000'][i, 0]:.0f} {joint['Rstair2000'][i, 1]:4.2f} {joint['Rstair2000'][i, 2]:4.2f} {joint['Rstair2000'][i, 3]:4.2f}")
            self.nodes.append(f"node {joint['Rstair7000'][i, 0]:.0f} {joint['Rstair7000'][i, 1]:4.2f} {joint['Rstair7000'][i, 2]:4.2f} {joint['Rstair7000'][i, 3]:4.2f}")
            self.nodes.append(f"node {joint['Lstair3000'][i, 0]:.0f} {joint['Lstair3000'][i, 1]:4.2f} {joint['Lstair3000'][i, 2]:4.2f} {joint['Lstair3000'][i, 3]:4.2f}")
            self.nodes.append(f"node {joint['Rstair5000'][i, 0]:.0f} {joint['Rstair5000'][i, 1]:4.2f} {joint['Rstair5000'][i, 2]:4.2f} {joint['Rstair5000'][i, 3]:4.2f}")

            self.nodes.append(f"node {10000 + joint['Lstair2000'][i, 0]:.0f} {joint['Lstair2000'][i, 1]:4.2f} {joint['Lstair2000'][i, 2]:4.2f} {joint['Lstair2000'][i, 3]:4.2f}")
            self.nodes.append(f"node {10000 + joint['Lstair7000'][i, 0]:.0f} {joint['Lstair7000'][i, 1]:4.2f} {joint['Lstair7000'][i, 2]:4.2f} {joint['Lstair7000'][i, 3]:4.2f}")
            self.nodes.append(f"node {10000 + joint['Rstair2000'][i, 0]:.0f} {joint['Rstair2000'][i, 1]:4.2f} {joint['Rstair2000'][i, 2]:4.2f} {joint['Rstair2000'][i, 3]:4.2f}")
            self.nodes.append(f"node {10000 + joint['Rstair7000'][i, 0]:.0f} {joint['Rstair7000'][i, 1]:4.2f} {joint['Rstair7000'][i, 2]:4.2f} {joint['Rstair7000'][i, 3]:4.2f}")
            self.nodes.append(f"node {10000 + joint['Lstair3000'][i, 0]:.0f} {joint['Lstair3000'][i, 1]:4.2f} {joint['Lstair3000'][i, 2]:4.2f} {joint['Lstair3000'][i, 3]:4.2f}")
            self.nodes.append(f"node {10000 + joint['Rstair5000'][i, 0]:.0f} {joint['Rstair5000'][i, 1]:4.2f} {joint['Rstair5000'][i, 2]:4.2f} {joint['Rstair5000'][i, 3]:4.2f}")
        
            self.nodes.append(f"element elasticBeamColumn {joint['Lstair2000'][i, 0]:.0f} {general['CoordsExtra1'][i, 0]:.0f} {joint['Lstair2000'][i, 0]:.0f} 1 30000000 15000000 1 1 1 99999")
            self.nodes.append(f"element elasticBeamColumn {joint['Lstair7000'][i, 0]:.0f} {general['CoordsExtra1'][i, 0]:.0f} {joint['Lstair7000'][i, 0]:.0f} 1 30000000 15000000 1 1 1 99999")
            self.nodes.append(f"element elasticBeamColumn {joint['Rstair2000'][i, 0]:.0f} {general['CoordsExtra2'][i, 0]:.0f} {joint['Rstair2000'][i, 0]:.0f} 1 30000000 15000000 1 1 1 99999")
            self.nodes.append(f"element elasticBeamColumn {joint['Rstair7000'][i, 0]:.0f} {general['CoordsExtra2'][i, 0]:.0f} {joint['Rstair7000'][i, 0]:.0f} 1 30000000 15000000 1 1 1 99999")
            self.nodes.append(f"element elasticBeamColumn {joint['Lstair3000'][i, 0]:.0f} {general['CoordsExtra1'][i, 0]:.0f} {joint['Lstair3000'][i, 0]:.0f} 1 30000000 15000000 1 1 1 88888")
            self.nodes.append(f"element elasticBeamColumn {joint['Rstair5000'][i, 0]:.0f} {general['CoordsExtra2'][i, 0]:.0f} {joint['Rstair5000'][i, 0]:.0f} 1 30000000 15000000 1 1 1 88888")
    
        # Calculates the centre of mass of the roof
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append(f"# Rigid diaphragms")
        self.nodes.append("# ---------------------------------------------------------------------------")
        masses = general['Masses2']
        positions = general['Plan']
        heights = general['Zvector'][1:]
        for i, mass in enumerate(masses):
            aux_x = mass * positions[:, 0]
            aux_y = mass * positions[:, 1]
            X = sum(aux_x)/sum(mass)
            Y = sum(aux_y)/sum(mass)
            self.nodes.append(f"node {100000*(i+1)+(i+1):.0f} {X:.6f} {Y:.6f} {heights[i]:.6f}")
            self.nodes.append(f"fix {100000*(i+1)+(i+1):.0f} 0 0 1 1 1 0")

        # Multi-point constraints: Rigid diaphragms
        self.nodes.append(f"set nstoreys {general['nstoreys']}")
        self.nodes.append("for {set x 1} {$x<=$nstoreys} {incr x} {")
        nodes = ["[expr 100000*$x+$x]"]
        for i in range(1, general['nonlin_diaph_nodeid_max'] + 1):
            nodes.append(f"[expr $x*100+{i}]")
        self.nodes.append("rigidDiaphragm 3 " + " ".join(nodes) + "")
        self.nodes.append("}")

        # Assign masses
        Masses = general['MassesQuasi']
        self.nodes.append("# ---------------------------------------------------------------------------")
        self.nodes.append("# Masses")
        self.nodes.append("# ---------------------------------------------------------------------------")
        for i in range(general['Coordsref'].shape[0]):
            self.nodes.append(f"mass {general['Coordsref'][i, 0]:.0f} {Masses[i]+0.01:4.3f} {Masses[i]+0.01:4.3f} 0.01 0.01 0.01 0.01")

        # # Add recorder for base shears and top displacement
        # self.nodes.append(f"# Base shear recorders")
        # recorder_nodes_reaction = " ".join([f"{node:.0f}" for node in general['Reference']])
        # self.nodes.append(f"recorder Node -file nodesR.out -node {recorder_nodes_reaction} -dof 1 reaction")
        # self.nodes.append(f"# Control node displacement recorder")
        # montoring_node = general['Reference'][-1] + general['nstoreys'] * 100
        # self.nodes.append(f"recorder Node -file nodeD.out -node {montoring_node:.0f} -dof 1 disp")
    
    def add_joints(self, general, joint):

        hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, gamm, P, Kspr = Common.preallocate_joint(joint, general)

        if general['BeamType'] == 1: # Rigid joints are imposed in the case of wide beams to force damage localization (""add reference""?????)--> Ask Nuno about this
            self.joints.append(f"# Rigid joints have been selected since DesignClass is {general['designlevel']} and wide beams are used")
            self.joints.append("set rigidM 100000")
            self.joints.append("uniaxialMaterial Elastic $rigidM 1.e15")
            for i in range(joint['Data'].shape[0]):
                self.joints.append(f"# Creating joint with central node {joint['Data'][i,0]:.0f}")
                self.joints.append(f"element zeroLength {10000+joint['Data'][i,0]:.0f} {joint['Data'][i,0]:.0f} {1000+joint['Data'][i,0]:.0f} -mat $rigidM $rigidM $rigidM $rigidM $rigidM $rigidM -dir 1 2 3 4 5 6 -orient 1 0 0 0 0 1")

        else: # defines joint type based on quality
            juntas = Common.get_joint_type(general['designlevel'], general['quality'])

            if juntas == 1: # Rigid joint
                self.joints.append(f"# Rigid joints have been selected for DesignClass: {general['designlevel']} and quality: {general['quality']}")
                self.joints.append("set rigidM 100000")
                self.joints.append("uniaxialMaterial Elastic $rigidM 1.e9")
                for i in range(joint['Data'].shape[0]):
                    self.joints.append(f"# Creating joint with central node {joint['Data'][i,0]:.0f}")
                    self.joints.append(f"element zeroLength {10000+joint['Data'][i,0]:.0f} {joint['Data'][i,0]:.0f} {1000+joint['Data'][i,0]:.0f} -mat $rigidM $rigidM $rigidM $rigidM $rigidM $rigidM -dir 1 2 3 4 5 6")
            
            elif juntas == 2: # Elastic joint 
                self.joints.append(f"# Elastic joints have been selected for DesignClass: {general['designlevel']} and quality: {general['quality']}")
                self.joints.append("set rigidM 100000")
                self.joints.append("uniaxialMaterial Elastic $rigidM 1.00e12")

                for i in range(joint['Data'].shape[0]):
                    MEjX1, MEjY1 = Common.get_elastic_joint(hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, general['hstorey'], P, i)

                    self.joints.append(f"# Creating joint with central node {joint['Data'][i,0]:.0f}")
                    self.joints.append(f"uniaxialMaterial Elastic {200000+joint['Data'][i, 0]:.0f} {Kspr[i]:4.6f}")
                    self.joints.append(f"uniaxialMaterial Elastic {300000+joint['Data'][i, 0]:.0f} {MEjX1/0.0002:4.6f}")
                    self.joints.append(f"uniaxialMaterial Elastic {400000+joint['Data'][i, 0]:.0f} {MEjY1/0.0002:4.6f}")
                    self.joints.append(f"section Aggregator {10000+joint['Data'][i, 0]:.0f} $rigidM P $rigidM Vy $rigidM Vz {400000+joint['Data'][i, 0]:.0f} My {300000+joint['Data'][i, 0]:.0f} Mz $rigidM T")
                    self.joints.append(f"element zeroLengthSection {1000+joint['Data'][i, 0]:.0f} {1000+joint['Data'][i, 0]:.0f} {joint['Data'][i, 0]:.0f} {10000+joint['Data'][i, 0]:.0f} -orient 0 0 1 0 1 0")

            elif juntas == 3: # Flexible nonlinear joint joint
                self.joints.append(f"# Rigid joints have been selected for DesignClass: {general['designlevel']} and quality: {general['quality']}")
                self.joints.append("set rigidM 100000")
                self.joints.append("uniaxialMaterial Elastic $rigidM 1.e9")

                for i in range(joint['Data'].shape[0]):
                    MjX1, MjX2, MjX3, MjX4, MjX5, MjX6, MjY1, MjY2, MjY3, MjY4, MjY5, MjY6 = Common.get_inelastic_joint(hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, general['hstorey'], P, i)

                    self.joints.append(f"# Creating joint with central node {joint['Data'][i,0]:.0f}")
                    self.joints.append(f"uniaxialMaterial Elastic {200000+joint['Data'][i,0]:.0f} {Kspr[i]:4.6f}")
                    self.joints.append(f"uniaxialMaterial Hysteretic {300000+joint['Data'][i,0]:.0f} {MjX1:4.6f} {gamm[0]:4.6f} {1.1*MjX2:4.6f} {gamm[1]:4.6f} {MjX3:4.6f} {gamm[2]:4.6f} {-MjX4:4.6f} {-gamm[3]:4.6f} {-1.1*MjX5:4.6f} {-gamm[4]:4.6f} {-MjX6:4.6f} {-gamm[5]:4.6f} 0 0 0 0 0") # hyst_int[0] hyst_int[1] hyst_int[2] hyst_int[3] hyst_int[4]")
                    self.joints.append(f"uniaxialMaterial Hysteretic {400000+joint['Data'][i,0]:.0f} {MjY1:4.6f} {gamm[0]:4.6f} {1.1*MjY2:4.6f} {gamm[1]:4.6f} {MjY3:4.6f} {gamm[2]:4.6f} {-MjY4:4.6f} {-gamm[3]:4.6f} {-1.1*MjY5:4.6f} {-gamm[4]:4.6f} {-MjY6:4.6f} {-gamm[5]:4.6f} 0 0 0 0 0") # hyst_int[0] hyst_int[1] hyst_int[2] hyst_int[3] hyst_int[4]")
                    self.joints.append(f"element zeroLength {1000+joint['Data'][i,0]:.0f} {joint['Data'][i,0]:.0f} {1000+joint['Data'][i,0]:.0f} -mat $rigidM $rigidM $rigidM {400000+joint['Data'][i,0]:.0f} {300000+joint['Data'][i,0]:.0f} $rigidM -dir 1 2 3 4 5 6")

    def add_columns(self, general, column):

        for i in range(len(column['Name'])):
            # Get inputs for plastic hinge
            comments, geomtransf, matflex, matshear, cdh_ele_inputs, notcdh_shear_inputsX, notcdh_shear_inputsY, noncdh_ele_inputs = Common.get_column_concentrated_plasticity(column, i)
            # ...........................................................................           
            geomtransf_text = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(geomtransf)])
            mat_flexXtop = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matflex[0])])
            mat_flexXbot = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matflex[1])])
            mat_flexYtop = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matflex[2])])
            mat_flexYbot = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matflex[3])])
            # mattag_ShearXbot = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matshear[0])])
            # mattag_ShearXtop = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matshear[1])])
            # mattag_ShearYbot = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matshear[2])])
            # mattag_ShearYtop = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(matshear[3])])
            # ...........................................................................
            # Writes the OpenSees column model including all the nodes, springs and materials necessary for the definition of the column
            self.columns.extend(comments)
            self.columns.append(f"geomTransf PDelta {geomtransf_text}")
            self.columns.append(f"uniaxialMaterial Hysteretic {mat_flexXtop}")
            self.columns.append(f"uniaxialMaterial Hysteretic {mat_flexXbot}")
            self.columns.append(f"uniaxialMaterial Hysteretic {mat_flexYtop}")
            self.columns.append(f"uniaxialMaterial Hysteretic {mat_flexYbot}")
            # self.columns.append(f"uniaxialMaterial Hysteretic {mattag_ShearXbot}")
            # self.columns.append(f"uniaxialMaterial Hysteretic {mattag_ShearXtop}")
            # self.columns.append(f"uniaxialMaterial Hysteretic {mattag_ShearYbot}")
            # self.columns.append(f"uniaxialMaterial Hysteretic {mattag_ShearYtop}")
            # ...........................................................................
            zero1_text = " ".join([f"{item:.0f}" for item in cdh_ele_inputs[2]])
            ele_text = " ".join([f"{item:.0f}" if j in [0, 1, 2, 9] else f"{item:4.6f}" for j, item in enumerate(cdh_ele_inputs[3])])
            zero2_text = " ".join([f"{item:.0f}" for item in cdh_ele_inputs[4]])
            # Even though capacity design for shear is not followed during design of CDH, it is assummed that there is no shear failure.
            # Therefore, shear springs are rigid. But they are nonlinear for other design classes. 
            # TODO: I think we need to do smth about the capacity design issue. At least consider during the design
            # if general['designlevel'] in ['CDH', 'CDM']:
            if general['designlevel'] == 'CDH':
                self.columns.append(f"section Aggregator {cdh_ele_inputs[0][0]:.0f} $rigM P $rigM Vy $rigM Vz {cdh_ele_inputs[0][1]:.0f} My {cdh_ele_inputs[0][2]:.0f} Mz $rigM T") # it has been corrected MyX will resist loads from XX pushover or Myy HMA
                self.columns.append(f"section Aggregator {cdh_ele_inputs[1][0]:.0f} $rigM P $rigM Vy $rigM Vz {cdh_ele_inputs[1][1]:.0f} My {cdh_ele_inputs[1][2]:.0f} Mz $rigM T") # it has been corrected  HMA
                self.columns.append(f"element zeroLengthSection {zero1_text} -orient 0 0 1 0 1 0")
                self.columns.append(f"element elasticBeamColumn {ele_text}")
                self.columns.append(f"element zeroLengthSection {zero2_text} -orient 0 0 1 0 1 0")
            else:
                curve_Xtop_text =  " ".join([f"{item:.0f}" if j in [0, 1, 10, 11, 12, 13, 14, 15] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsX[0])])
                limitstate_Xtop_text = " ".join([f"{item:.0f}" if j in [0, 18, 19] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsX[1])])
                curve_Xbot_text =  " ".join([f"{item:.0f}" if j in [0, 1, 10, 11, 12, 13, 14, 15] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsX[2])])
                limitstate_Xbot_text = " ".join([f"{item:.0f}" if j in [0, 18, 19] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsX[3])])
                curve_Ytop_text =  " ".join([f"{item:.0f}" if j in [0, 1, 10, 11, 12, 13, 14, 15] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsY[0])])
                limitstate_Ytop_text = " ".join([f"{item:.0f}" if j in [0, 18, 19] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsY[1])])
                curve_Ybot_text =  " ".join([f"{item:.0f}" if j in [0, 1, 10, 11, 12, 13, 14, 15] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsY[2])])
                limitstate_Ybot_text = " ".join([f"{item:.0f}" if j in [0, 18, 19] else f"{item:4.6f}" for j, item in enumerate(notcdh_shear_inputsY[3])])

                self.columns.append(f"limitCurve ThreePoint {curve_Xtop_text}")
                self.columns.append(f"uniaxialMaterial LimitState {limitstate_Xtop_text}")
                self.columns.append(f"limitCurve ThreePoint {curve_Xbot_text}")
                self.columns.append(f"uniaxialMaterial LimitState {limitstate_Xbot_text}")
                self.columns.append(f"limitCurve ThreePoint {curve_Ytop_text}")
                self.columns.append(f"uniaxialMaterial LimitState {limitstate_Ytop_text}")
                self.columns.append(f"limitCurve ThreePoint {curve_Ybot_text}")
                self.columns.append(f"uniaxialMaterial LimitState {limitstate_Ybot_text}")
                self.columns.append(f"section Aggregator {noncdh_ele_inputs[0][0]:.0f} $rigM P {noncdh_ele_inputs[0][1]:.0f} Vy {noncdh_ele_inputs[0][2]:.0f} Vz {noncdh_ele_inputs[0][3]:.0f} My {noncdh_ele_inputs[0][4]:.0f} Mz $rigM T") # it has been corrected HMA
                self.columns.append(f"section Aggregator {noncdh_ele_inputs[1][0]:.0f} $rigM P {noncdh_ele_inputs[1][1]:.0f} Vy {noncdh_ele_inputs[1][2]:.0f} Vz {noncdh_ele_inputs[1][3]:.0f} My {noncdh_ele_inputs[1][4]:.0f} Mz $rigM T") # it has been corrected HMA
                self.columns.append(f"element zeroLengthSection {zero1_text} -orient 0 0 1 0 1 0")
                self.columns.append(f"element elasticBeamColumn {ele_text}")
                self.columns.append(f"element zeroLengthSection {zero2_text} -orient 0 0 1 0 1 0")

    def add_beam(self, general, beam, attr):
        
        if attr == 'beams_x':
            tag = "X"
            geo_transf_tag = 2
            mat_dir = 5
            equal_dof_4th = 4
        elif attr == 'beams_y':
            tag = "Y"
            geo_transf_tag = 3
            mat_dir = 4
            equal_dof_4th = 5
        elif attr == 'beams_stair':
            tag = "Stair"
            geo_transf_tag = 2
            mat_dir = 5
            equal_dof_4th = 4

        for i in range(len(beam['Name'])):

            left_mat, right_mat, beam_ele, left_spring, right_spring, equaldof_left, equaldof_right = Common.get_beam_concentrated_plasticity(general, beam, i)
            left_mat_text = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(left_mat)])
            right_mat_text = " ".join([f"{item:.0f}" if j == 0 else f"{item:4.6f}" for j, item in enumerate(right_mat)])
            beam_ele_text = " ".join([f"{item:.0f}" if j in [0, 1, 2] else f"{item:4.6f}" for j, item in enumerate(beam_ele)])
            getattr(self, attr).append(f"# Beam{tag} {beam_ele[0]:.0f} {general['designlevel']} Linear")
            getattr(self, attr).append(f"uniaxialMaterial Hysteretic {left_mat_text} 0.8 0.2 0.0 0.0 0.85")
            getattr(self, attr).append(f"uniaxialMaterial Hysteretic {right_mat_text} 0.8 0.2 0.0 0.0 0.85")
            getattr(self, attr).append(f"element elasticBeamColumn {beam_ele_text} {geo_transf_tag}")
            getattr(self, attr).append(f"element zeroLength {left_spring[0]:.0f} {left_spring[1]:.0f} {left_spring[2]:.0f} -mat {left_spring[3]:.0f} -dir {mat_dir}")
            getattr(self, attr).append(f"element zeroLength {right_spring[0]:.0f} {right_spring[1]:.0f} {right_spring[2]:.0f} -mat {right_spring[3]:.0f} -dir {mat_dir}")
            getattr(self, attr).append(f"equalDOF {equaldof_left[0]:.0f} {equaldof_left[1]:.0f} 1 2 3 {equal_dof_4th} 6")
            getattr(self, attr).append(f"equalDOF {equaldof_right[0]:.0f} {equaldof_right[1]:.0f} 1 2 3 {equal_dof_4th} 6")

    def add_gravity_analysis(self, beamX, beamStair, beamY):
        
        # Add gravity loads
        self.gravity.append("pattern Plain 1 Constant {")
        self.gravity.append("# loading BeamsX")
        for i in range(len(beamX['pedEQ'])):
            self.gravity.append(f"eleLoad -ele {beamX['Name'][i]:.0f} -type -beamUniform {-1*beamX['pedEQ'][i]:4.1f} 0")
        self.gravity.append("# loading BeamsY")

        for i in range(len(beamY['pedEQ'])):
            self.gravity.append(f"eleLoad -ele {beamY['Name'][i]:.0f} -type -beamUniform {-1*beamY['pedEQ'][i]:4.1f} 0")
        self.gravity.append("# loading BeamsStair")

        for i in range(len(beamStair['pedEQ'])):
            self.gravity.append(f"eleLoad -ele {beamStair['Name'][i]:.0f} -type -beamUniform {-1*beamStair['pedEQ'][i]:4.1f} 0")
        self.gravity.append("}")

        # Perform gravity analysis
        self.gravity.append("# Perform gravity analysis")
        self.gravity.append("system UmfPack")
        self.gravity.append("numberer RCM")
        self.gravity.append("constraints Transformation")
        self.gravity.append("test NormDispIncr 1e-06 6")
        self.gravity.append("integrator LoadControl 1")
        self.gravity.append("algorithm Linear")
        self.gravity.append("analysis Static")
        self.gravity.append("analyze 1")
        self.gravity.append("puts \"Gravity analysis complete..\"")
        self.gravity.append("loadConst -time 0.0") # loadConst <-time $pseudoTime>

    def add_modal_analysis(self, general):

        # Perform modal analysis
        self.modal.append("puts \"Wait a second... Ready to go for modal analysis...\"")
        self.modal.append("set Modal Modal")        
        self.modal.append("file mkdir $Modal")  
        self.modal.append("eigen 3")
        self.modal.append("modalProperties -print -file \"Modal/ModalReport.txt\" -unorm")
        # self.modal.append("set periods \"Modal/Periods.txt\"") 
        # self.modal.append("set eigenValues [eigen 3]")
        # self.modal.append("set PPeriods [open $periods \"w\"]")
        # self.modal.append("puts \"Eigenvalues:\"")
        # self.modal.append("set pi 3.141596")
        # self.modal.append("set eigenValue [lindex $eigenValues 0]")
        # self.modal.append("set T1 [expr 2*$pi/sqrt($eigenValue)]")        
        # self.modal.append("puts \"T[expr 0+1] = [expr 2.*$pi/sqrt($eigenValue)]\"") 
        # self.modal.append("puts $PPeriods \"$T1\"") 
        # self.modal.append("set eigenValue [lindex $eigenValues 1]") 
        # self.modal.append("set T2 [expr 2*$pi/sqrt($eigenValue)]")      
        # self.modal.append("puts \"T[expr 1+1] = [expr 2.*$pi/sqrt($eigenValue)]\"") 
        # self.modal.append("puts $PPeriods \"$T2\"") 
        # self.modal.append("set eigenValue [lindex $eigenValues 2]") 
        # self.modal.append("set T3 [expr 2*$pi/sqrt($eigenValue)]")      
        # self.modal.append("puts \"T[expr 2+1] = [expr 2.*$pi/sqrt($eigenValue)]\"") 
        # self.modal.append("puts $PPeriods \"$T3\"")
        # self.modal.append("close $PPeriods") 
        self.modal.append("puts \"Modal Analysis Done\"")
        self.modal.append("set eivecs1 \"./Modal/eivecs1.txt\"; set EEivecs1 [open $eivecs1 \"w\"]")
        for j in range(general['nstoreys']):
            self.modal.append(f"set f [nodeEigenvector {(j+1)*100000+(j+1):.0f} 1]; puts $EEivecs1 \"$f\"")
        self.modal.append("set eivecs2 \"./Modal/eivecs2.txt\"; set EEivecs2 [open $eivecs2 \"w\"]")
        for j in range(general['nstoreys']):
            self.modal.append(f"set f [nodeEigenvector {(j+1)*100000+(j+1):.0f} 2]; puts $EEivecs2 \"$f\"")
        self.modal.append("set eivecs3 \"./Modal/eivecs3.txt\"; set EEivecs3 [open $eivecs3 \"w\"]")
        for j in range(general['nstoreys']):
            self.modal.append(f"set f [nodeEigenvector {(j+1)*100000+(j+1):.0f} 3]; puts $EEivecs3 \"$f\"")
        self.modal.append("close $EEivecs1; close $EEivecs2; close $EEivecs3") 

    def add_solution_algorithm(self):
        
        self.solution_algorithm.append("if {$ok != 0} {")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm KrylovNewton")
        self.solution_algorithm.append("set ok [analyze 1]")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm Newton -initial")
        self.solution_algorithm.append("}")
        self.solution_algorithm.append("if {$ok != 0} {")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm NewtonLineSearch 0.1")
        self.solution_algorithm.append("set ok [analyze 1]")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm Newton")
        self.solution_algorithm.append("}")
        self.solution_algorithm.append("if {$ok != 0} {")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm Broyden 50")
        self.solution_algorithm.append("set ok [analyze 1]")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm Newton")
        self.solution_algorithm.append("}")
        self.solution_algorithm.append("if {$ok != 0} {")
        self.solution_algorithm.append("test NormDispIncr   $currentTolerance 10")
        self.solution_algorithm.append("algorithm ModifiedNewton")
        self.solution_algorithm.append("set ok [analyze 1]")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm Newton")
        self.solution_algorithm.append("}")
        self.solution_algorithm.append("if {$ok != 0} {")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm BFGS")
        self.solution_algorithm.append("set ok [analyze 1]")
        self.solution_algorithm.append("test NormDispIncr $currentTolerance 10")
        self.solution_algorithm.append("algorithm Newton")
        self.solution_algorithm.append("}")

    def add_pushover(self, general, direction):
        
        # variables associated with direction
        if direction == "X":
            folder_name = "PUSH_X"
            dof = 1
            attr = 'pushover_x'
        elif direction == "Y":
            folder_name = "PUSH_Y"
            dof = 2
            attr = 'pushover_y'
        # ...........................................................................
        # Get mass proportional loads and storey heights
        Fi, Hi = Common.get_pushover_loads(general)
        # ...........................................................................
        getattr(self, attr).append(f"file mkdir {folder_name}")
        getattr(self, attr).append("# LATERAL-LOAD distribution for static pushover analysis")
        getattr(self, attr).append("# Calculate distribution of lateral load based on mass/weight distributions along building height")
        getattr(self, attr).append("# Fj = WjHj/sum(WiHi) * Weight at each floor j")
        getattr(self, attr).append("pattern Plain 200 Linear {")
        for j in range(general['nstoreys']):
            if direction == "X":
                getattr(self, attr).append(f"load {(j+1)*100000+(j+1):.0f} {Fi[j]:4.6f} 0.0 0.0 0.0 0.0 0.0")
            elif direction == "Y":
                getattr(self, attr).append(f"load {(j+1)*100000+(j+1):.0f} 0.0 {Fi[j]:4.6f} 0.0 0.0 0.0 0.0") 

        getattr(self, attr).append("}")
        # ...........................................................................
        montoringnode = 100000*general['nstoreys'] + general['nstoreys']
        getattr(self, attr).append(f"recorder Node -file {folder_name}/nodeD.out -node {montoringnode:.0f} -dof {dof} disp")
        getattr(self, attr).append(f"recorder Drift -file {folder_name}/drifts.out -iNode ")
        getattr(self, attr)[-1] += " ".join([f"{general['Reference'][-1] + i*100}" for i in range(general['nstoreys'])])
        getattr(self, attr)[-1] += " -jNode "
        getattr(self, attr)[-1] += " ".join([f"{general['Reference'][-1] + i*100}" for i in range(1, general['nstoreys'] + 1)])
        getattr(self, attr)[-1] += f" -dof {dof} -perpDirn 3"
        getattr(self, attr).append(f"recorder Node -file {folder_name}/nodesR.out -node ")
        getattr(self, attr)[-1] += " ".join([f"{7000 + general['Reference'][i]}" for i in range(len(general['Reference']))])
        getattr(self, attr)[-1] += f" -dof {dof} reaction"
        # ...........................................................................
        getattr(self, attr).append("set testTolerance0 1.0e-5")
        getattr(self, attr).append("set testTolerance1 1.0e-4")
        getattr(self, attr).append("set testTolerance2 1.0e-3")
        getattr(self, attr).append("set testTolerance3 1.0e-2")
        getattr(self, attr).append("# Perform static horizontal analysis")
        getattr(self, attr).append("system UmfPack")
        getattr(self, attr).append("numberer RCM")
        getattr(self, attr).append("constraints Penalty 10e9 10e9")
        getattr(self, attr).append("test NormDispIncr $testTolerance0 30 0")
        getattr(self, attr).append(f"set IDctrlNode {montoringnode:.0f}")
        getattr(self, attr).append(f"set IDctrlDOF {dof}")
        getattr(self, attr).append(f"set Dmax {0.06*Hi[-1]:4.3f}")
        getattr(self, attr).append("set Dincr [expr 0.001]")
        getattr(self, attr).append("integrator DisplacementControl $IDctrlNode $IDctrlDOF $Dincr")                                                
        getattr(self, attr).append("algorithm Newton")
        getattr(self, attr).append("analysis Static")
        getattr(self, attr).append("set currentTolerance $testTolerance0")
        getattr(self, attr).append("set currentTime 0")
        getattr(self, attr).append("set ok 0")
        getattr(self, attr).append("set avect 0")
        getattr(self, attr).append("set currentDisp [nodeDisp $IDctrlNode $IDctrlDOF]")
        getattr(self, attr).append(f"set currentDrift [expr 100*$currentDisp/{Hi[-1]:4.3f}]")
        getattr(self, attr).append("set Tagum 0")
        getattr(self, attr).append("set Tagum1 0")
        getattr(self, attr).append("set Tagum2 0")
        getattr(self, attr).append("set maxavect 0")
        # ...........................................................................
        getattr(self, attr).append("while {$ok == 0 && $Tagum==0} {")
        getattr(self, attr).append("test NormDispIncr $currentTolerance 10 0")
        getattr(self, attr).append("set ok [analyze 1]")
        getattr(self, attr).append("if {$ok != 0} {")
        getattr(self, attr).append("set Dincr [expr 0.001]")
        getattr(self, attr).append("integrator DisplacementControl $IDctrlNode $IDctrlDOF $Dincr")
        getattr(self, attr).append("set currentTolerance [expr $testTolerance0]")
        getattr(self, attr).append("source SolutionAlgorithm.tcl")
        getattr(self, attr).append("}")
        # ...........................................................................
        getattr(self, attr).append("if {$ok != 0} {")
        getattr(self, attr).append("set currentTolerance [expr $testTolerance1]")
        getattr(self, attr).append("source SolutionAlgorithm.tcl")
        getattr(self, attr).append("}")
        # ...........................................................................
        getattr(self, attr).append("if {$ok != 0} {")
        getattr(self, attr).append("set currentTolerance [expr $testTolerance2]")
        getattr(self, attr).append("source SolutionAlgorithm.tcl")
        getattr(self, attr).append("}")
        # ...........................................................................
        getattr(self, attr).append("if {$ok != 0} {")
        getattr(self, attr).append("set currentTolerance [expr $testTolerance3]")
        getattr(self, attr).append("source SolutionAlgorithm.tcl")
        getattr(self, attr).append("}")
        # ...........................................................................
        getattr(self, attr).append("if {$ok == 0} {")
        getattr(self, attr).append("set currentDisp [nodeDisp $IDctrlNode $IDctrlDOF]")
        getattr(self, attr).append("set avect [expr ")
        getattr(self, attr)[-1] += "+".join([f"[lindex [eleResponse {17000 + general['Reference'][i]} forces] {dof-1}]" for i in range(len(general['Reference']))])
        getattr(self, attr)[-1] += "]"
        getattr(self, attr).append("if {$avect<0} {set avect [expr -1.*$avect]}")
        getattr(self, attr).append("} else {")
        getattr(self, attr).append("return")
        getattr(self, attr).append("}")
        getattr(self, attr).append("if {$avect<50000} {")
        getattr(self, attr).append("} else {")
        getattr(self, attr).append("return")
        getattr(self, attr).append("}")
        getattr(self, attr).append("if {$avect<100} {set avect 0}")
        getattr(self, attr).append("if {$avect >= $maxavect} {")
        getattr(self, attr).append("set maxavect $avect")
        getattr(self, attr).append("} else {")
        getattr(self, attr).append("if {$avect >= [expr 0.20*$maxavect]} {")
        getattr(self, attr).append("} else {")
        getattr(self, attr).append("set Tagum1 1")
        getattr(self, attr).append("}")
        getattr(self, attr).append("}")     
        # ...........................................................................
        getattr(self, attr).append("if {$currentDisp<$Dmax} {")
        getattr(self, attr).append("} else {")
        getattr(self, attr).append("set Tagum2 1")
        getattr(self, attr).append("}")
        getattr(self, attr).append("set Tagum [expr $Tagum1+$Tagum2]")
        # ...........................................................................
        getattr(self, attr).append("}")
        getattr(self, attr).append("wipe all")
        getattr(self, attr).append(f"puts \"Pushover {direction} done...\"")
        getattr(self, attr).append("exit")


class Common:

    def get_pushover_loads(general):
        # Mass proportional pushover
        masses = general['Masses']
        Hi = general['Zvector'][1:]
        Wi = []
        for i in range(general['nstoreys']):
            Wi.append(9.81*sum(masses[i,:]))
        SumWiHi = sum(np.array(Wi) * np.array(Hi))
        Fi = [sum(Wi)*Wi[i]*Hi[i]/SumWiHi for i in range(general['nstoreys'])]
        # Fi = [Wi[i]*Hi[i]/SumWiHi for i in range(general['nstoreys'])] # sum(Wi) could be removed

        return Fi, Hi

    def get_beam_concentrated_plasticity(general, beam, i):
        
        nFactor = 10
        # Pre-alocate some stuff
        elenum = beam['Name'][i]
        nodeleft = beam['Nodei'][i]
        noderight = beam['Nodej'][i]

        B = beam['B'][i]
        H = beam['H'][i]
        L = beam['L'][i]  # I do not extract here the segments located inside the joints

        nbar_Top1 = beam['Ntopcorner1'][i]
        nbar_Top9 = beam['Ntopcorner9'][i]
        filongTop1 = beam['FItopcorner1'][i]  
        filongTop9 = beam['FItopcorner9'][i]

        nbar_Bot1 = beam['Nbotcorner1'][i]
        nbar_Bot9 = beam['Nbotcorner9'][i]
        filongBot1 = beam['FIbotcorner1'][i] 
        filongBot9 = beam['FIbotcorner9'][i] 

        nbar_Topint1 = beam['Ntopint1'][i]
        nbar_Topint9 = beam['Ntopint9'][i]
        filongTopint1 = beam['FItopint1'][i] 
        filongTopint9 = beam['FItopint9'][i]

        nbar_Botint1 = beam['Nbotint1'][i]
        nbar_Botint9 = beam['Nbotint9'][i]
        filongBotint1 = beam['FIbotint1'][i]
        filongBotint9 = beam['FIbotint9'][i]            

        rholong1 = ((nbar_Top1 * 0.25*np.pi*filongTop1**2) + (nbar_Topint1 * 0.25 * np.pi * filongTopint1**2) + (nbar_Bot1 * 0.25 * np.pi * filongBot1**2) + (nbar_Botint1 * 0.25 * np.pi * filongBotint1**2)) / (B*H)
        rholong9 = ((nbar_Top9 * 0.25*np.pi*filongTop9**2) + (nbar_Topint9 * 0.25 * np.pi * filongTopint9**2) + (nbar_Bot9 * 0.25 * np.pi * filongBot9**2) + (nbar_Botint9 * 0.25 * np.pi * filongBotint9**2)) / (B*H)

        fc = beam['fcm_Q'][i]
        fylong = 1.2 * beam['fsyl_Q'][i] # 1.2 to consider mean based on table 4.10 and table 4.14 from Wisniewski D (2007) PhD
        fyw = 1.2 * beam['fsyw_Q'][i] # 1.2 to consider mean based on table 4.10 and table 4.14 from Wisniewski D (2007) PhD
        cover = beam['cover_Q'][i]

        fiw1 = beam['FIw1'][i] 
        sw1 = beam['sw_Q1'][i] 
        nwparallel_to_h1 = beam['Nlegsyy1'][i]  
        fiw9 = beam['FIw9'][i] 
        sw9 = beam['sw_Q9'][i] 
        nwparallel_to_h9 = beam['Nlegsyy9'][i]

        sn1 = (sw1 / filongTop1) * (fylong / 100)**0.5
        sn9 = (sw9 / filongTop9) * (fylong / 100)**0.5

        bondslipfact = beam['bondslipfact_Q'][i]

        nodeleftspring = 10000 + nodeleft
        noderightspring = 10000 + noderight
        if general['ag'] <= 0.15:
            Ls = L/2 # Assuming Ls columns equal to 33% of the free length L of the element
        else: # TODO: These are the same, are we sure?
            Ls = L/2 # Assuming Ls columns equal to 50% of the free length L of the element

        Ec = 22000*(fc/10)**0.3
        Es = 202000
        ecu = 0.0035
        esy = fylong/Es
        stiffFactor1 = 10
        stiffFactor2 = (stiffFactor1+1)/stiffFactor1
        Iz = (B*H**3)/12
        Iy = (H*B**3)/12
        Ibeam_modz = Iz * stiffFactor2
        Ibeam_mody = Iy * stiffFactor2
        Jz = (H*B) * (H**2 + B**2)
        Abeam = H*B

        # My for Top reinforcement in tension
        # My calculations is done followign the  Panagiotakos and Fardis (ACI 2001; paper - page 137)                   
        # model following the Rough Spreadsheet to Compute the Yield Moment of an RC Column H Curt B. Haselton and Abbie B. Liel
        # i=0 for the section at theh left had side and 
        # i=8 for the cross-section located at the right-hand side of the beam
        My_Top1,My_Bot1,fiyTop1,fiyBot1,RatforRotBOT1 = Common.get_beam_my(H, B, cover, fiw1, nbar_Top1, nbar_Topint1, filongTop1, filongTopint1, nbar_Bot1, nbar_Botint1, filongBot1, filongBotint1, ecu, esy, fylong, fc, Es, Ec)
        My_Top9,My_Bot9,fiyTop9,fiyBot9,RatforRotBOT9 = Common.get_beam_my(H, B, cover, fiw9, nbar_Top9, nbar_Topint9, filongTop9, filongTopint9, nbar_Bot9, nbar_Botint9, filongBot9, filongBotint9, ecu, esy, fylong, fc, Es, Ec)
        # Calculate the parameters for the flexural spring component model following the Haselton et al 2016 approach
        # and the spreadsheet made available H Curt B. Haselton in his website.
        # Reference: Curt B. Haselton, Abbie B. Liel, Sarah C. Taylor-Lange, and Gregory G. Deierlein (2016)
        # Calibration of Model to Simulate Response of Reinforced Concrete Beam-Columns to Collapse. ACI Structural Journal 10.14359/51689245
        # thetay is calculated according to the Eurocode 8 - Part 3 proposal
        # tetacapXtot = 0.14 * (1+0.4*asl) * (0.19**niu) * ((0.02 + 40*roshX)**0.54) * (0.62**(0.01*fc))
        # tetacapYtot = 0.14 * (1+0.4*asl) * (0.19**niu) * ((0.02 + 40*roshY)**0.54) * (0.62**(0.01*fc))
        if fc < 27.6:
            betafc = 0.85
        elif fc > 55.17:
            betafc = 0.65
        else:
            betafc = 1.05 - 0.05*fc/6.9

        rosH1 = ((np.pi*(fiw1**2) * nwparallel_to_h1)/4) / (B * sw1)
        rosH9 = ((np.pi*(fiw9**2) * nwparallel_to_h9)/4) / (B * sw9)
        s_d1 = sw1 / (0.90 * H)
        s_d9 = sw9 / (0.90 * H)
        niu = 0         #  beams are assumed to have no axial load

        tetacap_pl1top = 0.12 * (1 + 0.55*bondslipfact) * (0.16**niu) * ((0.02 + 40*rosH1)**0.43) * (0.54**(0.01*1.0*fc)) * (0.66**(0.1*sn1)) * (2.27**(10.0*rholong1))
        tetacap_pl9top = 0.12 * (1 + 0.55*bondslipfact) * (0.16**niu) * ((0.02 + 40*rosH9)**0.43) * (0.54**(0.01*1.0*fc)) * (0.66**(0.1*sn9)) * (2.27**(10.0*rholong9))
        aux31top = 0.76 * (0.031**niu) * ((0.02 + 40*rosH1)**1.02)
        aux39top = 0.76 * (0.031**niu) * ((0.02 + 40*rosH9)**1.02)
        if aux31top >= 0.10:
            tetapc1top = 0.10
        else:
            tetapc1top = aux31top
        if aux39top >= 0.10:
            tetapc9top = 0.10
        else:
            tetapc9top = aux39top

        tetacap_pl1bot = RatforRotBOT1 * tetacap_pl1top
        tetacap_pl9bot = RatforRotBOT9 * tetacap_pl9top
        tetapc1bot = RatforRotBOT1 * tetapc1top
        tetapc9bot = RatforRotBOT9 * tetapc9top

        EIfact = 0.50
        E_mod = Ec*1000
        G_mod = E_mod/2.4
        McMy = 1.25 * (0.91**(0.01*fc))    
        Lambda = 30 * (0.3**niu)
        av = 1.0
        z = 0.81*H

        thetay1_1Top = fiyTop1 * ((Ls + (av*z))/3)
        thetay1_9Top = fiyTop9 * ((Ls + (av*z))/3)
        thetay1_1Bot = fiyBot1 * ((Ls + (av*z))/3)
        thetay1_9Bot = fiyBot9 * ((Ls + (av*z))/3)

        thetay3_1Top = 0.13 * fiyTop1 * filongTop1 * fylong / (fc**0.50)
        thetay3_9Top = 0.13 * fiyTop9 * filongTop9 * fylong / (fc**0.50)
        thetay3_1Bot = 0.13 * fiyBot1 * filongBot1 * fylong / (fc**0.50)
        thetay3_9Bot = 0.13 * fiyBot9 * filongBot9 * fylong / (fc**0.50)

        thetay2 = 0.0013 * (1 + 1.5*H/Ls)

        thetay_Top1 = thetay1_1Top + thetay2 + bondslipfact * thetay3_1Top
        thetay_Top9 = thetay1_9Top + thetay2 + bondslipfact * thetay3_9Top
        thetay_Bot1 = thetay1_1Bot + thetay2 + bondslipfact * thetay3_1Bot
        thetay_Bot9 = thetay1_9Bot + thetay2 + bondslipfact * thetay3_9Bot

        # Opensees printing
        teta1plus1 = thetay_Top1 / nFactor 
        teta2plus1 = thetay_Top1 / nFactor + 1 * tetacap_pl1top
        teta3plus1 = thetay_Top1 / nFactor + 1 * tetacap_pl1top + 1 * tetapc1top
        teta1neg1  = thetay_Bot1 / nFactor 
        teta2neg1  = thetay_Bot1 / nFactor + 1 * tetacap_pl1bot
        teta3neg1  = thetay_Bot1 / nFactor + 1 * tetacap_pl1bot + 1 * tetapc1bot

        teta1plus9 = thetay_Top9 / nFactor 
        teta2plus9 = thetay_Top9 / nFactor + tetacap_pl9top
        teta3plus9 = thetay_Top9 / nFactor + tetacap_pl9top + tetapc9top
        teta1neg9 = thetay_Bot9 / nFactor 
        teta2neg9 = thetay_Bot9 / nFactor + tetacap_pl9bot
        teta3neg9 = thetay_Bot9 / nFactor + tetacap_pl9bot + tetapc9bot

        left_mat = [nodeleftspring, My_Top1, teta1plus1, 1.13*My_Top1, teta2plus1, 0.10*McMy*My_Top1, teta3plus1, -My_Bot1, -teta1neg1, -1.13*My_Bot1, -teta2neg1, -0.10*McMy*My_Bot1, -teta3neg1] # Changed the residual force from 0.010*McMy*My to 0.010*McMy*My
        right_mat = [noderightspring, My_Top9, teta1plus9, 1.13*My_Top9, teta2plus9, 0.10*McMy*My_Top9, teta3plus9, -My_Bot9, -teta1neg9, -1.13*My_Bot9, -teta2neg9, -0.10*McMy*My_Bot9, -teta3neg9] # Changed the residual force from 0.010*McMy*My to 0.010*McMy*My
        beam_element = [elenum, nodeleftspring, noderightspring, Abeam, E_mod, G_mod, Jz, Ibeam_mody, Ibeam_modz]
        left_spring = [nodeleftspring, nodeleft, nodeleftspring, nodeleftspring]
        right_spring = [noderightspring, noderight, noderightspring, noderightspring]
        equaldof_left = [nodeleft, nodeleftspring]
        equaldof_right = [noderight, noderightspring]

        return left_mat, right_mat, beam_element, left_spring, right_spring, equaldof_left, equaldof_right

    def get_beam_my(H,B,cover,fiw,nficornertop,nfiinttop,ficornertop,fiinttop,nficornerbot,nfiintbot,ficornerbot,fiintbot,ecu,esy,fylong,fc,Es,Ec):

        if fc < 27.6:
            betafc = 0.85
        elif fc > 55.17:
            betafc = 0.65
        else:
            betafc = 1.05-0.05*fc/6.9

        d = 1000*H - 1000*cover - 1000*fiw - 0.5*ficornertop*1000 # in mm
        d_line = 1000*H - d # in mm
        cB = (ecu*d)/(ecu+esy)
        Astens = nficornertop*((0.25*np.pi) * (ficornertop*1000)**2) + nfiinttop*((0.25*np.pi)*(fiinttop*1000)**2) # in mm2
        ros = Astens/(B*1000*d)
        As_line = nficornerbot*((0.25*np.pi) * (ficornerbot*1000)**2) + nfiintbot*((0.25*np.pi)*(fiintbot*1000)**2) # in mm2
        ros_line = As_line/(B*1000*d)
        c = (Astens*fylong - As_line*fylong)/(0.85*fc*B*1000*betafc)
        
        AcomprCntrl = ros + ros_line
        AtensCntrl = ros + ros_line
        BcomprCntrl = ros + ros_line*(d_line/d) * (1 + (d_line/d))
        BtensCntrl = ros + ros_line*(d_line/d) * (1 + (d_line/d))
        nyoung = Es/Ec           
        if c < cB:
            Control = 1
            AtoUse = AtensCntrl
            BtoUse = BtensCntrl
        else:
            Control = 0
            AtoUse = AcomprCntrl
            BtoUse = BcomprCntrl

        ky = (nyoung**2 * AtoUse**2 + 2*nyoung*BtoUse) ** 0.5 - nyoung*AtoUse
        fiy1 = (10**3) * fylong/(Es * (1-ky)*d)
        fiy2 = (10**3) * (1.8*fc / (Ec*ky*d))
        if Control==1:
            fiy = fiy1
        else:
            fiy = fiy2

        Term1 = (10**6) * Ec*0.5*ky**2 * (0.5 * (1 + (d_line/d)) - (ky/3))
        Term2 = (10**6) * (0.50*Es) * ((1-ky) * ros + (ky - (d_line/d)) * ros_line) * (1 - (d_line/d))
        My_Top = (10**-3) * (B*((d/1000)**3)) * fiy * (Term1 + Term2)
        fiyTop = fiy
        # Mbot reinforcemetn in tension
        d = 1000*H - 1000*cover - 1000*fiw - 0.5*ficornerbot*1000 # in mm
        d_line = 1000*H - d  # in mm
        cB = (ecu*d)/(ecu + esy)
        Astens = nficornerbot*((0.25*np.pi)*(ficornerbot*1000)**2) + nfiintbot*((0.25*np.pi)*(fiintbot*1000)**2) # in mm2
        ros = Astens/(B*1000*d)
        As_line = nficornertop * ((0.25*np.pi) * (ficornertop*1000)**2) + nfiinttop * ((0.25*np.pi) * (fiinttop*1000)**2) # in mm2
        ros_line = As_line/(B*1000*d)
        c = (Astens*fylong - As_line*fylong)/(0.85*fc*B*1000*betafc)
        AcomprCntrl = ros + ros_line
        AtensCntrl = ros + ros_line
        BcomprCntrl = ros + ros_line * (d_line/d)*(1 + (d_line/d))
        BtensCntrl = ros + ros_line * (d_line/d)*(1 + (d_line/d))
        nyoung = Es/Ec
        if c < cB:
            Control = 1
            AtoUse = AtensCntrl
            BtoUse = BtensCntrl
        else:
            Control = 0
            AtoUse = AcomprCntrl
            BtoUse = BcomprCntrl

        ky = (nyoung**2 * AtoUse**2 + 2*nyoung*BtoUse)**0.5 - nyoung*AtoUse
        fiy1 = (10**3) * fylong/(Es * (1-ky) * d)
        fiy2 = (10**3) * (1.8*fc / (Ec*ky*d))
        if Control == 1:
            fiy = fiy1
        else:
            fiy = fiy2

        Term1 = (10**6) * (Ec*0.5*ky**2) * (0.5 * (1 + (d_line/d)) - (ky/3))
        Term2 = (10**6) * (0.50*Es) * ((1-ky) * ros + (ky - (d_line/d)) * ros_line) * (1 - (d_line/d))
        My_Bot = (10**-3) * (B*((d/1000)**3)) * fiy * (Term1 + Term2)
        fiyBot = fiy
        RatforRotBOT = Astens/As_line

        return My_Top,My_Bot,fiyTop,fiyBot,RatforRotBOT

    def get_column_concentrated_plasticity(column, i):

        anglerad = 0
        nFactor = 10
        # Pre-allocate some stuff
        elenum  = column['Name'][i]
        nodebot = column['Nodei'][i]
        nodetop = column['Nodej'][i]
        HY = column['HY'][i]
        HX = column['HX'][i]
        N = column['N_CP'][i]
        fiw = column['fiw_Q'][i]
        sw = column['sw_Q'][i]
        nwparallel_to_Y = column['nw_paraleltoY'][i]
        nwparallel_to_X = column['nw_paraleltoX'][i]
        nbar_HminusX = column['nBarHminus'][i]
        nbar_HplusX = column['nBarHminus'][i]
        nlayintY = nbar_HplusX - 2
        nlayintX = column['nlayintX'][i]
        ficorner = column['fi_corner_Q'][i]
        filayint = column['fi_layint_Q'][i]
        L = column['L'][i] # I do not extract here the segments located inside the joints
        cover = column['cover_Q'][i]
        fc = column['fcm_Q'][i]
        fylong = 1.2*column['fsyl_Q'][i] # 1.2 to consider mean based on table 4.10 and table 4.14 from Wisniewski D (2007) PhD HMA
        fyw = 1.2*column['fsyw_Q'][i] # 1.2 to consider mean based on table 4.10 and table 4.14 from Wisniewski D (2007) PhD HMA
        bondslipfact = column['bondslipfact_Q'][i]
        sn = sw/ficorner
        rholong = column['RHosl'][i]
        # ...........................................................................
        if elenum > 199 or L > 1.00:
            Ls = L/2 # Assuming Ls columns equal to 50% of the free length L of the element
        else: # TODO: for both cases Ls is the same? is there any error here? According to the statement it should be Ls = L
            Ls = L/2 # Assuming Ls columns equal to 100% of the free length L of the element
        # ...........................................................................
        ecu = 0.0035
        Area = HY*HX
        IgforloadinX = (HY * HX**3)/12
        IgforloadinY = (HX * HY**3)/12
        stiffFactor1 = nFactor
        stiffFactor2 = (stiffFactor1+1) / stiffFactor1
        Icol_modX = IgforloadinX * stiffFactor2
        Icol_modY = IgforloadinY * stiffFactor2
        Ec = 22000 * (fc/10)**0.3
        Jz = (HX * HY) * (HX**2 + HY**2)
        Es = 200000
        epsy_s = fylong/Es
        nyoung = Es/Ec
        niu = (N / 1000) / (HY * HX * fc)
        roshX = (0.25 * np.pi * (fiw**2) * nwparallel_to_X)/(HY * sw)
        roshY = (0.25 * np.pi * (fiw**2) * nwparallel_to_Y)/(HX * sw)
        E_mod = Ec*1000
        G_mod = E_mod/2.4 # Assumign a poisson coefficient of 0.20
        # ...........................................................................
        # Calculate the parameters for the flexural spring component model following the Haselton et al 2016 approach
        # and the spreadsheet made available HX Curt B. Haselton in his website.
        # Reference: Curt B. Haselton, Abbie B. Liel, Sarah C. Taylor-Lange, and Gregory G. Deierlein (2016)
        # Calibration of Model to Simulate Response of Reinforced Concrete Beam-Columns to Collapse. ACI Structural Journal 10.14359/51689245
        if fc < 27.6:
            betafc = 0.85
        elif fc> 55.17:
            betafc = 0.65
        else:
            betafc= 1.05 - 0.05*fc/6.9
        tetacapXpl = 0.12 * (1 + 0.55*bondslipfact) * (0.16**niu) * ((0.02 + 40*roshX)**0.43) * (0.54**(0.01 * 1.0 * fc)) * (0.66**(0.1*sn)) * (2.27**(10.0*rholong))
        tetacapYpl = 0.12 * (1 + 0.55*bondslipfact) * (0.16**niu) * ((0.02 + 40*roshY)**0.43) * (0.54**(0.01 * 1.0 * fc)) * (0.66**(0.1*sn)) * (2.27**(10.0*rholong))
        tetapcX = min(0.76 * (0.031**niu) * ((0.02 + 40*roshX)**1.02), 0.10)
        tetapcY = min(0.76 * (0.031**niu) * ((0.02 + 40*roshY)**1.02), 0.10)
        McMy = 1.25 * (0.89**niu)*(0.91**(0.01*fc))
        lambda1 = 30 * (0.3**niu)
        lambdaX = lambda1*tetacapXpl
        lambdaY = lambda1*tetacapYpl
        # ...........................................................................
        # My for a lateral load in the YY direction flexural spring
        # My calculations are done followign the  Panagiotakos and Fardis (ACI 2001; paper - page 137)
        # model as reported in the Rough Spreadsheet to Compute the Yield Moment of an RC Column HX Curt B. Haselton and Abbie B. Liel
        # The yieldign curvature is calculated as 2.10*epsy/H followign Priestley et al 2007
        # Thetay and initial stiffiness for a lateral load in the XX direction flexural spring
        # Thetay calculations are done followign the upcoming version of EC8/3
        # Kinit is done affectign the initial rotational stiffness HX a factor to compute its secant value
        # stiffness modifications to equate the stiffness of the spring-elastic element-spring subassembly to the stiffness of the actual frame member
        # References: (1) Ibarra, L. F., and Krawinkler, H. (2005). "Global collapse of frame structures under seismic excitations," Technical Report 152,
        # The John A. Blume Earthquake Engineering Research Center, Department of Civil Engineering, Stanford University, Stanford, CA.
        # (2) Zareian, F. and Medina, R. A. (2010). A practical method for proper modeling of structural damping in inelastic plane
        # structural systems, Computers & Structures, Vol. 88, 1-2, pp. 45-53.
        dX = 1000*HX - 1000*cover - 1000*fiw - 0.5*ficorner*1000
        d_lineX = 1000*HX - dX
        cHY=(ecu*dX)/(ecu+epsy_s)
        AsX = 2*(0.25*np.pi)*(ficorner*1000)**2 + nlayintY*(0.25*np.pi)*(filayint*1000)**2 # assume it for tension HMA
        rosX = AsX/(HY*1000*dX)                                                       # assume it for tension HMA rho
        As_lineX = AsX                                                                # assume it for compressive HMA                            
        ros_lineX = As_lineX/(HY*1000*dX)                                             # assume it for compressive HMA rho dash  
        AswX = 2*nlayintX * (0.25*np.pi) * (filayint*1000)**2                         # assume it for web reinforcement HMA 
        rowX = AswX/(HY*1000*dX)                                                      # assume it for web reinforcement  rho v HMA 
        cX = (AsX*fylong*1000 - As_lineX*fylong*1000 + N) / (0.85*(HY*1000)*betafc*fc)
        AcomprCntrlX = rosX + ros_lineX+rowX - ((N*1000) / (1.8*nyoung*(HY*1000)*dX*fc))
        AtensCntrlX = rosX + ros_lineX+rowX + ((N*1000) / ((HY*1000)*dX*fylong))
        BcomprCntrlX = rosX + ros_lineX*(d_lineX/dX) + 0.5*rowX*(1 + (d_lineX/dX))
        BtensCntrlX = rosX + ros_lineX*(d_lineX/dX) + 0.5*rowX*(1 + (d_lineX/dX)) + ((N*1000) / ((HY*1000)*dX*fylong))
        if cX < cHY:
            AtoUseX = AtensCntrlX
            BtoUseX = BtensCntrlX
            Control = 1
        else:
            AtoUseX = AcomprCntrlX
            BtoUseX = BcomprCntrlX
            Control = 0
        # ...........................................................................
        kyX = (nyoung**2 * AtoUseX**2 + 2*nyoung*BtoUseX) ** 0.5 - nyoung*AtoUseX
        fiy1 = (10**3) * fylong / (Es * (1-kyX) * dX)
        fiy2 = (10**3) * ((1.8 * fc) / (Ec*kyX*dX))
        if Control == 1:
            fiXy = fiy1
        else:
            fiXy = fiy2
        # ...........................................................................
        Term1X = (10**6) * Ec * ((kyX**2) / 2) * (0.5 * (1 + (d_lineX/dX)) - (kyX/3))
        Term2X = (10**6) * (Es/2) * ((1-kyX) * rosX + (kyX - (d_lineX/dX)) * ros_lineX + (rowX/6) * (1 - (d_lineX/dX))) * (1 - (d_lineX/dX))
        MyX = (10**-3) * (HY * ((dX/1000)**3)) * fiXy * (Term1X + Term2X)
        # ...........................................................................
        av = 1.0
        z = 0.81*HX
        thetay1X = fiXy * ((Ls + (av*z))/3)
        thetay3X = 0.13 * fiXy * ficorner * fylong / (fc**0.50)
        thetay2X = 0.0013 * (1 + 1.5 * HX/Ls)
        thetayX = thetay1X + thetay2X + bondslipfact * thetay3X
        # ...........................................................................
        K0X = MyX / thetayX
        # EIfactX = max(min(1.33 * (0.10+niu)**0.80, 0.80), 0.35)
        # IgforloadinX_mod = EIfactX * IgforloadinX * (nFactor + 1.0) / nFactor         # modified moment of inertia for columns with loading in XX
        # K0X = (nFactor + 1) * 3.0 * EIfactX * E_mod * IgforloadinX_mod / L
        a_memX = (nFactor + 1.0) * (MyX * (McMy - 1)) / (K0X * tetacapXpl)      # strain hardening ratio of spring
        bHY = (a_memX) / (1.0 + nFactor*(1.0 - a_memX))                         # modified strain hardening ratio of spring (Ibarra & Krawinkler 2005, note: Eqn B.5 is incorrect)
        # ...........................................................................
        dY = 1000*HY - 1000*cover - 1000*fiw - 0.5*ficorner*1000
        d_lineY = 1000*HY - dY
        cHX = (ecu*dY)/(ecu+epsy_s)
        AsY = 2* (0.25*np.pi) * (ficorner*1000)**2 + (nlayintX)*(0.25*np.pi) * (filayint*1000)**2
        rosY = AsY / (HX*1000*dY)
        As_lineY = AsY
        ros_lineY = As_lineY / (HX*1000*dY)
        AswY = 2 * nlayintY * (0.25*np.pi) * (filayint*1000)**2
        rowY = AswY / (HX*1000*dY)
        cY = (AsY*fylong*1000 - As_lineY*fylong*1000 + N) / (0.85 * (HX*1000) * betafc * fc)
        AcomprCntrlY = rosY + ros_lineY + rowY - ((N*1000) / (1.8*nyoung*(HX*1000) * dY * fc))
        AtensCntrlY = rosY + ros_lineY + rowY + ((N*1000) / ((HX*1000) * dY * fylong))
        BcomprCntrlY = rosY + ros_lineY * (d_lineY/dY) + 0.5 * rowY * (1 + (d_lineY/dY))
        BtensCntrlY=rosY+ros_lineY*(d_lineY/dY)+0.5*rowY*(1.+(d_lineY/dY)) + ((N*1000)/((HX*1000)*dY*fylong));
        if cY < cHX:
            AtoUseY = AtensCntrlY
            BtoUseY = BtensCntrlY
            Control = 1
        else:
            AtoUseY = AcomprCntrlY
            BtoUseY = BcomprCntrlY
            Control = 0
        # ...........................................................................
        kyY = (nyoung**2 * AtoUseY**2 + 2*nyoung*BtoUseY)**0.5 - nyoung*AtoUseY
        fiy1 = (10**3) * fylong / (Es * (1 - kyY) * dY)
        fiy2 = (10**3) * ((1.8 * fc) / (Ec * kyY * dY))
        if Control == 1:
            fiYy = fiy1
        else:
            fiYy = fiy2
        # ...........................................................................
        Term1Y = (10**6) * Ec * ((kyY**2) / 2) * (0.5 * (1 + (d_lineY/dY)) - (kyY/3))
        Term2Y = (10**6) * (Es/2) * ((1 - kyY) * rosY + (kyY-(d_lineY/dY)) * ros_lineY + (rowY/6) * (1 - (d_lineY/dY))) * (1 - (d_lineY/dY))
        MyY = (10**-3) * (HX* ((dY/1000)**3)) * fiYy * (Term1Y + Term2Y)
        # ...........................................................................
        av = 1.0
        z = 0.81 * HY
        thetay1Y = fiYy * ((Ls + (av*z))/3)
        thetay3Y = 0.13 * fiYy * ficorner * fylong / (fc**0.50)
        thetay2Y = 0.0013 * (1 + 1.5*HY/Ls)
        thetayY = thetay1Y + thetay2Y + bondslipfact * thetay3Y
        # ...........................................................................
        K0Y = MyY / thetayY
        a_memY = (nFactor + 1.0) * (MyY * (McMy-1)) / (K0Y*tetacapYpl)  # strain hardening ratio of spring
        bHY = a_memX / (1.0 + nFactor * (1.0-a_memX))                 # modified strain hardening ratio of spring (Ibarra & Krawinkler 2005, note: Eqn B.5 is incorrect)
        # nFactor=10;                                                        # stiffness multiplier for rotational spring
        # EIfactY=max(min(1.33*(0.10+niu)**0.80,0.80),0.35)
        # IgforloadinY_mod= EIfactY*IgforloadinY*(nFactor+1.0)/nFactor      # modified moment of inertia for columns with loading in YY
        # K0Y= (nFactor+1)*3.0*EIfactY*E_mod*IgforloadinY_mod/L
        # a_memY=(nFactor+1.0)*(MyY*(McMy-1)) / (K0Y*tetacapYpl)            # strain hardening ratio of spring
        # bHX=(a_memY)/(1.0+nFactor*(1.0-a_memY))                           # modified strain hardening ratio of spring (Ibarra & Krawinkler 2005, note: Eqn B.5 is incorrect)            
        # ...........................................................................
        # Define the shear component model following the methodology proposed HX Leborgne et al 2015
        # It involves defining the parameters necessary
        # to be completed with references and links!
        rigidSlope = (G_mod*HY*HX/Ls)*(5/6)
        AvX = (nwparallel_to_X * np.pi * fiw**2)/4
        AvY = (nwparallel_to_Y * np.pi * fiw**2)/4
        VnX = 1000 * (1.0 * 1.00 * ((0.50 * (fc**0.5) / (Ls / (0.90 * HX))) * (1 + (2 * N / 1000) / ((fc**0.5) * HX * HY))**0.5) * 0.80 * HX * HY + 1.00 * ((AvX * fyw * 0.81 * HX) / sw)) # ASCE 41-06 model has been corrected HMA
        VnY = 1000 * (1.0 * 1.00 * ((0.50 * (fc**0.5) / (Ls / (0.90 * HY))) * (1 + (2 * N / 1000) / ((fc**0.5) * HX * HY))**0.5) * 0.80 * HX * HY + 1.00 * ((AvY * fyw * 0.81 * HY) / sw)) # ASCE 41-06 model
        MuX = McMy * MyX
        VpX = MuX / Ls
        shearartioX = VpX / VnX
        MuY = McMy * MyY
        VpY = MuY / Ls
        shearartioY = VpY / VnY
        deltaVnX = VnX / rigidSlope
        deltaVnY = VnY / rigidSlope
        deltaVuX = (4 - 12*VnX / (HY * 0.90 * HX * fc * 1000)) * deltaVnX
        deltaAuX = max(0.04 + (5.5989 / (2.1445 + N * (sw / (AvX * fyw * 0.90 * HX * 2.1445)))), deltaVuX+0.001)
        deltaVuY = (4 - 12*VnY / (HX * 0.90 * HY * fc * 1000)) * deltaVnY
        deltaAuY = max(0.04 + (5.5989 / (2.1445 + N * (sw / (AvY * fyw * 0.90 * HY * 2.1445)))), deltaVuY+0.001)
        kdegX0 = (4.5 * N * ((AvX * fyw * 1000 * 0.90 * HX / (N * sw)) * 4.6 + 1)**2)
        kdegY0 = (4.5 * N * ((AvY * fyw * 1000 * 0.90 * HY / (N * sw)) * 4.6 + 1)**2)
        KunloadX = (12*E_mod * IgforloadinX) / (L**3)
        KunloadY = (12*E_mod * IgforloadinY) / (L**3)
        kdegX1 = 1 / (1/kdegX0 - 1/KunloadX)
        kdegY1 = 1 / (1/kdegY0 - 1/KunloadY)
        kdegX = kdegX0 / L
        kdegY = kdegY0 / L
        # ...........................................................................
        # Tags for the uniaxial materials and spring nodes
        # check the notation in the read me pdf file
        nodebotspring = 10000 + nodebot
        nodetopspring = 10000 + nodetop
        mattag_flexXtop = 21000000 + elenum
        mattag_flexYtop = 22000000 + elenum
        mattag_flexXbot = 71000000 + elenum
        mattag_flexYbot = 72000000 + elenum
        mattag_ShearXtop = 23000000 + elenum
        mattag_ShearYtop = 24000000 + elenum
        mattag_ShearXbot = 73000000 + elenum
        mattag_ShearYbot = 74000000 + elenum
        Curvtag_ShearXtop = mattag_ShearXtop
        Curvtag_ShearYtop = mattag_ShearYtop
        Curvtag_ShearXbot = mattag_ShearXbot
        Curvtag_ShearYbot = mattag_ShearYbot
        Springtoptag = nodetopspring
        Springbottag = nodebotspring
        Ks_colY = 10 * 6.0 * E_mod * Icol_modY / L
        tetaY = MyY / Ks_colY
        Ks_colX = 10 * 6.0 * E_mod * Icol_modX / L
        tetaX = MyX / Ks_colX
        # teta1plusX = thetayX/nFactor
        # teta2plusX = thetayX/nFactor+0.70*tetacapXpl
        # teta3plusX = thetayX/nFactor+0.70*tetacapXpl+0.50*tetapcX
        # teta1plusY = thetayY/nFactor
        # teta2plusY = thetayY/nFactor+0.70*tetacapYpl
        # teta3plusY = thetayY/nFactor+0.70*tetacapYpl+0.50*tetapcY
        teta1plusX = thetayX / nFactor
        teta2plusX = thetayX / nFactor + tetacapXpl
        teta3plusX = thetayX / nFactor + tetacapXpl + tetapcX
        teta1plusY = thetayY / nFactor
        teta2plusY = thetayY / nFactor + tetacapYpl
        teta3plusY = thetayY / nFactor + tetacapYpl + tetapcY
        # ...........................................................................
        # Prepare inputs for OpenSees
        comment1 = f"# Column {elenum} PDelta"
        comment2 = f"# tetayX={thetayX:4.6f}, MyX={MyX:4.6f}, tetayY={thetayY:4.6f}, MyY={MyY:4.6f}"
        comment3 = f"# HY={HY:4.6f}, HX={HX:4.6f}, L={L:4.6f}, N={N:4.6f}, cover={cover:4.6f}, anglerad={anglerad:4.6f} sw={sw:4.6f}, nwparallel_to_Y={nwparallel_to_Y:4.6f}, nwparallel_to_X={nwparallel_to_X:4.6f}, fiw={fiw:4.6f} nbar_HminusX={nbar_HminusX:4.6f}, nbar_HplusX={nbar_HplusX:4.6f}, nlayintX={nlayintX:4.6f}, ficorner={ficorner:4.6f}, filayint={filayint:4.6f} fc={fc:4.6f}, fyw={fyw:4.6f}, fylong={fylong:4.6f}"
        comment4 = f"# VnX={VnX:4.6f}, KdegX={kdegX:4.6f}, VnY={VnY:4.6f}, KdegY={kdegY:4.6f}"
        comments = [comment1, comment2, comment3, comment4]

        geomtransf = [elenum + 111000, np.cos(np.pi + anglerad), np.cos(np.pi/2 + anglerad), 0]

        # The residual forces on 6th and 12th elements were changed from 0.01 * McMy*My to 0.1*McMy*My for better convergence
        mat_flexXtop = [mattag_flexXtop, MyX, teta1plusX, 1.13*MyX, teta2plusX, 0.1*McMy*MyX, teta3plusX, -MyX, -teta1plusX, -1.13*MyX, -teta2plusX, -0.1*McMy*MyX, -teta3plusX, 1, 1, 0, 0, 0]
        mat_flexXbot = [mattag_flexXbot, MyX, teta1plusX, 1.13*MyX, teta2plusX, 0.1*McMy*MyX, teta3plusX, -MyX, -teta1plusX, -1.13*MyX, -teta2plusX, -0.1*McMy*MyX, -teta3plusX, 1, 1, 0, 0, 0]
        mat_flexYtop = [mattag_flexYtop, MyY, teta1plusY, 1.13*MyY, teta2plusY, 0.1*McMy*MyY, teta3plusY, -MyY, -teta1plusY, -1.13*MyY, -teta2plusY, -0.1*McMy*MyY, -teta3plusY, 1, 1, 0, 0, 0]
        mat_flexYbot = [mattag_flexYbot, MyY, teta1plusY, 1.13*MyY, teta2plusY, 0.1*McMy*MyY, teta3plusY, -MyY, -teta1plusY, -1.13*MyY, -teta2plusY, -0.1*McMy*MyY, -teta3plusY, 1, 1, 0, 0, 0]
        matflex = [mat_flexXtop, mat_flexXbot, mat_flexYtop, mat_flexYbot]

        mat_shearXbot = [mattag_ShearXbot, 0.80*VnX, 0.80*VnX/rigidSlope, 1.0*VnX, VnX/rigidSlope, 0.20*VnX, 0.80*VnX/kdegX, -0.80*VnX, -0.80*VnX/rigidSlope, -1.0*VnX, -VnX/rigidSlope, -0.20*VnX, -0.80*VnX/kdegX, 0.4, 0.3, 0.0, 0, 0]
        mat_shearXtop = [mattag_ShearXtop, 0.80*VnX, 0.80*VnX/rigidSlope, 1.0*VnX, VnX/rigidSlope, 0.20*VnX, 0.80*VnX/kdegX, -0.80*VnX, -0.80*VnX/rigidSlope, -1.0*VnX, -VnX/rigidSlope, -0.20*VnX, -0.80*VnX/kdegX, 0.4, 0.3, 0.0, 0, 0]
        mat_shearYbot = [mattag_ShearYbot, 0.80*VnY, 0.80*VnY/rigidSlope, 1.0*VnY, VnY/rigidSlope, 0.20*VnY, 0.80*VnY/kdegY, -0.80*VnY, -0.80*VnY/rigidSlope, -1.0*VnY, -VnY/rigidSlope, -0.20*VnY, -0.80*VnY/kdegY, 0.4, 0.3, 0.0, 0, 0]
        mat_shearYtop = [mattag_ShearYtop, 0.80*VnY, 0.80*VnY/rigidSlope, 1.0*VnY, VnY/rigidSlope, 0.20*VnY, 0.80*VnY/kdegY, -0.80*VnY, -0.80*VnY/rigidSlope, -1.0*VnY, -VnY/rigidSlope, -0.20*VnY, -0.80*VnY/kdegY, 0.4, 0.3, 0.0, 0, 0]
        matshear = [mat_shearXbot, mat_shearXtop, mat_shearYbot, mat_shearYtop]

        cdh_agg_bot = [Springbottag, mattag_flexXbot, mattag_flexYbot]
        cdh_agg_top = [Springtoptag, mattag_flexXtop, mattag_flexYtop]
        cdh_zero_bot = [Springbottag, nodebot, nodebotspring, Springbottag]
        cdh_ele = [elenum, nodebotspring, nodetopspring, Area, E_mod, G_mod, Jz, Icol_modX, Icol_modY, elenum + 111000]
        cdh_zero_top = [Springtoptag, nodetop, nodetopspring, Springtoptag]
        cdh_ele_inputs = [cdh_agg_bot, cdh_agg_top, cdh_zero_bot, cdh_ele, cdh_zero_top]

        limitcurve_xtop = [Curvtag_ShearXtop, elenum, -10, VnX, 0, VnX, 10, VnX, -kdegX, 0.050, 2, 0, nodebot, nodetop, 1, 3]
        mat_xtop = [mattag_ShearXtop, 0.25*VnX, 0.25*VnX/rigidSlope, 0.75*VnX, 0.75*VnX/rigidSlope, 2.5*VnX, 2.5*VnX/rigidSlope, -0.25*VnX, -0.25*VnX/rigidSlope, -0.75*VnX, -0.75*VnX/rigidSlope, -2.5*VnX, -2.5*VnX/rigidSlope, 0.4, 0.30, 0.003, 0.0, 0.00, Curvtag_ShearXtop, 2]
        limitcurve_xbot = [Curvtag_ShearXbot, elenum, -10, VnX, 0, VnX, 10, VnX, -kdegX, 0.050, 2, 0, nodebot, nodetop, 1, 3]
        mat_xbot = [mattag_ShearXbot, 0.25*VnX, 0.25*VnX/rigidSlope, 0.75*VnX, 0.75*VnX/rigidSlope, 2.5*VnX, 2.5*VnX/rigidSlope, -0.25*VnX, -0.25*VnX/rigidSlope, -0.75*VnX, -0.75*VnX/rigidSlope, -2.5*VnX, -2.5*VnX/rigidSlope, 0.4, 0.30, 0.003, 0.0, 0.00, Curvtag_ShearXbot, 2]
        notcdh_shear_inputsX = [limitcurve_xtop, mat_xtop, limitcurve_xbot, mat_xbot]

        limitcurve_ytop = [Curvtag_ShearYtop, elenum, -10, VnY, 0, VnY, 10, VnY, -kdegY, 0.050, 2, 0, nodebot, nodetop, 2, 3]
        mat_ytop = [mattag_ShearYtop, 0.25*VnY, 0.25*VnY/rigidSlope, 0.75*VnY, 0.75*VnY/rigidSlope, 2.5*VnY, 2.5*VnY/rigidSlope, -0.25*VnY, -0.25*VnY/rigidSlope, -0.75*VnY, -0.75*VnY/rigidSlope, -2.5*VnY, -2.5*VnY/rigidSlope, 0.4, 0.30, 0.003, 0.0, 0.00, Curvtag_ShearYtop, 2]
        limitcurve_ybot = [Curvtag_ShearYbot, elenum, -10, VnY, 0, VnY, 10, VnY, -kdegY, 0.050, 2, 0, nodebot, nodetop, 2, 3]
        mat_ybot = [mattag_ShearYbot, 0.25*VnY, 0.25*VnY/rigidSlope, 0.75*VnY, 0.75*VnY/rigidSlope, 2.5*VnY, 2.5*VnY/rigidSlope, -0.25*VnY, -0.25*VnY/rigidSlope, -0.75*VnY, -0.75*VnY/rigidSlope, -2.5*VnY, -2.5*VnY/rigidSlope, 0.4, 0.30, 0.003, 0.0, 0.00, Curvtag_ShearYbot, 2]
        notcdh_shear_inputsY = [limitcurve_ytop, mat_ytop, limitcurve_ybot, mat_ybot]

        noncdh_agg_bot = [Springbottag, mattag_ShearYbot, mattag_ShearXbot, mattag_flexXbot, mattag_flexYbot]
        noncdh_agg_top = [Springtoptag, mattag_ShearYtop, mattag_ShearXtop, mattag_flexXtop, mattag_flexYtop]
        noncdh_ele_inputs = [noncdh_agg_bot, noncdh_agg_top, cdh_zero_bot, cdh_ele, cdh_zero_top]

        return comments, geomtransf, matflex, matshear, cdh_ele_inputs, notcdh_shear_inputsX, notcdh_shear_inputsY, noncdh_ele_inputs

    def preallocate_joint(joint, general):

        FlagType = joint['Data'][:, 12]
        P = general['Njoint'].flatten() 
        hcX = joint['Data'][:, 1]
        hcY = joint['Data'][:, 2]
        hb = joint['Data'][:, 3]  # Larger value according to O'Reilly [2016]
        hbX = joint['Data'][:,13]
        hbY = joint['Data'][:,14]
        bbX = general['Bbeamfix_X'] # TODO: not clear to me, why are we using fixed width? This needs to be changed, and needs to be retrieved from final design.
        bbY = general['Bbeamfix_Y'] # The fix for bbX and bbY requires some thinking. I am leaving these as they are for now.
        # fcm = 20 # joint['fcm']  # TODO: Why is it 20 but not fcm of the final design? I guess this needs to be changed as well.
        fcm = general['fck'] + 8 # even though this reflects the design, it does not reflect the adjusted fcm with quality factors. This part requires discussion
        Ecm = 5624 * (fcm**0.47)
        
        # TODO: What are these stuff?
        ptcext = np.array([0.135, 0.135, 0.050, 0.135, 0.135, 0.05])
        ptcint = np.array([0.290, 0.420, 0.420, 0.290, 0.420, 0.420])
        ptext = ptcext * (fcm**0.5) * 1000
        ptint = ptcint * (fcm**0.5) * 1000
        gamm = np.array([0.0002, 0.0132, 0.020, 0.0002, 0.0127, 0.020])
        hyst_ext = np.array([0.600, 0.200, 0.000, 0.000, 0.300])
        hyst_int = np.array([0.600, 0.200, 0.000, 0.010, 0.300])
        hyst_rof = np.array([0.600, 0.200, 0.000, 0.000, 0.300])

        # Create the axial material
        Ac = hcY * hcX
        Ac = Ac.flatten()
        hb = hb.flatten()
        Kspr = 2*Ecm*Ac/hb

        return hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, gamm, P, Kspr

    def get_joint_type(designlevel, quality):
        
        if quality == 1:
            if designlevel in ['CDH', 'CDM']:
                joint_type = 1 
            elif designlevel == 'CDL':
                joint_type = 2
            else:
                joint_type = 3
        elif quality == 2:
            if designlevel == 'CDH':
                joint_type = 1
            elif designlevel in ['CDM', 'CDL']:
                joint_type = 2
            else:
                joint_type = 3
        elif quality == 3:
            if designlevel == 'CDH':
                joint_type = 1 # Rigid
            elif designlevel == 'CDM':
                joint_type = 2 # Linear elastic
            else:
                joint_type = 3 # Nonlinear
        
        return joint_type

    def get_elastic_joint(hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, hstorey, P, i):

        if hcY[i] >= bbX: # X DIRECTION
            bjX = hcY[i] + 0
        elif bbX + 0.5*hcX[i] < hcY[i]:
            bjX = bbX + 0.5*hcX[i]
        elif hcY[i] < bbX:
            bjX = bbX + 0
        elif hcY[i] + 0.5*hcX[i]<bbX[i]:
            bjX = hcY[i] + 0.5*hcX[i]

        if hcX[i] >= bbY: # Y DIRECTION
            bjY = hcX[i] + 0
        elif bbY + 0.5*hcY[i] < hcX[i]:
            bjY[i] = bbY + 0.5*hcY[i]
        elif hcX[i] < bbY[i]:
            bjY[i] = bbY + 0
        elif hcX[i] + 0.5*hcY[i] < bbY:
            bjY[i] = hcX[i] + 0.5*hcY[i]

        jX = 0.81*hbX[i] # replaced 0.9*(hbX[i] - cover-dbV-dbL/2) by 0.81hbX[i]
        jY = 0.81*hbY[i] # replaced 0.9*(hbY[i] - cover-dbV-dbL/2) by 0.81hbX[i]
        if FlagType[i] == 2: # Interior joint
            MEjX1 = ptint[0] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptint[0]))**0.5
            MEjY1 = ptint[0] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptint[0]))**0.5
        elif FlagType[i] == 1: # Exterior joint 
            MEjX1 = ptext[0] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptext[0]))**0.5
            MEjY1 = ptext[0] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptext[0]))**0.5
        elif FlagType[i] == 3: # Roof joint
            MEjX1 = ptext[0] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptext[0]))**0.5
            MEjY1 = ptext[0] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptext[0]))**0.5
        
        return MEjX1, MEjY1

    def get_inelastic_joint(hcY, bbX, hcX, bbY, hbX, hbY, FlagType, ptint, ptext, hstorey, P, i):

        if hcY[i] >= bbX: # X DIRECTION
            bjX = hcY[i] + 0
        elif bbX + 0.5*hcX[i] < hcY[i]:
            bjX = bbX + 0.5*hcX[i]
        elif hcY[i] < bbX:
            bjX = bbX + 0
        elif hcY[i] + 0.5*hcX[i]<bbX[i]:
            bjX = hcY[i] + 0.5*hcX[i]

        if hcX[i] >= bbY: # Y DIRECTION
            bjY = hcX[i] + 0
        elif bbY + 0.5*hcY[i] < hcX[i]:
            bjY = bbY + 0.5*hcY[i]
        elif hcX[i] < bbY[i]:
            bjY = bbY + 0
        elif hcX[i] + 0.5*hcY[i] < bbY:
            bjY = hcX[i] + 0.5*hcY[i]

        jX = 0.81*hbX[i] # replaced 0.9*(hbX[i] - cover-dbV-dbL/2) by 0.81hbX[i]
        jY = 0.81*hbY[i] # replaced 0.9*(hbY[i] - cover-dbV-dbL/2) by 0.81hbX[i]
        if FlagType[i] == 2: # Interior joint
            MjX1 = ptint[0] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptint[0]))**0.5
            MjX2 = ptint[1] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptint[1]))**0.5
            MjX3 = ptint[2] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptint[2]))**0.5
            MjX4 = ptint[3] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptint[3]))**0.5
            MjX5 = ptint[4] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptint[4]))**0.5
            MjX6 = ptint[5] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (1 + P[i] / (bjX * hcX[i] * ptint[5]))**0.5                    
            
            MjY1 = ptint[0] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptint[0]))**0.5
            MjY2 = ptint[1] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptint[1]))**0.5
            MjY3 = ptint[2] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptint[2]))**0.5
            MjY4 = ptint[3] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptint[3]))**0.5
            MjY5 = ptint[4] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptint[4]))**0.5
            MjY6 = ptint[5] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (1 + P[i] / (bjY * hcY[i] * ptint[5]))**0.5

        elif FlagType[i] == 1: # Exterior joint 
            MjX1 = ptext[0] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (hbX[i] / (2*hcX[i]) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[0]))**0.5)
            MjX2 = ptext[1] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (hbX[i] / (2*hcX[i]) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[1]))**0.5)
            MjX3 = ptext[2] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (hbX[i] / (2*hcX[i]) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[2]))**0.5)
            MjX4 = ptext[3] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (hbX[i] / (2*hcX[i]) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[3]))**0.5)
            MjX5 = ptext[4] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (hbX[i] / (2*hcX[i]) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[4]))**0.5)
            MjX6 = ptext[5] * bjX * hcX[i] * (hstorey * jX / (hstorey - jX)) * (hbX[i] / (2*hcX[i]) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[5]))**0.5)                    
            
            MjY1 = ptext[0] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (hbY[i] / (2*hcY[i]) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[0]))**0.5)
            MjY2 = ptext[1] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (hbY[i] / (2*hcY[i]) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[1]))**0.5)
            MjY3 = ptext[2] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (hbY[i] / (2*hcY[i]) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[2]))**0.5)
            MjY4 = ptext[3] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (hbY[i] / (2*hcY[i]) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[3]))**0.5)
            MjY5 = ptext[4] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (hbY[i] / (2*hcY[i]) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[4]))**0.5)
            MjY6 = ptext[5] * bjY * hcY[i] * (hstorey * jY / (hstorey - jY)) * (hbY[i] / (2*hcY[i]) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[5]))**0.5)

        elif FlagType[i] == 3: # Roof joint
            MjX1 = 2 * ptext[0] * bjX * hcX[i] * jX * ((hbX[i] / (2*hcX[i])) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[0]))**0.5)
            MjX2 = 2 * ptext[1] * bjX * hcX[i] * jX * ((hbX[i] / (2*hcX[i])) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[1]))**0.5)
            MjX3 = 2 * ptext[2] * bjX * hcX[i] * jX * ((hbX[i] / (2*hcX[i])) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[2]))**0.5)
            MjX4 = 2 * ptext[3] * bjX * hcX[i] * jX * ((hbX[i] / (2*hcX[i])) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[3]))**0.5)
            MjX5 = 2 * ptext[4] * bjX * hcX[i] * jX * ((hbX[i] / (2*hcX[i])) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[4]))**0.5)
            MjX6 = 2 * ptext[5] * bjX * hcX[i] * jX * ((hbX[i] / (2*hcX[i])) + ((hbX[i] / (2*hcX[i]))**2 + 1 + P[i] / (bjX * hcX[i] * ptext[5]))**0.5)

            MjY1 = 2 * ptext[0] * bjY * hcY[i] * jY * ((hbY[i] / (2*hcY[i])) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[0]))**0.5)
            MjY2 = 2 * ptext[1] * bjY * hcY[i] * jY * ((hbY[i] / (2*hcY[i])) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[1]))**0.5)
            MjY3 = 2 * ptext[2] * bjY * hcY[i] * jY * ((hbY[i] / (2*hcY[i])) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[2]))**0.5)
            MjY4 = 2 * ptext[3] * bjY * hcY[i] * jY * ((hbY[i] / (2*hcY[i])) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[3]))**0.5)
            MjY5 = 2 * ptext[4] * bjY * hcY[i] * jY * ((hbY[i] / (2*hcY[i])) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[4]))**0.5)
            MjY6 = 2 * ptext[5] * bjY * hcY[i] * jY * ((hbY[i] / (2*hcY[i])) + ((hbY[i] / (2*hcY[i]))**2 + 1 + P[i] / (bjY * hcY[i] * ptext[5]))**0.5)
        
        return MjX1, MjX2, MjX3, MjX4, MjX5, MjX6, MjY1, MjY2, MjY3, MjY4, MjY5, MjY6
