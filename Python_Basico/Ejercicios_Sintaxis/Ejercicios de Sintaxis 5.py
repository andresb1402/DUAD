# 5. Dada n cantidad de notas de un estudiante, calcular:

# Cuantas notas tiene aprobadas (mayor a 70).
# Cuantas notas tiene desaprobadas (menor a 70).
# El promedio de todas.
# El promedio de las aprobadas.
# El promedio de las desaprobadas.

approved_count = 0
not_approved_count = 0
approved_sum = 0
not_approved_sum = 0
total_sum = 0
total_grades_count = 0
grade = int(input("Por favor ingrese su nota: "))
while True:
    total_sum += grade
    total_grades_count += 1
    if grade >= 70:
        approved_count += 1
        approved_sum += grade
        
    else:
        not_approved_count += 1
        not_approved_sum += grade

    choice = int(input("Desea agregar otra nota? (1. Sí 2. No): "))
    if choice == 1:
        grade = int(input("Ingrese la siguiente nota: "))
    elif choice == 2:
        print("\n---Resultados---")
        break
    else:
        print("Opcion invalida, intente de nuevo.")

overall_avg = total_sum / total_grades_count
approved_avg = 0 
if approved_count > 0:
    approved_avg = approved_sum / approved_count

not_approved_avg = 0
if not_approved_count > 0:
    not_approved_avg = not_approved_sum / not_approved_count 

print(f"Su total de notas aprobadas fue de {approved_count}.")
print(f"Su total de notas desaprobadas fue de {not_approved_count}.")
print(f"Su promedio general fue {overall_avg:.2f}.")
print(f"Su promedio de notas aprobadas fue {approved_avg:.2f}.")
print(f"Su promedio de notas desaprobadas fue {not_approved_avg:.2f}.")