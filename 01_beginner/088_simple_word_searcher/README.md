# 🚀 Simple Word Searcher

## 📝 Description
Find the number of occurrences of a specific word in a text.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 088: Simple Word Searcher
Category: Text & Strings
Description: Find the number of occurrences of a specific word in a text.
"""

def run_project_88():
    print("=" * 45)
    print("      PYTHON PROJECT 088: SIMPLE WORD SEARCH")
    print("=" * 45)
    
    text = input("Enter a long text block: ").lower()
    word = input("Enter the word to search for: ").strip().lower()
    
    if not text or not word:
        return False
        
    count = text.split().count(word)
    
    print(f"\nFound the word '{word}' exactly {count} times as a full word.")
    return True

if __name__ == "__main__":
    run_project_88()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 088_simple_word_searcher.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Word Searcher in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
