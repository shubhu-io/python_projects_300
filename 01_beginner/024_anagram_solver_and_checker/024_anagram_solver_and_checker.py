"""
Project 024: Anagram Solver and Checker
Category: Text & Strings
Description: Check if two words are anagrams.
"""

def run_project_24():
    print("=" * 45)
    print("    PYTHON PROJECT 024: ANAGRAM CHECKER")
    print("=" * 45)
    
    word1 = input("Enter first word: ").strip().lower().replace(" ", "")
    word2 = input("Enter second word: ").strip().lower().replace(" ", "")
    
    if not word1 or not word2:
        print("Invalid input.")
        return False
        
    is_anagram = sorted(word1) == sorted(word2)
    
    if is_anagram:
        print(f"\nYes! '{word1}' and '{word2}' are anagrams.")
    else:
        print(f"\nNo, '{word1}' and '{word2}' are not anagrams.")
        
    return True

if __name__ == "__main__":
    run_project_24()
