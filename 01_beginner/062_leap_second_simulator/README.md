# 🚀 Leap Second Simulator

## 📝 Description
Simulate adding a leap second to a digital clock.

### 🎯 Category
**Utilities**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 062: Leap Second Simulator
Category: Utilities
Description: Simulate adding a leap second to a digital clock.
"""
import time

def run_project_62():
    print("=" * 45)
    print("   PYTHON PROJECT 062: LEAP SECOND SIMULATOR")
    print("=" * 45)
    
    print("Simulating a countdown to a leap second (23:59:60).")
    
    try:
        for sec in range(55, 62):
            if sec == 60:
                timer = "23:59:60 [LEAP SECOND]"
            elif sec == 61:
                timer = "00:00:00"
            else:
                timer = f"23:59:{sec:02d}"
                
            print(f"\r{timer}", end="", flush=True)
            time.sleep(1)
            
        print("\n\nSimulation complete.")
        return True
    except KeyboardInterrupt:
        print("\nSimulation aborted.")
        return False

if __name__ == "__main__":
    run_project_62()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 062_leap_second_simulator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Leap Second Simulator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
