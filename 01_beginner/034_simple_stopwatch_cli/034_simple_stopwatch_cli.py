"""
Project 034: Simple Stopwatch CLI
Category: CLI & Utilities
Description: A basic stopwatch that counts elapsed time.
"""
import time

def run_project_34():
    print("=" * 45)
    print("    PYTHON PROJECT 034: SIMPLE STOPWATCH CLI")
    print("=" * 45)
    
    print("Press ENTER to start the stopwatch.")
    print("Press ENTER again to stop.")
    
    input("Ready? [Press Enter]")
    start_time = time.time()
    print("Stopwatch started...")
    
    input("[Press Enter to stop]")
    end_time = time.time()
    
    elapsed = end_time - start_time
    print(f"\nElapsed Time: {elapsed:.2f} seconds")
    return True

if __name__ == "__main__":
    run_project_34()
