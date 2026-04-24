# Cree un diagrama de flujo que le pida un numero al usuario 
# y muestre “Fizz” si es divisible entre 3, “Buzz” si es divisible entre 5, 
# y “FizzBuzz” si es divisible entre ambos.

# Ejemplos:

# 33 → Fizz
# 25 → Buzz
# 30 → FizzBuzz

num = int(input("Ingrese un numero: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")

