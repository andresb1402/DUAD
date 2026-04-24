#Cree un programa que reciba una lista de números y calcule el 
# promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

numbers_list = []
greatest_numbers = []


while True:
    number = input("Ingrese el numero que desea agregar a lista (o 'ready' para finalizar): ")
    if number != "ready":
        numbers_list.append(int(number))
        list_length = len(numbers_list)
    else:
        break

average = 0
total_sum = 0

for i in numbers_list:
    total_sum += i 
    
average = total_sum / (list_length)

for j in numbers_list:
    if j > average:
        greatest_numbers.append(int(j))

print(f"\nLista original: {numbers_list}")
print(f"El promedio de la lista es: {average}")
print(f"La lista con numeros mayores al promedio: {greatest_numbers}")

