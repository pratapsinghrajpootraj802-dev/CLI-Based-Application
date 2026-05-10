# Student Manager CLI Application

students = []

# Function to add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    print("\n✅ Student added successfully!\n")


# Function to view students
def view_students():
    if len(students) == 0:
        print("\n⚠ No student records found.\n")
        return

    print("\n📋 Student List:")
    print("-" * 40)
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name   : {student['name']}")
        print(f"   Roll   : {student['roll']}")
        print(f"   Course : {student['course']}")
        print("-" * 40)
    print()


# Function to delete student
def delete_student():
    if len(students) == 0:
        print("\n⚠ No students to delete.\n")
        return

    view_students()
    try:
        index = int(input("Enter student number to delete: "))
        if 1 <= index <= len(students):
            removed = students.pop(index - 1)
            print(f"\n❌ Removed {removed['name']} successfully!\n")
        else:
            print("\n⚠ Invalid student number.\n")
    except ValueError:
        print("\n⚠ Please enter a valid number.\n")


# Main menu loop
def main():
    while True:
        print("===== 🎓 Student Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("\n👋 Exiting program... Goodbye!")
            break
        else:
            print("\n⚠ Invalid choice. Try again.\n")


# Run the program
main()
