"""
Project 041: Simple BMI Chart
Category: Health & Utilities
Description: Print a reference chart for BMI categories.
"""

def run_project_41():
    print("=" * 45)
    print("       PYTHON PROJECT 041: BMI CHART INFO")
    print("=" * 45)
    
    chart = [
        ("Underweight", "< 18.5"),
        ("Normal weight", "18.5 - 24.9"),
        ("Overweight", "25.0 - 29.9"),
        ("Obese Class I", "30.0 - 34.9"),
        ("Obese Class II", "35.0 - 39.9"),
        ("Obese Class III", ">= 40.0")
    ]
    
    print(f"{'Category':<20} | {'BMI Range'}")
    print("-" * 45)
    for category, bmi_range in chart:
        print(f"{category:<20} | {bmi_range}")
        
    return True

if __name__ == "__main__":
    run_project_41()
