# 🚀 Armstrong Number Checker

## 📝 Description
Check if a number is an Armstrong number.

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
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 025_armstrong_number_checker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Armstrong Number Checker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
