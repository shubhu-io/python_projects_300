# 🚀 Simple Grade Calculator

## 📝 Description
Calculate average grade and letter grade from a list.

### 🎯 Category
**Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Comprehensions
- User Input
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 044: Simple Grade Calculator
Category: Utilities
Description: Calculate average grade and letter grade from a list.
"""

def run_project_44():
    print("=" * 45)
    print("     PYTHON PROJECT 044: GRADE CALCULATOR")
    print("=" * 45)
    
    try:
        grades_str = input("Enter grades separated by spaces: ").strip()
        if not grades_str:
            return False
            
        grades = [float(g) for g in grades_str.split()]
        avg = sum(grades) / len(grades)
        
        if avg >= 90:
            letter = 'A'
        elif avg >= 80:
            letter = 'B'
        elif avg >= 70:
            letter = 'C'
        elif avg >= 60:
            letter = 'D'
        else:
            letter = 'F'
            
        print(f"\nAverage: {avg:.2f}")
        print(f"Letter Grade: {letter}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_44()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 044_simple_grade_calculator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Grade Calculator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
