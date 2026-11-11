from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation

CENT = Decimal("0.01")


@dataclass(frozen=True)
class Expense:
    id: int
    date: date
    category: str
    amount: Decimal
    note: str = ""


def parse_amount(value) -> Decimal:
    """Convert user input to a positive Decimal rounded to 2 places."""
    try:
        amount = Decimal(str(value).strip())
    except InvalidOperation:
        raise ValueError(f"Invalid amount: {value!r}") from None
    if not amount.is_finite() or amount <= 0:
        raise ValueError("Amount must be a positive number")
    return amount.quantize(CENT)


def parse_date(value) -> date:
    """Parse YYYY-MM-DD into a date."""
    try:
        return date.fromisoformat(str(value).strip())
    except ValueError:
        raise ValueError(f"Invalid date: {value!r} (use YYYY-MM-DD)") from None
