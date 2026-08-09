# 🚀 Vowel and Consonant Counter

## 📝 Description
Count vowels and consonants in a string.

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
Project 023: Vowel and Consonant Counter
Category: Text & Strings
Description: Count vowels and consonants in a string.
"""

def run_project_23():
    print("=" * 45)
    print("  PYTHON PROJECT 023: VOWEL & CONSONANT COUNTER")
    print("=" * 45)
    
    text = input("Enter a string: ").strip().lower()
    
    vowels = "aeiou"
    v_count = 0
    c_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
    print("\n--- Analysis ---")
    print(f"Vowels: {v_count}")
    print(f"Consonants: {c_count}")
    return True

if __name__ == "__main__":
    run_project_23()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 023_vowel_and_consonant_counter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Vowel and Consonant Counter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
