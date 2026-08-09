"""
Project 076: Word Wrapper Utility
Category: Text & Strings
Description: Wrap text to a specific width.
"""
import textwrap

def run_project_76():
    print("=" * 45)
    print("       PYTHON PROJECT 076: WORD WRAPPER")
    print("=" * 45)
    
    text = input("Enter a long string of text: ")
    try:
        width = int(input("Enter max line width: "))
        
        print(f"\n--- Wrapped Text (Width: {width}) ---")
        wrapped = textwrap.fill(text, width=width)
        print(wrapped)
        
        return True
    except ValueError:
        print("Invalid width.")
        return False

if __name__ == "__main__":
    run_project_76()
