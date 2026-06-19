# Implemente un bubble_sort que funcione para los ejercicios de estructura de datos: 

#   La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso


class Node:
	data: int
	next: "Node"
	prev: "Node"

	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev


class DoubleEndedQueue:
	def __init__(self):
		self.head = None
		self.tail = None


	def print_structure(self):
		current_node = self.head
		if self.head:
			while (current_node is not None):
				print(current_node.data)
				current_node = current_node.next
		else:
			print('Empty list.')


	def print_structure_reverse(self):
		current_node = self.tail # Empezamos desde el final
		if self.tail:
			while (current_node is not None):
				print(current_node.data)
				current_node = current_node.prev # Caminamos hacia atrás
		else:
			print('Empty list.')


	def push_left(self, data):
		if self.head is None:
			new_left_node = Node(data)
			self.head = new_left_node
			self.tail = new_left_node
		else:
			new_left_node = Node(data)
			new_left_node.next = self.head
			self.head.prev = new_left_node
			self.head = new_left_node


	def push_right(self, data):
		if self.head is None or self.tail is None:
			new_left_node = Node(data)
			self.head = new_left_node
			self.tail = new_left_node
		else:
			new_right_node = Node(data)
			new_right_node.prev = self.tail
			self.tail.next = new_right_node
			self.tail = new_right_node


	def pop_left(self):
		if self.head is None:
			print('\nEmpty list.')
			return None
		elif self.head == self.tail:
			to_be_popped = self.head.data
			self.head = None
			self.tail = None
			return to_be_popped
		else:
			current_head = self.head.data
			self.head = self.head.next
			self.head.prev = None
			return current_head

	
	def pop_right(self):
		if self.head is None:
			print('\nEmpty list.')
			return None
		elif self.head == self.tail:
			to_be_popped = self.tail.data
			self.head = None
			self.tail = None
			return to_be_popped
		else:
			current_tail = self.tail.data
			self.tail = self.tail.prev
			self.tail.next = None
			return current_tail


	def sorting_bubble(self):

		if self.head:
			while True:
				already_sorted = True
				current_node = self.head

				while current_node is not None and current_node.next is not None:
					if current_node.data > current_node.next.data:
						current_node.data, current_node.next.data = current_node.next.data, current_node.data
						already_sorted = False
					current_node = current_node.next
				if already_sorted:
					print('\nAlready sorted.')
					break
			return self.print_structure()
		

my_queue = DoubleEndedQueue()

# Metemos elementos en desorden
my_queue.push_right(1)
my_queue.push_left(3)
my_queue.push_left(4)
my_queue.push_right(2)
my_queue.push_right(5)

print("--- Estructura inicial del Deque ---")
my_queue.print_structure()

print(f"\nHacemos pop_left: {my_queue.pop_left()}")
# print(f"Hacemos pop_right: {my_queue.pop_right()}")


print("\n--- Estructura final ---")
my_queue.print_structure()

print("\n--- Ordenando ---")
my_queue.sorting_bubble()
