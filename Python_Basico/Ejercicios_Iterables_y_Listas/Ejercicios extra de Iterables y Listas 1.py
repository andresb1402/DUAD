#Cree un programa que cuente cuántas veces aparece un número 
# específico en una lista. Pida al usuario una lista de números y otro número a buscar

numbers_list = []
repeated_count = 0

while True:
    number = input("Ingrese el numero que desea agregar a lista (o 'ready' para finalizar): ")
    if number != "ready":
        numbers_list.append(number)
    else:
        break

user_number = input("\nIngrese el numero que desea buscar: ")

for i in numbers_list:
    if i == user_number:
        repeated_count += 1

print(f"\nLista original: {numbers_list}")
print(f"El numero {user_number} aparece {repeated_count} veces.")

