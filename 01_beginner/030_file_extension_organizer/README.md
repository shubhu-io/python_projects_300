# 🚀 File Extension Organizer

## 📝 Description
Analyze extensions in a directory (simulation).

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
Project 030: File Extension Organizer
Category: File Handling
Description: Analyze extensions in a directory (simulation).
"""
import os

def run_project_30():
    print("=" * 45)
    print("    PYTHON PROJECT 030: EXTENSION ORGANIZER")
    print("=" * 45)
    
    folder = input("Enter directory path to analyze (or '.' for current): ").strip()
    
    if not os.path.isdir(folder):
        print("Invalid directory path.")
        return False
        
    ext_count = {}
    try:
        for item in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, item)):
                _, ext = os.path.splitext(item)
                ext = ext.lower() if ext else "No Extension"
                ext_count[ext] = ext_count.get(ext, 0) + 1
                
        print("\n--- File Extensions Found ---")
        for ext, count in sorted(ext_count.items()):
            print(f"{ext}: {count} file(s)")
            
        return True
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return False

if __name__ == "__main__":
    run_project_30()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 030_file_extension_organizer.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch File Extension Organizer in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
