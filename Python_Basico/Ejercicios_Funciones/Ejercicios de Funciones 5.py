# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.

# “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

sentence = "My name is Jose Barboza"

def upper_and_lower_cases_count(sentence):
    upper_cases = 0
    lower_cases = 0
    for letter in sentence:
        if letter.isupper():
            upper_cases += 1
        elif letter.islower():
            lower_cases += 1
    return upper_cases, lower_cases
uppers, lowers = upper_and_lower_cases_count(sentence)


print(f"Your text: {sentence}")
print(f"Upper cases: {uppers}")
print(f"Lower cases: {lowers}")