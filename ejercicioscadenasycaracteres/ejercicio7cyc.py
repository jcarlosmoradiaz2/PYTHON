#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter
cadena=input("Introduzca una cadena:...")
caracter1=input("Introduzca un carácter:...").upper()
caracter2=input("Introduzca otro carácter:...").upper()
caracter1=ord(caracter1)
caracter2=ord(caracter2)


if ((caracter1>=65 and caracter1<=90)and(caracter2>=65 and caracter2<=90)):
    caracter1=(chr(caracter1).lower())
    caracter2=chr(caracter2).lower()
    for i in cadena:
        if i==caracter1:
            print(caracter2,end="")
        else:
            print(i,end="")
else: 
    print("Algunas de las dos cadenas introducidas no es un carácter")
