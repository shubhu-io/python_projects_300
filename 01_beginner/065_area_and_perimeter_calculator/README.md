# 🚀 Area and Perimeter Calculator

## 📝 Description
Calculate area and perimeter for rectangle, circle, etc.

### 🎯 Category
**Math & Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 065: Area and Perimeter Calculator
Category: Math & Utilities
Description: Calculate area and perimeter for rectangle, circle, etc.
"""
import math

def run_project_65():
    print("=" * 45)
    print("   PYTHON PROJECT 065: AREA & PERIMETER CALC")
    print("=" * 45)
    
    print("1. Rectangle")
    print("2. Circle")
    choice = input("Select a shape (1/2): ").strip()
    
    try:
        if choice == '1':
            w = float(input("Width: "))
            h = float(input("Height: "))
            print(f"Area: {w*h:.2f}")
            print(f"Perimeter: {2*(w+h):.2f}")
        elif choice == '2':
            r = float(input("Radius: "))
            print(f"Area: {math.pi * r**2:.2f}")
            print(f"Circumference (Perimeter): {2 * math.pi * r:.2f}")
        else:
            print("Invalid choice.")
            return False
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_65()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 065_area_and_perimeter_calculator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Area and Perimeter Calculator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
