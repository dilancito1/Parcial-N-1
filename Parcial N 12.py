#Trabajo N 12 programa que permita ingresar las edades de las personas, hasta que el usuario decida no 
#hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas

peronas = int(input("Ingrese las edades:"))
suma_total = 0
contador = 0

while contador < peronas:
    notas = float(input("El total de las peronas ingersadas es:"))
    suma_total += notas
    contador += contador+1


promedio = suma_total / peronas
print("El promedio total es:", (promedio))