"""
Project 023: Vowel and Consonant Counter
Category: Text & Strings
Description: Count vowels and consonants in a string.
"""

def run_project_23():
    print("=" * 45)
    print("  PYTHON PROJECT 023: VOWEL & CONSONANT COUNTER")
    print("=" * 45)
    
    text = input("Enter a string: ").strip().lower()
    
    vowels = "aeiou"
    v_count = 0
    c_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
    print("\n--- Analysis ---")
    print(f"Vowels: {v_count}")
    print(f"Consonants: {c_count}")
    return True

if __name__ == "__main__":
    run_project_23()
