print("#####STUDENT MANAGEMENT SYSTEM####")
def student_details():
    print("1. Add student details")
    print("2. Display student details")
    print("3. Exit")


details = []

while True:
    student_details()

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        roll_no = int(input("Enter student roll number: "))

        details.append((name, marks, roll_no))

        print("Student details added successfully\n")

    elif choice == 2:

        if len(details) == 0:
            print("No student details found\n")

        else:
            print("\nSTUDENT DETAILS")

            for student in details:
                print(student)

            print()

    elif choice == 3:
        print("You exited the program")
        break

    else:
        print("Invalid choice\n")