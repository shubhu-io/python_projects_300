"""
Project 001: Hello World Plus
Category: CLI & Utilities
Description: Enhanced greeting generator with time-based greetings.
"""
import datetime

def run_project_1():
    print("=" * 45)
    print("       PYTHON PROJECT 001: HELLO WORLD PLUS")
    print("=" * 45)
    
    name = input("Enter your name: ").strip()
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
        
    print(f"\n{greeting}, {name}! Welcome to your Python journey.")
    return True

if __name__ == "__main__":
    run_project_1()
