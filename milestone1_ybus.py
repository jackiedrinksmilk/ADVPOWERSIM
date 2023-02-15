from milestone1_line import Line
from milestone1_transformer import Transformer
from milestone1_Bundles import Bundles
from milestone1_geometry import Geometry
from milestone1_Generator import Generator
from milestone1_Bus import Bus

from typing import Dict, List

import numpy as n


class YBus:
    j = 1j

    def __init__(self, name: str):
        self.name: str = name
        self.buses_order: List[str] = list()
        self.buses: Dict[str, Bus] = dict()

        self.lines: Dict[str, Line] = dict()
        self.transformers: Dict[str, Transformer] = dict()
        self.generators: Dict[str, Generator] = dict()

    def calculate_Ybus_matrix(self):

        # given d = 1.5 in
        # n bundles = 2

        # From ACSR Table
        # r = 0.321 in, gmr = .0216 ft, R = 0.465

        # initializing square matrix size of number of busses, initializing all values to zero
        Y_Bus_matrix = n.zeros((len(self.buses_order), len(self.buses_order)), dtype=complex)

        # finding admittances for THIS SPECIFIC network
        # on non diagonals, y = -1/z
        Y_Bus_matrix[0][1] = -1 / (self.transformers["T1"].R + (YBus.j * self.transformers["T1"].X))  # T1 connected between bus 1 and 2
        Y_Bus_matrix[1][2] = -1 / (self.lines["L2"].Rpu + (YBus.j * self.lines["L2"].Xpu))
        Y_Bus_matrix[3][1] = -1 / (self.lines["L1"].Rpu + (YBus.j * self.lines["L1"].Xpu))
        Y_Bus_matrix[4][2] = -1 / (self.lines["L3"].Rpu + (YBus.j * self.lines["L3"].Xpu))
        Y_Bus_matrix[4][3] = -1 / (self.lines["L6"].Rpu + (YBus.j * self.lines["L6"].Xpu))
        Y_Bus_matrix[5][3] = -1 / (self.lines["L4"].Rpu + (YBus.j * self.lines["L4"].Xpu))
        Y_Bus_matrix[5][4] = -1 / (self.lines["L5"].Rpu + (YBus.j * self.lines["L5"].Xpu))
        Y_Bus_matrix[6][5] = -1 / (self.transformers["T2"].R + (YBus.j * self.transformers["T2"].X))

        # setting symmetry
        Y_Bus_matrix[1][0] = Y_Bus_matrix[0][1]
        Y_Bus_matrix[2][1] = Y_Bus_matrix[1][2]
        Y_Bus_matrix[1][3] = Y_Bus_matrix[3][1]
        Y_Bus_matrix[2][4] = Y_Bus_matrix[4][2]
        Y_Bus_matrix[3][4] = Y_Bus_matrix[4][3]
        Y_Bus_matrix[3][5] = Y_Bus_matrix[5][3]
        Y_Bus_matrix[4][5] = Y_Bus_matrix[5][4]
        Y_Bus_matrix[5][6] = Y_Bus_matrix[6][5]

        # Setting Diagonals, equal to all impedances connected to bus number
        Y_Bus_matrix[0][0] = -Y_Bus_matrix[0][1]
        Y_Bus_matrix[1][1] = -Y_Bus_matrix[0][1] - Y_Bus_matrix[1][3] - Y_Bus_matrix[1][2] + (
                    (YBus.j * self.lines["L1"].Bpu) / 2) + ((YBus.j * self.lines["L2"].Bpu) / 2)
        Y_Bus_matrix[2][2] = -Y_Bus_matrix[1][2] - Y_Bus_matrix[2][4] + ((YBus.j * self.lines["L2"].Bpu) / 2) + (
                    (self.lines["L3"].Bpu) / 2)
        Y_Bus_matrix[3][3] = -Y_Bus_matrix[3][1] - Y_Bus_matrix[4][3] - Y_Bus_matrix[5][3] + (
                    (YBus.j * self.lines["L1"].Bpu) / 2) + ((YBus.j * self.lines["L4"].Bpu) / 2)
        Y_Bus_matrix[4][4] = -Y_Bus_matrix[4][2] - Y_Bus_matrix[4][3] - Y_Bus_matrix[5][4] + (
                    (YBus.j * self.lines["L3"].Bpu) / 2) + ((YBus.j * self.lines["L5"].Bpu) / 2)
        Y_Bus_matrix[5][5] = -Y_Bus_matrix[5][3] - Y_Bus_matrix[5][4] - Y_Bus_matrix[6][5] + (
                    (YBus.j * self.lines["L4"].Bpu) / 2) + ((YBus.j * self.lines["L5"].Bpu) / 2)
        Y_Bus_matrix[6][6] = -Y_Bus_matrix[5][6]

        print("Y-Bus matrix: ")
        r = 0
        while (r < 7):
            c = 0
            print("\nRow " + str(r+1))
            while (c < 7):
                print(Y_Bus_matrix[r][c])
                c = c + 1
            r = r + 1

        return Y_Bus_matrix

        # method for adding a bus if it is not already added

    def addbus(self, bus: str):

        if bus not in self.buses.keys():
            self.buses[bus] = Bus(bus)
            self.buses_order.append(bus)

    # method for adding line if it is not already added, and creating busses
    def addline(self, name: str, length: float, linegeometry: Geometry, linebundle: Bundles,
                bus1: str, bus2: str, v_base: float):
        if name not in self.lines.keys():
            v_base = self.transformers[list(self.transformers.keys())[0]].v2
            self.lines[name] = Line(name, length, linegeometry, linebundle, bus1, bus2, v_base)
            self.addbus(bus1)
            self.addbus(bus2)

    def addtransformer(self, name: str, bus1: str, bus2: str, rated_power: float, v1: float, v2: float,
                       z: float, xr: float):
        if name not in self.transformers.keys():
            self.transformers[name] = Transformer(name, bus1, bus2, rated_power, v1, v2, z, xr)
            self.addbus(bus1)
            self.addbus(bus2)

    def addgenerator(self, name: str, bus: str, rated_power: float):

        if name not in self.generators.keys():
            self.generators[name] = Generator(name, bus, rated_power)
            self.addbus(bus)
