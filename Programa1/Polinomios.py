import numpy

def menu(): 
    print("\n\n\n\tOperaciones con polinomios de grado 'n' \n \n\tA)Valor en un punto \n\tB)Suma \n\tC)Resta \n\tD)Igualdad de 2 polinomios \n\tE) Polinomio opuesto \n\tF) Multiplicacion")
    option(input())

def option(a):
    if a== 'A' or 'a':
        print('\tValor en un punto\n Solo ingresa coeficientes , los coeficientes del polinomio se deben ingresar de forma decreciente.\n\tax^n + bx^2 + cx + d\n')
        p1 = numpy.poly1d(int_list(input()))
        print("\n" + str(p1))
        print("\n\tPunto a evaluar... ")
        val = int(input())
        print("\nValor en el punto = " + str(p1(val)))
        input("\nPresione enter para continuar\n")
        menu()
    if a == 'B' or 'b':
        print('\tSuma de polinomios \n Solo ingresa coeficientes , los coeficientes del polinomio se deben ingresar de forma decreciente.\n\tax^n + bx^2 + cx + d\n')
        p1 = numpy.poly1d(int_list(input()))
        print("\n" + str(p1) +'\n')
        p2 = numpy.poly1d(int_list(input()))
        print("\n" + str(p2)+ '\n')
        p3 = numpy.poly1d(p1+p2)
        print("= \n" + str(p3)+ '\n')
        input("\nPresione enter para continuar\n")
        menu()
    if a == 'C' or 'c':
        print('\tResta de polinomios \n Solo ingresa coeficientes , los coeficientes del polinomio se deben ingresar de forma decreciente.\n\tax^n + bx^2 + cx + d\n')
        p1 = numpy.poly1d(int_list(input()))
        print("\n" + str(p1) +'\n')
        p2 = numpy.poly1d(int_list(input()))
        print("\n" + str(p2)+ '\n')
        p3 = numpy.poly1d(p1-p2)
        print("= \n" + str(p3)+ '\n')
        input("\nPresione enter para continuar\n")
        menu()
    if a == 'D' or 'd' :
       print('\tIgualdad de polinomios \n Solo ingresa coeficientes , los coeficientes del polinomio se deben ingresar de forma decreciente.\n\tax^n + bx^2 + cx + d\n')
       p1 = numpy.poly1d(int_list(input()))
       print("\n" + str(p1) +'\n')
       p2 = numpy.poly1d(int_list(input()))
       print("\n" + str(p2)+ '\n')
       if p1 == p2 :
           print("Los polinomios son iguales")
       else:
           print("Los polinomios no son iguales")
       input("\nPresione enter para continuar\n")
       menu()
    if a == 'E' or 'e':
        print('\tPolinomio opuesto \n Solo ingresa coeficientes , los coeficientes del polinomio se deben ingresar de forma decreciente.\n\tax^n + bx^2 + cx + d\n')
        p1 = numpy.poly1d(int_list(input()))
        print("\n" + str(p1) +'\n')
        print("\nPolinomio opuesto: ")
        p1 = p1*-1
        print("\n" + str(p1) +'\n')
        input("\nPresione enter para continuar\n")
        menu() 
    if a == 'F' or 'f' :
        print('\tMultiplicacion de polinomios \n Solo ingresa coeficientes , los coeficientes del polinomio se deben ingresar de forma decreciente.\n\tax^n + bx^2 + cx + d\n')
        p1 = numpy.poly1d(int_list(input()))
        print("\n" + str(p1) +'\n')
        p2 = numpy.poly1d(int_list(input()))
        print("\n" + str(p2)+ '\n')
        p3 = numpy.poly1d(p1*p2)
        print("= \n" + str(p3)+ '\n')
        input("\nPresione enter para continuar\n")
        menu()
    else:
        print(" Opcion incorrecta")
        menu()

def int_list(user_input): # Casteamos todos los elementos de la lista a tipo 'int' para poder ser usado por las funciones de numpy
    user_input = list(map(int, user_input.split())) 
    return user_input
    
menu()