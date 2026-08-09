# 🚀 Caesar Cipher Tool

## 📝 Description
Encrypt and decrypt text using a Caesar cipher.

### 🎯 Category
**Security & Text**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 027: Caesar Cipher Tool
Category: Security & Text
Description: Encrypt and decrypt text using a Caesar cipher.
"""

def run_project_27():
    print("=" * 45)
    print("      PYTHON PROJECT 027: CAESAR CIPHER")
    print("=" * 45)
    
    mode = input("Select mode (e)ncrypt or (d)ecrypt: ").strip().lower()
    if mode not in ['e', 'd']:
        print("Invalid mode.")
        return False
        
    text = input("Enter the message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return False
        
    if mode == 'd':
        shift = -shift
        
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
            
    print(f"\nResult: {result}")
    return True

if __name__ == "__main__":
    run_project_27()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 027_caesar_cipher_tool.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Caesar Cipher Tool in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
