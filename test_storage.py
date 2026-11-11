import sys
import tempfile
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from expense_tracker.models import parse_amount  # noqa: E402
from expense_tracker.storage import ExpenseStore  # noqa: E402


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.store = ExpenseStore(Path(self.tmp.name) / "sub" / "expenses.csv")

    def test_empty_store(self):
        self.assertEqual(self.store.load(), [])

    def test_add_and_load(self):
        e = self.store.add("12.5", "Food", on=date(2026, 11, 1), note="lunch")
        self.assertEqual(e.id, 1)
        loaded = self.store.load()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].amount, Decimal("12.50"))
        self.assertEqual(loaded[0].category, "food")
        self.assertEqual(loaded[0].note, "lunch")

    def test_ids_increment_and_delete(self):
        self.store.add("1", "a")
        self.store.add("2", "b")
        self.assertTrue(self.store.delete(1))
        self.assertFalse(self.store.delete(99))
        self.assertEqual(self.store.add("3", "c").id, 3)

    def test_rejects_bad_input(self):
        for bad in ("abc", "-5", "0", "nan"):
            with self.assertRaises(ValueError):
                parse_amount(bad)
        with self.assertRaises(ValueError):
            self.store.add("5", "   ")


if __name__ == "__main__":
    unittest.main()
