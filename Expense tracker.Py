import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Add Expense
def add_expense():
    date = input("Enter Date (YYYY-MM-DD) or press Enter for today: ")
    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = float(input("Enter Amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("\nExpense Added Successfully!\n")


# View Expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    if len(data) <= 1:
        print("\nNo expenses found.\n")
        return

    print("\n{:12} {:15} {:25} {:10}".format(
        "Date", "Category", "Description", "Amount"))
    print("-" * 65)

    for row in data[1:]:
        print("{:12} {:15} {:25} {:10}".format(*row))
    print()


# Total Expense
def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expense = ₹{total:.2f}\n")


# Search Expense
def search_expense():
    keyword = input("Enter Category or Date to Search: ").lower()
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\nResults:\n")
        for row in reader:
            if keyword in row["Category"].lower() or keyword in row["Date"]:
                print(row)
                found = True

    if not found:
        print("No matching expense found.\n")


# Delete Expense
def delete_expense():
    view_expenses()

    date = input("\nEnter Date of expense to delete: ")
    description = input("Enter Description: ")

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not (row["Date"] == date and row["Description"] == description):
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["Date", "Category", "Description", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    print("\nExpense Deleted Successfully!\n")


# Main Menu
def menu():
    create_file()

    while True:
        print("========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Show Total Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            total_expense()

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid Choice! Try Again.\n")


menu()
