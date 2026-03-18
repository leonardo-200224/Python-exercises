"""
Peluquería: turno del día
Pide la hora de llegada de un cliente en formato entero de 0 a 23.
Mostrar:
 mañana si está entre 6 y 11
 tarde si está entre 12 y 17
 noche si está entre 18 y 22
 fuera de horario en cualquier otro caso
Practica: rangos con condicionales.

"""

print("\nHair_salon \n"
      "Day\n")
hour=int(input("Enter arrival time: "))
if hour >=6 and hour <=11:
    print("morning shift")
elif hour >=12 and hour <=17:
    print("afternoon shift")
elif hour >=18 and hour <=22:
    print("night shift")
else:
    print("Out of range")