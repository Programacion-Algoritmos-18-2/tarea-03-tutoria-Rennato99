#Principal
from Paquete_1.modelado import *
teacher1 = Docente("Docente BD", "Loja")
teacher2 = Docente("Docente Prog", "Quito")

listado = [teacher1, teacher2]

student = Estudiante("Lucho", listado)
print(student.presentData())