import random
import time 


def generarlista(elementos):
    v=[]
    i=0
    while i<elementos:
        numero=random.randint(0,elementos)
        v.append(numero)
        time.sleep(0.5)
        i=i+1 
    return v

bandera=True
while bandera==True:
    try:
        elementos=int(input("Introduzca el número de elementos:..."))
        print(generarlista(elementos))
        bandera=False    
    except:
        print("Debe introducir un número entero, no una letra")
        bandera=True

