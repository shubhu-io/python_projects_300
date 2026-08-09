"""
Project 098: Perfect Number Checker
Category: Math & Logic
Description: Check if a number is a perfect number.
"""

def run_project_98():
    print("=" * 45)
    print("     PYTHON PROJECT 098: PERFECT NUMBER")
    print("=" * 45)
    
    try:
        num = int(input("Enter an integer: "))
        
        if num <= 0:
            print("Number must be a positive integer.")
            return False
            
        divisors = [i for i in range(1, num) if num % i == 0]
        div_sum = sum(divisors)
        
        print(f"\nDivisors: {divisors}")
        print(f"Sum of divisors: {div_sum}")
        
        if div_sum == num:
            print(f"\n{num} IS a Perfect Number!")
        else:
            print(f"\n{num} is NOT a Perfect Number.")
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_98()
