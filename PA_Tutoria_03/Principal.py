#Principal
from Paquete_1.modelado import *
d = Docente("Docente BD", "Loja")
d2 = Docente("Docente Prog", "Quito")

listado = [d, d2]

e = Estudiante("Lucho", listado)
print(e.presentarDatos())