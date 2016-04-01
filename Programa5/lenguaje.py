import re

def evalExp(exp):

	ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "=": (lambda x,y: int(x==y)), "<=": (lambda x,y: int(x<=y)),
			"<": (lambda x,y: int(x<y)), "v": (lambda x,y: x or y), "^": (lambda x,y: x and y), "¬": (lambda x: int(not x))}

	pilaDatos = []
	pilaOp = []

	i = 0
	x, y = 0, 0

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
				if ord(exp[i])==61:
					pilaOp.append('=')
					i+=1
				elif ord(exp[i])==60 and ord(exp[i+1])==61:
					pilaOp.append('<=')
					i+=1
				elif ord(exp[i])==60:
					pilaOp.append('<')
				elif ord(exp[i])==118:
					pilaOp.append('v')
				elif ord(exp[i])==94:
					pilaOp.append('^')
				elif ord(exp[i])==172:
					pilaOp.append('¬')
				else:
					pilaOp.append(exp[i])
				print(pilaOp)
		elif exp[i] == ')':
			x = int(pilaDatos.pop())
			y = int(pilaDatos.pop())
			pilaDatos.append(ops[pilaOp.pop()] (y,x))
			print(pilaDatos)
		#print("Actual: " + str(exp[i]))
		i+=1
	return pilaDatos, pilaOp

def main_menu():

	res = evalExp(str(input("\nIngrese la expresion a evaluar -> ")))

	if len(res[0]) == 1 and len(res[1]) == 0:
		print("\nResultado de la expresion: " + "True" if res[0].pop() == 1 else "False")
	else:
		print("\nExpresion no valida")

main_menu()