# 🚀 Text File Summary Tool

## 📝 Description
Read a text file and output a summary of lines, words, etc.

### 🎯 Category
**File Handling**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 017: Text File Summary Tool
Category: File Handling
Description: Read a text file and output a summary of lines, words, etc.
"""
import os

def run_project_17():
    print("=" * 45)
    print("   PYTHON PROJECT 017: TEXT FILE SUMMARY TOOL")
    print("=" * 45)
    
    filename = input("Enter the path of the text file to analyze: ").strip()
    
    if not os.path.exists(filename):
        print("Error: File does not exist.")
        return False
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        
        print("\n--- File Summary ---")
        print(f"Total Lines: {num_lines}")
        print(f"Total Words: {num_words}")
        print(f"Total Characters: {num_chars}")
        return True
    except Exception as e:
        print(f"An error occurred reading the file: {e}")
        return False

if __name__ == "__main__":
    run_project_17()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 017_text_file_summary_tool.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Text File Summary Tool in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
