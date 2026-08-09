# 🚀 Rock Paper Scissors

## 📝 Description
Play the classic game against the computer.

### 🎯 Category
**Games**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Module Importing
- User Input

## 💻 Source Code
```python
"""
Project 010: Rock Paper Scissors
Category: Games
Description: Play the classic game against the computer.
"""
import random

def run_project_10():
    print("=" * 45)
    print("    PYTHON PROJECT 010: ROCK PAPER SCISSORS")
    print("=" * 45)
    
    choices = ['rock', 'paper', 'scissors']
    
    user = input("Choose rock, paper, or scissors: ").strip().lower()
    if user not in choices:
        print("Invalid choice. Must be rock, paper, or scissors.")
        return False
        
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")
    
    if user == comp:
        print("It's a tie!")
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
        
    return True

if __name__ == "__main__":
    run_project_10()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 010_rock_paper_scissors.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Rock Paper Scissors in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
