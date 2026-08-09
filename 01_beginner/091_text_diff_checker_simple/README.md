# 🚀 Text Diff Checker Simple

## 📝 Description
Compare two strings for differences.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Loops (`for`/`while`)
- User Input

## 💻 Source Code
```python
"""
Project 091: Text Diff Checker Simple
Category: Text & Strings
Description: Compare two strings for differences.
"""

def run_project_91():
    print("=" * 45)
    print("      PYTHON PROJECT 091: TEXT DIFF CHECKER")
    print("=" * 45)
    
    text1 = input("Enter first string: ")
    text2 = input("Enter second string: ")
    
    if text1 == text2:
        print("\nThe strings are exactly identical.")
        return True
        
    print("\nThe strings are different.")
    
    words1 = text1.split()
    words2 = text2.split()
    
    diff = set(words1) ^ set(words2)
    
    if diff:
        print("Words that are not in both strings:")
        for w in diff:
            print(f"- {w}")
    else:
        print("They contain the same words, but perhaps in a different order or with different spacing.")
        
    return True

if __name__ == "__main__":
    run_project_91()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 091_text_diff_checker_simple.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Text Diff Checker Simple in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
