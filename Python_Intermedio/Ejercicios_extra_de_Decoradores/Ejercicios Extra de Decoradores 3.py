# Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si

# A esta función se le debe combinar dos decoradores:

# @log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
# @validate_numbers: revisa que todos los argumentos sean numéricos

from datetime import date
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'This executes: {func.__name__.capitalize()}')
        print(f'Numbers received: {args}')
        print(f'Date: {date.today()}')
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        return result

    return wrapper


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        invalid_args = []
        for arg in args:
            if not isinstance(arg, (int, float)):
                invalid_args.append(arg)
        if invalid_args:
            raise ValueError(f"\nInvalid inputs: {invalid_args}")
        return func(*args, **kwargs)

    return wrapper


@log_call
@validate_numbers
def multiply(num1, num2):
    return num1 * num2

# multiply('n', 'j') # test error 1
# multiply('n', 5) # test error 2
multiply(15, 75)