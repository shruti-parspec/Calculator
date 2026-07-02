"""A simple command-line calculator with basic arithmetic operations.

Provides functions for addition, subtraction, multiplication, division, power,
and modulus, with an interactive menu-driven interface.
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus by zero.")
    return a % b


def display_menu():
    print("\n=== Python Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulus (%)")
    print("7. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def main():
    while True:
        display_menu()

        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Please select 1-7.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(num1, num2)
                op = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                op = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                op = "*"
            elif choice == "4":
                result = divide(num1, num2)
                op = "/"
            elif choice == "5":
                result = power(num1, num2)
                op = "**"
            elif choice == "6":
                result = modulus(num1, num2)
                op = "%"

            print(f"\nResult: {num1} {op} {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()