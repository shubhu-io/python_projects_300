"""
Project 071: ROT13 Cipher Tool
Category: Security & Text
Description: Encrypt/decrypt using ROT13.
"""

def run_project_71():
    print("=" * 45)
    print("      PYTHON PROJECT 071: ROT13 CIPHER")
    print("=" * 45)
    
    text = input("Enter text to apply ROT13: ")
    result = ""
    
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            result += char
            
    print(f"\nResult: {result}")
    return True

if __name__ == "__main__":
    run_project_71()
