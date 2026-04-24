# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:

# Lea el archivo JSON de Pokémon
# Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)


import json

def json_file_reader(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        pokemon_list_py = json.load(file)
    return pokemon_list_py


def print_list(pokemon_list_py):
    for pokemon in pokemon_list_py:
        name = pokemon['name']['english']
        level = pokemon['level']
        type = ", ".join(pokemon['type'])
        hp = pokemon['base']['HP']
        attack = pokemon['base']['Attack']
        defense = pokemon['base']['Defense']
        sp_attack = pokemon['base']['Sp. Attack']
        sp_defense = pokemon['base']['Sp. Defense']
        speed = pokemon['base']['Speed']

        print(f"--- Pokémon: {name} ---")
        print(f"Level: {level}.")
        print(f"Type: {type}.")
        print(f"HP: {hp}.")
        print(f"Attack: {attack}.")
        print(f"Defense: {defense}.")
        print(f"Sp. Attack: {sp_attack}.")
        print(f"Sp. Defense: {sp_defense}.")
        print(f"Speed: {speed}.")
        print("-" * 30)


poke_list = json_file_reader('json_pokemon.json')
print_list(poke_list)
