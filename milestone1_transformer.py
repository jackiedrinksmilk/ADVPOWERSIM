import numpy as n

# This class is for Transformer elements
# they have two rated voltages, one high and low (v1 and v2)
# as well as a rated power, per unit impedence z and an x/r ratio
class Transformer:

    # constant values
    w = 377
    j = 1j
    s_base = 100.0

    def __init__(self, name: str, bus1: str, bus2: str, rated_power: float, v1: float, v2: float, z: float, xr: float):

        self.name: str = name
        self.rated_power: float = rated_power
        self.v1: float = v1
        self.v2: float = v2
        self.z: float = z
        self.xr: float = xr
        self.bus1: str = bus1
        self.bus2: str = bus2

        self.v_base = v2

        # calculating R + jX
        self.R = self.z * ((self.v2 ** 2) / self.rated_power)/(self.v_base * (self.v_base/Transformer.s_base)) * n.cos(n.arctan(self.xr))
        self.X = self.z * ((self.v2 ** 2) / self.rated_power)/(self.v_base * (self.v_base/Transformer.s_base)) * n.sin(n.arctan(self.xr))

