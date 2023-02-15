import math as m
import numpy as n

# This class calculates the equivelent distance, deq, between three
# phases of a particular conductor, depending on the coordinates for
# each phase passed through the class
class Geometry:
    def __init__(self, phasea_x: float, phasea_y: float, phaseb_x: float,
                 phaseb_y: float, phasec_x: float, phasec_y: float):

        self.phasea_x: float = phasea_x
        self.phaseb_x: float = phaseb_x
        self.phasec_x: float = phasec_x
        self.phasea_y: float = phasea_y
        self.phaseb_y: float = phaseb_y
        self.phasec_y: float = phasec_y
        self.deq = Geometry.find_deq(self)

    # finding DEQ and returning it as a class variable
    def find_deq(self):
        dab_x = self.phasea_x - self.phaseb_x
        dab_y = self.phasea_y - self.phaseb_y
        dab = m.sqrt((dab_x ** 2) + (dab_y ** 2))

        dbc_x = self.phaseb_x - self.phasec_x
        dbc_y = self.phaseb_y - self.phasec_y
        dbc = m.sqrt((dbc_x ** 2) + (dbc_y ** 2))

        dca_x = self.phasec_x - self.phasea_x
        dca_y = self.phasec_y - self.phasea_y
        dca = m.sqrt((dca_x ** 2) + (dca_y ** 2))

        deq = n.cbrt(dab * dbc * dca)
        return deq
