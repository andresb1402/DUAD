#Actions to be performed based on the user's election. 

import csv
from data import *

def add_student():
    subjects = ["Spanish", "English", "Social Studies", "Science"]
    while True:
        new_student = {'Name':'', 'Grade Level':'', 'Group':'', 'Spanish grade':'', 'English grade':'', 'Social Studies grade':'', 'Science grade':''} 
        name = input("Please enter the full name of the student (name + last name): ").strip()
        if name.isspace() or len(name) == 0 or name.isdigit():
            print("Error: Name cannot be empty, a spaces or a number.")
            continue
        while True:
            try:
                grade_level = input(f"Please enter the grade level of {name} (Only numbers): ").strip()
                if not grade_level.isdigit():
                    print("Error: Grade level must be a number.")
                    continue

                group = input(f"Please enter the group of {name} (Only the letter): ").strip().upper()
                if group.isdigit() or len(group) != 1:
                    print("Error: Group must be a single letter.")
                    continue

                if student_exists(name, grade_level, group, students_list):
                    print(f"\nError: {name} already exists in grade {grade_level}, group {group}.\n")
                    again = input("Try a different student? (y/n): ").lower()
                    if again == 'y':
                        break
                    else:
                        return None
                    
                for s in subjects:
                    while True:
                        try:
                            grade = int(input(f"Enter the {s} grade. (Only numbers): ").strip())
                            if 0 <= grade <= 100:
                                new_student[f"{s} grade"] = str(grade)
                                break
                            print("Error: 0-100 only")
                        except ValueError:
                            print("Grade must be a number (0-100).")

                new_student['Name'] = name
                new_student['Grade Level'] = str(grade_level)
                new_student['Group'] = group

                return new_student
    
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


def student_exists(name, grade_level, group, students_list):
    for s in students_list:
        if name.strip() == s['Name'].strip() and str(grade_level).strip() == str(s['Grade Level']).strip() and group.strip() == s['Group'].strip():
            print(f"{name} from {grade_level}{group} already exists.\n")
            return s
    return None

def remove_student(students_list):
    while True:
        student = input("Please enter the name of the student you want to remove: ").strip()
        if student.isspace() or len(student) == 0 or student.isdigit():
            print("Error: Name cannot be empty, a spaces or a number.")
            continue
        try:
            level = input(f"Enter the grade level of {student}. (Only numbers): ").strip()
            if not level.isdigit():
                    print("Error: Grade level must be a number.")
                    continue
            group = input(f"Please enter the group of {student}. (Only the letter): ").capitalize().strip()
            if group.isdigit() or len(group) != 1:
                    print("Error: Group must be a single letter.")
                    continue
            found_student = None
            for s in students_list:
                if student == s['Name'] and str(level) == str(s['Grade Level']) and group == s['Group']:
                    print(f"{student} from {level}{group} was found.\n")
                    found_student = s
                    break
            if found_student:
                choice = input(f"{student} will be removed, are you sure? (y/n): ").capitalize().strip()
                if choice == 'Y':
                    students_list.remove(found_student)
                    deleted_students.append(found_student)
                    print(f"\n{student} from {level}{group} was removed.")
                    break
                elif choice == 'N':
                    print("Operation cancelled.\n")
                    break
                else:
                    print("Invalid option. (y/n)")
            else:
                print(f"Student '{student}' not found in {level}{group}.")
                again = input("Do you want to try again? (y/n): ").capitalize().strip()
                if again != 'Y':
                    break

        except Exception as e:
                print(f"An unexpected error occurred: {e}")


def add_student_to_list(new_student, students_list):
    students_list.append(new_student)


def display_students_information(students_list):
    print('--List of students--\n')
    for row in students_list:
        print(f'Name: {row["Name"]}')
        print(f'Grade level: {row["Grade Level"]}')
        print(f'Group: {row["Group"]}')
        print(f'Spanish grade: {row["Spanish grade"]}')
        print(f'English grade: {row["English grade"]}')
        print(f'Social Studies grade: {row["Social Studies grade"]}')
        print(f'Science grade: {row["Science grade"]}\n')


def display_top_3_performers(students_list):
    top_performers = []
    print('--Top 3 performers--\n')
    for row in students_list:
        average_dict = {'Name':'', 'Grade Level':'', 'Group':'', 'Average grade':''}
        average_grade = (float(row["Spanish grade"]) + float(row["English grade"]) + float(row["Social Studies grade"]) + float(row["Science grade"]))/4
        average_dict['Name'] = row["Name"]
        average_dict['Grade Level'] = row["Grade Level"]
        average_dict['Group'] = row["Group"]
        average_dict['Average grade'] = average_grade
        top_performers.append(average_dict)
    sorted_grades = sorted(top_performers, key=lambda x: x['Average grade'], reverse=True)
    top_3 = sorted_grades[:3]
    for student in top_3:
        print(f'Name: {student["Name"]}')
        print(f'Grade level: {student["Grade Level"]}')
        print(f'Group: {student["Group"]}') 
        print(f'Average grade: {student["Average grade"]:.2f}')
        print()
    return top_performers


def display_grade_point_average(top_performers):
    grade_counter = 0
    for student in top_performers:
        grade_counter += student['Average grade']
    overall_average_grade = grade_counter/len(top_performers)
    print(f'\n--The overall average grade is: {overall_average_grade:.2f}.--\n')
    return overall_average_grade


def display_failed_grades(students_list):
    low_performers = []
    print('--Failed grades--\n')
    subjects = ["Spanish grade", "English grade", "Social Studies grade", "Science grade"]

    for student in students_list:
        low_dict = {'Name': student['Name'], 'Grade Level': student['Grade Level'], 'Group': student['Group']}
        failed = False
        for s in subjects:
            grade = float(student[s])
            if grade < 60:
                low_dict[s] = grade
                failed = True
        if failed:
            low_performers.append(low_dict)
    if not low_performers:
        print("Great news! No students have failed grades.")
        return
    for lp in low_performers:
        print(f"Student: {lp['Name']} {lp['Grade Level']}{lp['Group']}")
        for key, value in lp.items():
            if "grade" in key:
                print(f"  - {key}: {value}")
        print("-" * 20)


def export_to_csv(students_list, students_csv):
    if not students_list:
        print("Nothing to export.")
        return
    
    keys = students_list[0].keys()

    with open('students.csv', 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(students_list)


def import_from_csv(students_csv, students_list):
    try:
        with open(students_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print('--List of students imported--\n')
            for row in reader:
                print(f'Name: {row["Name"]}')
                print(f'Grade level: {row["Grade Level"]}')
                print(f'Group: {row["Group"]}')
                print(f'Spanish grade: {row["Spanish grade"]}')
                print(f'English grade: {row["English grade"]}')
                print(f'Social Studies grade: {row["Social Studies grade"]}')
                print(f'Science grade: {row["Science grade"]}\n')
                row["Group"] = row["Group"].capitalize()
                row["Grade Level"] = int(row["Grade Level"])
                row["Spanish grade"] = int(row["Spanish grade"])
                row["English grade"] = int(row["English grade"])
                row["Social Studies grade"] = int(row["Social Studies grade"])
                row["Science grade"] = int(row["Science grade"])
                students_list.append(row)
            print(students_list)
    except FileNotFoundError:
        print("CSV file not found.")