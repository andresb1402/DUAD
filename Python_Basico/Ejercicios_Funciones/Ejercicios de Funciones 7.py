# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.

# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]

list_of_numbers = [1, 4, 6, 7, 13, 9, 67]
prime_numbers_list = []

def prime_numbers(list_of_numbers):
    for number in list_of_numbers:
        if number <= 1:
            continue
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers_list.append(number)
    return prime_numbers_list

print(f"Original list: {list_of_numbers}")
print(f"Prime numbers list: {prime_numbers(list_of_numbers)}")

