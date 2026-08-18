"""Sub-experiment 1: Python Variables and Data Types"""

DATA_TYPES = [
    ("Integer (int)", 42, "val + 10 = 52"),
    ("Float (float)", 98.6, "val / 2 = 49.3"),
    ("String (str)", "Hello, Python!", "Upper: 'HELLO, PYTHON!'"),
    ("Boolean (bool)", True, "not val = False"),
    ("List (list)", [10, "apple", 3.14], "val[0] = 10"),
    ("Tuple (tuple)", (10, 20, 30), "val[1] = 20"),
    ("Dictionary (dict)", {"name": "Alice", "age": 21}, "val['name'] = 'Alice'"),
    ("Set (set)", {1, 2, 3}, "Unique elements"),
    ("NoneType", None, "Absence of value"),
]

def show(name, val, extra=""):
    print(f"\n--- {name} ---\nExample: {val} | Type: {type(val).__name__}" + (f" | {extra}" if extra else ""))

def main():
    while True:
        print("\n=== DATA TYPES ===")
        for i, (name, *_) in enumerate(DATA_TYPES, 1):
            print(f"{i}. {name}")
        print("10. Show All\n0. Exit")
        
        choice = input("Choice (0-10): ").strip()
        if choice == '0':
            break
        elif choice == '10':
            for name, val, extra in DATA_TYPES:
                show(name, val, extra)
        elif choice.isdigit() and 1 <= int(choice) <= len(DATA_TYPES):
            name, val, extra = DATA_TYPES[int(choice) - 1]
            show(name, val, extra)
        else:
            print("Invalid choice! Select between 0 and 10.")

if __name__ == "__main__":
    main()
