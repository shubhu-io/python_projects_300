"""
Project 089: Simple Discount Calculator
Category: Finance & Math
Description: Calculate final price after a percentage discount.
"""

def run_project_89():
    print("=" * 45)
    print("    PYTHON PROJECT 089: DISCOUNT CALCULATOR")
    print("=" * 45)
    
    try:
        price = float(input("Enter original price: $"))
        discount = float(input("Enter discount percentage (e.g., 20): "))
        
        if price < 0 or discount < 0 or discount > 100:
            print("Invalid inputs.")
            return False
            
        savings = price * (discount / 100)
        final_price = price - savings
        
        print(f"\nOriginal Price: ${price:.2f}")
        print(f"Discount: {discount}%")
        print(f"You Save: ${savings:.2f}")
        print(f"Final Price: ${final_price:.2f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_89()
