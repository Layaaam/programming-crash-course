# Personal Finance Tracker

A command-line personal finance tracker, built over 7 days as a hands-on way to learn Python and core programming fundamentals. Each day adds a new concept — the project grows from a simple script into a tested, persistent, object-oriented application.

## What it does

Tracks income and expenses from the command line: add transactions, categorize them, view your balance, and see spending broken down by category. Data is saved to disk so it persists between runs.

## Tech Stack

- **Python 3**
- **JSON** for data persistence
- **unittest / pytest** for testing
- *(optional)* **Flask** for a minimal web interface

## Getting Started

```bash
git clone <your-repo-url>
cd finance-tracker
python3 main.py
```

No external dependencies required for the core CLI app (standard library only). If you build the optional Flask stretch goal:

```bash
pip install flask
python3 app.py
```

## Project Structure

```
finance-tracker/
├── main.py           # entry point / menu loop
├── helpers.py         # standalone helper functions
├── tracker.py          # FinanceTracker and Transaction classes
├── test_tracker.py    # unit tests
├── data.json           # saved transactions (generated at runtime)
├── errors.log          # error log (generated at runtime)
└── LEARNING_LOG.md     # daily notes on what was learned and why
```

## Build Log

| Day | Concepts | What Was Added |
|-----|----------|-----------------|
| 1 | Variables, types, I/O, operators | Basic transaction entry + balance printout |
| 2 | Control flow (`if`/`while`/`for`) | Menu-driven loop with input validation |
| 3 | Functions & modules | Refactored logic into reusable functions across files |
| 4 | Data structures | Transactions stored as list of dicts, list comprehensions for totals |
| 5 | File I/O & error handling | Persisted data to `data.json`, wrapped risky code in `try`/`except` |
| 6 | Object-oriented programming | Refactored into `Transaction` and `FinanceTracker` classes |
| 7 | Testing & polish | Added unit tests, docs, *(optional)* Flask web wrapper |

## Running Tests

```bash
python3 -m pytest test_tracker.py
```

## What I Learned

This project was built as part of a 7-day fundamentals bootcamp, one concept per day, applied directly to a real evolving codebase rather than isolated exercises. See `LEARNING_LOG.md` for daily notes on what was learned and why each concept mattered.

## License

MIT — free to use, copy, and adapt.
