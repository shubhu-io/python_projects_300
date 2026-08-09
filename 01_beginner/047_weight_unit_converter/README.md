# 🚀 Weight Unit Converter

## 📝 Description
Convert between kilograms, pounds, and ounces.

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
Project 047: Weight Unit Converter
Category: Utilities
Description: Convert between kilograms, pounds, and ounces.
"""

def run_project_47():
    print("=" * 45)
    print("     PYTHON PROJECT 047: WEIGHT CONVERTER")
    print("=" * 45)
    
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    
    choice = input("Select an option (1/2): ").strip()
    
    try:
        val = float(input("Enter weight: "))
        
        if choice == '1':
            res = val * 2.20462
            print(f"{val} kg = {res:.2f} lbs")
        elif choice == '2':
            res = val / 2.20462
            print(f"{val} lbs = {res:.2f} kg")
        else:
            print("Invalid choice.")
            return False
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_47()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 047_weight_unit_converter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Weight Unit Converter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
