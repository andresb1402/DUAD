#Cree una función que retorne la suma de todos los números de una lista.

# La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
# [4, 6, 2, 29] → 41

list_of_numbers = [1, 2, 3, 4]

def sum_of_numbers(list_of_numbers):
    result = 0
    for number in list_of_numbers:
        result += number 
    return result

print(f"The result is {sum_of_numbers(list_of_numbers)}.")

list_of_numbers = [4, 6, 2, 29]

def sum_of_numbers_method2(list_of_numbers):
    result = sum(list_of_numbers)
    return result

print(f"The result using another method is {sum_of_numbers_method2(list_of_numbers)}.")