"""
Project 055: Simple Tax Calculator
Category: Finance & Utilities
Description: Calculate tax based on a flat rate.
"""

def run_project_55():
    print("=" * 45)
    print("      PYTHON PROJECT 055: TAX CALCULATOR")
    print("=" * 45)
    
    try:
        income = float(input("Enter your income: $"))
        tax_rate = float(input("Enter tax rate percentage (e.g., 20 for 20%): "))
        
        tax_amount = income * (tax_rate / 100)
        net_income = income - tax_amount
        
        print(f"\nGross Income: ${income:.2f}")
        print(f"Tax Amount: ${tax_amount:.2f}")
        print(f"Net Income: ${net_income:.2f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_55()
