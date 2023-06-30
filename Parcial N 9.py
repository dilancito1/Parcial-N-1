#Trabajo N 9

cantidad_de_personas = int(input("Ingrese la cantidad de peronas que desea poner:"))

while (cantidad_de_personas>=1):
     nombre = input("Ingrese su Nombre")
     apellido = input("ingrese su Apellido")
     edad2 = int(input("Ingrese su edad"))
     print(f"{nombre} {apellido}, {edad2} años")
     cantidad_de_personas = cantidad_de_personas+1

     print("nombre", nombre)
     print("Apellido", apellido)
     print("edad", edad2)

else:
     print("Fin del programa")
