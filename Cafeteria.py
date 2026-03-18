"""
En una cafetería venden:
 café = 4000
 té = 3500
 jugo = 5000
Pide al usuario qué bebida quiere y cuántas unidades desea comprar.
Luego muestra el total a pagar.
Practica: condicionales, variables, multiplicación.

"""
#prices
cafeteria= [4000, 3500,5000]

#drink
cafeteria_name=["Coffee","Tea","Juice"]

#menu
print("\nCAFETERIA\n ")
print(" 0-Coffe\n "
      "1-Tea\n "
      "2-Juice ")

drink = int(input("Enter the beverage you wish to purchase (0-2): "))
if drink in [0, 1, 2]:
    units = int(input("How many units do you want to buy?: "))
    total = cafeteria[drink]*units
    #sale summary
    print(f"drink: {cafeteria_name[drink]}\n"
      f"Total: {total}")
else:
    print("Error: Invalid drink. Please try again. (0-2)")

