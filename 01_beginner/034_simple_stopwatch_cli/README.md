# 🚀 Simple Stopwatch CLI

## 📝 Description
A basic stopwatch that counts elapsed time.

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
Project 034: Simple Stopwatch CLI
Category: CLI & Utilities
Description: A basic stopwatch that counts elapsed time.
"""
import time

def run_project_34():
    print("=" * 45)
    print("    PYTHON PROJECT 034: SIMPLE STOPWATCH CLI")
    print("=" * 45)
    
    print("Press ENTER to start the stopwatch.")
    print("Press ENTER again to stop.")
    
    input("Ready? [Press Enter]")
    start_time = time.time()
    print("Stopwatch started...")
    
    input("[Press Enter to stop]")
    end_time = time.time()
    
    elapsed = end_time - start_time
    print(f"\nElapsed Time: {elapsed:.2f} seconds")
    return True

if __name__ == "__main__":
    run_project_34()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 034_simple_stopwatch_cli.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Stopwatch CLI in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
