# 🚀 Simple Voting System

## 📝 Description
A basic voting poll application.

### 🎯 Category
**CLI & Utilities**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Functions & Modular Code
- Comprehensions

## 💻 Source Code
```python
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
        vote = input("Vote for a candidate: ").strip().title()
        
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
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 059_simple_voting_system.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Voting System in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
