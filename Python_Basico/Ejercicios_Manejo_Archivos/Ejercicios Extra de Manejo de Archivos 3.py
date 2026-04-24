#Caps converter.

def text_reader(input_file):
    with open(input_file) as file:
        print('\nThis is the content of the file:\n')
        print(file.read())


def caps_converter(input_file, output_file):
    with open(input_file) as file:
        lines = [line.strip().upper() for line in file.readlines()]
        converted_text = "\n".join(lines)
        with open(output_file, "w") as joined_file:
            joined_file.write(converted_text)
        return converted_text
    

text_reader('songs.txt')
caps_converter('songs.txt', 'converted_file.txt')
text_reader('converted_file.txt')
