# 🚀 Morse Code Translator

## 📝 Description
Translate English to Morse code and back.

### 🎯 Category
**Security & Text**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Comprehensions
- User Input

## 💻 Source Code
```python
"""
Project 085: Morse Code Translator
Category: Security & Text
Description: Translate English to Morse code and back.
"""

def run_project_85():
    print("=" * 45)
    print("     PYTHON PROJECT 085: MORSE CODE TOOL")
    print("=" * 45)
    
    MORSE_CODE_DICT = {
        'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
        'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
        'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
        'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
        'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
        '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..',
        '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'
    }
    
    REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
    
    print("1. Text to Morse")
    print("2. Morse to Text (use spaces between letters)")
    choice = input("Choice: ").strip()
    
    if choice == '1':
        text = input("Enter text: ").upper()
        result = " ".join(MORSE_CODE_DICT.get(c, '?') for c in text if c != ' ')
        print(f"Morse: {result}")
    elif choice == '2':
        morse = input("Enter morse: ").strip()
        result = "".join(REVERSE_DICT.get(code, '?') for code in morse.split())
        print(f"Text: {result}")
    else:
        print("Invalid choice.")
        return False
        
    return True

if __name__ == "__main__":
    run_project_85()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 085_morse_code_translator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Morse Code Translator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
