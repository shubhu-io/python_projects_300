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
