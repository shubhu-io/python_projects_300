import json
import os

def generate_readme():
    json_path = 'projects_data.json'
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        projects = json.load(f)

    # Sort by ID
    projects.sort(key=lambda x: x['id'])

    beginner = [p for p in projects if 1 <= p['id'] <= 100]
    intermediate = [p for p in projects if 101 <= p['id'] <= 200]
    advanced = [p for p in projects if 201 <= p['id'] <= 300]

    def make_table(proj_list):
        lines = []
        lines.append("| # | Project Name | Category | Description |")
        lines.append("|---|--------------|----------|-------------|")
        for p in proj_list:
            pid = f"{p['id']:03d}"
            folder = p['folder'].replace('\\', '/')
            title = p['title'].replace('|', '\\|')
            category = p['category'].replace('|', '\\|')
            desc = p['description'].replace('|', '\\|')
            lines.append(f"| {pid} | [{title}]({folder}) | {category} | {desc} |")
        return "\n".join(lines)

    readme_content = f"""# 🚀 300 Python Projects

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
[![Ko-Fi](https://img.shields.io/badge/Support_Project-Ko--fi-F16061?style=flat&logo=ko-fi&logoColor=white)](https://ko-fi.com/T7W323SDIF)

Welcome to the ultimate collection of **300 Python Projects**! This repository is designed to take you from a complete beginner to an advanced Python developer through hands-on, practical coding exercises.

Every single project is self-contained in its own directory with a dedicated `README.md` explaining the concepts used and instructions on how to run it.

### 🌐 Interactive Web Explorer
Don't want to clone the repo just yet? You can explore all 300 projects directly in your browser!
👉 **[View the Live Explorer](https://shubhu-io.github.io/python_projects_300/)**

The web explorer allows you to:
- Filter projects by difficulty and category.
- Search for specific topics or keywords.
- View the complete Python source code with syntax highlighting without downloading anything.
- Copy code directly to your clipboard.

---

## 🛠️ How to Use This Repository

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubhu-io/python_projects_300.git
   cd python_projects_300
   ```
2. **Navigate to a project:**
   Pick a difficulty tier and navigate to a project folder that interests you.
   ```bash
   cd 01_beginner/001_hello_world_plus
   ```
3. **Read the Docs & Run the Code:**
   Open the `README.md` in that folder to understand the project. Then, run the Python file:
   ```bash
   python 001_hello_world_plus.py
   ```

---

## 📚 Complete Projects Index (300 Projects)

### 🟢 Beginner Projects (Projects 001 - 100)
Perfect for those just starting out with Python. These projects focus on core programming concepts such as variables, loops, conditionals, functions, basic I/O, and simple math/CLI logic.

{make_table(beginner)}

---

### 🟡 Intermediate Projects (Projects 101 - 200)
For developers ready to step up their game. These projects introduce object-oriented programming (OOP), external APIs, web scraping, data serialization (CSV/JSON), and simple GUIs.

{make_table(intermediate)}

---

### 🔴 Advanced Projects (Projects 201 - 300)
Complex, architecture-heavy projects designed for experienced developers. Covers concurrency (`asyncio`), machine learning, networking/sockets, advanced algorithms, and system design.

{make_table(advanced)}

---

## 🌟 Why This Repo?
Learning by doing is the best way to master a programming language. Whether you're looking for quick coding katas, inspiration for your portfolio, or deep technical challenges, you'll find something here.

Happy Coding! 🐍💻
"""

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print("README.md updated successfully with all 300 projects!")

if __name__ == "__main__":
    generate_readme()
