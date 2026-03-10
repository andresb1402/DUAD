# Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, 
# y le pida al usuario adivinar ese número. 
# El algoritmo no debe terminar hasta que el usuario adivine el numero.

secret_number = int(input("Por favor ingrese su numero secreto (1-10): "))
while True:
    user_number = int(input("Intente adivinar el numero secreto: "))
    if user_number > 10:
        print("El numero debe ser entre 1 y 10. Intentelo de nuevo")
    elif user_number < 10:
        if user_number == secret_number:
            print(f"El numero secreto es: {user_number}")
            break
        else:
            print(f"El numero no es correcto, intenta de nuevo.")

#_________________

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