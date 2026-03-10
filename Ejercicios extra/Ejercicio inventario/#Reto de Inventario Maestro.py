#Reto de Inventario Maestro

def file_reader(input_file):
    with open(input_file) as inventory:
        print('\nEste es el inventario:\n')
        print(inventory.read())



def str_to_dict(input_file):
    with open(input_file) as inventory:
        inventory_dict = {}
        for line in inventory:
            product, quantity = line.strip().split(":")
            inventory_dict[product] = int(quantity)
        return inventory_dict


def add_to_inventory(inventory_dict):
    new_product = input("Por favor ingrese el nombre del nuevo producto: ").capitalize()
    new_quantity = int(input("Por favor ingrese la cantidad del nuevo producto: "))
    if new_product in inventory_dict:
        inventory_dict[new_product] += new_quantity
    else:
        inventory_dict[new_product] = new_quantity
    return inventory_dict


def save_inventory(inventory_dict, input_file):
    with open(input_file, "w") as inventory_file:
        for product, quantity in inventory_dict.items():
            inventory_file.write(f"{product}:{quantity}\n")


my_inventory = file_reader('inventario.txt')
my_inventory = str_to_dict('inventario.txt')
my_inventory = add_to_inventory(my_inventory)
save_inventory(my_inventory, 'inventario.txt')