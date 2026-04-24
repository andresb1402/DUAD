#Songs reader.

def songs_reader(input_file):
    with open(input_file) as file:
        print('\nThis is the list of songs:\n')
        print(file.read())


def songs_name_sorter(input_file, output_file):
    with open(input_file) as file:
        songs = [line.strip() for line in file.readlines()]
        sorted_list = sorted(songs)
        with open(output_file, "w") as sorted_file:
            for song in sorted_list:
                sorted_file.write(song + "\n")
        return sorted_list
    

songs_reader('songs.txt')
songs_name_sorter('songs.txt', 'output_file.txt')
songs_reader('output_file.txt')
