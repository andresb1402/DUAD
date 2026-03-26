#Main program.

import csv
from menu import main_menu
from actions import *
from data import *

while True:
    choice = main_menu()

    if choice == 1:
        new_student = add_student()
        students_list.append(new_student)
        print("\nThe student has been added to the Students List.\n")
        print(students_list)

    elif choice == 2:
        remove_student(students_list)

    elif choice == 3:
        display_students_information(students_list)

    elif choice == 4:
        overall_avg_grade = display_top_3_performers(students_list)

    elif choice == 5:
        if overall_avg_grade:
            display_grade_point_average(overall_avg_grade)
        else:
            print("Please run option 3 first to calculate averages.")

    elif choice == 6:
        display_failed_grades(students_list)

    elif choice == 7:
        export_to_csv(students_list, 'students.csv')
        print("\nThe information has been exported, file 'students.csv' was created.\n")

    elif choice == 8:
        import_from_csv('students.csv', students_list)

    elif choice == 9:
        print("\n--Thank you for using the Student's Manager--\n")
        break
    else:
        print("The option must be a number (1-9).\n")
