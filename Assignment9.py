def main():
    print("Welcome to budget tracker!")
    income = get_income()           # Get income from user
    expenses = get_expenses()       # Get list of expenses
    printsummary(income, expenses)  # Display summary and expense list
    print("\nCompleted by, Vincent Cain")
def get_income():
    while True:
        income_input = input("Enter your total income: ")
        try:
            income = float(income_input)
            if income < 0:
                raise ValueError("Income cannot be negative.")
            return income
        except ValueError:
            print("Invalid input: Please enter a valid income amount greater than or equal to 0.")
def get_expenses():
    expenses = []
    while True:
        try:
            expense_input = input("Enter an expense amount (enter 0 to exit): ")
            expense = float(expense_input)
            if expense < 0:
                raise ValueError("Expense cannot be negative.")
            if expense == 0:
                break  
            expenses.append(expense)
        except ValueError:
            print("Invalid input: Please enter a valid expense amount greater than or equal to 0.")
    return expenses
def printsummary(income, expenses):
    total_expenses = sum(expenses)
    remaining = income - total_expenses

    # Print summary
    print("\n——— Budget Results ———")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining:.2f}")

    # Print each expense
    print("\n——— Expense List ———")
    count = 1
    for expense in expenses:
        print(f"{count}. ${expense:.2f}")
        count += 1
main()
