from composite import Composite


class SectorAdministrativo(Composite):
    def __init__(self, cantAdmin = 0):
        super().__init__()
        self._cantAdmin = cantAdmin

    @property
    def cantAdmin(self):
        return self._cantAdmin

    @cantAdmin.setter
    def setcantAdmin(self,cantAdmin):
        self._cantAdmin=cantAdmin
