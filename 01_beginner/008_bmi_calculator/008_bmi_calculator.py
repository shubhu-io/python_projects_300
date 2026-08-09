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
