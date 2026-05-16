import json
import os

def fix_labels_and_categories():
    path = 'data/graph.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    nodes = data.get('nodes', [])
    updated_pages = 0
    updated_files = 0
    
    for node in nodes:
        label = node.get('label', '')
        source = node.get('source_file', '')
        category = node.get('category', '')
        
        # 1. Fix Page Labels (from page.tsx to /route)
        if category == 'Feature' and (label == 'page.tsx' or 'page.tsx' in source):
            # Extract route from source path
            # e.g. nextjs-console/app/console/page.tsx -> /console
            parts = source.split('/')
            if 'app' in parts:
                app_idx = parts.index('app')
                route_parts = parts[app_idx+1:-1]
                if not route_parts:
                    node['label'] = '/'
                else:
                    node['label'] = '/' + '/'.join(route_parts)
                updated_pages += 1
        
        # 2. Fix File Categories/Layers for coloring
        if category == 'File':
            if any(ext in source for ext in ['.tsx', '.html', '.css']):
                node['layer'] = 'FE'
            elif any(ext in source for ext in ['.py', '.sh', '.js', '.ts']):
                node['layer'] = 'BE'
            updated_files += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Updated {updated_pages} Page labels and {updated_files} File layers.")

if __name__ == "__main__":
    fix_labels_and_categories()
