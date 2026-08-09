# 🚀 Simple Decision Maker

## 📝 Description
Input options and randomly choose one.

### 🎯 Category
**CLI & Utilities**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code

## 💻 Source Code
```python
"""
Project 092: Simple Decision Maker
Category: CLI & Utilities
Description: Input options and randomly choose one.
"""
import random

def run_project_92():
    print("=" * 45)
    print("      PYTHON PROJECT 092: DECISION MAKER")
    print("=" * 45)
    
    print("Enter options one by one. Type 'done' when finished.")
    options = []
    
    while True:
        opt = input("Option: ").strip()
        if opt.lower() == 'done':
            break
        if opt:
            options.append(opt)
            
    if not options:
        print("No options provided. Cannot make a decision.")
        return False
        
    print("\nThinking...")
    winner = random.choice(options)
    print(f"\nThe Decision Maker has chosen: {winner.upper()}")
    
    return True

if __name__ == "__main__":
    run_project_92()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 092_simple_decision_maker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Decision Maker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
