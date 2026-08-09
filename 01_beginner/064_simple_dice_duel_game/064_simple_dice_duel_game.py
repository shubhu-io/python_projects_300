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
