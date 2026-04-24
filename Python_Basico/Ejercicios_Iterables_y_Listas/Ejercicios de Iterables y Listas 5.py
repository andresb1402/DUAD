#Cree un programa que le pida al usuario 10 números, y al final 
# le muestre todos los números que ingresó, seguido del numero ingresado más alto.

numbers_list = []
greater = 0
print("--Ingrese 10 numeros--")
for i in range(10):
    number = int(input(f"#{i+1}: "))
    numbers_list.append(number)
    if number > greater:
        greater = number

print(f"Sus numeros fueron: {numbers_list} y el numero mayor fue {greater}.")