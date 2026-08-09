# 🚀 Character Frequency Counter

## 📝 Description
Count frequency of each character in a string.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Loops (`for`/`while`)
- User Input

## 💻 Source Code
```python
"""
Project 046: Character Frequency Counter
Category: Text & Strings
Description: Count frequency of each character in a string.
"""

def run_project_46():
    print("=" * 45)
    print("   PYTHON PROJECT 046: CHAR FREQUENCY COUNTER")
    print("=" * 45)
    
    text = input("Enter a string: ")
    freq = {}
    
    for char in text:
        if char.strip(): # Ignore spaces for display, or count them if desired
            freq[char] = freq.get(char, 0) + 1
            
    print("\n--- Frequency ---")
    for char, count in sorted(freq.items()):
        print(f"'{char}': {count}")
        
    return True

if __name__ == "__main__":
    run_project_46()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 046_character_frequency_counter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Character Frequency Counter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
