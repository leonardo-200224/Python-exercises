"""
Pide el tipo de mascota:
 perro
 gato
 conejo
Luego muestra una recomendación de alimento según el animal.
Practica: comparaciones con texto.

"""
pet = ["dog","cat", "rabbit"]
name_pet = input("Enter the name pet: ").strip()

if name_pet.lower() == pet[0]:
    print("high-quality proteins (chicken, turkey, fish, egg).")
elif name_pet.lower() == pet[1]:
    print("High in animal protein (chicken, fish), low in carbohydrates.")
elif name_pet.lower() == pet[2]:
    print("80-90% de heno de pasto de alta calidad (como fleo o avena)")
else:
    print("ERROR: invalid value")
    


