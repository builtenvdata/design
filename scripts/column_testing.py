# flake8: noqa
# import libraries
# ------------------------------------------------------------------------
# A library to use OpenSees via Python
import openseespy.opensees as ops
# A library provides high-performance vector, matrix and higher-dimensional data structures for Python
import numpy as np
# A Library to visualize data from Python
import matplotlib.pyplot as plt


ctrlNode = 1001
ctrlDof = 2
dMax = 1.0
dU = 0.001  # displacement increment
HingeI = 170001
HingeJ = 121001
Mfact = 10

ops.wipe()
ops.model('basic', '-ndm', 3, '-ndf', 6)

# Geometric transformations
ops.geomTransf('Linear', 88888, 0, -1, 0)
ops.geomTransf('Linear', 77777, 1, 0, 0)
ops.geomTransf('Linear', 99999, -1, 0, 0)
ops.geomTransf('PDelta', 66666, -1, 0, 0)

# Rigid-like material and section
ops.uniaxialMaterial('Elastic', 99999, 1000000000.0)
ops.section('Aggregator', 99999, 99999, 'P', 99999, 'Vy',  99999, 'Vz', 99999, 'My', 99999, 'Mz', 99999, 'T')

# Foundation or support under the column 1
# Fixed node
ops.node(1, 0.0, 0.0, 0.0)
ops.fix(1, 1, 1, 1, 1, 1, 1)
# Foundation node
ops.node(70001, 0.0, 0.0, 0.0, '-mass', 0.3412844036697248, 0.3412844036697248, 0.3412844036697248, 0.0, 0.0, 0.0)
ops.equalDOF(1, 70001, 1, 2, 3, 4, 5, 6)

# Joint grid ids (x, y, z): (0, 0, 1)
# Central joint node
ops.node(1001, 0.0, 0.0, 3.1, '-mass', 9.719495412844037, 9.719495412844037, 9.719495412844037, 0.0, 0.0, 0.0)
# Rigid-joint offset elements
ops.node(21001, 0.0, 0.0, 2.85)
ops.element('elasticBeamColumn', 21001, 21001, 1001, 99999, 99999)

# Create elastic column element nodes
ops.node(170001, 0.0, 0.0, 0.0)
ops.node(121001, 0.0, 0.0, 2.85)
# Create elastic column element
ops.element('elasticBeamColumn', 1, 170001, 121001, 0.1225, 28442268.75364299, 11850945.31401791, 0.00211338, 0.00137557, 0.00137557, 66666)
# Create materials describing flexural behaviour of plastic hinge
ops.uniaxialMaterial('Hysteretic', 20001, Mfact*131.72414555, 0.00118306, Mfact*159.70443413, 0.01990494, Mfact*15.97044341, 0.0676644, Mfact*-131.72414555, -0.00118306, Mfact*-159.70443413, -0.01990494, Mfact*-15.97044341, -0.0676644, 1.0, 1.0, 0.0, 0.0, 0.0)
ops.uniaxialMaterial('Hysteretic', 10001, Mfact*116.40545358, 0.00118306, Mfact*141.13181009, 0.01990494, Mfact*14.11318101, 0.0676644, Mfact*-116.40545358, -0.00118306, Mfact*-141.13181009, -0.01990494, Mfact*-14.11318101, -0.0676644, 1.0, 1.0, 0.0, 0.0, 0.0)
# Create new materials describing shear behaviour of plastic hinge
ops.limitCurve('ThreePoint', 20001, 1, -10, 141.52187535, 0, 141.52187535, 10, 141.52187535, -2040.35391729, 0.05*141.52187535, 2, 0, 70001, 21001, 2, 3)
ops.uniaxialMaterial('LimitState', 40001, 35.38046884, 9.066e-05, 106.14140652, 0.00027198, 353.80468838, 0.0009066, -35.38046884, -9.066e-05, -106.14140652, -0.00027198, -353.80468838, -0.0009066, 0.4, 0.3, 0.003, 0.0, 0.0, 20001, 2)
ops.limitCurve('ThreePoint', 10001, 1, -10, 141.52187535, 0, 141.52187535, 10, 141.52187535, -2040.35391729, 0.05*141.52187535, 2, 0, 70001, 21001, 1, 3)
ops.uniaxialMaterial('LimitState', 30001, 35.38046884, 9.066e-05, 106.14140652, 0.00027198, 353.80468838, 0.0009066, -35.38046884, -9.066e-05, -106.14140652, -0.00027198, -353.80468838, -0.0009066, 0.4, 0.3, 0.003, 0.0, 0.0, 10001, 2)
# Create plastic hinge sections at both ends
ops.section('Aggregator', 1, 99999, 'P', 40001, 'Vy', 30001, 'Vz', 20001, 'My', 10001, 'Mz', 99999, 'T')
# Create plastic hinge elements at both ends
ops.element('zeroLengthSection', 170001, 70001, 170001, 1, '-orient', 0, 0, 1, 0, 1, 0)
ops.element('zeroLengthSection', 121001, 121001, 21001, 1, '-orient', 0, 0, 1, 0, 1, 0)


# Define the load pattern
# ------------------------------------------------------------------------
ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)
if ctrlDof == 1:
    ops.load(ctrlNode, 1, 0, 0, 0, 0, 0)
elif ctrlDof == 2:
    ops.load(ctrlNode, 0, 1, 0, 0, 0, 0)

# Set analysis settings
# ------------------------------------------------------------------------
# Wipe any previous analysis object
ops.wipeAnalysis()

# Convergence Test -- determines when convergence has been achieved.
tol = 1.0e-8  # Set the tolerance (default)
iterMax = 50  # Set the max bumber of iterations (default)
pFlag = 0     # Optional print flag (default is 0). Valid options: 0-5
nType = 2     # optional type of norm (default is 2). Valid options: 0-2
ops.test('NormDispIncr', tol, iterMax, pFlag, nType)

# SolutionAlgorithm -- determines the sequence of steps taken to solve the non-linear equation at the current time step
ops.algorithm('KrylovNewton')

# DOF_Numberer -- determines the mapping between equation numbers and degrees-of-freedom
ops.numberer('RCM')

# SystemOfEqn/Solver -- within the solution algorithm, it specifies how to store and solve the system of equations in the analysis
ops.system('UmfPack')

# Constraints handler: determines how the constraint equations are enforced in the analysis -- how it handles the boundary conditions/imposed displacements
ops.constraints('Transformation')

# Integrator -- determines the predictive step for time t+dt
ops.integrator('DisplacementControl', ctrlNode, ctrlDof, dU)

# AnalysisType -- defines what type of analysis is to be performed ('Static', 'Transient' etc.)
ops.analysis('Static')

# Initialize some parameters
# ------------------------------------------------------------------------
HingeForcesI = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
HingeForcesJ = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
HingeDefI = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
HingeDefJ = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
disp = 0.0
ok = 0

# Perform step by step analysis
# ------------------------------------------------------------------------
while ok == 0 and disp < dMax:
    ok = ops.analyze(1)
    disp = ops.nodeDisp(ctrlNode, ctrlDof)

    HingeForcesI.append(ops.eleResponse(HingeI, 'localForce'))
    HingeForcesJ.append(ops.eleResponse(HingeJ, 'localForce'))
    HingeDefI.append(ops.eleResponse(HingeI, 'deformation'))
    HingeDefJ.append(ops.eleResponse(HingeJ, 'deformation'))
    if ok != 0:
        print("DispControl Analysis is FAILED")
        print("Analysis failed at nSteps: %s" % (disp))
        print('-------------------------------------------------------------------------')
        break

HingeForcesI = np.array(HingeForcesI)
HingeForcesJ = np.array(HingeForcesJ)
HingeDefI = np.array(HingeDefI)
HingeDefJ = np.array(HingeDefJ)

plt.figure()
plt.plot(HingeDefI[:, 3], HingeForcesI[:, 3], label='Hinge-I')
# plt.plot(HingeDefJ[:, 3], HingeForcesJ[:, 3], label='Hinge-J')
plt.xlabel('Theta-y')
plt.ylabel('Moment-y')
plt.legend()

plt.figure()
plt.plot(HingeDefJ[:, 1], HingeForcesJ[:, 1], label='Hinge-J')
plt.xlabel('dy')
plt.ylabel('Vy')
plt.legend()

plt.figure()
plt.plot(HingeDefI[:, 4], HingeForcesI[:, 4], label='Hinge-I')
# plt.plot(HingeDefJ[:, 4], HingeForcesJ[:, 4], label='Hinge-J')
plt.xlabel('Theta-z')
plt.ylabel('Moment-z')
plt.legend()

plt.figure()
plt.plot(HingeDefJ[:, 2], HingeForcesJ[:, 2], label='Hinge-J')
plt.xlabel('dz')
plt.ylabel('Vz')
plt.legend()
plt.show()

print('pause')
