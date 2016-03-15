import math

def flotante(n):
	"""
	Evalua si el numero que se ingresa es mayor o menor a 0 para definir el bit mas significativo de la cadena del
	numero decimal.
	Entero toma el valor de la funcion dec2bin con el valor absoluto del numero decimal a convertir
	decimal.
	Exp  llama a la funcion recursiva dec2bin, toma el valor de 8 bits mas la longitud de la cadena "entero" 
	menos uno para formar el exponente.
	decimal toma el valor de la llamada a la funcion frac2bin con la resta del valor absoluto del numero decimal menos
	el número m

	Regresa la cadena de signo, exp decimal y la longitud de la cadena decimal mas la cadena entero menos 1 para formar
	las cifras significativas.

	"""

	if n < 0:
		signo = [1]
	else:
		signo = [0]
	entero = dec2bin(math.floor(abs(n)), [])
	decimal = frac2bin(abs(n)-math.floor(abs(n)))
	exp = dec2bin(127 + (len(entero) -1), [])
	return signo + exp + entero[1:] + decimal + [0]*(23-(len(decimal) + len(entero) - 1))

def dec2bin(n, l):
	"""

	Toma el valor en decimal y concatena a la cadena con el numero binario el bit mas significativo que define el signo 
	con los valores del modulo de la division entre dos del numero decimal, se llama recursivamente la funcion dec2bin 
	hasta que el numero en decimal es menor o igual 1, desenvolviendo y regresando el uno de residuo e invirtiendo la cadena resultante. 

	"""
	l.append(n%2)
	n = int(n/2)
	if n>1:
		dec2bin(n, l)
	return [1] + l[::-1]

def bin2dec(n):
	"""
	Toma inicialmente el valor de dec como cero, itera sobre la longtud del numero binario elevando 2 al numero
	correspondiente de la iteracion para así sumarlo al valor de dec. 

	Se usa el algoritmo standard de conversion de binario a decimal 

	"""
	dec = 0
	n = n[::-1]
	for i in range(0,len(n)):
		dec = dec + int(n[i])*(2**i)
	return dec

def frac2bin(n):
	"""
	Itera sobre el numero de bits, concatena a la cadena "bits" el numero entero mas proximo de n (piso), le resta
	ese mismo numero a n.

	Regresa el contenido de bits
	"""

	bits = []
	while len(bits) < 23 and n != 0:
		n = n*2
		bits.append(math.floor(n))
		n = n - math.floor(n)
	return bits

def decimal(n):
	"""
	
	"""

	exp = bin2dec(n[1:9]) - 127
	frac = 1
	for (e,i) in zip(n[9:32], [x for x in range(1,23)]):
		frac = frac + int(e)*(1/(2**(i)))
	dec = ((-1)**int(n[0]))*frac*(2**exp)
	return dec

def main_menu():
	op = 1
	"""
	Menu que manda a llamar a las funciones dependiendo de el numero seleccionado, si se introduce 0 se termina la ejecucion del programa. 
	"""
	while op != 0:
		print("\n1) Decimal a binario \n2) Binario a decimal\n")
		op = int(input('-> '))
		if op > 0 and op < 3:
			if op == 1:
				resultado = flotante(float(input("\nIngrese el numero en decimal a convertir:\n -> ")))
				print("\nNumero binario: \n"+''.join(str(e) for e in resultado))
			if op == 2: 
				resultado = decimal(list(input("\nIngrese el numero binario a convertir:\n -> ")))
				print("\nNumero decimal: %e\n"% resultado)
		else:
			print("Verifica tu eleccion")

main_menu()