#Cree un programa que elimine todos los números impares de una lista.

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(f"Original list: {numbers_list}")
index_count = len(numbers_list)
odd_numbers = []

for i in range((index_count - 1), -1, -1):
    if numbers_list[i] % 2 != 0:
        odd_numbers.append(numbers_list.pop(i))

print(f"Pair numbers: {numbers_list}")

# for left in range(len(odd_numbers) // 2): #Opcional para mostrar los impares. 
#     index_count_odd = len(odd_numbers)
#     right = (index_count_odd - 1) - left
#     odd_numbers[left], odd_numbers[right] = odd_numbers[right], odd_numbers[left]

# print(f"Odd numbers removed: {odd_numbers}")