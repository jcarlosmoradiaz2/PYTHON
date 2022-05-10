#Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
def areaperimetro(radio):
    area=3.14*radio*radio
    perimetro=2*3.14*radio
    print("El perímetro de la circunferencia es: ", perimetro)
    print("El área de la circunferencia es: ", area )

radio=(int)(input("Introduzca el radio de la circunferencia:..."))
areaperimetro(radio)







