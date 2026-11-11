import sys
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from expense_tracker.models import Expense  # noqa: E402
from expense_tracker.reports import by_category, by_month, filter_expenses, total  # noqa: E402

DATA = [
    Expense(1, date(2026, 10, 30), "food", Decimal("10.00")),
    Expense(2, date(2026, 11, 1), "food", Decimal("5.50")),
    Expense(3, date(2026, 11, 2), "travel", Decimal("20.00")),
]


class ReportTests(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(DATA), Decimal("35.50"))
        self.assertEqual(total([]), Decimal("0.00"))

    def test_by_category_sorted_desc(self):
        self.assertEqual(
            list(by_category(DATA).items()),
            [("travel", Decimal("20.00")), ("food", Decimal("15.50"))],
        )

    def test_by_month(self):
        self.assertEqual(
            by_month(DATA), {"2026-10": Decimal("10.00"), "2026-11": Decimal("25.50")}
        )

    def test_filters(self):
        self.assertEqual(len(filter_expenses(DATA, month="2026-11")), 2)
        self.assertEqual(len(filter_expenses(DATA, category="FOOD")), 2)
        self.assertEqual(len(filter_expenses(DATA, "2026-11", "travel")), 1)


if __name__ == "__main__":
    unittest.main()
