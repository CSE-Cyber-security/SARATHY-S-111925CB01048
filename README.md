# Daily Expense Tracker

A small command-line app to log and review your daily expenses. Pure Python (3.10+), no dependencies, data stored in a plain CSV file.

## Project structure

```
expense-tracker/
├── .github/workflows/tests.yml   # CI: runs tests on every push
├── data/
│   └── sample.csv                # example data (your own *.csv is git-ignored)
├── src/expense_tracker/
│   ├── __init__.py
│   ├── __main__.py               # python -m expense_tracker
│   ├── cli.py                    # commands: add, list, delete, summary
│   ├── models.py                 # Expense dataclass + input parsing
│   ├── reports.py                # totals, filters, category/month summaries
│   └── storage.py                # CSV read/write
├── tests/
│   ├── test_reports.py
│   └── test_storage.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Setup

```bash
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker
```

Run directly, no install needed:

```bash
PYTHONPATH=src python -m expense_tracker --help
```

Or install the `expense-tracker` command:

```bash
pip install -e .
```

## Usage

```bash
# Add an expense (date defaults to today)
expense-tracker add 85 food --note "Breakfast and tea"
expense-tracker add 40 travel -d 2026-11-02

# List everything, or filter
expense-tracker list
expense-tracker list --month 2026-11 --category food

# Summary by category and month
expense-tracker summary
expense-tracker summary --month 2026-11

# Delete by id
expense-tracker delete 3
```

Data goes to `data/expenses.csv` by default. Use `--file path/to/file.csv` or set the `EXPENSE_FILE` environment variable to change it. To try the app with example data:

```bash
expense-tracker --file data/sample.csv summary
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

MIT
