"""
Academia de baile: asistencia
Pide la cantidad de clases asistidas por un estudiante en un mes.
Reglas:
     menos de 5 → asistencia baja
     entre 5 y 8 → asistencia media
     9 o más → asistencia alta
Practica: clasificación por rangos
"""

print("DANCE ACADEMY")
classes = int(input("Enter number of classes attended: ")).strip()
if classes <=0:
    print("invalid value")
elif classes < 5:
    print("low attendance")
elif classes >=5 and classes <=8:
    print("average attendance")
elif classes >=9 and classes <=30:
    print("high attendance")
else:
    print("invalid value")