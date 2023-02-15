from milestone1_ybus import YBus
from milestone1_ConductorData import ConductorData
from milestone1_geometry import Geometry
from milestone1_Bundles import Bundles

PartridgeData = ConductorData((.0216*12), 0.321, 0.350)
BundledPartridgeData = Bundles(2, PartridgeData, 2.0)
PhaseGeometry = Geometry(0, 0, 9.75, 0, 19.5, 0)

Matrix = YBus("Matrix")

Matrix.addgenerator("G1", "B1", 100)
Matrix.addgenerator("G2", "B7", 100)

Matrix.addtransformer("T1", "B1", "B2", 125, 20, 230, 0.085, 10)
Matrix.addtransformer("T2", "B7", "B6", 200, 18, 230, 0.105, 12)

Matrix.addline("L1", 10, PhaseGeometry, BundledPartridgeData, "B2", "B4", 1.5)
Matrix.addline("L2", 25, PhaseGeometry, BundledPartridgeData, "B2", "B3", 1.5)
Matrix.addline("L3", 20, PhaseGeometry, BundledPartridgeData, "B3", "B5", 1.5)
Matrix.addline("L4", 20, PhaseGeometry, BundledPartridgeData, "B4", "B6", 1.5)
Matrix.addline("L5", 10, PhaseGeometry, BundledPartridgeData, "B5", "B6", 1.5)
Matrix.addline("L6", 35, PhaseGeometry, BundledPartridgeData, "B4", "B5", 1.5)

Ybusmatrix = Matrix.calculate_Ybus_matrix()



