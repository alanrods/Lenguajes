import numpy.polynomial.polynomial as npy
#grado imprimir en inverso
__author__ = 'Alan'
p1 = []
p2 = []
n = 0
res = 0
flow = True

class Polinomios():
    def __init__(self):
        self.pol = []
        self.grd = 0

    def insertPol(self,grado,pln):
        self.grd = grado
        self.pol = pln
        for i in range(0,self.grd,1):
            print "Inserta el coeficiente en el grado: "+str(grado)+" del polinomio"
            grado-=1
            self.pol.append(input())
        return pln

    def evalPto(self,pol,pto):
        pos = len(pol)
        for i in range (0,len(pol)):
            if not pos == 1:
                res = pol[i]*(pto**pos)
                pos-=1
            else:
                res = res + pol[i]
        return res

obj = Polinomios()
while flow:
    print "1)Valor en un punto\n2)Suma\n3)Resta\n4)Multiplicacion\n5)Igualdad\n6)Polinomio opuesto:\n\tDigite \"exit\" si desea salir."
    entrada = raw_input()
    if entrada == "exit":
        flow = False
    else:
        op = int(entrada)
        if op == 1:
            print "Valor en un punto:\n"
            n = input("Grado del polinomio: ")
            p1 = obj.insertPol(n,p1)
            pto = input("Digite el punto a evaluar: ")
            print "El resultado es: "+str(obj.evalPto(p1,pto))
        elif op == 2:
            print "Suma"
            gr1 = input("Grado del polinomio 1")
            p1 = obj.insertPol(gr1,p1)
            gr1 = input("Grado del polinomio 2")
            p2 = obj.insertPol(gr1,p2)
            print "La suma es:"+str(npy.polyadd(p1,p2))
        elif op == 3:
            print "Resta"
            gr1 = input("Grado del polinomio 1")
            p1 = obj.insertPol(gr1,p1)
            gr1 = input("Grado del polinomio 2")
            p2 = obj.insertPol(gr1,p2)
            print "La resta es:"+str(npy.polysub(p1,p2))
        elif op == 4:
            print "Multiplicacion"
            gr1 = input("Grado del polinomio 1")
            p1 = obj.insertPol(gr1,p1)
            gr1 = input("Grado del polinomio 2")
            p2 = obj.insertPol(gr1,p2)
            print "La multiplicacion es:"+str(npy.polymul(p1,p2))
        elif op == 5:
            print "Igualdad"
            gr1 = input("Grado del polinomio 1")
            p1 = obj.insertPol(gr1,p1)
            gr1 = input("Grado del polinomio 2")
            p2 = obj.insertPol(gr1,p2)
        elif op == 6:
            print "Polinomio Opuesto"
            gr1 = input("Ingresa el grado del polinomio")
            p1 = obj.insertPol(gr1,p1)
            for i in range (0,len(p1)):
                p1[i]=-p1[i]
            print p1
        else:
            print "No es una opcion valida"