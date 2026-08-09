# 🚀 Simple CLI Calculator

## 📝 Description
Basic arithmetic operations (+, -, *, /).

### 🎯 Category
**Math & Logic**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
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
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        
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
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 002_simple_cli_calculator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple CLI Calculator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
