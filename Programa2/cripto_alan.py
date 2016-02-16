import math 
def cipher(msn,key):
	msn = msn.replace(" ","")
	tam = len(msn)	#2
	ren = int(math.ceil(tam/float(key))) 
	res = ren * key - tam
	magic = []
	pos = 0
	for i in range(0,ren):
		magic.append([])
		for j in range(0,key):
			if pos < tam and res!=0:
				magic[i].append(msn[pos])
				pos += 1
			else:
				magic[i].append('#')
	return magic

def by_column(matrix,col,ren):
	cad = ""
	for i in range (0,col):
		for j in range (0,ren):
			cad = cad + matrix[j][i]
	return cad

def decipher(cadena,key):
	tam = len(cadena)
	ren = int(math.ceil(tam/float(key))) 
	m = []
	p = 0
	for i in range (0,ren):
		m.append([])
		p=i
		for j in range (0,key):
			m[i].append(cadena[p])
			p = ren + p 
	return m

def by_row(matrix,ren,col):
	new_cad = ""
	for i in range (0,ren):
		for j in range (0,col):
			new_cad = new_cad + matrix[i][j]
	return new_cad

def check_key(msn,key):
	if key > 0 and key <= len(msn):
		return True #La llave es valida
	else:
		return False 





