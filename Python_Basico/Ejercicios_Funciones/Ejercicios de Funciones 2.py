#Intente accesar a una variable definida dentro de una función desde afuera.

def function1():
    name = "Jose"
    return name
    
print(f"My name is {function1()}")


#Intente accesar a una variable global desde una función y cambiar su valor.

age = 32

def function2():
    global age
    age = "32 years old"
    return age
    
print(f"I am {function2()}.")