# 🚀 Simple Word Frequency Graph

## 📝 Description
Print a text-based bar graph of word frequency.

### 🎯 Category
**Text & Analytics**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Loops (`for`/`while`)
- User Input

## 💻 Source Code
```python
"""
Project 095: Simple Word Frequency Graph
Category: Text & Analytics
Description: Print a text-based bar graph of word frequency.
"""

def run_project_95():
    print("=" * 45)
    print("    PYTHON PROJECT 095: WORD FREQ GRAPH")
    print("=" * 45)
    
    text = input("Enter a sentence: ").lower()
    if not text:
        return False
        
    words = text.split()
    freq = {}
    
    for w in words:
        # Clean basic punctuation
        w = w.strip(".,!?\"'")
        if w:
            freq[w] = freq.get(w, 0) + 1
            
    print("\n--- Word Frequency ---")
    for w, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{w:<15} | {'#' * count} ({count})")
        
    return True

if __name__ == "__main__":
    run_project_95()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 095_simple_word_frequency_graph.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Word Frequency Graph in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
