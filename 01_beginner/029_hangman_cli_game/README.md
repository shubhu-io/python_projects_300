# 🚀 Hangman CLI Game

## 📝 Description
A simple command-line hangman game.

### 🎯 Category
**Games**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Comprehensions

## 💻 Source Code
```python
"""
Project 029: Hangman CLI Game
Category: Games
Description: A simple command-line hangman game.
"""
import random

def run_project_29():
    print("=" * 45)
    print("       PYTHON PROJECT 029: HANGMAN CLI")
    print("=" * 45)
    
    words = ['python', 'programming', 'developer', 'algorithm', 'function']
    word = random.choice(words)
    guessed = set()
    attempts = 6
    
    while attempts > 0:
        display = "".join([c if c in guessed else "_" for c in word])
        print(f"\nWord: {display}")
        print(f"Attempts left: {attempts}")
        
        if display == word:
            print("Congratulations! You guessed the word!")
            return True
            
        guess = input("Guess a letter: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed:
            print("You already guessed that letter!")
        elif guess in word:
            guessed.add(guess)
            print("Good guess!")
        else:
            guessed.add(guess)
            attempts -= 1
            print("Wrong guess!")
            
    print(f"\nGame Over! The word was: {word}")
    return True

if __name__ == "__main__":
    run_project_29()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 029_hangman_cli_game.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Hangman CLI Game in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
