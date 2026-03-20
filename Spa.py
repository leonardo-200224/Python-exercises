"""
Spa: servicio disponible
En un spa hay estos servicios:
     masaje
     facial
     manicure
Pide al usuario qué servicio desea y muestra un mensaje confirmando
si existe o no.
Practica: condicionales con texto.

"""
spa={
    "massage":"If the service exists",
    "facial":"If the service exists",
    "manicure":"If the service exists"
    }
print("\nServices\n"
        "massage\n"
        "Facial\n"
        "manicure\n"
        )
Services= input("What service do you want?: ").strip()
print(spa.get(Services.lower(),"The entered service does not exist"))
