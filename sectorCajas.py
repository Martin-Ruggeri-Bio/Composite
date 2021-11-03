from composite import Composite


class SectorCajas(Composite):
    def __init_(self, cantidadCajeros = 0):
        super().__init__()
        self._cantidadCajeros = cantidadCajeros

    @property
    def cantidadCajeros(self):
        return self._cantidadCajeros

    @cantidadCajeros.setter
    def setcantidadCajeros(self,cantidadCajeros):
        self._cantidadCajeros=cantidadCajeros
