"""
Project 033: Reverse String Tool
Category: Text & Strings
Description: Reverse a given string.
"""

def run_project_33():
    print("=" * 45)
    print("      PYTHON PROJECT 033: REVERSE STRING")
    print("=" * 45)
    
    text = input("Enter a string to reverse: ")
    
    reversed_text = text[::-1]
    
    print("\n--- Result ---")
    print(f"Original: {text}")
    print(f"Reversed: {reversed_text}")
    return True

if __name__ == "__main__":
    run_project_33()
