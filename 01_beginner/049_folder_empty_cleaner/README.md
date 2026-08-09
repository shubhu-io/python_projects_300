# 🚀 Folder Empty Cleaner

## 📝 Description
Check for empty folders (simulated).

### 🎯 Category
**File Handling**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 049: Folder Empty Cleaner
Category: File Handling
Description: Check for empty folders (simulated).
"""
import os

def run_project_49():
    print("=" * 45)
    print("     PYTHON PROJECT 049: EMPTY FOLDER SCANNER")
    print("=" * 45)
    
    folder = input("Enter directory path to scan (or '.' for current): ").strip()
    
    if not os.path.isdir(folder):
        print("Invalid directory path.")
        return False
        
    empty_folders = []
    try:
        for root, dirs, files in os.walk(folder):
            if not dirs and not files:
                empty_folders.append(root)
                
        if empty_folders:
            print("\nFound empty folders:")
            for f in empty_folders:
                print(f)
        else:
            print("\nNo empty folders found.")
            
        return True
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return False

if __name__ == "__main__":
    run_project_49()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 049_folder_empty_cleaner.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Folder Empty Cleaner in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
