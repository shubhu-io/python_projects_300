"""
Project 061: Simple Shopping Cart
Category: CLI & Utilities
Description: A basic CLI shopping cart system.
"""

def run_project_61():
    print("=" * 45)
    print("      PYTHON PROJECT 061: SHOPPING CART")
    print("=" * 45)
    
    cart = {}
    
    while True:
        print("\n--- Cart Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart & Total")
        print("4. Checkout (Exit)")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            item = input("Item Name: ").strip().title()
            try:
                price = float(input("Price: $"))
                cart[item] = cart.get(item, 0) + price
                print(f"Added {item} for ${price:.2f}")
            except ValueError:
                print("Invalid price.")
        elif choice == '2':
            item = input("Item Name to remove: ").strip().title()
            if item in cart:
                del cart[item]
                print(f"Removed {item}")
            else:
                print("Item not found in cart.")
        elif choice == '3':
            if not cart:
                print("Cart is empty.")
            else:
                print("\n--- Current Cart ---")
                total = 0
                for item, price in cart.items():
                    print(f"{item}: ${price:.2f}")
                    total += price
                print(f"Total: ${total:.2f}")
        elif choice == '4':
            print("Checking out... Thank you for shopping!")
            break
        else:
            print("Invalid choice.")
            
    return True

if __name__ == "__main__":
    run_project_61()
