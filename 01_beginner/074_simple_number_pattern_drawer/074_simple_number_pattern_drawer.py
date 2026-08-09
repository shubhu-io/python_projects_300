"""
Project 074: Simple Number Pattern Drawer
Category: CLI & Utilities
Description: Draw a pyramid pattern of numbers.
"""

def run_project_74():
    print("=" * 45)
    print("   PYTHON PROJECT 074: NUMBER PATTERN DRAWER")
    print("=" * 45)
    
    try:
        rows = int(input("Enter number of rows for the pyramid: "))
        
        print("\n--- Pattern ---")
        for i in range(1, rows + 1):
            # Print spaces
            print(" " * (rows - i), end="")
            # Print numbers
            for j in range(1, i + 1):
                print(f"{j} ", end="")
            print()
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_74()
