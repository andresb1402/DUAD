# Cree una estructura que represente una cola básica (Queue) con objetos enlazados

# Restricción:
# 	no usar list, dict, tuple, collections 

# Métodos requeridos:
# 	enqueue(data): agrega un nodo al final
# 	dequeue(): elimina y retorna el nodo del inicio
# 	print_all(): imprime todos los elementos de la cola en orden


class Node:
	data: str
	next: "Node"

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def print_structure(self):
		current_node = self.head
		structure_list = []

		if self.head:
			while (current_node is not None):
				structure_list.append(current_node.data)
	
				current_node = current_node.next
			print(" -> ".join(structure_list))
		else:
			print('Empty list.')


	def enqueue(self, data):
		if self.tail is None:
			new_node = Node(data)
			self.head = new_node
			self.tail = new_node
		else:
			new_node = Node(data)
			self.tail.next = new_node
			self.tail = new_node
			

	def dequeue(self):
		if self.head is None:
			print('\nEmpty list.')
			return None
		elif self.head == self.tail:
			to_be_popped = self.tail.data
			self.head = None
			self.tail = None
			return to_be_popped
		else:
			to_be_popped = self.head.data
			self.head = self.head.next
			return to_be_popped


my_queue = Queue()

# 1. Agregamos elementos al stack
my_queue.enqueue("Elemento 1")
my_queue.enqueue("Elemento 2")
my_queue.enqueue("Elemento 3")

print("\n--- Estructura completa del Stack ---")
my_queue.print_structure()

# 2. Sacamos del queue
print(f"\n-> Sacando: {my_queue.dequeue()}")

print("\n--- Estructura después de sacar elementos ---")
my_queue.print_structure()