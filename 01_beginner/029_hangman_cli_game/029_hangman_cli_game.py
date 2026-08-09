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
