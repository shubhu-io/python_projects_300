# 🚀 Prime Number Finder

## 📝 Description
Find prime numbers up to a specified limit.

### 🎯 Category
**Math & Logic**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
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
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 012_prime_number_finder.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Prime Number Finder in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
