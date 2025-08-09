# String Replacement Tool
# - Gets a main string and a substring from the user
# - Reports whether the substring occurs and at what index (via .find)
# - Optionally replaces the FIRST occurrence with a new string (via .replace(old, new, 1))

def get_string(prompt): # Ask the user for a string and return it
    return input(prompt)

def find_substring(main_text, sub_text): # Return the starting index of sub_text in main_text using .find(), If not found, returns -1
    return main_text.find(sub_text)

def ask_yes_no(prompt): # Keep asking until the user types yes or no; return True for yes, False for no
    while True:
        answer = input(prompt).strip().lower()
        if answer == "yes":
            return True
        if answer == "no":
            return False
        print("Invalid entry. Please type 'yes' or 'no'.")

def maybe_replace_once(main_text, sub_text):
    # Ask whether to replace the first occurrence of sub_text
    # If yes, ask for a replacement and return the updated string
    # If no, return the original string unchanged
    if ask_yes_no("Would you like to replace the substring with a new string? (yes/no): "):
        new_sub = get_string("Enter the replacement string: ")
        updated = main_text.replace(sub_text, new_sub, 1)  # Replace only first occurrence
        print("\nUpdated string:")
        print(updated)
        return updated
    else:
        print("\nNo replacement was made. Original string:")
        print(main_text)
        return main_text

def main():
    print("Welcome to the String Replacement Tool!\n")

    # Inputs from user
    main_text = get_string("Enter the main string for an example: ")
    sub_text  = get_string("Enter the substring you are searching for: ")

    # Find substring index
    index = find_substring(main_text, sub_text)

    if index != -1:
        print(f"\nSuccess: The substring was found starting at index {index}.")
        # Replacement if found
        main_text = maybe_replace_once(main_text, sub_text)
    else:
        print("\nThe substring was not found in the main string.")
    # Closing messages
    print("\nThank you for using our program.")
    print("Completed by, Vincent Cain")

if __name__ == "__main__":
    main()