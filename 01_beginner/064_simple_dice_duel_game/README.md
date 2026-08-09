# 🚀 Simple Dice Duel Game

## 📝 Description
A simple dice game against the computer.

### 🎯 Category
**Games & Random**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Module Importing
- User Input

## 💻 Source Code
```python
"""
Project 064: Simple Dice Duel Game
Category: Games & Random
Description: A simple dice game against the computer.
"""
import random

def run_project_64():
    print("=" * 45)
    print("      PYTHON PROJECT 064: DICE DUEL GAME")
    print("=" * 45)
    
    input("Press Enter to roll your dice...")
    player_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)
    
    print(f"You rolled: {player_roll}")
    print(f"Computer rolled: {comp_roll}")
    
    if player_roll > comp_roll:
        print("You win!")
    elif player_roll < comp_roll:
        print("Computer wins!")
    else:
        print("It's a tie!")
        
    return True

if __name__ == "__main__":
    run_project_64()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 064_simple_dice_duel_game.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Dice Duel Game in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
