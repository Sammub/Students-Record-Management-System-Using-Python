students = []

# ================= ADD STUDENT =================
def add_student():
    roll = input("Enter Roll No: ")

    for student in students:
        if student["roll"] == roll:
            print("Student already exists!\n")
            return

    name = input("Enter Name: ")
    course = input("Enter Course: ")
    grade = input("Enter Grade: ")

    personal = {
        "phone": "",
        "email": "",
        "address": ""
    }

    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "grade": grade,
        "personal": personal
    }

    students.append(student)
    print("Student added successfully!\n")

# ================= SEARCH =================
def search_student():
    roll = input("Enter Roll No: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Details:")
            print(f"Roll: {student['roll']}")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Grade: {student['grade']}")

            print("---- Personal Info ----")
            for key, value in student["personal"].items():
                print(f"{key}: {value}")
            print()
            return

    print("Student not found!\n")

# ================= UPDATE ACADEMIC =================
def update_academic():
    roll = input("Enter Roll No: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("New Name: ")
            student["course"] = input("New Course: ")
            student["grade"] = input("New Grade: ")

            print("Academic info updated!\n")
            return

    print("Student not found!\n")

# ================= UPDATE PERSONAL INFO =================
def update_personal_info():
    roll = input("Enter Roll No: ")

    for student in students:
        if student["roll"] == roll:
            print("Enter Personal Details:")

            student["personal"]["phone"] = input("Phone: ")
            student["personal"]["email"] = input("Email: ")
            student["personal"]["address"] = input("Address: ")

            print("Personal info updated successfully!\n")
            return

    print("Student not found!\n")

# ================= DELETE =================
def delete_student():
    roll = input("Enter Roll No: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found!\n")

# ================= DISPLAY =================
def display_students():
    if not students:
        print("No records available!\n")
        return

    print("\n===== ALL STUDENT RECORDS =====")
    for student in students:
        print("\n----------------------")
        print(f"Roll: {student['roll']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Grade: {student['grade']}")

        print("---- Personal Info ----")
        for key, value in student["personal"].items():
            print(f"{key}: {value}")
    print()

# ================= COUNT =================
def count_students():
    total = len(students)
    if total == 0:
        print("No student records available.\n")
    else:
        print(f"Total number of students: {total}\n")

# ================= MENU =================
def menu():
    while True:
        print("===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Academic Info")
        print("4. Update Personal Info")
        print("5. Delete Student")
        print("6. Display All Students")
        print("7. Count Students")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_academic()
        elif choice == "4":
            update_personal_info()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            display_students()
        elif choice == "7":
            count_students()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

# ================= RUN =================
menu()