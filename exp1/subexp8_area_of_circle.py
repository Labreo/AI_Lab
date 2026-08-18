"""Sub-experiment 8: Area of Circle Function"""
import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2) if radius >= 0 else None

def main():
    try:
        r = float(input("Enter circle radius: "))
        area = calculate_circle_area(r)
        print(f"Area: {area:.4f} sq units" if area is not None else "Error: Radius cannot be negative.")
    except ValueError:
        print("Invalid numeric input!")

if __name__ == "__main__":
    main()
