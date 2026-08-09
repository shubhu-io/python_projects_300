"""
Project 052: Random Number List Generator
Category: Utilities & Math
Description: Generate a list of random numbers.
"""
import random

def run_project_52():
    print("=" * 45)
    print("   PYTHON PROJECT 052: RANDOM NUMBER LIST")
    print("=" * 45)
    
    try:
        count = int(input("How many random numbers? "))
        start = int(input("Enter minimum value: "))
        end = int(input("Enter maximum value: "))
        
        if count <= 0 or start > end:
            print("Invalid range or count.")
            return False
            
        numbers = [random.randint(start, end) for _ in range(count)]
        
        print(f"\nGenerated {count} random numbers:")
        print(numbers)
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_52()
