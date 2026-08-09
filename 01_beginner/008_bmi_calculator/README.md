# 🚀 BMI Calculator

## 📝 Description
Calculate Body Mass Index and category.

### 🎯 Category
**Health & Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 008: BMI Calculator
Category: Health & Utilities
Description: Calculate Body Mass Index and category.
"""

def run_project_8():
    print("=" * 45)
    print("       PYTHON PROJECT 008: BMI CALCULATOR")
    print("=" * 45)
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        if height <= 0 or weight <= 0:
            print("Height and weight must be positive numbers.")
            return False
            
        bmi = weight / (height ** 2)
        
        category = ""
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
            
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"Category: {category}")
        return True
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return False

if __name__ == "__main__":
    run_project_8()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 008_bmi_calculator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch BMI Calculator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
