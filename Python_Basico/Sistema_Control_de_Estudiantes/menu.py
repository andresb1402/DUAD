#This is the menu

def main_menu():
    
        print("\n--Welcome to the Student Manager--\n")
        print("1. Add a new student.")
        print("2. Remove a student.")
        print("3. Display all the students' information.")
        print("4. Display the top 3 students (highest averages).")
        print("5. Display the class average.")
        print("6. Display failed grades.")
        print("7. Export the all the information to a CSV file.")
        print("8. Import the information from a CSV file.")
        print("9. Exit.")
        while True:
            try:
                choice = int(input("\nPlease select one of the options: "))
                print()
                break
            except ValueError:
                print("Error: Please enter a valid number (1-9).\n")
            
        return choice