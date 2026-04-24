#Reto de Registro de Notas

def file_reader(input_file):
    with open(input_file) as inventory:
        print('\nEstas son las notas:\n')
        print(inventory.read())



def str_to_dict(input_file):
    with open(input_file) as grades:
        grades_dict = {}
        for line in grades:
            name, grade = line.strip().split(":")
            grades_dict[name] = int(grade)
        return grades_dict


def add_or_modify_grade(grades_dict):
    new_name = input("Por favor ingrese el nombre del estudiante: ").capitalize()
    new_grade = int(input("Por favor ingrese la nota: "))
    grades_dict[new_name] = new_grade
    return grades_dict


def save_grades(grades_dict, input_file):
    with open(input_file, "w") as grades_file:
        for name, grade in grades_dict.items():
            grades_file.write(f"{name}:{grade}\n")


students_grades = file_reader('notas.txt')
students_grades = str_to_dict('notas.txt')
students_grades = add_or_modify_grade(students_grades)
save_grades(students_grades, 'notas.txt')