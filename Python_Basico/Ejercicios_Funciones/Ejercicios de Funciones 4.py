#Cree una función que le de la vuelta a un string y lo retorne.

# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”

sentence = "This is from left to right"

def reverse_text(sentence):
    return sentence[::-1]

print(f"Original text: {sentence}")
print(f"Reversed text: {reverse_text(sentence)}")