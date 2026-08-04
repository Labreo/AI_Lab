"""
Sub-experiment 6: Multiplication Table of a Specific Number
"""

def print_table(n, limit=10):
    print(f"\n--- Multiplication Table of {n} ---")
    for i in range(1, limit + 1):
        print(f"{n} x {i:2d} = {n * i}")

def main():
    try:
        num = int(input("Enter a number to generate its multiplication table: "))
        print_table(num)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
