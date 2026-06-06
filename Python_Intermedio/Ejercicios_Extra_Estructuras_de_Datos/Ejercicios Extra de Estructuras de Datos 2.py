# Cree una clase LinkedList con los métodos:

#	insert_front(data): Inserta al inicio
# 	insert_back(data): Inserta al final
#   delete(data): Elimina el primer nodo con el valor dado
# 	print_all(): Imprime todos los valores


class Node:
	data: str
	next: "Node"

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def print_all(self):
		current_node = self.head

		if self.head:
			while current_node is not None:
				print(current_node.data)
				current_node = current_node.next
		else:
			print('Empty list.')


	def insert_front(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	
	def insert_back(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = new_node
			

	def delete(self, data):
		if self.head is None:
			print('\nEmpty list.')
			return None
		elif self.head.data == data:
			self.head = self.head.next
			return 
		else:
			current = self.head
			previous = None
			while current is not None and current.data != data:
				previous = current
				current = current.next
			if current is None:
				return "Value not found."
			else:
				previous.next = current.next



mi_lista = LinkedList()

# Insertamos elementos
mi_lista.insert_front("Nodo B")
mi_lista.insert_front("Nodo A")  # Pasa al inicio
mi_lista.insert_back("Nodo C")   # Pasa al final

print("--- Lista Original ---")
mi_lista.print_all()

# Probamos tu algoritmo borrando el nodo del medio
print("\n-> Borrando el 'Nodo B'...")
mi_lista.delete("Nodo B")

print("\n--- Lista Después de Borrar ---")
mi_lista.print_all()