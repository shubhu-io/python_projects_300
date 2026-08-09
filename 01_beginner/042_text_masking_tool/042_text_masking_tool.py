"""
Project 042: Text Masking Tool
Category: Text & Strings
Description: Mask sensitive information (like passwords) with asterisks.
"""

def run_project_42():
    print("=" * 45)
    print("      PYTHON PROJECT 042: TEXT MASKING TOOL")
    print("=" * 45)
    
    text = input("Enter sensitive information (e.g. credit card): ").strip()
    
    if len(text) <= 4:
        print(f"Masked: {'*' * len(text)}")
    else:
        visible = text[-4:]
        masked_part = '*' * (len(text) - 4)
        print(f"Masked: {masked_part}{visible}")
        
    return True

if __name__ == "__main__":
    run_project_42()
