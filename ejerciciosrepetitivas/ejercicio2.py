#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.
print("Hola")

#El "import random" es para importar las librerías de random y poder utilizarlas
import random 

#El "randint" es para un entero entre el 0 y 100
numAleatorio= random.randint(0,100)
intentos=10
numpedido=-1
aux=5

numpedido= (int)(input("Dime un número: "))

if numAleatorio==numpedido:
    print("genial, has acertado")
else: 
    while(numAleatorio!= numpedido and intentos>0)
    print("no has acertado")



