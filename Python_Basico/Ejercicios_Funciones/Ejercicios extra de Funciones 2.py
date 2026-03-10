#Cree una función que reciba una lista de palabras y un número n, 
# y retorne una nueva lista con solo las palabras que tengan más de n letras

user_list = ["house", "mountain", "sun", "bike", "cat", "motorbike", "ah", "camera", "function"]
user_number = int(input("Please enter the number of characters: "))


def word_length(user_list, user_number):
    new_list = []
    for word in user_list:
        if len(word) > user_number:
            new_list.append(word)
    return new_list

print(f"The new list is: {word_length(user_list, user_number)}")
