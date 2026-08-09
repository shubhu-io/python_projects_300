# 🚀 Basic Password Strength Meter

## 📝 Description
Check password strength based on length, digits, and cases.

### 🎯 Category
**Security & Text**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 060: Basic Password Strength Meter
Category: Security & Text
Description: Check password strength based on length, digits, and cases.
"""

def run_project_60():
    print("=" * 45)
    print("    PYTHON PROJECT 060: PASSWORD STRENGTH")
    print("=" * 45)
    
    pwd = input("Enter a password to test: ")
    
    score = 0
    if len(pwd) >= 8:
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.islower() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*()-_+=<>?/\\|~{}[]," for c in pwd):
        score += 1
        
    print("\n--- Result ---")
    if score < 3:
        print("Strength: Weak")
    elif score < 5:
        print("Strength: Medium")
    else:
        print("Strength: Strong")
        
    return True

if __name__ == "__main__":
    run_project_60()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 060_basic_password_strength_meter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Basic Password Strength Meter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
