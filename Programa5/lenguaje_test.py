"Calular expresiones booleans" 
def bool_Oper(equation, dic):
    """ 
    Cambiamos cada uno de los elementos operadorees 'formales' a argumentos con las que pueda trabajar python
    iterando sobre un diccionario para identificar que operando se va cambiar.
    """
    for i, j in dic.items():
        equation = equation.replace(i, j)
    return equation
def get_stacks(f):
    """
    Guarda en pilas diferentes los operadores y los operandos en la ecuacion, realiza los operaciones correspondientes cuando encuentra ')'
    """
    operands = []
    operators = []
    operations = []
    for item in f:
        if item != 'and'and item != 'or' and item != 'not' and item != '==' and item != ')' and item != '<=' and item != '>=':
            operands.append(item)
        elif item == ')':
            operations.insert(0, operands.pop())
            operations.insert(0, operators.pop())
            if operations[0] == 'not':
                str1 = " ".join(str(x) for x in operations)
                operations = []
                operands.append(str(eval(str1)))
            else:
                operations.insert(0, operands.pop())
                str1 = " ".join(str(x) for x in operations)
                operations = []
                operands.append(str(eval(str1)))
        else:
            operators.append(item)
    return operands

def remove(f):
    """
    Removemos '(' ya que no lo necesitaremos para el algoritmo
    """
    f = f.split()
    for item in f:
        if '(' in f:
            f.remove("(")
    return f

dic = {"^":"and", "v":"or", "~":"not", "==":"==", "<" : "<=", ">":">="}
equation = input("Ingresa tu cadena bien formada\n")
f = bool_Oper(equation, dic)
f = remove(f)
print (get_stacks(f))