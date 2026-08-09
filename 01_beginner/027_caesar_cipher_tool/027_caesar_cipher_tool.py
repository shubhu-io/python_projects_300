"""
Project 027: Caesar Cipher Tool
Category: Security & Text
Description: Encrypt and decrypt text using a Caesar cipher.
"""

def run_project_27():
    print("=" * 45)
    print("      PYTHON PROJECT 027: CAESAR CIPHER")
    print("=" * 45)
    
    mode = input("Select mode (e)ncrypt or (d)ecrypt: ").strip().lower()
    if mode not in ['e', 'd']:
        print("Invalid mode.")
        return False
        
    text = input("Enter the message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return False
        
    if mode == 'd':
        shift = -shift
        
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
            
    print(f"\nResult: {result}")
    return True

if __name__ == "__main__":
    run_project_27()
