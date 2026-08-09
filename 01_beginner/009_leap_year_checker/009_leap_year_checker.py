"""
Project 009: Leap Year Checker
Category: Math & Logic
Description: Check if a given year is a leap year.
"""

def run_project_9():
    print("=" * 45)
    print("      PYTHON PROJECT 009: LEAP YEAR CHECKER")
    print("=" * 45)
    
    try:
        year = int(input("Enter a year (e.g., 2024): "))
        
        # Leap year logic
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
        if is_leap:
            print(f"\n{year} is a leap year!")
        else:
            print(f"\n{year} is not a leap year.")
            
        return True
    except ValueError:
        print("Invalid input. Please enter a valid integer year.")
        return False

if __name__ == "__main__":
    run_project_9()
