# 🚀 Number Swap Utility

## 📝 Description
Swap two numbers without using a third variable.

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
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 094_number_swap_utility.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Number Swap Utility in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
