# 🚀 Length Converter

## 📝 Description
Convert lengths (meters, kilometers, miles, feet).

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
Project 022: Length Converter
Category: Utilities
Description: Convert lengths (meters, kilometers, miles, feet).
"""

def run_project_22():
    print("=" * 45)
    print("      PYTHON PROJECT 022: LENGTH CONVERTER")
    print("=" * 45)
    
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    
    choice = input("Select an option (1-4): ").strip()
    
    try:
        val = float(input("Enter the value to convert: "))
        
        if choice == '1':
            res = val * 3.28084
            print(f"{val} m = {res:.2f} ft")
        elif choice == '2':
            res = val / 3.28084
            print(f"{val} ft = {res:.2f} m")
        elif choice == '3':
            res = val * 0.621371
            print(f"{val} km = {res:.2f} mi")
        elif choice == '4':
            res = val / 0.621371
            print(f"{val} mi = {res:.2f} km")
        else:
            print("Invalid choice.")
            return False
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_22()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 022_length_converter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Length Converter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
