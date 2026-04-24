#    Cree una función convertir_a_entero(lista) que:

# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás

my_list = ['4', 'hola', '10', '5.2']

def string_to_int(my_list):
    print("---Resultados---\n")
    for element in my_list:
        try:
            converted = int(element)
            print(f"'{element}' convertido a '{converted}'")
        except ValueError:
            print(f"No se pudo convertir '{element}'")


string_to_int(my_list)