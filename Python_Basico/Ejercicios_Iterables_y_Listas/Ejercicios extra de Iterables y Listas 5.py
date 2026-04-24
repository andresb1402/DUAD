#Cree un programa que le pida al usuario ingresar 5 palabras. 
# Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

user_list = []
new_list = []

print("---Ingresar 5 palabras---\n")
for i in range(5):
    word = input(f"Ingrese la palabra #{i+1}: ")
    user_list.append(word)
    if len(word) > 4:
        new_list.append(word)

print(f"\nLista original: {user_list}")
print(f"La lista con palabras de mas de 4 letras: {new_list}")

