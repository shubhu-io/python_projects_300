# 🚀 Compound Interest Calculator

## 📝 Description
Calculate compound interest.

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
Project 051: Compound Interest Calculator
Category: Math & Finance
Description: Calculate compound interest.
"""

def run_project_51():
    print("=" * 45)
    print("  PYTHON PROJECT 051: COMPOUND INTEREST CALC")
    print("=" * 45)
    
    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter annual interest rate (e.g. 5 for 5%): "))
        t = float(input("Enter time in years: "))
        n = float(input("Enter number of times interest is compounded per year: "))
        
        amount = p * (1 + (r / 100) / n) ** (n * t)
        interest = amount - p
        
        print(f"\nCompound Interest: ${interest:.2f}")
        print(f"Total Amount: ${amount:.2f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_51()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 051_compound_interest_calculator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Compound Interest Calculator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
