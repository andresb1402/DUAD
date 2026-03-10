# 4. Cree un programa que le pida tres números al usuario y muestre el mayor.

num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
num3 = int(input("Por favor ingrese el tercer numero: "))

greater = num1

if num2 > greater:
    greater = num2
if num3 > greater:
    greater = num3

print(f"El numero mayor es {greater}")

