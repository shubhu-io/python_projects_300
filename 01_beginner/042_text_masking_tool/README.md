# 🚀 Text Masking Tool

## 📝 Description
Mask sensitive information (like passwords) with asterisks.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 042: Text Masking Tool
Category: Text & Strings
Description: Mask sensitive information (like passwords) with asterisks.
"""

def run_project_42():
    print("=" * 45)
    print("      PYTHON PROJECT 042: TEXT MASKING TOOL")
    print("=" * 45)
    
    text = input("Enter sensitive information (e.g. credit card): ").strip()
    
    if len(text) <= 4:
        print(f"Masked: {'*' * len(text)}")
    else:
        visible = text[-4:]
        masked_part = '*' * (len(text) - 4)
        print(f"Masked: {masked_part}{visible}")
        
    return True

if __name__ == "__main__":
    run_project_42()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 042_text_masking_tool.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Text Masking Tool in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
