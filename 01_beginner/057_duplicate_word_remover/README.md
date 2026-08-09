# 🚀 Duplicate Word Remover

## 📝 Description
Remove duplicate words from a string while preserving order.

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
Project 057: Duplicate Word Remover
Category: Text & Strings
Description: Remove duplicate words from a string while preserving order.
"""

def run_project_57():
    print("=" * 45)
    print("    PYTHON PROJECT 057: DUPLICATE WORD REMOVER")
    print("=" * 45)
    
    text = input("Enter a sentence with duplicate words: ").strip()
    
    if not text:
        return False
        
    words = text.split()
    seen = set()
    result = []
    
    for word in words:
        if word.lower() not in seen:
            seen.add(word.lower())
            result.append(word)
            
    print("\n--- Result ---")
    print(" ".join(result))
    return True

if __name__ == "__main__":
    run_project_57()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 057_duplicate_word_remover.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Duplicate Word Remover in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
