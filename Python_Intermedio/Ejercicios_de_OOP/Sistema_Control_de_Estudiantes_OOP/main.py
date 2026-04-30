#Main program.

import csv
from menu import main_menu
from actionsOOP import *
from data import *

while True:
    choice = main_menu()

    if choice == 1:
        create_student(students_list)

    elif choice == 2:
        if students_list:
            remove_student(students_list)
        else:
            print("Please add or import students first.")

    elif choice == 3:
        display_students_information(students_list)

    elif choice == 4:
        display_top_3_performers(students_list)

    elif choice == 5:
        if students_list:
            display_grade_point_average(students_list)
        else:
            print("Please add students to calculate the average.")

    elif choice == 6:
        display_failed_grades(students_list)

    elif choice == 7:
        students_list = import_from_csv('students.csv')

    elif choice == 8:
        export_to_csv(students_list, 'students.csv')

    elif choice == 9:
        print("\n-- Thank you for using the Student's Manager --\n")
        break
    else:
        print("The option must be a number (1-9).\n")
