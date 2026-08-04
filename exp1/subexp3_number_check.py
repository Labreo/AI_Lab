"""
Sub-experiment 3: Positive, Negative, or Zero Check
"""

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    try:
        val = float(input("Enter a number: "))
        result = check_number(val)
        print(f"The number {val} is {result}.")
    except ValueError:
        print("Invalid input! Please enter a valid numerical value.")

if __name__ == "__main__":
    main()
