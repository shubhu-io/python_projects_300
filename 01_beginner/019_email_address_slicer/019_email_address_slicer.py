"""
Project 019: Email Address Slicer
Category: Text & Strings
Description: Extract username and domain from an email address.
"""

def run_project_19():
    print("=" * 45)
    print("      PYTHON PROJECT 019: EMAIL ADDRESS SLICER")
    print("=" * 45)
    
    email = input("Enter an email address: ").strip()
    
    if "@" not in email:
        print("Error: Invalid email address format.")
        return False
        
    try:
        username, domain = email.split('@', 1)
        
        print("\n--- Slicer Results ---")
        print(f"Email: {email}")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        return True
    except ValueError:
        print("Error parsing the email.")
        return False

if __name__ == "__main__":
    run_project_19()
