"""
Day 2 — Control Flow 
Concepts: if/elif/else, while loops, for loops, boolean logic (and/or/not), break/continue

Build: Turn your script into a menu-driven loop:

1. Add income
2. Add expense
3. View balance
4. Exit
Use a while True loop that keeps showing the menu until the user picks Exit
Validate menu choices (reject anything not 1–4, loop back and ask again)
"""




def print_main_interface():
    print("=== Finance Tracker ===")
    print("1. Add income")
    print("2. Add expense")
    print("3. View Balance")
    print("4. Exit")
    
def print_income_interface(current_balance):
    income_description = input("Enter income description: ")
    income_amount = float(input("Enter amount: "))
    current_balance += income_amount
    return current_balance
    
def print_expense_interface(current_balance):
    expense_description = input("Enter expense description: ")
    expense_amount = float(input("Enter amount: "))
    current_balance -= expense_amount
    return current_balance
    
def print_view_balance_interface(current_balance):
    print(f"Current balance: ₱{current_balance}")
    
def print_exit_interface():
    print("Goodbye!")
    


current_balance = 500.00
while True:
    print_main_interface()
    user_input = input("Choose an option: ").strip()
    if user_input == "1":
        current_balance = print_income_interface(current_balance)
        print("Income Added!")
    elif user_input == "2":
        current_balance = print_expense_interface(current_balance)
        print("Expense Added!")
    elif user_input == "3":
        print_view_balance_interface(current_balance)
    elif user_input == "4":
        print_exit_interface()
        break
    else:
        print("Invalid choice. Please enter from 1-4.")


