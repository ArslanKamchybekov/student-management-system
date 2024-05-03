import csv

student_fields = ['name', 'account type', 'subject']
teacher_fields = ['name', 'account type', 'subject']
student_database = 'students.csv'
subject_database = 'subjects.csv'
teacher_database = 'teachers.csv'

def main():
    #accounts = load_accounts()
    print("To start the program, please enter your account type and your keyword:")
    account_type = input().strip().lower()
    keyword = input().strip()

    if account_type == "student" and keyword == "user-student":
        student_menu()
    elif account_type == "teacher" and keyword == "user-teacher":
        teacher_menu()
    elif account_type == "director" and keyword == "user-director":
        director_menu()
    else:
        print("Sorry, but we did not find this type of account.")

#Director Menu
def director_menu():
    print("--------------")
    print("Director Menu")
    print("--------------")
    print("1. View all subjects")
    print("2. View number of students by subject") #tbd
    print("3. View all teachers") #done
    print("4. Add new teacher") #done
    print("5. Delete teacher") #done
    print("6. Add new student") #done
    print("7. Delete student") #done
    print("8. Quit") #done

    #Director Menu functionality
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            view_subjects()
        elif choice == '2':
            view_students_num()
        elif choice == '3':
            view_teachers()
        elif choice == '4':
            add_teacher()
        elif choice == '5':
            delete_teacher()
        elif choice == '6':
            add_student()
        elif choice == '7':
            delete_student()
        else:
            break

#Teacher Menu
def teacher_menu():
    print("------------")
    print("Teacher Menu")
    print("------------")
    print("1. View all subjects")
    print("2. View all grades")
    print("3. View number of students by subject")
    print("4. View all exams by student")
    print("5. View all tests by student")
    print("6. View max score by subject")
    print("7. View min score by subject")
    print("8. Quit")
    
    #Teacher Menu functionality
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            #view_subjects()
            print("option 1")
        elif choice == '2':
           # view_grades()
           print("option 2")
        elif choice == '3':
            view_students_num()
        elif choice == '4':
            add_teacher()
        elif choice == '5':
            delete_teacher()
        elif choice == '6':
            add_student()
        elif choice == '7':
            delete_student()
        else:
            break  

#Student Menu
def student_menu():
    print("------------")
    print("Student Menu")
    print("------------")
    print("1. View all subjects")
    print("2. View all grades by subject")
    print("3. View all tasks by subject")
    print("4. View all exams by subject")
    print("5. View all tests by subject")
    print("6. View max score by subject")
    print("7. View min score by subject")
    print("8. Quit")   

def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return

def add_teacher():
    print("-------------------------")
    print("Add Teacher Information")
    print("-------------------------")
    global teacher_menu
    global teacher_database

    teacher_data = []
    for field in teacher_fields:
        value = input("Enter " + field + ": ")
        teacher_data.append(value)

    with open(teacher_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([teacher_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return

def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")
    
def view_subjects():
    global subject_database
    print("--- Subjects ---")
    with open(subject_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            for item in row:
                print(item)

    input("Press any key to continue")    
    
def view_students_num():
    global student_fields
    global student_database

    subject_name = input("Enter the subject name: ")

    print(f"--- Students Enrolled in {subject_name} ---")
    num_students = 0

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            if len(row) > 0 and row[2] == subject_name:
                for item in row:
                    print(item, end="\t |")
                print("\n")
                num_students += 1

    print(f"Total students enrolled in {subject_name}: {num_students}")
    return num_students
    
def view_teachers():
    global teacher_fields
    global teacher_database

    print("--- Teacher Records ---")

    with open(teacher_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in teacher_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")    

def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    name = input("Enter name to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if name != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Student ", name, "deleted successfully")
    else:
        print("Student not found in our database")

    input("Press any key to continue")
    
def delete_teacher():
    global teacher_fields
    global teacher_database

    print("--- Delete Teacher ---")
    name = input("Enter name to delete: ")
    teacher_found = False
    updated_data = []
    with open(teacher_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if name != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    teacher_found = True

    if teacher_found is True:
        with open(teacher_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Teacher ", name, "deleted successfully")
    else:
        print("Teacher not found in our database")

    input("Press any key to continue")      

#Student Menu functionality
# while True:
#     student_menu()

#     choice = input("Enter your choice: ")
#     if choice == '1':
#         view_subjects()
#     elif choice == '2':
#         view_students()
#     elif choice == '3':
#         view_teachers()
#     elif choice == '4':
#         add_teacher()
#     elif choice == '5':
#         delete_teacher()
#     elif choice == '6':
#         add_student()
#     elif choice == '7':
#         delete_student()
#     else:
#         break       

print("------------------------------")
print("Thank you for using our system")
print("------------------------------")

if __name__ == "__main__":
    main()
