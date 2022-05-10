#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.
def ConvertirEspaciado(cadena):
    espacios=""
    for i in cadena:
        espacios=espacios+i+" "
    return espacios


cadena=(str)(input("Introduzca la cadena:..."))
print(ConvertirEspaciado(cadena))