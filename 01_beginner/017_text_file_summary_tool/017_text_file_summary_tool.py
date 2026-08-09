"""
Project 017: Text File Summary Tool
Category: File Handling
Description: Read a text file and output a summary of lines, words, etc.
"""
import os

def run_project_17():
    print("=" * 45)
    print("   PYTHON PROJECT 017: TEXT FILE SUMMARY TOOL")
    print("=" * 45)
    
    filename = input("Enter the path of the text file to analyze: ").strip()
    
    if not os.path.exists(filename):
        print("Error: File does not exist.")
        return False
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        
        print("\n--- File Summary ---")
        print(f"Total Lines: {num_lines}")
        print(f"Total Words: {num_words}")
        print(f"Total Characters: {num_chars}")
        return True
    except Exception as e:
        print(f"An error occurred reading the file: {e}")
        return False

if __name__ == "__main__":
    run_project_17()
