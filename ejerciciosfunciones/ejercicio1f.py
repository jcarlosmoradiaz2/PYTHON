#Crea un procedimiento EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter 
def EscribirCentrado(cadena):
    longitud=len(cadena)
    posicion=(int)(75-(longitud/2))
    espacios=0
    cadenacentrada=" "
    for i in range(0,posicion):
        cadenacentrada=cadenacentrada+" "



    print(cadenacentrada+cadena)

cadena=input("Introduce una cadena:...")
EscribirCentrado(cadena)