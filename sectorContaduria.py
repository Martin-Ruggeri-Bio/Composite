from composite import Composite


class SectorContaduria(Composite):
    def __init_(self, cantidadContaduria = 0):
        super().__init__()
        self._cantidadContaduria = cantidadContaduria

    @property
    def cantidadContaduria(self):
        return self._cantidadContaduria

    @cantidadContaduria.setter
    def setcantidadContaduria(self,cantidadContaduria):
        self._cantidadContaduria=cantidadContaduria
