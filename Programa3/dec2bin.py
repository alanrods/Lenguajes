# Desarrollado por:
# Moreno Tagle Raphael Ivan
# Plata Martinez Jesus Alejandro
# Rodriguez Bribiesca Isaac
# Rodriguez Garcia Alan Julian

def dec2bin(number, bits): #Esta es la de complemento a 2
	"""
	La funcion dec2bin lo que haces es evaluar si el numero ingresado es negativo o positivo.

	Si es positivo entonces primero obtiene el numero en binario utilizando la funcion bin() y 
	remueve los caracteres "0b" que Python usa para representar un numero binario, tambien
	moviendo el string a la derecha y llenando con 0 usando .rjust completamos los bits en el numero.
	dependiendo del numero que se establecio. 

	Si es negativo seguimos el procedimiento para convertir un binario a complemento a 2:

	Sumamos un 1 al numero que queremos convertir ( en este caso lo restamos ya que se transforma
	el numero deseado a positivo, el resultado sigue siendo el mismo), remueve el caracter "0b", despues 
	agrega '1' a la izquierda dependiendo del numero de bits usando .rjust,
	finalmente realizamos la operacion de complemento a 1

	"""
	if number < 0:
		return complemento1(bin(abs(number) - 1)[2:]).rjust(bits, '1')
	else:
		return bin(number)[2:].rjust(bits, '0') 


def complemento1(value):
	"""
	El complemento a 1 se obtiene intercambiando los valores que encuentra en el string binario iterando sobre 
	el string y cambiando los valores usando un diccionario	(Tabla hash).

	"""
	return ''.join(complement[x] for x in value)


def menu_d2b():
	"""
	Se manda a llamar a las funciones de complemento a 2 y complemento a 1, la funcion regresa dos valores los cuales son usados en el menu principal.
	"""
	print("Ingresa tu numero decimal y numero de bits \n")
	numero = int(input("Numero decimal: "))
	bits = int(input("Numero de bits: "))
	binary1 = dec2bin(numero, bits)
	binary2 = complemento1(binary1)
	return binary1, binary2

def menu_b2d():
	"""
	La funcion menu_b2d cumple la funcion de capturar el numero binario que se sea transformar, si el bit mas significativo es uno entonces se toma como un numero
	negativo, se realiza un shift binario hacia la izquierda, se regresa 1 con un shift a la izquierda en funcion de la longitud de bits del numero binario introducido
	
	Si el bit mas significativo es 0 entonces se toma como un numero positivo y se transforma usando la funcion int(numero_binario, base), se corta el bit mas significativo ya que
	solo se trabajan con los bits de magnitud
	"""
	print("Ingresa tu numero binario, el bit mas significativo es tomado como signo\n")
	numero = str(input("Numero binario: "))
	if numero.startswith('1') is True:
		x = int(numero,2)
		num_bits = len(numero)
		num_dec = (x - (1 << num_bits))
	else:
		num_dec = int(str(numero)[1:], 2)
	return num_dec

def main_menu():
	op = 1
	"""
	Menu que manda a llamar a las funciones dependiendo de el numero seleccionado, si se introduce 0 se termina la ejecucion del programa. 
	"""
	while op != 0:
		print("\n1) Decimal a binario \n2) Binario a decimal\n")
		op = int(input('... '))
		if op > 0 and op < 3:
			if op == 1:
				resultado1, resultado2 = option[str(op)]()
				print("\nComplemento a 2: \n"+resultado1 +"\n\nComplemento a 1:\n"+resultado2)
			if op == 2: 
				resultado = option[str(op)]()
				print("Numero decimal: ")
				print(resultado)
		else:
			print("Verifica tu eleccion")

complement = {'1': '0', '0': '1'}
option = { '1':menu_d2b, '2':menu_b2d}
main_menu()
