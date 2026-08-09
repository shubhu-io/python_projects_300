# 🚀 Simple Countdown Timer

## 📝 Description
A basic countdown timer.

### 🎯 Category
**Utilities**

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
Project 043: Simple Countdown Timer
Category: Utilities
Description: A basic countdown timer.
"""
import time
import sys

def run_project_43():
    print("=" * 45)
    print("    PYTHON PROJECT 043: SIMPLE COUNTDOWN TIMER")
    print("=" * 45)
    
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        
        if seconds <= 0:
            print("Must be positive.")
            return False
            
        print("\nStarting countdown...")
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            sys.stdout.write(f"\r{timer}")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
            
        print("\n\nTIME IS UP!")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_43()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 043_simple_countdown_timer.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Countdown Timer in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
