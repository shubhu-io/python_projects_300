"""
Project 011: Fibonacci Sequence Generator
Category: Math & Logic
Description: Generates the Fibonacci sequence up to a given number of terms.
"""

def run_project_11():
    print("=" * 45)
    print("   PYTHON PROJECT 011: FIBONACCI GENERATOR")
    print("=" * 45)
    
    try:
        terms = int(input("Enter the number of terms to generate: "))
        
        if terms <= 0:
            print("Please enter a positive integer.")
            return False
            
        a, b = 0, 1
        sequence = []
        
        for _ in range(terms):
            sequence.append(a)
            a, b = b, a + b
            
        print(f"\nFibonacci Sequence ({terms} terms):")
        print(", ".join(map(str, sequence)))
        return True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return False

if __name__ == "__main__":
    run_project_11()
