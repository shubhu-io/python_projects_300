"""
Project 095: Simple Word Frequency Graph
Category: Text & Analytics
Description: Print a text-based bar graph of word frequency.
"""

def run_project_95():
    print("=" * 45)
    print("    PYTHON PROJECT 095: WORD FREQ GRAPH")
    print("=" * 45)
    
    text = input("Enter a sentence: ").lower()
    if not text:
        return False
        
    words = text.split()
    freq = {}
    
    for w in words:
        # Clean basic punctuation
        w = w.strip(".,!?\"'")
        if w:
            freq[w] = freq.get(w, 0) + 1
            
    print("\n--- Word Frequency ---")
    for w, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{w:<15} | {'#' * count} ({count})")
        
    return True

if __name__ == "__main__":
    run_project_95()
