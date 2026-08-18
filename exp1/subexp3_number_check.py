"""Sub-experiment 3: Positive, Negative, or Zero Check"""

def check_number(num):
    return "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")

def main():
    try:
        val = float(input("Enter a number: "))
        print(f"The number {val} is {check_number(val)}.")
    except ValueError:
        print("Invalid numeric input!")

if __name__ == "__main__":
    main()
