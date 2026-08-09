# 🚀 Text Truncator and Ellipsis

## 📝 Description
Truncate a long string and add '...' at the end.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 069: Text Truncator and Ellipsis
Category: Text & Strings
Description: Truncate a long string and add '...' at the end.
"""

def run_project_69():
    print("=" * 45)
    print("       PYTHON PROJECT 069: TEXT TRUNCATOR")
    print("=" * 45)
    
    text = input("Enter a long sentence: ")
    try:
        limit = int(input("Enter max length: "))
        
        if len(text) > limit:
            # truncate and add ellipsis
            # Make sure we don't end up longer than limit
            shortened = text[:limit-3] + "..." if limit > 3 else text[:limit]
            print(f"\nTruncated: {shortened}")
        else:
            print(f"\nText fits within limit: {text}")
            
        return True
    except ValueError:
        print("Invalid length.")
        return False

if __name__ == "__main__":
    run_project_69()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 069_text_truncator_and_ellipsis.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Text Truncator and Ellipsis in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
