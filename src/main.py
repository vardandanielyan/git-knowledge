import sys
from src.calculator import *

def print_banner():
    print("=" * 45)
    print(f"  {APP_NAME} (v{APP_VERSION})")
    print("  Git Training Sample Project")
    print("=" * 45)


def show_menu():
    print("Stat")
    print("Stat")


def main():
    print_banner()
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye! Happy Git coding!")
            sys.exit(0)

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid selection. Please choose 1-5.")
            continue

        try:
            N1 = float(input("Enter first number: "))
            N2 = float(input("Enter second number: "))

            if choice == "1":
                res = add(N1, N2)
                print(f"Result: {N1} + {N2} = {res}")
            elif choice == "2":
                res = subtract(N1, N2)
                print(f"Result: {N1} - {N2} = {res}")
            elif choice == "3":
                res = multiply(N1, N2)
                print(f"Result: {N1} * {N2} = {res}")
            elif choice == "4":
                res = divide(N1, N2)
                print(f"Result: {N1} / {N2} = {res}")
        except ValueError as err:
            print(f"Error: {err}")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)


if __name__ == "__main__":
    main()
