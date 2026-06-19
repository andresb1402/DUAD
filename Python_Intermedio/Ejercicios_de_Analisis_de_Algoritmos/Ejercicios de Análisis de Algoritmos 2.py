# Analice los siguientes algoritmos usando la Big O Notation:

def print_numbers_times_2(numbers_list): # O(1)
	for number in numbers_list: # O(n)
		print(number * 2) # O(1)
		
# Resultado Único: O(n) — Tiempo Lineal.
# El algoritmo cuenta con un solo bucle for que debe recorrer la lista de principio a fin de manera 
# secuencial. Si la lista tiene n elementos, la operación interna print(number * 2) (O(1)) se ejecutará 
# exactamente n veces. No existen mejores o peores casos aquí; el tiempo de ejecución crece en una 
# relación directa de 1 a 1 con el tamaño de los datos.

# Resultado General: O(1) — Memoria Constante.
# La función no almacena los resultados en una nueva lista ni duplica la estructura en memoria. Los 
# números multiplicados se imprimen directamente en la consola y se descartan inmediatamente, por lo 
# que el uso de memoria extra es fijo y no cambia sin importar el tamaño de numbers_list.

def check_if_lists_have_an_equal(list_a, list_b): # O(1)
	for element_a in list_a: # O(n)
		for element_b in list_b: # O(m)
			if element_a == element_b: # O(1)
				return True # O(1)
				
	return False # O(1)

# Peor Caso: O(n×m) — Donde n es la longitud de list_a y m es la longitud de list_b.
# Ocurre cuando las listas no comparten ningún elemento en común, o el único elemento igual está al final 
# de ambas listas. El bucle externo debe iterar las n veces completas, y por cada una de  ellas, el bucle 
# interno debe recorrer los m elementos de la segunda lista, multiplicando las ejecuciones de la comparación.

# Mejor Caso (Best Case): O(1) — Tiempo Constante.
# Ocurre si el primer elemento de list_a es exactamente igual al primer elemento de list_b. El condicional 
# se cumple de inmediato en la primera iteración y el return True corta toda la ejecución del algoritmo en
# un solo paso.

# Caso Promedio (Average Case): O(n×m)

def print_10_or_less_elements(list_to_print): # O(1)
	list_len = len(list_to_print) # O(1)
	for index in range(min(list_len, 10)): # O(1)
		print(list_to_print[index]) # O(1)
		
# Resultado Único: O(1) — Tiempo Constante.
# Aunque haya un bucle for, el uso de la función min(list_len, 10) restringe el número máximo de
# iteraciones a una constante fija (10). Si la lista es grande, el algoritmo solo procesará los primeros 
# 10 elementos.

# Resultado General: O(1) — Memoria Constante.
# El algoritmo solo guarda una variable entera (list_len) y el índice del bucle. No genera nuevas 
# estructuras ni colecciones de datos, por lo que el uso de memoria adicional se mantiene fijo.

def generate_list_trios(list_a, list_b, list_c): # O(1)
    result_list = [] # O(1)
    for element_a in list_a: # O(n) Donde n es el tamaño de list_a
        for element_b in list_b: # O(m) Donde m es el tamaño de list_b
            for element_c in list_c: # O(o) Donde o es el tamaño de list_c
                result_list.append(f'{element_a} {element_b} {element_c}') # O(1)
                
    return result_list # O(1)

# Resultado Único: O(n×m×o) — Tiempo Trilineal / Cúbico.
# El algoritmo cuenta con tres bucles for completamente anidados uno dentro del otro. Para procesar todas
# las combinaciones posibles, el ciclo interno se ejecutará un número de veces igual a la multiplicación 
# del tamaño de las tres listas independientes (n×m×o). No hay condicionales de salida rápida 
# (return o break), por lo que siempre se recorre al 100% en todos los casos.

# Resultado General: O(n×m×o) — Espacio Lineal Múltiple.
# A diferencia de todos los ejercicios anteriores que eran O(1) en espacio, este algoritmo SÍ gasta 
# memoria proporcional a las entradas. La variable result_list se va llenando con cada combinación generada.
# Al final, la lista contendrá exactamente el resultado de multiplicar n×m×o elementos guardados en la 
# memoria de la computadora de forma simultánea.