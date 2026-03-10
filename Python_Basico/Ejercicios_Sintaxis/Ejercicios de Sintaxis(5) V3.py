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
total_grades = int(input("Indique cuantas notas desea agregar: "))
print(f"Por favor ingrese sus {total_grades} notas.")
for i in range(total_grades):
    grade = int(input(f"Ingrese la nota #{i+1}: "))
    total_sum += grade

    if grade >= 70:
        approved_count += 1
        approved_sum += grade
        
    else:
        not_approved_count += 1
        not_approved_sum += grade
        
overall_avg = total_sum / total_grades
approved_avg = 0 
if approved_count > 0:
    approved_avg = approved_sum / approved_count

not_approved_avg = 0
if not_approved_count > 0:
    not_approved_avg = not_approved_sum / not_approved_count 

print("\n---Resultados---")
print(f"Su total de notas aprobadas fue de {approved_count}.")
print(f"Su total de notas desaprobadas fue de {not_approved_count}.")
print(f"Su promedio general fue {overall_avg:.2f}.")
print(f"Su promedio de notas aprobadas fue {approved_avg:.2f}.")
print(f"Su promedio de notas desaprobadas fue {not_approved_avg:.2f}.")