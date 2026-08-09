# 🚀 Reverse String Tool

## 📝 Description
Reverse a given string.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 033: Reverse String Tool
Category: Text & Strings
Description: Reverse a given string.
"""

def run_project_33():
    print("=" * 45)
    print("      PYTHON PROJECT 033: REVERSE STRING")
    print("=" * 45)
    
    text = input("Enter a string to reverse: ")
    
    reversed_text = text[::-1]
    
    print("\n--- Result ---")
    print(f"Original: {text}")
    print(f"Reversed: {reversed_text}")
    return True

if __name__ == "__main__":
    run_project_33()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 033_reverse_string_tool.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Reverse String Tool in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
