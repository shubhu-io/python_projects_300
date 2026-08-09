"""
Project 080: Simple Bookmark Saver
Category: File Handling
Description: Save URLs to a text file.
"""

def run_project_80():
    print("=" * 45)
    print("      PYTHON PROJECT 080: BOOKMARK SAVER")
    print("=" * 45)
    
    filename = "bookmarks.txt"
    url = input("Enter a URL to bookmark (or 'exit'): ").strip()
    
    if url.lower() == 'exit':
        return True
        
    title = input("Enter a title for this bookmark: ").strip()
    
    try:
        with open(filename, 'a') as f:
            f.write(f"{title}: {url}\n")
            
        print(f"\nSaved bookmark '{title}' to {filename}")
        return True
    except Exception as e:
        print(f"Error saving bookmark: {e}")
        return False

if __name__ == "__main__":
    run_project_80()
