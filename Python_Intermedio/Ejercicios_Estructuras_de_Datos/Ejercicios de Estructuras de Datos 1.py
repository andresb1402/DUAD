# Cree una estructura de objetos que asemeje un Stack.

#     Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
#     Debe incluir un método para hacer print de toda la estructura.
#     No se permite el uso de tipos de datos compuestos como lists, dicts o 
# 		tuples ni módulos como collections.


class Node:
	data: str
	next: "Node"

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Stack:
	def __init__(self):
		self.top = None


	def print_structure(self):
		current_node = self.top

		if self.top:
			while (current_node is not None):
				print(current_node.data)
				current_node = current_node.next
		else:
			print('Empty list.')


	def push(self, data):
		new_node = Node(data)
		new_node.next = self.top
		self.top = new_node


	def pop(self):
		if self.top:
			to_be_popped = self.top.data
			self.top = self.top.next
			return to_be_popped
		else:
			print('\nEmpty list.')


mi_pila = Stack()

# 1. Metemos platos a la pila
mi_pila.push("Plato 1 (Fondo)")
mi_pila.push("Plato 2 (Medio)")
mi_pila.push("Plato 3 (Tope)")

print("\n--- Estructura de la pila (LIFO) ---")
mi_pila.print_structure()

# 2. Sacamos el de arriba
print(f"\n-> Sacando con pop: {mi_pila.pop()}")
print(f"\n-> Sacando con pop: {mi_pila.pop()}")


print("\n--- Estructura después del pop ---")
mi_pila.print_structure()