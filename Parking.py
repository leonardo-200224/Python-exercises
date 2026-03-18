"""
Parqueadero: cobro por horas
Pide cuántas horas estuvo un carro en un parqueadero.
Reglas:
 primera hora = 5000
 cada hora adicional = 3000
Muestra el total a pagar.
Practica: condicionales y operaciones

"""
parking = int(input("How many hours was he in the parking lot?: "))
if parking >0:
    hours_total= (parking*3000)+2000
    print(f"total to pay: {hours_total}")
else:
    print("ERROR:  ")    