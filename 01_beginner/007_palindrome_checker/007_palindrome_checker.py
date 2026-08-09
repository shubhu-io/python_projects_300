"""
Project 007: Palindrome Checker
Category: Math & Logic
Description: Check if a given string is a palindrome.
"""
import re

def run_project_7():
    print("=" * 45)
    print("     PYTHON PROJECT 007: PALINDROME CHECKER")
    print("=" * 45)
    
    text = input("Enter a word or phrase: ").strip()
    
    # Remove non-alphanumeric chars and lowercase
    clean_text = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    
    if not clean_text:
        print("Invalid input.")
        return False
        
    is_palindrome = clean_text == clean_text[::-1]
    
    if is_palindrome:
        print(f"\n'{text}' IS a palindrome!")
    else:
        print(f"\n'{text}' is NOT a palindrome.")
        
    return True

if __name__ == "__main__":
    run_project_7()
