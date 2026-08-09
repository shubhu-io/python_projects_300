"""
Project 063: Text Alignment Utility
Category: Text & Strings
Description: Align text to left, right, or center.
"""

def run_project_63():
    print("=" * 45)
    print("     PYTHON PROJECT 063: TEXT ALIGNMENT")
    print("=" * 45)
    
    text = input("Enter a short string: ")
    try:
        width = int(input("Enter terminal width (e.g., 40): "))
        
        print("\n--- Left Aligned ---")
        print(text.ljust(width, '-'))
        
        print("\n--- Center Aligned ---")
        print(text.center(width, '-'))
        
        print("\n--- Right Aligned ---")
        print(text.rjust(width, '-'))
        
        return True
    except ValueError:
        print("Invalid width.")
        return False

if __name__ == "__main__":
    run_project_63()
