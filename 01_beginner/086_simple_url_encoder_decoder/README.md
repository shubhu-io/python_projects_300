# 🚀 Simple URL Encoder/Decoder

## 📝 Description
URL encode or decode a string.

### 🎯 Category
**Web & Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Module Importing
- User Input

## 💻 Source Code
```python
"""
Project 086: Simple URL Encoder/Decoder
Category: Web & Utilities
Description: URL encode or decode a string.
"""
import urllib.parse

def run_project_86():
    print("=" * 45)
    print("    PYTHON PROJECT 086: URL ENCODER/DECODER")
    print("=" * 45)
    
    print("1. Encode")
    print("2. Decode")
    choice = input("Choice (1/2): ").strip()
    
    text = input("Enter string: ")
    
    if choice == '1':
        print(f"\nEncoded: {urllib.parse.quote(text)}")
    elif choice == '2':
        print(f"\nDecoded: {urllib.parse.unquote(text)}")
    else:
        print("Invalid choice.")
        return False
        
    return True

if __name__ == "__main__":
    run_project_86()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 086_simple_url_encoder_decoder.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple URL Encoder/Decoder in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
