#Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.
cadena=input("Introduzca su nombre y apellidos:...").lower() #con el lower hemos convertuido todo el nombre a 

print(cadena[0]. upper(),end="")# ponemos la primera letra en mayúscula
contador=1

while(contador<len(cadena)):
    if (cadena[contador]==" "):
        print(" ",cadena[contador+1]. upper(), end="")
        contador=contador+1
    else:
        print(cadena[contador], end="")
    contador=contador+1


