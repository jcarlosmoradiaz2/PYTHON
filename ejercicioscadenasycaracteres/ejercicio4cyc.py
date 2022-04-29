#Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
cadena=input("Dime una cadena:...")
contador=0

for i in cadena:
    if i ==" ":
        contador=contador+1

print("Hay ", contador+1 , " palabras")
