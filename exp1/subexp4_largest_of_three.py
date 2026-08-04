"""
Sub-experiment 4: Find Largest of Three Numbers
"""

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        n3 = float(input("Enter third number: "))

        largest = find_largest(n1, n2, n3)
        print(f"The largest of {n1}, {n2}, and {n3} is: {largest}")
    except ValueError:
        print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    main()
