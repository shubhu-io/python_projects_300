"""
Project 067: Random Name Picker
Category: Utilities & Games
Description: Pick a random name from a provided list.
"""
import random

def run_project_67():
    print("=" * 45)
    print("      PYTHON PROJECT 067: RANDOM NAME PICKER")
    print("=" * 45)
    
    names_str = input("Enter names separated by commas:\n").strip()
    
    if not names_str:
        print("No names provided.")
        return False
        
    names = [n.strip() for n in names_str.split(',') if n.strip()]
    
    if not names:
        print("No valid names found.")
        return False
        
    winner = random.choice(names)
    print(f"\nAnd the winner is... {winner}!")
    return True

if __name__ == "__main__":
    run_project_67()
