# Debe leer el archivo para importar los Pokémones existentes.
# Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def json_file_reader(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        pokemon_list = json.load(file)
    return pokemon_list


def new_pokemon_entry():
    new_pokemon = {
    "name": {
        "english": ""
    },
    "level": 0,
    "type": [],
    "base": {
        "HP": 0,
        "Attack": 0,
        "Defense": 0,
        "Sp. Attack": 0,
        "Sp. Defense": 0,
        "Speed": 0,
    }
}
    
    new_pokemon['name']['english'] = input("\nPlease enter the name of the Pokemon: ")
    new_pokemon['level'] = int(input(f"Please enter the level of {new_pokemon['name']['english']}: "))
    pokemon_type = input(f"Please enter the type of {new_pokemon['name']['english']}: ")
    new_pokemon['type'].append(pokemon_type)
    while True:
        choice = input(f"Do you want to add another type (y/n): ").lower()
        if choice == 'y':
            new_type = input(f"Please enter the other type of {new_pokemon['name']['english']}: ")
            new_pokemon['type'].append(new_type)
        elif choice == 'n':
            break
        else:
            print("Please enter a valid option (y/n).")
    new_pokemon['base']['HP'] =  int(input(f"Please enter the HP of {new_pokemon['name']['english']}: "))
    new_pokemon['base']['Attack'] = int(input(f"Please enter the Attack of {new_pokemon['name']['english']}: "))
    new_pokemon['base']['Defense'] = int(input(f"Please enter the Defense of {new_pokemon['name']['english']}: "))
    new_pokemon['base']['Sp. Attack'] = int(input(f"Please enter the Sp. Attack of {new_pokemon['name']['english']}: "))
    new_pokemon['base']['Sp. Defense'] = int(input(f"Please enter the Sp. Defense of {new_pokemon['name']['english']}: "))
    new_pokemon['base']['Speed'] = int(input(f"Please enter the Speed of {new_pokemon['name']['english']}: "))
    print(f'\n{new_pokemon['name']['english']} has been added succesfully.')

    return new_pokemon


def add_pokemon_to_list(pokemon_list, new_pokemon):
    pokemon_list.append(new_pokemon)
    return pokemon_list


def save_to_file(input_file, pokemon_list):
    with open(input_file, 'w') as file:
        json.dump(pokemon_list, file, indent=4)


current_list = json_file_reader('json_pokemon.json')
new_poke = new_pokemon_entry()
final_list = add_pokemon_to_list(current_list, new_poke)
save_to_file('json_pokemon.json', final_list)