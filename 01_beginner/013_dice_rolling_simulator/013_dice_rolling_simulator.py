"""
Project 013: Dice Rolling Simulator
Category: Games & Random
Description: Simulates rolling dice.
"""
import random

def run_project_13():
    print("=" * 45)
    print("    PYTHON PROJECT 013: DICE ROLLING SIMULATOR")
    print("=" * 45)
    
    try:
        sides = int(input("Enter the number of sides on the dice (e.g., 6): "))
        rolls = int(input("Enter the number of dice to roll: "))
        
        if sides < 2 or rolls < 1:
            print("Invalid inputs. Must have at least 2 sides and 1 roll.")
            return False
            
        results = [random.randint(1, sides) for _ in range(rolls)]
        
        print(f"\nYou rolled {rolls} dice with {sides} sides:")
        print("Results:", ", ".join(map(str, results)))
        print("Total Sum:", sum(results))
        return True
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return False

if __name__ == "__main__":
    run_project_13()
