# 🚀 Speed Unit Converter

## 📝 Description
Convert between mph, km/h, and m/s.

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
Project 040: Speed Unit Converter
Category: Utilities
Description: Convert between mph, km/h, and m/s.
"""

def run_project_40():
    print("=" * 45)
    print("      PYTHON PROJECT 040: SPEED UNIT CONVERTER")
    print("=" * 45)
    
    print("1. km/h to mph")
    print("2. mph to km/h")
    print("3. km/h to m/s")
    print("4. m/s to km/h")
    
    choice = input("Select an option (1-4): ").strip()
    
    try:
        val = float(input("Enter the speed value: "))
        
        if choice == '1':
            res = val * 0.621371
            print(f"{val} km/h = {res:.2f} mph")
        elif choice == '2':
            res = val / 0.621371
            print(f"{val} mph = {res:.2f} km/h")
        elif choice == '3':
            res = val / 3.6
            print(f"{val} km/h = {res:.2f} m/s")
        elif choice == '4':
            res = val * 3.6
            print(f"{val} m/s = {res:.2f} km/h")
        else:
            print("Invalid choice.")
            return False
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_40()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 040_speed_unit_converter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Speed Unit Converter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
