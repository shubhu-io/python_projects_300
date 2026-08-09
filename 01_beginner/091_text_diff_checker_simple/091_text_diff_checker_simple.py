"""
Project 091: Text Diff Checker Simple
Category: Text & Strings
Description: Compare two strings for differences.
"""

def run_project_91():
    print("=" * 45)
    print("      PYTHON PROJECT 091: TEXT DIFF CHECKER")
    print("=" * 45)
    
    text1 = input("Enter first string: ")
    text2 = input("Enter second string: ")
    
    if text1 == text2:
        print("\nThe strings are exactly identical.")
        return True
        
    print("\nThe strings are different.")
    
    words1 = text1.split()
    words2 = text2.split()
    
    diff = set(words1) ^ set(words2)
    
    if diff:
        print("Words that are not in both strings:")
        for w in diff:
            print(f"- {w}")
    else:
        print("They contain the same words, but perhaps in a different order or with different spacing.")
        
    return True

if __name__ == "__main__":
    run_project_91()
