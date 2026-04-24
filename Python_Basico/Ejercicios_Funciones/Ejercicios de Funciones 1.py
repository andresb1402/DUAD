#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def function1():
    print("This is the 1st function.")
    function2()


def function2():
    print("This is the 2nd one...")

function1()