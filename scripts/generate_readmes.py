import os
import glob
import ast

def analyze_ast(source_code):
    concepts = set()
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        return ["Syntax Error in file"]
        
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            concepts.add("Control Flow (`if`/`else`)")
        elif isinstance(node, (ast.For, ast.While)):
            concepts.add("Loops (`for`/`while`)")
        elif isinstance(node, ast.Try):
            concepts.add("Error Handling (`try`/`except`)")
        elif isinstance(node, ast.FunctionDef):
            concepts.add("Functions & Modular Code")
        elif isinstance(node, ast.ClassDef):
            concepts.add("Object-Oriented Programming (Classes)")
        elif isinstance(node, (ast.ListComp, ast.DictComp, ast.SetComp)):
            concepts.add("Comprehensions")
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == 'input':
                concepts.add("User Input")
        elif isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            concepts.add("Module Importing")
            
    if not concepts:
        concepts.add("Basic Syntax")
        
    return list(concepts)

def extract_docstring_info(source_code):
    try:
        tree = ast.parse(source_code)
        docstring = ast.get_docstring(tree)
    except Exception:
        docstring = None
        
    info = {
        "title": "Unknown Project",
        "category": "General",
        "description": "A Python project."
    }
    
    if docstring:
        lines = docstring.strip().split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith("Project"):
                info["title"] = line.split(":", 1)[-1].strip()
            elif line.startswith("Category:"):
                info["category"] = line.split(":", 1)[-1].strip()
            elif line.startswith("Description:"):
                info["description"] = line.split(":", 1)[-1].strip()
                
    return info

def generate_readme(py_file_path):
    with open(py_file_path, 'r', encoding='utf-8') as f:
        source_code = f.read()
        
    info = extract_docstring_info(source_code)
    concepts = analyze_ast(source_code)
    
    folder_path = os.path.dirname(py_file_path)
    file_name = os.path.basename(py_file_path)
    
    concepts_bullets = "\n".join(f"- {c}" for c in concepts)
    
    readme_content = f"""# 🚀 {info['title']}

## 📝 Description
{info['description']}

### 🎯 Category
**{info['category']}**

## 💡 Concepts Covered
{concepts_bullets}

## 💻 Source Code
```python
{source_code.strip()}
```

## 🏃‍♂️ How to Run

### Option 1: Run Locally
If you have Python installed on your computer, you can run this project directly from your terminal:
```bash
python {file_name}
```

### Option 2: Run in Browser
You don't need to install anything to try this out! You can execute this code directly in your browser using our Interactive Web Explorer.

👉 **[Launch {info['title']} in Web Explorer](https://shubhu-io.github.io/python_projects_300/)**
"""
    
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

def main():
    folders = ["01_beginner", "02_intermediate", "03_advanced"]
    count = 0
    for folder in folders:
        pattern = os.path.join(folder, "*", "*.py")
        py_files = glob.glob(pattern)
        for py_file in py_files:
            if os.path.basename(py_file).startswith("__"):
                continue
            generate_readme(py_file)
            count += 1
            
    print(f"Successfully generated {count} README.md files!")

if __name__ == "__main__":
    main()
