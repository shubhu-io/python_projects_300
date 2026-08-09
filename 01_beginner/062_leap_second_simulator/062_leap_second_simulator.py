"""
Project 062: Leap Second Simulator
Category: Utilities
Description: Simulate adding a leap second to a digital clock.
"""
import time

def run_project_62():
    print("=" * 45)
    print("   PYTHON PROJECT 062: LEAP SECOND SIMULATOR")
    print("=" * 45)
    
    print("Simulating a countdown to a leap second (23:59:60).")
    
    try:
        for sec in range(55, 62):
            if sec == 60:
                timer = "23:59:60 [LEAP SECOND]"
            elif sec == 61:
                timer = "00:00:00"
            else:
                timer = f"23:59:{sec:02d}"
                
            print(f"\r{timer}", end="", flush=True)
            time.sleep(0.05)
            
        print("\n\nSimulation complete.")
        return True
    except KeyboardInterrupt:
        print("\nSimulation aborted.")
        return False

if __name__ == "__main__":
    run_project_62()
