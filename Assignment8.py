import csv

# Function to create a new contact file with header
def create_file():
    with open("contacts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
    print("Contact file created successfully.") 
# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    with open("contacts.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
    print("Contact added successfully.")
# Function to display all contacts
def view_contacts():
    try:
        with open("contacts.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No contact file found. Please create it first.")
# Function to modify an existing contact by name
def modify_contact():
    try:
        with open("contacts.csv", "r") as f:
            reader = csv.reader(f)
            contacts = list(reader) # convert to list to modify
        for contact in contacts:
            print(" | ".join(contact)) # show all contacts to choose from
        name_to_edit = input("Enter the name of the contact to edit: ")
        found = False

        for i in range(1, len(contacts)):  # skip header row
            if contacts[i][0] == name_to_edit:
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email address: ")
                contacts[i][1] = new_phone
                contacts[i][2] = new_email
                found = True
                break
        if found:
            with open("contacts.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(contacts)
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contact file found. Please create it first.")
# Main menu function
def main():
    print("Welcome to the Contact Manager Program")
    print("This program lets you create, add, view, and edit contacts stored in a CSV file.")

    while True:
        print("\nMenu:")
        print("1 - Create a new contact CSV file")
        print("2 - Add a new contact")
        print("3 - View all contacts")
        print("4 - Modify an existing contact")
        print("5 - Exit the program")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            view_contacts()
        elif choice == "4":
            modify_contact()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
    print("Completed by, Vincent Cain")