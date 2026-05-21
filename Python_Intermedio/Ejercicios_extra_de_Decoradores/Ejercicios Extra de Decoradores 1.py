#     Cree una función que imprima “Hola, [nombre]” dos veces:

# Cree un decorador @repeat_twice que haga que la función decorada 
# se ejecute dos veces seguidas, con los mismos argumentos

def repeat_twice(func):
    def wrapper(*args, **kwargs):
        print(f'Received input: {args}')

        output = func(*args, **kwargs)
        output = func(*args, **kwargs)
        return output
    return wrapper


@repeat_twice
def print_name(name):
    print(f'Hello, {name}')
    return

print_name('Jose')