# 🚀 Capitalize Sentence Tool

## 📝 Description
Capitalize the first letter of each word in a sentence.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 035: Capitalize Sentence Tool
Category: Text & Strings
Description: Capitalize the first letter of each word in a sentence.
"""

def run_project_35():
    print("=" * 45)
    print("   PYTHON PROJECT 035: CAPITALIZE SENTENCE")
    print("=" * 45)
    
    text = input("Enter a sentence: ").strip()
    
    if not text:
        print("Empty string provided.")
        return False
        
    # Titlecase capitalizes first letter of each word
    result = text.title()
    
    print("\n--- Result ---")
    print(result)
    return True

if __name__ == "__main__":
    run_project_35()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 035_capitalize_sentence_tool.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Capitalize Sentence Tool in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
