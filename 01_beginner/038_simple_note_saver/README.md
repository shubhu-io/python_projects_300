# 🚀 Simple Note Saver

## 📝 Description
Save short notes to a text file.

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
Project 038: Simple Note Saver
Category: File Handling
Description: Save short notes to a text file.
"""
import os

def run_project_38():
    print("=" * 45)
    print("      PYTHON PROJECT 038: SIMPLE NOTE SAVER")
    print("=" * 45)
    
    filename = "my_notes.txt"
    
    print("Enter your note (or type 'EXIT' to quit):")
    note = input("> ")
    
    if note.strip().upper() == 'EXIT':
        print("Cancelled.")
        return True
        
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(note + "\n")
        print(f"\nNote saved to {filename} successfully.")
        return True
    except Exception as e:
        print(f"Failed to save note: {e}")
        return False

if __name__ == "__main__":
    run_project_38()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 038_simple_note_saver.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Note Saver in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
