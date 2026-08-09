"""
Project 093: Simple Work Hours Tracker
Category: Utilities
Description: Track hours worked per day and calculate total.
"""

def run_project_93():
    print("=" * 45)
    print("     PYTHON PROJECT 093: WORK HOURS TRACKER")
    print("=" * 45)
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    total_hours = 0.0
    
    try:
        for day in days:
            hours = float(input(f"Enter hours worked on {day}: "))
            if hours < 0:
                print("Hours cannot be negative.")
                return False
            total_hours += hours
            
        rate = float(input("\nEnter hourly rate: $"))
        
        print("\n--- Weekly Summary ---")
        print(f"Total Hours: {total_hours:.2f}")
        print(f"Gross Pay: ${total_hours * rate:.2f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_93()
