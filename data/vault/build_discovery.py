import os
import json
import shutil
from datetime import datetime

# Paths
REPO_ROOT = r'c:\Users\user\Documents\Software-Developer\Freelancer\aivery'
OUTPUT_ROOT = r'C:\Users\user\Documents\Software-Developer\Freelancer\avry-discovery'
GRAPH_DATA_PATH = os.path.join(REPO_ROOT, 'graphify-out', 'graph.json')
SCHEMA_PATH = os.path.join(REPO_ROOT, 'graphify-out', 'schema_info.json')

VAULT_DIR = os.path.join(OUTPUT_ROOT, 'data', 'vault')
DATA_DIR = os.path.join(OUTPUT_ROOT, 'data')

# Knowledge Base for fallback descriptions
KNOWLEDGE_BASE = {
    "auth": "User Authentication & Session Management. Handles login, JWT, and security guards.",
    "payments": "Billing & Subscription Engine. Integrates with payment gateways for user tier management.",
    "vps": "Infrastructure Bridge. Manages communication between the console and VPS instances.",
    "agents": "AI Agent Orchestration. Logic for defining and executing automated assistant tasks.",
    "blueprints": "System Configuration & Templates. Defines the structure of generated AI solutions.",
    "diagnostic": "User Readiness Assessment. Analyzes business inputs to generate AI adoption scores.",
    "console": "Primary Management Interface. The central hub for user interaction and monitoring.",
    "workflows": "Automation Pipeline Logic. Visual or code-based process definition and execution.",
    "database": "Persistent Storage Layer. Houses user data, logs, and system state."
}

def get_rationale_map(graph_data):
    rmap = {}
    for node in graph_data.get('nodes', []):
        if node.get('file_type') == 'rationale':
            file = node.get('source_file')
            if not file: continue
            if file not in rmap: rmap[file] = []
            rmap[file].append({
                'line': int(node.get('source_location', 'L0').replace('L', '')),
                'text': node.get('label', '')
            })
    return rmap

def inject_comments(file_path, rationales):
    if not os.path.exists(file_path): return ""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except: return ""

    sorted_rat = sorted(rationales, key=lambda x: x['line'], reverse=True)
    ext = os.path.splitext(file_path)[1]
    comment_sym = "#" if ext in ['.py', '.sh', '.yaml', '.yml'] else "//"
    
    for r in sorted_rat:
        idx = min(r['line'] - 1, len(lines))
        if idx < 0: idx = 0
        lines.insert(idx, f"\n{comment_sym} ARCHITECTURE INSIGHT: {r['text']}\n")
    return "".join(lines)

def build():
    print("Loading graph data...")
    with open(GRAPH_DATA_PATH, 'r') as f:
        graph_data = json.load(f)
    
    schema_info = {}
    if os.path.exists(SCHEMA_PATH):
        with open(SCHEMA_PATH, 'r') as f:
            schema_info = json.load(f)

    rationale_map = get_rationale_map(graph_data)
    processed_nodes = []
    tests_list = []
    reports_list = []
    
    print("Mirroring repository with AI injections...")
    for root, dirs, files in os.walk(REPO_ROOT):
        if any(x in root for x in ['node_modules', '.git', '__pycache__', 'graphify-out', 'avry-discovery']):
            continue
            
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, REPO_ROOT).replace('\\', '/')
            
            # 1. Vault
            rationales = rationale_map.get(rel_path, [])
            injected_code = inject_comments(full_path, rationales)
            vault_path = os.path.join(VAULT_DIR, rel_path)
            os.makedirs(os.path.dirname(vault_path), exist_ok=True)
            with open(vault_path, 'w', encoding='utf-8') as f:
                f.write(injected_code)

            # 2. Metadata
            if rel_path.startswith('tests/') or '__tests__' in rel_path:
                tests_list.append({
                    "name": rel_path,
                    "description": rationales[0]['text'] if rationales else "System test file.",
                    "result_path": f"results/{file}.log",
                    "timestamp": datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
                })
            
            # Categorization for Reports, VPS, Documentation
            lower_rel = rel_path.lower()
            if file.endswith('.md') or file.endswith('.txt'):
                doc_type = "Report"
                if "analysis" in lower_rel: doc_type = "Analysis"
                elif "vps" in lower_rel or "bridge" in lower_rel: doc_type = "VPS"
                elif "doc" in lower_rel or "readme" in lower_rel or "guide" in lower_rel: doc_type = "Documentation"
                
                reports_list.append({
                    "name": file,
                    "path": rel_path,
                    "type": doc_type
                })

    # 3. Enrich Graph
    for node in graph_data['nodes']:
        if node.get('file_type') == 'rationale': continue
        filePath = (node.get('source_file') or "").replace('\\', '/')
        if filePath.endswith('.html') or 'pages/' in filePath or '/app/' in filePath:
            if 'page.tsx' in filePath or '.html' in filePath:
                node['label'] = f"Page: {filePath}"
                node['category'] = 'Feature'
        
        node_rationales = rationale_map.get(filePath, [])
        if node_rationales:
            node['functionDesc'] = node_rationales[0]['text']
            node['detailedLogic'] = "\n".join([f"• {r['text']}" for r in node_rationales])
        else:
            for key, desc in KNOWLEDGE_BASE.items():
                if key in filePath.lower():
                    node['functionDesc'] = desc
                    break
        processed_nodes.append(node)

    # 4. Save
    with open(os.path.join(DATA_DIR, 'tests.json'), 'w') as f: json.dump(tests_list, f, indent=4)
    with open(os.path.join(DATA_DIR, 'reports.json'), 'w') as f: json.dump(reports_list, f, indent=4)
    with open(os.path.join(DATA_DIR, 'graph.json'), 'w') as f:
        json.dump({"nodes": processed_nodes, "links": graph_data['links']}, f, indent=4)
    print("Build complete!")

if __name__ == "__main__":
    build()
