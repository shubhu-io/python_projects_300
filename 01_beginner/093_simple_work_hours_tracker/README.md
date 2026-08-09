# 🚀 Simple Work Hours Tracker

## 📝 Description
Track hours worked per day and calculate total.

### 🎯 Category
**Utilities**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
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
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 093_simple_work_hours_tracker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Work Hours Tracker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
