"""
Day 1 — Variables, Types, I/O, Operators

Concepts: variables, int/float/str/bool, type casting, input()/print(),
arithmetic & comparison operators, f-strings
"""

# TASK FOR TODAY:
# Asks the user for a transaction description, amount, and type (income/expense)
# Prints a formatted summary using f-strings
# Calculates and prints a running balance (hardcode a starting balance)

# ValueError - built in exception raised when a function or operation
#              receives an argument that has the correct data type but an 
#              inappropriate value


def print_transaction_summary(transaction_description, transaction_amount, transaction_type, starting_balance):
    print("--- Transaction Summary ---")
    print(f"Description: {transaction_description}")
    print(f"Amount: ₱{transaction_amount}")
    print(f"Type: {transaction_type}")
    print(f"New Balance: ₱{starting_balance}")

starting_balance = 500.00
print(f"Starting balance: ₱{starting_balance}")


transaction_description = input("Enter Transaction: ")
while True:
    try: 
        transaction_amount = float(input("Enter Amount: "))
        break     
    except ValueError:
        print("Error: Amount inputted isn't a number")
    
while True:
    transaction_type = input("Enter Type (Income/Expense): ").strip().lower()
    if transaction_type == "income":
        starting_balance += transaction_amount
        print_transaction_summary(transaction_description, transaction_amount, transaction_type, starting_balance)
        break
    elif transaction_type == "expense":
        starting_balance -= transaction_amount
        print_transaction_summary(transaction_description, transaction_amount, transaction_type, starting_balance)
        break
    else:
        print("Wrong Transaction Type: Please choose Income or Expense")
        


            
    
    
    