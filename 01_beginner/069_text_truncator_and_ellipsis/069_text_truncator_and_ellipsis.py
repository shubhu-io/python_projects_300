"""
Project 069: Text Truncator and Ellipsis
Category: Text & Strings
Description: Truncate a long string and add '...' at the end.
"""

def run_project_69():
    print("=" * 45)
    print("       PYTHON PROJECT 069: TEXT TRUNCATOR")
    print("=" * 45)
    
    text = input("Enter a long sentence: ")
    try:
        limit = int(input("Enter max length: "))
        
        if len(text) > limit:
            # truncate and add ellipsis
            # Make sure we don't end up longer than limit
            shortened = text[:limit-3] + "..." if limit > 3 else text[:limit]
            print(f"\nTruncated: {shortened}")
        else:
            print(f"\nText fits within limit: {text}")
            
        return True
    except ValueError:
        print("Invalid length.")
        return False

if __name__ == "__main__":
    run_project_69()
