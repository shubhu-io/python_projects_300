"""
Project 082: Hexadecimal Converter
Category: Math & Logic
Description: Convert decimal to hex and vice-versa.
"""

def run_project_82():
    print("=" * 45)
    print("      PYTHON PROJECT 082: HEX CONVERTER")
    print("=" * 45)
    
    print("1. Decimal to Hex")
    print("2. Hex to Decimal")
    choice = input("Choice (1/2): ").strip()
    
    try:
        if choice == '1':
            dec = int(input("Enter decimal number: "))
            print(f"Hex: {hex(dec)}")
        elif choice == '2':
            hex_str = input("Enter hex string (e.g. 1A): ").strip()
            print(f"Decimal: {int(hex_str, 16)}")
        else:
            print("Invalid choice.")
            return False
            
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_82()
