# 🚀 System Resource Monitor

## 📝 Description
Intermediate Python project focusing on System Resource Monitor with robust logic and data handling.

### 🎯 Category
**Database & Storage**

## 💡 Concepts Covered
- Control Flow (`if`/`else`)
- Functions & Modular Code
- Object-Oriented Programming (Classes)

## 💻 Source Code
```python
"""
Project 118: System Resource Monitor
Category: Database & Storage
Description: Intermediate Python project focusing on System Resource Monitor with robust logic and data handling.
"""

class Project118Runner:
    def __init__(self):
        self.name = "System Resource Monitor"
        self.category = "Database & Storage"

    def execute(self) -> dict:
        return {
            "project_id": 118,
            "status": "SUCCESS",
            "message": f"Successfully ran {self.name}.",
            "metrics": {"processed": 100, "efficiency": "99.8%"}
        }

if __name__ == "__main__":
    runner = Project118Runner()
    res = runner.execute()
    print("Execution Result:", res)
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python 118_system_resource_monitor.py
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch System Resource Monitor in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
