#Trabajo N 6

horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de las horas trabajadas:"))

sueldo_bruto = horas_trabajadas * valor_hora

if horas_trabajadas > 120:
    bonificacion = sueldo_bruto * 0.18
elif horas_trabajadas >= 80:
    bonificacion = sueldo_bruto * 0.15
else:
    bonificacion = sueldo_bruto * 0.13

sueldo_neto = sueldo_bruto + bonificacion

print("Sueldo Bruto", sueldo_bruto)
print("Monto a Bonificar:", bonificacion)
print("Sueldo Neto", sueldo_neto)