import os 
os.system('clear')
"""
Heladería: sabor más pedido

Una heladería quiere registrar 5 pedidos.

Por cada cliente, el programa debe pedir el sabor elegido:

* vainilla
* chocolate
* fresa

Al final debe mostrar cuántas veces se pidió cada sabor.
Practica: ciclos, condicionales, contadores.
"""


pedidos = []
sabores = [ 'vainilla','chocolate','fresa' ]
estadistica_sabores = []

print('Por favor eliga un sabor para su helado')

for i,sabor in enumerate(sabores):
    print(f'{i} - {sabor}')

for i in range(5):
    pedido = int(input('¿De que sabor desea el helado? '))
    pedidos.append(pedido)

for i,sabor in enumerate(sabores):
    estadistica_sabores.append({
        'sabor': sabor,
        'cantidad': pedidos.count(i+1)
    })
    
for s in estadistica_sabores:
    print(s)
