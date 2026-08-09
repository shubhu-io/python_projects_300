"""
Project 088: Simple Word Searcher
Category: Text & Strings
Description: Find the number of occurrences of a specific word in a text.
"""

def run_project_88():
    print("=" * 45)
    print("      PYTHON PROJECT 088: SIMPLE WORD SEARCH")
    print("=" * 45)
    
    text = input("Enter a long text block: ").lower()
    word = input("Enter the word to search for: ").strip().lower()
    
    if not text or not word:
        return False
        
    count = text.split().count(word)
    
    print(f"\nFound the word '{word}' exactly {count} times as a full word.")
    return True

if __name__ == "__main__":
    run_project_88()
