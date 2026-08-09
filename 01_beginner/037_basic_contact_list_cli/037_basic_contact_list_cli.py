"""
Project 037: Basic Contact List CLI
Category: CLI & Utilities
Description: Store and retrieve simple contacts during the session.
"""

def run_project_37():
    print("=" * 45)
    print("    PYTHON PROJECT 037: BASIC CONTACT LIST")
    print("=" * 45)
    
    contacts = {}
    
    while True:
        print("\n--- Menu ---")
        print("1. Add/Update Contact")
        print("2. Search Contact")
        print("3. List All Contacts")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            contacts[name] = phone
            print(f"Contact '{name}' saved.")
        elif choice == '2':
            name = input("Search Name: ").strip()
            if name in contacts:
                print(f"Phone: {contacts[name]}")
            else:
                print("Contact not found.")
        elif choice == '3':
            if not contacts:
                print("Contact list is empty.")
            else:
                for name, phone in sorted(contacts.items()):
                    print(f"{name}: {phone}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            
    return True

if __name__ == "__main__":
    run_project_37()
