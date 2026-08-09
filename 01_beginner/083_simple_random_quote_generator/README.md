# 🚀 Simple Random Quote Generator

## 📝 Description
Display a random quote from a predefined list.

### 🎯 Category
**Utilities & Text**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Module Importing
- User Input

## 💻 Source Code
```python
"""
Project 083: Simple Random Quote Generator
Category: Utilities & Text
Description: Display a random quote from a predefined list.
"""
import random

def run_project_83():
    print("=" * 45)
    print("     PYTHON PROJECT 083: RANDOM QUOTE GEN")
    print("=" * 45)
    
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "Get busy living or get busy dying. - Stephen King",
        "You only live once, but if you do it right, once is enough. - Mae West",
        "In the middle of difficulty lies opportunity. - Albert Einstein"
    ]
    
    input("Press Enter to get inspired...")
    print("\n" + "=" * 10 + " QUOTE " + "=" * 10)
    print(random.choice(quotes))
    print("=" * 27)
    
    return True

if __name__ == "__main__":
    run_project_83()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 083_simple_random_quote_generator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Random Quote Generator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
