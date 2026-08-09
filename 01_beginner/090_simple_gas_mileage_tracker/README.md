# 🚀 Simple Gas Mileage Tracker

## 📝 Description
Calculate Miles Per Gallon (MPG).

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
Project 090: Simple Gas Mileage Tracker
Category: Math & Utilities
Description: Calculate Miles Per Gallon (MPG).
"""

def run_project_90():
    print("=" * 45)
    print("      PYTHON PROJECT 090: GAS MILEAGE TRACKER")
    print("=" * 45)
    
    try:
        miles = float(input("Enter miles driven: "))
        gallons = float(input("Enter gallons of gas used: "))
        
        if gallons <= 0:
            print("Gallons must be greater than 0.")
            return False
            
        mpg = miles / gallons
        
        print(f"\nYour car's gas mileage is: {mpg:.2f} MPG")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_90()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 090_simple_gas_mileage_tracker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Gas Mileage Tracker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
