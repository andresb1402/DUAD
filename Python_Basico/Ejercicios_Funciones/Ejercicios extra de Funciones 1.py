#Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto

user_text = "The future belongs to those who believe in the beauty of their dreams"
user_letter = input("Please enter the letter you want to find: ")

def letter_finder(user_text, user_letter):
    letter_count = 0
    for letter in user_text:
        if user_letter.lower() == letter.lower():
            letter_count += 1
    return letter_count

print(f'The letter "{user_letter}" appears {letter_finder(user_text, user_letter)} times in "{user_text}"')