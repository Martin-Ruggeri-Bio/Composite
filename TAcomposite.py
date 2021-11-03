from banco import Banco
from sectorAdministrativo import SectorAdministrativo
from sectorCajas import SectorCajas
from sectorContaduria import SectorContaduria
from sectorGerencia import SectorGerencia
from sectorRRHH import SectorRRHH
from empleado import Empleado


if __name__ == "__main__":
        
    banco = Banco()
    administracion = SectorAdministrativo()
    cajas = SectorCajas()
    contaduria = SectorContaduria()
    gerencia = SectorGerencia()
    rrhh = SectorRRHH()
    
    banco.agregar(administracion)
    banco.agregar(contaduria)
    banco.agregar(gerencia)
    administracion.agregar(cajas)
    administracion.agregar(rrhh)
    
    cajero1 = Empleado("Nafer Salas","Cajero", 300)
    cajero2 = Empleado("Diana Roa","Cajero", 300)
    
    cajas.agregar(cajero1)
    cajas.agregar(cajero2)
    
    gerente = Empleado("Alvaro Molina","Gerente", 500)
    gerencia.agregar(gerente)
    
    selector = Empleado("Pedro Cañas","RRHH", 350)
    rrhh.agregar(selector)
    
    contador = Empleado("Monica Ardila","Contador", 380)
    contaduria.agregar(contador)
    
    print(banco.getSueldo())
