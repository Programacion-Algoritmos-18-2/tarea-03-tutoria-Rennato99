#Modelado
class Docente:

	def __init__(self, n, a):
		self.nombre = n
		self.ciudad = a

	def setNombre(self, n):
		self.nombre = n

	def setCiudad(self, a):
		self.ciudad = a

	def getNombre(self):
		return self.nombre

	def getCiudad(self):
		return self.ciudad

	def presentarDatos(self):
		cadena = "%s\n\t%s" % (self.getNombre(), self.getCiudad())

class Estudiante:

	def __init__(self, n, lista_docentes):
		self.nombres = n
		self.docentes = lista_docentes

	def setNombres(self, n):
		self.nombres = n

	def setDocentes(self, lista_docentes):
		self.docentes = lista_docentes

	def getNombres(self):
		return self.nombres

	def getDocentes(self):
		return self.docentes

	def presentarDatos(self):
		cadena = "Estudiante: %s" % (self.getNombres())
		cadena = "%s\nLista Docentes:" % (cadena)
		for i in range(len(self.docentes)):
			print(i)
			cadena = "%s\n\t%s\t%s" % (cadena, self.docentes[i].getNombre(), self.docentes[i].getCiudad())
		return cadena

