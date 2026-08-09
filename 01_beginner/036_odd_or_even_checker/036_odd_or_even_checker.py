"""
Project 036: Odd or Even Checker
Category: Math & Logic
Description: Check if a number is odd or even.
"""

def run_project_36():
    print("=" * 45)
    print("     PYTHON PROJECT 036: ODD OR EVEN CHECKER")
    print("=" * 45)
    
    try:
        num = int(input("Enter an integer: "))
        
        if num % 2 == 0:
            print(f"\n{num} is EVEN.")
        else:
            print(f"\n{num} is ODD.")
            
        return True
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False

if __name__ == "__main__":
    run_project_36()
