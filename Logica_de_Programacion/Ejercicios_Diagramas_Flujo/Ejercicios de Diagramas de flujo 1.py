# Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, 
# y le pida al usuario adivinar ese número. 
# El algoritmo no debe terminar hasta que el usuario adivine el numero.

numero_secreto = int(input("Por favor ingrese su numero secreto: "))
while True:
    numero = int(input("Intente adivinar el numero secreto: "))
    if numero == numero_secreto:
        print(f"El numero secreto es: {numero}")
        break
    else:
        print(f"El numero no es correcto, intenta de nuevo.")
