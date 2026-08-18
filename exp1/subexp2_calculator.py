"""Sub-experiment 2: Menu Driven Calculator"""
import operator

OPS = {
    '1': ('Addition (+)', operator.add),
    '2': ('Subtraction (-)', operator.sub),
    '3': ('Multiplication (*)', operator.mul),
    '4': ('Division (/)', lambda a, b: a / b if b != 0 else "Error: Division by zero"),
    '5': ('Modulus (%)', lambda a, b: a % b if b != 0 else "Error: Division by zero"),
    '6': ('Exponentiation (**)', operator.pow),
}

def main():
    while True:
        print("\n=== CALCULATOR ===")
        for k, (name, _) in OPS.items():
            print(f"{k}. {name}")
        print("7. Exit")

        choice = input("Choice (1-7): ").strip()
        if choice == '7':
            break
        if choice not in OPS:
            print("Invalid Choice!")
            continue

        try:
            a, b = float(input("First number: ")), float(input("Second number: "))
            _, fn = OPS[choice]
            print(f"Result: {fn(a, b)}")
        except ValueError:
            print("Invalid numeric input!")

if __name__ == "__main__":
    main()
