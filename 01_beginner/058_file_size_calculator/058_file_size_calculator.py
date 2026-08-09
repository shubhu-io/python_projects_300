"""
Project 058: File Size Calculator
Category: File Handling
Description: Calculate size of a file in bytes, KB, MB (simulation).
"""
import os

def run_project_58():
    print("=" * 45)
    print("     PYTHON PROJECT 058: FILE SIZE CALCULATOR")
    print("=" * 45)
    
    file_path = input("Enter the file path: ").strip()
    
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return False
        
    size_bytes = os.path.getsize(file_path)
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    
    print("\n--- File Size ---")
    print(f"Bytes: {size_bytes}")
    print(f"KB: {size_kb:.2f}")
    print(f"MB: {size_mb:.2f}")
    return True

if __name__ == "__main__":
    run_project_58()
