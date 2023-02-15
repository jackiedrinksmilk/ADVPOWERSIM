from milestone1_ConductorData import ConductorData
import math as m
import numpy as n


# class is for calculatting dsl and dsc values depending on the number of bundles and conductor data class

class Bundles:
    def __init__(self, num: int, conductorData: ConductorData, d: float):

        if num < 1 or num > 4:
            print("invalid input for number of bundles. bundle not created")

        else:
            self.num: int = num
            self.d: float = d
            self.conductorData: ConductorData = conductorData

            self.R = self.conductorData.r / self.num
            self.gmr = self.conductorData.gmr
            self.cond_res = conductorData.res
            self.dsl = Bundles.find_dsl(self)
            self.dsc = Bundles.find_dsc(self)
            self.res = self.cond_res / self.num

    # function for finding DSL depending on bundle number
    def find_dsl(self) -> float:

        if self.num == 1:
            dsl = self.gmr
        if self.num == 2:
            dsl = m.sqrt(self.gmr * self.d)
        if self.num == 3:
            dsl = n.cbrt(self.gmr * (self.d ** 2))
        if self.num == 4:
            dsl = 1.0941 * m.pow((self.gmr * (self.d ** 3)), (0.25))

        return dsl

    # function for finding DSC depending on bundle number
    def find_dsc(self) -> float:
        if self.num == 1:
            dsc = self.R
        if self.num == 2:
            dsc = m.sqrt(self.R * self.d)
        if self.num == 3:
            dsc = n.cbrt(self.R * (self.d ** 2))
        if self.num == 4:
            dsc = 1.0941 * m.pow((self.R * (self.d ** 3)), (0.25))

        return dsc
