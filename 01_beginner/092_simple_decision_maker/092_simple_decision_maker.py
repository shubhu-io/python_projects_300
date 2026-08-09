"""
Project 092: Simple Decision Maker
Category: CLI & Utilities
Description: Input options and randomly choose one.
"""
import random

def run_project_92():
    print("=" * 45)
    print("      PYTHON PROJECT 092: DECISION MAKER")
    print("=" * 45)
    
    print("Enter options one by one. Type 'done' when finished.")
    options = []
    
    while True:
        try:
            opt = input("Option: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if opt.lower() == 'done':
            break
        if opt:
            options.append(opt)
            
    if not options:
        print("No options provided. Cannot make a decision.")
        return False
        
    print("\nThinking...")
    winner = random.choice(options)
    print(f"\nThe Decision Maker has chosen: {winner.upper()}")
    
    return True

if __name__ == "__main__":
    run_project_92()
