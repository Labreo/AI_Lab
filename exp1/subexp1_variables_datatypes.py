"""
Sub-experiment 1: Interactive Menu for Python Variables and Data Types
"""

def show_integer():
    print("\n--- 1. Integer (int) ---")
    print("Integers are whole numbers without a fractional component.")
    val = 42
    print(f"Example: val = {val}")
    print(f"Type: {type(val)}")
    print(f"Operations: val + 10 = {val + 10}")

def show_float():
    print("\n--- 2. Float (float) ---")
    print("Floats represent real numbers with fractional components/decimals.")
    val = 98.6
    print(f"Example: val = {val}")
    print(f"Type: {type(val)}")
    print(f"Operations: val / 2 = {val / 2}")

def show_string():
    print("\n--- 3. String (str) ---")
    print("Strings are sequences of characters enclosed in quotes.")
    val = "Hello, Python!"
    print(f"Example: val = '{val}'")
    print(f"Type: {type(val)}")
    print(f"Length: {len(val)}, Upper: {val.upper()}")

def show_boolean():
    print("\n--- 4. Boolean (bool) ---")
    print("Booleans represent truth values: True or False.")
    val = True
    print(f"Example: val = {val}")
    print(f"Type: {type(val)}")
    print(f"Logical NOT: not val = {not val}")

def show_list():
    print("\n--- 5. List (list) ---")
    print("Lists are ordered, mutable (changeable) collections of items.")
    val = [10, "apple", 3.14, True]
    print(f"Example: val = {val}")
    print(f"Type: {type(val)}")
    print(f"First element: {val[0]}, Appended: val + ['new']")

def show_tuple():
    print("\n--- 6. Tuple (tuple) ---")
    print("Tuples are ordered, immutable (unchangeable) collections.")
    val = (10, 20, 30)
    print(f"Example: val = {val}")
    print(f"Type: {type(val)}")
    print(f"Element access: val[1] = {val[1]}")

def show_dictionary():
    print("\n--- 7. Dictionary (dict) ---")
    print("Dictionaries store key-value pairs.")
    val = {"name": "Alice", "role": "Student", "age": 21}
    print(f"Example: val = {val}")
    print(f"Type: {type(val)}")
    print(f"Value for 'name': {val['name']}")

def show_set():
    print("\n--- 8. Set (set) ---")
    print("Sets are unordered collections of unique elements (no duplicates).")
    val = {1, 2, 2, 3, 4, 4}
    print(f"Example: {1, 2, 2, 3, 4, 4} -> set = {val}")
    print(f"Type: {type(val)}")

def show_none():
    print("\n--- 9. NoneType ---")
    print("NoneType represents the absence of a value or null state.")
    val = None
    print(f"Example: val = {val}")
    print(f"Type: {type(val)}")

def show_all():
    show_integer()
    show_float()
    show_string()
    show_boolean()
    show_list()
    show_tuple()
    show_dictionary()
    show_set()
    show_none()

def main():
    while True:
        print("\n=============================================")
        print("  SUB-EXPERIMENT 1: VARIABLES & DATA TYPES   ")
        print("=============================================")
        print("1. Integer (int)")
        print("2. Float (float)")
        print("3. String (str)")
        print("4. Boolean (bool)")
        print("5. List (list)")
        print("6. Tuple (tuple)")
        print("7. Dictionary (dict)")
        print("8. Set (set)")
        print("9. NoneType")
        print("10. Show All Data Types")
        print("0. Exit to Main Menu")
        print("=============================================")
        
        choice = input("Enter choice (0-10): ").strip()
        
        if choice == '0':
            print("Exiting Sub-experiment 1.")
            break
        elif choice == '1':
            show_integer()
        elif choice == '2':
            show_float()
        elif choice == '3':
            show_string()
        elif choice == '4':
            show_boolean()
        elif choice == '5':
            show_list()
        elif choice == '6':
            show_tuple()
        elif choice == '7':
            show_dictionary()
        elif choice == '8':
            show_set()
        elif choice == '9':
            show_none()
        elif choice == '10':
            show_all()
        else:
            print("Invalid choice! Please select between 0 and 10.")

if __name__ == "__main__":
    main()
