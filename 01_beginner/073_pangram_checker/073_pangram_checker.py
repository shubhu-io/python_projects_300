"""
Project 073: Pangram Checker
Category: Text & Strings
Description: Check if a sentence contains every letter of the alphabet.
"""
import string

def run_project_73():
    print("=" * 45)
    print("      PYTHON PROJECT 073: PANGRAM CHECKER")
    print("=" * 45)
    
    text = input("Enter a sentence to check: ").lower()
    
    alphabet = set(string.ascii_lowercase)
    letters_in_text = set(char for char in text if char in alphabet)
    
    if alphabet == letters_in_text:
        print("\nYes! This sentence is a pangram.")
    else:
        missing = alphabet - letters_in_text
        print("\nNo, this is not a pangram.")
        print(f"Missing letters: {', '.join(sorted(missing))}")
        
    return True

if __name__ == "__main__":
    run_project_73()
