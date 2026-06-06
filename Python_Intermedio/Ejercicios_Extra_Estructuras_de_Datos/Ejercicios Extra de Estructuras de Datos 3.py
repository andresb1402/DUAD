# Cree una Lista doblemente enlazada

# Cada nodo debe tener referencia al siguiente y al anterior 
# Metodos:
# 	append(data)
# 	prepend(data)
# 	delete(data)
# 	print_forward()
# 	print_backward()


class Node:
	data: str
	next: "Node"
	prev: "Node"

	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None


	def print_forward(self):
		current_node = self.head
		if self.head:
			while current_node is not None:
				print(current_node.data)
				current_node = current_node.next
		else:
			print('Empty list.')

	def print_backward(self):
		current_node = self.tail
		if self.tail:
			while current_node is not None:
				print(current_node.data)
				current_node = current_node.prev
		else:
			print('Empty list.')


	def prepend(self, data):
		if self.head is None:
			new_left_node = Node(data)
			self.head = new_left_node
			self.tail = new_left_node
		else:
			new_left_node = Node(data)
			new_left_node.next = self.head
			self.head.prev = new_left_node
			self.head = new_left_node


	def append(self, data):
		if self.head is None or self.tail is None:
			new_left_node = Node(data)
			self.head = new_left_node
			self.tail = new_left_node
		else:
			new_right_node = Node(data)
			new_right_node.prev = self.tail
			self.tail.next = new_right_node
			self.tail = new_right_node


	def delete(self, data):
		if self.head is None:
			print('\nEmpty list.')
			return None
		elif self.head.data == data:
			to_be_removed = self.head
			self.head = self.head.next
			if self.head is not None:
				self.head.prev = None
				return to_be_removed.data
			else:
				self.tail = None
			return to_be_removed.data
		elif self.tail.data == data:
			to_be_removed = self.tail
			self.tail = self.tail.prev
			self.tail.next = None
			return to_be_removed.data
		else:
			current = self.head
			while current is not None and current.data != data:
				current = current.next
			if current is None:
				return "Value not found."
			else:
				current.prev.next = current.next
				current.next.prev = current.prev
				return current.data


my_queue = DoublyLinkedList()

# Metemos elementos en desorden
my_queue.append("Elemento 2")
my_queue.prepend("Elemento 1")
my_queue.append("Elemento 3")
my_queue.append("Elemento 4")

print("--- Estructura inicial del Deque ---")
my_queue.print_forward()
print("\n--- Estructura inicial del Deque (reversa) ---")
my_queue.print_backward()

print(f"\n--- Borrando: {my_queue.delete('Elemento 3')} ---")


print("\n--- Estructura final ---")
my_queue.print_forward()