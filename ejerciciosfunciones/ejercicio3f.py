#Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
def temperaturamedia(maxima,minima):
    media=(maxima+minima)/2
    return media

dias=(int)(input("Introduzca el número de días de los que va a saber la temperatra media:..."))

for i in range(dias):
    maxima=(int)(input("Temperatura máxima del día:..."))
    minima=(int)(input("Temperatura mínima del día:..."))
    print("La temperatura media es ",temperaturamedia(maxima,minima), " º")
    

