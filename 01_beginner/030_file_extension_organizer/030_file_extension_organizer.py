"""
Project 030: File Extension Organizer
Category: File Handling
Description: Analyze extensions in a directory (simulation).
"""
import os

def run_project_30():
    print("=" * 45)
    print("    PYTHON PROJECT 030: EXTENSION ORGANIZER")
    print("=" * 45)
    
    folder = input("Enter directory path to analyze (or '.' for current): ").strip()
    
    if not os.path.isdir(folder):
        print("Invalid directory path.")
        return False
        
    ext_count = {}
    try:
        for item in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, item)):
                _, ext = os.path.splitext(item)
                ext = ext.lower() if ext else "No Extension"
                ext_count[ext] = ext_count.get(ext, 0) + 1
                
        print("\n--- File Extensions Found ---")
        for ext, count in sorted(ext_count.items()):
            print(f"{ext}: {count} file(s)")
            
        return True
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return False

if __name__ == "__main__":
    run_project_30()
