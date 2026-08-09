# 🚀 Bill and Tip Calculator

## 📝 Description
Calculate tip amount and total bill per person.

### 🎯 Category
**Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 028: Bill and Tip Calculator
Category: Utilities
Description: Calculate tip amount and total bill per person.
"""

def run_project_28():
    print("=" * 45)
    print("    PYTHON PROJECT 028: BILL & TIP CALCULATOR")
    print("=" * 45)
    
    try:
        bill = float(input("Enter the total bill amount: $"))
        tip_pct = float(input("Enter tip percentage (e.g., 15): "))
        people = int(input("How many people are splitting the bill? "))
        
        if people <= 0:
            print("Number of people must be at least 1.")
            return False
            
        tip_amount = bill * (tip_pct / 100)
        total = bill + tip_amount
        per_person = total / people
        
        print(f"\nTotal Tip: ${tip_amount:.2f}")
        print(f"Total Bill: ${total:.2f}")
        print(f"Amount per person: ${per_person:.2f}")
        
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_28()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 028_bill_and_tip_calculator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Bill and Tip Calculator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
