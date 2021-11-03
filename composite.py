from iSueldo import ISueldo


class Composite(ISueldo):
    def __init__(self, sueldo=0, empleado=[]):
        super().__init__(sueldo)
        self.empleado = empleado

    def getSueldo(self):
        sumador = 0
        for i in range(len(self.empleado)):
            sumador = sumador + int(self.empleado[i].sueldo)
        return sumador
    
    def agregar(self, p={}):
        self.empleado.append(p)
