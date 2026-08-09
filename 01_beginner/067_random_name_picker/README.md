# 🚀 Random Name Picker

## 📝 Description
Pick a random name from a provided list.

### 🎯 Category
**Utilities & Games**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Comprehensions

## 💻 Source Code
```python
"""
Project 067: Random Name Picker
Category: Utilities & Games
Description: Pick a random name from a provided list.
"""
import random

def run_project_67():
    print("=" * 45)
    print("      PYTHON PROJECT 067: RANDOM NAME PICKER")
    print("=" * 45)
    
    names_str = input("Enter names separated by commas:\n").strip()
    
    if not names_str:
        print("No names provided.")
        return False
        
    names = [n.strip() for n in names_str.split(',') if n.strip()]
    
    if not names:
        print("No valid names found.")
        return False
        
    winner = random.choice(names)
    print(f"\nAnd the winner is... {winner}!")
    return True

if __name__ == "__main__":
    run_project_67()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 067_random_name_picker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Random Name Picker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
