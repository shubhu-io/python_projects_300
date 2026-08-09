"""
Project 031: Factorial Calculator
Category: Math & Logic
Description: Calculate the factorial of a given number.
"""

def run_project_31():
    print("=" * 45)
    print("    PYTHON PROJECT 031: FACTORIAL CALCULATOR")
    print("=" * 45)
    
    try:
        num = int(input("Enter a non-negative integer: "))
        
        if num < 0:
            print("Factorial is not defined for negative numbers.")
            return False
            
        result = 1
        for i in range(1, num + 1):
            result *= i
            
        print(f"\n{num}! = {result}")
        return True
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False

if __name__ == "__main__":
    run_project_31()
