#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.
cadena=input("Introduzca una cadena:...")
subcadena=input("Introduzca una subcadena:...")
if(subcadena==cadena[0:len(subcadena)]):
    print("Son iguales")
else:
    print("Son diferentes")
    