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
