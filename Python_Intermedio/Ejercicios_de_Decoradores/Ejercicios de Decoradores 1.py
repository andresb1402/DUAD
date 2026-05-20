# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def func_decorator(func):
    def wrapper(*args):
        print(f"\n[DECORATOR] Received parameters: {args}")
        
        result = func(*args)
        
        print(f"[DECORATOR] Function return: {result}")
        return result

    return wrapper

@func_decorator
def print_info(name, age):
    print(f'\nName: {name}')
    print(f'Age: {age}')
    return "Operation successful"

print_info("Jose", 33)