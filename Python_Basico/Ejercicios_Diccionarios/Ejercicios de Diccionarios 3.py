#Cree un programa que use una lista para eliminar keys de un diccionario.

keys_to_be_deleted = ['Last name', 'Favourite color']
my_dict = {
    'First name': 'Jose', 
    'Last name': 'Barboza', 
    'Age': 32,
    'Favourite color': 'Gray',
    'Favourite song': 'Juicy',
}

for i in keys_to_be_deleted:
    my_dict.pop(i)

print(my_dict)