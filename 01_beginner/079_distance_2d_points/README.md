# 🚀 Distance 2D Points

## 📝 Description
Calculate distance between two 2D points.

### 🎯 Category
**Math & Logic**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 079: Distance 2D Points
Category: Math & Logic
Description: Calculate distance between two 2D points.
"""
import math

def run_project_79():
    print("=" * 45)
    print("      PYTHON PROJECT 079: 2D POINT DISTANCE")
    print("=" * 45)
    
    try:
        print("Point 1:")
        x1 = float(input("  x1: "))
        y1 = float(input("  y1: "))
        print("Point 2:")
        x2 = float(input("  x2: "))
        y2 = float(input("  y2: "))
        
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        print(f"\nThe distance between ({x1}, {y1}) and ({x2}, {y2}) is: {dist:.4f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_79()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 079_distance_2d_points.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Distance 2D Points in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
