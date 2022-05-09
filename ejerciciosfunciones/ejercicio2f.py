#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo
def Esmultiplo(numero1,numero2):
    resto=numero1%numero2
    if resto==0:
        return True
    else:
        return False
        

numero1=(int)(input("Introduce un número:..."))
numero2=(int)(input("Introduce otro número:..."))
if (Esmultiplo(numero1,numero2)==True):
    print("El ", numero1, " es múltiplo de ", numero2)
else:
    print("El ", numero1, " no es múltiplo de ", numero2)