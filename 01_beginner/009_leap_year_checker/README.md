# 🚀 Leap Year Checker

## 📝 Description
Check if a given year is a leap year.

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
Project 009: Leap Year Checker
Category: Math & Logic
Description: Check if a given year is a leap year.
"""

def run_project_9():
    print("=" * 45)
    print("      PYTHON PROJECT 009: LEAP YEAR CHECKER")
    print("=" * 45)
    
    try:
        year = int(input("Enter a year (e.g., 2024): "))
        
        # Leap year logic
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
        if is_leap:
            print(f"\n{year} is a leap year!")
        else:
            print(f"\n{year} is not a leap year.")
            
        return True
    except ValueError:
        print("Invalid input. Please enter a valid integer year.")
        return False

if __name__ == "__main__":
    run_project_9()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 009_leap_year_checker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Leap Year Checker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
