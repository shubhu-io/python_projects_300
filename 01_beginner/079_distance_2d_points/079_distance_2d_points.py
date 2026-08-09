"""
Project 079: Distance 2D Points
Category: Math & Logic
Description: Calculate distance between two 2D points.
"""
import math

def run_project_79():
    print("=" * 45)
    print("      PYTHON PROJECT 079: 2D POINT DISTANCE")
    print("=" * 45)
    
    try:
        print("Point 1:")
        x1 = float(input("  x1: "))
        y1 = float(input("  y1: "))
        print("Point 2:")
        x2 = float(input("  x2: "))
        y2 = float(input("  y2: "))
        
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        print(f"\nThe distance between ({x1}, {y1}) and ({x2}, {y2}) is: {dist:.4f}")
        return True
    except ValueError:
        print("Invalid input.")
        return False

if __name__ == "__main__":
    run_project_79()
