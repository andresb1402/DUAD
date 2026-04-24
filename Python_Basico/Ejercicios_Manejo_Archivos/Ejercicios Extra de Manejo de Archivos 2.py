#Word counter.

def text_reader(input_file):
    with open(input_file) as file:
        print('\nEste es el contenido del archivo:\n')
        print(file.read())


def word_counter(input_file):
    with open(input_file) as file:
        words = file.read().split()
        total_words = len(words)
        print(f"\nEste archivo contiene {total_words} palabras.")
        return total_words
    

text_reader('lyrics.txt')
word_counter('lyrics.txt')

