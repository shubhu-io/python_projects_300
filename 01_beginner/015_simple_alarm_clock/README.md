# 🚀 Simple Alarm Clock

## 📝 Description
A basic alarm clock that waits for a specific time.

### 🎯 Category
**CLI & Utilities**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 015: Simple Alarm Clock
Category: CLI & Utilities
Description: A basic alarm clock that waits for a specific time.
"""
import time
import datetime

def run_project_15():
    print("=" * 45)
    print("      PYTHON PROJECT 015: SIMPLE ALARM CLOCK")
    print("=" * 45)
    
    alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ").strip()
    
    try:
        # Validate format
        datetime.datetime.strptime(alarm_time, "%H:%M")
        
        print(f"Alarm set for {alarm_time}. Waiting... (Press Ctrl+C to cancel)")
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            if now == alarm_time:
                print("\n" + "=" * 20)
                print("WAKE UP! ALARM RINGING!")
                print("=" * 20 + "\n")
                break
            time.sleep(10) # check every 10 seconds
        return True
    except ValueError:
        print("Invalid time format. Please use HH:MM.")
        return False
    except KeyboardInterrupt:
        print("\nAlarm cancelled.")
        return False

if __name__ == "__main__":
    run_project_15()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 015_simple_alarm_clock.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Alarm Clock in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
