#Trabajo N 7

horas_trabajadas_mensuales = 120
sueldo_horas = 1500
sueldo_anual = horas_trabajadas_mensuales * sueldo_horas * 12

monto_bonificaciones = 0

if sueldo_anual > 2000000:
    descuento = sueldo_anual * 0.05
elif sueldo_anual >= 1000000:
    descuento = sueldo_anual * 0.03
else:
    descuento = sueldo_anual * 0.01

salario_bruto_anual = sueldo_anual + monto_bonificaciones
monto_a_descontar = descuento

print("Salario anual bruto: ", salario_bruto_anual)
print("Monto anual de bonificaciones: ", monto_bonificaciones)
print("Monto anual a descontarse: ", monto_a_descontar)
print("Horas trabajadas en todo el año: ", horas_trabajadas_mensuales * 12)