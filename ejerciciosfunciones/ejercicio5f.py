#Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
def calcularmaxmin(vector):
    min=v[0]
    max=v[0]
    for i in vector:
        if min>i:
            min=i
        if max<i:
            max=i
    print("El minimo del vector es: ", min)
    print("El máximo del vector es: ",max)

v=[]
numeros=(int)(input("¿Cuántos números va a introducir?..."))
for i in range(0,numeros):
    numero=(int)(input("Introduzca un número:..."))
    v.append(numero)

print(calcularmaxmin(v))
