import json
import os
import glob

projects_json_path = 'projects_data.json'

if not os.path.exists(projects_json_path):
    print("projects_data.json not found!")
    exit(1)

with open(projects_json_path, 'r', encoding='utf-8') as f:
    projects = json.load(f)

# Build a map of project_id -> py_file_path
py_file_map = {}

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.py') and not file.startswith('sync_') and not file.startswith('generate_') and not file.startswith('organize_'):
            prefix = file.split('_')[0]
            if prefix.isdigit():
                pid = int(prefix)
                py_file_map[pid] = os.path.join(root, file)

updated_count = 0
missing_count = 0

for proj in projects:
    pid = proj.get('id')
    if pid in py_file_map:
        py_path = py_file_map[pid]
        with open(py_path, 'r', encoding='utf-8') as py_file:
            real_code = py_file.read()
            proj['code'] = real_code
            proj['folder'] = os.path.dirname(py_path).replace('\\', '/')
            proj['filename'] = os.path.basename(py_path)
            updated_count += 1
    else:
        print(f"File not found for project ID: {pid}")
        missing_count += 1

with open(projects_json_path, 'w', encoding='utf-8') as f:
    json.dump(projects, f, indent=2)

print(f"Successfully updated {updated_count} projects with real Python code. Missing: {missing_count}")

