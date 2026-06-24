# Cree una clase de pruebas que contenga al menos 3 funciones 
# que operen con números (como suma, promedio, conversión, etc.) y escriba:

#   Un caso con números positivos
#   Un caso con números negativos
#   Un caso con ceros

class Tests:
    def sum(*args):
        if not args:
            return 0
        
        result = args[0]
        for num in args[1:]:
            result += num
        return result


    def average(*args):
        if not args:
            return 0
        
        result = args[0]
        for num in args[1:]:
            result += num
        if result == 0:
            return 0
        else:
            return result / len(args)
    

    def subtract(*args):
        if not args:
            return 0
    
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
