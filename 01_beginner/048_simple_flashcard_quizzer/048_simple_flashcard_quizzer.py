"""
Project 048: Simple Flashcard Quizzer
Category: Utilities & Games
Description: A basic CLI flashcard tool.
"""
import random

def run_project_48():
    print("=" * 45)
    print("     PYTHON PROJECT 048: FLASHCARD QUIZZER")
    print("=" * 45)
    
    flashcards = {
        "Python": "A high-level programming language.",
        "HTML": "Standard markup language for documents designed to be displayed in a web browser.",
        "CSS": "Style sheet language used for describing the presentation of a document.",
        "API": "Application Programming Interface."
    }
    
    keys = list(flashcards.keys())
    random.shuffle(keys)
    
    score = 0
    for key in keys:
        print(f"\nTerm: {key}")
        input("Press Enter to reveal the definition...")
        print(f"Definition: {flashcards[key]}")
        correct = input("Did you get it right? (y/n): ").strip().lower()
        if correct == 'y':
            score += 1
            
    print(f"\nQuiz complete. Score: {score}/{len(flashcards)}")
    return True

if __name__ == "__main__":
    run_project_48()
