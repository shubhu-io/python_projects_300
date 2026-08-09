# 🚀 Simple Interest Calculator

## 📝 Description
Calculate simple interest.

### 🎯 Category
**Math & Finance**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 050: Simple Interest Calculator
Category: Math & Finance
Description: Calculate simple interest.
"""

def run_project_50():
    print("=" * 45)
    print("    PYTHON PROJECT 050: SIMPLE INTEREST CALC")
    print("=" * 45)
    
    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter annual interest rate (e.g. 5 for 5%): "))
        t = float(input("Enter time in years: "))
        
        interest = (p * r * t) / 100
        total = p + interest
        
        print(f"\nSimple Interest: ${interest:.2f}")
        print(f"Total Amount: ${total:.2f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_50()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 050_simple_interest_calculator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Interest Calculator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
