"""
Project 047: Weight Unit Converter
Category: Utilities
Description: Convert between kilograms, pounds, and ounces.
"""

def run_project_47():
    print("=" * 45)
    print("     PYTHON PROJECT 047: WEIGHT CONVERTER")
    print("=" * 45)
    
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    
    choice = input("Select an option (1/2): ").strip()
    
    try:
        val = float(input("Enter weight: "))
        
        if choice == '1':
            res = val * 2.20462
            print(f"{val} kg = {res:.2f} lbs")
        elif choice == '2':
            res = val / 2.20462
            print(f"{val} lbs = {res:.2f} kg")
        else:
            print("Invalid choice.")
            return False
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_47()
