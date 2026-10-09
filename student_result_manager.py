
student = {}

while True:
    print("\n===== Student Result Manager =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter student marks (0-100): "))

        if  0 < 100:
            student[name] = marks
            print("Student added successfully!")
        else:
            print("Marks must be between 0 and 100.")

    # View all students
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    # Check result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found!")

    # Exit
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid input!")