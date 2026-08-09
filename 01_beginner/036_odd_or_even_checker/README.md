# 🚀 Odd or Even Checker

## 📝 Description
Check if a number is odd or even.

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
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 036_odd_or_even_checker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Odd or Even Checker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
