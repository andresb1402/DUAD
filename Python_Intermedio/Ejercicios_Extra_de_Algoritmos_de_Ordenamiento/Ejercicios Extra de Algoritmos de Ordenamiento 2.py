# Conteo de pasos (bubble_sort_steps)

#     Modifique su implementación de bubble_sort para que:
#         Cuente cuántas iteraciones (pasadas) realiza el algoritmo
#         Cuente cuántos intercambios se hicieron en total


class Node:
	data: int
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

	
	def sorting_bubble(self):

		if self.top:
			lap_counter = 0
			changes_counter = 0
			while True:
				lap_counter += 1
				already_sorted = True
				current_node = self.top
				while current_node is not None and current_node.next is not None:
				
					if current_node.data > current_node.next.data:
						current_node.data, current_node.next.data = current_node.next.data, current_node.data
						already_sorted = False
						changes_counter += 1
					current_node = current_node.next
				if already_sorted:
					print('\nAlready sorted.')
					break
			print(f'Iteraciones: {lap_counter}')
			print(f'Intercambios: {changes_counter}')
			return self.print_structure()
					


mi_pila = Stack()

# 1. Metemos elementos a la pila
mi_pila.push(3)
mi_pila.push(10)
mi_pila.push(1)
mi_pila.push(7)
mi_pila.push(2)
mi_pila.push(8)
mi_pila.push(5)
mi_pila.push(4)
mi_pila.push(9)
mi_pila.push(6)

print("\n--- Estructura de la pila (LIFO) ---")
mi_pila.print_structure()

# 2. Sacamos el arriba
print(f"\n-> Sacando con pop: {mi_pila.pop()}")
print(f"\n-> Sacando con pop: {mi_pila.pop()}")


print("\n--- Estructura después del pop ---")
mi_pila.print_structure()


print("\n--- Ordenando ---")
mi_pila.sorting_bubble()