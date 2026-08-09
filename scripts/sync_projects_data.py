import json
import os
import ast
import re

projects_json_path = 'projects_data.json'

if not os.path.exists(projects_json_path):
    print("projects_data.json not found!")
    exit(1)

with open(projects_json_path, 'r', encoding='utf-8') as f:
    projects = json.load(f)

# Build a map of project_id -> py_file_path
py_file_map = {}

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.py') and not file.startswith('sync_') and not file.startswith('generate_') and not file.startswith('organize_'):
            prefix = file.split('_')[0]
            if prefix.isdigit():
                pid = int(prefix)
                py_file_map[pid] = os.path.join(root, file)

# Selected featured project IDs (diverse, high quality)
FEATURED_IDS = {1, 2, 3, 6, 10, 27, 34, 101, 105, 114, 201, 214}

# Libraries that cannot run in Pyodide or have limited support
DESKTOP_ONLY_MODULES = {'tkinter', 'pygame', 'cv2', 'PIL', 'matplotlib', 'seaborn', 'scipy', 'sklearn', 'torch', 'tensorflow', 'wx', 'PyQt5', 'PyQt6', 'PySide2', 'PySide6'}
LIMITED_MODULES = {'subprocess', 'socket', 'urllib', 'requests', 'asyncio', 'threading', 'multiprocessing'}

def clean_prompt(prompt_str):
    if not prompt_str:
        return "Enter input:"
    # Unescape common escaped characters and strip trailing newlines/tabs
    s = prompt_str.encode().decode('unicode-escape') if '\\' in prompt_str else prompt_str
    s = s.replace('\r\n', ' ').replace('\n', ' ').replace('\t', ' ').strip()
    return s if s else "Enter input:"

def analyze_python_code(source_code):
    prompts = []
    imports = set()
    
    try:
        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
            elif isinstance(node, ast.Call):
                # Check for input() call
                if isinstance(node.func, ast.Name) and node.func.id == 'input':
                    prompt_val = ""
                    if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                        prompt_val = node.args[0].value
                    elif node.args and isinstance(node.args[0], ast.Str): # Python <3.8 compat
                        prompt_val = node.args[0].s
                    prompts.append(clean_prompt(prompt_val))
    except Exception as e:
        # Fallback to regex if AST fails
        input_matches = re.findall(r'input\s*\(\s*(?:([\'"])(.*?)\1)?\s*\)', source_code)
        for m in input_matches:
            prompts.append(clean_prompt(m[1]))

    # Determine browser compatibility
    if imports.intersection(DESKTOP_ONLY_MODULES):
        compat = "terminal_only"
    elif imports.intersection(LIMITED_MODULES):
        compat = "limited"
    else:
        compat = "compatible"

    return {
        "requiresInput": len(prompts) > 0,
        "inputCount": len(prompts),
        "inputPrompts": prompts,
        "browserCompatibility": compat,
        "imports": list(imports)
    }

updated_count = 0
missing_count = 0

for proj in projects:
    pid = proj.get('id')
    if pid in py_file_map:
        py_path = py_file_map[pid]
        rel_folder = os.path.dirname(py_path).replace('\\', '/').lstrip('./')
        filename = os.path.basename(py_path)
        
        with open(py_path, 'r', encoding='utf-8') as py_file:
            real_code = py_file.read()
            
        analysis = analyze_python_code(real_code)
        
        proj['code'] = real_code
        proj['folder'] = rel_folder
        proj['filename'] = filename
        proj['requiresInput'] = analysis['requiresInput']
        proj['inputCount'] = analysis['inputCount']
        proj['inputPrompts'] = analysis['inputPrompts']
        proj['browserCompatibility'] = analysis['browserCompatibility']
        proj['featured'] = pid in FEATURED_IDS
        
        # Paths
        proj['githubUrl'] = f"https://github.com/shubhu-io/python_projects_300/blob/main/{rel_folder}/{filename}"
        
        readme_path = os.path.join(os.path.dirname(py_path), 'README.md')
        if os.path.exists(readme_path):
            proj['readmeUrl'] = f"https://github.com/shubhu-io/python_projects_300/blob/main/{rel_folder}/README.md"
        else:
            proj['readmeUrl'] = None

        updated_count += 1
    else:
        print(f"File not found for project ID: {pid}")
        missing_count += 1

with open(projects_json_path, 'w', encoding='utf-8') as f:
    json.dump(projects, f, indent=2)

print(f"Successfully processed {updated_count} projects with AST analysis. Missing: {missing_count}")
