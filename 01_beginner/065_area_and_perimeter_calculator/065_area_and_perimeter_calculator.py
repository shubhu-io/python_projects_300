"""
Project 065: Area and Perimeter Calculator
Category: Math & Utilities
Description: Calculate area and perimeter for rectangle, circle, etc.
"""
import math

def run_project_65():
    print("=" * 45)
    print("   PYTHON PROJECT 065: AREA & PERIMETER CALC")
    print("=" * 45)
    
    print("1. Rectangle")
    print("2. Circle")
    choice = input("Select a shape (1/2): ").strip()
    
    try:
        if choice == '1':
            w = float(input("Width: "))
            h = float(input("Height: "))
            print(f"Area: {w*h:.2f}")
            print(f"Perimeter: {2*(w+h):.2f}")
        elif choice == '2':
            r = float(input("Radius: "))
            print(f"Area: {math.pi * r**2:.2f}")
            print(f"Circumference (Perimeter): {2 * math.pi * r:.2f}")
        else:
            print("Invalid choice.")
            return False
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_65()
