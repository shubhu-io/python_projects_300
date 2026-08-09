"""
Project 068: Simple Age Calculator
Category: Utilities
Description: Calculate age given a birth year.
"""
import datetime

def run_project_68():
    print("=" * 45)
    print("      PYTHON PROJECT 068: SIMPLE AGE CALC")
    print("=" * 45)
    
    try:
        birth_year = int(input("Enter your birth year (e.g. 1990): "))
        current_year = datetime.datetime.now().year
        
        if birth_year > current_year:
            print("You cannot be born in the future!")
            return False
            
        age = current_year - birth_year
        print(f"\nYou turn {age} years old in {current_year}.")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_68()
