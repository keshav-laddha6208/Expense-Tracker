from utils import load_expenses, save_expenses, add_expense, view_expenses, show_total


def menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")


def main():
    expenses = load_expenses()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Category: ")
            amount = float(input("Amount: "))
            note = input("Note: ")

            add_expense(expenses, category, amount, note)
            save_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
