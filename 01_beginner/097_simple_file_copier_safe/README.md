# 🚀 Simple File Copier

## 📝 Description
Copy content from one text file to another.

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
Project 097: Simple File Copier
Category: File Handling
Description: Copy content from one text file to another.
"""
import os

def run_project_97():
    print("=" * 45)
    print("      PYTHON PROJECT 097: SIMPLE FILE COPIER")
    print("=" * 45)
    
    source = input("Enter source file path: ").strip()
    dest = input("Enter destination file path: ").strip()
    
    if not os.path.isfile(source):
        print("Source file does not exist.")
        return False
        
    try:
        with open(source, 'r', encoding='utf-8') as src:
            content = src.read()
            
        with open(dest, 'w', encoding='utf-8') as dst:
            dst.write(content)
            
        print(f"\nSuccessfully copied contents from {source} to {dest}.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    run_project_97()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 097_simple_file_copier_safe.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple File Copier in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
