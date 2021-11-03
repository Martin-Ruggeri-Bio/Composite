from composite import Composite

class Banco(Composite):
    def __init__(self):
        super().__init__()

    def getSueldo(self):
        return super().getSueldo()

    def agregar(self, p=...):
        return super().agregar(p=p)
