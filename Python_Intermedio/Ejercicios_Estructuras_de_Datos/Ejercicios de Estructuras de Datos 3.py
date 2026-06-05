# Cree una estructura de objetos que asemeje un Binary Tree.

#     Debe incluir un método para hacer print de toda la estructura.
#     No se permite el uso de tipos de datos compuestos como lists, 
# 		dicts o tuples ni módulos como collections.


class Node:
	data: str
	right: "Node"
	left: "Node"

	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


class BinaryTree:
	def __init__(self):
		self.root = None


	def print_structure(self):
    
		def check_tree(current_node):
			if current_node is None:
				return
			else:
				print(current_node.data)
				check_tree(current_node.left)
				check_tree(current_node.right)

		if self.root is None:
			print('Empty tree.')
		else:
			check_tree(self.root)


my_tree = BinaryTree()

# Ingreso de datos.
my_tree.root = Node("Abuelo")
my_tree.root.left = Node("Padre")
my_tree.root.right = Node("Tío")

# Le metemos más datos.
my_tree.root.left.left = Node("Nieto Mayor")
my_tree.root.left.right = Node("Nieto Menor")

# --- Print ---
print("--- Estructura del Árbol ---")
my_tree.print_structure()