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
    print("product": ,cont1["product"],"\n",
          "price": ,cont1["price"])