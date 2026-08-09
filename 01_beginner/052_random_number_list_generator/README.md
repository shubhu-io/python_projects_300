# 🚀 Random Number List Generator

## 📝 Description
Generate a list of random numbers.

### 🎯 Category
**Utilities & Math**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Comprehensions
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 052: Random Number List Generator
Category: Utilities & Math
Description: Generate a list of random numbers.
"""
import random

def run_project_52():
    print("=" * 45)
    print("   PYTHON PROJECT 052: RANDOM NUMBER LIST")
    print("=" * 45)
    
    try:
        count = int(input("How many random numbers? "))
        start = int(input("Enter minimum value: "))
        end = int(input("Enter maximum value: "))
        
        if count <= 0 or start > end:
            print("Invalid range or count.")
            return False
            
        numbers = [random.randint(start, end) for _ in range(count)]
        
        print(f"\nGenerated {count} random numbers:")
        print(numbers)
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_52()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 052_random_number_list_generator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Random Number List Generator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
