# 🚀 ASCII Art Banner Generator

## 📝 Description
Create simple text banners.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 045: ASCII Art Banner Generator
Category: Text & Strings
Description: Create simple text banners.
"""

def run_project_45():
    print("=" * 45)
    print("    PYTHON PROJECT 045: ASCII ART BANNER")
    print("=" * 45)
    
    text = input("Enter text for the banner: ").strip()
    
    if not text:
        return False
        
    width = len(text) + 6
    print("\n" + "=" * width)
    print(f"== {text} ==")
    print("=" * width + "\n")
    
    return True

if __name__ == "__main__":
    run_project_45()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 045_ascii_art_banner_generator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch ASCII Art Banner Generator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
