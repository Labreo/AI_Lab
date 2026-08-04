"""
Sub-experiment 8: Area of Circle Function
"""

import math

def calculate_circle_area(radius):
    """Calculates and returns the area of a circle given its radius."""
    if radius < 0:
        return None
    return math.pi * (radius ** 2)

def main():
    print("--- Area of Circle Calculator ---")
    try:
        r = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(r)
        if area is None:
            print("Error: Radius cannot be negative.")
        else:
            print(f"Radius: {r}")
            print(f"Calculated Area: {area:.4f} sq units")
    except ValueError:
        print("Invalid input! Please enter a numeric radius.")

if __name__ == "__main__":
    main()
