def linear_search(my_list, target): # O(1)
    for item in my_list: # O(n)
        if item == target: # O(1)
            return True # O(1)
    return False # O(1)

# Peor Caso: O(n) — Tiempo Lineal.
# Cuando el elemento buscado (target) no existe en la lista, o se encuentra en la última posición. En esta situación, 
# el bucle for se ve obligado a recorrer los n elementos completos de la lista antes de poder retornar False.

# Mejor Caso: O(1) — Tiempo Constante.
# Si el target coincide exactamente con el primer elemento de my_list. El condicional if se cumple de inmediato en la 
# primera iteración y el return True corta instantáneamente la ejecución de la función en un solo paso.

# Caso Promedio: O(n) — Tiempo Lineal.
# Si el elemento existe y los datos están desordenados, el algoritmo encontrará el objetivo a mitad de la lista (n/2​ pasos). 
# Al eliminar la constante 1/2​, la complejidad de crecimiento sigue siendo lineal.

# Resultado General: O(1) — Memoria Constante.

# Realiza una búsqueda in-place utilizando únicamente la variable del iterador (item). No duplica la lista de entrada ni 
# reserva estructuras de datos adicionales en memoria, por lo que el espacio utilizado se mantiene fijo e independiente 
# de cuántos elementos tenga la lista.

def binary_search(my_list, target): # O(1)
    low = 0 # O(1) 
    high = len(my_list) - 1 # O(1)
    while low <= high: # O(log n)
        mid = (low + high) // 2 # O(1)
        if my_list[mid] == target: # O(1)
            return True # O(1)
        elif my_list[mid] < target: # O(1)
            low = mid + 1 # O(1)
        else: 
            high = mid - 1 # O(1)
    return False # O(1)

# Peor Caso: O(logn) — Tiempo Logarítmico.
# Cuando el elemento buscado (target) no está en la lista o se encuentra en los extremos finales de las subdivisiones. 
# Como la lista se divide estrictamente a la mitad en cada iteración del ciclo while, el número máximo de pasos necesarios 
# para reducir el espacio de búsqueda a un solo elemento crece de forma logarítmica respecto al tamaño de la lista (n).

# Mejor Caso: O(1) — Tiempo Constante.
# Si el target se encuentra exactamente en la mitad de la lista original en la primera iteración. El primer cálculo de 
# mid apunta directo al objetivo, el if se cumple y la función termina de inmediato.

# Caso Promedio: O(logn) — Tiempo Logarítmico.

# Resultado General: O(1) — Memoria Constante.
# Esta versión es de carácter iterativo (usa un ciclo while en lugar de llamadas recursivas). Solo utiliza tres variables 
# de tipo entero (low, high, mid) para controlar los índices, por lo que el espacio en memoria no cambia sin importar 
# qué tan grande sea la lista. Por ende, si la lista está desordenada, la lógica de descartar las mitades se rompe 
# por completo.

# La busqueda lineal es mejor usarla para datos completamente desordenados, listas muy pequeñas, estructuras de datos 
# sin acceso directo y/o búsquedas de "única vez".

# La busqueda binaria es ideal para datos previamente ordenados, bases de datos gigantescas o "Big Data", sistemas de 
# consultas repetitivas...
