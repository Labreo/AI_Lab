"""
Sub-experiment 9: Interactive Menu for List Operations
"""

def main():
    fruits = ["Apple", "Banana", "Cherry"]
    
    while True:
        print("\n=============================================")
        print("     SUB-EXPERIMENT 9: LIST OPERATIONS       ")
        print("=============================================")
        print(f"Current List: {fruits}")
        print("---------------------------------------------")
        print("1. Append an element (append)")
        print("2. Insert an element at index (insert)")
        print("3. Remove an element by value (remove)")
        print("4. Pop an element by index (pop)")
        print("5. Merge with another list (+ / extend)")
        print("6. Slice the list")
        print("7. Sort the list")
        print("8. Reverse the list")
        print("9. Reset list to default")
        print("0. Exit to Main Menu")
        print("=============================================")
        
        choice = input("Enter choice (0-9): ").strip()
        
        if choice == '0':
            print("Exiting List Operations.")
            break
        elif choice == '1':
            item = input("Enter element to append: ").strip()
            fruits.append(item)
            print(f"Updated List: {fruits}")
        elif choice == '2':
            try:
                idx = int(input(f"Enter index (0 to {len(fruits)}): "))
                item = input("Enter element to insert: ").strip()
                fruits.insert(idx, item)
                print(f"Updated List: {fruits}")
            except ValueError:
                print("Invalid index format!")
        elif choice == '3':
            item = input("Enter element value to remove: ").strip()
            if item in fruits:
                fruits.remove(item)
                print(f"Updated List: {fruits}")
            else:
                print(f"'{item}' not found in list!")
        elif choice == '4':
            if not fruits:
                print("List is empty!")
                continue
            try:
                idx = int(input(f"Enter index to pop (0 to {len(fruits)-1}): "))
                popped = fruits.pop(idx)
                print(f"Popped '{popped}'. Updated List: {fruits}")
            except (ValueError, IndexError):
                print("Invalid index!")
        elif choice == '5':
            new_items = input("Enter items to merge (comma-separated, e.g. Mango, Orange): ").strip()
            if new_items:
                second_list = [x.strip() for x in new_items.split(',')]
                fruits = fruits + second_list
                print(f"Merged List: {fruits}")
        elif choice == '6':
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(f"Sliced List [{start}:{end}]: {fruits[start:end]}")
            except ValueError:
                print("Invalid indices!")
        elif choice == '7':
            fruits.sort()
            print(f"Sorted List: {fruits}")
        elif choice == '8':
            fruits.reverse()
            print(f"Reversed List: {fruits}")
        elif choice == '9':
            fruits = ["Apple", "Banana", "Cherry"]
            print(f"List reset to: {fruits}")
        else:
            print("Invalid choice! Please select between 0 and 9.")

if __name__ == "__main__":
    main()
