# 🚀 Word and Text Analyzer

## 📝 Description
Count characters, words, and sentences in a given text.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
    Project 005: Word and Text Analyzer
Category: Text & Strings
Description: Count characters, words, and sentences in a given text.
"""

def run_project_5():
    print("=" * 45)
    print("   PYTHON PROJECT 005: WORD & TEXT ANALYZER")
    print("=" * 45)
    
    text = input("Enter some text to analyze:\n").strip()
    if not text:
        print("No text provided.")
        return False
        
    chars = len(text)
    words = len(text.split())
    # Basic sentence counting by punctuation
    sentences = max(1, text.count('.') + text.count('!') + text.count('?'))
    
    print("\n--- Analysis Results ---")
    print(f"Characters (with spaces): {chars}")
    print(f"Words: {words}")
    print(f"Sentences: {sentences}")
    return True

if __name__ == "__main__":
    run_project_5()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 005_word_and_text_analyzer.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Word and Text Analyzer in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
