nombre = "Vladimir Maidana Acarapi"
nombre = nombre.upper()
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abecedarioD = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
desplazamiento = 3;
nuevaCad = ""

descifra = ""

def cifrado(nom,des,abe):
	nuevaCad = ""
	for i in nom:
		if i in abe:
			posLetra = abe.index(i);
			nuevaPos = (posLetra + des) % len(abe)
			nuevaCad = nuevaCad+abe[nuevaPos]
		else:
			nuevaCad = nuevaCad+i;
	return nuevaCad

nuevaCad = cifrado(nombre,desplazamiento,abecedario)
#Para descifrar le mandamos el abecedario de forma invertida
descifra = cifrado(nuevaCad,desplazamiento,abecedarioD)
print (nuevaCad)
print (descifra)




