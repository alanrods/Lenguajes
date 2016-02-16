def completa(frase,n):
    	if len(frase) % n == 0:
    		return frase
    	else:
    		for i in range(len(frase) % n,n):
    			frase=frase+'z'
    		return frase
    	print ("Valor incorrecto")

def coddecod(frase,n):
	copia=''
	for i in range (0,n):
		for j in range(0,len(frase),n):
			copia=copia+frase[j+i]
	return copia



f=str(input("Frase a codificar: "))
clave=int(input("Numero clave: "))
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
