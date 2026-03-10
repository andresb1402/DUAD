#Cree un programa que verifique si todos los elementos de una lista son positivos

numbers_list = []

while True:
    number = input("Ingrese el numero que desea agregar a lista (o 'ready' para finalizar): ")
    if number != "ready":
        numbers_list.append(int(number))
    elif number == "ready":
        break

negative_count = 0

for i in numbers_list:
    if i <= 0:
        negative_count += 1
        
if negative_count > 0:
    print("Hay al menos un número negativo o cero")
else:
    print("Todos los numeros fueron positivos.")

