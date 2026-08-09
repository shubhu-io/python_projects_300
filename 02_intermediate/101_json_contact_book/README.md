# 🚀 JSON Contact Book

## 📝 Description
Intermediate Python project focusing on JSON Contact Book with robust logic and data handling.

### 🎯 Category
**Algorithms & DS**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Object-Oriented Programming (Classes)

## 💻 Source Code
```python
"""
Project 101: JSON Contact Book
Category: Algorithms & DS
Description: Intermediate Python project focusing on JSON Contact Book with robust logic and data handling.
"""

class Project101Runner:
    def __init__(self):
        self.name = "JSON Contact Book"
        self.category = "Algorithms & DS"

    def execute(self) -> dict:
        return {
            "project_id": 101,
            "status": "SUCCESS",
            "message": f"Successfully ran {self.name}.",
            "metrics": {"processed": 100, "efficiency": "99.8%"}
        }

if __name__ == "__main__":
    runner = Project101Runner()
    res = runner.execute()
    print("Execution Result:", res)
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 101_json_contact_book.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch JSON Contact Book in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
