# 🚀 Currency Converter (Static)

## 📝 Description
Converts between currencies using static hardcoded rates.

### 🎯 Category
**Utilities**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Error Handling (`try`/`except`)
- User Input

## 💻 Source Code
```python
"""
Project 016: Currency Converter (Static)
Category: Utilities
Description: Converts between currencies using static hardcoded rates.
"""

def run_project_16():
    print("=" * 45)
    print("  PYTHON PROJECT 016: STATIC CURRENCY CONVERTER")
    print("=" * 45)
    
    # Static exchange rates relative to 1 USD
    rates = {
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'JPY': 150.2,
        'INR': 83.0
    }
    
    print("Available currencies: USD, EUR, GBP, JPY, INR")
    base = input("Enter base currency: ").strip().upper()
    target = input("Enter target currency: ").strip().upper()
    
    if base not in rates or target not in rates:
        print("Unsupported currency selected.")
        return False
        
    try:
        amount = float(input(f"Enter amount in {base}: "))
        
        # Convert to USD first, then to target
        amount_in_usd = amount / rates[base]
        converted = amount_in_usd * rates[target]
        
        print(f"\n{amount:.2f} {base} = {converted:.2f} {target}")
        return True
    except ValueError:
        print("Invalid amount.")
        return False

if __name__ == "__main__":
    run_project_16()
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 016_currency_converter_static.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch Currency Converter (Static) in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
