# 🚀 Simple Number Pattern Drawer

## 📝 Description
Draw a pyramid pattern of numbers.

### 🎯 Category
**CLI & Utilities**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 074: Simple Number Pattern Drawer
Category: CLI & Utilities
Description: Draw a pyramid pattern of numbers.
"""

def run_project_74():
    print("=" * 45)
    print("   PYTHON PROJECT 074: NUMBER PATTERN DRAWER")
    print("=" * 45)
    
    try:
        rows = int(input("Enter number of rows for the pyramid: "))
        
        print("\n--- Pattern ---")
        for i in range(1, rows + 1):
            # Print spaces
            print(" " * (rows - i), end="")
            # Print numbers
            for j in range(1, i + 1):
                print(f"{j} ", end="")
            print()
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_74()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 074_simple_number_pattern_drawer.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Number Pattern Drawer in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
