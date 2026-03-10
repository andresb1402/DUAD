#    Cree una función sumar_valores(lista) que:

# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total

my_list = ['4', 'bike', '14.2', '17.5', '10', 'gun']

def sum_values(my_list):
    total = 0
    for element in my_list:
        try:
            converted = float(element)
            total += converted
            #float_list.append(converted)
            print(f"'{converted}' sumado correctamente.")
        except ValueError:
            print(f"Elemento invalido '{element}'")
    print(f"\nLa suma total es: {total}")
    return total


sum_values(my_list)
