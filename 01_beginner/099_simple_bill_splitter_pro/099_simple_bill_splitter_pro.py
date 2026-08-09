"""
Project 099: Simple Bill Splitter Pro
Category: Finance & Utilities
Description: Split bill unevenly among friends.
"""

def run_project_99():
    print("=" * 45)
    print("    PYTHON PROJECT 099: BILL SPLITTER PRO")
    print("=" * 45)
    
    friends = {}
    total_bill = 0
    
    print("Enter the names and amounts each person owes.")
    print("Type 'done' when finished.")
    
    while True:
        name = input("Name: ").strip().title()
        if name.lower() == 'done':
            break
            
        try:
            amount = float(input(f"Amount {name} owes: $"))
            friends[name] = friends.get(name, 0) + amount
            total_bill += amount
        except ValueError:
            print("Invalid amount.")
            
    if not friends:
        print("No one owes anything.")
        return False
        
    print("\n--- Summary ---")
    print(f"Total Bill: ${total_bill:.2f}")
    for n, a in friends.items():
        print(f"- {n} pays: ${a:.2f}")
        
    return True

if __name__ == "__main__":
    run_project_99()
