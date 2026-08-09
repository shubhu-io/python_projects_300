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
