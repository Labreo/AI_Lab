"""
Sub-experiment 7: Multiplication Tables 1 to 10 (Interactive Menu)
"""

def show_table(n):
    print(f"\n--- Multiplication Table of {n} ---")
    for i in range(1, 11):
        print(f"{n:2d} x {i:2d} = {n * i:3d}")

def show_all_tables():
    print("\n=======================================================")
    print("            ALL MULTIPLICATION TABLES (1 TO 10)         ")
    print("=======================================================")
    for i in range(1, 11):
        print(f"\nTable of {i}:")
        row = [f"{i}x{j}={i*j}" for j in range(1, 11)]
        print("  ".join(row[:5]))
        print("  ".join(row[5:]))

def main():
    while True:
        print("\n=============================================")
        print(" SUB-EXP 7: MULTIPLICATION TABLES (1 to 10)  ")
        print("=============================================")
        print("1. View Specific Table (Pick 1 to 10)")
        print("2. View All Tables from 1 to 10")
        print("0. Exit to Main Menu")
        print("=============================================")
        
        choice = input("Enter choice (0-2): ").strip()
        
        if choice == '0':
            print("Exiting Sub-experiment 7.")
            break
        elif choice == '1':
            try:
                n = int(input("Enter table number (1-10): "))
                if 1 <= n <= 10:
                    show_table(n)
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid integer input!")
        elif choice == '2':
            show_all_tables()
        else:
            print("Invalid choice! Select 0, 1, or 2.")

if __name__ == "__main__":
    main()
