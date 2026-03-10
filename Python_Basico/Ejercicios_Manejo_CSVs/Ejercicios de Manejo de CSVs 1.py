# Cree un programa que me permita ingresar información 
# de n cantidad de videojuegos y los guarde en un archivo csv.

games_list = []

def add_game():
    while True:
        try:
            choice = int(input('1. Add a new game.\n2. Exit.\nPlease type your option: '))
            if choice == 1:
                games_dict = {'Name':'', 'Genre':'', 'Developer':'', 'Classification':''}
                new_game = input("Please enter the name of the game: ")
                games_dict['Name'] = new_game
                new_genre = input(f"Please enter the genre of {new_game}: ")
                games_dict['Genre'] = new_genre
                new_developer = input(f"Please enter the developer of {new_game}: ")
                games_dict['Developer'] = new_developer
                new_classification = input(f"Please enter the classification of {new_game}: ")
                games_dict['Classification'] = new_classification
                games_list.append(games_dict)
            elif choice == 2:
                print("Thank you for using. Good Bye!\n")
                break
            else:
                print("Please enter a valid option (1-2).\n")
        except: 
            print("Please enter only numbers (1-2).\n")
    return games_list


def save_to_csv(games_list, games_csv):
    with open(games_csv, "w") as file:
        file.write("Nombre,Genero,Desarrollador,Clasificacion\n")

        for game in games_list:
            values = list(game.values())
            csv_line = ",".join(values)
            file.write(csv_line + "\n")
    return games_csv


add_game()
print(games_list)
save_to_csv(games_list, 'games.csv')



