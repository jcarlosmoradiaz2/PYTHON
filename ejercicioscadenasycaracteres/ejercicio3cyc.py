#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.
from shutil import get_unpack_formats


cadena=input("Introduzca una cadena:...")
caracter=(input("Introduzca un carácter:..."))
caracter=ord(caracter)
contador=0

if (caracter>=65 and caracter<90):
    print("Es un carácter")
    for aux in cadena:
        if(ord(aux.upper()==caracter)):
            contador=contador+1

print("El caracter aparece ", contador,  " veces")


