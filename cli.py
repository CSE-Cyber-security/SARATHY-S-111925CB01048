import argparse
import os
import sys

from . import __version__
from .models import parse_date
from .reports import by_category, by_month, filter_expenses, total
from .storage import ExpenseStore

DEFAULT_FILE = os.environ.get("EXPENSE_FILE", os.path.join("data", "expenses.csv"))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="expense-tracker", description="Track your daily expenses."
    )
    p.add_argument("--version", action="version", version=__version__)
    p.add_argument(
        "--file", default=DEFAULT_FILE, help=f"CSV data file (default: {DEFAULT_FILE})"
    )
    sub = p.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="add an expense")
    add.add_argument("amount")
    add.add_argument("category")
    add.add_argument("-n", "--note", default="")
    add.add_argument("-d", "--date", help="YYYY-MM-DD (default: today)")

    ls = sub.add_parser("list", help="list expenses")
    ls.add_argument("-m", "--month", help="filter by month, YYYY-MM")
    ls.add_argument("-c", "--category", help="filter by category")

    rm = sub.add_parser("delete", help="delete an expense by id")
    rm.add_argument("id", type=int)

    sm = sub.add_parser("summary", help="totals by category and month")
    sm.add_argument("-m", "--month", help="limit to one month, YYYY-MM")

    return p


def print_table(expenses) -> None:
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':>4}  {'Date':<10}  {'Category':<14}  {'Amount':>10}  Note")
    for e in expenses:
        print(
            f"{e.id:>4}  {e.date.isoformat():<10}  {e.category:<14}  "
            f"{e.amount:>10.2f}  {e.note}"
        )
    print(f"{'':>4}  {'':<10}  {'TOTAL':<14}  {total(expenses):>10.2f}")


def run(args: argparse.Namespace) -> int:
    store = ExpenseStore(args.file)

    if args.command == "add":
        on = parse_date(args.date) if args.date else None
        e = store.add(args.amount, args.category, on=on, note=args.note)
        print(f"Added #{e.id}: {e.amount:.2f} on {e.category} ({e.date.isoformat()})")
    elif args.command == "list":
        print_table(filter_expenses(store.load(), args.month, args.category))
    elif args.command == "delete":
        if store.delete(args.id):
            print(f"Deleted #{args.id}")
        else:
            print(f"No expense with id {args.id}", file=sys.stderr)
            return 1
    elif args.command == "summary":
        expenses = filter_expenses(store.load(), month=args.month)
        if not expenses:
            print("No expenses found.")
            return 0
        print("By category")
        for cat, amt in by_category(expenses).items():
            print(f"  {cat:<14} {amt:>10.2f}")
        if not args.month:
            print("By month")
            for month, amt in by_month(expenses).items():
                print(f"  {month:<14} {amt:>10.2f}")
        print(f"Total: {total(expenses):.2f}")
    return 0


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return run(args)
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 2
