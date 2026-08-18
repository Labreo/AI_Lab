"""Sub-experiment 4: Find Largest of Three Numbers"""

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    try:
        nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
        print(f"The largest number is: {find_largest(*nums)}")
    except ValueError:
        print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    main()
