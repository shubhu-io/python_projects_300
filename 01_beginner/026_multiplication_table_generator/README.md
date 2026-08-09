# 🚀 Multiplication Table Generator

## 📝 Description
Print multiplication table for a given number.

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
Project 026: Multiplication Table Generator
Category: Math & Logic
Description: Print multiplication table for a given number.
"""

def run_project_26():
    print("=" * 45)
    print("   PYTHON PROJECT 026: MULTIPLICATION TABLE")
    print("=" * 45)
    
    try:
        num = int(input("Enter a number to see its table: "))
        limit = int(input("Enter the limit (e.g., 10): "))
        
        print(f"\n--- Multiplication Table for {num} ---")
        for i in range(1, limit + 1):
            print(f"{num} x {i} = {num * i}")
            
        return True
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return False

if __name__ == "__main__":
    run_project_26()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 026_multiplication_table_generator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Multiplication Table Generator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
