from milestone1_geometry import Geometry
from milestone1_Bundles import Bundles
import math as m


class Line:
    # Constants in the particular system we are solving
    w = 377
    j = 1j
    s_base = 100

    def __init__(self, name: str, length: float, linegeometry: Geometry, linebundle: Bundles, bus1: str, bus2: str,
                 v_base: float):
        self.name: str = name
        self.length: float = length
        self.bus1: str = bus1
        self.bus2: str = bus2
        self.v_base: float = v_base

        self.deq = linegeometry.deq * 12  # convert to ft
        self.dsl = linebundle.dsl
        self.dsc = linebundle.dsc

        self.L = Line.findL(self)  # finds inductance in ohms
        self.C = Line.findC(self)  # finds capacitance in ohms

        Zbase = (self.v_base ** 2) / Line.s_base

        self.Rpu = (linebundle.R / Zbase) * self.length # Resistance in per unit
        self.Xpu = ((self.L * Line.w) / Zbase)  # X in per unit
        self.Bpu = ((self.C * Line.w) * Zbase)   # B in per unit
        print("Rpu = ", self.Rpu, "   Xpu = ", self.Xpu, "   Bpu = ", self.Bpu)

    def findL(self):
        Din = self.deq / self.dsl
        L = (2 * (10 ** (-7)) * m.log(Din)) * self.length
        return L

    def findC(self):
        Din = self.deq / self.dsc
        e0 = 8.854187812 * (10 ** (-12))  # definition
        C = ((2) * (m.pi) * (e0)) / (m.log(Din)) * self.length * 1609.344
        return C
