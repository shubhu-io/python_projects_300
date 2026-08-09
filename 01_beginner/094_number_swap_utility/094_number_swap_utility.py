"""
Project 094: Number Swap Utility
Category: Math & Logic
Description: Swap two numbers without using a third variable.
"""

def run_project_94():
    print("=" * 45)
    print("       PYTHON PROJECT 094: NUMBER SWAP")
    print("=" * 45)
    
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        
        print(f"\nBefore Swap: a = {a}, b = {b}")
        
        # Swapping in Python is easy, but doing it mathematically:
        a = a + b
        b = a - b
        a = a - b
        
        print(f"After Swap:  a = {a}, b = {b}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_94()
