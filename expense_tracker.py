"""
Personal Expense Tracker
A small command-line Python application for recording and reviewing expenses.
"""

import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    """Load expenses from the JSON data file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Expense data must be a list.")
        return data
    except (json.JSONDecodeError, OSError, ValueError):
        print("Warning: Could not read expense data. Starting with an empty list.")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON data file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
        return True
    except OSError as exc:
        print(f"Error saving expenses: {exc}")
        return False


def validate_amount(value):
    """Return a positive float amount or raise ValueError."""
    try:
        amount = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("Amount must be a valid number.") from exc

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    return round(amount, 2)


def validate_category(category):
    """Return a cleaned category or raise ValueError."""
    category = category.strip()
    if not category:
        raise ValueError("Category cannot be empty.")
    if len(category) > 30:
        raise ValueError("Category must be 30 characters or fewer.")
    return category.title()


def validate_description(description):
    """Return a cleaned description or raise ValueError."""
    description = description.strip()
    if not description:
        raise ValueError("Description cannot be empty.")
    if len(description) > 100:
        raise ValueError("Description must be 100 characters or fewer.")
    return description


def add_expense(expenses, amount, category, description):
    """Validate and add an expense. Return the created record."""
    amount = validate_amount(amount)
    category = validate_category(category)
    description = validate_description(description)

    expense = {
        "id": len(expenses) + 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(expense)
    return expense


def calculate_total(expenses):
    """Return the total amount of all expenses."""
    return round(sum(expense["amount"] for expense in expenses), 2)


def category_totals(expenses):
    """Return spending totals grouped by category."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = round(totals.get(category, 0) + expense["amount"], 2)
    return totals


def display_expenses(expenses):
    """Print all stored expenses in a readable table."""
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\nID  Date        Amount       Category        Description")
    print("-" * 65)
    for expense in expenses:
        print(
            f"{expense['id']:<3} "
            f"{expense['date']:<11} "
            f"₹{expense['amount']:<10.2f} "
            f"{expense['category']:<15} "
            f"{expense['description']}"
        )


def display_summary(expenses):
    """Print total spending and category-wise totals."""
    print(f"\nTotal spending: ₹{calculate_total(expenses):.2f}")
    print("Category totals:")
    totals = category_totals(expenses)
    if not totals:
        print("  No data available.")
        return

    for category, amount in sorted(totals.items()):
        print(f"  {category}: ₹{amount:.2f}")


def print_menu():
    """Display the application menu."""
    print("\n=== Personal Expense Tracker ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. Exit")


def run_app():
    """Run the interactive command-line application."""
    expenses = load_expenses()

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            try:
                amount = input("Amount (₹): ")
                category = input("Category: ")
                description = input("Description: ")
                expense = add_expense(expenses, amount, category, description)

                if save_expenses(expenses):
                    print(
                        f"Added expense #{expense['id']} "
                        f"for ₹{expense['amount']:.2f}."
                    )
            except ValueError as exc:
                print(f"Input error: {exc}")

        elif choice == "2":
            display_expenses(expenses)

        elif choice == "3":
            display_summary(expenses)

        elif choice == "4":
            print("Thank you for using Personal Expense Tracker.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    run_app()
