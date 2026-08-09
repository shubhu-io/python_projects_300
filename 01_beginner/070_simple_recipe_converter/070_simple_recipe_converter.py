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
