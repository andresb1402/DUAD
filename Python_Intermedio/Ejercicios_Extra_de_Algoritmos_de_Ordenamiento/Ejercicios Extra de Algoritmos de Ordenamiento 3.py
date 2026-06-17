# Validación de entrada antes de ordenar

#     Cree una función que reciba una lista y valide:
#         Que todos los elementos sean números
#         Que no esté vacía
#         Luego aplique bubble_sort si pasa las validaciones
#         Si hay error, debe lanzar un mensaje apropiado


def list_validation(list):
	if list:
		print(f'Original list: {list}')
		has_error = False
		for element in list:
			if type(element) not in (int, float):
				has_error = True
				print(f"Error: List contains non-numeric values: '{element}'")
				break

		if not has_error:
			return sorting_bubble(list)
				
	else:
		print("Empty list")


def sorting_bubble(list):
	for i in range (len(list)):
		already_sorted = True
		for index in range (0, len(list) - 1):

			if list[index] > list[index + 1]:
				list[index], list[index + 1] = list[index + 1], list[index]
				already_sorted = False

		if already_sorted:
			print('\nDone.')
			break
	print(f'Sorted list: {list}')

my_list1 = ['Ana', 2, 4, 5, 1]
my_list2 = [3, 2, 1, 5, 'Jose']
my_list3 = []
my_list4 = [3, 2, 4, 5, 1]

print('\n--- Checking list #1 ---')
list_validation(my_list1)

print('\n--- Checking list #2 ---')
list_validation(my_list2)

print('\n--- Checking list #3 ---')
list_validation(my_list3)

print('\n--- Checking list #4 ---')
list_validation(my_list4)