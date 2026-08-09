"""
    Project 005: Word and Text Analyzer
Category: Text & Strings
Description: Count characters, words, and sentences in a given text.
"""

def run_project_5():
    print("=" * 45)
    print("   PYTHON PROJECT 005: WORD & TEXT ANALYZER")
    print("=" * 45)
    
    text = input("Enter some text to analyze:\n").strip()
    if not text:
        print("No text provided.")
        return False
        
    chars = len(text)
    words = len(text.split())
    # Basic sentence counting by punctuation
    sentences = max(1, text.count('.') + text.count('!') + text.count('?'))
    
    print("\n--- Analysis Results ---")
    print(f"Characters (with spaces): {chars}")
    print(f"Words: {words}")
    print(f"Sentences: {sentences}")
    return True

if __name__ == "__main__":
    run_project_5()
