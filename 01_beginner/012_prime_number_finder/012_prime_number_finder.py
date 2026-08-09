"""
Project 012: Prime Number Finder
Category: Math & Logic
Description: Find prime numbers up to a specified limit.
"""

def run_project_12():
    print("=" * 45)
    print("     PYTHON PROJECT 012: PRIME NUMBER FINDER")
    print("=" * 45)
    
    try:
        limit = int(input("Enter a limit to find primes up to: "))
        
        if limit < 2:
            print("There are no prime numbers less than 2.")
            return False
            
        primes = []
        for num in range(2, limit + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
                
        print(f"\nPrime numbers up to {limit}:")
        print(", ".join(map(str, primes)))
        return True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return False

if __name__ == "__main__":
    run_project_12()
