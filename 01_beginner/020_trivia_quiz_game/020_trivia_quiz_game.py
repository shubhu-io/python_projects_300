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
