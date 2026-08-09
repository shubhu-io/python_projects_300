# 🚀 ROT13 Cipher Tool

## 📝 Description
Encrypt/decrypt using ROT13.

### 🎯 Category
**Security & Text**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Loops (`for`/`while`)
- User Input

## 💻 Source Code
```python
"""
Project 071: ROT13 Cipher Tool
Category: Security & Text
Description: Encrypt/decrypt using ROT13.
"""

def run_project_71():
    print("=" * 45)
    print("      PYTHON PROJECT 071: ROT13 CIPHER")
    print("=" * 45)
    
    text = input("Enter text to apply ROT13: ")
    result = ""
    
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            result += char
            
    print(f"\nResult: {result}")
    return True

if __name__ == "__main__":
    run_project_71()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 071_rot13_cipher_tool.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch ROT13 Cipher Tool in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
