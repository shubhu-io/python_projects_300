"""
Project 077: Simple High Score Tracker
Category: Games & CLI
Description: Maintain a list of top 3 scores.
"""

def run_project_77():
    print("=" * 45)
    print("     PYTHON PROJECT 077: HIGH SCORE TRACKER")
    print("=" * 45)
    
    scores = []
    
    while True:
        try:
            val = input("Enter a score (or 'q' to quit): ").strip()
            if val.lower() == 'q':
                break
                
            score = int(val)
            scores.append(score)
            scores.sort(reverse=True)
            
            # Keep top 3
            if len(scores) > 3:
                scores = scores[:3]
                
            print("\nTop 3 Scores:")
            for i, s in enumerate(scores, 1):
                print(f"{i}. {s}")
            print("-" * 20)
            
        except ValueError:
            print("Invalid score.")
            
    print("Tracker closed.")
    return True

if __name__ == "__main__":
    run_project_77()
