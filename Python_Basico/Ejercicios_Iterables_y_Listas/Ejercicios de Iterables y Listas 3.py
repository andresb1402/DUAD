#Cree un programa que intercambie el primer y ultimo 
# elemento de una lista. Debe funcionar con listas de cualquier tamaño.

list1 = ["A","B","C","D","E","F","G"]
index_count = len(list1)

for left in range(len(list1) // 2):
    right = (index_count - 1) - left
    list1[left], list1[right] = list1[right], list1[left]
print(list1)

