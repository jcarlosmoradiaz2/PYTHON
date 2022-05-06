#devolvemos el nombre con más probabilidad: Franco o Guerra
import random

def francovshistoria(ite): #ite son las interaciones que vamos a realizar
    contadorguerra=0
    contadorfranco=0
    
    
    for i in range(0,ite):
        numAleatorio= random.randint(1,2)
        if numAleatorio==1:
            contadorfranco=contadorfranco+1
        else:
            contadorguerra=contadorguerra+1
    print("La probabilidad de que caiga Franco es: ",(contadorfranco/ite)*100)
    print("La probabilidad de que caiga Guerra Civil es: ",(contadorguerra/ite)*100)
    if contadorfranco>contadorguerra:
        return "Franco"
    else:
        return "Guerra"

ite=(int)(input("Cuántas veces quiere que compruebe?..."))
print("Estudiate: ",francovshistoria(ite))