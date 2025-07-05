import random

def get_total(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def get_average(grades):
    return get_total(grades) / len(grades)

def main():
    grades = []

    # Get input from user
    while True:
        user_input = input("Please enter the grade or -1 to stop: ")
        if user_input == "-1":
            break
        grades.append(int(user_input))

    print(grades)

    # Remove lowest grade
    print("Removing lowest grade")
    lowest = min(grades)
    lowest_index = grades.index(lowest)
    grades.pop(lowest_index)
    print(grades)

    # Remove a random grade
    print("Removing random grade")
    random_grade = random.choice(grades)
    grades.remove(random_grade)
    print(grades)

    # Edit a grade
    print("Edit a grade")
    index = 1
    for grade in grades:
        print(str(index) + ". " + str(grade))
        index += 1

    while True:
        choice = int(input("Which grade do you want to edit (enter an number between 1 and " + str(len(grades)) + "): "))
        if 1 <= choice <= len(grades):
            break
        print("Please enter a valid grade!")

    new_grade = int(input("Enter the new grade: "))
    grades[choice - 1] = new_grade
    print(grades)

    # Sort and reverse list
    print("Sorting and Reversing List")
    grades.sort()
    grades.reverse()
    print(grades)

    # Total and average
    print("Getting Grade Total and Average")
    total = get_total(grades)
    average = get_average(grades)
    print("Total:", total)
    print("Average:", average)

    # Completion statement
    print("Completed by, [Your Name Here]")

main()
