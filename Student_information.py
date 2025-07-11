def main():
    # Create dictionary to store student information
    student_info = {}

    # Add students to the dictionary
    student_info["Jim"] = {
        'id': 1,
        'gpa': 3.1,
        'credits-completed': 97.0,
        'grades': [80, 50, 100, 98]
    }

    student_info["Sarah"] = {
        'id': 2,
        'gpa': 3.6,
        'credits-completed': 40.0,
        'grades': [80, 98]
    }

    # Print dictionary containing all student information
    print(student_info)
    print()

    # List the student names
    print("List of Students")
    for name in student_info:
        print(name)
    print()

    # Access and display all student info
    print("Student Information")
    print("Name\tID\tGPA\tCredits Completed\tGrades")
    for name, info in student_info.items():
        print(f"{name}\t{info['id']}\t{info['gpa']}\t{info['credits-completed']}\t\t{info['grades']}")
    print()

    # Remove a student
    print("Sarah has dropped out, removing from student info registry")
    student_info.pop("Sarah")
    print("Updated student registry:")
    print(student_info)
    print()

    # Access GPA information
    print("Getting Jim's GPA")
    print(student_info.get("Jim").get("gpa"))
    print()

    # Clear the dictionary
    print("Students have graduated, clearing the student registry")
    student_info.clear()
    print(student_info)
    print()

    # Completion statement
    print("Completed by, Vincent Cain")


# Run the main function
if __name__ == "__main__":
    main()
