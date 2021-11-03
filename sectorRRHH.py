from composite import Composite


class SectorRRHH(Composite):
    def __init_(self, cantidadRRHH = 0):
        super().__init__()
        self._cantidadRRHH = cantidadRRHH

    @property
    def cantidadRRHH(self):
        return self._cantidadRRHH

    @cantidadRRHH.setter
    def setcantidadRRHH(self,cantidadRRHH):
        self._cantidadRRHH=cantidadRRHH
