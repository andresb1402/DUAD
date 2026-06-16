# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
my_list = [14, 30, 15, 25, 2, 6]

def sorting_bubble(my_list):
    for i in range (len(my_list)):
        already_sorted = True
        print(f"\n--- PASADA GENERAL #{i + 1} ---")
        for index in range (0, len(my_list) - 1):

            if my_list[index] > my_list[index + 1]:
                my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
                already_sorted = False
            print(f"  Comparando índice {index} y {index+1} -> Lista actual: {my_list}")
        if already_sorted:
            print('\nLa lista ya está ordenada.')
            break
    print(f'Lista ordenada: {my_list}')

print(f'Lista original: {my_list}')
sorting_bubble(my_list)