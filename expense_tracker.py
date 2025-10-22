expenses = []

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    expenses.append({"category": category, "amount": amount})
    print("Expense added!")

def calculate_stats():
    if not expenses:
        print("No expenses recorded.")
        return
    total = sum(expense["amount"] for expense in expenses)
    highest = max(expenses, key=lambda x: x["amount"])
    print(f"Total spent: ${total:.2f}")
    print(f"Highest expense: ${highest['amount']:.2f} ({highest['category']})")

def view_by_category():
    if not expenses:
        print("No expenses recorded.")
        return
    categories = {}
    for expense in expenses:
        cat = expense["category"]
        categories[cat] = categories.get(cat, 0) + expense["amount"]
    
    print("\nExpenses by category:")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")

def main():
    while True:
        print("\n1. Add expense\n2. View stats\n3. View by category\n4. Exit")
        choice = input("Choose option: ")
        
        if choice == "1": add_expense()
        elif choice == "2": calculate_stats()
        elif choice == "3": view_by_category()
        elif choice == "4": break
        else: print("Invalid option")

if __name__ == "__main__":
    main()