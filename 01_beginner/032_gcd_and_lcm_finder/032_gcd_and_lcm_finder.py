"""
Project 032: GCD and LCM Finder
Category: Math & Logic
Description: Find the Greatest Common Divisor and Least Common Multiple.
"""
import math

def run_project_32():
    print("=" * 45)
    print("      PYTHON PROJECT 032: GCD & LCM FINDER")
    print("=" * 45)
    
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if num1 == 0 or num2 == 0:
            print("Numbers must be non-zero.")
            return False
            
        gcd = math.gcd(num1, num2)
        lcm = abs(num1 * num2) // gcd
        
        print(f"\nFor numbers {num1} and {num2}:")
        print(f"GCD (Greatest Common Divisor): {gcd}")
        print(f"LCM (Least Common Multiple): {lcm}")
        return True
    except ValueError:
        print("Invalid input. Please enter integers.")
        return False

if __name__ == "__main__":
    run_project_32()
