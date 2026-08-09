# 🚀 Binary to Decimal Converter

## 📝 Description
Convert binary string to decimal integer.

### 🎯 Category
**Math & Logic**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 081: Binary to Decimal Converter
Category: Math & Logic
Description: Convert binary string to decimal integer.
"""

def run_project_81():
    print("=" * 45)
    print("   PYTHON PROJECT 081: BINARY CONVERTER")
    print("=" * 45)
    
    binary_str = input("Enter a binary number: ").strip()
    
    if not all(c in '01' for c in binary_str):
        print("Invalid binary number.")
        return False
        
    decimal = int(binary_str, 2)
    print(f"\nBinary: {binary_str}")
    print(f"Decimal: {decimal}")
    
    return True

if __name__ == "__main__":
    run_project_81()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 081_binary_to_decimal_converter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Binary to Decimal Converter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
