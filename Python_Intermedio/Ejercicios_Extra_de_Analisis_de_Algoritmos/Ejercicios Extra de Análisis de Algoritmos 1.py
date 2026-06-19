def manual_add(n): # O(1)
    result = 0 # O(1)
    for i in range(1, n + 1): # O(n)
        result += i # O(1)
    print (result) # O(1)

# Resultado Único: O(n) — Tiempo Lineal.
# Utiliza un bucle for cuyo rango está determinado por el valor del argumento de entrada n. Al crecer n, la 
# operación interna de acumulación (result += i) se repetirá  exactamente n veces, haciendo que el tiempo de ejecución aumente de forma lineal.

# Resultado General: O(1) — Memoria Constante.

# Solo requiere dos variables numéricas en memoria (result e i). No importa el valor, el programa no crea listas ni 
# colecciones de datos, por lo que el uso de memoria extra permanece fijo.

def add_formula(n): # O(1) 
    print(n * (n + 1) // 2) # O(1)

# Resultado Único: O(1) — Tiempo Constante.
# Calcula la suma de los primeros n números en un solo paso, sin importar su valor. Al no existir bucles ni 
# recursividad, el número de operaciones lógicas internas permanece fijo e independiente del valor del parámetro de entrada.
# Por eso, si tuviera que usar number = 1 000 000 000, usaría la segunda función. 