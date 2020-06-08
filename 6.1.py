import math

from abc import ABC,abstractmethod
class Figure(ABC):

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        super().__init__()

    def plosha(self, radius, height):
        raise NotImplementedError

    def ob6em(self, radius, height):
        raise NotImplementedError

class Culindr(Figure):
    def __init__(self,*args):
        super().__init__(args)

    def S_bokovoe_culindr(self):
        plosha_bokovoe = 2 * math.pi * self.radius * self.height
        return plosha_bokovoe

    def S_polnoe_culindr(self):
        plosha_polnoe = self.S_bokovoe_culindr + 2 * math.pi * self.radius ^ 2
        return plosha_polnoe

    def V_culindr(self):
        V_culindra = math.pi * self.radius ^ 2 * self.height
        return V_culindra
    super().__init__(self.radius,self.height)

class Konys(Figure):
    def __init__(self, *args):
        super().__init__(args)

    def S_polnoe_konys(self):
        polnoe_konys = math.pi*self.radius * (self.radius + self.height)
        return polnoe_konys
    def V_konys(self):
        v_konys = (self.height/3) * math.pi * self.radius
        return v_konys
    super().__init__(self.radius,self.height)

class Elipt_culindr(Culindr):
    def __init__(self, *args):
        super().__init__(args)

    def set_E(self, E):
        self._E = E

    def set_a(self, a):
        self._a = a

    def set_b(self, b):
        self._b = b

    def S_elipt(self):
        S_elipt_culindr = (4 * self._a * self.height * self._E)*((math.sqrt(self._a ^
                                                                      2-self._b ^ 2)/self._a), math.pi/2)+2*math.pi*self._a*self._b
        return S_elipt_culindr

    def V_elipt(self):
        V_elipt_culindr = math.pi * self._a * self._b * self.height
        return V_elipt_culindr
    super().__init__(self._b,self._a,self._E)
