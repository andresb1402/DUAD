#     Cree una clase Product con:

# Nombre, precio y cantidad
# Cree una clase Inventory que:

#     Guarde productos en una lista
#     Tenga métodos para:
#         Agregar un producto
#         Mostrar todos los productos
#         Calcular el valor total del inventario


class Product:
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.product_list = []


    def add_product(self, product):
        self.product_list.append(product)

    
    def show_products(self):
        if self.product_list:
            print('\n--- List of products in stock ---')
            for i, p in enumerate(self.product_list, start=1):
                print(f'\n--- Product #{i} ---')
                print(f'\nProduct: {p.product}')
                print(f'Price: {p.price}')
                print(f'Quantity: {p.quantity}')
        else:
            print('\nNo products to show, try adding some.')

    
    def remove_products(self): # added this extra step just for fun.
        if not self.product_list:
            print('\nNo products to remove, try adding some.')
            return
    
        print('\n--- Deleting a product ---')
        to_be_removed = input('\nEnter the Product you want to remove: ').capitalize()
        found_product = None

        for p in self.product_list:
            if to_be_removed == p.product:
                found_product = p
                break

        if found_product:
            while True:
                choice = input(f'\n"{to_be_removed}" found, are you sure? (y/n): ').upper()
                if choice == 'Y':
                    self.product_list.remove(found_product)
                    print(f'\n"{to_be_removed}" was successfully removed from the list.')
                    break
                elif choice == 'N':
                    print('\nOperation cancelled')
                    break
                else:
                    print('Error: Invalid option (y/n).')
                    
        
        else:
            print(f'\n"{to_be_removed}" not found.')

    
    def calculate_total(self):
        if self.product_list:
            print('\n--- Total cost of products in stock ---')
            total = 0

            for p in self.product_list:
                total += (p.price * p.quantity)

            print(f'\nThe total cost is ${total}')

        else:
            print('\nNo products to calculate, try adding some.')

store = Inventory()

while True:

    print('\n--- Welcome to the product manager ---')
    print('\n1. Add a product.')
    print('2. Remove a product.')
    print('3. Show all products.')
    print('4. Calculate the total of all products.')
    print('5. Exit.')

    choice = input('\nPlease select one the options (1-5): ')
    if choice == '1':
        while True:
            product = input("\nEnter the product: ").capitalize()
            if product.isspace() or len(product) == 0 or product.isdigit():
                print("Error: Product cannot be empty, a space or a number.")
                continue

            try:
                price = float(input(f"\nEnter the price of '{product}': "))
                if price <= 0:
                    print("Error: Value must be greater than zero.")
                    continue

                quantity = int(input(f"\nEnter the quantity of '{product}': "))
                if quantity <= 0:
                    print("Error: Value must be greater than zero.")
                    continue

            except ValueError:
                print("Error: Value must be a positive number.")
                continue
            
    
            new_product = Product(product, price, quantity)
            store.add_product(new_product)
            print(f'\n--- Product added successfully ---')
            print(f'Product:    {product}')
            print(f'Price:      ${price}')
            print(f'Quantity:   {quantity}')
            break

    
    elif choice == '2':
        store.remove_products()
        
    elif choice == '3':
        store.show_products()

    elif choice == '4':
        store.calculate_total()

    elif choice == '5':
        print('\n--- Thank you for using, bye ---')
        break

    else:
        print('\nError: Please enter a numeric option (1-5).')