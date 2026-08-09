"""
Project 025: Armstrong Number Checker
Category: Math & Logic
Description: Check if a number is an Armstrong number.
"""

def run_project_25():
    print("=" * 45)
    print("    PYTHON PROJECT 025: ARMSTRONG NUMBER")
    print("=" * 45)
    
    try:
        num_str = input("Enter an integer: ").strip()
        num = int(num_str)
        
        power = len(num_str)
        arm_sum = sum(int(digit) ** power for digit in num_str)
        
        if arm_sum == num:
            print(f"\n{num} IS an Armstrong number!")
        else:
            print(f"\n{num} is NOT an Armstrong number.")
            
        return True
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False

if __name__ == "__main__":
    run_project_25()
