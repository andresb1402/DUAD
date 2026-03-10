# Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.

# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

list_of_words = []
sentence = "House-Dog-Bike-Tool-Ball-Moto"

def sorting_words(sentence):
    list_of_words = sentence.split('-')
    list_of_words = sorted(list_of_words)
    list_of_words = "-".join(list_of_words)
    return list_of_words


print(f"Your sentence: {sentence}")
print(f"Sorted sentence: {sorting_words(sentence)}")
