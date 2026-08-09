"""
Project 006: Random Password Generator
Category: Security & Utilities
Description: Generate a strong random password.
"""
import random
import string

def run_project_6():
    print("=" * 45)
    print(" PYTHON PROJECT 006: RANDOM PASSWORD GENERATOR")
    print("=" * 45)
    
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length < 4:
            print("Password should be at least 4 characters.")
            return False
            
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        chars = string.ascii_letters + string.digits
        if use_special:
            chars += string.punctuation
            
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"\nGenerated Password: {password}")
        return True
    except ValueError:
        print("Invalid length provided.")
        return False

if __name__ == "__main__":
    run_project_6()
