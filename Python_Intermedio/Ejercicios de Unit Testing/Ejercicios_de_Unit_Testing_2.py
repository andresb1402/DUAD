# exercise 3

def sum_of_numbers_method(list_of_numbers):
    result = sum(list_of_numbers)
    return result

# exercise 4

def reverse_text(sentence):
    return sentence[::-1]

# exercise 5

def upper_and_lower_cases_count(sentence):
    upper_cases = 0
    lower_cases = 0
    for letter in sentence:
        if letter.isupper():
            upper_cases += 1
        elif letter.islower():
            lower_cases += 1
    return upper_cases, lower_cases

# exercise 6

def sorting_words(sentence):
    list_of_words = sentence.split('-')
    list_of_words = sorted(list_of_words)
    list_of_words = "-".join(list_of_words)
    return list_of_words

# exercise 7

def prime_numbers(list_of_numbers):
    prime_numbers_list = []
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

