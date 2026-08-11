"""
Project 002: Simple CLI Calculator
Category: Math & Logic
Description: Basic arithmetic operations (+, -, *, /).
"""

def run_project_2():
    print("=" * 45)
    print("       PYTHON PROJECT 002: CLI CALCULATOR")
    print("=" * 45)
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return False
            result = num1 / num2
        else:
            print("Invalid operator!")
            return False
            
        print(f"\nResult: {num1} {op} {num2} = {result}")
        return True
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return False

if __name__ == "__main__":
    run_project_2()
