"""
Simple Calculator
A beginner-friendly command-line calculator for basic arithmetic.
"""

def calculate(first_number: float, operator: str, second_number: float) -> float:
    """Perform a basic arithmetic operation."""
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    else:
        raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main() -> None:
    print("=== Simple Python Calculator ===")
    print("Supported operations: +  -  *  /")
    print("Type 'q' at the operator prompt to quit.\n")

    while True:
        try:
            first_input = input("Enter the first number: ").strip()
            first_number = float(first_input)

            operator = input("Enter an operator (+, -, *, /) or q to quit: ").strip()
            if operator.lower() == "q":
                print("Goodbye!")
                break

            second_number = float(input("Enter the second number: ").strip())
            result = calculate(first_number, operator, second_number)
            print(f"Result: {result:g}\n")

        except ValueError as error:
            print(f"Input error: {error}\n")
        except ZeroDivisionError as error:
            print(f"Calculation error: {error}\n")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
