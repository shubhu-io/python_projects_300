"""
Project 083: Simple Random Quote Generator
Category: Utilities & Text
Description: Display a random quote from a predefined list.
"""
import random

def run_project_83():
    print("=" * 45)
    print("     PYTHON PROJECT 083: RANDOM QUOTE GEN")
    print("=" * 45)
    
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "Get busy living or get busy dying. - Stephen King",
        "You only live once, but if you do it right, once is enough. - Mae West",
        "In the middle of difficulty lies opportunity. - Albert Einstein"
    ]
    
    input("Press Enter to get inspired...")
    print("\n" + "=" * 10 + " QUOTE " + "=" * 10)
    print(random.choice(quotes))
    print("=" * 27)
    
    return True

if __name__ == "__main__":
    run_project_83()
