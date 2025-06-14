while True:
    try:
        investment = int(input("Enter investment amount (1 - 49999): "))
        if 0 < investment < 50000:
            break
        else:
            print("Invalid input. Please enter a value between 1 and 49,999.")
    except ValueError:
        print("Please enter a valid integer.")
        # interest rate
while True:
    try:
        rate = float(input("Enter yearly interest rate (greater than 0 and less than 15): "))
        if 0 < rate < 15:
            break
        else:
            print("Invalid input. Please enter a rate between 0 and 15.")
    except ValueError:
        print("Please enter a valid number.")

# input time duration
while True:
    try:
        duration = int(input("Enter duration in years (greater than 0): "))
        if duration > 0:
            break
        else:
            print("Invalid input. Duration must be greater than 0.")
    except ValueError:
        print("Please enter a valid integer.")

# Convert to months and monthly interest rate
months = duration * 12
monthly_rate = rate / 12 / 100

# Calculate compounded interest
total_value = 0

for month in range(1, months + 1):
    total_value += investment  # Add monthly investment
    interest = round(total_value * monthly_rate, 2)  # Calculate interest
    total_value += interest  # Add interest to total

    # Output every full year
    if month % 12 == 0:
        year = month // 12
        print(f"Year {year}: Current value = ${round(total_value, 2)}")

# Final output
print("\nFinal Results:")
print(f"Years calculated: {duration}")
print(f"Yearly interest rate: {rate}%")
print(f"Monthly investment amount: ${investment}")
print(f"Total after compounding: ${round(total_value, 2)}")

# Completion statement
print('\nCompleted by, Vincent Cain')