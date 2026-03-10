#Line joiner.

def line_reader(input_file):
    with open(input_file) as file:
        print('\nThis is the content of the file:\n')
        print(file.read())


def line_joiner(input_file, output_file):
    with open(input_file) as file:
        lines = [line.strip() for line in file.readlines()]
        joined_text = " ".join(lines)
        with open(output_file, "w") as joined_file:
            joined_file.write(joined_text)
        return joined_text
    

line_reader('songs.txt')
line_joiner('songs.txt', 'joined_file.txt')
line_reader('joined_file.txt')
