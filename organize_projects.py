import os
import re
import shutil

def extract_metadata(filepath):
    basename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(basename)[0]
    
    # Fallback default values
    project_title = name_without_ext.replace('_', ' ').title()
    description = "A Python project."
    concepts = set(["Variables"])
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract from docstring if present
    docstring_match = re.search(r'\"\"\"(.*?)\"\"\"', content, re.DOTALL)
    if docstring_match:
        doc = docstring_match.group(1)
        for line in doc.split('\n'):
            if line.strip().startswith('Project '):
                # e.g., "Project 001: Hello World Plus"
                parts = line.split(':', 1)
                if len(parts) > 1:
                    project_title = parts[1].strip()
            elif line.strip().startswith('Description:'):
                parts = line.split(':', 1)
                if len(parts) > 1:
                    description = parts[1].strip()
                    
    # Detect concepts
    if re.search(r'\binput\(', content) or re.search(r'\bprint\(', content):
        concepts.add("Input/Output")
    if re.search(r'\bif\b', content) or re.search(r'\belif\b', content):
        concepts.add("Conditions")
    if re.search(r'\bfor\b', content) or re.search(r'\bwhile\b', content):
        concepts.add("Loops")
    if re.search(r'\bdef\b', content):
        concepts.add("Functions")
    if re.search(r'\bclass\b', content):
        concepts.add("Classes/OOP")
    if re.search(r'\btry:\b', content):
        concepts.add("Error Handling")
    if re.search(r'\bimport\b', content):
        concepts.add("Modules/Libraries")
    if re.search(r'\bopen\(', content):
        concepts.add("File Handling")
    if re.search(r'\[.*?\]', content) and 'append(' in content:
        concepts.add("Lists/Arrays")
    if re.search(r'\{.*?\}', content):
        concepts.add("Dictionaries/Sets")
        
    return project_title, description, sorted(list(concepts))

def process_directory(base_dir):
    if not os.path.exists(base_dir):
        return
        
    for filename in os.listdir(base_dir):
        filepath = os.path.join(base_dir, filename)
        
        # Only process .py files in the root of the directory
        if os.path.isfile(filepath) and filename.endswith('.py'):
            name_without_ext = os.path.splitext(filename)[0]
            target_dir = os.path.join(base_dir, name_without_ext)
            
            # Create subdirectory
            os.makedirs(target_dir, exist_ok=True)
            
            # Extract metadata before moving
            title, desc, concepts = extract_metadata(filepath)
            
            # Move file
            new_filepath = os.path.join(target_dir, filename)
            shutil.move(filepath, new_filepath)
            
            # Write README.md
            readme_path = os.path.join(target_dir, 'README.md')
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write("## Description\n")
                f.write(f"{desc}\n\n")
                f.write("## Concepts Used\n")
                for concept in concepts:
                    f.write(f"- {concept}\n")
                f.write("\n## How to Run\n\n")
                f.write("```bash\n")
                f.write(f"python {filename}\n")
                f.write("```\n")
                
            print(f"Processed: {filename}")

if __name__ == "__main__":
    directories = [
        r"d:\Codeing\Ai generator\antigravity\python_projects_100\01_beginner",
        r"d:\Codeing\Ai generator\antigravity\python_projects_100\02_intermediate",
        r"d:\Codeing\Ai generator\antigravity\python_projects_100\03_advanced"
    ]
    
    for d in directories:
        print(f"\\nProcessing directory: {d}")
        process_directory(d)
    
    print("\\nAll done!")
