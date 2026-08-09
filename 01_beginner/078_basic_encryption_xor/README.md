# 🚀 Basic Encryption XOR

## 📝 Description
Encrypt and decrypt a string using XOR.

### 🎯 Category
**Security**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 078: Basic Encryption XOR
Category: Security
Description: Encrypt and decrypt a string using XOR.
"""

def run_project_78():
    print("=" * 45)
    print("       PYTHON PROJECT 078: XOR ENCRYPTION")
    print("=" * 45)
    
    text = input("Enter text to encrypt/decrypt: ")
    try:
        key = int(input("Enter a numeric key (0-255): "))
        if not (0 <= key <= 255):
            print("Key out of range.")
            return False
            
        result = "".join(chr(ord(c) ^ key) for c in text)
        
        print(f"\nResult (can contain unprintable chars): {result}")
        print(f"Hex representation: {result.encode().hex()}")
        return True
    except ValueError:
        print("Invalid key.")
        return False

if __name__ == "__main__":
    run_project_78()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 078_basic_encryption_xor.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Basic Encryption XOR in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
