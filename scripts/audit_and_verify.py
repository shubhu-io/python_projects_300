import os
import glob
import sys
import subprocess
import json
from concurrent.futures import ThreadPoolExecutor

py_files = sorted(glob.glob('./**/*.py', recursive=True))

projects = {}

for py_path in py_files:
    fname = os.path.basename(py_path)
    if fname.startswith('sync_') or fname.startswith('generate_') or fname.startswith('organize_') or fname.startswith('audit_'):
        continue
    
    prefix = fname.split('_')[0]
    if prefix.isdigit():
        pid = int(prefix)
    else:
        continue
        
    folder = os.path.dirname(py_path).replace('\\', '/')
    
    if pid not in projects:
        projects[pid] = {
            'pid': pid,
            'folder': folder,
            'files': []
        }
    projects[pid]['files'].append(py_path)

canned_input = "1\n1\n1\n1\n1\n2\n3\n4\n5\n9\nq\nquit\nexit\n0\n"

def test_file(file_path):
    cmd = [sys.executable, file_path]
    try:
        proc = subprocess.run(
            cmd,
            input=canned_input,
            capture_output=True,
            text=True,
            timeout=4
        )
        if proc.returncode == 0:
            return {'file': file_path, 'status': 'PASS', 'output': proc.stdout[:150]}
        else:
            return {'file': file_path, 'status': 'FAIL', 'returncode': proc.returncode, 'error': proc.stderr[:300]}
    except subprocess.TimeoutExpired:
        return {'file': file_path, 'status': 'TIMEOUT', 'error': 'Execution exceeded 4s timeout'}
    except Exception as e:
        return {'file': file_path, 'status': 'ERROR', 'error': str(e)}

print(f"Discovered {len(projects)} projects containing {sum(len(p['files']) for p in projects.values())} Python files.")

results = {}
with ThreadPoolExecutor(max_workers=15) as executor:
    file_futures = {executor.submit(test_file, f): f for p in projects.values() for f in p['files']}
    for future in file_futures:
        res = future.result()
        results[res['file']] = res

# Aggregate by project
project_summary = []
passed_projects = 0
failed_projects = 0

for pid in sorted(projects.keys()):
    pdata = projects[pid]
    p_files = pdata['files']
    file_results = [results[f] for f in p_files]
    
    pass_cnt = sum(1 for r in file_results if r['status'] == 'PASS')
    fail_cnt = sum(1 for r in file_results if r['status'] in ['FAIL', 'TIMEOUT', 'ERROR'])
    
    status = 'VERIFIED' if fail_cnt == 0 else 'NEEDS FIX'
    if status == 'VERIFIED':
        passed_projects += 1
    else:
        failed_projects += 1
        
    project_summary.append({
        'pid': pid,
        'folder': pdata['folder'],
        'total_files': len(p_files),
        'passed': pass_cnt,
        'failed': fail_cnt,
        'status': status,
        'details': file_results
    })

report = {
    'total_projects': len(projects),
    'verified_projects': passed_projects,
    'failed_projects': failed_projects,
    'total_files': len(results),
    'files_passed': sum(1 for r in results.values() if r['status'] == 'PASS'),
    'files_failed': sum(1 for r in results.values() if r['status'] != 'PASS'),
    'projects': project_summary
}

with open('verification_audit.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)

print("\n========================================")
print("AUDIT SUMMARY FOR ALL 300 PROJECTS")
print("========================================")
print(f"Total Projects: {len(projects)}")
print(f"Verified Projects: {passed_projects}")
print(f"Projects Needing Fix: {failed_projects}")
print(f"Total Python Files: {len(results)}")
print(f"Files Passed: {report['files_passed']}")
print(f"Files Failed: {report['files_failed']}")
