"""
Sub-experiment 2: Menu Driven Calculator
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a % b

def exponent(a, b):
    return a ** b

def main():
    while True:
        print("\n=============================")
        print("    MENU DRIVEN CALCULATOR   ")
        print("=============================")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (**)")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()
        if choice == '7':
            print("Exiting Calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid Choice! Please select between 1 and 7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '6':
            print(f"Result: {num1} ** {num2} = {exponent(num1, num2)}")

if __name__ == "__main__":
    main()
