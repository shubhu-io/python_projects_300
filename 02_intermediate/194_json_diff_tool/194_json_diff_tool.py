"""
Project 194: JSON Diff Tool
Category: Algorithms & DS
Description: JSON file storage manager with record indexing, searching, serialization, and deserialization.
"""
import json

class JSONStorageEngine194:
    def __init__(self):
        self.data = {}

    def add_item(self, key, value_dict):
        self.data[key] = value_dict
        return True

    def search(self, query):
        query = query.lower()
        results = {}
        for k, v in self.data.items():
            if query in k.lower() or any(query in str(val).lower() for val in v.values()):
                results[k] = v
        return results

    def to_json(self):
        return json.dumps(self.data, indent=2)

def run_project_194():
    print("=" * 45)
    print("   PYTHON PROJECT 194: JSON DIFF TOOL")
    print("=" * 45)
    
    storage = JSONStorageEngine194()
    storage.add_item("Alice Smith", {"email": "alice@example.com", "role": "Developer"})
    storage.add_item("Bob Jones", {"email": "bob@example.com", "role": "Designer"})
    
    print("\nStored JSON Document:")
    print(storage.to_json())
    
    print("\nSearching for 'Developer':")
    matches = storage.search("Developer")
    for k, v in matches.items():
        print(f"  Found: {k} -> {v}")
    return True

if __name__ == "__main__":
    run_project_194()
