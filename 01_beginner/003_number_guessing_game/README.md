# 🚀 Number Guessing Game

## 📝 Description
User guesses a randomly generated number.

### 🎯 Category
**Games**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 003: Number Guessing Game
Category: Games
Description: User guesses a randomly generated number.
"""
import random

def run_project_3():
    print("=" * 45)
    print("     PYTHON PROJECT 003: NUMBER GUESSING")
    print("=" * 45)
    
    target = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")
            
    return True

if __name__ == "__main__":
    run_project_3()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 003_number_guessing_game.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Number Guessing Game in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
