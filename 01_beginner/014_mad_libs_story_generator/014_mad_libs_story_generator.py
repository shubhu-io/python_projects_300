"""
Project 014: Mad Libs Story Generator
Category: Text & Strings
Description: Fills placeholders in stories with custom user words.
"""

def run_project_14():
    print("=" * 45)
    print("    PYTHON PROJECT 014: MAD LIBS GENERATOR")
    print("=" * 45)
    
    print("Please provide the following words:")
    noun1 = input("A noun: ").strip()
    adjective = input("An adjective: ").strip()
    verb = input("A past-tense verb: ").strip()
    place = input("A place: ").strip()
    noun2 = input("Another noun: ").strip()
    
    story = f"""
    One day, a {adjective} {noun1} went to the {place}.
    While there, it {verb} a completely normal {noun2}.
    Everyone was very surprised!
    """
    
    print("\nHere is your Mad Libs Story:")
    print("-" * 30)
    print(story.strip())
    print("-" * 30)
    return True

if __name__ == "__main__":
    run_project_14()
