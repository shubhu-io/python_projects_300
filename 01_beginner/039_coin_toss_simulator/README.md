# 🚀 Coin Toss Simulator

## 📝 Description
Simulate tossing a coin multiple times.

### 🎯 Category
**Games & Random**

## 💡 Concepts Covered
- Loops (`for`/`while`)
- Control Flow (`if`/`else`)
- User Input
- Module Importing
- Functions & Modular Code
- Error Handling (`try`/`except`)

## 💻 Source Code
```python
"""
Project 039: Coin Toss Simulator
Category: Games & Random
Description: Simulate tossing a coin multiple times.
"""
import random

def run_project_39():
    print("=" * 45)
    print("      PYTHON PROJECT 039: COIN TOSS SIMULATOR")
    print("=" * 45)
    
    try:
        tosses = int(input("How many times to toss the coin? "))
        
        if tosses <= 0:
            print("Please enter a positive number.")
            return False
            
        heads = 0
        tails = 0
        
        for _ in range(tosses):
            if random.choice(['Heads', 'Tails']) == 'Heads':
                heads += 1
            else:
                tails += 1
                
        print(f"\n--- Results for {tosses} tosses ---")
        print(f"Heads: {heads} ({(heads/tosses)*100:.1f}%)")
        print(f"Tails: {tails} ({(tails/tosses)*100:.1f}%)")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_39()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 039_coin_toss_simulator.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Coin Toss Simulator in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
