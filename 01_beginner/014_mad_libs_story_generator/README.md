# 🚀 Mad Libs Story Generator

## 📝 Description
Fills placeholders in stories with custom user words.

### 🎯 Category
**Text & Strings**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- User Input

## 💻 Source Code
```python
"""
Project 014: Mad Libs Story Generator
Category: Text & Strings
Description: Fills placeholders in stories with custom user words.
"""

def run_project_14():
    print("=" * 45)
    print("    PYTHON PROJECT 014: MAD LIBS GENERATOR")
    print("=" * 45)
    
    print("Please provide the following words:")
    noun1 = input("A noun: ").strip()
    adjective = input("An adjective: ").strip()
    verb = input("A past-tense verb: ").strip()
    place = input("A place: ").strip()
    noun2 = input("Another noun: ").strip()
    
    story = f"""
    One day, a {adjective} {noun1} went to the {place}.
    While there, it {verb} a completely normal {noun2}.
    Everyone was very surprised!
    """
    
    print("\nHere is your Mad Libs Story:")
    print("-" * 30)
    print(story.strip())
    print("-" * 30)
    return True

if __name__ == "__main__":
    run_project_14()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 014_mad_libs_story_generator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Mad Libs Story Generator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
