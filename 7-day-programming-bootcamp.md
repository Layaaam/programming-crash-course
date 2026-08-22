# 7-Day Programming Fundamentals Bootcamp
### Stack: Python 3 + VS Code + Git/GitHub
### Project: Personal Finance Tracker (evolves daily, CLI → simple web app)

---

## Why this setup

- **Python** — clean syntax means you spend your energy learning *concepts*, not fighting semicolons or brackets. Skills transfer 1:1 to JS, Java, C#, Go, etc.
- **One evolving project** — instead of 20 disconnected mini-exercises, you rebuild the same app with better tools each day. You *feel* why functions, error handling, and classes exist because you hit the pain they solve.
- **VS Code** — free, has a built-in terminal and a great Python extension (install "Python" by Microsoft).
- **Git/GitHub** — commit at the end of each day. By day 7 you have a public portfolio piece with commit history showing your growth.

### Setup (do this before Day 1, ~20 min)
1. Install Python 3.12+ from python.org
2. Install VS Code + the Python extension
3. Create a folder `finance-tracker`, open it in VS Code
4. Run `git init` inside it, create a GitHub repo, connect it
5. Verify: run `python3 --version` in the terminal

---

## Day 1 — Variables, Types, I/O, Operators
**Concepts:** variables, `int`/`float`/`str`/`bool`, type casting, `input()`/`print()`, arithmetic & comparison operators, f-strings

**Build:** `main.py` — a script that:
- Asks the user for a transaction description, amount, and type (income/expense)
- Prints a formatted summary using f-strings
- Calculates and prints a running balance (hardcode a starting balance)

**Expected output** (example run):
```
$ python3 main.py
Starting balance: $500.00
Enter transaction description: Groceries
Enter amount: 45.20
Is this income or expense? (i/e): e

--- Transaction Summary ---
Description: Groceries
Amount: $45.20
Type: Expense
New balance: $454.80
```

**Stretch:** handle bad input gracefully with a basic `if` check (preview of Day 2).

**Commit message:** `feat: add basic transaction input and balance printout`

---

## Day 2 — Control Flow
**Concepts:** `if`/`elif`/`else`, `while` loops, `for` loops, boolean logic (`and`/`or`/`not`), `break`/`continue`

**Build:** Turn your script into a menu-driven loop:
```
1. Add income
2. Add expense
3. View balance
4. Exit
```
- Use a `while True` loop that keeps showing the menu until the user picks Exit
- Validate menu choices (reject anything not 1–4, loop back and ask again)

**Expected output** (example run):
```
$ python3 main.py

=== Finance Tracker ===
1. Add income
2. Add expense
3. View balance
4. Exit
Choose an option: 5
Invalid choice. Please enter 1-4.
Choose an option: 2
Enter expense description: Coffee
Enter amount: 4.50
Expense added.

=== Finance Tracker ===
1. Add income
2. Add expense
3. View balance
4. Exit
Choose an option: 3
Current balance: $495.50

=== Finance Tracker ===
1. Add income
2. Add expense
3. View balance
4. Exit
Choose an option: 4
Goodbye!
```

**Stretch:** add a category prompt (food, rent, etc.) and reject empty strings.

**Commit message:** `feat: add menu-driven loop with input validation`

---

## Day 3 — Functions & Modules
**Concepts:** `def`, parameters, return values, default arguments, scope (local vs global), splitting code across files (`import`)

**Build:** Refactor everything into functions:
- `add_transaction(transactions, description, amount, category)`
- `calculate_balance(transactions)`
- `print_summary(transactions)`
- `show_menu()`
Move helper functions into a `helpers.py` and `import` them into `main.py`.

**Expected output** (should behave identically to Day 2, but now driven by function calls under the hood):
```
$ python3 main.py

=== Finance Tracker ===
1. Add income
2. Add expense
3. View balance
4. Exit
Choose an option: 1
Enter income description: Freelance payment
Enter amount: 200
Income added via add_transaction()

Choose an option: 3
calculate_balance() returned: $695.50
```
*(The visible behavior shouldn't change much from Day 2 — what matters is that the code is now organized into reusable functions instead of one long block.)*

**Stretch:** write a function `filter_by_category(transactions, category)`.

**Commit message:** `refactor: extract transaction logic into functions and modules`

---

## Day 4 — Data Structures
**Concepts:** lists, dictionaries, tuples, sets, list comprehensions, nested data structures

**Build:** Replace loose variables with a proper structure — each transaction becomes a dictionary:
```python
{"description": "Groceries", "amount": -45.20, "category": "food"}
```
Store all transactions in a list of dicts. Use list comprehensions to:
- Sum all expenses
- Sum all income
- Get unique categories used (`set`)

**Expected output:**
```
$ python3 main.py

Choose an option: 5
--- Category Summary ---
Categories used: {'food', 'transport', 'income'}
Total income: $700.00
Total expenses: $150.70
Net balance: $549.30
```

**Stretch:** produce a dict summarizing total spent per category.

**Commit message:** `refactor: store transactions as list of dicts, add totals via comprehensions`

---

## Day 5 — File I/O & Error Handling
**Concepts:** reading/writing files, the `json` module, `try`/`except`/`finally`, custom exceptions

**Build:** Make the tracker persistent:
- Save transactions to `data.json` on exit
- Load them back on startup
- Wrap file operations and numeric conversions in `try`/`except` (handle missing file, corrupted JSON, non-numeric amount input) without crashing

**Expected output:**
```
$ python3 main.py
No existing data.json found — starting fresh.

Choose an option: 2
Enter expense description: Internet bill
Enter amount: sixty
Error: "sixty" is not a valid number. Please enter a numeric amount.
Enter amount: 60
Expense added.

Choose an option: 4
Saving transactions to data.json...
Goodbye!

$ python3 main.py
Loaded 4 transactions from data.json.
Current balance: $489.30
```

**Stretch:** log errors to an `errors.log` file instead of just printing them.

**Commit message:** `feat: persist transactions to json, handle invalid input and file errors`

---

## Day 6 — Object-Oriented Programming
**Concepts:** classes, `__init__`, instance attributes/methods, encapsulation, one simple parent/child class relationship

**Build:** Refactor around classes:
- `Transaction` class (description, amount, category, date)
- `FinanceTracker` class holding a list of `Transaction` objects, with methods `add()`, `balance()`, `by_category()`, `save()`, `load()`
- Move all logic that touched raw dicts to use these classes instead

**Expected output:**
```
$ python3 main.py
Loaded 4 transactions from data.json.

Choose an option: 3
tracker.balance() -> $489.30

Choose an option: 6
Recurring transaction added: Transaction(description='Rent', amount=-800.00, category='housing', recurring=True)
```

**Stretch:** add a `RecurringTransaction(Transaction)` subclass for things like rent.

**Commit message:** `refactor: introduce Transaction and FinanceTracker classes`

---

## Day 7 — Testing, Polish, and (optional) a Web Face
**Concepts:** unit testing (`unittest` or `pytest`), README writing, optionally Flask basics

**Build:**
1. Write `test_tracker.py` with at least 5 tests covering `add()`, `balance()`, and error cases (e.g., negative amount rejected)
2. Write a proper `README.md`: what it does, how to run it, what you learned
3. **Optional stretch (if energy allows):** wrap your `FinanceTracker` class in a tiny Flask app with 2 routes — one to view transactions, one to add one — so you've touched the web layer too

**Expected output** (running the test suite):
```
$ python3 -m pytest test_tracker.py -v

test_tracker.py::test_add_income PASSED
test_tracker.py::test_add_expense PASSED
test_tracker.py::test_balance_calculation PASSED
test_tracker.py::test_rejects_negative_amount PASSED
test_tracker.py::test_save_and_load_json PASSED

===================== 5 passed in 0.12s =====================
```

**Expected output** (optional Flask stretch):
```
$ python3 app.py
 * Running on http://127.0.0.1:5000
```
Visiting `http://127.0.0.1:5000/transactions` in a browser should return a JSON list of your saved transactions.

**Commit message:** `test: add unit tests for FinanceTracker` + `docs: add README with setup and usage instructions`

---

## Daily rhythm (repeat each day)
1. **15 min** — read/watch the concept (official Python docs or a short tutorial)
2. **60–90 min** — build that day's feature into the project
3. **10 min** — commit to git with a clear message
4. **5 min** — write one sentence in a `LEARNING_LOG.md`: "Today I learned X because it solved Y problem in my project"

## By the end of the week you will have:
- A real, working, persistent Python application
- Hands-on fluency in variables, control flow, functions, data structures, file I/O, error handling, and OOP — the core fundamentals in *every* language
- A GitHub repo with 7 days of commits — genuine proof of progress
- The instinct for *when* to reach for each tool, because you hit the actual problem it solves, not just the syntax
