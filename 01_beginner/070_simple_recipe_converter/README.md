# 🚀 Simple Recipe Converter

## 📝 Description
Scale ingredients based on number of servings.

### 🎯 Category
**Utilities**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 070: Simple Recipe Converter
Category: Utilities
Description: Scale ingredients based on number of servings.
"""

def run_project_70():
    print("=" * 45)
    print("     PYTHON PROJECT 070: RECIPE SCALER")
    print("=" * 45)
    
    recipe = {
        "Flour (cups)": 2.0,
        "Sugar (cups)": 1.0,
        "Eggs": 3.0,
        "Butter (tbsp)": 4.0
    }
    
    original_servings = 4
    print("Original Recipe (Serves 4):")
    for item, qty in recipe.items():
        print(f"- {item}: {qty}")
        
    try:
        new_servings = float(input("\nEnter desired number of servings: "))
        
        ratio = new_servings / original_servings
        
        print(f"\nScaled Recipe (Serves {new_servings}):")
        for item, qty in recipe.items():
            print(f"- {item}: {qty * ratio:.2f}")
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_70()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 070_simple_recipe_converter.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Recipe Converter in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
