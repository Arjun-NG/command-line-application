import csv

# File to store expenses
filename = "expenses.csv"


def load_expenses():
    """Load existing expenses from the file"""
    expenses = []
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            expenses = list(reader)
    except FileNotFoundError:
        pass
    return expenses


def add_expense():
    """Prompt the user for expense details and add them"""
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    amount = input("Enter amount (₹): ")
    description = input("Enter description: ")

    expense = [date, category, amount, description]
    expenses.append(expense)
    save_expenses(expenses)
    print("\nExpense added successfully!")


def view_expenses(expenses):
    """Display all expenses"""
    print("\nExpenses:")
    for expense in expenses:
        print(f"Date: {expense[0]}, Category: {expense[1]}, Amount: ₹{expense[2]}, Description: {expense[3]}")


def save_expenses(expenses):
    """Save expenses to the file"""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)


# Load expenses from file
expenses = load_expenses()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
