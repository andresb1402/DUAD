#Convertidor de unidades de temperatura

    # Pida al usuario ingresar una temperatura en Celsius
    # Conviértala a Fahrenheit y Kelvin
    # Muestre los tres valores

celsius = int(input("Ingrese la temperatura en grados Celsius: "))
print("\nConvirtiendo...\n")
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"{celsius} grados Celsius = {fahrenheit} grados Fahrenheit.")
print(f"{celsius} grados Celsius = {kelvin} grados Kelvin.")

