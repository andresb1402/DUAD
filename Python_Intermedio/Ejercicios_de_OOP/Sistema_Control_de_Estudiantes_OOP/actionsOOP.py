import csv
from data import *

class Student():
    def __init__(self, name, grade_level, group, spanish_score, english_score, social_studies_score, science_score):
        self.name = name
        self.grade_level = grade_level
        self.group = group
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.social_studies_score = social_studies_score
        self.science_score = science_score
	
    
    def get_average(self):
        return (self.spanish_score + self.english_score + self.social_studies_score + self.science_score) / 4
    

    def get_failed_subjects(self):
        all_scores = {
            "Spanish": self.spanish_score,
            "English": self.english_score,
            "Social Studies": self.social_studies_score,
            "Science": self.science_score
        }
        return {sub: score for sub, score in all_scores.items() if score < 60}

    def to_dict(self):
        return {
            "Name": self.name,
            "Grade Level": self.grade_level,
            "Group": self.group,
            "Spanish score": self.spanish_score,
            "English score": self.english_score,
            "Social Studies score": self.social_studies_score,
            "Science score": self.science_score,
            "Average": self.get_average()
        }


def create_student(students_list):
        subjects = ["Spanish", "English", "Social Studies", "Science"]
        while True:
            name = input("Please enter the full name: ").strip()
            if not name or name.isdigit():
                print("Error: Invalid name.")
                continue

            while True:
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
                
                grades = {}
                for s in subjects:
                    while True:
                        try:
                            grade = int(input(f"Enter the {s} grade. (Only numbers): ").strip())
                            if 0 <= grade <= 100:
                                grades[s] = grade
                                break
                            print("Error: 0-100 only")
                        except ValueError:
                            print("Grade must be a number (0-100).")

                
                new_student = Student(
                    name, 
                    grade_level, 
                    group, 
                    grades["Spanish"], 
                    grades["English"], 
                    grades["Social Studies"], 
                    grades["Science"]
                )
                
                students_list.append(new_student)
                print(f"\nSuccessfully added {name}!")
                return new_student


def student_exists(name, grade_level, group, students_list):
    for s in students_list:
        if name.strip().lower() == s.name.strip().lower() and str(grade_level).strip() == str(s.grade_level).strip() and group.strip() == s.group.strip():
            print(f"{name} from {grade_level}{group} already exists.\n")
            return s
    return None


def remove_student(students_list):
    deleted_students = []
    while True:
        name = input("Please enter the full name: ").strip()
        if not name or name.isdigit():
            print("Error: Invalid name.")
            continue
        
        try:
            grade_level = input(f"Please enter the grade level of {name} (Only numbers): ").strip()
            if not grade_level.isdigit():
                print("Error: Grade level must be a number.")
                continue

            group = input(f"Please enter the group of {name} (Only the letter): ").strip().upper()
            if group.isdigit() or len(group) != 1:
                print("Error: Group must be a single letter.")
                continue

            found_student = student_exists(name, grade_level, group, students_list)

            if found_student:
                choice = input(f"Confirm removal of {found_student.name}? (y/n): ").lower().strip()
                if choice == 'y':
                    students_list.remove(found_student)
                    print(f"--- {found_student.name} removed successfully. ---")
                    return
                elif choice == 'N':
                    print("Operation cancelled.\n")
                    break
                else:
                    print("Invalid option. (y/n)")
            else:
                again = input("Student not found. Try again? (y/n): ").lower().strip()
                if again != 'y':
                    return

        except Exception as e:
                print(f"An unexpected error occurred: {e}")


def display_students_information(students_list):
    if not students_list:
        print("No students to show.")
        return
    
    print('-- List of students --')
    for student in students_list:
        print(f'\nName:                   {student.name}')
        print(f'Grade level:            {student.grade_level}')
        print(f'Group:                  {student.group}') 
        print(f'Spanish grade:          {student.spanish_score:.2f}')
        print(f'English grade:          {student.english_score:.2f}')
        print(f'Social Studies grade:   {student.social_studies_score:.2f}')
        print(f'Science grade:          {student.science_score:.2f}')
        print("-" * 45)


def display_top_3_performers(students_list):
    if not students_list:
        print("No students to evaluate.")
        return
    
    sorted_students = sorted(students_list, key=lambda s: s.get_average(), reverse=True)
    top_3 = sorted_students[:3]

    print('-- Top 3 students --')
    for student in top_3:
        print(f'\nName:                   {student.name}')
        print(f'Grade level:            {student.grade_level}')
        print(f'Group:                  {student.group}') 
        print(f'Average grade:          {student.get_average():.2f}')
        print("-" * 45)



def display_grade_point_average(students_list):
    if not students_list:
        print("No students to evaluate.")
        return

    grade_counter = 0
    for student in students_list:
        grade_counter += student.get_average()
    overall_average_grade = grade_counter / len(students_list)
    print(f'-- The overall average grade is: {overall_average_grade:.2f} --')
    return overall_average_grade


def display_failed_grades(students_list):
    print('-- Failed Grades Report --')
    found = False
    for s in students_list:
        failed = s.get_failed_subjects()
        if failed:
            found = True
            print(f"\nStudent: {s.name}")
            for name, score in failed.items():
                print(f"  - {name}: {score}")
            print("-" * 30)
    
    if not found:
        print("\nNo students have failed grades.")


def import_from_csv(students_csv):
    temp_list = []
    try:
        with open(students_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    new_student = Student(
                        row['Name'], 
                        row['Grade Level'], 
                        row['Group'],
                        float(row['Spanish score']),
                        float(row['English score']),
                        float(row['Social Studies score']),
                        float(row['Science score'])
                    )
                    temp_list.append(new_student)
                except ValueError:
                    print(f"Error: Skipping record for {row.get('name')} due to invalid scores.")
        print(f'-- {len(temp_list)} students imported successfully --')
        return temp_list
    except FileNotFoundError:
        print("CSV file not found.")
        return []
    

def export_to_csv(students_list, students_csv):
    if not students_list:
        print("Nothing to export.")
        return
    
    to_export = []
    for s in students_list:
        student_dictionary = s.to_dict()
        to_export.append(student_dictionary)

    keys = to_export[0].keys()

    with open(students_csv, 'w', newline='', encoding='utf-8') as file:
        dict_writer = csv.DictWriter(file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_export)

    print(f"\nData successfully exported to {students_csv}.")