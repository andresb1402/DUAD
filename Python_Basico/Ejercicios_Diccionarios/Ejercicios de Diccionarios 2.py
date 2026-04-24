#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
# usando una para sus keys, y la otra para sus values.

list1 = ['First name', 'Fast name', 'Favourite color']
list2 = ['Jose', 'Barboza', 'Gray']
my_dict = {}

for i in range(len(list1)):
    key = list1[i]
    value = list2[i]
    my_dict[key] = value

print(my_dict)

