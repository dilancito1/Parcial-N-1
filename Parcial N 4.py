#Trabajo N 4

def promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3 
    return prom

nota1 = float(input("ingrese la primera nota"))
nota2 = float(input("ingrese la segunda nota"))
nota3 = float(input("ingrese la tercera nota"))

promedio_final = promedio(nota1, nota2, nota3)

if promedio_final>=6:
      print("El alumno aprobo la materia con un promedio final de:",promedio_final)
else:
      print("El alumno debe recursar la materia con un promedio final de:", promedio_final)
