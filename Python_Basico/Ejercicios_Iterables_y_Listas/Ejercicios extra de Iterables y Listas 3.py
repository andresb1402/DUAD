#Cree un programa que muestre el valor más pequeño de una lista sin usar min().

numbers_list = []

while True:
    number = input("Ingrese el numero que desea agregar a lista (o 'ready' para finalizar): ")
    if number != "ready":
        numbers_list.append(int(number))
    elif number == "ready":
        break

smaller_number = numbers_list[0]

for i in numbers_list:
    if i < smaller_number:
        smaller_number = i

print(f"\nLista original: {numbers_list}")
print(f"El numero menor es: {smaller_number}")

