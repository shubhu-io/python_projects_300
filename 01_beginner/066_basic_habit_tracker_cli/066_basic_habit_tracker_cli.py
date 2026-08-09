"""
Project 066: Basic Habit Tracker CLI
Category: CLI & Utilities
Description: Simple daily habit checklist during a session.
"""

def run_project_66():
    print("=" * 45)
    print("     PYTHON PROJECT 066: BASIC HABIT TRACKER")
    print("=" * 45)
    
    habits = ["Drink Water", "Exercise", "Read 10 Pages", "Meditate"]
    status = {h: False for h in habits}
    
    while True:
        print("\n--- Daily Habits ---")
        for i, h in enumerate(habits, 1):
            check = "[X]" if status[h] else "[ ]"
            print(f"{i}. {check} {h}")
            
        print("5. Exit")
        
        choice = input("\nEnter number to toggle status (or 5 to exit): ").strip()
        
        if choice == '5':
            break
            
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(habits):
                habit_name = habits[idx]
                status[habit_name] = not status[habit_name]
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")
            
    return True

if __name__ == "__main__":
    run_project_66()
