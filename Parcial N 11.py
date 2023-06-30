#Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
#a. Si es número es par o impar.
#b. Cuanto es la suma total de todos los números mostrados.
#c. Cuanto es la suma total de todos los números pares mostrados.
#d. Cuanto es la suma total de todos los números impares mostrados.

numero = 1
suma_general = 0
suma_de_pares = 0
suma_de_impares = 0

while numero <= 10:
    print(numero)

    #Verificar si el numero es par o impar
    if numero % 2 == 0:
        print("Es un numero par")
        suma_de_pares += numero
    else:
        print("Es un numero impar")
        suma_de_impares += numero

    #Calcular las sumas total
    suma_general += numero

    numero += 1 

print("La suma general es:", suma_general)
print("La suma de los num pares son: ",suma_de_pares)
print("La suma de los num impares son:", suma_de_impares)