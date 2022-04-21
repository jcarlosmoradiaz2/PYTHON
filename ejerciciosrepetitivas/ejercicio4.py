print("Hola")
numero=0
menores=0
mayores=0
iguales=0
numeros=(int)(input("Introduzca la cantidad de números que quiere introducir:..."))
while(numeros!=0):
    numero=(int)(input("Introduzca un número:..."))
    numeros=(numeros-1)
    if(numero<0):
        menores=(menores+1)
    elif(numero>0):
        mayores=(mayores+1)
    else:
        iguales=(iguales+ 1)

print("Hay ", menores, " números menores que 0")
print("Hay ", mayores, " números mayores que 0")
print("Hay ", iguales, " números iguales a 0")
