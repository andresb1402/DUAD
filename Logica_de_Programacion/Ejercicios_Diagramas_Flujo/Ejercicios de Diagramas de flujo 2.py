# Cree un diagrama de flujo que pida 3 números al usuario. 
# Si uno de esos números es 30, o si los 3 sumados dan 30, 
# mostrar “Correcto”. Sino, mostrar “incorrecto”.

num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
num3 = int(input("Por favor ingrese el tercer numero: "))
if num1 == 30 or num2 == 30 or num3 == 30:
    print("Correcto")
elif num1 + num2 + num3 == 30:
    print("Correcto")
else:
    print("Incorrecto")