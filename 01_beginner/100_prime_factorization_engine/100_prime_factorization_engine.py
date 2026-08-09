"""
Project 100: Prime Factorization Engine
Category: Math & Logic
Description: Find prime factors of a number.
"""

def run_project_100():
    print("=" * 45)
    print("    PYTHON PROJECT 100: PRIME FACTORIZATION")
    print("=" * 45)
    
    try:
        n = int(input("Enter an integer to factorize: "))
        
        if n < 2:
            print("Number must be greater than 1.")
            return False
            
        factors = []
        original = n
        
        # Divide by 2
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
            
        # Divide by odd numbers
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n = n // i
            i += 2
            
        # If n is a prime > 2
        if n > 2:
            factors.append(n)
            
        print(f"\nPrime factors of {original}:")
        print(" * ".join(map(str, factors)))
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_100()
