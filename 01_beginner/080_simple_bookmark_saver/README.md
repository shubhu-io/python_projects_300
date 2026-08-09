# 🚀 Simple Bookmark Saver

## 📝 Description
Save URLs to a text file.

### 🎯 Category
**File Handling**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
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
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 080_simple_bookmark_saver.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Bookmark Saver in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
