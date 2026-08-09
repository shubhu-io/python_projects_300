# 🚀 Temperature Converter

## 📝 Description
Convert between Celsius, Fahrenheit, and Kelvin.

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
Project 004: Temperature Converter
Category: Utilities
Description: Convert between Celsius, Fahrenheit, and Kelvin.
"""

def run_project_4():
    print("=" * 45)
    print("   PYTHON PROJECT 004: TEMPERATURE CONVERTER")
    print("=" * 45)
    
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Select an option (1/2): ").strip()
    
    try:
        temp = float(input("Enter the temperature: "))
        if choice == '1':
            converted = (temp * 9/5) + 32
            print(f"{temp}°C is equal to {converted:.2f}°F")
        elif choice == '2':
            converted = (temp - 32) * 5/9
            print(f"{temp}°F is equal to {converted:.2f}°C")
        else:
            print("Invalid choice!")
            return False
        return True
    except ValueError:
        print("Invalid input for temperature.")
        return False

if __name__ == "__main__":
    run_project_4()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 004_temperature_converter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Temperature Converter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
