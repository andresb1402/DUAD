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