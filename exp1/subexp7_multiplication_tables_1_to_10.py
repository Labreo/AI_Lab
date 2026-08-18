"""Sub-experiment 7: Multiplication Tables 1 to 10"""

def show_table(n):
    print(f"\n--- Table of {n} ---")
    for i in range(1, 11):
        print(f"{n:2d} x {i:2d} = {n * i:3d}")

def show_all():
    print("\n--- Multiplication Tables (1 to 10) ---")
    for i in range(1, 11):
        print(f"Table of {i:2d}: " + "  ".join(f"{i}x{j}={i*j}" for j in range(1, 11)))

def main():
    while True:
        print("\n=== MULTIPLICATION TABLES ===\n1. Specific Table (1-10)\n2. All Tables (1-10)\n0. Exit")
        choice = input("Choice (0-2): ").strip()
        if choice == '0':
            break
        elif choice == '1':
            try:
                n = int(input("Enter table (1-10): "))
                show_table(n) if 1 <= n <= 10 else print("Number out of range (1-10).")
            except ValueError:
                print("Invalid integer!")
        elif choice == '2':
            show_all()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
