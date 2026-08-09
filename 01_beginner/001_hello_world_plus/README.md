# 🚀 Hello World Plus

## 📝 Description
Enhanced greeting generator with time-based greetings.

### 🎯 Category
**CLI & Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Module Importing
- User Input

## 💻 Source Code
```python
"""
Project 001: Hello World Plus
Category: CLI & Utilities
Description: Enhanced greeting generator with time-based greetings.
"""
import datetime

def run_project_1():
    print("=" * 45)
    print("       PYTHON PROJECT 001: HELLO WORLD PLUS")
    print("=" * 45)
    
    name = input("Enter your name: ").strip()
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
        
    print(f"\n{greeting}, {name}! Welcome to your Python journey.")
    return True

if __name__ == "__main__":
    run_project_1()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 001_hello_world_plus.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Hello World Plus in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
