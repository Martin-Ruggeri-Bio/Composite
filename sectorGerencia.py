from composite import Composite


class SectorGerencia(Composite):
    def __init_(self, cantidadGerencia = 0):
        super().__init__()
        self._cantidadGerencia = cantidadGerencia

    @property
    def cantidadGerencia(self):
        return self._cantidadGerencia

    @cantidadGerencia.setter
    def setcantidadGerencia(self,cantidadGerencia):
        self._cantidadGerencia=cantidadGerencia
