"""
Project 081: Binary to Decimal Converter
Category: Math & Logic
Description: Convert binary string to decimal integer.
"""

def run_project_81():
    print("=" * 45)
    print("   PYTHON PROJECT 081: BINARY CONVERTER")
    print("=" * 45)
    
    binary_str = input("Enter a binary number: ").strip()
    
    if not all(c in '01' for c in binary_str):
        print("Invalid binary number.")
        return False
        
    decimal = int(binary_str, 2)
    print(f"\nBinary: {binary_str}")
    print(f"Decimal: {decimal}")
    
    return True

if __name__ == "__main__":
    run_project_81()
