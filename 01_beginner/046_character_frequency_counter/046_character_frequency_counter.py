"""
Project 046: Character Frequency Counter
Category: Text & Strings
Description: Count frequency of each character in a string.
"""

def run_project_46():
    print("=" * 45)
    print("   PYTHON PROJECT 046: CHAR FREQUENCY COUNTER")
    print("=" * 45)
    
    text = input("Enter a string: ")
    freq = {}
    
    for char in text:
        if char.strip(): # Ignore spaces for display, or count them if desired
            freq[char] = freq.get(char, 0) + 1
            
    print("\n--- Frequency ---")
    for char, count in sorted(freq.items()):
        print(f"'{char}': {count}")
        
    return True

if __name__ == "__main__":
    run_project_46()
