from iSueldo import ISueldo


class  Empleado(ISueldo):
    def __init__(self, nombreCompleto, cargo, sueldo,):
        super().__init__(sueldo)
        self._nombreCompleto = nombreCompleto
        self._cargo = cargo

    @property
    def nombreCompleto(self):
        return self._nombreCompleto

    @nombreCompleto.setter
    def setnombreCompleto(self,nombreCompleto):
        self._nombreCompleto=nombreCompleto
    
    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def setcargo(self,cargo):
        self._cargo=cargo
