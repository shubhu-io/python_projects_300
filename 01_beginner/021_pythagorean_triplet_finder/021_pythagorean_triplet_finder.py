"""
Project 021: Pythagorean Triplet Finder
Category: Math & Logic
Description: Find Pythagorean triplets up to a given limit.
"""

def run_project_21():
    print("=" * 45)
    print("  PYTHON PROJECT 021: PYTHAGOREAN TRIPLETS")
    print("=" * 45)
    
    try:
        limit = int(input("Enter a limit for the hypotenuse: "))
        
        if limit < 5:
            print("Limit must be at least 5.")
            return False
            
        triplets = []
        for c in range(5, limit + 1):
            for b in range(4, c):
                for a in range(3, b):
                    if a*a + b*b == c*c:
                        triplets.append((a, b, c))
                        
        print(f"\nPythagorean triplets up to c={limit}:")
        for t in triplets:
            print(f"{t[0]}^2 + {t[1]}^2 = {t[2]}^2")
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_21()
