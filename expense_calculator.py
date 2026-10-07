def get_expenses():
    expenses = {}

    print("\nEnter your expenses.")
    print("Type 'done' when you have finished.\n")

    while True:
        category = input("Enter expense category (Food, Travel, Shopping, etc.): ")

        if category.lower() == "done":
            break

        try:
            amount = float(input(f"Enter amount spent on {category}: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            # Add amount to existing category
            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount

        except ValueError:
            print("Please enter a valid number.")

    return expenses


def calculate_savings(income, total_expenses):
    return income - total_expenses


def display_summary(income, expenses):
    total_expenses = sum(expenses.values())
    savings = calculate_savings(income, total_expenses)

    print("\n" + "=" * 40)
    print("       PERSONAL EXPENSE SUMMARY")
    print("=" * 40)

    print(f"Income          : ₹{income:.2f}")
    print(f"Total Expenses  : ₹{total_expenses:.2f}")
    print(f"Savings         : ₹{savings:.2f}")

    print("\nExpense Categories:")
    print("-" * 40)

    for category, amount in expenses.items():
        percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
        print(f"{category:<15} ₹{amount:>10.2f}  ({percentage:.1f}%)")

    print("-" * 40)

    # Conditions
    if savings > 0:
        print("Status: Great! You have money left after expenses.")
    elif savings == 0:
        print("Status: You spent exactly your income.")
    else:
        print("Status: Warning! Your expenses are greater than your income.")

    print("=" * 40)


# Main program
print("=" * 40)
print("       PERSONAL EXPENSE CALCULATOR")
print("=" * 40)

# Get income
while True:
    try:
        income = float(input("\nEnter your monthly income: ₹"))

        if income < 0:
            print("Income cannot be negative.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")

# Get expenses
expenses = get_expenses()

# Display final report
display_summary(income, expenses)