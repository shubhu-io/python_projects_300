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
        except (EOFError, KeyboardInterrupt):
            print("\nExiting game.")
            break
            
    return True

if __name__ == "__main__":
    run_project_3()
