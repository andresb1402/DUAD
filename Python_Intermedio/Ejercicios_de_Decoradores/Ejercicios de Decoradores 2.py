# Cree un decorador que se encargue de revisar si todos los parámetros 
# de la función que decore son números, y arroje una excepción de no ser así.

def func_decorator(func):
    def wrapper(*args):
        print(f"\n[DECORATOR] Checking parameters: {args}\n")
        
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"{arg}: Is not a valid number")
            else:
                print(f"{arg}: Is a number")

        return func(*args)
        
    return wrapper


@func_decorator
def sum_numbers(*args):
    return f"\nTotal: {sum(args)}"

print(sum_numbers(22, 33, 15))
print(sum_numbers(22, 33, 15, "Jose"))