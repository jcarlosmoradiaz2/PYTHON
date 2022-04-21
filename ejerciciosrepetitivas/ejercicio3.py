#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
print("Hola")
contador=0
suma=0
vNum = []
numero=1
while(numero!=0):
    numero=(int)(input("Introduzca un número:.."))
    if numero!=0:
        vNum.append(numero)
    else:
        break

for i in vNum:
    suma=suma+i

print("La suma total es ", suma)
print("La media es ", (suma/len(vNum)))
    
