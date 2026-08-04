"""
Sub-experiment 5: Print Numbers 1 to 10 (Interactive Menu)
"""

def print_using_for_loop():
    print("\n--- Numbers 1 to 10 using FOR loop ---")
    for i in range(1, 11):
        print(i, end=" ")
    print()

def print_using_while_loop():
    print("\n--- Numbers 1 to 10 using WHILE loop ---")
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1
    print()

def print_custom_range():
    try:
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
        print(f"\n--- Numbers {start} to {end} ---")
        step = 1 if start <= end else -1
        for i in range(start, end + step, step):
            print(i, end=" ")
        print()
    except ValueError:
        print("Invalid input! Please enter integer values.")

def main():
    while True:
        print("\n=============================================")
        print("    SUB-EXPERIMENT 5: PRINT NUMBERS MENU     ")
        print("=============================================")
        print("1. Print 1 to 10 using FOR loop")
        print("2. Print 1 to 10 using WHILE loop")
        print("3. Print Custom Range (User Defined)")
        print("0. Exit to Main Menu")
        print("=============================================")
        
        choice = input("Enter choice (0-3): ").strip()
        
        if choice == '0':
            print("Exiting Sub-experiment 5.")
            break
        elif choice == '1':
            print_using_for_loop()
        elif choice == '2':
            print_using_while_loop()
        elif choice == '3':
            print_custom_range()
        else:
            print("Invalid choice! Select between 0 and 3.")

if __name__ == "__main__":
    main()
