# 🚀 Simple Tax Calculator

## 📝 Description
Calculate tax based on a flat rate.

### 🎯 Category
**Finance & Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 055: Simple Tax Calculator
Category: Finance & Utilities
Description: Calculate tax based on a flat rate.
"""

def run_project_55():
    print("=" * 45)
    print("      PYTHON PROJECT 055: TAX CALCULATOR")
    print("=" * 45)
    
    try:
        income = float(input("Enter your income: $"))
        tax_rate = float(input("Enter tax rate percentage (e.g., 20 for 20%): "))
        
        tax_amount = income * (tax_rate / 100)
        net_income = income - tax_amount
        
        print(f"\nGross Income: ${income:.2f}")
        print(f"Tax Amount: ${tax_amount:.2f}")
        print(f"Net Income: ${net_income:.2f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_55()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 055_simple_tax_calculator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Tax Calculator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
