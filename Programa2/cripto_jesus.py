def completa(frase,n):
    """ 
    Completa los espacios en la tabla en caso de necesitarlos con el caracter 'z'

    """
    	if len(frase) % n == 0:
    		return frase
    	else:
    		for i in range(len(frase) % n,n):
    			frase=frase+'z'
    		return frase
    	print ("Valor incorrecto")

def coddecod(frase,n):
    """
    Realiza el cifrado del mensaje de acuerdo a la llave proporcionada.

    El cifrado consiste en formar una tabla con tantas columnas como indique el número 
    de clave ingresado por el usuario, después de ello se escribe en la
    tabla de izquierda a derecha y de arriba hacia abajo el mensaje ingresado

     se toman los caracteres por columna de arriba hacia abajo y de izquierda
    a derecha obteniendo finalmente el texto codificado

    """
	copia=''
	for i in range (0,n):
		for j in range(0,len(frase),n):
			copia=copia+frase[j+i]
	return copia

""" 
Se capturan los datos de mensaje y clave.

En caso de que la clave sea mayor a la longitud del mensaje se formara una
clave "equivalente" tomando como valor el modulo de la siguiente operacion.

clave = clave  %  len(mensaje)

La clave corresponde a un número entero positivo.
En caso de ingresar un número negativo el programa desplegará un mensaje de error. 

"""

f=str(input("Frase a codificar: "))
clave=int(input("Numero clave: "))
if clave > len(f):
    clave = clave % len(f) 
if clave > 0:
    f=f.replace(" ","")
    f=completa(f,clave)
    f=coddecod(f,clave)
    print("La frase codificada= "+f)
    q=len(f)/(clave)
    f=coddecod(f,int(q))
    print("La frase decodificada= "+f)
else:
    print("Valor incorrecto")
