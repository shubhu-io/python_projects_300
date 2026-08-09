# 🚀 Fibonacci Sequence Generator

## 📝 Description
Generates the Fibonacci sequence up to a given number of terms.

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
Project 011: Fibonacci Sequence Generator
Category: Math & Logic
Description: Generates the Fibonacci sequence up to a given number of terms.
"""

def run_project_11():
    print("=" * 45)
    print("   PYTHON PROJECT 011: FIBONACCI GENERATOR")
    print("=" * 45)
    
    try:
        terms = int(input("Enter the number of terms to generate: "))
        
        if terms <= 0:
            print("Please enter a positive integer.")
            return False
            
        a, b = 0, 1
        sequence = []
        
        for _ in range(terms):
            sequence.append(a)
            a, b = b, a + b
            
        print(f"\nFibonacci Sequence ({terms} terms):")
        print(", ".join(map(str, sequence)))
        return True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return False

if __name__ == "__main__":
    run_project_11()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 011_fibonacci_sequence_generator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Fibonacci Sequence Generator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
