"""
Gimnasio: acceso por edad
Un gimnasio ofrece clases según la edad:
 menor de 13 → no puede ingresar
 de 13 a 17 → clase juvenil
 de 18 a 59 → clase general
 60 o más → clase senior
Pide la edad de una persona y muestra a qué grupo pertenece.
Practica: if, elif, else.
"""

print("GYM")

age = int(input("ingrese edad: "))

conditions = {
    "<13": "No puede ingresar",
    "13a17": "Clase juvenil",
    "18a59": "clase general",
    "60>"  : "Clase senior"
}

if age < 13:
    print(conditions["<13"])
elif age >=13 and age <=17:
    print(conditions["13a17"])
elif age >= 18 and age <=59:
    print(conditions["18a59"])
else:
    print(conditions["60>"])
    