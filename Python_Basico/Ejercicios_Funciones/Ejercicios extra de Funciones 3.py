#Cree una función que reciba un string y retorne cuántas vocales contiene

user_text = input("Please enter your text: ")

def vowels_counter(user_text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    for character in user_text.lower():
        if character in vowels:
            vowels_count += 1
    return vowels_count

print(f'The text "{user_text}" contains {vowels_counter(user_text)} vowels.')

