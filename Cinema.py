"""
El precio de la entrada cambia así:
 niños menores de 12 → 8000
 adultos de 12 a 59 → 12000
 mayores de 60 → 9000
Pide la edad del cliente y muestra cuánto debe pagar.
Practica: condicionales.

"""

value= [8000,1200,9000]

age = int(input("Ingrese edad: "))

if age < 12:
    print(f"Total a pagar: {value[0]}")
if age >= 12 and age <=59:
    print(f"Total a pagar: {value[1]}")
else:
    print(f"Total a pagar: {value[2]}")

