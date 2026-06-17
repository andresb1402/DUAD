# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero
my_list = [14, 30, 15, 25, 2, 6]

def sorting_bubble(my_list):
    for i in range (len(my_list)):
        already_sorted = True
        print(f"\n--- PASADA GENERAL #{i + 1} ---")
        for index in range (0, len(my_list) - 1):
            left = -2 - index
            right = -1 - index
            if my_list[right] < my_list[left]:
                my_list[right], my_list[left] = my_list[left], my_list[right]
                already_sorted = False
            print(f"  Comparando índices {right} y {left} -> Lista actual: {my_list}")

        if already_sorted:
            print('\nLa lista ya está ordenada.')
            break
    print(f'Lista ordenada: {my_list}')

print(f'Lista original: {my_list}')
sorting_bubble(my_list)