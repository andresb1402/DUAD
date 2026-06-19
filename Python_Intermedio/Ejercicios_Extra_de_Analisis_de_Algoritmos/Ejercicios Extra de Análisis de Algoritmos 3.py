def print_all_pairs(my_dict): # O(1)
    for key1 in my_dict: # O(n)
        for key2 in my_dict: # O(n)
            print(f"{key1}-{key2}") # O(1)

# Resultado Único: O(n2) — Tiempo Cuadrático.
# Genera todas las combinaciones posibles de parejas de llaves del mismo diccionario. Al tener dos bucles for anidados
# que iteran sobre la misma estructura de tamaño n, el ciclo interno ejecutará la operación de impresión O(1) un 
# total de n×n veces. No existen condiciones de salida anticipada, por lo que siempre realiza el recorrido completo.

# Resultado General: O(1) — Memoria Constante.
# A pesar de que la salida en la consola crece de forma cuadrática, el algoritmo no almacena esas parejas en ninguna 
# lista, tupla o estructura de datos interna. La memoria extra utilizada para los iteradores key1 y key2 es fija, por 
# lo que el uso de memoria no depende del tamaño del diccionario.

# Podría durar 2,777 horas 