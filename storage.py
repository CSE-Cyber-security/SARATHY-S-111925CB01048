import csv
from datetime import date
from pathlib import Path

from .models import Expense, parse_amount, parse_date

FIELDS = ["id", "date", "category", "amount", "note"]


class ExpenseStore:
    """Reads and writes expenses in a CSV file."""

    def __init__(self, path):
        self.path = Path(path)

    def load(self) -> list[Expense]:
        if not self.path.exists():
            return []
        with self.path.open(newline="", encoding="utf-8") as f:
            return [
                Expense(
                    id=int(row["id"]),
                    date=parse_date(row["date"]),
                    category=row["category"],
                    amount=parse_amount(row["amount"]),
                    note=row["note"],
                )
                for row in csv.DictReader(f)
            ]

    def _save(self, expenses: list[Expense]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            for e in expenses:
                writer.writerow(
                    {
                        "id": e.id,
                        "date": e.date.isoformat(),
                        "category": e.category,
                        "amount": f"{e.amount:.2f}",
                        "note": e.note,
                    }
                )

    def add(self, amount, category, on: date | None = None, note: str = "") -> Expense:
        category = category.strip().lower()
        if not category:
            raise ValueError("Category cannot be empty")
        expenses = self.load()
        new = Expense(
            id=max((e.id for e in expenses), default=0) + 1,
            date=on or date.today(),
            category=category,
            amount=parse_amount(amount),
            note=note.strip(),
        )
        expenses.append(new)
        self._save(expenses)
        return new

    def delete(self, expense_id: int) -> bool:
        expenses = self.load()
        remaining = [e for e in expenses if e.id != expense_id]
        if len(remaining) == len(expenses):
            return False
        self._save(remaining)
        return True
