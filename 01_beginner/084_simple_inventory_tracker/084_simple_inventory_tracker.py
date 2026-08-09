"""
Project 084: Simple Inventory Tracker
Category: CLI & Utilities
Description: Track items and quantities.
"""

def run_project_84():
    print("=" * 45)
    print("     PYTHON PROJECT 084: INVENTORY TRACKER")
    print("=" * 45)
    
    inventory = {}
    
    while True:
        print("\n1. Add/Update Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Exit")
        
        choice = input("Choice: ").strip()
        
        if choice == '1':
            item = input("Item Name: ").title()
            try:
                qty = int(input("Quantity: "))
                inventory[item] = inventory.get(item, 0) + qty
                print(f"Updated {item}.")
            except ValueError:
                print("Invalid quantity.")
        elif choice == '2':
            item = input("Item to remove: ").title()
            if item in inventory:
                del inventory[item]
                print(f"Removed {item}.")
            else:
                print("Item not found.")
        elif choice == '3':
            if not inventory:
                print("Inventory empty.")
            else:
                for k, v in inventory.items():
                    print(f"{k}: {v}")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
            
    return True

if __name__ == "__main__":
    run_project_84()
