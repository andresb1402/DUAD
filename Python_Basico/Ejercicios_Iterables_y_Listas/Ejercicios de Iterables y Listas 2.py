#Cree un programa que itere e imprima un string 
# letra por letra de derecha a izquierda

my_string = "Life is 10% what happens to you and 90% how you react to it"

for character in range(len(my_string), 0, -1):
    index = character
    print(my_string[character - 1])