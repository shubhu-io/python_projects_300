# 🚀 Text Alignment Utility

## 📝 Description
Align text to left, right, or center.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 063: Text Alignment Utility
Category: Text & Strings
Description: Align text to left, right, or center.
"""

def run_project_63():
    print("=" * 45)
    print("     PYTHON PROJECT 063: TEXT ALIGNMENT")
    print("=" * 45)
    
    text = input("Enter a short string: ")
    try:
        width = int(input("Enter terminal width (e.g., 40): "))
        
        print("\n--- Left Aligned ---")
        print(text.ljust(width, '-'))
        
        print("\n--- Center Aligned ---")
        print(text.center(width, '-'))
        
        print("\n--- Right Aligned ---")
        print(text.rjust(width, '-'))
        
        return True
    except ValueError:
        print("Invalid width.")
        return False

if __name__ == "__main__":
    run_project_63()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 063_text_alignment_utility.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Text Alignment Utility in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
