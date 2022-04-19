#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5
print("Hola, a continuación te voy a mostrar las tablas de multiplicar de los números 1,2,3,4 y 5")
numero=(int)=1
while (numero<5):
    for i in range(1,10):
        print(numero, "x ", i, "=", (numero)*i)
    numero=numero+1
