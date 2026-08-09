"""
Project 043: Simple Countdown Timer
Category: Utilities
Description: A basic countdown timer.
"""
import time
import sys

def run_project_43():
    print("=" * 45)
    print("    PYTHON PROJECT 043: SIMPLE COUNTDOWN TIMER")
    print("=" * 45)
    
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        
        if seconds <= 0:
            print("Must be positive.")
            return False
            
        print("\nStarting countdown...")
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            sys.stdout.write(f"\r{timer}")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
            
        print("\n\nTIME IS UP!")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_43()
