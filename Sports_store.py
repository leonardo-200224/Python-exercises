"""
Tienda deportiva: contar productos caros
Pide el precio de 6 productos deportivos.
Al final indica cuántos cuestan más de 100000.
Practica: ciclo, contador, condicional.

"""

products = []
num=100000
counter=0

for cont in range(1,7):
    product =input(f"enter product {cont}: ").strip()
    price = float(input(f"enter price of {product}: "))
    if price > num:
        counter +=1
    
    dictionary = {
        "product": product,
        "price"  : price
    }
    
    products.append(dictionary)
    

for cont1 in products:
    print(f"product: {cont1["product"]} \n"
        f"price: ${cont1["price"]:,.0f}\n"
        )
print(f"greater than 100.000: {counter}")

# {valor:,.0f} → Formatea un número de la siguiente manera:
# valor → es la variable que contiene el número
# :     → indica que se va a aplicar un formato
# ,     → agrega separador de miles (ej: 200000 → 200,000)
# .0    → indica que no se mostrarán decimales
# f     → indica que el número es tipo float
# el valor se REDONDEA automáticamente (ej: 200000.75 → 200,001)