# 🚀 Basic Battery Estimator

## 📝 Description
Estimate time remaining for a battery.

### 🎯 Category
**Math & Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 075: Basic Battery Estimator
Category: Math & Utilities
Description: Estimate time remaining for a battery.
"""

def run_project_75():
    print("=" * 45)
    print("     PYTHON PROJECT 075: BATTERY ESTIMATOR")
    print("=" * 45)
    
    try:
        capacity = float(input("Enter battery capacity (mAh): "))
        consumption = float(input("Enter device power consumption (mA): "))
        
        if consumption <= 0:
            print("Consumption must be greater than 0.")
            return False
            
        hours = capacity / consumption
        
        print(f"\nEstimated battery life: {hours:.2f} hours")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_75()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 075_basic_battery_estimator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Basic Battery Estimator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
