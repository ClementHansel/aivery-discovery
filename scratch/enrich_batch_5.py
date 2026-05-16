import json
import os

# Batch 5 Enriched Data
BATCH_5 = {
    "app_config_py": {
        "functionDesc": "Centralized configuration management for Aivory backend services and LLM providers.",
        "detailedLogic": "Uses pydantic-settings for environment-based configuration. Implements typed settings for OpenRouter, n8n, and CORS policies. Includes proactive validation for high-tier API requirements.",
        "importance": "HIGH"
    },
    "package_json": {
        "functionDesc": "Project manifest and dependency manager for the Aivory multi-service ecosystem.",
        "detailedLogic": "Defines workspace scripts for parallel execution (Console + Backend). Manages the shared dependency tree and establishes the versioning baseline for the platform.",
        "importance": "HIGH"
    },
    "deploy_layered_system_sh": {
        "functionDesc": "Automated deployment orchestrator for the multi-layered Aivory architecture.",
        "detailedLogic": "Sequential service rollout (Gateway -> Backend -> Frontend). Handles environment injection and internal network aliasing to ensure cross-service connectivity.",
        "importance": "HIGH"
    },
    "updated_docker_compose_yml": {
        "functionDesc": "Container orchestration manifest for production-grade deployment and networking.",
        "detailedLogic": "Defines multi-container topology with persistent volume mapping and internal aliasing. Sets resource limits and restart policies for high-availability.",
        "importance": "HIGH"
    },
    "build_discovery_py": {
        "functionDesc": "Master build script for generating the AVRY Discovery Dashboard and injecting AI insights.",
        "detailedLogic": "Performs repository mirroring and injects AI-driven architectural logic as code comments. Optimizes static assets for portable deployment (Netlify/Vercel).",
        "importance": "HIGH"
    }
}

def enrich_graph():
    path = 'data/graph.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    nodes = data.get('nodes', [])
    updated_count = 0
    
    for node in nodes:
        node_id = node.get('id')
        if node_id in BATCH_5:
            updates = BATCH_5[node_id]
            node.update(updates)
            updated_count += 1
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully enriched {updated_count} nodes in Batch 5.")

if __name__ == "__main__":
    enrich_graph()
