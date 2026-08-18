"""Sub-experiment 9: Interactive Menu for List Operations"""

def main():
    items = ["Apple", "Banana", "Cherry"]
    menu = (
        "\n=== LIST OPERATIONS ===\n"
        "1. Append  | 2. Insert  | 3. Remove | 4. Pop\n"
        "5. Merge   | 6. Slice   | 7. Sort   | 8. Reverse\n"
        "9. Reset   | 0. Exit"
    )
    
    while True:
        print(f"{menu}\nCurrent List: {items}")
        choice = input("Choice (0-9): ").strip()
        
        if choice == '0':
            break
        elif choice == '1':
            items.append(input("Item to append: ").strip())
        elif choice == '2':
            try:
                idx = int(input(f"Index (0 to {len(items)}): "))
                items.insert(idx, input("Item to insert: ").strip())
            except ValueError:
                print("Invalid index!")
        elif choice == '3':
            val = input("Item value to remove: ").strip()
            items.remove(val) if val in items else print(f"'{val}' not in list!")
        elif choice == '4':
            if not items:
                print("List is empty!")
                continue
            try:
                print(f"Popped: {items.pop(int(input(f'Index (0 to {len(items)-1}): ')))}")
            except (ValueError, IndexError):
                print("Invalid index!")
        elif choice == '5':
            raw = input("Items to merge (comma-separated): ").strip()
            items += [x.strip() for x in raw.split(',') if x.strip()]
        elif choice == '6':
            try:
                s, e = int(input("Start index: ")), int(input("End index: "))
                print(f"Slice [{s}:{e}]: {items[s:e]}")
            except ValueError:
                print("Invalid slice indices!")
        elif choice == '7':
            items.sort()
        elif choice == '8':
            items.reverse()
        elif choice == '9':
            items = ["Apple", "Banana", "Cherry"]
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
