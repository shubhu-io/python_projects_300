"""
Project 087: Base64 Encoder/Decoder
Category: Security & Utilities
Description: Encode or decode a string using Base64.
"""
import base64

def run_project_87():
    print("=" * 45)
    print("    PYTHON PROJECT 087: BASE64 ENCODER/DECODER")
    print("=" * 45)
    
    print("1. Encode")
    print("2. Decode")
    choice = input("Choice (1/2): ").strip()
    
    text = input("Enter string: ")
    
    try:
        if choice == '1':
            b64 = base64.b64encode(text.encode()).decode()
            print(f"\nEncoded: {b64}")
        elif choice == '2':
            plain = base64.b64decode(text.encode()).decode()
            print(f"\nDecoded: {plain}")
        else:
            print("Invalid choice.")
            return False
            
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    run_project_87()
