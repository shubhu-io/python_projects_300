# 🚀 Palindrome Checker

## 📝 Description
Check if a given string is a palindrome.

### 🎯 Category
**Math & Logic**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Module Importing
- User Input

## 💻 Source Code
```python
"""
Project 007: Palindrome Checker
Category: Math & Logic
Description: Check if a given string is a palindrome.
"""
import re

def run_project_7():
    print("=" * 45)
    print("     PYTHON PROJECT 007: PALINDROME CHECKER")
    print("=" * 45)
    
    text = input("Enter a word or phrase: ").strip()
    
    # Remove non-alphanumeric chars and lowercase
    clean_text = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    
    if not clean_text:
        print("Invalid input.")
        return False
        
    is_palindrome = clean_text == clean_text[::-1]
    
    if is_palindrome:
        print(f"\n'{text}' IS a palindrome!")
    else:
        print(f"\n'{text}' is NOT a palindrome.")
        
    return True

if __name__ == "__main__":
    run_project_7()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 007_palindrome_checker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Palindrome Checker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
