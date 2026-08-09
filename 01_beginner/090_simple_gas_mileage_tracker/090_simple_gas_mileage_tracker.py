"""
Project 090: Simple Gas Mileage Tracker
Category: Math & Utilities
Description: Calculate Miles Per Gallon (MPG).
"""

def run_project_90():
    print("=" * 45)
    print("      PYTHON PROJECT 090: GAS MILEAGE TRACKER")
    print("=" * 45)
    
    try:
        miles = float(input("Enter miles driven: "))
        gallons = float(input("Enter gallons of gas used: "))
        
        if gallons <= 0:
            print("Gallons must be greater than 0.")
            return False
            
        mpg = miles / gallons
        
        print(f"\nYour car's gas mileage is: {mpg:.2f} MPG")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_90()
