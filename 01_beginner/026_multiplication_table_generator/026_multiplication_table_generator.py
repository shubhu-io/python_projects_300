"""
Project 026: Multiplication Table Generator
Category: Math & Logic
Description: Print multiplication table for a given number.
"""

def run_project_26():
    print("=" * 45)
    print("   PYTHON PROJECT 026: MULTIPLICATION TABLE")
    print("=" * 45)
    
    try:
        num = int(input("Enter a number to see its table: "))
        limit = int(input("Enter the limit (e.g., 10): "))
        
        print(f"\n--- Multiplication Table for {num} ---")
        for i in range(1, limit + 1):
            print(f"{num} x {i} = {num * i}")
            
        return True
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return False

if __name__ == "__main__":
    run_project_26()
