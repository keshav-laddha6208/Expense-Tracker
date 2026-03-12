import json
from datetime import datetime

DATA_FILE = "data/expenses.json"


def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses, category, amount, note):
    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)
    print("Expense added!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for e in expenses:
        print(f"{e['date']} | {e['category']} | ₹{e['amount']} | {e['note']}")


def show_total(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Spending: ₹{total}")
