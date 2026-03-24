"""
Registrar varios pedidos en una cafetería hasta que el usuario escriba
“salir”.
Productos:
     café = 4000
     capuchino = 7000
     pastel = 6000
Reglas:
     si la compra supera 20000, aplicar 10% de descuento
     si no, cobrar normal
Mostrar total por cliente y al final total acumulado del día.
Practica: menú simple, ciclos, descuentos.

"""
#creating a list to save the data for each sale
sale= [ ]
# counter to identify customers
customer=1
# Total sales counter per customer
sale_client=0
# Total sales counter per day
coffee_shop_total=0

# product dictionary
products= {
    "coffee"   : 4000,
    "cappuccino": 7000,
    "cake"   : 6000
}

# while loops for the menu
count = True
count_total= True
# while to sort orders by customer
while count_total:
    # menu orders
    print("\ncoffee shop")
    menu= input("-New order\n"
                "-Exit\n"
                ": ")
    # It is validated that the entered data is "exit"
    if menu.lower() == "exit":
        # If the list is empty, the system ends without displaying data.
        if not sale:
            break
        print("customer total")
        # we go through the data on the list
        for value in sale:
            # iterate through each value of the dictionaries entered in the list exits
            for key, con in value.items():
                # Total sales per customer displayed in console
                print(f"{key}: ${con}\n")
        # The total sales per day are shown
        print(f"Day total: ${coffee_shop_total}")
        break
    # Validate that the data entered by the user is a new order; otherwise, notify the user.
    elif menu.lower().replace(" ", "") != "neworder":
        print("Invalid value entered")
        continue
    # while that validates the customer sale
    while count:
        # product menu
        sale_coffee = input("\nProducts\n"
                            "-Coffee\n"
                            "-cappuccino\n"
                            "-cake\n"
                            "Enter Product Name or exit to finish: ")#The user is notified that to complete the sale they must enter "exit"
        # User sales exit validation
        if sale_coffee.lower() == "exit":
            # Validation that the user's total is greater than 20000 to validate the discount
            if sale_client > 20000:
                sale_client= sale_client - (sale_client*10/100)
            # After the discount, a dictionary is created with the user's sales data
            new_product={
                f"Customer {customer}": sale_client
            }
            # The user's sales data is stored in the sale list# The user's sales data is stored in the sale list
            sale.append(new_product)
            # Customer counter becomes 2 to identify customer 2
            customer +=1
            # The total amount due from the customer is added to the variable that stores the total sales for the day.
            coffee_shop_total += sale_client
            # Counter to calculate total sales for the customer resets to 0, to be used with the next customer
            sale_client =0
            # We end the while loop
            break
        
        # Enter new product
        # We validate using get() that the product entered by the user is in the product list.
        # If get() returns a string value and not a numeric value, the user is notified that the entered product does not exist.
        if type(products.get(sale_coffee.lower(), "\nThe product does not exist. \n")) == str:
            print(f"\n{sale_coffee}: {products.get(sale_coffee.lower(), "\nThe product does not exist. \n")}\n")
            # We continue with the next do while loop without executing the following code.
            continue
        # Validation that get() returns a numeric value, validating the entered product
        elif type(products.get(sale_coffee.lower())) == int:
                # The price of the entered product is added to the variable sale_client
                sale_client +=products.get(sale_coffee.lower())
                # The user is shown their current total and we continue with the next cycle, requesting a new product.
                print(f"\nTotal: ${sale_client}\n")


