import json

expenses = []

# Load existing data
try:
    with open("expense.json", "r") as file:
        expenses = json.load(file)
except:
    expenses = []

print("Monthly or Yearly Expense")

while True:
    print("\n1.ADD EXPENSE\n2.VIEW EXPENSES\n3.TOTAL EXPENSE\n4.SAVE AND EXIT")
    
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Please enter a valid number (1-4)")
        continue

    # Add Expense
    if choice == 1:
        try:
            amount = float(input("Enter the amount: "))
        except:
            print("Invalid amount")
            continue

        category = input("Enter the category: ").strip()
        note = input("Enter the notes: ").strip()

        if category == "" or note == "":
            print("Category and Note cannot be empty")
            continue

        expense = {
            'amount': amount,
            'category': category,
            'note': note
        }

        expenses.append(expense)
        print("Successfully added")

    # View Expenses
    elif choice == 2:
        if not expenses:
            print("No expenses found")
        else:
            print("\n--- Expense List ---")
            for exp in expenses:
                print(f"Amount: ₹{exp['amount']} | Category: {exp['category']} | Note: {exp['note']}")

    # Total Expense
    elif choice == 3:
        total = sum(exp["amount"] for exp in expenses)
        print(f"Total Expense: ₹{total}")

    # Save & Exit
    elif choice == 4:
        with open("expense.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print("Data saved successfully")
        break

    else:
        print("Invalid choice (1-4 only)")
