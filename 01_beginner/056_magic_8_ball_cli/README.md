# 🚀 Magic 8 Ball CLI

## 📝 Description
A virtual Magic 8 Ball.

### 🎯 Category
**Games & Random**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Module Importing
- User Input

## 💻 Source Code
```python
"""
Project 056: Magic 8 Ball CLI
Category: Games & Random
Description: A virtual Magic 8 Ball.
"""
import random

def run_project_56():
    print("=" * 45)
    print("       PYTHON PROJECT 056: MAGIC 8 BALL")
    print("=" * 45)
    
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.",
        "Don't count on it.", "My reply is no.", "My sources say no.",
        "Outlook not so good.", "Very doubtful."
    ]
    
    input("Ask the Magic 8 Ball a yes/no question: ")
    print(f"\nMagic 8 Ball says: {random.choice(responses)}")
    return True

if __name__ == "__main__":
    run_project_56()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 056_magic_8_ball_cli.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Magic 8 Ball CLI in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
