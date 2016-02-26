
def dec2bin(number, bits):
	"""
	La funcion dec2bin lo que haces es evaluar si el numero ingresado es negativo o positivo.

	Si es positivo entonces primero obtiene el número en binario utilizando la funcion bin() y 
	remueve los caracteres "0b" que Python usa para representar un numero binario, también
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
	El comlemento a 1 se obtiene intercambiando los valores que encuentra en el string binario iterando sobre 
	el string y cambiando los valores usando un diccionario	(Tabla hash).

	"""
	return ''.join(complement[x] for x in value)

complement = {'1': '0', '0': '1'}

print("Ingresa tu numero decimal y numero de bits \n")
numero = int(input())
bits = int(input())
print('Complemento a 2 \t')
binary1 = dec2bin(numero, bits)
print(binary1)
print('Complemento a 1 \t')
print(complemento1(binary1))