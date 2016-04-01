# Programa que evalua expresiones booleanas bien formadas en el lenguaje propuesto

# Desarrollado por:
# Moreno Tagle Raphael Ivan
# Plata Martinez Jesus Alejandro
# Rodriguez Bribiesca Isaac
# Rodriguez Garcia Alan Julian

def evalExp(exp):
	"""
	Esta función permite ir recorriendo caracter por caracter la cadena que el usuario desea evaluar. 

	Se define un diccionario para una evaluacion mas optima de las expresiones. Las claves de dicho diccionario corresponden 
	a los operandos que se definieron en el lenguaje para expresiones aritmeticas y para las expresiones booleanas. Así mismo, los valores 
	asociados a dichas claves estan dados por funciones lambda que permiten obtener el resultado de la operacion correspondiente con los 
	operandos dados.

	El programa reconoce los valores de verdad como T para verdadero y F para falso en la cadena de entrada.

    	De acuerdo con el algoritmo simplificado Shunting-yard se definen dos listas que tienen la funcion de las pilas de operandos y 
        operadores. Se va iterando la cadena de entrada, ignorando parentesis de apertura, reconociendo si se trata de un valor numerico 
	o de un operando y recuerriendo al diccionario para obtener la evaluacion de subexpresiones. Para los valores booleanos, se 
        considera el uso de valores numericos 0 y 1 asociados a T y F.

    	La funcion devuelve las pilas de operandos y operadores para su posterior analisis de acuerdo al algoritmo
	"""
	ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "=": (lambda x,y: int(x==y)), "<=": (lambda x,y: int(x<=y)),
			"<": (lambda x,y: int(x<y)), "v": (lambda x,y: x or y), "^": (lambda x,y: x and y), "¬": (lambda x: int(not x))}

	pilaDatos = []
	pilaOp = []
	i=0
	while i<len(exp): 
		if exp[i] != '(' and exp[i] != ')':
			if (ord(exp[i])>47 and ord(exp[i])<58) or exp[i]=='F' or exp[i]=='T':
				if exp[i]=='F':
					pilaDatos.append(0)
					print(pilaDatos)
				elif exp[i]=='T':
					pilaDatos.append(1)
					print(pilaDatos)
				else:
					pilaDatos.append(exp[i])
					print(pilaDatos)
			else:
				if exp[i]=='=':
					pilaOp.append('=')
					i+=1
				elif exp[i]=='<' and exp[i+1]=='=':
					pilaOp.append('<=')
					i+=1
				elif exp[i]=='<':
					pilaOp.append('<')
				elif exp[i]=='v':
					pilaOp.append('v')
				elif exp[i]=='^':
					pilaOp.append('^')
				elif exp[i]=='¬':
					pilaOp.append('¬')
				else:
					pilaOp.append(exp[i])
				print(pilaOp)
		elif exp[i] == ')':
			if pilaOp[len(pilaOp)-1] == '¬':
				x = int(pilaDatos.pop())
				pilaDatos.append(ops[pilaOp.pop()] (x))
				print(pilaDatos)
			else:
				x = int(pilaDatos.pop())
				y = int(pilaDatos.pop())
				pilaDatos.append(ops[pilaOp.pop()] (y,x))
				print(pilaDatos)
		#print("Actual: " + str(exp[i]))
		i+=1
	return pilaDatos, pilaOp

def main_menu():
	"""
	Se recibe la cadena de entrada y se manda a llamar la funcion para evaluarla.

	Al obtener las pilas de operandos y operadores resultado del llamado a la funcion, se determina si la cadena esta bien formada
	o si fue ingresada una cadena incorrecta.
	"""
	res = evalExp(str(input("\nIngrese la expresion a evaluar -> ")))

	if len(res[0]) == 1 and len(res[1]) == 0:
		print("\nResultado de la expresion: " + "True" if res[0].pop() == 1 else "False")
	else:
		print("\nExpresion no valida")

main_menu()
