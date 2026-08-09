"""
Project 059: Simple Voting System
Category: CLI & Utilities
Description: A basic voting poll application.
"""

def run_project_59():
    print("=" * 45)
    print("      PYTHON PROJECT 059: SIMPLE VOTING SYS")
    print("=" * 45)
    
    candidates = ["Alice", "Bob", "Charlie"]
    votes = {c: 0 for c in candidates}
    
    print("Candidates:", ", ".join(candidates))
    print("Type 'results' to end voting and see results.\n")
    
    while True:
        try:
            vote = input("Vote for a candidate: ").strip().title()
        except (EOFError, KeyboardInterrupt):
            break
        
        if vote.lower() == 'results':
            break
            
        if vote in candidates:
            votes[vote] += 1
            print("Vote counted.")
        else:
            print("Invalid candidate.")
            
    print("\n--- Voting Results ---")
    for c, v in votes.items():
        print(f"{c}: {v} vote(s)")
        
    return True

if __name__ == "__main__":
    run_project_59()
