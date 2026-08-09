"""
Project 086: Simple URL Encoder/Decoder
Category: Web & Utilities
Description: URL encode or decode a string.
"""
import urllib.parse

def run_project_86():
    print("=" * 45)
    print("    PYTHON PROJECT 086: URL ENCODER/DECODER")
    print("=" * 45)
    
    print("1. Encode")
    print("2. Decode")
    choice = input("Choice (1/2): ").strip()
    
    text = input("Enter string: ")
    
    if choice == '1':
        print(f"\nEncoded: {urllib.parse.quote(text)}")
    elif choice == '2':
        print(f"\nDecoded: {urllib.parse.unquote(text)}")
    else:
        print("Invalid choice.")
        return False
        
    return True

if __name__ == "__main__":
    run_project_86()
