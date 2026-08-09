# 🚀 Roman Numeral Converter

## 📝 Description
Convert an integer to Roman numerals.

### 🎯 Category
**Math & Logic**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 053: Roman Numeral Converter
Category: Math & Logic
Description: Convert an integer to Roman numerals.
"""

def run_project_53():
    print("=" * 45)
    print("    PYTHON PROJECT 053: ROMAN NUMERALS")
    print("=" * 45)
    
    try:
        num = int(input("Enter an integer (1 - 3999): "))
        
        if not (0 < num < 4000):
            print("Number out of range.")
            return False
            
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        
        roman_num = ''
        i = 0
        original = num
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
            
        print(f"\n{original} in Roman Numerals is: {roman_num}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_53()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 053_roman_numeral_converter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Roman Numeral Converter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
