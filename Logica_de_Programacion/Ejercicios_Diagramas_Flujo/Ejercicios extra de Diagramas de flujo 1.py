# Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.

# Ejemplos:

# 4, 76, 43, 6, 8 → 76
# 1, 2, 3, 6, 7 → 7
# 2132, 4355, 1132, 2323, 1214 → 4355

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))
num5 = int(input("Ingrese el quinto numero: "))
mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3
if num4 > mayor:
    mayor = num4
if num5 > mayor:
    mayor = num5

print(f"El numero mayor es {mayor}")

