#Trabajo N 10

estudiantes = int(input("Cuantos estudiantes quiere ingresar"))
suma_total = 0
contador = 0

while contador < estudiantes:
     notas = float(input("Ingrese las notas de los estudiantes"))
     suma_total += notas
     contador = contador +1 

promedio = suma_total / estudiantes
print("El primedio total de la clase es: ", (promedio))