"""
Project 078: Basic Encryption XOR
Category: Security
Description: Encrypt and decrypt a string using XOR.
"""

def run_project_78():
    print("=" * 45)
    print("       PYTHON PROJECT 078: XOR ENCRYPTION")
    print("=" * 45)
    
    text = input("Enter text to encrypt/decrypt: ")
    try:
        key = int(input("Enter a numeric key (0-255): "))
        if not (0 <= key <= 255):
            print("Key out of range.")
            return False
            
        result = "".join(chr(ord(c) ^ key) for c in text)
        
        print(f"\nResult (can contain unprintable chars): {result}")
        print(f"Hex representation: {result.encode().hex()}")
        return True
    except ValueError:
        print("Invalid key.")
        return False

if __name__ == "__main__":
    run_project_78()
