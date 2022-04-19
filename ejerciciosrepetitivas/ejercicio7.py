#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado
print("Hola")
numero=0
numero= (int)(input("Dime el número del que quiere saber su tabla de multiplicar: "))

for i in range(1,10):
    print((i, " x ", numero," = ",i*numero))