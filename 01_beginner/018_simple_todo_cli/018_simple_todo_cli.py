"""
Project 018: Simple Todo CLI
Category: CLI & Utilities
Description: Manage a simple to-do list in memory during the session.
"""

def run_project_18():
    print("=" * 45)
    print("        PYTHON PROJECT 018: SIMPLE TODO CLI")
    print("=" * 45)
    
    todos = []
    
    while True:
        print("\n--- To-Do Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            if not todos:
                print("Your to-do list is empty.")
            else:
                for i, task in enumerate(todos, 1):
                    print(f"{i}. {task}")
        elif choice == '2':
            task = input("Enter the new task: ").strip()
            if task:
                todos.append(task)
                print("Task added!")
        elif choice == '3':
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting To-Do CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")
            
    return True

if __name__ == "__main__":
    run_project_18()
