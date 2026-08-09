# 🚀 Simple Multiplication Quiz

## 📝 Description
Generate a few random multiplication questions.

### 🎯 Category
**Games & Math**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 096: Simple Multiplication Quiz
Category: Games & Math
Description: Generate a few random multiplication questions.
"""
import random

def run_project_96():
    print("=" * 45)
    print("    PYTHON PROJECT 096: MULTIPLICATION QUIZ")
    print("=" * 45)
    
    score = 0
    num_questions = 5
    
    print(f"Answer {num_questions} questions:\n")
    
    for i in range(1, num_questions + 1):
        n1 = random.randint(1, 12)
        n2 = random.randint(1, 12)
        ans = n1 * n2
        
        try:
            user_ans = int(input(f"Q{i}: What is {n1} x {n2}? "))
            if user_ans == ans:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong. The answer is {ans}.\n")
        except ValueError:
            print(f"Invalid input. The answer is {ans}.\n")
            
    print(f"Quiz over! Your score: {score}/{num_questions}")
    return True

if __name__ == "__main__":
    run_project_96()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 096_simple_multiplication_quiz.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Simple Multiplication Quiz in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
