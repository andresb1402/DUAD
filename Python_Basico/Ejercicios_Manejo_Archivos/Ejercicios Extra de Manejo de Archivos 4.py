#Add lines.

def new_line_request():
    user_line = input("Please enter the text you want to add: ")
    print(f'The new line will be: {user_line}')
    return user_line


def text_reader(output_file):
    with open(output_file) as file:
        print('\nThis is the content of the file:\n')
        print(file.read())


def add_line(user_line, output_file):
    with open(output_file, "a") as file:
        file.write(user_line + "\n")

    
user_line = new_line_request()
add_line(user_line, 'final_file.txt')
text_reader('final_file.txt')
