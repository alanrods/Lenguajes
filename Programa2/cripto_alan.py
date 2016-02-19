import math 
class Crypto(object):
	def __init__(self):
		self.magic = []
		self.rows = 0
		self.key = 0
		self.user_input = []
		self.crip = []
	
	def data(self, message, key):
		"""Funcion para capturar el mensaje a cifrar y la llave de cifrado
		Se divide el mensaje en una lista para poder manipularlo como matriz."""
		self.crip = []
		self.key = key
		message.split()
		message = message.replace(" ","")
		for word in message:
		   for c in word:
		       self.user_input.append(c)
		return self.user_input

	def cipher(self):
		"""Se manda a llamar recursivamente la funcion para hacerlo una matriz tomando el numero de columnas la llave que se proporciono.
		Se toma una variable auxiliar msn para llenarla con las partes del mensaje (los renglones de la matriz),el mensaje introducido se maneja como una pila 
		y cuando esta pila se encuentra vacia se llenan los espacios restantes en la matriz si es que se necesita """
		msn = []
		if self.user_input:
			for i in range (0, self.key):
				if len(self.user_input) > 0:
					msn.append(self.user_input.pop(0))
				else:
					msn.append('#')
			self.crip.append(msn)
			if len(self.user_input) == 0 :
				pass
			else:
				self.cipher()
		else:
			return False
		return self.by_column()

	def by_column(self):
		""" Devuelve lo que se encuentra en la matriz imprimiendo por columnas"""
		cad = ""
		for i in range(0, len(self.crip[0])): #Columna
			for j in range(0, len(self.crip)): #Renglon
				cad = cad + self.crip[j][i]
		return cad

	def decipher(self, cadena, key):
		self.data(cadena, key)
		return self.by_column()

	#def decipher(self, cadena, key):
	#	tam = len(cadena)
	#	ren = int(math.ceil(tam / float(key))) 
	#	m = []
	#	p = 0
	#	for i in range(0,ren):
	#		m.append([])
	#		p = i
	#		for j in range(0, key):
	#			m[i].append(cadena[p])
	#			p = ren + p 
	#	return m
	
	def by_row(self, ren, col):
		new_cad = ""
		for i in range(0,ren):
			for j in range(0,col):
				new_cad = new_cad + self.magic[i][j]
		return new_cad
	
	def check_key(self, msn):
		if self.key > 0 and self.key <= len(msn):
			return True #La llave es valida
		else:
			return False 