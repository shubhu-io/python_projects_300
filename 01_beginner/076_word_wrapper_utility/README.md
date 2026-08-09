# 🚀 Word Wrapper Utility

## 📝 Description
Wrap text to a specific width.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 076: Word Wrapper Utility
Category: Text & Strings
Description: Wrap text to a specific width.
"""
import textwrap

def run_project_76():
    print("=" * 45)
    print("       PYTHON PROJECT 076: WORD WRAPPER")
    print("=" * 45)
    
    text = input("Enter a long string of text: ")
    try:
        width = int(input("Enter max line width: "))
        
        print(f"\n--- Wrapped Text (Width: {width}) ---")
        wrapped = textwrap.fill(text, width=width)
        print(wrapped)
        
        return True
    except ValueError:
        print("Invalid width.")
        return False

if __name__ == "__main__":
    run_project_76()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 076_word_wrapper_utility.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Word Wrapper Utility in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
