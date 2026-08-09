"""
Project 038: Simple Note Saver
Category: File Handling
Description: Save short notes to a text file.
"""
import os

def run_project_38():
    print("=" * 45)
    print("      PYTHON PROJECT 038: SIMPLE NOTE SAVER")
    print("=" * 45)
    
    filename = "my_notes.txt"
    
    print("Enter your note (or type 'EXIT' to quit):")
    note = input("> ")
    
    if note.strip().upper() == 'EXIT':
        print("Cancelled.")
        return True
        
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(note + "\n")
        print(f"\nNote saved to {filename} successfully.")
        return True
    except Exception as e:
        print(f"Failed to save note: {e}")
        return False

if __name__ == "__main__":
    run_project_38()
