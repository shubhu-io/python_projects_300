# 🚀 Anagram Solver and Checker

## 📝 Description
Check if two words are anagrams.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 024: Anagram Solver and Checker
Category: Text & Strings
Description: Check if two words are anagrams.
"""

def run_project_24():
    print("=" * 45)
    print("    PYTHON PROJECT 024: ANAGRAM CHECKER")
    print("=" * 45)
    
    word1 = input("Enter first word: ").strip().lower().replace(" ", "")
    word2 = input("Enter second word: ").strip().lower().replace(" ", "")
    
    if not word1 or not word2:
        print("Invalid input.")
        return False
        
    is_anagram = sorted(word1) == sorted(word2)
    
    if is_anagram:
        print(f"\nYes! '{word1}' and '{word2}' are anagrams.")
    else:
        print(f"\nNo, '{word1}' and '{word2}' are not anagrams.")
        
    return True

if __name__ == "__main__":
    run_project_24()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 024_anagram_solver_and_checker.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Anagram Solver and Checker in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
