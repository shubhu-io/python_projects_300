"""
Project 054: Text Case Converter
Category: Text & Strings
Description: Convert string to UPPERCASE, lowercase, and Title Case.
"""

def run_project_54():
    print("=" * 45)
    print("     PYTHON PROJECT 054: TEXT CASE CONVERTER")
    print("=" * 45)
    
    text = input("Enter a string: ")
    
    print("\n--- Conversions ---")
    print(f"UPPERCASE: {text.upper()}")
    print(f"lowercase: {text.lower()}")
    print(f"Title Case: {text.title()}")
    print(f"sWAP cASE: {text.swapcase()}")
    return True

if __name__ == "__main__":
    run_project_54()
