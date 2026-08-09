"""
Project 057: Duplicate Word Remover
Category: Text & Strings
Description: Remove duplicate words from a string while preserving order.
"""

def run_project_57():
    print("=" * 45)
    print("    PYTHON PROJECT 057: DUPLICATE WORD REMOVER")
    print("=" * 45)
    
    text = input("Enter a sentence with duplicate words: ").strip()
    
    if not text:
        return False
        
    words = text.split()
    seen = set()
    result = []
    
    for word in words:
        if word.lower() not in seen:
            seen.add(word.lower())
            result.append(word)
            
    print("\n--- Result ---")
    print(" ".join(result))
    return True

if __name__ == "__main__":
    run_project_57()
