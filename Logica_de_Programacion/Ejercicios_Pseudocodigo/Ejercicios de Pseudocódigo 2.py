# Cree un pseudocódigo que le pida un tiempo en segundos al usuario y 
# calcule si es menor o mayor a 10 minutos. Si es menor, muestre 
# cuantos segundos faltarían para llegar a 10 minutos. 
# Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.

# Ejemplos:

# 1040 → Mayor
# 140 → 460
# 600 → Igual
# 599 → 1

time = int(input("Ingrese el tiempo (segundos): "))
if time < 600:
    difference = 600 - time
    print(f"Su tiempo fue {time} segundos y faltaron {difference} segundos para completar 10 minutos.")
elif time == 600:
    print("Su tiempo fue igual a 10 minutos.")
else:
    print("Su tiempo fue mayor a 10 minutos.")

