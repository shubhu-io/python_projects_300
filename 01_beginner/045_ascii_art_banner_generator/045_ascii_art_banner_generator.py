"""
Project 045: ASCII Art Banner Generator
Category: Text & Strings
Description: Create simple text banners.
"""

def run_project_45():
    print("=" * 45)
    print("    PYTHON PROJECT 045: ASCII ART BANNER")
    print("=" * 45)
    
    text = input("Enter text for the banner: ").strip()
    
    if not text:
        return False
        
    width = len(text) + 6
    print("\n" + "=" * width)
    print(f"== {text} ==")
    print("=" * width + "\n")
    
    return True

if __name__ == "__main__":
    run_project_45()
