# Analice el algoritmo de bubble_sort usando la Big O Notation.

my_list = [14, 30, 15, 25, 2, 6] # O(1)

def sorting_bubble(my_list):
    for i in range (len(my_list)): # O(n)
        already_sorted = True # O(1) 
        print(f"\n--- PASADA GENERAL #{i + 1} ---") # O(1)
        for index in range (0, len(my_list) - 1): # O(n) 
            if my_list[index] > my_list[index + 1]: # O(1)
                my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index] # O(1)
                already_sorted = False # O(1)
            print(f"  Comparando índice {index} y {index+1} -> Lista actual: {my_list}") # O(1)
        if already_sorted: # O(1)
            print('\nLa lista ya está ordenada.') # O(1)
            break # O(1)
    print(f'Lista ordenada: {my_list}') # O(1)

print(f'Lista original: {my_list}') # O(1)
sorting_bubble(my_list) # O(1)

# Peor Caso: O(n^2) — Tiempo Cuadrático.
# Ocurre cuando la lista está completamente invertida. El bucle externo (O(n)) se 
# multiplica con el bucle interno anidado (O(n)), generando un total de operaciones proporcionales a n×n.

# Mejor Caso (Best Case): O(n) — Tiempo Lineal.
# Justificación: Ocurre cuando la lista ya viene ordenada. Gracias a la bandera already_sorted, 
# el bucle interno realiza una sola pasada de verificación y rompe el ciclo principal con el break.

# Caso Promedio (Average Case): O(n^2) — Tiempo Cuadrático.

# Resultado General: O(1) — Memoria Constante.
# Justificación: Es un algoritmo de ordenamiento in-place (en el sitio). No crea copias de la lista ni 
# estructuras auxiliares en memoria; la cantidad de memoria extra utilizada por las variables 
# already_sorted e index es fija y no cambia sin importar si la lista tiene 6 elementos o 6 millones.