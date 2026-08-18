"""Sub-experiment 5: Print Numbers (Loops & Range)"""

def main():
    while True:
        print("\n=== PRINT NUMBERS ===\n1. For Loop (1-10)\n2. While Loop (1-10)\n3. Custom Range\n0. Exit")
        choice = input("Choice (0-3): ").strip()
        if choice == '0':
            break
        elif choice == '1':
            print("For Loop:", *(i for i in range(1, 11)))
        elif choice == '2':
            i, res = 1, []
            while i <= 10:
                res.append(str(i))
                i += 1
            print("While Loop:", " ".join(res))
        elif choice == '3':
            try:
                s, e = int(input("Start: ")), int(input("End: "))
                step = 1 if s <= e else -1
                print(f"Range {s} to {e}:", *range(s, e + step, step))
            except ValueError:
                print("Invalid integers!")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
