"""
Project 072: Simple Expense Logger
Category: CLI & Utilities
Description: Log expenses to a text file.
"""
import datetime

def run_project_72():
    print("=" * 45)
    print("     PYTHON PROJECT 072: EXPENSE LOGGER")
    print("=" * 45)
    
    filename = "expenses_log.txt"
    item = input("Enter the expense description (or 'exit'): ").strip()
    
    if item.lower() == 'exit':
        return True
        
    try:
        cost = float(input("Enter the cost: $"))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(filename, 'a') as f:
            f.write(f"[{date}] {item}: ${cost:.2f}\n")
            
        print(f"\nLogged '{item}' for ${cost:.2f} to {filename}")
        return True
    except ValueError:
        print("Invalid cost.")
        return False

if __name__ == "__main__":
    run_project_72()
