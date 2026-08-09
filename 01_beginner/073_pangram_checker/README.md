# 🚀 Pangram Checker

## 📝 Description
Check if a sentence contains every letter of the alphabet.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Module Importing
- User Input

## 💻 Source Code
```python
"""
Project 073: Pangram Checker
Category: Text & Strings
Description: Check if a sentence contains every letter of the alphabet.
"""
import string

def run_project_73():
    print("=" * 45)
    print("      PYTHON PROJECT 073: PANGRAM CHECKER")
    print("=" * 45)
    
    text = input("Enter a sentence to check: ").lower()
    
    alphabet = set(string.ascii_lowercase)
    letters_in_text = set(char for char in text if char in alphabet)
    
    if alphabet == letters_in_text:
        print("\nYes! This sentence is a pangram.")
    else:
        missing = alphabet - letters_in_text
        print("\nNo, this is not a pangram.")
        print(f"Missing letters: {', '.join(sorted(missing))}")
        
    return True

if __name__ == "__main__":
    run_project_73()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 073_pangram_checker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Pangram Checker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
