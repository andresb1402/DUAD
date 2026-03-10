#1. Cree un pseudocódigo que le pida un precio de producto al usuario, 
# calcule su descuento y muestre el precio final tomando en cuenta que:

#Si el precio es menor a 100, el descuento es del 2%.
#Si el precio es mayor o igual a 100, el descuento es del 10%.
#Ejemplos:

#120 → 108
#40 → 39.2

product_price = int(input("Por favor ingrese el precio del producto: "))
if product_price < 100:
    discount = 0.02
else:
    discount = 0.10
final_price = product_price - (product_price * discount)
print(f"El precio final de su producto es: {final_price}")

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

# Cree un algoritmo que le pida un numero al usuario, y 
# realice una suma de cada numero del 1 hasta ese número ingresado. 
# Luego muestre el resultado de la suma.

# 5 → 15 (1 + 2 + 3 + 4 + 5)
# 3 → 6 (1 + 2 + 3)
# 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

sum = 0
number = int(input("Por favor ingrese un numero: "))
for i in range(1, number+1):
    sum = sum + i
list_of_numbers = [str(i) for i in range(1, number+1)]
result = " + ".join(list_of_numbers)
print(f"{result} = {sum}")
