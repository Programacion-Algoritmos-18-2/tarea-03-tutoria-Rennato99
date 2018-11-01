#Modelado
class Docente:				# Creando la clase Docente

	def __init__(self, n, a):  # Constructor que recibe dos argumentos
		self.name = n          
		self.city = a

	def setName(self, n):  # Metodo set del atributo name
		self.name = n

	def setCity(self, a):  # Metodo set del atributo city
		self.city = a

	def getName(self):     # Metodo get del atributo name
		return self.name

	def getCity(self):     # Metodo get del atributo city
		return self.city

	def presentData(self):    # Metodo para presentar los datos
		string = "%s\n\t%s" % (self.getName(), self.getCity())    # Foramteamos la cadena
		return string

class Estudiante:

	def __init__(self, n, lista_docentes):   # Constructor que recibe dos argumentos
		self.names = n
		self.docentes = lista_docentes

	def setNames(self, n):  # Metodo set del argumetno name
		self.names = n

	def setDocentes(self, lista_docentes):  # Metodo set del argumetno docentes
		self.docentes = lista_docentes

	def getNames(self):  # Metodo get del argumento names
		return self.names

	def getDocentes(self):  # Metodo get del argumento docentes
		return self.docentes

	def presentData(self):   # Metodo para presentar los datos
		cadena = "Estudiante: %s" % (self.getNames())
		cadena = "%s\nLista Docentes:" % (cadena)
		for i in range(len(self.docentes)): # Recorre la lista de docentes y los presenta a cada uno
			cadena = "%s\n\t%s\t%s" % (cadena, self.docentes[i].getName(), self.docentes[i].getCity())
		return cadena

