"""
Project 050: Simple Interest Calculator
Category: Math & Finance
Description: Calculate simple interest.
"""

def run_project_50():
    print("=" * 45)
    print("    PYTHON PROJECT 050: SIMPLE INTEREST CALC")
    print("=" * 45)
    
    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter annual interest rate (e.g. 5 for 5%): "))
        t = float(input("Enter time in years: "))
        
        interest = (p * r * t) / 100
        total = p + interest
        
        print(f"\nSimple Interest: ${interest:.2f}")
        print(f"Total Amount: ${total:.2f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_50()
