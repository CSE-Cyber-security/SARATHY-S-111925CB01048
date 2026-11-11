from collections import defaultdict
from decimal import Decimal

from .models import Expense


def filter_expenses(
    expenses: list[Expense], month: str | None = None, category: str | None = None
) -> list[Expense]:
    """Filter by month (YYYY-MM) and/or category."""
    result = expenses
    if month:
        result = [e for e in result if e.date.strftime("%Y-%m") == month]
    if category:
        result = [e for e in result if e.category == category.strip().lower()]
    return sorted(result, key=lambda e: (e.date, e.id))


def total(expenses: list[Expense]) -> Decimal:
    return sum((e.amount for e in expenses), Decimal("0.00"))


def by_category(expenses: list[Expense]) -> dict[str, Decimal]:
    """Totals per category, largest first."""
    sums: dict[str, Decimal] = defaultdict(lambda: Decimal("0.00"))
    for e in expenses:
        sums[e.category] += e.amount
    return dict(sorted(sums.items(), key=lambda kv: kv[1], reverse=True))


def by_month(expenses: list[Expense]) -> dict[str, Decimal]:
    """Totals per month (YYYY-MM), oldest first."""
    sums: dict[str, Decimal] = defaultdict(lambda: Decimal("0.00"))
    for e in expenses:
        sums[e.date.strftime("%Y-%m")] += e.amount
    return dict(sorted(sums.items()))
