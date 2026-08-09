# 🚀 Trivia Quiz Game

## 📝 Description
A simple command-line trivia quiz.

### 🎯 Category
**Games**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Loops (`for`/`while`)
- User Input

## 💻 Source Code
```python
"""
Project 020: Trivia Quiz Game
Category: Games
Description: A simple command-line trivia quiz.
"""

def run_project_20():
    print("=" * 45)
    print("        PYTHON PROJECT 020: TRIVIA QUIZ GAME")
    print("=" * 45)
    
    questions = [
        {"q": "What is the capital of France?", "a": "paris"},
        {"q": "Which planet is known as the Red Planet?", "a": "mars"},
        {"q": "What is 7 multiplied by 8?", "a": "56"}
    ]
    
    score = 0
    
    print("Welcome to the Trivia Quiz! Answer the following questions:\n")
    
    for i, item in enumerate(questions, 1):
        answer = input(f"Q{i}: {item['q']} \nYour answer: ").strip().lower()
        
        if answer == item['a']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {item['a'].title()}\n")
            
    print("=" * 30)
    print(f"Quiz Complete! You scored {score} out of {len(questions)}.")
    print("=" * 30)
    return True

if __name__ == "__main__":
    run_project_20()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 020_trivia_quiz_game.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Trivia Quiz Game in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
