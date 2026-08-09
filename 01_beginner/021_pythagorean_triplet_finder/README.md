# 🚀 Pythagorean Triplet Finder

## 📝 Description
Find Pythagorean triplets up to a given limit.

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
Project 021: Pythagorean Triplet Finder
Category: Math & Logic
Description: Find Pythagorean triplets up to a given limit.
"""

def run_project_21():
    print("=" * 45)
    print("  PYTHON PROJECT 021: PYTHAGOREAN TRIPLETS")
    print("=" * 45)
    
    try:
        limit = int(input("Enter a limit for the hypotenuse: "))
        
        if limit < 5:
            print("Limit must be at least 5.")
            return False
            
        triplets = []
        for c in range(5, limit + 1):
            for b in range(4, c):
                for a in range(3, b):
                    if a*a + b*b == c*c:
                        triplets.append((a, b, c))
                        
        print(f"\nPythagorean triplets up to c={limit}:")
        for t in triplets:
            print(f"{t[0]}^2 + {t[1]}^2 = {t[2]}^2")
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_21()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 021_pythagorean_triplet_finder.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Pythagorean Triplet Finder in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
