"""
Project 060: Basic Password Strength Meter
Category: Security & Text
Description: Check password strength based on length, digits, and cases.
"""

def run_project_60():
    print("=" * 45)
    print("    PYTHON PROJECT 060: PASSWORD STRENGTH")
    print("=" * 45)
    
    pwd = input("Enter a password to test: ")
    
    score = 0
    if len(pwd) >= 8:
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.islower() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*()-_+=<>?/\\|~{}[]," for c in pwd):
        score += 1
        
    print("\n--- Result ---")
    if score < 3:
        print("Strength: Weak")
    elif score < 5:
        print("Strength: Medium")
    else:
        print("Strength: Strong")
        
    return True

if __name__ == "__main__":
    run_project_60()
