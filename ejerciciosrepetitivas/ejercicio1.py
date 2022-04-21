#Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),
factorial=1
print("Hola")
numero=(int)(input("Introduzca el número del que quiere saber su factorial:..."))
if (numero<0):
    print("No existe el factorial de un número negativo")
else:
    for i in range(2,(numero+1)):
        factorial= factorial*i
print("El factorial de ", numero, " es ", factorial)














