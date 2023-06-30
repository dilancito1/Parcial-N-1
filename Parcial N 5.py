#Trabajo N 5

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas:"))

if horas_trabajadas > 120:
    valor_hora = 1500
elif horas_trabajadas > 80:
    valor_hora = 1300
else:
     valor_hora = 1100

sueldo = horas_trabajadas * valor_hora

print("Su sueldo es de $", sueldo)